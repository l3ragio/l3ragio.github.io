"""Regression tests for the crawl-path checks in validate_papers.py.

A minimal built site that Google Scholar can crawl without JavaScript
(/ -> /research/ -> /research/papers/ -> paper page and PDF) must pass; removing
any one of those plain links, or a redirect in --live mode, must be reported.

Run: python -m unittest scripts/test_validate_discovery.py
"""

from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

SPEC = importlib.util.spec_from_file_location("validate_papers", Path(__file__).with_name("validate_papers.py"))
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)

BASE = "https://example.test"
PAGE = "/research/papers/example/"
PDF = PAGE + "paper.pdf"
PDF_BYTES = b"%PDF-1.4 fixture"


def page_html(pdf_link: bool) -> str:
    return (
        '<html><head><link rel="canonical" href="' + BASE + PAGE + '">'
        '<meta name="citation_title" content="A paper">'
        '<meta name="citation_author" content="One, Author">'
        '<meta name="citation_publication_date" content="2026/11/15">'
        '<meta name="citation_doi" content="10.5281/zenodo.123">'
        '<meta name="citation_pdf_url" content="' + BASE + PDF + '">'
        '<script type="application/ld+json">{"@type":"ScholarlyArticle","headline":"A paper",'
        '"encoding":{"contentUrl":"' + BASE + PDF + '"}}</script>'
        "</head><body><h1>A paper</h1>"
        '<div class="paper-abstract">' + "A visible abstract. " * 20 + "</div>"
        + (f'<a href="{PDF}">PDF (full text)</a>' if pdf_link else "")
        + "</body></html>"
    )


class CrawlPathChecks(unittest.TestCase):
    def build(self, root: Path, **drop: bool) -> Path:
        site = root / "site"
        (root / "_papers").mkdir()
        (root / "_papers" / "example.md").write_text("---\n---\n", encoding="utf-8")
        (root / "_config.yml").write_text(f'url: "{BASE}"\n', encoding="utf-8")
        (root / "inventory.json").write_text(json.dumps({"works": [{
            "slug": "example", "title": "A paper", "authors": ["One, Author"],
            "publication_date": "2026-11-15", "concept_doi": "10.5281/zenodo.123",
            "pdf_sha256": hashlib.sha256(PDF_BYTES).hexdigest(),
        }]}), encoding="utf-8")
        d = site / "research" / "papers" / "example"
        d.mkdir(parents=True)
        (d / "paper.pdf").write_bytes(PDF_BYTES)
        (d / "index.html").write_text(page_html(not drop.get("page_pdf")), encoding="utf-8")
        index = f'<a href="{PAGE}">A paper</a>' + ("" if drop.get("index_pdf") else f'<a href="{PDF}">PDF</a>')
        (site / "research" / "papers" / "index.html").write_text(index, encoding="utf-8")
        research = f'<a href="{PAGE}">A paper</a>' + ("" if drop.get("research_index") else '<a href="/research/papers/">All papers</a>')
        (site / "research" / "index.html").write_text(research, encoding="utf-8")
        (site / "index.html").write_text("" if drop.get("home_research") else '<a href="/research/">Research</a>', encoding="utf-8")
        (site / "sitemap.xml").write_text(f"<loc>{BASE}{PAGE}</loc>", encoding="utf-8")
        (site / "robots.txt").write_text(f"Sitemap: {BASE}/sitemap.xml\n", encoding="utf-8")
        return site

    def run_validator(self, **drop: bool) -> tuple[int, str]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            site = self.build(root, **drop)
            out = io.StringIO()
            with patch.object(validator, "ROOT", root), \
                    patch.object(validator, "INVENTORY", root / "inventory.json"), \
                    patch.object(validator, "PAPERS_SRC", root / "_papers"), \
                    patch.object(validator, "check_thesis", return_value=True), \
                    patch.object(sys, "argv", ["validate_papers.py", "--site", str(site)]), \
                    contextlib.redirect_stdout(out):
                return validator.main(), out.getvalue()

    def test_complete_site_passes(self):
        code, out = self.run_validator()
        self.assertEqual(code, 0, out)

    def test_each_missing_edge_is_reported(self):
        cases = {
            "index_pdf": "example: no direct PDF link from /research/papers/",
            "page_pdf": "example: no plain link from the paper page to its PDF",
            "home_research": "no plain link from / to /research/",
            "research_index": "no plain link from /research/ to /research/papers/",
        }
        for edge, message in cases.items():
            with self.subTest(edge=edge):
                code, out = self.run_validator(**{edge: True})
                self.assertEqual(code, 1, out)
                self.assertIn("FAIL: " + message, out)
                self.assertEqual(out.count("FAIL:"), 1, out)

    def test_live_redirect_is_recorded(self):
        src = validator.Source(None, BASE)
        resp = MagicMock(status=200)
        resp.headers.get.return_value = "application/pdf"
        resp.geturl.return_value = BASE + "/elsewhere/paper.pdf"
        resp.read.return_value = PDF_BYTES
        resp.__enter__.return_value = resp
        with patch.object(validator.urllib.request, "urlopen", return_value=resp):
            self.assertEqual(src.get(PDF), PDF_BYTES)
        self.assertEqual(src.redirected, {PDF: BASE + "/elsewhere/paper.pdf"})
        resp.geturl.return_value = BASE + PDF
        src2 = validator.Source(None, BASE)
        with patch.object(validator.urllib.request, "urlopen", return_value=resp):
            src2.get(PDF)
        self.assertEqual(src2.redirected, {})


if __name__ == "__main__":
    unittest.main()
