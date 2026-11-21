#!/usr/bin/env python3
"""Google Search Console client for the scholarly paper pages of l3ragio.github.io.

Read-only by default. The only write operation is a sitemap submission, and it
needs `sitemaps submit --confirm`. There is no delete command.

Secrets live outside the repository, in GSC_SECRETS_DIR
(default: %USERPROFILE%\\.secrets\\gsc):
  client_secret.json   OAuth client of type "Desktop app" (installed flow)
  token.dpapi          authorised credentials, encrypted with Windows DPAPI
                       (current user); never printed, never in the repository
  raw/                 raw API responses of each audit, for reproducibility

Commands:
  auth login            installed-app flow: opens the Google consent page in the
                        browser, loopback redirect on 127.0.0.1, PKCE
  auth status [--refresh]
  auth logout           deletes the local token (revoke the grant itself at
                        https://myaccount.google.com/permissions)
  properties
  sitemaps status
  sitemaps submit --confirm
  inspect papers
  performance papers [--days N]
  audit --all [--write]  everything above (read-only); --write updates
                         docs/papers/gsc_status.json and GSC_STATUS.md
  doctor

Run with the dedicated environment, which has the Google libraries:
  C:/Users/Davide/.venvs/l3ragio-gsc/Scripts/python.exe scripts/gsc_client.py audit --all --write
"""

from __future__ import annotations

import argparse
import ctypes
import json
import os
import random
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INVENTORY = ROOT / "docs" / "papers" / "zenodo_inventory.json"
STATUS_JSON = ROOT / "docs" / "papers" / "gsc_status.json"
STATUS_MD = ROOT / "docs" / "papers" / "GSC_STATUS.md"

PROPERTY = "https://l3ragio.github.io/"
ALLOWED_PROPERTIES = frozenset({PROPERTY})
SITEMAP = PROPERTY + "sitemap.xml"
SCOPES = ["https://www.googleapis.com/auth/webmasters"]
SM_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
TRANSIENT = {429, 500, 502, 503, 504}
HTTP_TIMEOUT = 60


class GscError(Exception):
    """A diagnosed failure; the message is already redacted."""


class AuthError(GscError):
    pass


# --------------------------------------------------------------------------- redaction

_SECRET_PATTERNS = [
    re.compile(r"ya29\.[0-9A-Za-z_\-\.]+"),              # access tokens
    re.compile(r"1//[0-9A-Za-z_\-]{10,}"),              # refresh tokens
    re.compile(r"GOCSPX-[0-9A-Za-z_\-]+"),              # client secrets
    re.compile(r"4/[0-9A-Za-z_\-]{10,}"),               # authorization codes
    re.compile(r'("(?:access_token|refresh_token|client_secret|id_token|code)"\s*:\s*")[^"]*(")'),
    re.compile(r"((?:access_token|refresh_token|client_secret|code)=)[^&\s]+"),
]


def redact(text: object) -> str:
    s = str(text)
    for p in _SECRET_PATTERNS:
        s = p.sub(lambda m: (m.group(1) + "[REDACTED]" + m.group(2)) if m.re.groups == 2
                  else (m.group(1) + "[REDACTED]") if m.re.groups == 1 else "[REDACTED]", s)
    return s


# --------------------------------------------------------------------------- secret storage

def secrets_dir() -> Path:
    return Path(os.environ.get("GSC_SECRETS_DIR", Path.home() / ".secrets" / "gsc"))


def _inside_repo(p: Path) -> bool:
    try:
        p.resolve().relative_to(ROOT.resolve())
        return True
    except ValueError:
        return False


class _Blob(ctypes.Structure):
    _fields_ = [("cbData", ctypes.c_uint32), ("pbData", ctypes.POINTER(ctypes.c_char))]


def _dpapi(data: bytes, protect: bool) -> bytes:
    crypt32, kernel32 = ctypes.windll.crypt32, ctypes.windll.kernel32  # type: ignore[attr-defined]
    buf = ctypes.create_string_buffer(data, len(data))
    src, out = _Blob(len(data), buf), _Blob()
    fn = crypt32.CryptProtectData if protect else crypt32.CryptUnprotectData
    ok = (fn(ctypes.byref(src), "l3ragio-gsc" if protect else None, None, None, None, 0x1, ctypes.byref(out))
          if protect else fn(ctypes.byref(src), None, None, None, None, 0x1, ctypes.byref(out)))
    if not ok:
        raise AuthError(f"DPAPI {'encryption' if protect else 'decryption'} failed "
                        f"(Windows error {ctypes.GetLastError()}); run `auth login` again")
    try:
        return ctypes.string_at(out.pbData, out.cbData)
    finally:
        kernel32.LocalFree(out.pbData)


class TokenStore:
    """Credentials JSON encrypted with DPAPI (Windows, current user).

    Elsewhere it falls back to a 0600 plaintext file and says so in `doctor`.
    """

    def __init__(self, directory: Path | None = None) -> None:
        self.dir = directory or secrets_dir()
        self.dpapi = os.name == "nt"
        self.path = self.dir / ("token.dpapi" if self.dpapi else "token.json")
        if _inside_repo(self.dir):
            raise GscError("refusing to keep secrets inside the repository: set GSC_SECRETS_DIR elsewhere")

    def exists(self) -> bool:
        return self.path.exists()

    def load(self) -> dict:
        raw = self.path.read_bytes()
        if self.dpapi:
            raw = _dpapi(raw, protect=False)
        return json.loads(raw.decode("utf-8"))

    def save(self, info: dict) -> None:
        self.dir.mkdir(parents=True, exist_ok=True)
        data = json.dumps(info).encode("utf-8")
        if self.dpapi:
            data = _dpapi(data, protect=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_bytes(data)
        if not self.dpapi:
            os.chmod(tmp, 0o600)
        os.replace(tmp, self.path)

    def delete(self) -> bool:
        if self.path.exists():
            self.path.unlink()
            return True
        return False


# --------------------------------------------------------------------------- client file

def check_client_file(path: Path) -> dict:
    """Validate the OAuth client JSON without returning or printing any value of it."""
    if not path.exists():
        raise AuthError(f"OAuth client file not found: {path}")
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise AuthError(f"OAuth client file is not valid JSON: {type(e).__name__}") from None
    if "installed" not in d:
        kind = next(iter(d), "none")
        raise AuthError(f"OAuth client type is '{kind}', expected 'installed' (Desktop app)")
    c = d["installed"]
    missing = [k for k in ("client_id", "client_secret", "auth_uri", "token_uri") if not c.get(k)]
    if missing:
        raise AuthError(f"OAuth client file lacks: {', '.join(missing)}")
    return {
        "type": "installed",
        "client_id_format_ok": c["client_id"].endswith(".apps.googleusercontent.com"),
        "project_id_present": bool(c.get("project_id")),
        "loopback_redirect": any(u.startswith("http://localhost") or u.startswith("http://127.0.0.1")
                                 for u in c.get("redirect_uris", [])),
    }


# --------------------------------------------------------------------------- credentials

def _creds_from_info(info: dict):
    from google.oauth2.credentials import Credentials
    return Credentials.from_authorized_user_info(info, SCOPES)


def get_credentials(store: TokenStore | None = None, force_refresh: bool = False):
    """Load the stored credentials and refresh the access token when needed."""
    from google.auth.exceptions import RefreshError
    from google.auth.transport.requests import Request

    store = store or TokenStore()
    if not store.exists():
        raise AuthError("not logged in: run `auth login`")
    info = store.load()
    creds = _creds_from_info(info)
    if force_refresh or not creds.valid:
        if not creds.refresh_token:
            raise AuthError("stored credentials have no refresh token: run `auth login`")
        try:
            creds.refresh(Request())
        except RefreshError as e:
            msg = redact(e)
            if "invalid_grant" in msg:
                raise AuthError("refresh token rejected (invalid_grant): it was revoked or expired. "
                                "An OAuth app in Testing status issues refresh tokens that expire after "
                                "7 days. Run `auth login` again.") from None
            raise AuthError(f"token refresh failed: {msg}") from None
        new = json.loads(creds.to_json())
        new.setdefault("refresh_token", info.get("refresh_token"))
        store.save(new)
    return creds


def login(client_file: Path, store: TokenStore, login_hint: str | None = None) -> dict:
    from google_auth_oauthlib.flow import InstalledAppFlow

    check_client_file(client_file)
    flow = InstalledAppFlow.from_client_secrets_file(str(client_file), SCOPES, autogenerate_code_verifier=True)
    url_file = store.dir / "last_consent_url.txt"
    store.dir.mkdir(parents=True, exist_ok=True)
    print("Opening the Google consent page in your browser (loopback 127.0.0.1, PKCE).")
    print(f"If it does not open, the URL is in {url_file}")

    orig = flow.authorization_url

    def _authorization_url(**kw):
        url, state = orig(**kw)
        url_file.write_text(url, encoding="utf-8")
        return url, state

    flow.authorization_url = _authorization_url  # type: ignore[method-assign]
    creds = flow.run_local_server(host="localhost", bind_addr="127.0.0.1", port=0, open_browser=True,
                                  authorization_prompt_message="", success_message=(
                                      "Authorisation complete. You can close this tab."),
                                  timeout_seconds=900, access_type="offline", prompt="consent",
                                  **({"login_hint": login_hint} if login_hint else {}))
    url_file.unlink(missing_ok=True)
    info = json.loads(creds.to_json())
    store.save(info)
    granted = sorted(getattr(creds, "granted_scopes", None) or info.get("scopes") or [])
    return {"refresh_token": bool(creds.refresh_token), "granted_scopes": granted,
            "required_scopes_granted": set(SCOPES) <= set(granted) if granted else None}


# --------------------------------------------------------------------------- API access

def service(creds):
    import google_auth_httplib2
    import httplib2
    from googleapiclient.discovery import build

    http = google_auth_httplib2.AuthorizedHttp(creds, http=httplib2.Http(timeout=HTTP_TIMEOUT))
    return build("searchconsole", "v1", http=http, cache_discovery=False)


def call(request, *, attempts: int = 5, base_delay: float = 1.0, sleep=time.sleep):
    """Execute a googleapiclient request with exponential backoff on transient errors."""
    from googleapiclient.errors import HttpError

    for i in range(attempts):
        try:
            return request.execute()
        except HttpError as e:
            status = getattr(e.resp, "status", 0)
            if status in TRANSIENT and i < attempts - 1:
                sleep(base_delay * 2 ** i + random.uniform(0, base_delay))
                continue
            raise GscError(describe_http_error(e)) from None
        except (TimeoutError, OSError) as e:
            if i < attempts - 1:
                sleep(base_delay * 2 ** i)
                continue
            raise GscError(f"network error: {type(e).__name__}: {redact(e)}") from None
    raise GscError("unreachable")


def describe_http_error(e) -> str:
    status = getattr(e.resp, "status", "?")
    try:
        body = json.loads(e.content.decode("utf-8"))["error"]
        reason = (body.get("errors") or [{}])[0].get("reason") or body.get("status", "")
        msg = body.get("message", "")
    except Exception:  # noqa: BLE001
        reason, msg = "", str(e)
    hint = {
        403: "the account lacks access to this property, or the API is not enabled in the client's project",
        401: "credentials rejected: run `auth login`",
        429: "quota exhausted: URL Inspection allows 2000 calls per day and 600 per minute per property",
        404: "not found",
    }.get(status if isinstance(status, int) else 0, "")
    return redact(f"HTTP {status} {reason}: {msg}" + (f" ({hint})" if hint else ""))


def require_allowed(site: str) -> str:
    if site not in ALLOWED_PROPERTIES:
        raise GscError(f"property not in the allowlist: {site}")
    return site


def list_properties(svc) -> list[dict]:
    return call(svc.sites().list()).get("siteEntry", [])


def sitemap_status(svc) -> dict:
    site = require_allowed(PROPERTY)
    listed = call(svc.sitemaps().list(siteUrl=site)).get("sitemap", [])
    try:
        record = call(svc.sitemaps().get(siteUrl=site, feedpath=SITEMAP))
    except GscError as e:
        record = {"_error": str(e)}
    return {"listed": listed, "record": record}


def submit_sitemap(svc) -> None:
    call(svc.sitemaps().submit(siteUrl=require_allowed(PROPERTY), feedpath=SITEMAP))


def classify_sitemap(record: dict, http_ok: bool, xml_ok: bool) -> str:
    """A-G classification of the sitemap incident."""
    if not http_ok:
        return "A_HTTP_RETRIEVAL_FAILURE"
    if not xml_ok:
        return "B_XML_VALIDATION_ERROR"
    if not record or "_error" in record:
        return "G_INSUFFICIENT_INFORMATION"
    errors = int(record.get("errors", 0) or 0)
    if record.get("lastDownloaded"):
        return "E_PROCESSED_WITH_ERRORS" if errors else "F_SUCCESSFULLY_PROCESSED"
    if record.get("isPending"):
        return "D_SUBMITTED_NOT_YET_PROCESSED"
    return "G_INSUFFICIENT_INFORMATION"


def inspect_url(svc, url: str) -> dict:
    site = require_allowed(PROPERTY)
    if not url.startswith(site):
        raise GscError(f"URL outside the allowed property: {url}")
    body = {"inspectionUrl": url, "siteUrl": site, "languageCode": "en-US"}
    return call(svc.urlInspection().index().inspect(body=body)).get("inspectionResult", {})


INSPECT_FIELDS = ["verdict", "coverageState", "indexingState", "pageFetchState", "robotsTxtState",
                  "lastCrawlTime", "googleCanonical", "userCanonical", "sitemap", "referringUrls", "crawledAs"]


def summarize_inspection(result: dict) -> dict:
    idx = result.get("indexStatusResult", {}) or {}
    out = {k: idx[k] for k in INSPECT_FIELDS if k in idx}
    if result.get("inspectionResultLink"):
        out["inspectionResultLink"] = result["inspectionResultLink"]
    out["state"] = classify_inspection(idx)
    return out


def classify_inspection(idx: dict) -> str:
    cov = (idx.get("coverageState") or "").lower()
    verdict = idx.get("verdict", "")
    if idx.get("robotsTxtState") == "DISALLOWED" or idx.get("indexingState", "").startswith("BLOCKED"):
        return "blocked_or_inaccessible"
    if verdict == "PASS" or ("indexed" in cov and "not indexed" not in cov):
        gc, uc = idx.get("googleCanonical"), idx.get("userCanonical")
        return "indexed_other_canonical" if gc and uc and gc != uc else "indexed"
    if "unknown to google" in cov:
        return "unknown_to_google"
    if "discovered" in cov:
        return "discovered_not_crawled"
    if "crawled" in cov:
        return "crawled_not_indexed"
    fetch = idx.get("pageFetchState")
    if fetch and fetch not in ("SUCCESSFUL", "PAGE_FETCH_STATE_UNSPECIFIED"):
        return "blocked_or_inaccessible"
    return "indeterminate"


def performance(svc, days: int = 90) -> dict:
    site = require_allowed(PROPERTY)
    end = date.today()
    start = end - timedelta(days=days)
    flt = [{"filters": [{"dimension": "page", "operator": "contains", "expression": "/research/papers/"}]}]
    pages = call(svc.searchanalytics().query(siteUrl=site, body={
        "startDate": start.isoformat(), "endDate": end.isoformat(), "dimensions": ["page"],
        "dimensionFilterGroups": flt, "rowLimit": 1000, "dataState": "all"})).get("rows", [])
    site_total = call(svc.searchanalytics().query(siteUrl=site, body={
        "startDate": start.isoformat(), "endDate": end.isoformat(), "dataState": "all"})).get("rows", [])
    queries = call(svc.searchanalytics().query(siteUrl=site, body={
        "startDate": start.isoformat(), "endDate": end.isoformat(), "dimensions": ["query"],
        "dimensionFilterGroups": flt, "rowLimit": 1000, "dataState": "all"})).get("rows", [])
    dates = call(svc.searchanalytics().query(siteUrl=site, body={
        "startDate": start.isoformat(), "endDate": end.isoformat(), "dimensions": ["date"],
        "rowLimit": 1000, "dataState": "all"})).get("rows", [])
    tot = site_total[0] if site_total else {}
    return {
        "requested_interval": [start.isoformat(), end.isoformat()],
        "data_dates": [dates[0]["keys"][0], dates[-1]["keys"][0]] if dates else None,
        "site": {k: tot.get(k, 0) for k in ("clicks", "impressions", "ctr", "position")} if tot else None,
        "paper_pages": {r["keys"][0]: {k: r.get(k) for k in ("clicks", "impressions", "ctr", "position")}
                        for r in pages},
        # query strings are not stored: only how many distinct queries reached paper pages
        "paper_query_count": len(queries),
    }


# --------------------------------------------------------------------------- website side

def paper_urls() -> list[tuple[str, str, str]]:
    inv = json.loads(INVENTORY.read_text(encoding="utf-8"))
    return [(w["slug"], w["title"], w["concept_doi"]) for w in inv["works"]]


def page_url(slug: str) -> str:
    return f"{PROPERTY}research/papers/{slug}/"


def http_get(url: str) -> tuple[int, dict, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": "l3ragio.github.io gsc audit"})
    try:
        with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as r:
            return r.status, dict(r.headers), r.read()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers or {}), b""
    except OSError:
        return 0, {}, b""


def check_sitemap_xml(body: bytes, expected: list[str]) -> dict:
    try:
        root = ET.fromstring(body)
    except ET.ParseError as e:
        return {"xml_ok": False, "error": str(e)}
    locs = [u.findtext(SM_NS + "loc", "").strip() for u in root.findall(SM_NS + "url")]
    return {
        "xml_ok": root.tag == SM_NS + "urlset",
        "root": root.tag,
        "urls": len(locs),
        "unique": len(set(locs)),
        "foreign": [u for u in locs if not u.startswith(PROPERTY)],
        "papers_missing": [u for u in expected if u not in locs],
    }


def website_checks() -> dict:
    expected = [page_url(s) for s, _, _ in paper_urls()]
    code, headers, body = http_get(SITEMAP)
    sm = {"http_status": code, "content_type": headers.get("Content-Type", ""),
          "bytes": len(body), **(check_sitemap_xml(body, expected) if code == 200 else {"xml_ok": False})}
    rc, _, rb = http_get(PROPERTY + "robots.txt")
    robots = rb.decode("utf-8", "replace")
    disallow = [ln.split(":", 1)[1].strip() for ln in robots.splitlines() if ln.lower().startswith("disallow:")]
    blocked = [u for u in expected if any(d and u[len(PROPERTY) - 1:].startswith(d) for d in disallow)]
    pages = {}
    for slug, _, _ in paper_urls():
        hc, hh, hb = http_get(page_url(slug))
        pc, ph, _ = http_get(page_url(slug) + "paper.pdf")
        pages[slug] = {"html": hc, "pdf": pc, "pdf_type": ph.get("Content-Type", ""),
                       "noindex": bool(re.search(rb'<meta[^>]+name="robots"[^>]+noindex', hb, re.I))}
    return {"sitemap": sm, "robots": {"http_status": rc, "sitemap_directive": SITEMAP in robots,
                                      "disallow": disallow, "papers_blocked": blocked}, "pages": pages}


# --------------------------------------------------------------------------- reports

def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def save_raw(name: str, data) -> Path:
    d = secrets_dir() / "raw"
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}_{name}.json"
    p.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
    return p


def run_audit(svc) -> dict:
    report = {"generated": now_utc(), "property": PROPERTY}
    props = list_properties(svc)
    entry = next((p for p in props if p.get("siteUrl") == PROPERTY), None)
    report["property_access"] = {"accessible": bool(entry),
                                 "permissionLevel": entry.get("permissionLevel") if entry else None,
                                 "visible_properties": len(props)}
    if not entry:
        raise GscError(f"{PROPERTY} is not among the properties of the authorised account "
                       f"({len(props)} visible): sign in with the account that owns it")
    web = website_checks()
    report["website"] = web
    sm = sitemap_status(svc)
    rec = sm["record"]
    report["sitemap"] = {
        "path": SITEMAP,
        "api": {k: rec[k] for k in ("path", "lastSubmitted", "lastDownloaded", "isPending", "isSitemapsIndex",
                                    "type", "errors", "warnings", "contents", "_error") if k in rec},
        "listed_paths": [s.get("path") for s in sm["listed"]],
        "classification": classify_sitemap(rec, web["sitemap"]["http_status"] == 200, web["sitemap"]["xml_ok"]),
    }
    inspections = {}
    for slug, _, _ in paper_urls():
        try:
            inspections[slug] = summarize_inspection(inspect_url(svc, page_url(slug)))
        except GscError as e:
            inspections[slug] = {"state": "indeterminate", "_error": str(e)}
    report["inspections"] = inspections
    try:
        report["performance"] = performance(svc)
    except GscError as e:
        report["performance"] = {"_error": str(e)}
    save_raw("audit", {"properties_visible": len(props), "sitemap": sm, "report": report})
    return report


STATE_LABEL = {
    "indexed": "indexed", "indexed_other_canonical": "indexed (other canonical)",
    "unknown_to_google": "unknown to Google", "discovered_not_crawled": "discovered, not crawled",
    "crawled_not_indexed": "crawled, not indexed", "blocked_or_inaccessible": "blocked or inaccessible",
    "indeterminate": "indeterminate",
}


def render_markdown(r: dict) -> str:
    titles = {s: (t, d) for s, t, d in paper_urls()}
    sm = r["sitemap"]
    api = sm["api"]
    perf = r.get("performance", {})
    lines = [
        "# Google Search Console status",
        "",
        f"Generated by `scripts/gsc_client.py audit --all --write` at {r['generated']}, through the Search "
        f"Console API for the property `{r['property']}` (permission: "
        f"{r['property_access']['permissionLevel']}). Google Search only: this says nothing about Google "
        "Scholar, which has no API.",
        "",
        "## Sitemap",
        "",
        f"- URL: {sm['path']}",
        f"- Live: HTTP {r['website']['sitemap']['http_status']}, "
        f"{r['website']['sitemap'].get('urls', '?')} URLs, XML {'valid' if r['website']['sitemap']['xml_ok'] else 'INVALID'}; "
        f"paper pages missing from it: {len(r['website']['sitemap'].get('papers_missing', []))}",
        f"- API: lastSubmitted {api.get('lastSubmitted', 'absent')}, lastDownloaded {api.get('lastDownloaded', 'absent')}, "
        f"isPending {api.get('isPending', 'absent')}, errors {api.get('errors', 'absent')}, "
        f"warnings {api.get('warnings', 'absent')}"
        + (f", contents {json.dumps(api['contents'])}" if api.get("contents") else "")
        + (f", error: {api['_error']}" if api.get("_error") else ""),
        f"- Classification: **{sm['classification']}**",
        "",
        "## Paper pages (URL Inspection API)",
        "",
        "| Paper | DOI | HTML | PDF | State | Coverage | Last crawl | Google canonical |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for slug, ins in r["inspections"].items():
        t, d = titles.get(slug, (slug, ""))
        p = r["website"]["pages"].get(slug, {})
        gc = ins.get("googleCanonical", "")
        gc = "self" if gc == page_url(slug) else (gc or "")
        lines.append(f"| {t[:60]} | {d} | {p.get('html')} | {p.get('pdf')} | {STATE_LABEL[ins['state']]} | "
                     f"{ins.get('coverageState', ins.get('_error', ''))} | {ins.get('lastCrawlTime', '')} | {gc} |")
    lines += ["", "## Search performance (paper pages)", ""]
    if perf.get("_error"):
        lines.append(f"Not available: {perf['_error']}")
    else:
        pp = perf.get("paper_pages", {})
        lines += [
            f"- Requested interval: {perf['requested_interval'][0]} to {perf['requested_interval'][1]}; "
            f"days with site data: {perf['data_dates'][0] + ' to ' + perf['data_dates'][1] if perf.get('data_dates') else 'none'}",
            f"- Paper URLs with data: {len(pp)}; impressions {sum(v['impressions'] or 0 for v in pp.values())}; "
            f"clicks {sum(v['clicks'] or 0 for v in pp.values())}; distinct queries {perf.get('paper_query_count', 0)}",
            "- No row for a page means no impressions in the interval, not that the page is unindexed.",
        ]
    return "\n".join(lines) + "\n"


def sanitized(r: dict) -> dict:
    """What goes into the repository: no account data, no query strings."""
    keep = dict(r)
    keep["property_access"] = {k: v for k, v in r["property_access"].items() if k != "visible_properties"}
    return keep


# --------------------------------------------------------------------------- doctor

def doctor(client_file: Path, store: TokenStore) -> list[tuple[str, bool, str]]:
    checks: list[tuple[str, bool, str]] = []
    try:
        import google.auth  # noqa: F401
        import google_auth_oauthlib  # noqa: F401
        import googleapiclient  # noqa: F401
        checks.append(("libraries", True, "google-auth, google-auth-oauthlib, google-api-python-client"))
    except ImportError as e:
        checks.append(("libraries", False, f"{e}; use C:/Users/Davide/.venvs/l3ragio-gsc"))
    try:
        info = check_client_file(client_file)
        checks.append(("client file", True, json.dumps(info)))
    except GscError as e:
        checks.append(("client file", False, str(e)))
    checks.append(("secrets outside repository", not _inside_repo(store.dir), str(store.dir)))
    checks.append(("token storage", store.dpapi, "Windows DPAPI (current user)" if store.dpapi
                   else "plaintext 0600 file: no OS encryption on this platform"))
    try:
        creds = get_credentials(store, force_refresh=True)
        checks.append(("token refresh", True, f"access token valid until {creds.expiry:%Y-%m-%d %H:%M} UTC"))
        props = list_properties(service(creds))
        e = next((p for p in props if p.get("siteUrl") == PROPERTY), None)
        checks.append(("property access", bool(e), f"{PROPERTY} {e.get('permissionLevel') if e else 'NOT visible'}"))
    except GscError as e:
        checks.append(("token refresh / API", False, str(e)))
    code, _, body = http_get(SITEMAP)
    checks.append(("live sitemap", code == 200, f"HTTP {code}, {len(body)} bytes"))
    return checks


# --------------------------------------------------------------------------- CLI

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--client-file", type=Path, default=None)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("auth")
    a.add_argument("action", choices=["login", "status", "logout"])
    a.add_argument("--refresh", action="store_true")
    a.add_argument("--login-hint", default=None, help="Google account to preselect on the consent page")
    sub.add_parser("properties")
    s = sub.add_parser("sitemaps")
    s.add_argument("action", choices=["status", "submit"])
    s.add_argument("--confirm", action="store_true")
    i = sub.add_parser("inspect")
    i.add_argument("what", choices=["papers"])
    p = sub.add_parser("performance")
    p.add_argument("what", choices=["papers"])
    p.add_argument("--days", type=int, default=90)
    au = sub.add_parser("audit")
    au.add_argument("--all", action="store_true", required=True)
    au.add_argument("--write", action="store_true")
    sub.add_parser("doctor")
    args = ap.parse_args(argv)

    store = TokenStore()
    client_file = args.client_file or store.dir / "client_secret.json"
    try:
        if args.cmd == "auth" and args.action == "login":
            print(json.dumps(login(client_file, store, args.login_hint), indent=1))
            return 0
        if args.cmd == "auth" and args.action == "logout":
            print("local token deleted" if store.delete() else "no local token")
            print("To revoke the grant itself: https://myaccount.google.com/permissions")
            return 0
        if args.cmd == "doctor":
            ok = True
            for name, good, detail in doctor(client_file, store):
                ok &= good
                print(f"{'OK  ' if good else 'FAIL'} {name}: {redact(detail)}")
            return 0 if ok else 1
        creds = get_credentials(store, force_refresh=getattr(args, "refresh", False))
        if args.cmd == "auth":
            print(json.dumps({"logged_in": True, "valid": creds.valid, "refresh_token": bool(creds.refresh_token),
                              "scopes": sorted(creds.scopes or []), "expiry_utc": f"{creds.expiry:%Y-%m-%dT%H:%M:%SZ}"
                              if creds.expiry else None}, indent=1))
            return 0
        svc = service(creds)
        if args.cmd == "properties":
            for p_ in list_properties(svc):
                mark = "*" if p_.get("siteUrl") in ALLOWED_PROPERTIES else " "
                print(f"{mark} {p_.get('siteUrl')} {p_.get('permissionLevel')}")
            return 0
        if args.cmd == "sitemaps" and args.action == "submit":
            if not args.confirm:
                print("sitemap submission changes Search Console state: add --confirm")
                return 2
            submit_sitemap(svc)
            print(f"submitted {SITEMAP} at {now_utc()}")
            return 0
        if args.cmd == "sitemaps":
            print(json.dumps(sitemap_status(svc), indent=1))
            return 0
        if args.cmd == "inspect":
            for slug, _, _ in paper_urls():
                print(slug, json.dumps(summarize_inspection(inspect_url(svc, page_url(slug)))))
            return 0
        if args.cmd == "performance":
            print(json.dumps(performance(svc, args.days), indent=1))
            return 0
        if args.cmd == "audit":
            r = run_audit(svc)
            md = render_markdown(r)
            print(md)
            if args.write:
                STATUS_JSON.write_text(json.dumps(sanitized(r), indent=1, ensure_ascii=False) + "\n",
                                       encoding="utf-8", newline="\n")
                STATUS_MD.write_text(md, encoding="utf-8", newline="\n")
                print(f"wrote {STATUS_JSON.relative_to(ROOT)} and {STATUS_MD.relative_to(ROOT)}", file=sys.stderr)
            return 0
    except GscError as e:
        print(f"ERROR: {redact(e)}", file=sys.stderr)
        return 1
    return 2


if __name__ == "__main__":
    sys.exit(main())
