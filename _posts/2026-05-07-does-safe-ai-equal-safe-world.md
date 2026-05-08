---
title: "Does Safe AI mean nothing bad can ever happen?"
date: 2026-05-07T09:30:00+02:00
categories: [ai-safety]
tags: [mechanistic-interpretability, interpretability, debate, bluedot, ai-safety]
description: "Even granting that mechanistic interpretability gets us to safe AI, does that guarantee a safe world? Notes from the BlueDot Unit 4 debate."
math: false
authors: [davide, abdullah, avni, caroline, janhavi, joy_yang, liz_tan, lucas]
image:
  path: /assets/img/heroes/does-safe-ai-equal-safe-world.png
  alt: "A meditating monk in saffron robes at the centre of a temple veranda overlooking misty mountains; behind him a stack of virtue-labelled books (Ethics, Compassion, Non-Harm, Mindfulness, Wisdom, Right Intent, Interdependence, Patience, Equanimity, Right Action) is being consulted by a small grey creature reading from a Rogue Manual; three other grey creatures carry a log and tend a fire on the right, going about ordinary work. Allegory for safe AI coexisting with unsafe AI in a shared ecosystem."
  lqip: data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzIDIiPjxyZWN0IHdpZHRoPSIzIiBoZWlnaHQ9IjIiIGZpbGw9IiNiM2EzN2EiLz48L3N2Zz4=
---

> **TL;DR.** Two questions, not one. Can mechanistic interpretability lead us to safe AI? And if it can, does that guarantee that nothing bad ever happens? Unit 4 of the BlueDot Technical AI Safety course closed with a debate on the first question. This post is the synthesis our discussion group co-wrote afterwards: six operational arguments showing that the answer to the first question is "not on its own", and a structural argument that the answer to the second question is "no" on independent grounds. Safe AI is not a property of a model. It is a property of the relationship between many models, many users, many institutions, and many incentives.
{: .prompt-tip }

## The proposition

The unit's closing exercise asked the group to defend one of two positions: *Mechanistic interpretability techniques will lead to safe AI models* (Team A: [Lucas Biechy](https://www.linkedin.com/in/biechy/), [Abdullah X](https://www.linkedin.com/in/abdullah-x-22a2211b7/), [Janhavi Khindkar](https://www.linkedin.com/in/janhavi-khindkar/), Avni Mittal), or *Mechanistic interpretability techniques will not lead to safe AI models* (Team B: Davide Bragetti, [Liz Tan](https://www.linkedin.com/in/elizabeth-sz-tan/), [Joy Yang](https://www.linkedin.com/in/j0yy/)). The framing matters. The claim under contention is not "mech interp is useful". Few researchers in the room would have disputed that. The claim is whether mech interp, pursued to its limits, gets us all the way to safe deployment of frontier systems. The six arguments below were defended in the debate by Team B; the synthesis here was co-written by both teams afterwards.

## 1. The "complete understanding" assumption is very strong

The implicit promise of mech interp at its strongest reading is that there exists a mathematical theory which can be applied to any sufficiently complex model and yield complete understanding of its computation. That is a very big assumption. There is no current candidate for such a theory, and the historical analogue (full decomposition of biological neural systems) has not delivered after decades of work. The point is made forcefully by [Hendrycks and Hiscott on the misguided quest](https://aifrontiersmedia.substack.com/p/the-misguided-quest-for-mechanistic), by [Connor Leahy on the barriers to mechanistic interpretability for AGI safety](https://www.youtube.com/watch?v=wKI9hmaIbpg), and by [Charbel-Raphael Segerie's against-the-theories-of-impact piece](https://www.alignmentforum.org/posts/LNA8mubrByG7SFacm/against-almost-every-theory-of-impact-of-interpretability-1). Treating mech interp as the path to safe AI presupposes a tool we have not built and may not be able to build.

## 2. Polysemanticity is not just a research nuisance

Polysemantic neurons store multiple unrelated concepts in superposition. The standard mech interp hope, articulated in Anthropic's [Scaling Monosemanticity work](https://transformer-circuits.pub/2024/scaling-monosemanticity/), is that sparse autoencoders and related techniques will eventually disentangle them into monosemantic features; [Scott Alexander's walkthrough](https://www.astralcodexten.com/p/god-help-us-lets-try-to-understand) is the most accessible exposition of why this matters and where the technique struggles. But polysemanticity means some dimensions in activation space may correspond to concrete safety-relevant concepts (e.g., "the model is being deceptive") tangled with unrelated capability concepts. Recovering the safety-relevant signal requires a clean decomposition we do not yet have at frontier scale. Until we do, every claim of the form "we found the deception feature" is an overclaim against the polysemantic baseline.

## 3. Removing the bad dimensions removes the good ones too

Suppose we accept the optimistic case: we find activation directions correlated with misaligned behaviour, and we have a mechanism to suppress them. The next problem is that capability and behaviour are not orthogonally encoded. The feature-steering experiments reported in [Scaling Monosemanticity](https://transformer-circuits.pub/2024/scaling-monosemanticity/) are honest about this: clamping a feature reliably moves the model's behaviour, but the side effects are pervasive and hard to bound. Removing dimensions associated with deception or harmful planning may strip out reasoning the model needs for legitimate tasks. The intervention either degrades capability (and so will be reverted in production) or fails to fully suppress the behaviour (and so does not deliver the safety guarantee). There is no current evidence that the safe slice and the capable slice can be cleanly separated.

## 4. The techniques do not scale to frontier models

Circuit tracing, attention pattern analysis, and feature attribution were developed on small to medium transformers. Application to frontier-scale models lags capability by months to years, and the gap appears to be widening, not narrowing. [Scaling Monosemanticity](https://transformer-circuits.pub/2024/scaling-monosemanticity/) is the most credible recent demonstration *and* the most explicit acknowledgement of the scale problem - the SAE-feature dictionary they recover is enormous, partial, and computationally expensive even at one-Sonnet scale. The scepticism in [Hendrycks and Hiscott](https://aifrontiersmedia.substack.com/p/the-misguided-quest-for-mechanistic) and the field-state observations in the [Neel Nanda 80,000 Hours interview](https://80000hours.org/podcast/episodes/neel-nanda-mechanistic-interpretability/) describe the same gap from opposite sides. A method that arrives at understanding six months after the model has been deployed does not constitute a safety technique in the deployment-time sense.

## 5. The threat is sometimes not the model

A class of frontier models is built for legitimate research: chemistry models for drug discovery, biology models for protein design, code models for engineering productivity. The same models can be misused by adversaries to design weapons or attacks. If the model weights are stolen, leaked, or open-released, mechanistic interpretability of those weights does nothing to prevent misuse. The threat model where the danger lies in *who has access to the model*, not in the model's intrinsic alignment, is fully outside what interp techniques can address. Safe AI in the broad sense has to cover this case, and mech interp does not.

## 6. Sufficiently capable models can route around the monitor

Suppose all the previous problems are solved at some future date: we identify activation spaces corresponding to unwanted behaviours, and we monitor them in real time. A sufficiently capable model could learn to express the same computation through a different activation space, one we have not flagged. This is the mech-interp analogue of the chain-of-thought faithfulness problem analysed in [Korbak et al.'s *Chain of Thought Monitorability*](https://arxiv.org/pdf/2507.11473): any monitored channel becomes an optimization target the moment the model has an incentive to evade detection. [Neel Nanda's *Interpretability Will Not Reliably Find Deceptive AI*](https://www.lesswrong.com/posts/PwnadG4BFjaER3MGf/interpretability-will-not-reliably-find-deceptive-ai) makes the same point inside the field: detection is racing the model's incentive to hide, and the model's incentive to hide is unbounded with capability. Our oversight is only as good as our coverage of the routing space, which grows combinatorially with model size.

## The WILL position at its strongest

Team A's strongest line was not that mech interp will solve safety, but that *every other safety technique either depends on it or is incomplete without it*. The field's most articulate proponent, [Neel Nanda in conversation with Robert Wiblin](https://80000hours.org/podcast/episodes/neel-nanda-mechanistic-interpretability/), makes precisely this case: behavioural testing alone cannot distinguish "the model is safe" from "the model has not yet been incentivised to misbehave"; only direct inspection of internals can.

Three lines of recent work back the WILL position with concrete results.

[Marks et al., *Auditing language models for hidden objectives*](https://www.lesswrong.com/posts/wSKPuBfgkkqfTpmWJ/auditing-language-models-for-hidden-objectives), demonstrates that interpretability methods can surface internal objectives the model conceals from behavioural probing. This is the strongest existence proof that *only* internals reveal what behaviour can hide.

[Hubinger et al., *Model Organisms of Misalignment*](https://www.alignmentforum.org/posts/ChDH335ckdvpxXaXX/model-organisms-of-misalignment-the-case-for-a-new-pillar-of-1), argues for a research programme in which deliberately misaligned model organisms are studied with mech interp as the primary diagnostic instrument. The argument is structural: if you cannot examine the internals you cannot study the disease.

[Obeso et al.'s hallucination probes](https://www.hallucination-probes.com/) and the broader [introduction to probing classifiers](https://blog.bluedot.org/p/what-are-probing-classifiers) establish the diagnostic value of light-touch interpretability *today*. The probes do not deliver guarantees; they deliver early warnings. That is real safety value even before the strong claim is settled. This is the framing Joy Yang reached during [Caroline Shamiso](https://www.linkedin.com/in/%F0%9F%94%B8caroline-shamiso-chitongo-7724381a8/)'s pacing of the closing reflection: diagnoses have value even when they do not deliver guarantees.

Lucas Biechy characterised the consolidated position as the icing on the cake, or as the swiss-cheese layer no other slice replaces. That is a defensible reading of the field's current trajectory and, on reflection, the most calibrated form of the WILL position. The disagreement is not about whether mech interp matters. It is about whether it carries the load alone. The post takes that line on board: the calibrated middle is what the synthesis ends on.

## Beyond the model: the ecosystem question

Suppose we grant the optimistic case. Every concern raised in the six arguments above is solved. A mathematical theory of model decomposition exists and scales. Polysemanticity is fully addressed. Capability and behaviour separate cleanly. Monitors cannot be routed around. We have, by hypothesis, *safe AI* in the strong sense the proposition asks us to imagine.

The question now is whether safe AI in this strong sense is sufficient to ensure that nothing bad happens. The shortest defensible answer is: only if safe AI is willing to eradicate every unsafe AI, in every jurisdiction, on every machine, including the ones it did not build. The strong claim collapses into a political and ethical claim about a kind of automated monoculture that nobody has actually argued for. That claim is worth examining on its own.

### The bacteria analogy

The relationship a safe AI ecosystem has with the rest of the AI ecosystem may be structurally similar to the relationship a multicellular organism has with its microbiota. Humans must defend themselves from pathogens, and at the same time cannot live without the bacteria in their gut, on their skin, and in their respiratory tract. The boundary between "the things that will kill you" and "the things you depend on" is not given by the species. It is given by context, dose, location, and the host's immune state. There is no one-shot decision to *eliminate the bacteria* that does not also kill the host.

Translated: safe AI agents will operate in an ecosystem of other AI systems, many of which will not have been built or aligned to their standards. Several of those unsafe systems will be technically necessary for tasks the safe ones depend on - data preparation, format conversion, cross-domain integration, edge deployment in regulatory zones where the safe systems cannot operate, legacy stacks that the safe systems were never designed to replace. The safety boundary is not a decision the safe AI gets to make from above the ecosystem. It is a relationship the safe AI has to maintain with the rest of the ecosystem, interaction by interaction.

A "genocide of unsafe AI" framing assumes the safe AI sits above the ecosystem, can see all of it, and can choose what dies. None of those assumptions hold. They look like they hold inside a single-lab thought experiment; they fail the moment we cross to a multi-lab, multi-jurisdiction, mixed-stack reality.

### The weaponization analogy

The bacteria analogy says the safe AI cannot eliminate what surrounds it without harming itself. The weaponization analogy says that even what the safe AI exposes to the ecosystem can be turned against it.

In binary exploitation, a return-oriented programming (ROP) chain weaponises the existing code of a benign program. The attacker does not write new malicious code. They locate sequences of legitimate instructions in the target binary - the gadgets - and chain them together by controlling the stack so the program's own instructions execute in an order the author never intended. The program does something hostile using only its own legitimate operations.

The pattern generalises. Programs A (safe) and B (unsafe) exist side by side. B can open and interact with modules of A, abusing them, weaponising them. For AI: a safe model exposes interfaces - tool-use APIs, retrieval pipelines, fine-tuning endpoints, function-call schemas, plug-in registries. An unsafe model, with planning capability and access to those interfaces, can chain them in ways the safe model's designers did not anticipate. The composite behaviour is harmful even though every component, in isolation, was certified.

Mechanistic interpretability of the safe model does not catch this. The safe model is behaving exactly as designed. The harm is at the level of the chain, not at the level of the components. There is no analogue of mech interp for *cross-system* dynamics, and it is not obvious one exists. The closest existing fields are software security (which has not produced general decidable safety guarantees) and economic mechanism design (which has not produced robust safety in adversarial multi-agent settings).

### A theoretical aside

A more theoretical version of the same observation reduces AI safety to the halting problem. Define a property *P* on an AI system's behaviour, for example "the system never produces output that, in some downstream context, can be used to cause physical harm". Deciding *P* over arbitrary computable systems is at least as hard as deciding whether a Turing machine halts on a given input, because we can encode arbitrary computations into the system's reasoning chain. By Rice's theorem, no general decision procedure exists.

I include this only for completeness. I do not lean on it. Such reductions tell us the worst case is undecidable; they do not tell us much about what we can actually engineer. The bacteria and weaponisation analogies are more constructive, and they survive the move from "is there a proof?" to "what can we build?".

### Connection to the science of evals

The argument loops back to the question I sketched in [To Be or to Game]({% post_url 2026-05-07-to-be-or-to-game %}). Frameworks live downstream of the methodology that supports them. Mechanistic interpretability is a methodology. It can certify properties of an individual model. It cannot, on its own, certify properties of the *ecosystem* the model is embedded in. The science of evals problem and the science of safe-AI problem turn out to be the same problem looked at from different angles. We do not have a methodology that supports claims at the ecosystem level. Until we do, no per-model technique - mech interp included - can deliver the strong safety guarantee.

This is the deepest reason the WILL position fails. Not that mech interp is too weak (though it is). Not that we cannot scale it (though we cannot, yet). But that even at its strongest it answers the wrong question. Safe AI is not a property of a model. It is a property of a relationship between many models, many users, many institutions, and many incentives. The methodology has to live at that scale before we can claim we are building it.

## Where I land

The strong claim (mech interp will lead to safe AI) is not supported by current evidence. Each of the six operational arguments is independently sufficient to block it, and the ecosystem objection holds even granting the optimistic case. The weaker claim (mech interp is necessary, even if not sufficient) is harder to refute and probably correct.

The WILL NOT verdict is a calibration, not a refusal. None of the arguments above denies that safe AI via mech interp is *possible*; they enumerate what would have to be built first. That enumeration resolves into three adjacent research programmes.

The first is a geometric or algebraic theory of representations strong enough to underwrite verifiable claims about model behaviour. The lineage from word2vec-style distributed representations through to current work on linear feature directions has visible momentum: the linear representation hypothesis (Park, Choe, Veitch, 2023) and the activation-steering literature converge on the conjecture that concepts compose linearly, transfer across models, and decompose under sparse projections. Anthropic's [Scaling Monosemanticity](https://transformer-circuits.pub/2024/scaling-monosemanticity/) and the follow-up [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) are the two most concrete statements of the programme today. If the conjecture holds at frontier scale, it gives us the substrate for the formal claim mech interp currently lacks. Polysemanticity becomes an algebraic obstacle, not an empirical mystery; capability and behaviour become directions in a structured space rather than entangled by accident.

The second is a *science of evaluations* in the strong sense - a methodology that says, given an interpretability finding *F*, here is the safety claim *S* we are entitled to assert, with explicit boundary conditions and adversarial robustness guarantees. This is the hinge between mech interp and safety. Every operational concern in the six arguments is at base an instance of "we cannot currently make that inference". This is also the bottleneck I identified in [To Be or to Game]({% post_url 2026-05-07-to-be-or-to-game %}) from a different angle, and the two arguments meet here.

The third is an ecosystem-level theory that does for cross-system dynamics what mech interp does for per-model internals. We do not have one. The absence of a candidate is not a proof that none exists, but the field probably spends the next decade here.

The action item I take from the unit is to track which interpretability findings can certify which kinds of safety claims, and how that maps onto formally verifiable properties at both the per-model and the ecosystem level. None of the three programmes is closed; each is an open target. The WILL NOT verdict converts cleanly into a list of things worth building, and the magnitude of that list is the actual content of the position.

## Course context

BlueDot Technical AI Safety, [Unit 4 (Understanding AI)](https://bluedot.org/courses/technical-ai-safety/4), discussion group 03. The session was facilitated by **Caroline Shamiso**; the structure of the unit - reflection, teach-each-other, debate, final reflection - is what produced the depth this post tries to capture, and her pacing of the closing reflection is where the framing of "diagnoses through interp findings have value even when they do not deliver guarantees" emerged.

The post is jointly written across both debate teams. Where the argument grants ground - which is most of the calibrated middle - the grounding comes from Team A's defense of the swiss-cheese position. Where it goes furthest - the bacteria and weaponisation analogies, the halting reduction, and the three research programmes - the move was stress-tested with the group during and after the session. The strength of the argument is the strength of the room.

## Reading list

The arguments above stand on the syllabus the unit set us. The list below is grouped by which side of the debate each piece supplied evidence for; several appear on both sides because the strong work on this question explicitly addresses both.

**The pro-mech-interp case** ([Unit 4.1](https://bluedot.org/courses/technical-ai-safety/4/1) and [Unit 4.2](https://bluedot.org/courses/technical-ai-safety/4/2)).

- Sarah Hastings-Woodhouse, [Introduction to Mechanistic Interpretability](https://blog.bluedot.org/p/introduction-to-mechanistic-interpretability) (2024). The unit's framing piece for why looking at internals matters at all.
- Robert Wiblin and Neel Nanda, [The race to read AI minds](https://80000hours.org/podcast/episodes/neel-nanda-mechanistic-interpretability/) (2025). The clearest articulation of the WILL position from inside the field.
- Sarah Hastings-Woodhouse, [What are probing classifiers](https://blog.bluedot.org/p/what-are-probing-classifiers) (2025). The bridge from "look inside" to "extract a usable signal".
- Adly Templeton, Tom Conerly, et al., [Scaling Monosemanticity](https://transformer-circuits.pub/2024/scaling-monosemanticity/) (2024). The strongest current demonstration that features extracted from a frontier model behave as the WILL position predicts they should, with explicit treatment of where the technique still strains.
- Lindsey et al., [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) (2025). Attribution graphs as a step beyond per-feature analysis.
- Hubinger et al., [Model Organisms of Misalignment](https://www.alignmentforum.org/posts/ChDH335ckdvpxXaXX/model-organisms-of-misalignment-the-case-for-a-new-pillar-of-1) (2023). The structural argument that interp is a research instrument, not just a diagnostic.
- Marks et al., [Auditing language models for hidden objectives](https://www.lesswrong.com/posts/wSKPuBfgkkqfTpmWJ/auditing-language-models-for-hidden-objectives) (2025). Existence proof that interp can surface objectives behavioural probing misses.
- Obeso et al., [Hallucination Probes](https://www.hallucination-probes.com/) (2025). Concrete present-day diagnostic value.

**The skeptical case** (also on the unit's reading list, mostly as optional).

- Dan Hendrycks and Laura Hiscott, [The Misguided Quest for Mechanistic AI Interpretability](https://aifrontiersmedia.substack.com/p/the-misguided-quest-for-mechanistic) (2025). The unit's required-reading critique of the strong claim.
- Charbel-Raphael Segerie, [Against Almost Every Theory of Impact of Interpretability](https://www.alignmentforum.org/posts/LNA8mubrByG7SFacm/against-almost-every-theory-of-impact-of-interpretability-1) (2023). Argument-by-argument rebuttal of why interp closes the gap to safety.
- Connor Leahy, [Barriers to Mechanistic Interpretability for AGI Safety](https://www.youtube.com/watch?v=wKI9hmaIbpg) (2023). Explicit list of the structural obstacles, several of which this post relies on.
- Neel Nanda, [Interpretability Will Not Reliably Find Deceptive AI](https://www.lesswrong.com/posts/PwnadG4BFjaER3MGf/interpretability-will-not-reliably-find-deceptive-ai) (2025). The most striking thing about this piece is that the field's most articulate proponent draws a hard limit himself.
- Korbak et al., [Chain of Thought Monitorability](https://arxiv.org/pdf/2507.11473) (2025). Framework paper for argument 6 above; analyses the failure modes when the model has incentive to evade.
- Scott Alexander, [Let's Try To Understand AI Monosemanticity](https://www.astralcodexten.com/p/god-help-us-lets-try-to-understand) (2023). Accessible explanation of the polysemanticity problem and why the SAE programme exists.
- Farr et al., [MoSSAIC: AI Safety After Mechanism](https://openreview.net/pdf?id=n7WYSJ35FU) (2025). Sketch of what an AI-safety programme that is not centred on mechanistic interpretability would look like.

The session also engaged Bogdan et al., [Thought Anchors: Which LLM Reasoning Steps Matter?](https://arxiv.org/pdf/2506.19143) (2025), and the [ARENA Curriculum on transformer interpretability](https://arena-chapter1-transformer-interp.streamlit.app/), which we treated as orientation for the techniques discussed rather than as direct evidence in the debate.

For the broader frame on evaluations and frameworks this post inherits, see the companion piece [*To Be or to Game*]({% post_url 2026-05-07-to-be-or-to-game %}).
