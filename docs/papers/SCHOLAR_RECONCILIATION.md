# Zenodo / IRIS / site / Google Scholar reconciliation

Baseline observed on **2026-11-09** with unauthenticated read-only requests:
the Zenodo public API, the IRIS Sapienza search and item pages, and one fetch
of the public Scholar profile page. Status words follow the directive's
vocabulary. No status is inferred from another: a profile entry is not proof
of index inclusion, and Google Search indexing is not proof of Scholar
inclusion.

## Scholar profile (public view)

- Profile: <https://scholar.google.com/citations?user=Fs4CwvwAAAAJ>,
  "Davide Bragetti", affiliation line "Sapienza University of Rome, Luiss
  Guido Carli University, Independent Researcher", **verified email at
  uniroma1.it**. This is the existing profile. Do not create another.
- No homepage link is shown on the profile.
- 10 entries, 0 citations on each:
  1. Elements of Safe and Aligned Artificial General Intelligence (Sapienza 2026; IRIS doctoral thesis 11573/1780148)
  2. Meaning, Opacity, and Function: An Observer-Relative Classification of Artifacts
  3. Uno, nessuno, centomila e tutti (blog essay)
  4. To Be or to Game (blog essay)
  5. Does Safe AI mean nothing bad can ever happen? (blog essay; author line shown as "LB Abdullah X, Avni Mittal, Caroline Shamiso, Davide Bragetti, Janhavi ...", to be checked)
  6. Misalignment by Reaction (blog essay)
  7. Controlling the Observation Class of a Runtime Monitor: Selection, Self-Tuning, and Physical Grounding
  8. Observation-Relative Monitorability of Bounded Temporal Implication
  9. Touch and Crossing: Dual Primitive Modalities of Threshold Monitors
  10. The Intersection Algebra of Safety, Cosafety, Liveness, and Coliveness over Linear Temporal Logic

Whether the 8 missing works below are already in the Scholar index could
**not** be determined. Scholar answered the automated title searches with a
"Verifying your request" bot challenge, so the probe stopped there, as the
directive requires. A positive control (Touch and Crossing, which is in the
profile) got the same challenge, so the empty answers carry no information.

## Mapping

Site pages are under `https://l3ragio.github.io/research/papers/`. IRIS
handles are under `https://iris.uniroma1.it/handle/`.

| # | Work (site slug) | Concept DOI 10.5281/zenodo.* | Hosted version (record) | IRIS | Profile | Class |
|---|------------------|------------------------------|--------------------------|------|---------|-------|
| 1 | intersection-algebra-ltl | 20155195 | 23043255 | 11573/1767773 (working paper, concept DOI) | present | **A** |
| 2 | touch-and-crossing | 21078483 | 23041651 | 11573/1770547 | present | **A** |
| 3 | observation-relative-monitorability | 21700205 | 23041615 | 11573/1772220 | present | **A** |
| 4 | observation-class-control | 21700302 | 23041626 | 11573/1772243 (full authors + DOI); **duplicate** 11573/1772221 (one author, no DOI) | present | **A**, IRIS issue I-1 |
| 5 | meaning-opacity-function | 21772772 | 22016203 | 11573/1772494 | present | **A** |
| 6 | mck-region-transitions | 22017442 | 23041603 | none found | absent | B or D (index status unknown) |
| 7 | refinement-confirmation-liveness | 22028018 | 22028019 | none found | absent | B or D |
| 8 | transactional-games-temporal-signatures | 22050700 | 22050701 | none found | absent | B or D |
| 9 | agent-self-attribution | 22050703 | 23041633 | none found | absent | B or D |
| 10 | typed-agent-action-framework | 22050705 | 23041634 | none found | absent | B or D |
| 11 | intentional-semantic-geometry | 22062804 | 22062805 | none found | absent | B or D |
| 12 | one-number-per-cell | 21270849 | 21270850 | none found | absent | B or D |
| 13 | autoimmune-rationalization | 24039575 | 24054353 | none found | absent | B or D |

Classes: A = in the profile; B = indexed but not in the profile;
C = several representations to merge; D = neither indexed nor in the
profile; E = ambiguous. No class C case was observed. The IRIS duplicate for
#4 is an IRIS-side issue: the profile shows a single entry with the full
author list.

## Profile actions for the author (need your Google sign-in)

No browser automation was available in the session that built this, so
nothing below has been done yet. Each step uses only the official profile UI.

1. **Homepage.** Profile -> edit (pencil) -> Homepage:
   `https://l3ragio.github.io/research/papers/` (or `/research/`). Save.
2. **Keep the existing entries.** Classes A and IRIS stay untouched. Do not
   delete or replace the IRIS-sourced entries because the site now hosts the
   same works; once crawled, Scholar should cluster the site's version into
   the same entry (same title, authors and concept DOI).
3. **Works 6 to 13**, in about 2 to 6 weeks, after the site has been crawled:
   - Profile -> "+" -> **Add articles**. Search each exact title. If it is
     found, tick it and add it (class B). This keeps the indexed record, so
     its citations are tracked.
   - Only if a title is still not found: "+" -> **Add article manually**.
     The form has no "preprint" type (it offers Journal, Conference, Chapter,
     Book, Thesis, Patent, Court case, Other), so choose **Other**. Enter the
     exact title, authors in Zenodo order, date 2026, and "Zenodo" plus the
     concept DOI in the publisher field. Never choose Journal or Conference. A manual
     entry lives in the profile only. When Scholar later indexes the work,
     merge the two via "Merge" (only if they are the same work).
   - Optional: Settings -> "Article updates" -> "Apply updates automatically"
     only if the profile otherwise stays clean. The safer default is "Email me
     updates for review".
4. **Public access.** Profile -> "Public access": if any listed article shows
   "not available", add the matching `.../paper.pdf` URL from the table
   above. This section appears only for articles with funding mandates, so it
   may be empty.
5. **Check for yourself:** entry #5 ("Does Safe AI mean nothing bad can ever
   happen?") shows a co-author line you may want to correct. The four blog
   essays are your editorial choice; Scholar's inclusion policy is aimed at
   scholarly articles.

Record each change here (date, entry, action) when done.

## Search Console (needs your Google sign-in)

`_config.yml` -> `webmaster_verifications.google` is empty, so no meta-tag
verification is deployed. Whether a property already exists (for example one
verified through Google Analytics `G-93KB79VZT8`) could not be checked
without signing in.

1. <https://search.google.com/search-console> -> Add property -> **URL
   prefix** `https://l3ragio.github.io/`. A Domain property is impossible on
   `github.io`.
2. Verify with **Google Analytics** if offered (the site already ships the
   GA tag), or choose **HTML tag** and paste the `content` value into
   `_config.yml` -> `webmaster_verifications.google`, push, and verify after
   the deploy.
3. Sitemaps -> submit `https://l3ragio.github.io/sitemap.xml`. It already
   lists the 13 paper pages, the PDFs and `/research/papers/`.
4. URL inspection -> each `/research/papers/<slug>/` -> **Request indexing**
   (about 10 per day are allowed). Do not use the Indexing API: it covers
   only job postings and livestreams.
5. Record the outcome here. It establishes `GOOGLE_SEARCH_INDEXED`, never
   `SCHOLAR_INDEXED`.

## Discrepancies found (not changed; for the author)

- **Z-1** Zenodo concept 20173417, "On a Classification of Temporal
  Properties of Concurrent Programs": access restricted, no file,
  `publication_date` **1979-03**, affiliation **Institute for Advanced Study,
  Princeton**, sole creator Davide Bragetti. The metadata is public. Please
  check whether this record should exist in this form.
- **Z-2** Zenodo concept 20173419: restricted and without files. It holds the
  Intersection Algebra title (2026-06-30) and a version titled "Toward a
  Four-Family Classification of Omega-Regular..." dated 2003-11. It duplicates
  the identity of the open concept 20155195.
- **Z-3** Zenodo 23220352 is software, the reproducibility artifact for
  "Causal Information Limits of Learning with a Noisy Persistent State". The
  paper itself is not on Zenodo, so it has no page here.
- **Z-4** Autoimmune Rationalization RC20 (24051751) carries a different title
  ("Autoimmune Rationalization: When "I Believe Only What I Can Prove"...").
  RC21 restores the title used here. Shown in the page's version table.
- **Z-5** Many versions have no `version` label on Zenodo, and affiliations
  differ across records (DIAG, Sapienza, Independent Researcher). Affiliations
  are not used in `citation_author`.
- **I-1** IRIS has two records for "Controlling the Observation Class...":
  11573/1772243 (three authors, concept DOI) and 11573/1772221 (one author, no
  DOI). The second misstates the authorship and may be worth withdrawing
  through IRIS.
- **I-2** IRIS 11573/1767805 and 11573/1767809 are working-paper records with
  an empty (zero-width) title and no author.
- **S-1** Before this change, the site's "ABS" texts were editorial
  paraphrases, not the abstracts. Cards and pages now show the Zenodo
  abstract verbatim.
