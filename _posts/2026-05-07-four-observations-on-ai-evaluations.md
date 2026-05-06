---
title: "Four Observations on AI Evaluations from BlueDot Unit 3"
date: 2026-05-07T10:00:00+02:00
categories: [ai-safety]
tags: [evaluations, risk-management, frontier-ai, bluedot, science-of-evals]
description: "What 'eval' actually means, what would close the proprietary benchmark gap, why frameworks live downstream of evaluations, and one bootstrap proposal worth testing."
---

> **TL;DR.** AI evaluation today is roughly where cryptography was in the early 1980s. We have plenty of techniques but no shared soundness definition. Risk management frameworks inherit the gaps of the evaluations they reference, and frontier models themselves may be the production engine for the formal specification we are missing.

I am partway through the BlueDot Technical AI Safety course, through the unit on detecting danger and how AI companies test for safety. The unit covers four risk management frameworks (Anthropic, OpenAI, Google DeepMind, Meta), three categories of artifact (risk management policies, system cards, red team reports), and the field wide question of what counts as a rigorous evaluation. Across two live discussions on the unit I left a set of comments in the shared docs that I want to expand here, because they got at something I think is worth saying out loud.

## What "evaluation" actually means

The first observation. The word "evaluation" is doing a lot of work that nobody has sorted out properly. Each paper, each benchmark, each company defines its own implicit notion of what is being measured. There is no shared formal specification of what an evaluation should certify. Apollo Research's *We need a Science of Evals* lays the diagnosis out cleanly. The field is closer to a best practice checklist than to a science.

What I would add to the diagnosis. We are advancing toward a common specification framework, slowly. The four frameworks this unit covers are converging on a small shared vocabulary (capability thresholds, mitigations, deployment gates, accountability mechanisms). Even where they disagree on substance, they agree on the question shape. That is progress. A minimum set of metrics across semantic areas is emerging, even if no two frameworks measure the same thing.

The way to read this. We are between phases. The pre formal phase (everyone defining their own thing) is mostly behind us. The formal shared phase (one specification language the field agrees on) is not yet here. We are in the messy in between, where labs converge informally and the open question is whether the convergence will stabilise into a real standard.

## What would close the gap

The second observation, in question form. What would it actually take to close the gap between proprietary benchmarks and a shared formal spec? I see three plausible scenarios.

**A. A regulator demands formalised eval specs.** Government intervention forces standardisation. Plausible in jurisdictions already drafting AI policy (EU AI Act, UK AISI work, US executive orders). Specifications become the regulatory artifact, not lab choice.

**B. A lab finds a technique that requires comparing benchmarks formally.** Some methodology, maybe automated red teaming or cross model contamination detection, only works if benchmarks share a specification language. Once one lab uses it, others have to adopt or be left behind.

**C. A paper proves a soundness theorem.** Specifically, a result of the form

```text
Pr(adversary fools the eval) <= epsilon
```

under stated conditions. Once you have that for one eval, follow up papers either have to match the theorem or explain why theirs cannot. The theorem becomes the new floor.

Any one of the three would probably suffice. What is interesting is that all three are imaginable but none of them have actually happened yet. The field is in a stable disequilibrium. The strongest near term force toward closure is probably (A), because regulators are moving and labs respond to regulation faster than they respond to academic results.

## Frameworks live downstream of evaluations

The second live session reframed the discussion. We started critiquing the four risk management frameworks individually, and ended up noticing a structural pattern. Each framework's weakest area in METR's five criterion rubric (limits, protections, evaluation, response, accountability) reflects where the underlying evaluation methodology is least mature. The frameworks are downstream of the evaluations they rely on. Build a framework on top of a methodology that has structural gaps and you inherit those gaps as framework gaps.

The implication. An ideal risk management framework cannot be designed top down by smart people in a room. It has to wait for the evaluation methodology to mature underneath it. Only then can a framework that covers every threat in every semantic area become possible. The session collapsed the framework conversation into the evaluation conversation one layer up. Critiques of any specific framework are mostly critiques of the evaluation methodology that framework references, dressed in policy language.

This raises an obvious next question. If the formal specification is the bottleneck, why are we waiting for it? One answer worth testing. Frontier AI models themselves may be the production engine for the specification. Set up a tightly bounded specification task where the model is given a target objective (produce a candidate framework), a set of rules on how the framework must be written, and a list of ideal properties the output must satisfy (completeness across semantic areas, falsifiability of each constraint, formal specification language). The hypothesis is that current frontier models, given a well constrained specification task, can produce candidate formal specifications faster than a human committee can. Worth testing in a small scope first, one threat category and one semantic area, before scaling. This is itself an experiment in using AI to bootstrap the conditions for AI safety. It could go very right or very wrong depending on whether the constraints on the specification task are themselves specified well enough to bind the output.

## The limitation worth flagging

The third observation. Even if the gap closes for simple usecases, there is no guarantee the formal specification generalises cleanly. A spec that works for text only single turn evaluations may not generalise to multimodal models, agentic deployments, or long horizon scenarios. The specification language might end up describing one slice of the problem while another slice grows uncovered.

Worse, closing one specification gap can open another. Once you have a formal spec for capability evaluation, you might find you need a different specification for propensity evaluation. Once you have both, the question of how they compose becomes its own specification problem. The chain extends.

This is not an argument against formalisation. It is an argument for staying realistic about what formalisation buys. The first formal spec will not be the last one, and the lab that publishes it will probably have to publish a v2 within two years.

## Closing thought

The unit's lesson, compressed, is that AI evaluation today is roughly where cryptography was in the early 1980s. We have plenty of techniques, lots of empirical findings, and a growing number of papers. We do not yet have the soundness definitions that turned cryptography from a collection of clever ideas into a field with theorems. Soundness arrived for cryptography around 1985 and the field has been formal ever since. There is no reason a similar transition cannot happen for evaluations.

The bet I would make. The transition will happen sooner if frontier models are part of the production engine, with constrained specification tasks and clear target properties. The papers that are going to do it are probably being written now, but they may not be written by humans alone. The action I am taking, set up a small scope experiment on that bootstrap path and report back when there is something worth saying.

## Acknowledgements

Thanks to [BlueDot Impact](https://bluedot.org/courses/technical-ai-safety) for the Technical AI Safety course and the materials the team pulls together. The two live discussions that produced these observations are part of the course's format, shared documents plus seven minute breakout pairs plus a short reflection round. That structure is well designed to surface structural insights I would not have reached reading the source material alone. The four framework side by side reading in Unit 3 (Anthropic, OpenAI, Google DeepMind, Meta) paired with METR's five criterion rubric is the specific design move that made the frameworks downstream of evaluations observation possible.

## References

- Apollo Research, *We need a Science of Evals*.
- BlueDot Impact, [Technical AI Safety course](https://bluedot.org/courses/technical-ai-safety).
- METR, frontier safety framework rubric (limits, protections, evaluation, response, accountability).
- Anthropic Responsible Scaling Policy, OpenAI Preparedness Framework, Google DeepMind Frontier Safety Framework, Meta Frontier AI Framework (links on each lab's safety page).
