# Article idea (PARKED): PCIE and REI as a general methodology

**Status: idea capture only.** The user reserved the PCIE / REI
concepts for a dedicated article rather than spending them inside the
Kipling paper. This note records the idea so it is not lost. To be
picked up later.

Excluded from the Jekyll build (`docs` in `_config.yml` exclude).

## The idea in one paragraph

PCIE (Partition with Complementary Excluded Interval) names a
recurring epistemic failure: a binary cut that presents itself as
exhaustive while silently discarding the interval between its poles.
REI (Recomposition via Excluded Interval) names the repair: make the
discarded interval explicit and reinsert it into the analysis. The
article would present PCIE/REI as a *general-purpose methodology* for
auditing arguments, specifications, and policies, with worked examples
drawn from domains where the programme has already applied it
implicitly.

## Worked examples already available (from existing work)

1. **The exhaustion clause in Kipling's If—.** The poetic spec
   `□(Exhausted → Continue)` against the sanity requirement
   `□(Exhausted → Recover)`: absolutised, contradictory. The repair
   splits the trigger by context (duty-critical + recovery-possible
   vs no-immediate-duty-window). The excluded interval is the space
   between courage and self-destruction. (Source: Kipling blog post /
   paper, where it is described in plain language without naming the
   framework.)
2. **Identity capture by triumph/disaster.** The binary
   `Success ⇒ Worthy / Failure ⇒ Unworthy` excludes the middle in
   which events are trace data, not identity verdicts. REI: identity
   as property over the trace. (Same source.)
3. **Self-trust vs others' doubt.** The cut `SelfTrust ∨ OthersRight`
   excludes the recomposed position `SelfTrust ∧ DoubtIntegration`.
   (ChatGPT source seg 55 §3 names this explicitly as anti-PCIE.)
4. **Safety-vs-capability data filtration.** The curative/development
   alignment debate (mask post): "filter the data ∨ accept the risk"
   excludes the developmental middle (exposure + ethical frame).
5. **Finite evidence for infinite-trace properties.** The programme's
   own founding case: claiming infinite-trace conclusions from finite
   witnesses without declaring the excluded interval (REI as the
   declared-decomposition discipline; ties to docs/research-methodology.md
   in the research repo).

## Likely structure (very rough)

1. The pattern: how false binaries form and why they feel exhaustive.
2. PCIE defined; detection heuristics (where to look for the cut).
3. REI defined; repair patterns (context-split, trace-lift,
   third-position recomposition).
4. Worked examples (selection from the list above).
5. Relation to known ideas: false dilemma (informal logic), excluded
   middle (logic), partiality in specification languages, abstraction
   refinement. What PCIE/REI adds: the *temporal/spec-level* reading
   and the repair discipline.
6. Methodological payoff for AI safety specs.

## Open decisions (for when resumed)

- Venue: blog post first or straight to Zenodo working paper?
- Whether to formalise PCIE/REI definitions or keep them
  semi-formal with examples carrying the weight.
- Relationship to `docs/research-methodology.md` in the research
  repo (which already documents REI/PCIE for internal use): the
  article would be the public-facing treatment.

## Provenance

Created 2026-05-27 when the user decided to keep PCIE/REI out of the
Kipling Zenodo paper and reserve them for a dedicated piece. Companion
to `docs/KIPLING_ZENODO_PAPER_PLAN.md` (which records the exclusion).
