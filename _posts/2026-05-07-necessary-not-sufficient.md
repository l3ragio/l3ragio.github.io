---
title: "Necessary, not sufficient"
date: 2026-05-07T09:30:00+02:00
categories: [ai-safety]
tags: [mechanistic-interpretability, interpretability, debate, bluedot, ai-safety]
description: "Six arguments against the strong claim that mechanistic interpretability will lead to safe AI. Notes from the BlueDot Unit 4 debate."
math: false
---

> **TL;DR.** In Unit 4 of the BlueDot Technical AI Safety course, my team (Liz Tan, Joy Yang, and myself) was assigned to defend the position that mechanistic interpretability *will not* lead to safe AI. Six arguments are worth carrying out of that debate. Each is independently sufficient to undermine the strong claim that mech interp is *the* path. None denies that it is a useful diagnostic. The conclusion is calibration, not dismissal: mech interp is a load-bearing component of the safety stack, not the spec for the whole stack.
{: .prompt-tip }

## The proposition

The unit's closing exercise asked the group to defend one of two positions: *Mechanistic interpretability techniques will lead to safe AI models* (Team A: Lucas, Abdullah, Janhavi, Avni), or *Mechanistic interpretability techniques will not lead to safe AI models* (Team B: Liz Tan, Joy Yang, myself). The framing matters. The claim under contention is not "mech interp is useful". Few researchers in the room would have disputed that. The claim is whether mech interp, pursued to its limits, gets us all the way to safe deployment of frontier systems. Our six arguments target the second claim.

## 1. The "complete understanding" assumption is very strong

The implicit promise of mech interp at its strongest reading is that there exists a mathematical theory which can be applied to any sufficiently complex model and yield complete understanding of its computation. That is a very big assumption. There is no current candidate for such a theory, and the historical analogue (full decomposition of biological neural systems) has not delivered after decades of work. Treating mech interp as the path to safe AI presupposes a tool we have not built and may not be able to build.

## 2. Polysemanticity is not just a research nuisance

Polysemantic neurons store multiple unrelated concepts in superposition. The standard mech interp hope is that sparse autoencoders and related techniques will eventually disentangle them into monosemantic features. But polysemanticity means some dimensions in activation space may correspond to concrete safety-relevant concepts (e.g., "the model is being deceptive") tangled with unrelated capability concepts. Recovering the safety-relevant signal requires a clean decomposition we do not yet have at frontier scale. Until we do, every claim of the form "we found the deception feature" is an overclaim against the polysemantic baseline.

## 3. Removing the bad dimensions removes the good ones too

Suppose we accept the optimistic case: we find activation directions correlated with misaligned behaviour, and we have a mechanism to suppress them. The next problem is that capability and behaviour are not orthogonally encoded. Removing dimensions associated with deception or harmful planning may strip out reasoning the model needs for legitimate tasks. The intervention either degrades capability (and so will be reverted in production) or fails to fully suppress the behaviour (and so does not deliver the safety guarantee). There is no current evidence that the safe slice and the capable slice can be cleanly separated.

## 4. The techniques do not scale to frontier models

Circuit tracing, attention pattern analysis, and feature attribution were developed on small to medium transformers. Application to frontier-scale models lags capability by months to years, and the gap appears to be widening, not narrowing. Anthropic and DeepMind teams have publicly acknowledged the scale problem; some labs that previously bet heavily on SAEs have reduced or pivoted that effort. A method that arrives at understanding six months after the model has been deployed does not constitute a safety technique in the deployment-time sense.

## 5. The threat is sometimes not the model

A class of frontier models is built for legitimate research: chemistry models for drug discovery, biology models for protein design, code models for engineering productivity. The same models can be misused by adversaries to design weapons or attacks. If the model weights are stolen, leaked, or open-released, mechanistic interpretability of those weights does nothing to prevent misuse. The threat model where the danger lies in *who has access to the model*, not in the model's intrinsic alignment, is fully outside what interp techniques can address. Safe AI in the broad sense has to cover this case, and mech interp does not.

## 6. Sufficiently capable models can route around the monitor

Suppose all the previous problems are solved at some future date: we identify activation spaces corresponding to unwanted behaviours, and we monitor them in real time. A sufficiently capable model could learn to express the same computation through a different activation space, one we have not flagged. This is the mech-interp analogue of the chain-of-thought faithfulness problem: any monitored channel becomes an optimization target the moment the model has an incentive to evade detection. Our oversight is only as good as our coverage of the routing space, which grows combinatorially with model size.

## What the other side argued

Team A's strongest line was not that mech interp will solve safety, but that *every other safety technique either depends on it or is incomplete without it*. Behavioural evaluations cannot distinguish "the model is safe" from "the model has not yet been incentivised to misbehave". Only inspection of internals can. Diagnoses through interp findings have, in Joy's reflection, real value even when they do not deliver guarantees. Lucas characterised mech interp as the icing on the cake, or as the swiss-cheese layer no other slice replaces. That is a defensible reading of the field's current trajectory and, I think, the most calibrated form of the WILL position. The disagreement is not about whether mech interp matters. It is about whether it carries the load alone.

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

The first is a geometric or algebraic theory of representations strong enough to underwrite verifiable claims about model behaviour. The lineage from word2vec-style distributed representations through to current work on linear feature directions has visible momentum: the linear representation hypothesis (Park, Choe, Veitch, 2023) and the activation-steering literature converge on the conjecture that concepts compose linearly, transfer across models, and decompose under sparse projections. If that conjecture holds at frontier scale, it gives us the substrate for the formal claim mech interp currently lacks. Polysemanticity becomes an algebraic obstacle, not an empirical mystery; capability and behaviour become directions in a structured space rather than entangled by accident.

The second is a *science of evaluations* in the strong sense - a methodology that says, given an interpretability finding *F*, here is the safety claim *S* we are entitled to assert, with explicit boundary conditions and adversarial robustness guarantees. This is the hinge between mech interp and safety. Every operational concern in the six arguments is at base an instance of "we cannot currently make that inference". This is also the bottleneck I identified in [To Be or to Game]({% post_url 2026-05-07-to-be-or-to-game %}) from a different angle, and the two arguments meet here.

The third is an ecosystem-level theory that does for cross-system dynamics what mech interp does for per-model internals. We do not have one. The absence of a candidate is not a proof that none exists, but the field probably spends the next decade here.

The action item I take from the unit is to track which interpretability findings can certify which kinds of safety claims, and how that maps onto formally verifiable properties at both the per-model and the ecosystem level. None of the three programmes is closed; each is an open target. The WILL NOT verdict converts cleanly into a list of things worth building, and the magnitude of that list is the actual content of the position.

## Acknowledgements

Co-defenders: Liz Tan and Joy Yang. Course context: BlueDot Technical AI Safety, Unit 4 (Understanding AI), discussion group 03. Thanks to Caroline for facilitating, and to Lucas, Abdullah, Janhavi, and Avni for arguing the strongest version of the WILL position.
