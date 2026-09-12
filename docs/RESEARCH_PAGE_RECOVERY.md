# Research Page Recovery

Internal research architecture and claim-audit note. This file is under
`docs/`, which is excluded from the Jekyll build.

## Public Evidence Inspected

Local public posts:

- `_posts/2026-05-07-to-be-or-to-game.md`
- `_posts/2026-05-07-does-safe-ai-equal-safe-world.md`
- `_posts/2026-05-09-misalignment-by-reaction.md`
- `_posts/2026-05-19-uno_nessuno_centomila_e_tutti.md`

Local drafts and internal notes were inspected for source recovery but
are not exposed directly:

- `_drafts/2026-05-27-kipling-if-as-ltl.md`
- `_drafts/2026-05-19-the-mask-is-the-person.md`
- `docs/KIPLING_ZENODO_PAPER_PLAN.md`
- `docs/MASK_POST_FOLLOWUP.md`
- `docs/PCIE_REI_ARTICLE_IDEA.md`

Zenodo records were verified through the Zenodo API on 2026-08-26.

## Publication Classification

Core to this research page:

- `10.5281/zenodo.22066362` - When Can an Agent Attribute Properties to
  Itself? A Cognitive Algebra for Identity, Integrity, and Freedom.
- `10.5281/zenodo.22017443` - MCK Region Transitions: Restricted
  Realization Mechanisms and Their Limits.
- `10.5281/zenodo.22016203` - Meaning, Opacity, and Function: An
  Observer-Relative Classification of Artifacts.
- `10.5281/zenodo.21099448` - The Intersection Algebra of Safety,
  Cosafety, Liveness, and Coliveness over Linear Temporal Logic.
- `10.5281/zenodo.21701303` - Observation-Relative Monitorability of
  Bounded Temporal Implication.
- `10.5281/zenodo.21701310` - Controlling the Observation Class of a
  Runtime Monitor.
- `10.5281/zenodo.22028019` - Refinement-Based Confirmation of Liveness
  Properties from Monitor Verdict Traces.
- `10.5281/zenodo.22050706` - A Typed Agent Action Framework with
  Prefix-Verdict Semantics.
- `10.5281/zenodo.22050701` - Recognising Before Reacting: Temporal
  Signatures of Transactional Games.

Adjacent/background:

- `10.5281/zenodo.22062805` - Intentional Semantic Geometry.
- `10.5281/zenodo.21270850` - One Number Per Cell.

Excluded from the rendered page:

- Restricted/no-file and superseded records such as
  `10.5281/zenodo.21078491` and `10.5281/zenodo.20155196`.
- The suspicious 1979-dated record `10.5281/zenodo.20173418`, because it
  does not help explain the current public research program.
- Adjacent/background outputs that would make the page too broad for a
  2-4 minute reader.

## Research-Line Matrix

| Line | Research question | Formal object | Method | Current evidence | Public output | Next experiment/status |
|---|---|---|---|---|---|---|
| MCK Properties | Which properties of an agent or artifact can be represented, evaluated, and self-attributed relative to an observer? | MCK regions; two-layer agent state; property signatures for continuity, viability, owned branching. | Observer-relative classification, region-transition analysis, finite decision procedures, checker suites. | Multiple Zenodo preprints, including MCK foundations, restricted realization mechanisms, and cognitive algebra. | DOIs 22016203, 22017443, 22066362. | Preprint cluster; no peer-review acceptance claimed. |
| LTL / property-class evaluation | What can finite observation prefixes justify about temporal claims over traces? | Omega-regular LTL properties; safety, cosafety, liveness, coliveness; verdict alphabets; observation models. | Runtime verification, monitorability analysis, prefix-verdict semantics, refinement confirmation. | Zenodo working paper and preprints. | DOIs 21099448, 21701303, 21701310, 22028019, 22050706. | Active formal-methods line with working paper/preprints. |
| Drama / role-transition dynamics | Can role traces in transactional games be monitored before reactive failure becomes locked in? | Karpman-projected role traces; finite-trace LTL properties; antithesis window; agent-property formulae. | Finite-trace LTL, transactional-game corpus formalisation, property classification. | Zenodo preprint on transactional games plus public essay on reward disruption and governance. | DOI 22050701; blog post `Misalignment by Reaction`. | "Drama to Empowerment" remains active research framing; no public publication under that exact title found. |

## Dependency Assessment

The dependency chain is supported in a partial but useful form:

1. MCK supplies the observer-relative vocabulary for meaning, opacity,
   function, and agent property attribution.
2. LTL/property-class work supplies the temporal and monitorability
   vocabulary for deciding what finite traces can justify.
3. Transactional-game and governance work uses role traces and temporal
   properties to study reactive multi-agent patterns.

The exact phrase "MCK Properties -> LTL Triangles -> Drama to
Empowerment" is not a publication taxonomy. It is best rendered as a
public research program:

Properties -> Temporal evidence -> Role transitions.

## Claim Discipline

- Published/preprint facts may cite titles, authors, dates, DOIs,
  resource types, and abstracts from Zenodo.
- Formal results are attributed only when Zenodo metadata says the paper
  proves or establishes them.
- "LTL Triangles" is described as a project shorthand/testbed, not as a
  publication title.
- "Drama to Empowerment" is described as active research extending the
  transactional-role testbed toward recovery/transition dynamics.
- No BlueDot funding outcome is mentioned.
- No private or internal repository content is linked.
- No institutional affiliation is invented beyond what public Zenodo
  metadata already displays inside Zenodo itself; the page itself does
  not add an affiliation label for Davide.

## v2 Timeline Note

The v2 page adds a structured progress timeline from
`_data/research_timeline.yml`, rendered by
`_includes/research_timeline.html`. Achieved milestones require public
evidence. Current, next, planned, and exploratory milestones are allowed
without a completed-result URL, but must be visibly distinct from
achieved milestones and must not imply grant funding or completed
experiments.

See `docs/RESEARCH_TIMELINE_V2.md` for the provenance table, status
audit, and update instructions.

## v3 Publication And Project Controls

The v3 page adds data-driven publication and project components:

- `_data/research_publications.yml`
- `_data/research_projects.yml`
- `_includes/research_publications.html`
- `_includes/research_projects.html`

Publications now expose DOI, PDF, ABS, and CITE controls where verified
metadata exists. ABS uses source-grounded summaries derived from Zenodo
metadata rather than private drafts. CITE uses explicit BibTeX blocks.

Project cards now expose meaningful controls only where resources exist:
details, papers, notes, and progress. No CODE buttons are shown because no
exact public project-specific code repository was found for the current
research lines.

The LTL Triangles public dossier now lives at `/research/ltl-triangles/` and
retains the validated experimental design: 36 core conditions, adaptive
replication of approximately 8-12 seeded rollouts per condition, and a rough
300-500 rollout envelope. The overview at `/research/` links this downstream
testbed to the upstream ChronoSpec dossier at `/research/chronospec/`. Neither
page presents a grant as awarded or publishes a grant amount.

See `docs/RESEARCH_PAGE_V3.md` for the data model and update workflow.
