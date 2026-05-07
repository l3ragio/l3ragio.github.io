---
title: "To Be or to Game"
date: 2026-05-07T00:30:00+02:00
categories: [ai-safety]
tags: [evaluations, science-of-evals, ai-deception, governance, formal-methods]
description: "An answer for the need of the Science of Evals."
math: true
image:
  path: /assets/img/heroes/to-be-or-to-game.png
  alt: "Tiered tower under construction with figures negotiating, an oversight eye, scales of justice, and scaffolding - allegory for the layered structure of AI evaluation."
  lqip: data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiA5Ij48cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iOSIgZmlsbD0iI2QyYzdhYyIvPjwvc3ZnPg==
---

> **TL;DR.** Evals are the bottleneck of AI safety, and the field knows it. The problem is doubly hard because the evaluation domain is computationally infinite and the subject of evaluation can game the evaluator. The solution shape is a top-down tiered governance that constrains deception level by level, a bottom-up axiomatisation that recovers properties from the most computationally constrained environments, and a meet-in-the-middle effort that ties the two. This post sketches that shape and ends with three practical ways the work can begin.
{: .prompt-tip }

## The problem

The word "evaluation" is doing a lot of work that nobody has sorted out properly. Each paper, each benchmark, each company defines its own implicit notion of what is being measured. There is no shared formal specification of what an evaluation should certify. Apollo Research's *We need a Science of Evals* lays out the diagnosis cleanly: the field is closer to a best-practice checklist than to a science. Stein-Perlman's [AI Lab Watch](https://ailabwatch.org/) makes the diagnosis concrete by attempting an external side-by-side comparison of the major labs' safety claims, and the very need for such a dashboard signals that there is no agreed internal rubric the labs can be measured against from inside the field.

I am writing this partly because I have a stake in it. While serving as an AI Risk Management Framework Expert at the United Nations Joint Staff Pension Fund (UNJSPF), I have proposed a solution that is on its way to publication. The framing in this post grew out of that work: a structural answer to why a science of evals is hard, and what a viable starting point looks like.

## Evaluation is everywhere science is

Evaluation is not exotic. It is the everyday discipline of any mature field.

Particle physics has the Standard Model, a body of falsifiable predictions, and a global experimental apparatus that evaluates the model against nature year after year. Mathematics has proof systems and peer review. Engineering has reliability standards. Risk management has frameworks: ISO 31000, NIST AI RMF, the EU AI Act risk tiers, METR's five-criterion rubric for frontier safety policies (limits, protections, evaluation, response, accountability), and the four lab-internal frameworks the field reads side by side, Anthropic's Responsible Scaling Policy, OpenAI's Preparedness Framework, Google DeepMind's Frontier Safety Framework, and Meta's Frontier AI Framework. Every mature field has converged on some way to evaluate its own claims.

AI has not yet. The pattern, then, is not "AI needs something new"; it is "AI needs the analogue of what every other field eventually built". The question is what that analogue looks like.

## The shape of the solution: divide et impera

The classical move in front of an intractable domain is to divide and conquer. Two complementary halves: a top-down side that governs the problem as it grows, and a bottom-up side that recovers axioms from the simplest computationally constrained settings. They meet in the middle.

## Does it work?

Three structural difficulties stand in the way before we can claim that this shape works.

**The domain is computationally infinite.** Every eval introduces the need for new evals. Patch one capability and a downstream behaviour appears. The field will never finish.

**Yet we can start anyway.** Bottom-up, the axioms are buildable. Top-down, a process can govern the growth. We do not need a closed-form solution to the whole domain to start the work.

**There is an elephant in the room: gaming.** What if the subject of the evaluation games the evaluator? Particle physics teaches that experiments can depend on the presence of the observer (the evaluator in our case). AI evaluation is meeting this advanced setting now. Anthropic's Claude Opus 4.6 system card devotes a section to white-box probes for "eval-context recognition", measuring whether the model can tell it is being evaluated. Comparing chain-of-thought traces with the final chatbot answer reveals subjects that behave differently when they realise they are being watched, or that produce reasoning intended to be inspected separately from the action they actually take. The gaming question has moved from thought experiment to instrumentation problem.

So we are solving a problem that is infinitely complex, evolves through time, and may attempt to game us.

## The computational way

Cryptography crossed a similar threshold around 1985, when soundness definitions turned a collection of clever ideas into a field with theorems. The bet here is the same: model the problem as computationally constrained, build definitions that admit theorems, and let practice close the gap behind the theory.

### Top-down: governance that grows with the problem

Existing lab frameworks already lean on tiered structures, but along a different axis. Anthropic's RSP defines AI Safety Levels (ASL 1 through 5+) keyed to capability thresholds. Google DeepMind's Frontier Safety Framework defines Critical Capability Levels per risk domain (cyber, bio, ML R&D, persuasion, autonomy). OpenAI's Preparedness Framework assigns Low, Medium, High, or Critical per category, distinguishing pre-mitigation from post-mitigation risk. Meta's Frontier AI Framework classifies outcomes as high-risk or critical-risk, gating the open-weight release decision. These are tiers of capability or outcome. The proposal here is orthogonal: tier the deception mechanism itself, not the capability level.

Establish a process that takes care of the problem while it grows. Model deception as a tiered phenomenon and impose constraints tier by tier.

- **Tier 1.** If the chain of thought is the place where the agent can be deceptive, impose constraints on the chain of thought and monitor it.
- **Tier 2.** If the agent is observing its own chain of thought and manipulating it to be deceptive, locate where and how this mechanism happens, impose constraints there, and monitor.
- **Tier ...**
- **Tier N.** We do not know whether an ultimate tier exists. We do know three things.

   1. We can attempt to model a solution that converges to acceptable overall behaviour. Even when the agent is deceptive, if our governance is good enough, the agent ends up "believing it is being clever and deceptive while in fact staying at our rules trying to cover its deceptive abilities".
   2. We can assume that an agent acts deceptively because it has a positive feedback loop for doing so. Cut the deceptive feedback, and mirror the move on the honest side: shape the incentive landscape so the agent prefers behaviour the evaluator can verify. The mechanism-design precedent is established. Bitcoin and Algorand do not theoretically exclude attacks on the chain; they reduce attacks to negligible by aligning every participant's incentive toward honest behaviour, block rewards conditional on honest mining in Bitcoin, validator stake bound to correct attestation in Algorand. The same move applies here: not only remove the reward for fooling the evaluator, route it (with interest) to behaviour that exposes itself to verification.
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

## Limitations

Two honest constraints on the approach are worth naming.

**Practical solutions may not scale across tiers.** It is feasible to build immediate, concrete interventions at any single tier (Tier 1 chain-of-thought monitoring is largely tractable today, for example). The harder claim is that a working Tier 1 solution generalises to Tier 2, where the agent is reasoning about its own chain of thought. The mechanisms differ, the instrumentation differs, and the cost of intervention may grow non-linearly with tier depth. We can win locally without winning globally.

**Solving the formula on specific parameters may not generalise.** The negligibility statement $\Pr(\text{harm} \mid \text{constraints}) \le \mathrm{negl}(n)$ is an instance schema. Proving it for a specific (model, capability, deployment) tuple may be computationally demanding, and the proof may be silent on neighbouring instances. A soundness bound for text-to-text models tells us little about text-to-image, image-to-image, or video-to-action settings. Multimodal and agentic deployments may each need their own re-derivation. Existing frameworks already partition risk by modality or domain (Google DeepMind's Frontier Safety Framework runs separate Critical Capability Levels for cyber, bio, ML R&D, persuasion, autonomy; Meta's Llama Guard is a content classifier, not an alignment-behaviour evaluator), and the partitions exist precisely because no general specification has been found. The science of evals risks being modality-specific in the same way that early cryptography was algorithm-specific before the field abstracted up to indistinguishability arguments.

These limitations do not invalidate the shape of the solution. They set realistic expectations about how slowly the formal frontier will advance, and where the field should pour effort.

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

The following resources, surveyed during the BlueDot Technical AI Safety course Unit 3, were used as concrete anchors for the claims above.

**Cross-lab and methodology.**

- Apollo Research, *We need a Science of Evals*. The diagnostic piece on why the field lacks a shared formal specification.
- Stein-Perlman, [AI Lab Watch](https://ailabwatch.org/). External side-by-side dashboard of safety practices across labs.
- METR, *Responsible Scaling Policies* (2023). Source of the five-criterion rubric (limits, protections, evaluation, response, accountability) the field now reads RSPs against.

**Anthropic.**

- *Responsible Scaling Policy* v3 (2026). AI Safety Levels (ASL 1 to 5+) with capability thresholds and required protective measures per level.
- *System Card Claude Opus 4.6*, section 8 (2026). Documented safety evaluations for a flagship release, including white-box probes for eval-context recognition, persuasion-versus-truth measurements, and capability uplift evaluations on autonomy, biosecurity, and cybersecurity.
- *Threat Intelligence Report* (2025). Real-world misuse attempts observed against deployed Anthropic models.
- The Long-Term Benefit Trust (LTBT). Independent governance body with authority over key strategic decisions.

**OpenAI.**

- *Preparedness Framework* v2 (2025). Tracked categories (Cybersecurity, Biosecurity, Persuasion, Autonomy) with risk levels (Low, Medium, High, Critical) and pre- versus post-mitigation evaluation.
- *GPT-5 System Card*, section 5 (2025). Cross-lab counterpart to the Opus 4.6 safety evaluations.
- The Safety Advisory Group, OpenAI's deployment-decision body.

**Google DeepMind.**

- *Frontier Safety Framework* v2.0 (2025). Critical Capability Levels per risk domain (cyber, bio, ML R&D, persuasion, autonomy), with explicit acknowledgement of AI-driven AI research as a tracked risk.
- *Gemini 3 Pro Model Card* (2025). Capabilities, evaluations, and safety measures.

**Meta.**

- *Frontier AI Framework* (Feb 2025). Outcome-centric framework focused on the open-weight release decision.
- *Llama Guard 4 Model Card* (2025). Content-moderation model with a defined harm taxonomy, distinct in shape from frontier-model cards.

**Course.**

- BlueDot Impact, [Technical AI Safety course](https://bluedot.org/courses/technical-ai-safety). The four-framework side-by-side reading paired with METR's rubric is the design move that surfaced the framework-downstream-of-evaluations observation underpinning this post.
