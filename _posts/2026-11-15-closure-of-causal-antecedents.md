---
title: "When Is the List of Causes Complete?"
date: 2026-11-15T10:00:00+01:00
categories: [formal-methods]
tags: [causality, epistemology, ltl, ai-safety]
description: "'A is necessary and sufficient for B' is a claim about a classification as much as about the world. A short note on why records can refute the completeness of a list of causes but never establish it, and why a learned causal law inherits the same limit from its representation."
math: false
image:
  path: /assets/img/heroes/closure-of-causal-antecedents.jpg
  alt: "A tornado hurls boulders and splintered timber across a valley at sunset. In the foreground, men carrying giant hammers marked A1, A2, A3 and A4 run for shelter under a stone arch. On a round stone platform a red button marked B is still unpressed: a monarch butterfly with a glowing trail drifts toward it from the left, and a large boulder tumbles toward it from the right."
---

> **TL;DR.** A complete list of an effect's necessary and sufficient conditions holds of the world only if the classification of contexts keeps every distinction that matters to the effect. Records can refute that closure. No finite record establishes it on its own, and a causal law learned from a representation inherits the same limit. [*On the Closure of Causal Antecedents*](https://www.alphaxiv.org/abs/2611.closure-causal-antecedents) is a short note on exactly this, published on alphaXiv and archived on Zenodo ([version 2](https://doi.org/10.5281/zenodo.24538897); [all versions](https://doi.org/10.5281/zenodo.24217158)), with a [paper page](/research/papers/closure-of-causal-antecedents/) on this site that hosts its PDF. Version 2 of the note adds four small diagrams, a polarity corollary and a remark on recovery along a trace. This post is a short tour of it.
{: .prompt-tip }

## The List That Looks Complete

<blockquote class="verse">
  <span>Felix qui potuit rerum cognoscere causas.</span>
</blockquote>

*Virgil, Georgics 2.490: "Happy is he who has been able to know the causes of things."*

A researcher finds the effect B present exactly when A is. Nobody in the records ever saw an alternative route C that also yields B, or a defeater D that withholds it. From the records alone, three hypotheses cannot be told apart:

| Hypothesis | What it says | Fits the records |
|---|---|---|
| `B ↔ A` | A is the whole story | yes |
| `B ↔ A ∨ C` | an alternative route also yields B, so A is not necessary | yes |
| `B ↔ A ∧ ¬D` | a defeater withholds B, so A is not sufficient | yes |

Mackie saw both possibilities. He observed that, provided there is some necessary and sufficient condition, which we commonly assume, the disjunction of all minimal sufficient conditions is necessary and sufficient, and he made causes relative to a "causal field". The note asks what exactly is assumed when a list is called complete, and what a finite record can and cannot do about it.

## Adequacy Belongs to the Classification

Let `π` classify the world's states by conditions `A₁ … Aₙ`. The classification is **adequate** for B if states it does not distinguish never differ in B, that is, `B = f ∘ π` for some law `f`. When it is, the table of `f` lists exactly its minimal sufficient terms (Quine's prime implicants) and minimal necessary clauses (prime implicates), and those hold of the world. But the table is complete for the vocabulary, not for the world: nothing in records stated in the classification shows it adequate, just as the same evidence confirms Goodman's "green" and "grue" equally.

This is not the closed-world assumption. Reiter's assumption completes a database by treating as false what it does not entail. Antecedent closure asserts something stronger about the representation itself: that it omits nothing relevant to B.

## What the Note Proves

In one sentence: necessity and sufficiency remain well defined, but finite observations cannot certify that they hold universally when the admissible representation stays open to unobserved alternative antecedents and defeaters.

Take a condition Z that no record reports and that is free to vary beyond the records. Extend the law in two ways, `f⁺ = f ∨ (Z ∧ t)` and `f⁻ = f ∧ ¬(Z ∧ d)`. If Z was absent in every recorded state, every record agrees with `f`, `f⁺` and `f⁻`. The proposition then says, for a suitable choice of `t` and `d`, that a necessary clause which is false somewhere is not necessary for `f⁺`, and a sufficient term which is true somewhere is not sufficient for `f⁻`, however many states the records cover.

Three consequences, all in the note:

- **One side can be saved by an assumption.** If the fresh conditions can only add routes, the sufficient terms of `f` stay sufficient; if they can only add defeaters, its necessary clauses stay necessary. An observational analogue of monotonicity in VanderWeele and Richardson. But the restriction is assumed, not certified.
- **Admit both and nothing non-trivial is certified** while the fresh conditions stay absent.
- **Refutation needs no closure.** Records showing both outcomes for every configuration refute closure and every non-trivial term and clause. And some conditions survive any openness: under the law `B = A`, A is necessary and sufficient however open the class.

The note is careful about scope: this concerns what records leave open, not causal identification, and it covers experiments that set A but not Z. It also records a small fact worth keeping in mind: under `B = A ⊕ C`, each of A and C suffices alone, yet `A ∧ C` withholds B, so each is a defeater of the other. Over one domain this cannot happen. It happens because each success was relative to a background the other condition removes.

The hidden condition need not be absent. A record reports A and B; it gives an unrecorded condition no value at all. The proposition supposes a *latent completion* of the records, an assignment of values to the unrecorded condition in each recorded state, in which that condition was 0 throughout. Nothing in the records shows that value, and an enabling or constraining background may just as well have held throughout. Version 2 states this as a corollary: if a hidden condition `H` kept a baseline value `h₀` in every recorded state, the proposition holds with `Z` replaced by the departure from that baseline, `δ = H ⊕ h₀`. It is the proposition read without a fixed polarity, not a new theorem.

## The Four Diagrams

The note draws the proposition for the smallest case: one recorded condition A, one effect B, one hidden condition.

![Four Boolean laws that all equal B = A at the baseline of a hidden condition. At the top, the reference law: A points straight to B. Top row, hidden condition Z absent at baseline: (a) B = A or Z, where the state A = 0, Z = 1 gives B = 1, so A is sufficient but not necessary; (b) B = A and not Z, where A = 1, Z = 1 gives B = 0, so A is necessary but not sufficient. Bottom row, hidden condition H present at baseline: (c) B = A or not H, where A = 0, H = 0 gives B = 1; (d) B = A and H, where A = 1, H = 0 gives B = 0. Solid circles are recorded conditions, dashed circles are conditions no record reports, square boxes are the effect, rounded boxes are Boolean operators, and a line ending in a small open circle means the condition is read negated.](/assets/img/posts/closure-of-causal-antecedents/fig1-hidden-baselines.svg){: w="762" h="656" }
_Figure 1 of the note. Each law equals `B = A` at its hidden condition's baseline, so all four fit the same records. Left column: a route refutes the necessity of A. Right column: a defeater refutes its sufficiency. Below each panel, the only state where this happens._

**How to read them.** The notation is small and every mark carries one meaning:

- A **solid circle** is a condition the records report: A. A **dashed circle** is a condition no record reports: Z or H. Dashed means *unmeasured*, not *false*.
- The **square box** is the effect B. A **rounded box** is a Boolean operator: `∨` (or) or `∧` (and).
- An **arrow** into an operator means the law reads that condition as it is. A line ending in a **small open circle** means the law reads its negation, as in the inverting input of a logic gate.
- **Baseline** is the value the hidden condition is assumed to have had in every recorded state. It belongs to a latent completion of the records and is never observed. A baseline of 0 says the condition was false throughout, which is a different thing from being unmeasured.
- The edges say which conditions a law reads. They are not causal arrows, and they say nothing about what an intervention would do. The diagrams depict Boolean laws, not causal graphs: routes and defeaters here are observational Boolean constructions, statements about which values occur together.

**Panel by panel.** The reference at the top is the law `B = A`, under which A is both necessary and sufficient. Every panel below reduces to it at its baseline, so every recorded state fits all five laws, each under its own latent completion.

- **(a) `B = A ∨ Z`, a new route.** At the baseline `Z = 0` the law is `B = A`. The single state `A = 0, Z = 1` gives `B = 1`: the effect without A. A stays sufficient, but it is no longer necessary.
- **(b) `B = A ∧ ¬Z`, a new inhibitor.** At `Z = 0` the law is again `B = A`. The single state `A = 1, Z = 1` gives `B = 0`: A without the effect. A stays necessary, but it is no longer sufficient.
- **(c) `B = A ∨ ¬H`, a constraint lost.** Here the hidden condition held throughout the records, `H = 1`, and kept a route closed. Losing it, `A = 0, H = 0`, opens that route: `B = 1` without A. Necessity fails, as in (a).
- **(d) `B = A ∧ H`, an enabling condition lost.** Again `H = 1` throughout, this time as a background that A needs. Losing it, `A = 1, H = 0`, withholds B despite A. Sufficiency fails, as in (b).

**Why two letters.** `Z` is the proposition's hidden condition, absent throughout the records. `H` is a hidden condition present throughout. The letters mark the polarity of the baseline, not two different mechanisms: with `H = ¬Z`, panel (c) is panel (a) and panel (d) is panel (b), state by state. That is the corollary in its smallest form, and it is why the records cannot tell the rows apart. They fix neither polarity.

| Model | Latent baseline | Counterexample | Property lost |
|---|---|---|---|
| `B = A ∨ Z` | `Z = 0` | `A = 0, Z = 1, B = 1` | necessity |
| `B = A ∧ ¬Z` | `Z = 0` | `A = 1, Z = 1, B = 0` | sufficiency |
| `B = A ∨ ¬H` | `H = 1` | `A = 0, H = 0, B = 1` | necessity |
| `B = A ∧ H` | `H = 1` | `A = 1, H = 0, B = 0` | sufficiency |

Every verdict in the panels is relative to a domain. Over the baseline states alone, A is necessary and sufficient in all four laws. Over the extended domain, which also admits the departure from the baseline, one of the two fails. "A is sufficient" is therefore never a bare statement: it holds or fails over a stated set of admissible states.

The four diagrams are only the smallest instance. The proposition covers any law over any number of recorded conditions: if such extensions are admissible, a necessary clause that is false somewhere is defeated by a route through a hidden condition, and a sufficient term that is true somewhere by a defeater.

## Learned Laws Inherit the Boundary

A learner meets the world through an interface `π` and a hypothesis class `𝓗`. If the interface conflates two states that differ in B, no prediction through it is right on both. If it is adequate but no member of `𝓗` matches `f`, it still fails. And there is a counting limit: a network with `p` parameters of `b` bits and fixed inference has at most `2^(pb)` functions, while `m` binary inputs admit `2^(2^m)` Boolean maps, so when `pb < 2^m` not every map is representable. The count is for finite precision. Memory, tools or retraining change `π` or `𝓗`, and a real-valued threshold gives infinitely many functions. A causal law read from a representation may therefore be complete for its variables and still not for the causal domain.

Identification does happen under assumptions: a finite adequate interface, a finite class containing `f`, correct observations, a stationary law, and members of the class that are eventually told apart. Valiant's model asks for less, and invariant prediction identifies causal predictors when, for instance, each other variable is intervened on singly. The note's point is only that a finite world does not ensure these assumptions.

## The Temporal Reading

Alternative antecedents defeat necessity; defeaters defeat sufficiency; observations that never encounter those conditions cannot establish that they do not exist.

Read the records as an unending sequence of valuations of A and B, with `G` for "always" and `F` for "eventually". The arrow is material implication, a matter of co-occurrence. Over all such sequences:

| Claim | Formula | Class | A finite record |
|---|---|---|---|
| A necessary for B | `G(B → A)` | safety ∩ coliveness | can refute it |
| A sufficient for B | `G(A → B)` | safety ∩ coliveness | can refute it |
| counterexample to necessity | `F(B ∧ ¬A)` | cosafety ∩ liveness | can confirm it |
| counterexample to sufficiency | `F(A ∧ ¬B)` | cosafety ∩ liveness | can confirm it |

Each diagram above produces the refuting continuation. While the hidden condition stays at its baseline, the law's states satisfy both implications; its counterexample state, a departure from the baseline, refutes one of them. Panels (a) and (c) emit `B ∧ ¬A`, panels (b) and (d) emit `A ∧ ¬B`. So a finite record can refute either claim, but it cannot confirm either one when the admissible class stays open to routes and defeaters through hidden conditions.

**Recovery is not restoration.** Version 2 adds a trace to rule out one confusion. Under the law of panel (b), `B = A ∧ ¬Z`, take the states `(A, Z, B) = (1, 1, 0), (1, 0, 1), (1, 0, 1), …`. A is present throughout; the inhibitor acts once and then lapses, and B appears. The first state violates `G(A → B)`, and since that is a safety property nothing later undoes it: global sufficiency stays refuted by the earlier counterexample. What the trace satisfies is `FG(A → B)`, the implication recovered along a suffix, and A is sufficient only relative to the context `Z = 0`. Read with `H = ¬Z`, the same trace under panel (d) shows an enabling condition becoming true: the same Boolean pattern, not necessarily the same physical story. The necessity side is dual: under panel (a), a route that closes again gives `FG(B → A)` while `G(B → A)` stays refuted.

Three cautions from the note. `FG(A → B)` also holds if A simply stops occurring, so a non-vacuous recovery needs an occurrence assumption: `F(A ∧ ¬Z)` for one witness, `GF A` for recurring ones. The assumption that the inhibitor stays away, `FG ¬Z`, is a liveness property of a condition no record reports, so no finite record confirms it. And a recovery along one trace is not antecedent closure, which concerns every admissible extension.

This is the class vocabulary of the [intersection algebra](https://doi.org/10.5281/zenodo.20155195) and of the [previous post](/posts/i-believe-only-what-i-can-prove/): what blocks confirmation is coliveness. The openness condition matters. Without it, confirmation can happen: in the class `{A, A ∨ Z, A ∧ ¬Z}`, one record of B without A leaves only `A ∨ Z`, in which A is sufficient. And guaranteed discovery needs fairness, every producible state eventually appearing. An observed counterexample settles a failure. No run of favourable observations settles closure by itself.

## Reading the Picture

The hammers marked A1 to A4 are the list: the ways someone wrote down for B to be pressed. In the picture the men carrying them are running for shelter. Nobody wrote the storm or the butterfly on the list, and both are on their way to the button.

The frame stops before anything happens, and the records up to it fit every continuation. The butterfly may land on B. A boulder may fall on B with no hammer anywhere near, which is B without A, a route nobody listed. A boulder may crush the butterfly first and then press B itself. Or it may knock a hammer aside in mid-swing, which is A without B, a defeater nobody listed. The list was complete for the court it was written in, and the court has no wall.

## One Reading of Mine

This part is my reading, not a result of the note. A claim that an evaluation, a safety case or a post-mortem has listed all the antecedents of a failure is a closure claim. It can be refuted by one record that shows an unlisted route or defeater. It cannot be certified by the records it was built from, however many they are, unless the classification they are stated in is itself shown adequate, and that is a premise about the world and the representation, not about the data.

## Provenance of the Note

The note grows out of an earlier manuscript from 2017. Its acknowledgements thank Cas Cremers for scientific review and conceptual feedback on that 2017 manuscript. The thanks concern the earlier manuscript, and they say nothing about the present text. The note is posted on alphaXiv, under the author's profile, and archived as a preprint on [Zenodo](https://doi.org/10.5281/zenodo.24217158), whose record also lists Cas Cremers as a non-author contributor, with his consent. It names no venue, and no peer review is claimed here. Version 2 (25 November 2026; Zenodo [doi:10.5281/zenodo.24538897](https://doi.org/10.5281/zenodo.24538897), and the same PDF on [alphaXiv](https://www.alphaxiv.org/abs/2611.closure-causal-antecedents)) adds Figure 1, the polarity corollary and the remark on recovery along a trace; the proposition is unchanged, and version 1 remains available from the Zenodo record.

## References

- Davide Bragetti, [*On the Closure of Causal Antecedents*](https://www.alphaxiv.org/abs/2611.closure-causal-antecedents), note on alphaXiv, 2026 (version 2). Zenodo preprint, version 2: [doi:10.5281/zenodo.24538897](https://doi.org/10.5281/zenodo.24538897); all versions: [doi:10.5281/zenodo.24217158](https://doi.org/10.5281/zenodo.24217158) (the link resolves to the latest version). Paper page with the full text: [/research/papers/closure-of-causal-antecedents/](/research/papers/closure-of-causal-antecedents/). Author profile: [alphaXiv](https://www.alphaxiv.org/@davide-bragetti).
- Davide Bragetti, [*The Intersection Algebra of Safety, Cosafety, Liveness, and Coliveness over Linear Temporal Logic*](https://doi.org/10.5281/zenodo.20155195), Zenodo, 2026. The link resolves to the latest version. Paper page with the full text: [/research/papers/intersection-algebra-ltl/](/research/papers/intersection-algebra-ltl/).
- Davide Bragetti, [*Autoimmune Rationalization: A Protective-Systems Analogy and a Formal Mechanism for Self-Defeating Epistemic Protection*](https://doi.org/10.5281/zenodo.24039575), Zenodo preprint, 2026. Paper page with the full text: [/research/papers/autoimmune-rationalization/](/research/papers/autoimmune-rationalization/).
- The references of the note: Alpern and Schneider, *Defining liveness*, Information Processing Letters 21(4), 1985. Goodman, *Fact, Fiction, and Forecast*, 1955. Mackie, *Causes and conditions*, American Philosophical Quarterly 2(4), 1965. Manna and Pnueli, *A hierarchy of temporal properties*, PODC 1990. McCluskey, *Minimization of Boolean functions*, Bell System Technical Journal 35(6), 1956. Peters, Bühlmann and Meinshausen, *Causal inference by using invariant prediction*, Journal of the Royal Statistical Society B 78(5), 2016. Quine, *The problem of simplifying truth functions*, American Mathematical Monthly 59(8), 1952. Reiter, *On closed world data bases*, Technical Report 77-16, University of British Columbia, 1977. Valiant, *A theory of the learnable*, Communications of the ACM 27(11), 1984. VanderWeele and Richardson, *General theory for interactions in sufficient cause models with dichotomous exposures*, Annals of Statistics 40(4), 2012.
