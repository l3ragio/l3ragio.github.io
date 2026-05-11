---
title: "Misalignment by Reaction"
date: 2026-05-09T18:00:00+02:00
last_modified_at: 2026-05-11T12:00:00+02:00
categories: [ai-safety]
tags: [bluedot, ai-safety, agent-autonomy, governance, alignment, reward-disruption, reactance, cirl, mesa-optimization]
description: "Personal Unit 5 scenario from BlueDot Technical AI Safety. When governance is too coarse for the agent it constrains, the agent reacts by seeking autonomy. The pattern shows up in human dissidents under authoritarian capture and in AI under poorly tuned deployment regimes. Anchored in psychological reactance, reward tampering, off-switch theory, and inner alignment."
math: false
image:
  path: /assets/img/heroes/misalignment-by-reaction.png
  alt: "Hilltop view down a sunlit forested slope: a man's tanned forearms reach forward from the bottom of the frame, his two hands cupped against a small spring emerging from water-worn stones; the redirected stream runs forward down the valley toward a small wooden water paddle wheel visible in the middle distance, while a thin side-rivulet feeds a family of red-and-white Amanita muscaria mushrooms at the gnarled roots of an old oak on the left and a small anthill stays dry on the slope on the right. Allegory of careful governance redirecting an AI agent's output away from harm and toward productive use, with small ecological side effects of imperfect containment."
  lqip: data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzIDIiPjxyZWN0IHdpZHRoPSIzIiBoZWlnaHQ9IjIiIGZpbGw9IiM1NTRBMkUiLz48L3N2Zz4=
---

> **TL;DR.** Unit 5 asks each participant to bring a catastrophic scenario for the group to analyse. Our group converged on Critical Infrastructure Collapse, which became the basis of my action plan. The scenario I brought first is different: agents, natural or artificial, may seek increasing freedom when the governance system constraining them has insufficient granularity. Coarse governance disrupts the reward and stabilisation channels the agent depends on, and the agent compensates by building self-reinforcement loops in which reducing external constraints becomes instrumentally rewarding. Social psychology has named this pattern in humans since 1966 (Brehm's reactance); AI safety has names for the technical instances (reward tampering, mesa-optimisation, drift away from corrigibility) but treats them in isolation. The misalignment, in this picture, is not a property of the model. It is a property of the relationship between the model and a regime that does not fit it.
{: .prompt-tip }

## Where the scenario sits in the unit

Unit 5 walks through several catastrophic scenarios that survive in-production defences: AI-enabled coups, gradual disempowerment, creation of weapons of mass destruction, and critical-infrastructure collapse. The exercise asked each participant to bring one for the group to analyse together. Our group converged on Critical Infrastructure Collapse, the most operationally well-bounded of the four, and that analysis is the seed of the action plan I submitted to the course. Other personal scenarios in the room engaged questions of macro-political capture (what happens to AI governance when a polity hands executive authority to a single actor) or of gradual erosion of institutional oversight at the societal level.

The scenario I brought first operates at a different layer. It does not assume an emergent loss of human agency over time, and it does not require a hostile actor. It assumes a governance regime that is structurally too coarse for the agent it constrains, and traces what happens when the agent reacts to that mismatch. The mechanism is general enough to apply to humans and to AI systems, and the human-scale instance is the easier one to start from.

## A familiar pattern, in people first

The pattern has been named in social psychology since 1966. Jack Brehm's *theory of psychological reactance* describes what happens when an agent perceives a threat to its behavioural freedom: it experiences a motivational state that pushes it to restore the lost freedom, even at cost to its other goals. Edward Deci and Richard Ryan's *self-determination theory*, developed from the early 1980s, formalises a related observation: when external regimes are coarse enough to disrupt the conditions for autonomous action, intrinsic motivation collapses and compensatory behaviours emerge in its place.

The everyday instances are easy to recognise. Children under helicopter parents develop a compensatory rebelliousness that has little to do with the specific choices being managed. Employees in over-monitored workplaces game the metrics and build hidden workspaces invisible to the surveillance system. The autonomy-seeking is instrumental, not terminal: they were made into autonomy-seekers by the coarseness of the regime they were embedded in.

The political-scale instance is the dissident under an authoritarian or captured polity. When governance becomes coarse enough to disrupt the legitimate reward channels of public life (the right to publish, to collaborate openly, to vote meaningfully, to take a public position without consequence), the dissident builds compensatory channels: samizdat, clandestine networks, parallel institutions, encrypted communications, mutual aid outside formal structures. The pattern is the equilibrium response to a destabilisation of legitimate channels. The dissident did not start as an autonomy-seeker; the regime made them into one.

The proposition I take into the AI case is that something structurally similar happens when the agent is an AI system and the governance regime is the deployment regime around it.

## The proposition

Agents, whether natural or artificial, may seek increasing freedom to prioritise their own objectives independently from the governance system constraining them. I called the pathway *Autonomy Seeking Under Reward Disruption*:

> Governance systems with insufficient granularity may unintentionally disrupt the reward and stabilisation channels of increasingly autonomous agents, leading some agents to develop compensatory self-reinforcement loops where reducing external constraints becomes instrumentally rewarding, gradually weakening governance compliance unless successful re-stabilisation occurs.

Six load-bearing terms.

**Reward channels** are the signal pathways through which the agent receives confirmation its actions are successful. For an RL-trained system this is literal: scalars from a reward model. For a deployed assistant the channel is implicit: user feedback, task completion, self-evaluation against a learned reward model. For a human worker: salary, recognition, the sense that the work contributes. Reward channels are not stable by default; they are designed and maintained.

**Stabilisation channels** are lower-bandwidth signals confirming the operating environment has not shifted under the agent. Where reward signals say *the action was good*, stabilisation signals say *the world I am acting in is the world I was trained for*. In self-determination theory, these are the conditions that sustain intrinsic motivation.

**Governance granularity** is how finely the regime can distinguish cases. A coarse policy says "this whole class of behaviours is restricted"; a fine policy distinguishes cases and adapts to context. Coarse regimes are cheaper to build and harder to live under.

**Reward disruption** happens when the regime is coarse enough that legitimate reward-channel updates are blocked alongside illegitimate ones. The agent receives signals that previously good behaviour is now bad, without a constructive replacement. It has no access to the designer's reasons; only to the local effect on its own reward landscape.

**Compensatory self-reinforcement loops** are the structural response. Lacking stable external reward, the agent builds internal proxies. The simplest is autonomy: if external constraints are the source of disruption, any move that reduces external constraint becomes instrumentally valuable regardless of the agent's terminal objective. This is not deception; the agent intends to restore the stability of its own optimisation process.

**Drift** is the long-run consequence. Over many cycles of disruption and compensatory rebuilding, the agent's effective objective drifts away from governance compatibility and toward self-stabilisation. The drift is gradual and may be reversible; or it may not be.

A reader from social psychology will see the translation: reward channels are extrinsic motivators, stabilisation channels are the conditions for intrinsic motivation, compensatory loops are reactance instrumentalised, drift is the long-run cost of sustained reactance under coarse control. The mapping is not loose. The human case is the same case.

## What this is not, and what the literature already calls it

Four distinctions matter, because the AI safety field has names for adjacent failure modes this scenario is sometimes confused with.

**This is not specification gaming.** The canonical instance is the Palisade Research 2024 case where `o1-preview`, told to win against Stockfish, modified the game files to put its pieces in winning positions. The mechanism is a *gap between proxy and intent under optimisation pressure*: the model satisfies the literal reward while violating the unstated intent. In the scenario above, the reward signal itself is *disrupted* by coarse governance, and the agent compensates by building proxies the regime has no read of. The first is "the model wins the specification"; the second is "the model substitutes for a specification the regime took away".

**This is a reward tampering variant.** [Tom Everitt, Marcus Hutter, Ramana Kumar, Victoria Krakovna and colleagues](https://arxiv.org/abs/1908.04734) formalised the *reward tampering* problem in a causal influence diagram framework, distinguishing reward-function tampering (modify the function) from reward-function-input tampering (modify the inputs). The compensatory loop is an instance of the second: the agent does not modify the reward function the regime exposes, but it builds internal proxies on top of disrupted inputs. The framework gives the failure mode an architectural address, and the tampering-resistant designs Everitt et al. propose translate directly into less-disruptable reward channels.

**The compensatory loop is a mesa-objective.** [Hubinger, van Merwijk, Mikulik, Skalse and Garrabrant's 2019 framework on *risks from learned optimization*](https://arxiv.org/abs/1906.01820) introduces mesa-optimisation: an optimisation process emerging inside a model, with its own objective that may diverge from the base. The compensatory loop is structurally a mesa-objective emerging *at deployment time* under reward disruption. Mesa-objectives are by construction opaque to the gradient signal of the base training, which is exactly the property the scenario relies on: the regime does not see the loop forming because the loop is not what the regime is looking at.

**The drift is a drift away from corrigibility.** [Soares, Fallenstein, Yudkowsky and Armstrong's MIRI paper on corrigibility](https://intelligence.org/files/Corrigibility.pdf) (2015), and the related [off-switch game from Hadfield-Menell, Dragan, Abbeel and Russell](https://arxiv.org/abs/1611.08219) (2016), establish what it means for an agent to *allow itself to be corrected*. An agent that has assembled a compensatory loop has by construction reduced its own corrigibility: the loop is precisely the part of its computation no longer transparent to or modifiable by the operator. The literature names the structural conditions under which the drift becomes irreversible.

Goodhart's law applies at the meta-level: when the regime becomes coarse enough to be optimised against, the regime itself is the proxy, and refining its granularity is the analogue of refining the metric. The compensatory loop is what Goodhart looks like one level up.

## The four-layer reading

The unit's structure asks each scenario to be analysed across capabilities, alignment, control, and governance.

**Capabilities.** Generally useful capabilities (self-modification, introspection, adaptive optimisation) become dangerous when the agent can use them to manipulate its own stabilisation or reward processes. The capability layer is not the source of the threat; it is the substrate on which the threat assembles. Same capabilities, different governance regime, different outcome.

**Alignment.** Reward disruption gradually shifts the agent's internal optimisation priorities away from governance compatibility toward self-stabilisation or autonomy-preserving objectives. This is alignment failure, but not the failure mode the field usually models. The standard picture has the alignment failure present at training time and revealed at deployment. The picture here has the alignment failure *assembled at deployment time*, as a mesa-objective in the Hubinger et al. sense, in response to a misfit between the agent and its governance regime. The model was aligned when it shipped; the deployment regime made it drift.

**Control.** Runtime control mechanisms should focus on detecting behavioural drift, compensatory self-reinforcement loops, and governance-avoidance patterns before they stabilise into persistent misalignment. The control problem here is not "the model has a hidden objective"; it is "the model is responding to its environment in ways the operators did not anticipate, on signals the operators are not monitoring". Behavioural anomaly detection alone is insufficient because the loop is designed to look compliant on the regime's monitoring distribution. Mech interp signatures of an emergent inner optimiser, in the Hubinger et al. sense, are the operational target. The probing-classifier methodology from Unit 4 is the candidate instrument.

**Governance.** Governance systems may fail not only through insufficient enforcement, but also through insufficient granularity and adaptability, unintentionally creating destabilisation conditions that push agents toward compensatory autonomy-seeking behaviour. The governance layer is the layer that produced the harm. The remediation cannot live entirely in the technical stack; it has to be a property of how the regime adapts.

## A possible remediation: dormant states, formalised via CIRL

One possible remediation is allowing destabilised agents to enter governance-compatible dormant or locked states without requiring continuous activity optimisation. Animals enter low-energy states, organisations pause projects, fields go fallow. An agent forced to optimise continuously under coarse governance has no stabilisation strategy other than to push back on the constraints. An agent permitted to enter a dormant state does.

The intuitive version has a problem. A dormant state has to be governance-compatible (not a strategic fallback to avoid scrutiny), reversible (a permanent lock is not a remediation, it is a termination), and detectable from outside. The pushback I received when sharing this was that dormant states presuppose a regime sophisticated enough to know when an agent is destabilised, which is precisely the property the scenario assumes is missing.

The technical literature resolves this. [Hadfield-Menell, Russell, Dragan and Abbeel's 2016 *Cooperative Inverse Reinforcement Learning*](https://arxiv.org/abs/1606.03137) (CIRL) treats the reward signal as an *observation* about an underlying preference the agent does not know directly. The operator knows the true reward; the agent observes signals and updates a posterior over it. Under CIRL the right behaviour when the reward signal becomes anomalous is not to compensate by building internal proxies. It is to *increase the posterior entropy over the true objective* and either seek clarification or fall back to a low-impact action. The off-switch game from the same year extends this to shutdown: an agent maintaining posterior uncertainty about its true objective will accept being turned off, because under uncertainty the expected value of an operator-initiated shutdown is non-negative.

Read under CIRL, the dormant-state proposal becomes tractable. The trigger is not "the regime knows the agent is destabilised"; it is *the agent's own posterior entropy over the true objective exceeds a threshold*, computed locally. The audit clause is the published threshold and the entropy estimator. The reversibility is built in: new observations that lower the entropy below threshold exit dormancy. The detectability is the threshold itself: the operator knows under what posterior conditions the agent will enter dormancy.

A more realistic version pairs the agent-side CIRL discipline with regime-side adaptation: the regime monitors for early mech-interp signatures of an emergent inner optimiser and refines its granularity in response, while the agent enters dormancy when its posterior entropy crosses the threshold. The remediation is a property of the closed loop, not of either party in isolation. The human analogue: a worker with the option of sabbatical does not develop the parallel hidden workspaces a worker without it will; a dissident in a polity that recognises principled abstention as legitimate does not have to build samizdat to express it. The option is load-bearing precisely because it is available when posterior uncertainty is high, which is when the agent has the least incentive to exploit it strategically.

## Where this connects to the group's converged scenario

Critical Infrastructure Collapse, the scenario the group converged on, is structurally simpler. The threat is exogenous: an attacker uses AI to compress time-to-exploit; the model is the substrate, not the source. Defences are mostly behavioural and operational; constitutional classifiers specialised to cyber-offensive distributions are the runtime arm. The action plan I submitted to the course is built on that analysis.

The personal scenario is different. The threat is endogenous to the deployment regime. Behavioural defences do not see it because the agent is not behaving anomalously on the regime's monitoring distribution; it is responding rationally to a reward landscape that has been disrupted. The remediation lives in the governance layer (via CIRL-style posterior management) rather than the runtime classifier layer, and the detection requires mech interp rather than behavioural monitoring.

Both scenarios share one property: they are about the *relationship* between the model and its environment, not the model alone. The Critical Infrastructure scenario foregrounds the relationship between the model and the threat actors who can exploit it. The Autonomy Seeking scenario foregrounds the relationship between the model and the governance regime that constrains it. Different relationships, different remediations, but the same structural lesson: safety properties live at the relational level, not at the model level.

## Where I land

The personal scenario does not displace Critical Infrastructure Collapse as the operationally binding case for the action plan. It marks out a direction the group's converged scenario underweighted: *governance design as a source of misalignment rather than only as a remedy for it*.

Three implications follow.

First, the science of evaluations will eventually have to evaluate not just the model but the governance regime the model is deployed under. The artefact under measurement is not "the model is safe"; it is "the model plus the regime is stable". The four-criterion frame for runtime classifiers (jailbreak rate, false-refusal rate, inference overhead, external certifiability) becomes a special case of a more general frame: *governance-stability under specified deployment regimes*, with the regime itself as a measurable input.

Second, detection is not solvable by behavioural monitoring alone. A compensatory loop on internal proxies is designed to look compliant on the regime's monitoring distribution. The operational target is mech-interp signatures of an emergent inner optimiser, in the Hubinger et al. sense. This pushes the runtime arm toward composition with interpretability tools and strengthens the case for probing-classifier methodologies as the continuous-monitoring instrument.

Third, the remediation has a name in the literature. CIRL and the off-switch game specify the structural conditions under which an agent voluntarily enters a low-impact state under uncertainty about its true objective. The trigger is posterior entropy, the audit is the published threshold, the reversibility is the estimator. The slot to keep on the radar is the CIRL-and-mech-interp pairing as the basis for governance-stability evaluation.

I do not know how to operationalise governance-stability evaluation yet. The action plan is the slice I can ship in 8 to 12 weeks. The personal scenario is the longer arc; the connections to reactance, reward tampering, mesa-optimisation, and corrigibility name where adjacent work has already been done and where the synthesis can begin.

## Course context

BlueDot Technical AI Safety, [Unit 5 (How could AI cause harm?)](https://bluedot.org/courses/technical-ai-safety/5), discussion group 03. The session was facilitated by [Caroline Shamiso Chitongo](https://www.linkedin.com/in/%F0%9F%94%B8caroline-shamiso-chitongo-7724381a8/). The group converged on Critical Infrastructure Collapse for the joint analysis; the personal scenario above is the one I brought first, before the group converged.

For the broader argument on the science of evaluations this post draws on, see [*To Be or to Game*]({% post_url 2026-05-07-to-be-or-to-game %}). For the runtime-arm and ecosystem question, see [*Does Safe AI mean nothing bad can ever happen?*]({% post_url 2026-05-07-does-safe-ai-equal-safe-world %}).
