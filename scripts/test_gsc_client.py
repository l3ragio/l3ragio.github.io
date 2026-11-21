"""Unit tests for scripts/gsc_client.py. Every Google API call is mocked:
these tests say nothing about real connectivity (see `gsc_client.py doctor`).

Run with the environment that has the Google libraries:
    C:/Users/Davide/.venvs/l3ragio-gsc/Scripts/python.exe -m unittest scripts/test_gsc_client.py
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gsc_client as g  # noqa: E402

from googleapiclient.errors import HttpError  # noqa: E402
from google.auth.exceptions import RefreshError  # noqa: E402


def http_error(status: int, reason: str = "x", message: str = "m") -> HttpError:
    resp = MagicMock()
    resp.status = status
    resp.reason = reason
    body = json.dumps({"error": {"code": status, "message": message, "errors": [{"reason": reason}]}}).encode()
    return HttpError(resp, body)


def request_raising(*effects):
    req = MagicMock()
    req.execute.side_effect = list(effects)
    return req


class TempStore:
    def __enter__(self):
        self.tmp = tempfile.TemporaryDirectory()
        return g.TokenStore(Path(self.tmp.name))

    def __exit__(self, *a):
        self.tmp.cleanup()


AUTH_INFO = {"token": "ya29.old", "refresh_token": "1//refreshtokenvalue", "client_id": "x.apps.googleusercontent.com",
             "client_secret": "GOCSPX-secret", "token_uri": "https://oauth2.googleapis.com/token",
             "scopes": g.SCOPES, "expiry": (datetime.utcnow() - timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ")}


class ClientFile(unittest.TestCase):
    def write(self, d) -> Path:
        f = Path(tempfile.mkdtemp()) / "client_secret.json"
        f.write_text(json.dumps(d), encoding="utf-8")
        return f

    def test_missing(self):
        with self.assertRaisesRegex(g.AuthError, "not found"):
            g.check_client_file(Path(tempfile.mkdtemp()) / "nope.json")

    def test_wrong_type(self):
        with self.assertRaisesRegex(g.AuthError, "'web'"):
            g.check_client_file(self.write({"web": {}}))

    def test_valid_and_no_values_returned(self):
        f = self.write({"installed": {"client_id": "1-a.apps.googleusercontent.com", "client_secret": "GOCSPX-s",
                                      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                                      "token_uri": "https://oauth2.googleapis.com/token", "project_id": "p",
                                      "redirect_uris": ["http://localhost"]}})
        info = g.check_client_file(f)
        self.assertTrue(info["loopback_redirect"])
        self.assertNotIn("GOCSPX", json.dumps(info))
        self.assertNotIn("1-a", json.dumps(info))


class Storage(unittest.TestCase):
    def test_roundtrip_encrypted_on_windows(self):
        with TempStore() as st:
            st.save({"refresh_token": "1//abc"})
            if os.name == "nt":
                self.assertNotIn(b"1//abc", st.path.read_bytes())
            self.assertEqual(st.load(), {"refresh_token": "1//abc"})
            self.assertTrue(st.delete())

    def test_refuses_repository_dir(self):
        with self.assertRaises(g.GscError):
            g.TokenStore(g.ROOT / "secrets")


class Credentials(unittest.TestCase):
    def test_missing_token(self):
        with TempStore() as st, self.assertRaisesRegex(g.AuthError, "auth login"):
            g.get_credentials(st)

    def test_refresh_saves_new_token(self):
        with TempStore() as st:
            st.save(AUTH_INFO)

            def fake_refresh(self_, request):
                self_.token = "ya29.new"
                self_.expiry = datetime.utcnow() + timedelta(hours=1)

            with patch("google.oauth2.credentials.Credentials.refresh", fake_refresh):
                creds = g.get_credentials(st)
            self.assertTrue(creds.valid)
            self.assertEqual(st.load()["token"], "ya29.new")
            self.assertEqual(st.load()["refresh_token"], AUTH_INFO["refresh_token"])

    def test_revoked_token_is_diagnosed_without_leaking(self):
        with TempStore() as st:
            st.save(AUTH_INFO)
            err = RefreshError("invalid_grant: Token has been expired or revoked. refresh_token=1//refreshtokenvalue")
            with patch("google.oauth2.credentials.Credentials.refresh", side_effect=err):
                with self.assertRaises(g.AuthError) as cm:
                    g.get_credentials(st)
            self.assertIn("7 days", str(cm.exception))
            self.assertNotIn("1//refreshtokenvalue", str(cm.exception))


class Calls(unittest.TestCase):
    def test_retries_transient_then_succeeds(self):
        sleeps = []
        req = request_raising(http_error(503), http_error(429), {"ok": 1})
        self.assertEqual(g.call(req, sleep=sleeps.append), {"ok": 1})
        self.assertEqual(len(sleeps), 2)
        self.assertGreater(sleeps[1], sleeps[0] * 1.2)

    def test_quota_exhausted_after_attempts(self):
        req = request_raising(*[http_error(429, "rateLimitExceeded")] * 3)
        with self.assertRaisesRegex(g.GscError, "429.*quota"):
            g.call(req, attempts=3, sleep=lambda s: None)

    def test_permission_error_not_retried(self):
        req = request_raising(http_error(403, "forbidden", "User does not have sufficient permission"))
        with self.assertRaisesRegex(g.GscError, "403.*lacks access"):
            g.call(req, sleep=lambda s: None)
        self.assertEqual(req.execute.call_count, 1)


class Allowlist(unittest.TestCase):
    def test_other_property_refused(self):
        with self.assertRaises(g.GscError):
            g.require_allowed("https://example.com/")

    def test_inspect_outside_property_refused(self):
        with self.assertRaises(g.GscError):
            g.inspect_url(MagicMock(), "https://example.com/x/")

    def test_audit_stops_when_property_not_visible(self):
        svc = MagicMock()
        svc.sites().list().execute.return_value = {"siteEntry": [{"siteUrl": "sc-domain:other.org",
                                                                  "permissionLevel": "siteOwner"}]}
        with self.assertRaisesRegex(g.GscError, "not among the properties"):
            g.run_audit(svc)


class SitemapClassification(unittest.TestCase):
    def test_pending(self):
        self.assertEqual(g.classify_sitemap({"isPending": True, "lastSubmitted": "t"}, True, True),
                         "D_SUBMITTED_NOT_YET_PROCESSED")

    def test_processed(self):
        self.assertEqual(g.classify_sitemap({"lastDownloaded": "t", "errors": "0"}, True, True),
                         "F_SUCCESSFULLY_PROCESSED")
        self.assertEqual(g.classify_sitemap({"lastDownloaded": "t", "errors": "2"}, True, True),
                         "E_PROCESSED_WITH_ERRORS")

    def test_site_side_failures_first(self):
        self.assertEqual(g.classify_sitemap({}, False, False), "A_HTTP_RETRIEVAL_FAILURE")
        self.assertEqual(g.classify_sitemap({}, True, False), "B_XML_VALIDATION_ERROR")
        self.assertEqual(g.classify_sitemap({"_error": "HTTP 404"}, True, True), "G_INSUFFICIENT_INFORMATION")

    def test_xml_check(self):
        ok = (b'<?xml version="1.0"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
              b'<url><loc>https://l3ragio.github.io/research/papers/a/</loc></url></urlset>')
        r = g.check_sitemap_xml(ok, ["https://l3ragio.github.io/research/papers/a/",
                                     "https://l3ragio.github.io/research/papers/b/"])
        self.assertTrue(r["xml_ok"])
        self.assertEqual(r["papers_missing"], ["https://l3ragio.github.io/research/papers/b/"])
        self.assertFalse(g.check_sitemap_xml(b"<urlset><url>", [])["xml_ok"])
        self.assertFalse(g.check_sitemap_xml(b"<urlset/>", [])["xml_ok"])  # wrong namespace


class Inspection(unittest.TestCase):
    U = "https://l3ragio.github.io/research/papers/a/"

    def test_states(self):
        c = g.classify_inspection
        self.assertEqual(c({"verdict": "PASS", "coverageState": "Submitted and indexed",
                            "googleCanonical": self.U, "userCanonical": self.U}), "indexed")
        self.assertEqual(c({"verdict": "PASS", "googleCanonical": "https://zenodo.org/x",
                            "userCanonical": self.U}), "indexed_other_canonical")
        self.assertEqual(c({"verdict": "NEUTRAL", "coverageState": "URL is unknown to Google"}), "unknown_to_google")
        self.assertEqual(c({"verdict": "NEUTRAL", "coverageState": "Discovered - currently not indexed"}),
                         "discovered_not_crawled")
        self.assertEqual(c({"verdict": "NEUTRAL", "coverageState": "Crawled - currently not indexed"}),
                         "crawled_not_indexed")
        self.assertEqual(c({"robotsTxtState": "DISALLOWED"}), "blocked_or_inaccessible")
        self.assertEqual(c({}), "indeterminate")

    def test_missing_optional_fields(self):
        s = g.summarize_inspection({"indexStatusResult": {"verdict": "NEUTRAL",
                                                          "coverageState": "URL is unknown to Google"}})
        self.assertEqual(s["state"], "unknown_to_google")
        self.assertNotIn("lastCrawlTime", s)
        self.assertNotIn("inspectionResultLink", s)


class Report(unittest.TestCase):
    def test_render_and_sanitize(self):
        slug, title, doi = g.paper_urls()[0]
        r = {"generated": "2026-11-21T00:00:00Z", "property": g.PROPERTY,
             "property_access": {"accessible": True, "permissionLevel": "siteOwner", "visible_properties": 7},
             "website": {"sitemap": {"http_status": 200, "urls": 98, "xml_ok": True, "papers_missing": []},
                         "pages": {slug: {"html": 200, "pdf": 200}}},
             "sitemap": {"path": g.SITEMAP, "api": {"isPending": True}, "listed_paths": [],
                         "classification": "D_SUBMITTED_NOT_YET_PROCESSED"},
             "inspections": {slug: {"state": "unknown_to_google", "coverageState": "URL is unknown to Google"}},
             "performance": {"requested_interval": ["a", "b"], "data_dates": None, "paper_pages": {},
                             "paper_query_count": 0}}
        md = g.render_markdown(r)
        self.assertIn("D_SUBMITTED_NOT_YET_PROCESSED", md)
        self.assertIn("unknown to Google", md)
        self.assertIn("not that the page is unindexed", md)
        self.assertNotIn("visible_properties", json.dumps(g.sanitized(r)))
        self.assertEqual(md, g.render_markdown(r))  # deterministic


class Redaction(unittest.TestCase):
    def test_patterns(self):
        s = g.redact('ya29.a0Abc 1//0gAbcdefghijkl GOCSPX-xyz {"refresh_token": "abc"} code=4/0AbCdEfGhIjKl&s=1')
        for leak in ("ya29.a0Abc", "1//0gAbcdefghijkl", "GOCSPX-xyz", '"abc"', "4/0AbCdEfGhIjKl"):
            self.assertNotIn(leak, s)

    def test_http_error_redacted(self):
        msg = g.describe_http_error(http_error(401, "authError", "bad token ya29.secretvalue"))
        self.assertNotIn("ya29.secretvalue", msg)


class Cli(unittest.TestCase):
    def test_submit_requires_confirm(self):
        with patch.object(g, "get_credentials"), patch.object(g, "service"), \
                patch.object(g, "submit_sitemap") as sub:
            self.assertEqual(g.main(["sitemaps", "submit"]), 2)
            sub.assert_not_called()


if __name__ == "__main__":
    unittest.main()
