# Scholarly paper pages: how they work

Each public Zenodo paper by Davide Bragetti has one landing page at
`https://l3ragio.github.io/research/papers/<slug>/`, with the full-text PDF
next to it at `.../<slug>/paper.pdf`. The pages are built to be indexed by
Google Scholar.

Zenodo remains the archive and the DOI authority. The site mirrors the
preferred version's PDF byte for byte and points to Zenodo for every version.

## Files

| Path | Role | Edited by |
|------|------|-----------|
| `_data/paper_sources.yml` | the gate: which Zenodo concepts get a page, slug, BibTeX key, research line, verified IRIS handles, explicit exclusions | hand |
| `scripts/sync_zenodo_papers.py` | Zenodo API -> `_papers/*.md` + PDFs + inventory | - |
| `_papers/<slug>.md` | generated front matter (title, authors, dates, DOIs, abstract, versions, BibTeX, PDF hash) | **never by hand** |
| `research/papers/<slug>/paper.pdf` | byte-identical copy of the Zenodo PDF | sync only |
| `_layouts/paper.html` | the landing page | hand |
| `_includes/paper-meta.html` | `citation_*` tags + ScholarlyArticle JSON-LD (paper pages only) | hand |
| `research/papers.md` | `/research/papers/`, the index of all papers | hand |
| `_data/research_publications.yml` | editorial cards on `/research/` (`paper:` links to a generated page) | hand |
| `docs/papers/zenodo_inventory.json` | machine-readable inventory: works, versions, hashes, PDF checks, exclusions, new records | sync only |
| `scripts/validate_papers.py` | compliance and completeness checks (CI and `--live`) | - |
| `docs/papers/SCHOLAR_RECONCILIATION.md` | Zenodo / IRIS / Scholar mapping and the profile to-do list | hand |

## Publishing a new Zenodo paper

1. Publish the paper on Zenodo (open access, CC BY 4.0, one PDF).
2. Run the sync in report mode. A record that is not yet in the gate is
   listed as `NEW` and is **not** published:

   ```bash
   python scripts/sync_zenodo_papers.py --check
   ```

3. Add the concept record id to `_data/paper_sources.yml` with a new kebab-case
   slug (the slug becomes the permanent URL) and a BibTeX key.
4. Run the sync. It selects the latest open version that has exactly one
   PDF, verifies the download against Zenodo's MD5, records the SHA-256,
   checks the PDF (size <= 5 MB, text layer, title and authors on page 1, a
   references section) and writes the page:

   ```bash
   python scripts/sync_zenodo_papers.py
   ```

   Exit code 1 means a `PROBLEM:` line needs attention (wrong licence,
   journal/conference type needing venue review, oversized PDF, ...).
5. Optionally add an editorial card to `_data/research_publications.yml`
   with `paper: <slug>`.
6. Build and validate (WSL has the Ruby toolchain on this machine):

   ```bash
   JEKYLL_ENV=production bundle exec jekyll b -d ~/l3build
   python3 scripts/validate_papers.py --site ~/l3build
   ```

7. Commit and push to `main`. CI builds, runs html-proofer **and**
   `validate_papers.py`, then deploys. A failed check blocks the deploy.
8. After deployment: `python scripts/validate_papers.py --live`, then the
   Scholar profile step in `SCHOLAR_RECONCILIATION.md`.

A new Zenodo version of an existing paper needs only steps 4, 6 and 7. The
sync replaces the PDF and updates the version table and `last_modified_at`.

The sync is idempotent. A second run with nothing new on Zenodo prints
`No changes.` and touches no file, so the sitemap `lastmod` moves only on
real changes.

## The doctoral thesis (not a Zenodo paper)

The thesis lives at `/research/thesis/` and is maintained by hand in
`_data/thesis.yml` from its authoritative record, IRIS Sapienza 11573/1780148.
It is deliberately outside `paper_sources.yml` and the sync script. To update
it, re-read the IRIS page, edit `_data/thesis.yml` (title, abstract, files,
dates), and run the validator. The page never hosts a PDF; it carries
dissertation tags only; it must not claim that a degree was conferred (the
validator checks all three).

## Other tools

| Command | Purpose |
|---------|---------|
| `python3 scripts/validate_papers.py [--site DIR \| --live]` | Scholar compliance for the 13 papers and the thesis |
| `python3 scripts/indexing_report.py [--write]` | Per-item status table (measured plus recorded fields) |
| `python3 scripts/check_overflow.py --site DIR [--all-papers]` | Horizontal overflow at 320 to 1280 px; run before a release. In Git Bash set `MSYS_NO_PATHCONV=1` when passing `--pages /x/` |

Sitemap `lastmod` comes from git history (`_plugins/pages-lastmod-hook.rb`),
so it moves only when a page's source changes. A generated paper page carries
its own `last_modified_at`.

## Metadata decisions

- `citation_doi` and every DOI button use the **concept** DOI. It always
  resolves to the latest version and it is the DOI the IRIS Sapienza records
  carry, so the Zenodo, IRIS and site representations share one identifier.
  The version DOI of the hosted PDF is shown on the page and in the version
  table.
- `citation_publication_date` is the Zenodo publication date of the hosted
  version. `citation_online_date` is its Zenodo deposit date. The first
  public version's date is shown on the page.
- No `citation_journal_title`, `citation_conference_title` or
  `citation_technical_report_institution`: none of these works has a
  verified venue or issuing institution. The validator fails if one appears.
- Every page is self-canonical (jekyll-seo-tag). It is not canonicalised to
  Zenodo: the page must stay eligible for Google Search in its own right,
  and the DOI relation is carried by `citation_doi`, the JSON-LD `sameAs`
  and the visible links.
- The abstract is the Zenodo description, unchanged. HTML is reduced to a
  small whitelist; plain text is split into paragraphs. It is visible in the
  initial HTML and not inside `<details>`.

## Monitoring (repeat after the crawler has had time, about 2 to 6 weeks)

1. `python scripts/validate_papers.py --live`: everything deployed and compliant.
2. Search Console -> Pages / URL inspection for `/research/papers/<slug>/`:
   Google Search indexing (`GOOGLE_SEARCH_INDEXED`). This is **not** evidence
   of Scholar inclusion.
3. In a normal browser, search Google Scholar for the exact title in quotes.
   If the result lists `l3ragio.github.io` among its versions ("All N
   versions"), record `SCHOLAR_INDEXED` and `SCHOLAR_GITHUB_VERSION_RECOGNIZED`
   in `SCHOLAR_RECONCILIATION.md`. Do not script Scholar searches: Scholar
   serves a bot-verification challenge to automated requests.
4. In the Scholar profile, add newly indexed works from "Add articles"
   instead of creating manual entries (see `SCHOLAR_RECONCILIATION.md`).
