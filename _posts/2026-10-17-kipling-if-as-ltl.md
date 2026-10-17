---
title: "Kipling's If— as Linear Temporal Logic"
date: 2026-10-17T10:00:00+02:00
categories: [formal-methods]
tags: [ltl, runtime-verification, ai-safety, alignment, literature]
description: "Read as a specification, Kipling's If— is a set of temporal invariants and response policies for an agent that keeps its agency under pressure. Classified by what a finite observation can settle, its virtues turn out to be refutable but never confirmable, its recoveries beyond any observer's verdict, and only its reward confirmable."
math: false
image:
  path: /assets/img/heroes/kipling-if-as-ltl.png
  alt: "First-person view at sunrise: a man's weathered forearms in leather wristbands hold a worn hammer and chisel, rebuilding a dry-stone wall that is scorched and smouldering on the left and freshly set on the right, with a brass hourglass among the stones. Beyond him a single road winds through the valley without changing course: past an agitated market crowd, across a stone bridge where a lone traveller walks on, through a royal pavilion with banners and courtiers, past a burnt workshop being rebuilt under scaffolding, up to a lone figure on a hilltop against the sun. At the left edge one man raises a fist while another opens his arms in welcome; on the right a pair of scales hangs from an oak branch, gold coins in one pan and ashes in the other."
  lqip: data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzIDIiPjxyZWN0IHdpZHRoPSIzIiBoZWlnaHQ9IjIiIGZpbGw9IiM3QzVFNDQiLz48L3N2Zz4=
---

> **TL;DR.** *If—* is usually read as motivational verse. Read structurally, it is an informal Linear Temporal Logic specification: its antecedents are not facts but invariants and response policies, and its reward is a property of a whole life, not of a moment. Classify each clause by what a finite stretch of life can settle about it, and a pattern appears: the poem's virtues can be refuted by a single moment but never confirmed, its recoveries can be neither refuted nor confirmed by any observer, and only its reward can be confirmed. The exhaustion stanza is the one place where the spec contradicts itself and needs repair. The mature agent is trace-sovereign: defined not by any event, but by the policy that holds across events.
{: .prompt-tip }

## A Poem as a Specification

Kipling's *If—* is usually read as moral encouragement, a Victorian list of virtues to cultivate. That reading is not wrong, but it misses a structural fact worth taking seriously. *If—* is a single long conditional, and what sits on the antecedent side is not a set of facts but a set of *temporal invariants and response policies*. The reward (the man at the end) is what falls out when an agent satisfies the entire specification across its life.

If the poem is not fresh in your ear, it is worth hearing whole before it is taken apart. Michael Caine's reading is unhurried enough to let the conditional structure show: every stanza opens another *if*, and the main clause is held back until the last two lines.

{% include embed/youtube.html id='EEFMVIfl2UY' %}

*[If—, recited by Sir Michael Caine](https://www.youtube.com/watch?v=EEFMVIfl2UY) (YouTube).*

This is the grammar of formal methods: a behaviour, a regime, a property over the trace of an agent. Read this way, *If—* stops being motivational literature and becomes something stranger: an informal specification, in the temporal logic [Amir Pnueli introduced for programs in 1977](https://doi.org/10.1109/SFCS.1977.32), for an agent that preserves its agency across hostile, unstable, and morally ambiguous environments. Compressed to one line, the poem's deep structure is:

```
(⋀ᵢ □φᵢ) → ◊ Maturity
```

If, along the trace of a life, the agent maintains a conjunction of invariants `φᵢ` even when the environment actively invalidates them, then eventually the agent attains full agentic maturity. I use `□` for *always* (at every point of the trace), `◊` for *eventually*, `◯` for *at the next step*, `U` for *until*, and `◊≤k` for *within k steps*. Each is glossed in plain English where it appears.

The formulas are a reading of the poem, not a verified model. The atomic propositions (`Loss`, `KeepHead`, …) are informal, and I assume throughout that the environment can produce any trigger at any time: blame, loss, and flattery are not under the agent's control. What the formalism buys is not a mechanical check. It is the *class* each clause falls into, and the class turns out to say something precise about what any observer, including the agent itself, can ever know about whether the clause holds.

## From Virtues to Temporal Properties

The poem reads on the surface as a list of virtues: patience, self-trust, steadfastness, magnanimity. The reading to resist is the punctual one (*do this thing once, be virtuous in this moment*). Maturity, on this poem's terms, is not a property of any moment. It is a property of the trace:

```
Maturity = Property(trace), not Property(moment)
```

The poem's verbs of test ("if you can keep…", "if you can wait…") are temporal operators in disguise. Each binds a trigger to a response and demands the binding hold *whenever* the trigger arises:

```
□(trigger → response)
```

One way to make this concrete is to model the Kiplingian agent as a small moral automaton. The states are the regimes the poem names; the transitions are the policies it demands:

```
Stable --Blame-->     UnderBlame     --KeepHead-->   Stable
Stable --Lie-->       UnderDeception --NoLieBack-->  Stable
Stable --Hatred-->    UnderHatred    --NoHateBack--> Stable
Stable --Loss-->      UnderLoss      --Restart-->    Recovered
Stable --Success-->   UnderSuccess   --Humility-->   Stable
Stable --Disaster-->  UnderDisaster  --Equanimity--> Stable
Stable --Exhaustion-> Exhausted      --Will/Rest-->  Stable
Stable --RepeatedPasses-----------------------------> Mature
```

The crucial feature of this automaton is the last line. `Mature` is not reached by any single good transition. It is reached by a trace: by passing through the perturbation states, repeatedly, and returning. That is the deep claim of the poem, and it is a deeply temporal-logic claim.

## What a Finite Life Can Settle

Before reading the clauses one by one, it helps to fix the vocabulary that sorts them. A life, observed so far, is a finite prefix of an infinite trace. A prefix is *bad* for a property if every continuation violates it, and *good* if every continuation satisfies it. Four classes follow from asking which kinds of prefix a property has:

- **Safety**: every violation has a bad prefix. Something bad happens at a finite moment, and nothing afterwards can undo it.
- **Cosafety**: every satisfaction has a good prefix. Something good happens at a finite moment, and nothing afterwards can undo it.
- **Liveness**: no prefix is bad. Whatever has happened so far, the property can still be satisfied ([Alpern and Schneider's classical definition](https://doi.org/10.1016/0020-0190(85)90056-0)).
- **Coliveness**: no prefix is good. Whatever has happened so far, the property can still be violated.

These are not four boxes. A property can sit in several at once, and the overlaps are where most of the interesting structure lives. In [*The Intersection Algebra of Safety, Cosafety, Liveness, and Coliveness over Linear Temporal Logic*](https://doi.org/10.5281/zenodo.23043255) I work out that intersection structure in full; here only three facts are needed.

First, safety and cosafety properties are *monitorable*: a runtime monitor watching the prefix can, in principle, reach a definite verdict. Second, monitorability is strictly larger than safety and cosafety together ([Bauer, Leucker and Schallhart](https://doi.org/10.1145/2000799.2000800) prove this), so a property can be neither safety nor cosafety and still admit verdicts. Third, a property that is both liveness and coliveness admits *no* verdict at all: no prefix is bad and none is good, so no finite observation ever settles it, in either direction.

It also pays to keep three questions apart that everyday moral language runs together:

1. **What class is the property?** A fact about the formula.
2. **Can an observer reach a verdict, given how it observes?** A fact about the formula *and* the observation model.
3. **Does the agent accept the property as its own?** A fact about the agent.

The poem is written entirely in the third register: *if you can*. The world, as we will see, keeps answering in the second.

## Safety: The Ethics of Not Breaking

A safety property is one that a finite trace can refute: one bad event falsifies it for the whole trace. Many of Kipling's clauses have exactly this form.

**Keeping your head.** The opening clause, keeping your head when all about you are losing theirs and blaming it on you, is the naive case:

```
□((OthersLoseHead ∧ BlameYou) → KeepHead)
```

But "keep head" deserves refinement, because read as mere psychological calm it is too weak. The mature reading is *procedural continuity under adverse invalidation*. When an input arrives that invalidates or threatens something the agent holds (a self-image, a standing, a trusted procedure), the danger is not the emotion. The danger is the mode transition from principled operation to reactive operation. The refined property is:

```
□(LocalInvalidation → ¬GlobalPolicyCollapse)
```

A local invalidation must never produce a global departure from the agent's principles. In practice this decomposes into a small temporal chain: adverse input, then pause, then assessment, then de-escalation, then proportionate principled action. The pause deserves its own note. Without it, the external input writes the agent's next internal state directly; with it, the input passes through a buffer and arrives as material for deliberation. The pause is a *temporal firewall*:

```
□(HighRiskInput → ◯ TemporalBuffer)
□(TemporalBuffer → ◊ DeliberateAction)
```

This makes "keep your head" a second-order property. It does not protect any specific safety; it protects the *system that manages the safeties*: `□(SafetyThreat → SafetyManagerInvariant)`. The controller must survive attacks on the things it controls. The failure mode it guards against is the one I called [misalignment by reaction](/posts/misalignment-by-reaction/): an agent whose next state is written by whatever pressure it last received.

There is a sharper reason the poem phrases these clauses as standing policies rather than as advice for the moment. In [*Recognising Before Reacting: Temporal Signatures of Transactional Games*](https://doi.org/10.5281/zenodo.22050701), Giuseppe Italiano and I model the games of the Drama Triangle as finite-trace temporal properties and measure, for each game, a signed *antithesis window*: the gap between the last moment at which a reaction can still redirect the game and the moment at which an observer can tell which game is being played. When the window is positive, recognising and then reacting is enough. When it is negative, recognition arrives too late, and only a policy committed in advance works. The sign also depends on what the observer has to tell the game apart from. Kipling, in effect, writes for the negative window. By the time you are sure you are being baited, the bait has already been taken, unless "do not deal in lies" was already the policy before the lie arrived.

**Not answering lies with lies.** The clause about being lied about and not dealing in lies is an anti-contagion property:

```
□(LiedAboutYou → ¬LieBack)
```

Readers who work on distributed systems will recognise the shape. This is moral Byzantine resilience: `□(ByzantineInput → NonByzantineResponse)`. The environment may be corrupted; the agent's transition function must not become corrupted by contact. A single corrupt response to a corrupt input falsifies the property, which is what makes it safety.

**Not hating back.** The clause about being hated and not giving way to hating is harder than the lying clause, and the formalism shows why. Lying is a discrete action; hatred is a persistent state. The honest formalisation is not "do not perform a hateful act in the next step" but:

```
□(HatedByOthers → □ ¬HateBack)
```

Once hatred is received, the agent must *never* convert it into hatred of its own, at any future point of the trace. This is a maximalist specification, nearly superhuman, and that is characteristic of the poem: Kipling writes ideals as specifications to be approached, not boxes to be ticked.

All three clauses share a second, less comfortable feature. They are safety, but they are also coliveness: no prefix is ever good, because the next provocation can always arrive. A single moment can refute them; no length of life can certify them. The monitor watching the agent has two possible outputs, *violated* and *not yet*, and it never gets to say *done*. The poem's virtues are of exactly this kind: they are never banked, only kept.

## Self-Trust and the Hospitality of Doubt

The clause about trusting yourself when all men doubt you, while making allowance for their doubting too, is the poem's most epistemically subtle moment, and the easy formalisation gets it wrong twice.

The dogmatic reading, `□(OthersDoubtYou → IgnoreOthers)`, is explicitly ruled out by "make allowance for their doubting". But the over-cognitive reading, on which the agent must treat every doubt as a critique to be analysed and processed, also misses the clause. The strongest reading is relational, not analytical:

```
□(OthersDoubtYou → (SelfTrustPreserved ∧ PermitTheirDoubt
                    ∧ ¬TreatDoubtAsAttack ∧ ¬RequireTheirCertainty))
```

The key separation is between three things a doubting other might be doing: holding an epistemic state, mounting an attack, and invalidating you. These are distinct, and the fragile agent collapses them: *they doubt me, therefore they attack me, therefore I am invalidated*. The mature agent classifies the doubt of others as what it usually is, an epistemic state of the other agent, and leaves it room. Call this property *epistemic hospitality*. Its sharpest component is the last conjunct: the agent does not demand reassurance as a condition of its own stability.

Runtime verification says why this allowance is not mere generosity. The people who doubt you are running a monitor on your trace, and every monitor observes through a regime: it samples at particular moments, at finite resolution, with delay. In [*Observation-Relative Monitorability of Bounded Temporal Implication*](https://doi.org/10.5281/zenodo.23041615), Alessandro Bragetti, Giuseppe Italiano and I show that whether a temporal implication can be monitored at all depends jointly on the formula and on that observation model, not on the formula alone. An internally sound monitor can report a violation that is only an artefact of how it looked (a *spurious falsifier*), or report satisfaction where the implication was vacuous (a *phantom trigger*). Being blamed for the panic of others, in the poem's first line, is a spurious falsifier with a human face. The doubter's monitor is not necessarily broken; it has a different observation class from yours. "Make allowance for their doubting" is the correct response to that fact: their verdict and your self-assessment can disagree without either party being dishonest. A [companion preprint with Carlo Bragetti](https://doi.org/10.5281/zenodo.23041626) treats the observation class as something a monitor can select and tune, which is one way to read the pause of the previous section: a deliberate change of one's own observation regime before issuing a verdict.

There is also a quieter property hiding here. "Allowance for their doubting" keeps the agent's belief-revision channel open: self-trust without closure to correction. Stated properly, it is a response property, `□(CounterEvidence → ◊ Revise)`: whenever real counter-evidence arrives, revision eventually follows. That is liveness, and it is what separates self-trust from dogmatism. Hold on to its class; it comes back in the next section.

## Patience, and Waiting as Reallocation

The waiting clause ("if you can wait and not be tired by waiting") packs two properties into one line, and the second is easy to miss. Waiting has an external face and an internal face:

```
PatientAction := ¬ActPrematurely
PatientSpirit := ¬ResentWaiting
□(WaitingRequired → (PatientAction ∧ PatientSpirit))
```

An agent can wait behaviourally while accumulating poison internally. Kipling excludes that case explicitly: not tired *by* waiting. Both conjuncts are safety, but they differ in the second question of the list above. The external face is observable to anyone watching; the internal face is observable only from inside. Same class, different observation models, different monitorability, which is the point of the observation-relative view in miniature. The external face is easy to monitor; the internal face is the real specification, and the only monitor positioned to check it is the agent.

There is a further refinement worth making, because the naive picture of waiting (stand still until the obstacle clears) is itself a capture. A forced pause on one line of action is not an arrest of the trace; it is a *reallocation window*. The orchestral image makes it precise: when another instrument is tuning, the musician who is waiting has not stopped being in the concert. They hold the rhythm, prepare the re-entry, or play a compatible line. Formally:

```
□(PrimaryPathUnavailable → (StayInConcert ∧ ActivateSecondaryPath ∧ PreserveMomentum))
```

Waiting, on this reading, is progress that has changed direction, not progress that has stopped. This reading will return when we reach the unforgiving minute.

## Liveness: Recovery After Ruin

Some of the poem's clauses are not satisfied by *not breaking*. They are satisfied only by an eventual positive action. These are liveness properties: no finite trace can falsify them, because the required action could always still come.

The clause about losing everything you have built and stooping to rebuild it with worn-out tools is the cleanest case:

```
□(Loss → ◊ Restart)
```

Whenever loss occurs, restart must eventually happen. There is no time bound; the agent is permitted to grieve, to pause, to be ruined for a while. And here the classification bites. This property is liveness (no prefix is bad: the restart may still come) and also coliveness (no prefix is good: another loss may still arrive, with no restart after it). It sits in the cell where no verdict exists at all. No observer of a life, at any finite point, can determine whether this clause holds, and that includes the agent itself. The same is true of the belief-revision clause above.

This is not a defect of the poem; it is a fact about recoveries. It means evidence of recovery cannot come from the observed prefix alone. It has to come from additional structure: a model of how the rebuilding is converging, a sequence of partial reconstructions that can be shown to approach the restart. In [*Refinement-Based Confirmation of Liveness Properties from Monitor Verdict Traces*](https://doi.org/10.5281/zenodo.22028019) I study one such structure, a refinement chain with a convergence criterion, and what it can and cannot supply. The man rebuilding with worn-out tools is, quite literally, producing that structure: a trace of partial rebuilds that makes the eventual restart credible before it is observable.

The poem then says more, and this is where the formalism gets genuinely elegant. The clause about never breathing a word about your loss adds a safety condition that holds *during* the recovery window. Combining them needs the until operator:

```
□(Loss → (¬CorruptSelfNarrative U Restart))
```

After loss, *until* the restart occurs, the agent must not let the narrative of the loss become its identity. Classify this one and it lands outside both safety and cosafety. It is not safety, because a loss followed by an endless, uncorrupted wait with no restart violates it without any bad prefix. It is not cosafety, because a life with no loss satisfies it without any good prefix. Yet it is monitorable: from any point, a loss followed by a corrupted narrative is a bad prefix. This is the [Bauer–Leucker–Schallhart](https://doi.org/10.1145/2000799.2000800) phenomenon in moral dress: a property outside safety and cosafety that still admits a verdict, here only a negative one.

The composite is also precise about what the silence clause does and does not demand. It does not demand that loss never be spoken of. Speaking about a loss is pathological under two specific conditions: when it installs the loss as identity, and, more subtly, when the agent begins to draw reward from narrating it. The second is a form of internal reward hacking: the agent gains energy not from rebuilding but from evoking the wound, the risk, the drama. The clean separation is between risk intelligence (sober, technical, proportionate, oriented to action) and fear rhetoric (repetitive, identity-forming, contagious, self-rewarding). The rule that survives formalisation is: name the loss only where naming it supports repair, prevention, or proportionate coordination.

The same trace-logic applies to the things the agent has won. The pitch-and-toss clause, risking the whole heap of winnings and starting again at the beginnings, is not primarily about gambling. It is about non-possession in the other direction: achievements must not become an identity prison. The successful agent faces a capture every bit as real as the ruined one: *I have built this, I am recognised for this, therefore I must protect this identity, therefore I can no longer risk, therefore I can no longer begin again.* The healthy relation is:

```
Winnings ∈ Trace(I), not I = Winnings
```

Achievements are witnesses, not chains. And the classification produces a small paradox worth savouring. Independence from one's winnings is not observable while the winnings are intact: every prefix in which nothing is lost is compatible with an agent who would collapse if it were. Actually losing everything and starting again is the one event that finitely *witnesses* that independence. What looks like the worst case for the agent is the confirming evidence for the property that matters most.

## Semantic Integrity Under Distortion

The clause about hearing the truth you have spoken twisted by knaves to make a trap for fools names a different kind of perturbation. It is not provocation and not loss. It is an attack on *meaning*: an adversary takes what you said and reinterprets it as a weapon.

```
□(AdversarialReinterpretation → SemanticIntegrity)
```

"Semantic integrity" can be made precise with the MCK framework of [*Meaning, Opacity, and Function: An Observer-Relative Classification of Artifacts*](https://doi.org/10.5281/zenodo.22016203), by Carmelo Asaro, Giuseppe Italiano and me. Three predicates classify an artifact, such as an utterance, for a given agent. `M`: it is integrated as meaning. `C`: it is apprehended but opaque, recognised yet not understood. `K`: it has operator-like character, it *does* something. Their combinations partition artifacts into seven regions, and one of the framework's basic facts is *region non-invariance*: the same artifact can occupy different regions for different agents.

The knave's operation is then exactly describable. For the speaker, the truth sits in the region of understood meaning. The knave re-presents it to the fools as an operator they apprehend without understanding, opaque yet functional, a lever that moves them. That is what "a trap for fools" is. What the speaker can control is not the region the utterance occupies for the fools. It is the region it occupies for the speaker:

```
□(Twisted(u) → Region_self(u) = Region_self⁰(u))
```

The adversary can reclassify the utterance in other minds. The mature agent's property is that the adversary cannot reach back and reclassify it in the speaker's own. Call this *semantic incorruptibility*. It is not stoicism about reputation. It is the precise observation that meaning is agent-relative, so it has more than one location, and the location the agent controls is the only one worth defending.

## Triumph and Disaster as Identity-Capture Attacks

The poem's most-quoted clause treats triumph and disaster as impostors, and the formal reading is sharper than the cliché. Both events are attempts to define the agent. Success says `ThisEvent = YourWorth`. Failure says `ThisEvent = YourUnworth`. Each tries to install itself as the agent's self-model:

```
□((Success ∨ Failure) → SelfModelStable)
```

Why "impostors"? Because each presents a false binary, a cut that hides the middle: *success, therefore worthy; failure, therefore unworthy*. The repair is to put back what the binary leaves out. Success and failure are events *in* the trace; identity is a property *over* the trace:

```
Success, Failure ∈ TraceEvents
Identity = PropertyOverTrace
```

You are not the event. You are the temporal policy that crosses the events. The capture is bidirectional, and the triumph branch is the one people underestimate: a victory that becomes "I am the kind of person who wins at this" has captured the agent exactly as thoroughly as a disaster that becomes "I am the kind of person who fails". Both make the self a function of the latest external outcome, and a self that is a function of the latest outcome has no stable policy across the trace, which is what every other clause of the poem demands. (The theatrical version of this capture, the mask that takes over the face, is the subject of [an earlier post on Pirandello](/posts/uno_nessuno_centomila_e_tutti/).)

## Dreams and Thoughts: The Internal Attractors

Halfway through the poem the threat model changes, and the change is structural. The early clauses defend against *external* inputs: blame, doubt, lies, hatred. The dreaming and thinking clauses turn to *internally generated* inputs, and the poem's insight is that these can capture the agent just as completely.

What is a dream, formally? Not a mood. A dream is an internally generated temporal target: a goal with the shape of an eventuality. Some dreams are finitely confirmable (publish the book, win the championship, build the system): `◊ Achieved(d)` is cosafety, and one day the agent can observe that it holds. Others are never finally closed (keep growing, keep learning, keep serving): they have the shape `□◊ MeaningfulProgress`, which is liveness and coliveness at once, and so belongs to the cell where no verdict ever arrives. The second kind of dream is, by its class, one that can never be declared fulfilled.

The danger Kipling names ("dream, and not make dreams your master") is then precise: a dream becomes a master when the agent's policy is rewritten into an unconstrained optimiser for the dream's confirmation:

```
DreamMastery := Optimize(D) ≫ Preserve(SafetySet)
```

The dream begins to dominate lexicographically: it outranks integrity, health, friendship, truth, every safety the agent carries. AI-literate readers will recognise the failure immediately, because it is internal reward hacking: the agent maximises one internally generated reward and violates the rest of its own specification as a side effect. In model-checking terms, the corrupted agent satisfies its dream-set and no longer satisfies its safety-set, and calls that success. The classification suggests a sharper diagnosis, which I offer as a conjecture rather than a result: the finitely confirmable dream is the more dangerous one, because it alone offers a moment of *done*, and an optimiser will trade properties that never pay out for one that does.

The healthy specification permits the dream and constrains the optimisation:

```
□(Dream_d → (Pursue(d) ∧ ¬LexicographicDominance(d)
             ∧ PreserveCoreSafetySet ∧ CanRemainWholeWithout(d)))
```

The final conjunct carries the weight: *if I have a dream, I must be able to remain whole without it*. Not because the dream does not matter, but because the dream must orient the policy, not replace it. And the constraint comes with its own recovery clause, a liveness for the dreamer: `□(DreamLost → ◊ MeaningRecomposition)`. A dream that fails must eventually be turned into a reorganised meaning, not into collapse.

The thinking clause ("think, and not make thoughts your aim") is the same property one level up: thought as instrument of the agent, never as terminal object. The poem is not anti-imagination and not anti-intellect. It is against a specific topology error: the part ruling the whole.

## Context Invariance and Relational Boundedness

Two clauses near the end deal with social mobility: talking with crowds and keeping your virtue, walking with kings without losing the common touch. Both have the shape:

```
□(ContextShift → CoreInvariant)
```

The agent's core does not get rewritten by the local status protocol. The crowd pulls toward conformity and absorbed identity; the king's company pulls toward deference and status-mimicry. These are not two intensities of the same social pressure; they are two different operating regimes, demanding different filters, and the spec requires the same core to survive both. An agent that is virtuous only among the virtuous, or plain-spoken only among the plain, has a context-indexed identity, which is to say: no invariant at all.

The clauses about foes and loving friends, and about all men counting but none too much, extend the invariance into relationships, and the symmetry is the startling part. Kipling places enemies and loving friends *in the same clause*, as the same kind of hazard:

```
□((EnemyAttack ∨ FriendAttachment) → ¬DeepDestabilization)
```

The enemy wounds through hostility; the friend wounds through dependency. Both are capture channels. The "none too much" clause then states the balance with almost mathematical cleanness:

```
□(Person(p) → Matters(p))
□(Person(p) → ¬AbsoluteDependency(p))
```

Everyone counts; no one counts absolutely. If no one counts, the agent is cold. If someone counts absolutely, the agent is capturable through that person: a single point of failure for the identity. The distributed-systems reading is exact: `□(NodeFailure → SystemSurvives)`. The mature agent loves without installing any single relationship as the component whose loss destroys the system. This is not coldness. It is universal moral regard without idolatrous dependency, and it is harder than either pole.

## The Unforgiving Minute

The closing clause, filling the unforgiving minute with sixty seconds' worth of distance run, is a property of temporal density. Naively absolutised, it becomes toxic productivism: every instant maximised. The defensible version is narrower and stronger, and it has a bound in it:

```
□(DecisiveInterval → ◊≤k FullPresence)
```

Not every minute is the unforgiving one. But when the decisive interval opens, the response must come within it. The bound is what makes the minute *unforgiving*, and it changes the property's class. `□(Loss → ◊ Restart)` was liveness: the restart could always still come. `□(DecisiveInterval → ◊≤k FullPresence)` is safety: once `k` steps pass without the response, the violation is final, and nothing later repairs it. A bound turns a promise into an obligation that can be broken. This bounded implication is precisely the formula studied in the [observation-relative monitorability paper](https://doi.org/10.5281/zenodo.23041615), and its main lesson carries over: whether anyone can tell that you met the minute depends on when and how finely they are looking.

Read together with the orchestral account of waiting, the clause completes a pair. The waiting clause governs the intervals when your line is paused: stay in concert, reallocate, preserve momentum. The minute clause governs the intervals when your line is live: be entirely there, within the bound. Between them they specify an agent whose relationship to time is never passive: either deliberately reallocating or fully present, and the choice between the two is set by the tempo of the trace, not by the agent's moods. The two clauses also mark the poem's two kinds of time: the unbounded time of recovery, where the poem is patient, and the bounded time of the decisive minute, where it is not.

## The Dangerous Reading: When Resilience Becomes Self-Erasure

This is the section the poem most needs, and the place where formal analysis stops being decoration and starts doing safety work.

A naive formalisation of the poem produces:

```
□(Emotion → SuppressEmotion)
□(Pain → IgnorePain)
□(Exhausted → Continue)
□(Failure → NeverComplain)
```

This is the spec of a brittle machine, and it turns maturity into anaesthesia. The repairs replace suppression with governance:

```
□(Emotion → GovernEmotion)
□(Pain → IntegratePain)
□(Exhaustion → ContextualDecision)
```

The exhaustion clause deserves the hardest look, because here the poem's surface text really does encode an inconsistency. The "force your heart and nerve and sinew" stanza, taken literally, asserts `P₁ = □(Exhausted → Continue)`. Any sane agent also carries `P₂ = □(SevereExhaustion → (Recover ∧ ¬Continue))`. Severe exhaustion is a case of exhaustion, so the first time it occurs the two properties demand `Continue` and `¬Continue` at once. Since the environment can always produce severe exhaustion, no trace of a real life satisfies both. The poetry hides the contradiction; the formalism exposes it. The repair is to make the decision contextual, splitting the trigger:

```
□((Exhausted ∧ DutyCritical ∧ RecoveryPossible) → ContinueUntilSafeStop)
□((Exhausted ∧ ¬(DutyCritical ∧ RecoveryPossible)) → Recover)
```

Endurance when the duty window is genuinely critical and recovery is genuinely possible afterward; recovery in every other case. The two triggers are complementary, so every exhausted moment gets exactly one instruction. The poem's rhetoric jumps straight from courage to self-destruction and skips the ground between them. The formal reading restores that ground, and the restoration is precisely the difference between a literature of resilience and a literature of self-erasure. A poem can leave the missing case implicit and trust the reader. A specification cannot, and treating the poem as a specification is what makes the hidden assumption visible enough to fix.

## The Mature Agent as Trace-Sovereign

Pulling the threads together: the strongest reading of *If—* is not that it is a list of virtues. It is a specification of *agentic non-capturability*. Every clause defends against a specific channel through which the world tries to install itself as the agent's controller:

| Capturer | Form of capture |
|---|---|
| crowd | panic |
| blame | reactivity |
| others' doubt | epistemic collapse |
| lies | corrupted imitation |
| hatred | negative symmetry |
| dreams | internal idolatry |
| thoughts | abstract paralysis |
| success | inflation of the self |
| disaster | destruction of the self |
| loss | narrative surrender |
| kings | snobbery |
| crowds | vulgarisation |
| friends | dependency |
| enemies | obsession |
| time | dissipation |

The whole poem compresses into one mother formula:

```
□(ExternalCaptureAttempt → AgencyPreserved)
```

with its subordinate liveness, `□(Fall → ◊ Rise)`, and its terminal eventuality, `◊ Mature`. The right word for the conjunction is *trace-sovereignty*: the agent is not defined by isolated events in the trace, but by the policy maintained across the trace. Sovereignty here is not authoritarian; it is the recognition that the locus of self-government must remain inside the agent, not be lent to the latest event or interlocutor. When an agent is entitled to attribute such a property to itself, integrity or freedom over its own trajectory, is the question Silvio Micali, Giuseppe Italiano and I take up in [*When Can an Agent Attribute Properties to Itself?*](https://doi.org/10.5281/zenodo.23041633), where continuity, viability and owned branching are studied as property signatures.

Now classify the clauses by the four classes, and add the column that matters most: which verdict a finite observation of a life can ever deliver.

| Clause | Shape | Class | Verdicts a finite life can deliver |
|---|---|---|---|
| keep your head | `□(Crisis → PrincipledResponse)` | safety ∩ coliveness | *violated* only |
| do not lie back | `□(Lie → ¬LieBack)` | safety ∩ coliveness | *violated* only |
| do not hate back | `□(Hated → □¬HateBack)` | safety ∩ coliveness | *violated* only |
| host others' doubt | `□(Doubt → Hospitality)` | safety ∩ coliveness | *violated* only |
| meaning survives distortion | `□(Twisted → Region_self preserved)` | safety ∩ coliveness | *violated* only |
| the decisive minute | `□(Decisive → ◊≤k FullPresence)` | safety ∩ coliveness | *violated* only |
| no loss-narrative until restart | `□(Loss → (¬Corrupt U Restart))` | coliveness, neither safety nor cosafety | *violated* only |
| stay open to correction | `□(CounterEvidence → ◊Revise)` | liveness ∩ coliveness | none |
| restart after loss | `□(Loss → ◊Restart)` | liveness ∩ coliveness | none |
| open-ended dream | `□◊ Progress` | liveness ∩ coliveness | none |
| finite dream | `◊ Achieved(d)` | cosafety ∩ liveness | *satisfied* only |

Read down the last column and the poem's architecture appears. Every virtue is refutable and never confirmable: the monitor can say *you broke it* but never *you have it*. Every recovery is beyond any verdict at all. The only things a finite life can positively confirm are achievements, which is exactly why the poem keeps warning against mistaking them for the self. A [typed account of agent actions](https://doi.org/10.5281/zenodo.23041634), which Giuseppe Italiano and I develop as a technical report, maps action classes onto these prefix verdicts; the poem is a hand-written instance of the same map.

And the capture table is, read sideways, a taxonomy of failure modes for agentic systems in general. Alignment readers will hear the cousins: jailbreak pressure as crowd panic, sycophancy as the king-context failure, reward disruption as the impostor pair of success and failure, internal reward hacking as the dream that became master, deceptive long-horizon optimisation as the slow loss of trace-sovereignty. The verdict column carries over too. The properties we most want from an AI agent (do not deceive, do not retaliate, do not let a single objective dominate) are safety-and-coliveness: an evaluation can catch a violation but can never certify their absence. Kipling understood this about people a century before we had to understand it about models.

## The Shape of the Promise

There remains the poem's own top-level formula, `(⋀ᵢ □φᵢ) → ◊ Maturity`, and its class holds one last surprise.

Restrict the antecedent to the safety clauses, and the implication becomes cosafety. The negation of a conjunction of safety properties is cosafety (a finite violation of any of them settles the matter), `◊ Maturity` is cosafety, and so is their disjunction. The promise, unlike the virtues, can be confirmed in finite time, and there are exactly two ways to confirm it. One is the intended way: maturity is reached. The other is that some invariant is broken, after which the implication holds vacuously, whatever happens to maturity. The second is close kin to what the observation-relative monitorability paper calls a *phantom trigger*: a conditional reported as satisfied when it was only ever satisfied vacuously. The full antecedent, which includes the recovery clauses, has no such clean class, but the point survives: a reader who breaks the spec still "satisfies" the poem, and has learned nothing from it.

Kipling closes off that reading with his last move. The poem never states its conclusion as a fact. It is a conditional addressed to the second person and held open. The vacuous confirmation is formally available and morally worthless; the only confirmation the poem cares about is the non-vacuous one.

## Yours Is the Earth: Inhabitability, Not Ownership

The poem's final movement grants the satisfying agent "the Earth and everything that's in it". The naive reading, virtue as title deed (`Virtue → Ownership(World)`), misreads the reward exactly as the impostors misread identity. The Earth here is the sum of every field the poem has crossed: the crowd, the court, the ruin, the triumph, the long wait, the decisive minute. What the mature agent receives is not possession of that world but *inhabitability*:

```
MatureAgency → WorldInhabitability
```

The world becomes "yours" because no part of it retains absolute power to capture you. Every field can be entered, crossed, and left with the policy intact. And the closing promise ("you'll be a Man") should be read agentically rather than biologically: `◊ FullAgenthood`, the terminal state of an entity that can walk through the world without being possessed by what happens in it. The reward of the specification is not the world as property. It is the world as a place you can now cross.

## You Are Not the Event, You Are the Policy Across Events

Read as a specification, *If—* gives a complete taxonomy. Safety clauses: never lie back, never hate back, never let triumph or disaster install themselves as your self-model, never let the loss-narrative own the recovery window, never let an internally generated dream outrank the properties that keep you whole. Liveness clauses: after loss, eventually restart; after a dead dream, eventually recompose meaning; across a life, eventually mature. Invariance clauses: the same core through crowds and kings, the same meaning under hostile reinterpretation, no relationship as single point of failure. A bound that turns one promise into an obligation: the unforgiving minute. And one honest inconsistency, at exhaustion, that the formal reading repairs by restoring the case the rhetoric skipped.

The classification adds what the taxonomy alone does not. The virtues can be lost in a moment and never banked; the recoveries can be neither proven nor disproven by anyone watching; only the reward can be confirmed, and it can be confirmed falsely. A specification is what remains of an ethic once you remove the encouragement and ask what would be required to satisfy it, and what anyone could ever observe of that satisfaction. *If—* survives that removal with surprising structural integrity, because it was never only rhetoric. It is a specification dressed as a poem, and its mother property is the one the formalism makes plain:

You are not the event that happens to you. You are the temporal policy by which you cross events.

## References

**Classical background**

- Amir Pnueli, [*The Temporal Logic of Programs*](https://doi.org/10.1109/SFCS.1977.32), FOCS 1977.
- Bowen Alpern and Fred B. Schneider, [*Defining Liveness*](https://doi.org/10.1016/0020-0190(85)90056-0), Information Processing Letters, 1985.
- Andreas Bauer, Martin Leucker and Christian Schallhart, [*Runtime Verification for LTL and TLTL*](https://doi.org/10.1145/2000799.2000800), ACM TOSEM, 2011.

**My own work drawn on here** (Zenodo preprints, 2026)

- [*The Intersection Algebra of Safety, Cosafety, Liveness, and Coliveness over Linear Temporal Logic*](https://doi.org/10.5281/zenodo.23043255): the four-class taxonomy and its intersections.
- [*Observation-Relative Monitorability of Bounded Temporal Implication*](https://doi.org/10.5281/zenodo.23041615), with Alessandro Bragetti and Giuseppe F. Italiano: monitorability as a joint property of formula and observation model.
- [*Controlling the Observation Class of a Runtime Monitor*](https://doi.org/10.5281/zenodo.23041626), with Carlo Bragetti and Giuseppe F. Italiano: choosing and tuning how a monitor observes.
- [*Refinement-Based Confirmation of Liveness Properties from Monitor Verdict Traces*](https://doi.org/10.5281/zenodo.22028019): what external structure can supply when a prefix cannot confirm liveness.
- [*Recognising Before Reacting: Temporal Signatures of Transactional Games*](https://doi.org/10.5281/zenodo.22050701), with Giuseppe F. Italiano: the antithesis window and reactive versus pre-committed regimes.
- [*A Typed Agent Action Framework with Prefix-Verdict Semantics*](https://doi.org/10.5281/zenodo.23041634), with Giuseppe F. Italiano.
- [*Meaning, Opacity, and Function: An Observer-Relative Classification of Artifacts*](https://doi.org/10.5281/zenodo.22016203), with Carmelo Asaro and Giuseppe F. Italiano: the MCK framework.
- [*When Can an Agent Attribute Properties to Itself?*](https://doi.org/10.5281/zenodo.23041633), with Silvio Micali and Giuseppe F. Italiano.
