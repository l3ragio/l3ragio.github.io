#!/usr/bin/env python3
"""Google Scholar compliance and completeness checks for the paper pages.

Checks every work in docs/papers/zenodo_inventory.json against the built
site (default: ./_site) or against the live site (--live):

  * exactly one landing page per work, and no citation_* tags elsewhere;
  * Highwire tags: one citation_title (= Zenodo title), citation_author tags
    equal to the Zenodo creators in order, citation_publication_date in
    YYYY/MM/DD, citation_doi = concept DOI, citation_pdf_url absolute and in
    the same directory as the page;
  * self-canonical URL, no robots noindex;
  * the full abstract is in the initial HTML and not inside <details>,
    <script>, <noscript> or <template>;
  * ScholarlyArticle JSON-LD parses and agrees with the visible title;
  * the PDF exists, starts with %PDF, is <= 5 MB, and its SHA-256 equals the
    inventory value (i.e. it is the Zenodo file, byte for byte);
  * the sitemap lists every page; /research/papers/ and /research/ link to
    every page;
  * with --live: HTTP 200 and the right Content-Type for page and PDF.

For the doctoral thesis (_data/thesis.yml, /research/thesis/) it checks the
dissertation tags (citation_dissertation_institution, no journal / DOI /
citation_pdf_url, since no PDF is hosted here), the abstract against the IRIS
text, the Thesis JSON-LD, the IRIS link, discovery links and sitemap entry,
and that the page makes no degree-conferral claim.

Standard library only, so it runs unchanged in CI.

Usage:
    python3 scripts/validate_papers.py               # against ./_site
    python3 scripts/validate_papers.py --site DIR
    python3 scripts/validate_papers.py --live        # against https://l3ragio.github.io
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INVENTORY = ROOT / "docs" / "papers" / "zenodo_inventory.json"
PAPERS_SRC = ROOT / "_papers"
LIMIT = 5 * 1024 * 1024
UA = "l3ragio.github.io paper validator"


def site_url() -> str:
    m = re.search(r'^url:\s*["\']?([^"\'\s#]+)', (ROOT / "_config.yml").read_text(encoding="utf-8"), re.M)
    return m.group(1).rstrip("/")


class Page(HTMLParser):
    HIDING = {"details", "script", "noscript", "template"}

    def __init__(self) -> None:
        super().__init__()
        self.meta: list[tuple[str, str]] = []
        self.canonical: list[str] = []
        self.links: set[str] = set()
        self.jsonld: list[str] = []
        self._in_jsonld = False
        self._buf: list[str] = []
        self._hide_depth = 0
        self._abs_depth = 0           # >0 while inside div.paper-abstract
        self.abstract_text: list[str] = []
        self.abstract_hidden = False
        self.abstract_found = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "meta" and a.get("name"):
            self.meta.append((a["name"], a.get("content", "")))
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical.append(a.get("href", ""))
        if tag == "a" and a.get("href"):
            self.links.add(a["href"])
        if tag == "script" and a.get("type") == "application/ld+json":
            self._in_jsonld, self._buf = True, []
        if tag in self.HIDING:
            self._hide_depth += 1
        if self._abs_depth:
            if tag == "div":
                self._abs_depth += 1
        elif tag == "div" and "paper-abstract" in (a.get("class") or "").split():
            self._abs_depth = 1
            self.abstract_found = True
            self.abstract_hidden = self._hide_depth > 0

    def handle_endtag(self, tag):
        if tag == "script" and self._in_jsonld:
            self.jsonld.append("".join(self._buf))
            self._in_jsonld = False
        if tag in self.HIDING and self._hide_depth:
            self._hide_depth -= 1
        if self._abs_depth and tag == "div":
            self._abs_depth -= 1

    def handle_data(self, data):
        if self._in_jsonld:
            self._buf.append(data)
        if self._abs_depth:
            self.abstract_text.append(data)


class Source:
    """Reads site files either from a build directory or from the live site."""

    def __init__(self, site: Path | None, base: str) -> None:
        self.site, self.base = site, base
        self.content_types: dict[str, str] = {}

    def get(self, path: str) -> bytes | None:
        if self.site is not None:
            f = self.site / path.lstrip("/")
            if path.endswith("/"):
                f = f / "index.html"
            return f.read_bytes() if f.exists() else None
        req = urllib.request.Request(self.base + path, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                self.content_types[path] = r.headers.get("Content-Type", "")
                return r.read() if r.status == 200 else None
        except Exception:  # noqa: BLE001
            return None

    def all_html(self):
        if self.site is None:
            return []
        return [p for p in self.site.rglob("*.html")]


def norm_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


THESIS_YML = ROOT / "_data" / "thesis.yml"


def thesis_values() -> dict:
    """The few thesis.yml fields the checks need (regex, to stay stdlib-only)."""
    text = THESIS_YML.read_text(encoding="utf-8")
    vals = {}
    for key in ("title", "author", "issued", "institution", "iris_url", "handle", "handle_url"):
        m = re.search(rf'^{key}:\s*"([^"]*)"', text, re.M)
        vals[key] = m.group(1) if m else ""
    bib = re.search(r"^bibtex: \|\n((?:  .*\n?)+)", text, re.M)
    vals["bibtex"] = bib.group(1) if bib else ""
    block = re.search(r"^abstract:\n(.*?)^files:", text, re.M | re.S)
    vals["abstract"] = re.findall(r'^  - "(.*)"\s*$', block.group(1), re.M) if block else []
    return vals


def check_thesis(src: "Source", base: str, args, err, research: "Page", sitemap: str) -> bool:
    t = thesis_values()
    path = "/research/thesis/"
    page_abs = base + path
    raw = src.get(path)
    if raw is None:
        err(f"thesis: landing page {path} missing")
        return False
    if args.live and "text/html" not in src.content_types.get(path, ""):
        err(f"thesis: page Content-Type {src.content_types.get(path)!r}")
    html = raw.decode("utf-8")
    p = Page()
    p.feed(html)
    meta: dict[str, list[str]] = {}
    for k, v in p.meta:
        meta.setdefault(k, []).append(v)

    def one(name: str, want: str) -> None:
        vals = meta.get(name, [])
        if vals != [want]:
            err(f"thesis: {name} {vals} != [{want!r}]")

    for want in (f"title = {{{t['title']}}}", f"author = {{{t['author']}}}", f"year = {{{t['issued'][:4]}}}",
                 f"school = {{{t['institution']}}}", t["handle"], t["handle_url"]):
        if want not in t["bibtex"]:
            err(f"thesis: BibTeX in _data/thesis.yml lacks {want!r}")
    one("citation_title", t["title"])
    one("citation_author", t["author"])
    one("citation_publication_date", t["issued"].replace("-", "/"))
    one("citation_dissertation_institution", t["institution"])
    for name in ("citation_pdf_url", "citation_doi", "citation_journal_title", "citation_conference_title",
                 "citation_technical_report_institution", "citation_technical_report_number"):
        if name in meta:
            err(f"thesis: unexpected {name} (no hosted PDF, no DOI, not a journal/conference/report)")
    if p.canonical != [page_abs]:
        err(f"thesis: canonical {p.canonical} != [{page_abs}]")
    robots = " ".join(meta.get("robots", []) + meta.get("googlebot", [])).lower()
    if "noindex" in robots or "nofollow" in robots:
        err(f"thesis: robots meta {robots!r}")
    if not p.abstract_found or p.abstract_hidden:
        err("thesis: abstract missing or hidden (details/script/noscript/template)")
    else:
        # paragraphs are separate <p> elements, so compare without whitespace
        got = re.sub(r"\s+", "", "".join(p.abstract_text))
        want = re.sub(r"\s+", "", "".join(t["abstract"]))
        if not want or got != want:
            err("thesis: visible abstract differs from the IRIS abstract in _data/thesis.yml")
    ld = []
    for block in p.jsonld:
        try:
            data = json.loads(block)
        except json.JSONDecodeError as e:
            err(f"thesis: JSON-LD does not parse: {e}")
            continue
        if isinstance(data, dict) and data.get("@type") == "Thesis":
            ld.append(data)
    if len(ld) != 1 or ld[0].get("headline") != t["title"]:
        err("thesis: expected one Thesis JSON-LD whose headline is the thesis title")
    if t["iris_url"] not in p.links:
        err("thesis: no link to the IRIS record")
    if re.search(r"\.pdf", " ".join(l for l in p.links if l.startswith(base))):
        err("thesis: links to a PDF on this site (the thesis is not hosted here)")
    if src.site is not None and list((src.site / "research" / "thesis").glob("*.pdf")):
        err("thesis: a PDF is present in research/thesis/ (must not be hosted)")
    body = re.sub(r"<script.*?</script>|<style.*?</style>", " ", html, flags=re.S)
    text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body))
    if re.search(r"\b(conferred|awarded|was granted|has been granted)\b", text, re.I):
        err("thesis: page makes a degree-conferral claim; IRIS records only a deposit and a discussion date")
    if path not in research.links and base + path not in research.links:
        err("thesis: no plain link from /research/")
    if f"<loc>{page_abs}</loc>" not in sitemap:
        err("thesis: not in sitemap.xml")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--site", default=str(ROOT / "_site"))
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    base = site_url()
    src = Source(None if args.live else Path(args.site), base)
    inv = json.loads(INVENTORY.read_text(encoding="utf-8"))
    works = inv["works"]
    errors: list[str] = []
    ok = 0

    def err(msg: str) -> None:
        errors.append(msg)

    # gate <-> generated pages <-> inventory
    gen = {p.stem for p in PAPERS_SRC.glob("*.md")}
    slugs = [w["slug"] for w in works]
    if len(slugs) != len(set(slugs)):
        err("inventory: duplicate slug")
    if gen != set(slugs):
        err(f"_papers/ vs inventory mismatch: only in _papers {sorted(gen - set(slugs))}, only in inventory {sorted(set(slugs) - gen)}")

    for w in works:
        slug = w["slug"]
        path = f"/research/papers/{slug}/"
        page_abs = base + path
        pdf_abs = page_abs + "paper.pdf"
        raw = src.get(path)
        if raw is None:
            err(f"{slug}: landing page {path} missing")
            continue
        if args.live and "text/html" not in src.content_types.get(path, ""):
            err(f"{slug}: page Content-Type {src.content_types.get(path)!r}")
        p = Page()
        p.feed(raw.decode("utf-8"))
        meta: dict[str, list[str]] = {}
        for k, v in p.meta:
            meta.setdefault(k, []).append(v)

        def one(name: str) -> str | None:
            vals = meta.get(name, [])
            if len(vals) != 1:
                err(f"{slug}: expected exactly one {name}, found {len(vals)}")
                return None
            return vals[0]

        if one("citation_title") != w["title"]:
            err(f"{slug}: citation_title {meta.get('citation_title')} != Zenodo title")
        if meta.get("citation_author", []) != w["authors"]:
            err(f"{slug}: citation_author {meta.get('citation_author')} != {w['authors']}")
        d = one("citation_publication_date")
        if d != w["publication_date"].replace("-", "/") or not re.fullmatch(r"\d{4}(/\d{2}(/\d{2})?)?", d or ""):
            err(f"{slug}: citation_publication_date {d!r}")
        if one("citation_doi") != w["concept_doi"]:
            err(f"{slug}: citation_doi != concept DOI {w['concept_doi']}")
        pu = one("citation_pdf_url")
        if pu != pdf_abs or pu.rsplit("/", 1)[0] != page_abs.rstrip("/"):
            err(f"{slug}: citation_pdf_url {pu!r} is not {pdf_abs} (same directory as the page)")
        for name in ("journal_title", "conference_title", "technical_report_institution"):
            if f"citation_{name}" in meta:
                err(f"{slug}: unexpected citation_{name} (no verified venue)")
        if p.canonical != [page_abs]:
            err(f"{slug}: canonical {p.canonical} != [{page_abs}]")
        robots = " ".join(meta.get("robots", []) + meta.get("googlebot", [])).lower()
        if "noindex" in robots or "nofollow" in robots:
            err(f"{slug}: robots meta {robots!r}")
        if not p.abstract_found:
            err(f"{slug}: no div.paper-abstract in the HTML")
        elif p.abstract_hidden:
            err(f"{slug}: abstract is inside details/script/noscript/template")
        elif len(norm_ws("".join(p.abstract_text))) < 200:
            err(f"{slug}: abstract text too short ({len(norm_ws(''.join(p.abstract_text)))} chars)")
        articles = []
        for block in p.jsonld:
            try:
                data = json.loads(block)
            except json.JSONDecodeError as e:
                err(f"{slug}: JSON-LD does not parse: {e}")
                continue
            if isinstance(data, dict) and data.get("@type") == "ScholarlyArticle":
                articles.append(data)
        if len(articles) != 1:
            err(f"{slug}: expected one ScholarlyArticle JSON-LD, found {len(articles)}")
        elif articles[0].get("headline") != w["title"] or articles[0]["encoding"]["contentUrl"] != pdf_abs:
            err(f"{slug}: JSON-LD disagrees with the page")

        pdf = src.get(path + "paper.pdf")
        if pdf is None:
            err(f"{slug}: PDF missing")
        else:
            if args.live and "application/pdf" not in src.content_types.get(path + "paper.pdf", ""):
                err(f"{slug}: PDF Content-Type {src.content_types.get(path + 'paper.pdf')!r}")
            if not pdf.startswith(b"%PDF"):
                err(f"{slug}: PDF does not start with %PDF")
            if len(pdf) > LIMIT:
                err(f"{slug}: PDF {len(pdf)} bytes > 5 MB")
            if hashlib.sha256(pdf).hexdigest() != w["pdf_sha256"]:
                err(f"{slug}: PDF SHA-256 differs from the Zenodo file")
        ok += 1

    # discovery paths
    sitemap = (src.get("/sitemap.xml") or b"").decode("utf-8")
    index = Page()
    index.feed((src.get("/research/papers/") or b"").decode("utf-8"))
    research = Page()
    research.feed((src.get("/research/") or b"").decode("utf-8"))
    for slug in slugs:
        path = f"/research/papers/{slug}/"
        if f"<loc>{base}{path}</loc>" not in sitemap:
            err(f"{slug}: not in sitemap.xml")
        for name, pg in (("/research/papers/", index), ("/research/", research)):
            if path not in pg.links and base + path not in pg.links:
                err(f"{slug}: no plain link from {name}")
    thesis_ok = check_thesis(src, base, args, err, research, sitemap)
    robots_txt = (src.get("/robots.txt") or b"").decode("utf-8")
    if f"Sitemap: {base}/sitemap.xml" not in robots_txt:
        err("robots.txt does not reference the sitemap")
    if re.search(r"^Disallow:\s*/(research)?\s*$", robots_txt, re.M):
        err("robots.txt disallows the papers")

    # citation tags only on single-paper pages
    if src.site is not None:
        paper_pages = {(src.site / "research" / "papers" / s / "index.html").resolve() for s in slugs}
        paper_pages.add((src.site / "research" / "thesis" / "index.html").resolve())  # dissertation tags, checked above
        for f in src.all_html():
            if f.resolve() not in paper_pages and b'name="citation_title"' in f.read_bytes():
                err(f"citation_title on a non-paper page: {f.relative_to(src.site)}")

    target = base if args.live else args.site
    print(f"validate_papers: {len(works)} works + thesis checked against {target}; "
          f"{ok} paper pages found, thesis page {'found' if thesis_ok else 'MISSING'}; {len(errors)} problem(s).")
    for e in errors:
        print("FAIL:", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
