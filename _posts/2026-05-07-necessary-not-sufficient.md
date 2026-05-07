---
title: "Necessary, not sufficient"
date: 2026-05-07T22:30:00+02:00
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

## Where I land after the debate

The strong claim (mech interp will lead to safe AI) is not supported by current evidence. Each of the six arguments above is independently sufficient to block it. The weaker claim (mech interp is necessary, even if not sufficient) is harder to refute and probably correct. The debate exercise is useful precisely because it forces this distinction. Treating mech interp as the spec for safe AI overcommits; treating it as an irreplaceable diagnostic layer in a defence-in-depth strategy is consistent with what the field has demonstrated so far.

The action item I am taking from the unit is to track which interpretability findings can certify which kinds of safety claims, and how that maps onto formally verifiable properties. The relationship between an interp finding and a verifiable guarantee is still the bottleneck on whether mech interp graduates from "valuable evidence" to "load-bearing layer of the safety stack". This is the same diagnosis I sketched in [To Be or to Game]({% post_url 2026-05-07-to-be-or-to-game %}): frameworks live downstream of the methodology that supports them, and the methodology is what we are still building.

## Acknowledgements

Co-defenders: Liz Tan and Joy Yang. Course context: BlueDot Technical AI Safety, Unit 4 (Understanding AI), discussion group 03. Thanks to Caroline for facilitating, and to Lucas, Abdullah, Janhavi, and Avni for arguing the strongest version of the WILL position.
