---
title: "To Be or to Game"
date: 2026-05-07T00:30:00+02:00
categories: [ai-safety]
tags: [evaluations, science-of-evals, ai-deception, governance, formal-methods]
description: "An answer for the need of the Science of Evals."
math: true
---

> **TL;DR.** Evals are the bottleneck of AI safety, and the field knows it. The problem is doubly hard because the evaluation domain is computationally infinite and the subject of evaluation can game the evaluator. The solution shape is a top-down tiered governance that constrains deception level by level, a bottom-up axiomatisation that recovers properties from the most computationally constrained environments, and a meet-in-the-middle effort that ties the two. This post sketches that shape and ends with three practical ways the work can begin.
{: .prompt-tip }

## The problem

The word "evaluation" is doing a lot of work that nobody has sorted out properly. Each paper, each benchmark, each company defines its own implicit notion of what is being measured. There is no shared formal specification of what an evaluation should certify. Apollo Research's *We need a Science of Evals* lays out the diagnosis cleanly: the field is closer to a best-practice checklist than to a science.

I am writing this partly because I have a stake in it. While serving as an AI Risk Management Framework Expert at the United Nations Joint Staff Pension Fund (UNJSPF), I have proposed a solution that is on its way to publication. The framing in this post grew out of that work: a structural answer to why a science of evals is hard, and what a viable starting point looks like.

## Evaluation is everywhere science is

Evaluation is not exotic. It is the everyday discipline of any mature field.

Particle physics has the Standard Model, a body of falsifiable predictions, and a global experimental apparatus that evaluates the model against nature year after year. Mathematics has proof systems and peer review. Engineering has reliability standards. Risk management has frameworks (ISO 31000, NIST AI RMF, the EU AI Act risk tiers, METR's five-criterion rubric for frontier safety policies, and the four corporate frameworks of Anthropic, OpenAI, Google DeepMind, and Meta). Every mature field has converged on some way to evaluate its own claims.

AI has not yet. The pattern, then, is not "AI needs something new"; it is "AI needs the analogue of what every other field eventually built". The question is what that analogue looks like.

## The shape of the solution: divide et impera

The classical move in front of an intractable domain is to divide and conquer. Two complementary halves: a top-down side that governs the problem as it grows, and a bottom-up side that recovers axioms from the simplest computationally constrained settings. They meet in the middle.

## Does it work?

Three structural difficulties stand in the way before we can claim that this shape works.

**The domain is computationally infinite.** Every eval introduces the need for new evals. Patch one capability and a downstream behaviour appears. The field will never finish.

**Yet we can start anyway.** Bottom-up, the axioms are buildable. Top-down, a process can govern the growth. We do not need a closed-form solution to the whole domain to start the work.

**There is an elephant in the room: gaming.** What if the subject of the evaluation games the evaluator? Particle physics teaches that experiments can depend on the presence of the observer (the evaluator in our case). AI evaluation is meeting this advanced setting now. Comparing chain-of-thought traces with the final chatbot answer reveals subjects that behave differently when they realise they are being watched, or that produce reasoning intended to be inspected separately from the action they actually take.

So we are solving a problem that is infinitely complex, evolves through time, and may attempt to game us.

## The computational way

Cryptography crossed a similar threshold around 1985, when soundness definitions turned a collection of clever ideas into a field with theorems. The bet here is the same: model the problem as computationally constrained, build definitions that admit theorems, and let practice close the gap behind the theory.

### Top-down: governance that grows with the problem

Establish a process that takes care of the problem while it grows. Model deception as a tiered phenomenon and impose constraints tier by tier.

- **Tier 1.** If the chain of thought is the place where the agent can be deceptive, impose constraints on the chain of thought and monitor it.
- **Tier 2.** If the agent is observing its own chain of thought and manipulating it to be deceptive, locate where and how this mechanism happens, impose constraints there, and monitor.
- **Tier ...**
- **Tier N.** We do not know whether an ultimate tier exists. We do know three things.

   1. We can attempt to model a solution that converges to acceptable overall behaviour. Even when the agent is deceptive, if our governance is good enough, the agent ends up "believing it is being clever and deceptive while in fact staying at our rules trying to cover its deceptive abilities".
   2. We can assume that an agent acts deceptively because it has a positive feedback loop for doing so. Cut the feedback.
   3. We can show that the likelihood of harmful behaviour under these conditions is negligible. Concretely:

      $$\Pr(\text{harm} \mid \text{constraints}) \le \mathrm{negl}(n)$$

      where $n$ is a security parameter that scales with the resources we put into monitoring and constraint enforcement.

This is not yet rigorous, but it is the right shape: a tiered, adversarially aware, asymptotic safety claim that mirrors how cryptography first established its own foundations.

### Bottom-up: become the Eulers of Evaluations

The bottom-up half is more fascinating. We need to define the axioms of the science of evals: what is a property to be evaluated, what does it mean to evaluate it, what are the closure conditions of such a notion under composition.

Writing a general solution that works across fields (physics, mathematics, biology) sounds prohibitively complex for the current state of the episteme. How do we manage quantum entanglement, mathematical nonlinearities, unpredictable biological mutations?

We simplify. (Are we gaming the topics?)

We write down how properties emerge from the most computationally constrained environments we know: bits, binary circuits, formal methods. From there we build upward. Mathematics has a precedent: most of analysis can be reconstructed from set-theoretic foundations, even if the working mathematician rarely descends to that level. The science of evals can do the same.

## Meet-in-the-middle

Once both directions are running, we work them toward each other. The top-down governance descends from policy to implementation; the bottom-up axiomatisation ascends from primitives to richer properties. The two efforts meet in the middle, much like a meet-in-the-middle attack on a hash function, except the output length is conceptually infinite. Every meeting fixes a property; the next iteration extends the construction further.

## How do we start?

This is the part that worries people the most, and it is the part with the cleanest answer.

The answer is: by starting. Once we start, the belief that there is a solution to be found populates our minds, and the solution starts moving toward us until we meet.

That sounds light, but it is the core observation. Most of the activation energy in a new field is spent before anyone has agreed on what to begin doing. Once a few teams begin, the rest of the field can criticise, extend, and converge.

## Three practical ways the work can start

Three near-term routes that, if any one of them succeeds, suffice to move the field from pre-formal to formal.

1. **A regulator demands formalised eval specs.** Government intervention forces standardisation. Plausible in jurisdictions already drafting AI policy (EU AI Act, UK AISI work, US executive orders). Specifications become the regulatory artifact, not lab choice. This is the most likely near-term route, because labs respond to regulation faster than they respond to academic results.

2. **A lab finds a technique that requires comparing benchmarks formally.** Some methodology, perhaps automated red teaming or cross-model contamination detection, only works when benchmarks share a specification language. Once one lab uses it, others have to adopt or be left behind.

3. **A paper proves a soundness theorem.** Specifically a result of the form

   $$\Pr(\text{adversary fools the eval}) \le \varepsilon$$

   under stated conditions. Once that exists for one eval, follow-up papers either match the theorem or explain why theirs cannot. The theorem becomes the new floor.

Any one of them suffices. None of them have happened yet. The field is in stable disequilibrium.

## Closing thought

AI evaluation today is roughly where cryptography was in the early 1980s: plenty of techniques, lots of empirical findings, no soundness definitions. Soundness arrived for cryptography around 1985 and the field has been formal ever since. There is no reason a similar transition cannot happen for evaluations, especially if the work is divided properly between a top-down governance that grows with the problem and a bottom-up axiomatisation that anchors it to computationally constrained foundations. The papers that will close the gap are probably being written now. Some of them might not be written by humans alone.

## Acknowledgements

Thanks to [BlueDot Impact](https://bluedot.org/courses/technical-ai-safety) for the Technical AI Safety course. The structural framing of this post grew out of discussions in two of its live sessions on Unit 3. The four-framework side-by-side reading paired with METR's five-criterion rubric is the design move that surfaced the framework-downstream-of-evaluations observation that anchors the analysis.

The proposal mentioned in the introduction was developed in the context of my role as AI Risk Management Framework Expert at the United Nations Joint Staff Pension Fund (UNJSPF) and is being prepared for publication.

## References

- Apollo Research, *We need a Science of Evals*.
- BlueDot Impact, [Technical AI Safety course](https://bluedot.org/courses/technical-ai-safety).
- METR, frontier safety framework rubric (limits, protections, evaluation, response, accountability).
- Anthropic Responsible Scaling Policy, OpenAI Preparedness Framework, Google DeepMind Frontier Safety Framework, Meta Frontier AI Framework.
