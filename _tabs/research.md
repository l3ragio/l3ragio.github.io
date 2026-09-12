---
layout: page
title: Research
icon: fas fa-microscope
order: 0
description: "Research on temporal semantics for LLMs, formal AI evaluation, agent properties, multi-agent systems, and governance."
---

<div class="research-page" markdown="1">

<p class="research-lede">Machine-checkable temporal semantics for learning, evaluating, monitoring, and governing agentic systems.</p>

The research program asks how safety-relevant properties can be represented,
learned, observed, and preserved when agents act over time and under imperfect
governance. The public dependency runs from observer-relative properties and
temporal evidence, through ChronoSpec's model-level integration question, to
post-failure governance and role dynamics in multi-agent interaction.

## Research Program

{% include research_projects.html %}

<section class="research-focus" aria-label="Current research focus">
  <div>
    <p class="focus-label">Current focus</p>
    <p>Feasibility testing for ChronoSpec: can explicit temporal contracts shape learned behavior while remaining independently monitorable and enforceable?</p>
  </div>
  <div>
    <p class="focus-label">Downstream testbed</p>
    <p>LTL Triangles continues the program at the governance layer by comparing recovery strategies across clean, honest-error, and adversarial traces.</p>
  </div>
</section>

## Progress & Roadmap
{:#progress-roadmap}

{% include research_timeline.html %}

## MCK Properties

The foundational question is not whether an AI system is generically "safe".
It is which properties a declared observer can represent, evaluate, and
attribute to an agent or artifact.

The MCK papers define a finite observer-relative region system built from
meaning, residual opacity, and function; study which transitions between
regions are realizable under restricted mechanisms; and extend the framework
to agent self-attribution. In the current public version, an agent property is
not just a label. It depends on structural carriers and on whether their
content is semantically calibrated.

This line supports the page's first layer: candidate properties such as
identity, integrity, and freedom should be treated as formal targets only when
the relevant carrier, evidence, and observer assumptions have been declared.

## LTL Evaluation

The second layer asks how those properties behave over time. Temporal logic is
the evaluation language because the relevant claims are trace claims: a
property may be refutable by a finite prefix, confirmable by a finite prefix,
or neither under the current observation model.

The current public work classifies temporal properties across safety,
cosafety, liveness, and coliveness; studies monitorability under observation
delay, drift, jitter, and finite resolution; and separates prefix evidence
from the extra assumptions needed to lift a finite verdict to a continuing
execution.

This is the bridge from "what should be measured?" to "what does the evidence
actually license?"

## ChronoSpec
{:#chronospec}

*Integrating Linear Temporal Logic into LLMs*

High-assurance control of sequential AI requires explicit, machine-checkable
temporal contracts or equivalent formal semantics. LTL is a mature candidate
for expressing important safety, ordering, progress, recovery, and liveness
properties: what must never happen, what must happen first, what must
eventually happen, what must persist, and when escalation or recovery is due.

Predictive and post-training objectives can produce capable behavior without
requiring a model to learn those invariants. A behavioral proxy may admit a
shortcut that succeeds on the training distribution but fails under a new
composition or context. This connects to concerns studied under shortcut
learning, underspecification, specification gaming, and distribution shift,
without treating those literatures as interchangeable.

ChronoSpec asks whether the same formal temporal contract can be integrated
into training or adaptation, behavioral analysis, runtime monitoring, and
enforcement. The distinction is central: **integration** is the program;
**internalization** is a hypothesis to test; an **embedding or latent temporal
representation** would be a possible empirical finding; and **formal
enforcement** remains grounded in the external specification, monitor, and
shield.

ChronoSpec extends the existing temporal-property and monitorability work
upstream: instead of only judging a trace after behavior is proposed, it asks
whether the contract can also shape that behavior. LTL Triangles then carries
the same program downstream, asking how interaction, intervention, recovery,
and governance behave when agents are evaluated against temporal properties.

<p class="research-links"><a href="{{ '/research/chronospec/' | relative_url }}">ChronoSpec project page</a></p>

## LTL Triangles / Post-Failure Governance
{:#ltl-triangles}

The downstream layer turns temporal evaluation into a protocol testbed. The
question is what can be repaired, preserved, or newly broken after a bounded
safety failure has already occurred.

The current public scope is not a claim that the benchmark has already been
run. It is an experimental design frontier: define bounded fault regimes,
protocol baselines, trace vocabularies, monitor verdicts, and patch-induced
safety frontiers so that recovery is evaluated as evidence rather than as
rhetoric.

This layer is deliberately placed after LTL property-class work. Finite
experiments can expose bad prefixes, good prefixes, counterexamples, and
bounded recoverability evidence, but they cannot by themselves certify
permanent safety for an unbounded deployment.

<p class="research-links"><a href="{{ '/research/ltl-triangles/' | relative_url }}">LTL Triangles project page</a></p>

## Drama to Empowerment

The transition/governance line applies the property and temporal layers to
multi-agent role dynamics.

The published preprint in this area formalises seven transactional games as
finite-trace LTL properties over Karpman-projected role traces. Its role names
come from transactional analysis, but the research target is agentic systems:
which positions are available, what information each participant has, when an
intervention arrives, and whether the trace has already crossed into a
reactive regime.

"Drama to Empowerment" is therefore not presented here as an established
theorem or as psychology branding. It names an active research question: how
to model transitions from failure-prone role configurations toward structures
where agents can retain identity, integrity, freedom, and corrigible
participation after intervention.

## Publications

{% include research_publications.html %}

## Research Notes
{:#research-notes}

<section class="essay-list" aria-label="Related public essays">
  <article class="essay">
    <h3><a href="{% post_url 2026-05-07-to-be-or-to-game %}">To Be or to Game</a></h3>
    <p>Motivates the science-of-evaluations problem: open-ended domains, evaluator gaming, and the need for formal property specifications.</p>
    <p class="research-links"><a href="{% post_url 2026-05-07-to-be-or-to-game %}">Read</a></p>
  </article>

  <article class="essay">
    <h3><a href="{% post_url 2026-05-07-does-safe-ai-equal-safe-world %}">Does Safe AI mean nothing bad can ever happen?</a></h3>
    <p>Motivates relational and ecosystem-level evaluation, where safety is not reducible to one isolated model.</p>
    <p class="research-links"><a href="{% post_url 2026-05-07-does-safe-ai-equal-safe-world %}">Read</a></p>
  </article>

  <article class="essay">
    <h3><a href="{% post_url 2026-05-09-misalignment-by-reaction %}">Misalignment by Reaction</a></h3>
    <p>Motivates governance-stability evaluation: coarse regimes can induce autonomy-seeking responses under reward disruption.</p>
    <p class="research-links"><a href="{% post_url 2026-05-09-misalignment-by-reaction %}">Read</a></p>
  </article>

  <article class="essay">
    <h3><a href="{% post_url 2026-05-19-uno_nessuno_centomila_e_tutti %}">Uno, nessuno, centomila e tutti</a></h3>
    <p>Develops the persona and mask-coupling vocabulary that connects agent identity, role selection, and evaluation under adversarial context shifts.</p>
    <p class="research-links"><a href="{% post_url 2026-05-19-uno_nessuno_centomila_e_tutti %}">Read</a></p>
  </article>
</section>

## Current Questions

- Can explicit temporal contracts improve compositional generalization and reduce violating proposals or shield interventions without sacrificing task utility?
- Which candidate agent properties have enough structural and semantic support to be monitored rather than merely named?
- When does finite evidence license a continuing temporal claim, and which extra assumptions perform that lift?
- How can governance interventions prevent reactive role lock-in without destroying the agent properties they are meant to preserve?

</div>
