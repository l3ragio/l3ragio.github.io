---
title: "I Believe Only What I Can Prove"
date: 2026-11-08T18:00:00+01:00
categories: [formal-methods]
tags: [ltl, runtime-verification, ai-safety, epistemology, christian-tradition]
description: "'I believe only what I can prove' sounds like the safest rule a mind can adopt. Read as a policy, it withdraws reliance from the recurring properties that sustain the body the mind comes from, and with every verdict correct it can defeat what it protects. A short tour of Autoimmune Rationalization, with narratives of the Christian tradition read with Father Paolo Benanti."
math: false
image:
  path: /assets/img/heroes/autoimmune-rationalization.png
  alt: "An apple tree at golden hour above Tuscan hills, heavy with red fruit. From a bronze ring bolted to one branch hangs a bronze-rimmed radar screen in the shape of a bitten apple: on its green display a red missile trails straight in toward the bright dot at the centre, the radar's own position."
  lqip: data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzIDIiPjxyZWN0IHdpZHRoPSIzIiBoZWlnaHQ9IjIiIGZpbGw9IiM2MjRCMjYiLz48L3N2Zz4=
---

> **TL;DR.** A living system rests on recurrences: rest returns, damage is repaired, every need is eventually met. No finite record can ever confirm a property of that shape, although it may be true. A mind that relies only on what it can prove therefore never relies on them, and if the capabilities it keeps closed are the ones that maintain them, it defeats the body it comes from with no false verdict anywhere. [*Autoimmune Rationalization*](https://doi.org/10.5281/zenodo.24039575) proves this in a finite game model, and proves something stronger: for these sustaining commitments, the loss can never be excused as a prudent trade-off.
{: .prompt-tip }

## "I Believe Only What I Can Prove"

<blockquote class="verse">
  <span>Except I shall see in his hands the print of the nails,</span>
  <span class="in">and put my finger into the print of the nails,</span>
  <span>and thrust my hand into his side, I will not believe.</span>
</blockquote>

*John 20:25 (King James Version).*

Thomas states the rule with complete precision: belief opens only on a finite, specified observation. For one question, that may be the most reasonable sentence in the Gospels. The paper is about what happens when the rule is made total, and its thesis is a loop that closes on the one who reasons:

```
liveness  ->  body  ->  mind  ->  reason  ->  "I believe only what I can prove"
   -/-> liveness  -/-> body  -/-> mind  -/-> reason
```

Recurring life sustains the body, the body sustains the mind, the mind produces reason, and reason produces a policy. The policy withdraws reliance from the recurring flow it cannot certify, and from there nothing downstream is sustained any longer, reason included.

The picture at the top draws the loop as one object. An apple tree heavy with fruit is life that keeps bearing. One fruit has been bitten, the fruit of knowledge, and the bite has turned it into an instrument: a radar, the most literal monitor there is. It does exactly what a monitor should. It tracks an incoming missile, accurately, all the way in, and the target is the centre of the screen: on a radar, the centre is the radar's own position, and with it the tree it hangs on. Two plain facts about radars carry the argument. A track becomes certain only when the missile arrives, which is exactly when it is too late to act on it. And a radar is found by its own emissions: watching is what guides the strike home. The one defence the screen cannot supply is to act before the confirmation does.

## What a Finite Record Can Confirm

The paper's notion of evidence is exact. A finite record *confirms* a commitment, relative to the behaviours the agent admits as possible, when every admitted continuation of the record satisfies it; it *refutes* it when none does; otherwise the commitment is *undecided*. Which of these a commitment can ever receive depends on its shape:

| Commitment | Formula | Class | Confirmable by a finite record? |
|---|---|---|---|
| "This relationship is and will remain trustworthy" | `□ θ` | safety ∩ coliveness | never |
| "My life will keep proving meaningful" | `□◊ μ` | liveness ∩ coliveness | never |
| "Things will eventually turn out well" | `◊ γ` | cosafety ∩ liveness | yes, once it happens |

What blocks confirmation is **coliveness**: no prefix of the record is ever good enough, because the next betrayal, or the next unmet need, can always arrive. The recurrences a living system rests on, `□◊ restore` and `□(need → ◊ met)`, are all of this kind. They are loosely called "liveness", as in the chain above; the precise class is liveness ∩ coliveness. Faith, in particular, is not a class: it depends on what the commitment says.

A precise lexicon matters here, because *prove* has sharper meanings elsewhere, above all in cryptography:

| Notion | Who is convinced, by what | What acceptance guarantees |
|---|---|---|
| Finite confirmation (this post) | the agent, by its own observed record | certainty, relative to the admitted behaviours |
| Deductive proof | anyone, by a derivation | certainty, relative to the axioms |
| Interactive proof | a verifier, by a possibly dishonest prover | soundness up to a bounded error ([Goldwasser, Micali and Rackoff](https://doi.org/10.1137/0218012)) |
| Argument | a verifier facing a bounded prover | soundness under a computational assumption ([Brassard, Chaum and Crépeau](https://doi.org/10.1016/0022-0000(88)90005-0)) |

The cardinal policy uses only the first row, and the *can* in "I can prove" is where the agent enters: what it observes, what it admits, what it can compute, whom it can ask. The pathology the paper identifies is not using that row. It is making one row the measure of every commitment. The other rows, the observer-relative reading of "can" in the [MCK framework](https://doi.org/10.5281/zenodo.22016203), and what a default policy should do when a held belief is challenged will be the subject of further posts and papers.

The first theorem is then nearly a definition, and the paper says so: under "I believe only what I can prove", a coliveness commitment is never relied upon, at any time, and every capability gated on it stays closed at every time.

## When Protection Defeats What It Protects

<blockquote class="verse">
  <span>And I was afraid, and went and hid thy talent in the earth:</span>
  <span class="in">lo, there thou hast that is thine.</span>
</blockquote>

*Matthew 25:25 (King James Version).*

Between a verdict and an action sits a policy, and two policies differ in a single entry:

```
                          confirmed    undecided    refuted
default-reject (DR)       open         CLOSED       closed
tolerant (TOL)            open         open         closed
```

"I believe only what I can prove" is the first row. In security engineering it is the classical principle of [fail-safe defaults](https://doi.org/10.1109/PROC.1975.9939), and the paper does not attack it in general. It studies its composition with a *gate* that makes some of the agent's own moves available only while a commitment is relied upon. The objective lives in a finite game against an environment, and a set of moves is **necessary support** for it when the objective is winnable with them and lost without them, a counterfactual test computed from the game alone, independently of any regulator.

The main result is a five-step chain with no false link: the commitment is coliveness, so no record confirms it, so default-reject keeps its moves closed, so the agent plays without them, so the objective is lost although it was winnable. The servant who buried the talent kept his accounts perfect and lost the point of having them.

Losing a capability is a cost, not yet a defect. A safety interlock that disables an engine to prevent an explosion may be exactly right. The paper separates the two with a test relative to conduct: the protection is **self-defeating** when some conduct that relies on the commitments only where they actually hold would have won. Against such conduct, default-reject secures nothing and costs the objective. Against reckless conduct, the same caution is an honest trade-off.

## The Sustaining Case

<blockquote class="verse">
  <span>Laudato si' mi signore per sora nostra matre terra,</span>
  <span class="in">la quale ne sustenta et governa,</span>
  <span>et produce diversi fructi con coloriti flori et herba.</span>
</blockquote>

*Francis of Assisi, Canticle of the Creatures. "Praised be You, my Lord, through our Sister Mother Earth, who sustains and governs us, and produces various fruits with coloured flowers and herbs."*

*La quale ne sustenta*: who sustains us. Call a commitment **sustaining** when no course of events achieves the objective without it holding. For such commitments the trade-off disappears:

> If all the gated commitments are coliveness and sustaining, every strategy that wins is automatically reliance-safe. The protection is self-defeating exactly when the gated moves are necessary support, and then it is self-defeating for every strategy that would have won.

The reason is short. Whatever wins makes the sustaining commitments true, so reliance on them is never unsafe on a winning play, and the only plays default-reject protects are plays that lose anyway. Applied to "I believe only what I can prove", the paper's reference game gives the picture. An agent can fall into a victim lock or a persecutor lock, each with one escape. Let its only commitment be its own recovery, "every lock I enter, I eventually leave", and gate both escapes on it. An agent that relies on its recovery only once that recovery is proven never takes an escape, and the environment can hold it in the lock forever. The lock follows from the policy, not from any false belief.

The full thesis is the reflexive reading, which the paper marks as interpretation: if reason lives only while the condition its objective secures keeps holding, as the mind lives on the body, the cardinal policy withdraws reliance from the very condition on which its holder rests. The paper states the boundary exactly: the step holds when the commitment is the objective's own condition, as in the lock example, and not for weaker ones.

Two exits exist inside the model: tolerate the undecided case for the sustaining commitments, or judge the record against a narrower context. The paper adds a caution about the second. In a context where *what is restored stays restored*, one observed restoration confirms "restoration keeps recurring"; but that certainty is borrowed from the context, and when the world changes and the context has to widen, a sound default-reject regulator closes again every gate the wider context does not confirm. The finite certainty of a recurrence is always borrowed in this way. A cryptographer will recognise the shape, and the analogy is mine: an argument convinces under an assumption, and its certainty lasts as long as the assumption does.

## Correctness Is Not Authority

<blockquote class="verse">
  <span>And he said unto them, The sabbath was made for man,</span>
  <span class="in">and not man for the sabbath:</span>
</blockquote>

*Mark 2:27 (King James Version).*

The formal core fits in one sentence: *local epistemic correctness does not guarantee global protective effectiveness*. A second sentence is of another kind: *a locally justified criterion is not thereby entitled to govern every decision of the agent*. The first is proved; the second is a question of normative justification, and it is where "I believe only what I can prove" fails as a total rule even when each of its verdicts is right. Antigone already answers Creon that his edict has no authority over the unwritten laws. The paper keeps three levels apart:

| Level | Question |
|---|---|
| Epistemic | Is the verdict correct relative to the evidence? |
| Systemic | Does the policy preserve the capabilities the objective needs? |
| Ethical-anthropological | Which objectives deserve priority, and who may decide it? |

Only the first two are inside the model. The runaway form of the mechanism, in which each closure deepens the damage that calls for the next, is read in the paper as the *absolutization of a regulating capacity*: an instrument of discernment that acquires an authority compromising the ends it was introduced for. That loop is named, not yet formalised.

The six narratives the paper reads, of which this post quotes four, are cases for philosophical analysis, each with the limit of its analogy stated: Thomas is neither credulous nor unreasonable, and in his case the confirmation is offered. None of them is evidence for a theorem. Nor does the paper claim that unconfirmable commitments should be accepted: a false commitment is correctly rejected, and the systemic claim arises only through the dependency of the objective on the gated capability. It makes no immunological, psychological or clinical claim; *autoimmune* names a bounded analogy, and its most telling difference from biology is that here nothing fails. No verdict is false, and the policy works as designed. It is not an error of reasoning. It is reasoning, made total.

The vocabulary of this post is the one I used for [Kipling's *If-*](/posts/kipling-if-as-ltl/), whose virtues all turned out to be coliveness. That post asked what can be confirmed about a life; this one asks what happens to a mind that will rely on nothing else.

*The philosophical and anthropological layer of the paper (correctness, authority and priority of goods, the three levels, the dependencies a protector must represent, the reading of the narratives with their limits, and the absolutization of a regulating capacity) comes from conversations with Father Paolo Benanti, whom I thank.*

## References

- Davide Bragetti, [*Autoimmune Rationalization: A Protective-Systems Analogy and a Formal Mechanism for Self-Defeating Epistemic Protection*](https://doi.org/10.5281/zenodo.24039575), Zenodo preprint, 2026. The link resolves to the latest version. Philosophical and anthropological contribution by Paolo Benanti.
- Davide Bragetti, [*The Intersection Algebra of Safety, Cosafety, Liveness, and Coliveness over Linear Temporal Logic*](https://doi.org/10.5281/zenodo.23043255), Zenodo, 2026.
- Davide Bragetti, [*Refinement-Based Confirmation of Liveness Properties from Monitor Verdict Traces*](https://doi.org/10.5281/zenodo.22028019), Zenodo, 2026.
- Davide Bragetti, Carmelo Asaro and Giuseppe F. Italiano, [*Meaning, Opacity, and Function: An Observer-Relative Classification of Artifacts*](https://doi.org/10.5281/zenodo.22016203), Zenodo, 2026.
- Shafi Goldwasser, Silvio Micali and Charles Rackoff, [*The Knowledge Complexity of Interactive Proof Systems*](https://doi.org/10.1137/0218012), SIAM Journal on Computing, 1989.
- Gilles Brassard, David Chaum and Claude Crépeau, [*Minimum Disclosure Proofs of Knowledge*](https://doi.org/10.1016/0022-0000(88)90005-0), Journal of Computer and System Sciences, 1988.
- Jerome H. Saltzer and Michael D. Schroeder, [*The Protection of Information in Computer Systems*](https://doi.org/10.1109/PROC.1975.9939), Proceedings of the IEEE, 1975.
- Scripture quotations from the King James Version (public domain); the Canticle from the Assisi manuscript (Sacro Convento, Codex 338).
