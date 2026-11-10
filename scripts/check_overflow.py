#!/usr/bin/env python3
"""Detect horizontal overflow at phone and tablet widths.

Each page is loaded in an iframe whose width is exactly the test width, so
CSS media queries see that viewport (a headless-Chrome window cannot go below
about 500 px, which makes plain narrow screenshots misleading). Inside each
frame the script compares the document's scrollWidth with its clientWidth and
lists the elements that stick out, ignoring those inside a scroll container
(tables and code blocks that scroll on purpose).

Standard library only. Needs a Chrome/Chromium binary.

Usage:
    python3 scripts/check_overflow.py --site _site
    python3 scripts/check_overflow.py --site _site --widths 320 390 --all-papers
    python3 scripts/check_overflow.py --site _site --chrome "/path/to/chrome"

Exit code 1 if any page overflows by more than --tolerance pixels.
"""

from __future__ import annotations

import argparse
import functools
import http.server
import json
import re
import shutil
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PAGES = ["/", "/research/", "/research/papers/", "/research/thesis/", "/research/mck-properties/", "/about/"]
CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome",
]

HARNESS = """<!doctype html><meta charset="utf-8"><title>overflow harness</title>
<body style="margin:0"><pre id="out">running</pre><div id="frames"></div>
<script>
const jobs = %(jobs)s;
const results = [];
function selector(el) {
  let s = el.tagName.toLowerCase();
  if (el.id) s += '#' + el.id;
  if (el.className && typeof el.className === 'string') s += '.' + el.className.trim().split(/\\s+/).slice(0, 2).join('.');
  return s;
}
function inScroller(el, root) {
  for (let p = el.parentElement; p && p !== root; p = p.parentElement) {
    const o = getComputedStyle(p).overflowX;
    if (o === 'auto' || o === 'scroll' || o === 'hidden' || o === 'clip') return true;
  }
  return false;
}
function run(i) {
  if (i >= jobs.length) {
    document.getElementById('out').textContent = JSON.stringify(results);
    document.title = 'done';
    return;
  }
  const [page, width] = jobs[i];
  const f = document.createElement('iframe');
  f.style.cssText = 'border:0;width:' + width + 'px;height:900px;display:block';
  // A frame that never loads (bad path, blocked URL) must not stall the run.
  const guard = setTimeout(() => {
    results.push({page, width, error: 'frame did not load within 20 s'});
    f.remove();
    run(i + 1);
  }, 20000);
  f.onload = () => { clearTimeout(guard); setTimeout(() => {
    try {
      const d = f.contentDocument, de = d.documentElement;
      const over = de.scrollWidth - de.clientWidth;
      const out = [];
      if (over > 0) {
        for (const el of d.body.querySelectorAll('*')) {
          const r = el.getBoundingClientRect();
          if (r.width > 0 && r.right > de.clientWidth + 1 && !inScroller(el, d.body)) {
            out.push([Math.round(r.right - de.clientWidth), selector(el)]);
          }
        }
        out.sort((a, b) => b[0] - a[0]);
      }
      results.push({page, width, bodyChars: d.body.innerText.length, scrollWidth: de.scrollWidth, clientWidth: de.clientWidth, over, offenders: out.slice(0, 6)});
    } catch (e) { results.push({page, width, error: String(e)}); }
    f.remove();
    run(i + 1);
  }, 400); };
  f.src = page;
  document.getElementById('frames').appendChild(f);
}
run(0);
</script>
"""


def find_chrome(explicit: str | None) -> str:
    for c in ([explicit] if explicit else CHROME_CANDIDATES):
        if c and (Path(c).exists() or shutil.which(c)):
            return c
    sys.exit("No Chrome/Chromium found; pass --chrome PATH")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--site", default=str(ROOT / "_site"), help="built site directory to serve")
    ap.add_argument("--widths", type=int, nargs="+", default=[320, 375, 390, 768, 1280])
    ap.add_argument("--pages", nargs="+", default=None)
    ap.add_argument("--all-papers", action="store_true", help="also test every /research/papers/<slug>/")
    ap.add_argument("--chrome")
    ap.add_argument("--tolerance", type=int, default=1, help="allowed overflow in px")
    ap.add_argument("--verbose", action="store_true", help="print every measurement, not only overflows")
    args = ap.parse_args()

    site = Path(args.site)
    pages = args.pages or list(DEFAULT_PAGES)
    if args.all_papers:
        pages += [f"/research/papers/{p.name}/" for p in sorted((site / "research" / "papers").iterdir()) if p.is_dir()]
    jobs = [[p, w] for p in pages for w in args.widths]
    harness = (HARNESS % {"jobs": json.dumps(jobs)}).encode("utf-8")

    class Handler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):  # noqa: N802
            if self.path.split("?")[0] == "/__harness__.html":
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(harness)))
                self.end_headers()
                self.wfile.write(harness)
            else:
                super().do_GET()

        def log_message(self, *a):  # silence
            pass

    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Handler, directory=str(site)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    port = srv.server_address[1]

    chrome = find_chrome(args.chrome)
    with tempfile.TemporaryDirectory() as prof:
        proc = subprocess.run(
            [chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--user-data-dir={prof}",
             "--enable-logging=stderr", "--v=0",
             "--virtual-time-budget=120000", "--dump-dom", f"http://127.0.0.1:{port}/__harness__.html"],
            capture_output=True, text=True, timeout=600, encoding="utf-8", errors="replace")
    srv.shutdown()
    m = re.search(r'<pre id="out">(.*?)</pre>', proc.stdout, re.S)
    if not m or m.group(1).strip() == "running":
        print("harness did not finish. Chrome exit", proc.returncode,
              "\nstdout tail:", proc.stdout[-600:], "\nstderr tail:", proc.stderr[-600:])
        return 2
    import html
    results = json.loads(html.unescape(m.group(1)))

    bad = 0
    for r in results:
        if "error" in r:
            print(f"ERROR {r['page']} @{r['width']}: {r['error']}")
            bad += 1
        elif r["bodyChars"] < 150:
            # a 404 page has ~120 characters and no overflow: do not let it pass as "fine"
            print(f"SUSPECT  {r['page']} @{r['width']}px: only {r['bodyChars']} characters of text (missing page?)")
            bad += 1
        elif args.verbose and r["over"] <= args.tolerance:
            print(f"ok       {r['page']} @{r['width']}px: scrollWidth {r['scrollWidth']} / clientWidth {r['clientWidth']}, {r['bodyChars']} chars of text")
        elif r["over"] > args.tolerance:
            bad += 1
            off = "; ".join(f"+{px}px {sel}" for px, sel in r["offenders"][:4])
            print(f"OVERFLOW {r['page']} @{r['width']}px: scrollWidth {r['scrollWidth']} > {r['clientWidth']} ({off})")
    print(f"check_overflow: {len(jobs)} page/width combinations, {bad} with overflow")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
