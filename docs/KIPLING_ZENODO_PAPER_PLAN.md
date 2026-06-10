# Zenodo paper idea (PARKED): Temporal Properties of Moral Resilience

**Status: idea capture, not an active writing plan.** The user will
pick this up later. Nothing here is scheduled; the structure below
records the shape the article would take so the thinking is not lost.

Derived from the blog post `_drafts/2026-05-27-kipling-if-as-ltl.md`
and the ChatGPT source dump `docs/KIPLING_POST_CHATGPT_SOURCE.md`
(60 segments).

Excluded from the Jekyll build (`docs` in `_config.yml` exclude).

## Scope decisions (user-confirmed)

- **If— only.** The comparative material on Invictus, Desiderata,
  Ulysses (source segment 57) is OUT of scope. Reserved for a possible
  separate piece later; not referenced in this paper beyond, at most,
  a one-line remark in the conclusion.
- **No PCIE / REI lexicon.** The excluded-interval methodology
  (Partition with Complementary Excluded Interval, Recomposition via
  Excluded Interval) is deliberately NOT named or used in this paper.
  Those concepts are reserved for a dedicated methodological article
  (see `docs/PCIE_REI_ARTICLE_IDEA.md`). Where the Kipling analysis
  needs the underlying move (the exhaustion repair, the
  triumph/disaster identity capture), it is described in plain
  language: "false binary that hides an excluded middle",
  "reinserting the excluded interval", without naming the framework.
- **Venue**: Zenodo, working paper (same channel as Bragetti 2026).
- **Language**: English.
- **Positioning**: methodological case study. The contribution is the
  *method* (property-class analysis of an informal ethical
  specification) demonstrated on one canonical text, not literary
  criticism of Kipling. Title and abstract must reflect this.
- **Dependency**: cites Bragetti 2026 (Intersection Algebra) as the
  property-class foundation. **Gated on the v2 Zenodo upload** (2019
  prior-art reconciliation), consistent with the deploy-preconditions
  policy in the BlueDot integration map. The paper should cite the v2
  version-DOI.
- **DAG status**: dissemination artifact tied to `ltl_classes`; NOT
  registered as a new paper node in the research dependency graph
  (leaf node, no downstream dependents; P4 considerations).

## Candidate title

*Temporal Properties of Moral Resilience: Reading Kipling's "If—" as
a Linear Temporal Logic Specification*

## Target length

8,000–10,000 words + two appendices.

## Structure

1. **Introduction**
   - The poem as informal spec; thesis: maturity as a trace property;
     contribution list (method, clause taxonomy, automaton, coined
     properties, the inconsistency-and-repair result).
2. **Preliminaries**
   - LTL syntax/semantics (minimal); safety / cosafety / liveness /
     coliveness with finite-witness characterisations; the
     intersection algebra (cite Bragetti 2026 v2). No PCIE/REI
     (reserved, see scope decisions).
3. **The poem as a conditional over traces**
   - Global form `(⋀ᵢ □φᵢ) → ◊Maturity`; Maturity = Property(trace);
     the moral automaton; **maturity as an acceptance condition of an
     ω-automaton** (Büchi sketch) — the paper's main technical novelty
     over the blog post.
4. **Clause-by-clause analysis** (the bulk; poem order)
   - 4.1 Keep your head → procedural meta-safety, temporal buffer
     (source segs 54, 55, 56)
   - 4.2 Trust yourself / allowance for doubt → epistemic hospitality
     (segs 50, 51, 52, 53)
   - 4.3 Wait and not be tired by waiting → PatientAction ∧
     PatientSpirit; waiting as orchestral reallocation (segs 2, 55)
   - 4.4 Being lied about, don't deal in lies → Byzantine moral
     resilience (seg 55 §5)
   - 4.5 Being hated, don't give way to hating → state vs action;
     maximalist spec (seg 55 §6)
   - 4.6 Don't look too good nor talk too wise → check segs 43–49 for
     coverage; likely modesty-as-non-signalling property [VERIFY]
   - 4.7 Dream / think clauses → internal attractors; dreams as
     cosafety/liveness targets; constrained optimisation; internal
     reward hacking; dream plasticity (segs 38, 39, 40, 41, 42)
   - 4.8 Triumph and Disaster → identity capture as false binary;
     trace-level recomposition (segs 21, 55 §8)
   - 4.9 Truth twisted by knaves → MCK; semantintegrity (segs 55 §9,
     45–48)
   - 4.10 Watch things broken, stoop and rebuild → liveness;
     `□(Loss → (¬CorruptSelfNarrative U Restart))` (segs 30, 31, 29)
   - 4.11 Pitch-and-toss → identity independence from winnings;
     achievements as witnesses; paradoxical finite confirmation
     (segs 21, 23, 24, 26)
   - 4.12 Never breathe a word about your loss → anti-complacency;
     risk intelligence vs fear rhetoric; loss-speech reward check
     (segs 19, 20, 28)
   - 4.13 Force heart and nerve and sinew → THE INCONSISTENCY:
     P₁ = □(Exhaustion→Continue) vs P₂ = □(Exhaustion→Recover);
     hidden excluded interval between courage and self-destruction;
     repair via context-split triggers (segs 32, 33, 34, 55 §11)
   - 4.14 Talk with crowds / walk with Kings → contextual invariance;
     two operating regimes, not two intensities (segs 11, 12, 13, 14)
   - 4.15 Foes and loving friends → bounded relational exposure;
     friend↔foe transitions; node-failure reading (segs 6, 7, 8, 9)
   - 4.16 All men count, none too much → weight bounds
     0 < Weight(p) < 1 (segs 5, 10)
   - 4.17 The unforgiving minute → temporal density; decisive
     interval; safety + local cosafety; pairing with the waiting
     clause (segs 2, 15, 16, 55 §15)
   - 4.18 Yours is the Earth / you'll be a Man → inhabitability not
     ownership; ◊FullAgenthood (segs 1, 3, 4)
5. **The property taxonomy applied**
   - Full classification table; distribution across the four classes;
     what the distribution reveals about the specification style
     (safety-heavy with load-bearing liveness at exactly the recovery
     points).
6. **Trace-sovereignty: the unifying property**
   - The capture table (15 capturers); mother formula
     `□(ExternalCaptureAttempt → AgencyPreserved)`; formal definitions
     of the coined properties: trace-sovereignty, semantintegrity,
     epistemic hospitality, bounded relational exposure, procedural
     meta-safety.
7. **The dangerous reading: inconsistency and repair**
   - The exhaustion contradiction as a genuine spec inconsistency;
     excluded intervals; the methodological claim: formal analysis as
     safety work on ethical texts (the analysis *protects readers*
     from the self-erasure reading).
8. **Implications for AI alignment** (compact)
   - Capture taxonomy ↔ agentic failure modes (jailbreaks, sycophancy,
     reward disruption, internal reward hacking, deceptive
     optimisation); trace-sovereignty as an alignment desideratum;
     link to the persona/mask post's open question #3 (property
     classes ↔ mask-coupling claims).
9. **Related work**
   - Temporal logic in normative/deontic systems; formal narrative
     analysis; runtime verification of behavioural policies; (light)
     Kipling context. [NEEDS literature retrieval via MCP — H9: no
     fabricated citations.]
10. **Conclusion**
- **Appendix A**: complete formula inventory (every clause, naive and
  refined forms side by side).
- **Appendix B**: the moral automaton, formal definition (states,
  alphabet, transitions, acceptance).

## What must be written ex novo (not in blog post or source dump)

1. Preliminaries section (§2) — standard but must be written.
2. The Büchi/ω-automaton formalisation (§3) — sketched nowhere yet;
   main new technical content.
3. §4.6 (look too good / talk too wise) — verify source coverage.
4. Distribution analysis in §5 (the "specification style" remark).
5. Related work (§9) — requires literature retrieval (MCP, H9).
6. Abstract + contribution list.

## Effort estimate (for when this is resumed)

- Skeleton → full draft: 2–3 working sessions.
- Related-work retrieval: 1 session (MCP / Semantic Scholar).
- LaTeX port + Zenodo metadata: 0.5 session.
- **Blocking precondition**: Bragetti 2026 v2 upload (the paper cites
  the v2 DOI). Do not finalise citations before v2 exists.

## Relationship to the blog post

The blog post (`2026-05-27-kipling-if-as-ltl.md`, in drafts) is the
divulgative companion: shorter, selective, no programme lexicon, no
automaton formalisation. On publication both link to each other
(post cites DOI; paper cites post URL as companion). The post is NOT
gated on the paper; it can ship first.
