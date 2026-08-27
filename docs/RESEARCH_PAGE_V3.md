# Research Page v3

Internal architecture and QA note for the publication/project controls on
`/research/`. This file is excluded from the Jekyll build.

## Reference Pattern

Sohan Venkatesh's research page was inspected on 2026-08-27. Transferable
patterns:

- publication entries expose compact status, title, authors, venue, ABS,
  CITE, and PDF controls;
- research projects expose concise project descriptions and direct artifact
  links;
- the useful principle is one click from claim to artifact.

No HTML, CSS, colors, spacing, or typography were copied.

## Data Architecture

Publications are defined in `_data/research_publications.yml`.

Relevant fields:

- `id`: stable anchor suffix, rendered as `#pub-<id>`;
- `status`, `year`, `research_line`, `title`, `authors`, `venue`;
- `description`: card summary;
- `abstract`: source-grounded abstract summary derived from Zenodo metadata;
- `doi`, `record`, `pdf`;
- `code` or `project` only when an exact public artifact exists;
- `bibtex`: verified citation block.

Projects are defined in `_data/research_projects.yml`.

Relevant fields:

- `id`: project anchor suffix, rendered as `#project-<id>`;
- `status`, `title`, `question`, `description`, `methods`,
  `current_state`;
- `buttons`: only non-empty, meaningful public links;
- `related_publications`: publication IDs linked through the reusable
  publication component.

Rendering is handled by:

- `_includes/research_projects.html`;
- `_includes/research_publications.html`;
- `_includes/research_timeline.html`.

## Publication QA

Publication metadata was rechecked through Zenodo public records on
2026-08-27. The rendered page includes 9 core/public research outputs:

- 3 MCK Properties papers;
- 5 Temporal Evaluation papers/reports;
- 2 Agent / Triangle Dynamics papers/reports, with `typed-agent-actions`
  shared by Temporal Evaluation and Agent / Triangle Dynamics.

Each displayed publication has DOI, PDF, ABS, and CITE controls. No CODE
button is rendered because no exact public project-specific code repository
was found for these research lines.

## LTL Triangles Public Dossier

The LTL Triangles section was expanded from the current validated grant
package:

- `06_UPDATED_ACTION_PLAN.md`;
- `17_UPDATED_GRANT_ONE_PAGER.md`;
- `22_AIRTABLE_PASTE_READY_ANSWERS.md`.

Public language now uses:

- 36 core experimental conditions;
- adaptive replication, approximately 8-12 independent seeded rollouts per
  condition;
- roughly 300-500 experimental rollouts including a smaller targeted
  adversarial-ablation set.

The page does not mention the grant amount, does not imply funding has been
awarded, and does not expose private application materials.

## Update Workflow

To add a paper:

1. Verify metadata from DOI/Zenodo or the canonical publication page.
2. Add one entry to `_data/research_publications.yml`.
3. Include `code` only if an exact public repository or directory exists.
4. Add the publication ID to a project in `_data/research_projects.yml` if it
   belongs to a research line.
5. Run the Jekyll build and link checks.

To add public code:

1. Confirm the repository/path is public.
2. Add `code: <exact URL>` to the publication or a project button.
3. Do not link generic GitHub profile pages as CODE.

To update project status:

1. Edit `_data/research_projects.yml`.
2. Keep statuses epistemically accurate: `Preprint`, `Working paper`,
   `Active research`, `Experimental design`, or equivalent.
3. Update `_data/research_timeline.yml` only if the change is also a milestone.

## Claim Boundaries

- LTL Triangles is active research/experimental design, not a completed
  benchmark.
- Drama to Empowerment remains active research, not a proved theory.
- Honeypot/decoy is a targeted adversarial ablation, not evidence of intent or
  alignment.
- Formal claims remain abstraction-bound.
- Empirical claims remain tested-model/prompt/horizon-bound.

## Local QA Result

Completed on 2026-08-27 against `http://127.0.0.1:4000/research/`.

- `bundle exec jekyll b`: passed.
- Focused HTML-Proofer on `_site/research/index.html`: passed, 47 internal
  links checked.
- Added DOI/PDF/public artifact links: passed, 19 checked destinations
  returned HTTP 200.
- Desktop 1440 px: document scroll width 1440, no horizontal overflow.
- Tablet 768 px: document scroll width 768, no horizontal overflow.
- Mobile 375 px: document scroll width 375, no horizontal overflow.
- Publication controls: 9 publications, 9 ABS controls, 9 CITE controls, 9
  PDF links, 17 DOI links in generated HTML.
- CODE controls: 0, because no exact public project-specific code repository
  was found.
- Local/private link scan: passed for `localhost`, `127.0.0.1`, `file:///`,
  and `C:/`.

Warnings observed during build were pre-existing: Medium profile fetch 403,
the visual-stories Liquid warning, and Sass `@import` deprecation warnings.
