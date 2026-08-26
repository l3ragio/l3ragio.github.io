# Research Timeline v2

Internal provenance and QA note for the public `/research/` timeline.
This file is under `docs/`, which is excluded from the Jekyll build.

## Timeline Provenance Table

| Date | Research line | Milestone | Status | Evidence | Public? | Confidence |
|---|---|---|---|---|---|---|
| May 2026 | Foundational questions | Framed safety as an evaluation and governance problem | achieved | `To Be or to Game`; `Does Safe AI mean nothing bad can ever happen?`; `Misalignment by Reaction` | yes | high |
| July 2026 | LTL / Property-Class Evaluation | Released the temporal property-class substrate | achieved | `10.5281/zenodo.21099448` | yes | high |
| July 2026 | Observation and monitoring | Defined observation-relative monitorability | achieved | `10.5281/zenodo.21701303`; `10.5281/zenodo.21701310` | yes | high |
| August 2026 | MCK Properties | Formalized observer-relative property attribution | achieved | `10.5281/zenodo.22016203`; `10.5281/zenodo.22017443`; `10.5281/zenodo.22066362` | yes | high |
| August 2026 | Role traces | Published temporal signatures for transactional games | achieved | `10.5281/zenodo.22050701`; `10.5281/zenodo.22050706` | yes | high |
| Now | LTL Triangles / Post-Failure Governance | Freezing the post-failure governance testbed | current | current grant package and public research-page section | partial | medium |
| Next | Experimental validation | Compare recovery protocols across bounded failure regimes | next | grant package experimental contract | not yet | medium |
| Later | Public release | Publish benchmark traces, verdicts, and counterexamples | planned | 16-week execution plan | not yet | medium |
| Research horizon | Drama to Empowerment | Connect role transitions to preserved agent properties | exploratory | public transactional-games preprint plus active research framing | partial | medium |

## Milestone Status Audit

- Achieved entries have public witnesses: DOI records or public posts.
- Current, next, planned, and exploratory entries are visually and
  textually distinct from achieved entries.
- The timeline does not say BlueDot funding exists, and it does not
  expose grant amount, budget, or submission state.
- LTL Triangles is presented as active experimental design, not as a
  completed empirical benchmark.
- Drama to Empowerment remains exploratory/active research framing, not
  a published theorem.

## Files Created/Modified

- Created `_data/research_timeline.yml`.
- Created `_includes/research_timeline.html`.
- Created `docs/RESEARCH_TIMELINE_V2.md`.
- Modified `_tabs/research.md`.
- Modified `_sass/dragetti/_research.scss`.
- Existing import in `assets/css/jekyll-theme-chirpy.scss` is reused.

## Visual QA Result

Completed on 2026-08-27 with local Playwright/Chrome against
`http://127.0.0.1:4000/research/`.

- Desktop 1440 px: passed.
- Tablet 768 px: passed.
- Mobile 375 px: passed.
- Light-mode tablet pass: passed.
- Timeline node alignment: passed.
- Current/next/planned status distinction: passed.
- Horizontal overflow: passed.

Measured widths:

- 1440 px viewport: document scroll width 1440.
- 768 px viewport: document scroll width 768.
- 375 px viewport: document scroll width 375.

## Scientific QA Result

Passed at source level:

- achieved milestones have public witnesses;
- current and future milestones are not described as completed;
- the conceptual map and timeline remain separate;
- publications and essays remain separate.

Post-build checks:

- `bundle exec jekyll b`: passed.
- Focused HTML-Proofer on `_site/research/index.html`: passed, 38
  internal links checked.
- DOI/PDF link verification: passed, 18 Zenodo/DOI URLs returned HTTP
  200.

## Future Update Instructions

To add a milestone, add one entry to `_data/research_timeline.yml` with:

- `status`: one of `achieved`, `current`, `next`, `planned`,
  `exploratory`;
- `date`: a supported month/year or a roadmap label such as `Now`,
  `Next`, `Later`, or `Research horizon`;
- `line`, `title`, `description`;
- optional `evidence` list with `label` and `url`.

To promote `next` to `achieved`, change `status`, replace the roadmap
date with an evidence-supported date, and add at least one public
witness URL. Do not promote a milestone without a DOI, public post,
public repository, released artifact, experiment report, or equivalent
public evidence.
