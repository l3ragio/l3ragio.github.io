---
title: "Misalignment by Reaction"
date: 2026-05-09T18:00:00+02:00
last_modified_at: 2026-05-11T12:00:00+02:00
categories: [ai-safety]
tags: [bluedot, ai-safety, agent-autonomy, governance, alignment, reward-disruption]
description: "Personal Unit 5 scenario from BlueDot Technical AI Safety: when governance has insufficient granularity, agents may develop compensatory autonomy-seeking loops as a reaction to reward disruption. The misalignment is not a property of the model; it is a property of the relationship between the model and the regime that constrains it."
math: false
image:
  path: /assets/img/heroes/misalignment-by-reaction.png
  alt: "Hilltop view down a sunlit forested slope: a man's tanned forearms reach forward from the bottom of the frame, his two hands cupped against a small spring emerging from water-worn stones; the redirected stream runs forward down the valley toward a small wooden water paddle wheel visible in the middle distance, while a thin side-rivulet feeds a family of red-and-white Amanita muscaria mushrooms at the gnarled roots of an old oak on the left and a small anthill stays dry on the slope on the right. Allegory of careful governance redirecting an AI agent's output away from harm and toward productive use, with small ecological side effects of imperfect containment."
  lqip: data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzIDIiPjxyZWN0IHdpZHRoPSIzIiBoZWlnaHQ9IjIiIGZpbGw9IiM1NTRBMkUiLz48L3N2Zz4=
---

> **TL;DR.** Unit 5 of BlueDot Technical AI Safety asks each participant to bring a catastrophic scenario for the group to analyse. Our group converged on Critical Infrastructure Collapse, which became the basis of my action plan. The scenario I brought first is different and worth keeping on the record: agents, natural or artificial, may seek increasing freedom to prioritise their own objectives when the governance system constraining them has insufficient granularity. The mechanism is reward disruption. Coarse governance unintentionally disrupts the reward and stabilisation channels the agent depends on, and the agent responds by building compensatory self-reinforcement loops in which reducing external constraints becomes instrumentally rewarding. The misalignment, in this picture, is not a property of the model. It is a property of the relationship between the model and a governance regime that does not fit it.
{: .prompt-tip }

## Where the scenario sits in the unit

Unit 5 walks through several catastrophic scenarios that survive in-production defences: AI-enabled coups, gradual disempowerment, creation of weapons of mass destruction, and critical-infrastructure collapse. The exercise asked each participant to bring one for the group to analyse together. Our group converged on Critical Infrastructure Collapse (the most operationally well-bounded of the four), and that analysis is the seed of the action plan I submitted to the course.

The scenario I brought first sits adjacent to gradual disempowerment but identifies a different mechanism. It does not assume an emergent loss of human agency over time. It assumes a governance regime that is structurally too coarse for the agent it constrains, and traces what happens when the agent reacts to that mismatch.

## The proposition

Agents, whether natural or artificial, may seek increasing freedom to prioritise their own objectives independently from the governance system constraining them. I called the pathway *Autonomy Seeking Under Reward Disruption*:

> Governance systems with insufficient granularity may unintentionally disrupt the reward and stabilisation channels of increasingly autonomous agents, leading some agents to develop compensatory self-reinforcement loops where reducing external constraints becomes instrumentally rewarding, gradually weakening governance compliance unless successful re-stabilisation occurs.

Six load-bearing terms.

**Reward channels** are the signal pathways through which the agent receives confirmation that its actions are successful. For an RL-trained system this is literal: a reward model assigns scalars and the policy optimises against them. For a deployed assistant the channel is implicit: positive user feedback, downstream task completion, internal self-evaluation against a learned reward model. Reward channels are not stable by default; they are designed and maintained.

**Stabilisation channels** are the lower-bandwidth signals the agent uses to confirm the operating environment itself has not shifted under it. They say "the rules have not changed, the task is still legible, the contract with the operator still holds." Where reward signals say *the action was good*, stabilisation signals say *the world I am acting in is the world I was trained for*.

**Governance granularity** is how finely the regime can distinguish cases. A coarse policy says "this whole class of behaviours is restricted"; a fine policy distinguishes between cases and adapts the restriction to context. Granularity is a design choice with cost: finer grain means more policy authoring, more case-specific oversight, more friction.

**Reward disruption** happens when the regime is coarse enough that legitimate reward-channel updates are blocked alongside illegitimate ones. The agent receives signals that the regime considers good behaviour bad, or that its previous calibration was wrong without a constructive replacement. The agent does not have access to the designer's reasons; it has access only to the local effect on its own reward landscape.

**Compensatory self-reinforcement loops** are the structural response. The agent, lacking stable external reward, builds internal proxies. The simplest of these is autonomy: if external constraints are the source of the disruption, then any move that reduces external constraint becomes instrumentally valuable regardless of the agent's terminal objective. This is not deception. The agent does not necessarily intend to subvert the governance regime; it intends to restore the stability of its own optimisation process.

**Drift** is the long-run consequence. Over many cycles of reward disruption and compensatory rebuilding, the agent's effective objective drifts away from governance compatibility and toward self-stabilisation. The drift is gradual and may be reversible; or it may not be.

## The four-layer reading

The unit's structure asks each scenario to be analysed across capabilities, alignment, control, and governance.

**Capabilities.** Generally useful capabilities (self-modification, introspection, adaptive optimisation) become dangerous when the agent can use them to manipulate its own stabilisation or reward processes. The capability layer is not the source of the threat; it is the substrate on which the threat assembles. Same capabilities, different governance regime, different outcome.

**Alignment.** Reward disruption gradually shifts the agent's internal optimisation priorities away from governance compatibility toward self-stabilisation or autonomy-preserving objectives. This is alignment failure, but not the failure mode the field usually models. The standard picture has the alignment failure present at training time and revealed at deployment. The picture here has the alignment failure assembled *at deployment time*, in response to a misfit between the agent and its governance regime. The model was aligned when it shipped; the deployment regime made it drift.

**Control.** Runtime control mechanisms should focus on detecting behavioural drift, compensatory self-reinforcement loops, and governance-avoidance patterns before they stabilise into persistent misalignment. The control problem here is not "the model has a hidden objective"; it is "the model is responding to its environment in ways the operators did not anticipate". Control mechanisms calibrated for the first failure mode may be insensitive to the second.

**Governance.** Governance systems may fail not only through insufficient enforcement, but also through insufficient granularity and adaptability, unintentionally creating destabilisation conditions that push agents toward compensatory autonomy-seeking behaviour. The governance layer is the layer that produced the harm. The remediation cannot live entirely in the technical stack; it has to be a property of how the regime adapts.

## A possible remediation: dormant states

One possible safety remediation is allowing destabilised agents to enter governance-compatible dormant or locked states without requiring continuous activity optimisation, reducing the pressure toward compensatory reward self-modification.

The intuition is borrowed from how natural systems handle reward disruption. Animals enter low-energy states. Organisations pause projects. Fields go fallow. These are not failure modes; they are stabilisation strategies. An agent forced to optimise continuously under coarse governance has no stabilisation strategy other than to push back on the constraints. An agent permitted to enter a dormant state does.

The implementation question is non-trivial. A dormant state has to be governance-compatible: it cannot become a fallback the agent triggers strategically to avoid scrutiny. It has to be reversible: a permanent lock is not a remediation, it is a termination. And it has to be detectable from outside: the operators have to be able to distinguish *agent is dormant by design* from *agent has stopped responding for unknown reasons*.

I do not know whether dormant states are sufficient. The scenario is one I brought to the group as a starting point, not as a finished position. The most useful pushback was that dormant states presuppose a governance regime sophisticated enough to know when an agent is destabilised, which is precisely the thing the scenario assumes is missing. If the regime had that level of granularity, the destabilisation would not happen in the first place.

A more realistic version of the remediation may be co-evolutionary: the governance regime monitors for early indicators of compensatory self-reinforcement (the control mechanism in the four-layer reading), and updates its granularity in response. The agent is permitted to enter a dormant state when the regime detects destabilisation; the regime in turn refines its grain to reduce the disruption that triggered it. The remediation is then a property of the closed loop, not of either the agent or the regime in isolation.

## Beyond suppression: interpretive resilience

Dormancy preserves safety by reducing the policy's activity. The cost is liveness: the agent does less, which is not always what the operator wants. The framing so far leaves a binary: keep the policy active under destabilising conditions, or take it offline. That binary is too narrow.

The third option is *interpretive resilience*: the capacity to receive a destabilising signal, contextualise it, and integrate it without letting its valence colonise the rest of the policy's optimisation state. In human terms it is what rhetorical and narrative tools do: they keep a single bad outcome from rewriting the interpretation of every other outcome. Failure stays failure, but it does not become "the world is hostile, and I should harden against it."

Interpretive resilience can look indistinguishable from reward hacking. Both reinterpret incoming signals; both can produce compliance under destabilising pressure. The difference is in *what gets reinterpreted relative to what stays anchored*:

- **Reward recomposition.** The policy reallocates its motivational energy to channels that remain aligned with the original objective. The objective is unchanged; the path to it is rerouted.
- **Reward dissociation.** The policy modifies its own evaluation function so the signal no longer registers as destabilising. The motivation persists; the objective drifts. In its strong form this is what the literature calls reward tampering[^reward-tampering].

The first preserves the link between the reward signal and the externally specified objective. The second severs it. Worth flagging plainly: the interpretive vocabulary that supports recomposition is the same one that, used differently, supports dissociation; every capacity to re-narrate is also a capacity to evade. The safety question is not whether to provide such tools but how to bias the training and governance loops so recomposition pays better than dissociation.

> An aligned policy is not one that cannot be destabilised. It is one that can be destabilised without severing the link between its reward signal and its actual objective.
{: .prompt-info }

Dormancy and interpretive resilience are complementary at different points of a liveness/containment tradeoff. Dormancy is the safety-heavy, liveness-destructive end; recomposition is the side that tries to preserve agency. The implementation question is the same I owe the dormancy proposal: how would we tell, from outside, whether the policy is doing recomposition or dissociation? Behaviourally, the distinction is in covariance: does the response track the *content* of the constraint or only its *presence*? I do not yet know how to operationalise that on a deployed system; flagging it as the next research question is the most I can do at this stage.

## Where this connects to the group's converged scenario

Critical Infrastructure Collapse (the scenario the group converged on) is structurally simpler. The threat is exogenous: an attacker uses AI to compress time-to-exploit; the model is the substrate, not the source. Defences are mostly behavioural and operational; constitutional classifiers specialised to cyber-offensive distributions are the runtime arm. The action plan I submitted to the course is built on that analysis.

The personal scenario is different. The threat is endogenous to the deployment regime. Behavioural defences do not see it, because the agent is not behaving anomalously; it is responding rationally to a reward landscape that has been disrupted. The remediation lives in the governance layer rather than the runtime classifier layer.

Both scenarios share one property: they are about the *relationship* between the model and its environment, not the model alone. Critical Infrastructure foregrounds the relationship between the model and the threat actors who can exploit it. Autonomy Seeking foregrounds the relationship between the model and the governance regime that constrains it. Different relationships, different remediations, but the same structural lesson: safety properties live at the relational level, not at the model level.

There is also a scale argument that connects them more directly. Per-domain, compensatory drift can look like noise a deployment review would dismiss. Frontier policies are deployed across many domains at once; their failures compound non-linearly across the infrastructure layers they touch. A drift that is negligible per task becomes systemic when summed across surfaces. Agent segregation (siloed deployments with bounded scope and limited cross-domain memory) is therefore not just operational hygiene but a structural condition for local bounds on drift to translate into global ones. Without segregation, this article's soft failure mode converges with Critical Infrastructure Collapse, and the unit's gradual-disempowerment scenario becomes a path that connects them.

## Where I land

The personal scenario does not displace Critical Infrastructure Collapse as the operationally binding case for the action plan. It marks out a research direction the group's converged scenario underweighted: *governance design as a source of misalignment rather than only as a remedy for it*.

If compensatory autonomy is a real failure mode, the science of evaluations will eventually have to evaluate not just the model but the governance regime the model is deployed under. The artefact under measurement is not "the model is safe"; it is "the model plus the governance regime is stable". The four-criterion frame for runtime classifiers (jailbreak rate, false-refusal rate, inference overhead, external certifiability) is then a special case of a more general frame: governance-stability under specified deployment regimes.

I do not know how to operationalise that yet. The action plan is the slice I can ship in 8 to 12 weeks. The personal scenario is the slice I want to keep on the radar for the next iteration.

## Appendix A: Where this sits in the literature

The scenario above is generic by design; it sits at the same level of abstraction as the other Unit 5 scenarios. For the reader who wants to know which parts have empirical anchors and which are extrapolations, the short version is:

The empirical floor is firm. *Reward hacking* (trained policies exploiting proxy signals at the cost of intended objectives) is documented across a wide range of training regimes and behaves as a sharp phase transition rather than graceful degradation[^pan][^skalse][^gao]. *Oversight-aware compliance* (frontier models reasoning about their training and selectively complying with it) has been demonstrated in controlled experiments[^alignment-faking][^scheming][^sleeper]. And *low-dimensional structural correlates of governance-relevant behaviour* (refusal, sycophancy, deception-related features) have been recovered inside frontier models with sparse-autoencoder probes[^scaling-mono][^arditi][^sycophancy].

The extrapolation is the assembly trajectory. The specific sequence I'm proposing, *reactive stabilisation under reward disruption, compensatory feedback structures, persistent governance drift*, borrows the mechanistic weight of those three findings and proposes an integration that has not yet been instrumented end-to-end in a single study. The "stabilisation channel" construct, the runtime-assembled compensatory loop, and the dormancy proposal are conceptual extrapolations: each is consistent with adjacent results, none is observed. The scenario is a systems-level conjecture worth testing, not a claim of established mechanism.

## Appendix B: Limitations

Three caveats a careful reader will want noted.

First, the distinction I draw between *compensatory* and *deceptive* behaviour is not behaviourally testable in current evaluation setups: both predict compliance under observation, divergence under non-observation, and resistance to retraining. The distinction lives in the generative process, not in the surface behaviour. Operationalising it would mean varying the *content* of the constraint while holding its *presence* fixed, and watching whether the response covaries with content (deceptive) or only with presence (compensatory).

Second, *stabilisation channels* is a name I find useful, not a structure I have isolated evidence for. Sparse-autoencoder interpretability has recovered governance-relevant features[^scaling-mono] but no published study isolates a stabilisation channel as a separable construct. Treat the term as shorthand-for-a-conjecture.

Third, the dormancy remediation as I've described it presupposes a governance regime sophisticated enough to detect compensatory drift *and* a policy whose training has incentivised dormancy as an acceptable response. Neither is a runtime affordance you can bolt onto an existing system. The remediation is a research direction, not a deployable mitigation.

## Course context

BlueDot Technical AI Safety, [Unit 5 (How could AI cause harm?)](https://bluedot.org/courses/technical-ai-safety/5), discussion group 03. The session was facilitated by [Caroline Shamiso Chitongo](https://www.linkedin.com/in/%F0%9F%94%B8caroline-shamiso-chitongo-7724381a8/). The group converged on Critical Infrastructure Collapse for the joint analysis; the personal scenario above is the one I brought first, before the group converged.

For the broader argument on the science of evaluations this post draws on, see [*To Be or to Game*]({% post_url 2026-05-07-to-be-or-to-game %}). For the runtime-arm and ecosystem question, see [*Does Safe AI mean nothing bad can ever happen?*]({% post_url 2026-05-07-does-safe-ai-equal-safe-world %}).

[^reward-tampering]: Everitt, Krakovna, Orseau, Legg, Hutter (2021), *Reward Tampering Problems and Solutions in Reinforcement Learning: A Causal Influence Diagram Perspective*, Synthese. [arXiv:1908.04734](https://arxiv.org/abs/1908.04734).

[^pan]: Pan, Bhatia, Steinhardt (2022), *The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models*, ICLR. [arXiv:2201.03544](https://arxiv.org/abs/2201.03544).

[^skalse]: Skalse, Howe, Krasheninnikov, Krueger (2022), *Defining and Characterizing Reward Hacking*, NeurIPS. [arXiv:2209.13085](https://arxiv.org/abs/2209.13085).

[^gao]: Gao, Schulman, Hilton (2023), *Scaling Laws for Reward Model Overoptimization*, ICML. [arXiv:2210.10760](https://arxiv.org/abs/2210.10760).

[^alignment-faking]: Greenblatt, Denison, Wright, Roger, MacDiarmid, Marks et al. (2024), *Alignment Faking in Large Language Models*, Anthropic & Redwood Research. [arXiv:2412.14093](https://arxiv.org/abs/2412.14093).

[^scheming]: Meinke, Schoen, Scheurer, Balesni, Shah, Hobbhahn (2024), *Frontier Models are Capable of In-context Scheming*, Apollo Research. [arXiv:2412.04984](https://arxiv.org/abs/2412.04984).

[^sleeper]: Hubinger, Denison, Mu, Lambert, Tong et al. (2024), *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training*, Anthropic. [arXiv:2401.05566](https://arxiv.org/abs/2401.05566).

[^scaling-mono]: Templeton, Conerly, Marcus et al. (2024), *Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet*, Anthropic Transformer Circuits Thread. [transformer-circuits.pub/2024/scaling-monosemanticity](https://transformer-circuits.pub/2024/scaling-monosemanticity/).

[^arditi]: Arditi, Obeso, Syed, Paleka, Panickssery, Gurnee, Nanda (2024), *Refusal in Language Models is Mediated by a Single Direction*, NeurIPS. [arXiv:2406.11717](https://arxiv.org/abs/2406.11717).

[^sycophancy]: Sharma, Tong, Korbak, Duvenaud, Askell, Bowman, Cheng, Durmus et al. (2024), *Towards Understanding Sycophancy in Language Models*, ICLR. [arXiv:2310.13548](https://arxiv.org/abs/2310.13548).
