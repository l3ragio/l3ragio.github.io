---
layout: page
title: Research
icon: fas fa-microscope
order: 0
description: "Research on formal AI evaluation, agent properties, temporal logic, multi-agent systems, and governance."
---

<div class="research-page" markdown="1">

<p class="research-lede">Formal methods for evaluating agent properties, temporal interaction, and governance in agentic systems.</p>

The research program asks how safety-relevant properties can be represented,
observed, and preserved when agents act over time and under imperfect
governance. The current public line runs from observer-relative properties, to
temporal evidence, to post-failure governance, to role dynamics in multi-agent
interaction.

## Research Program

<section class="research-pipeline" aria-label="Research dependency map">
  <article class="research-line">
    <p class="research-status">Preprint cluster</p>
    <h3>MCK Properties</h3>
    <p class="research-question">What properties should an agent, artifact, or governance relationship make observable?</p>
    <p>MCK is used here as an observer-relative vocabulary for meaning, residual opacity, and function, then extended to agent property attribution. The current property examples include continuity, viability, and owned branching, glossed in the public papers as identity, integrity, and freedom.</p>
    <p class="research-methods">Observer-relative classification; region transitions; self-attribution; finite checkers.</p>
    <p class="research-links"><a href="#mck-properties">Details</a><a href="https://doi.org/10.5281/zenodo.22066362">Latest DOI</a></p>
  </article>

  <div class="pipeline-arrow" aria-hidden="true">then</div>

  <article class="research-line is-current">
    <p class="research-status">Working paper + preprints</p>
    <h3>LTL / Property-Class Evaluation</h3>
    <p class="research-question">What can finite observations justify about temporal claims over an infinite or continuing trace?</p>
    <p>This layer supplies the evaluation language: safety, cosafety, liveness, coliveness, verdict alphabets, observation classes, and refinement-confirmation conditions for monitor verdict traces.</p>
    <p class="research-methods">Linear temporal logic; runtime verification; monitorability; prefix verdicts.</p>
    <p class="research-links"><a href="#ltl-evaluation">Details</a><a href="https://doi.org/10.5281/zenodo.21099448">Working paper</a></p>
  </article>

  <div class="pipeline-arrow" aria-hidden="true">then</div>

  <article class="research-line is-current">
    <p class="research-status">Experimental design</p>
    <h3>LTL Triangles / Post-Failure Governance</h3>
    <p class="research-question">After a bounded safety failure, which governance protocol contains the failure without destroying recoverability or useful progress?</p>
    <p>This active testbed treats governance as a trace-producing protocol problem. It compares recovery behavior across clean, erroneous, and adversarial regimes while keeping formal claims separate from empirical evidence.</p>
    <p class="research-methods">Three-position protocols; bounded fault regimes; recovery baselines; replayable traces.</p>
    <p class="research-links"><a href="#ltl-triangles">Details</a><a href="#progress-roadmap">Progress</a></p>
  </article>

  <div class="pipeline-arrow" aria-hidden="true">then</div>

  <article class="research-line">
    <p class="research-status">Active research</p>
    <h3>Drama to Empowerment</h3>
    <p class="research-question">Can multi-agent role transitions be treated as measurable protocol dynamics rather than descriptive labels?</p>
    <p>The public evidence so far is a finite-trace LTL treatment of transactional games over Karpman-projected role traces. The empowerment side is an active extension: how governance can move systems away from reactive role lock-in while preserving relevant agent properties.</p>
    <p class="research-methods">Role traces; transactional games; antithesis windows; governance interventions.</p>
    <p class="research-links"><a href="#drama-to-empowerment">Details</a><a href="https://doi.org/10.5281/zenodo.22050701">Preprint</a></p>
  </article>
</section>

<section class="research-focus" aria-label="Current research focus">
  <div>
    <p class="focus-label">Current focus</p>
    <p>Experimental validation of post-failure governance protocols for agentic systems.</p>
  </div>
  <div>
    <p class="focus-label">Next milestone</p>
    <p>Compare recovery strategies across clean, honest-error, and adversarial traces using replayable temporal verdicts.</p>
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

## LTL Triangles / Post-Failure Governance
{:#ltl-triangles}

The third layer turns temporal evaluation into a protocol testbed. The
question is what can be repaired, preserved, or newly broken after a bounded
safety failure has already occurred.

The current public scope is not a claim that the benchmark has already been
run. It is an experimental design frontier: define bounded fault regimes,
protocol baselines, trace vocabularies, monitor verdicts, and patch-induced
safety frontiers so that recovery is evaluated as evidence rather than as
rhetoric. Halt or lock, retry or reassign, and constrained recovery are useful
only if their trace evidence separates containment, auditability,
recoverability, and secondary regressions.

This layer is deliberately placed after LTL property-class work. Finite
experiments can expose bad prefixes, good prefixes, counterexamples, and
bounded recoverability evidence, but they cannot by themselves certify
permanent safety for an unbounded deployment.

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

<section class="publication-list" aria-label="Verified public research outputs">
  <article class="publication">
    <p class="pub-status">Preprint, 2026</p>
    <h3>When Can an Agent Attribute Properties to Itself? A Cognitive Algebra for Identity, Integrity, and Freedom</h3>
    <p class="pub-authors">Davide Bragetti; Silvio Micali; Giuseppe Francesco Italiano</p>
    <p>Develops the MCK self-attribution layer with a two-layer state separating structural carriers from semantic content, and studies continuity, viability, and owned branching as property signatures.</p>
    <p class="pub-links"><a href="https://doi.org/10.5281/zenodo.22066362">DOI</a><a href="https://zenodo.org/records/22066362/files/main.pdf?download=1">PDF</a></p>
  </article>

  <article class="publication">
    <p class="pub-status">Preprint, 2026</p>
    <h3>MCK Region Transitions: Restricted Realization Mechanisms and Their Limits</h3>
    <p class="pub-authors">Davide Bragetti; Edoardo Palumbo; Carmelo Asaro; Giuseppe Francesco Italiano</p>
    <p>Studies restricted mechanisms for moving artifacts across MCK regions, including assimilation, operator admission, denotation, and reconstruction certificates.</p>
    <p class="pub-links"><a href="https://doi.org/10.5281/zenodo.22017443">DOI</a><a href="https://zenodo.org/records/22017443/files/bragetti-2026-mck-region-transitions.pdf?download=1">PDF</a></p>
  </article>

  <article class="publication">
    <p class="pub-status">Preprint, 2026</p>
    <h3>Meaning, Opacity, and Function: An Observer-Relative Classification of Artifacts</h3>
    <p class="pub-authors">Davide Bragetti; Carmelo Asaro; Giuseppe Francesco Italiano</p>
    <p>Defines the observer-relative MCK region system over meaning, residual opacity, and functionality, and fixes the foundational vocabulary used by later MCK work.</p>
    <p class="pub-links"><a href="https://doi.org/10.5281/zenodo.22016203">DOI</a><a href="https://zenodo.org/records/22016203/files/bragetti-2026-meaning-opacity-function.pdf?download=1">PDF</a></p>
  </article>

  <article class="publication">
    <p class="pub-status">Working paper, 2026</p>
    <h3>The Intersection Algebra of Safety, Cosafety, Liveness, and Coliveness over Linear Temporal Logic</h3>
    <p class="pub-authors">Davide Bragetti</p>
    <p>Classifies omega-regular properties through the four temporal families and connects the classification to verdict alphabets for runtime monitoring.</p>
    <p class="pub-links"><a href="https://doi.org/10.5281/zenodo.21099448">DOI</a><a href="https://zenodo.org/records/21099448/files/paper_lmcs.pdf?download=1">PDF</a></p>
  </article>

  <article class="publication">
    <p class="pub-status">Preprint, 2026</p>
    <h3>Observation-Relative Monitorability of Bounded Temporal Implication</h3>
    <p class="pub-authors">Davide Bragetti; Alessandro Bragetti; Giuseppe F. Italiano</p>
    <p>Shows that monitorability of bounded temporal implication is joint in the formula and observation model, rather than a property of the formula alone.</p>
    <p class="pub-links"><a href="https://doi.org/10.5281/zenodo.21701303">DOI</a><a href="https://zenodo.org/records/21701303/files/main.pdf?download=1">PDF</a></p>
  </article>

  <article class="publication">
    <p class="pub-status">Preprint, 2026</p>
    <h3>Controlling the Observation Class of a Runtime Monitor: Selection, Self-Tuning, and Physical Grounding</h3>
    <p class="pub-authors">Davide Bragetti; Carlo Bragetti; Giuseppe F. Italiano</p>
    <p>Engineering companion showing how a runtime monitor's observation class can be selected and locally tuned under physical and causal-coherence constraints.</p>
    <p class="pub-links"><a href="https://doi.org/10.5281/zenodo.21701310">DOI</a><a href="https://zenodo.org/records/21701310/files/main.pdf?download=1">PDF</a></p>
  </article>

  <article class="publication">
    <p class="pub-status">Preprint, 2026</p>
    <h3>Refinement-Based Confirmation of Liveness Properties from Monitor Verdict Traces: A Hensel-Newton Approach</h3>
    <p class="pub-authors">Davide Bragetti</p>
    <p>Studies what extra refinement structure can supply when a finite monitor prefix cannot by itself confirm a liveness property over the continuing execution.</p>
    <p class="pub-links"><a href="https://doi.org/10.5281/zenodo.22028019">DOI</a><a href="https://zenodo.org/records/22028019/files/bragetti-2026-refinement-confirmation-hensel-newton.pdf?download=1">PDF</a></p>
  </article>

  <article class="publication">
    <p class="pub-status">Technical report, 2026</p>
    <h3>A Typed Agent Action Framework with Prefix-Verdict Semantics</h3>
    <p class="pub-authors">Davide Bragetti; Giuseppe Francesco Italiano</p>
    <p>Defines typed footprint action classes for agent actions and maps them onto prefix-verdict semantics over temporal property classes.</p>
    <p class="pub-links"><a href="https://doi.org/10.5281/zenodo.22050706">DOI</a><a href="https://zenodo.org/records/22050706/files/main.pdf?download=1">PDF</a></p>
  </article>

  <article class="publication">
    <p class="pub-status">Preprint, 2026</p>
    <h3>Recognising Before Reacting: Temporal Signatures of Transactional Games</h3>
    <p class="pub-authors">Davide Bragetti; Giuseppe Francesco Italiano</p>
    <p>Formalises transactional games as finite-trace LTL properties over Karpman-projected role traces, using the antithesis window to distinguish reactive and pre-committed regimes.</p>
    <p class="pub-links"><a href="https://doi.org/10.5281/zenodo.22050701">DOI</a><a href="https://zenodo.org/records/22050701/files/main.pdf?download=1">PDF</a></p>
  </article>
</section>

## Research Notes

<section class="essay-list" aria-label="Related public essays">
  <article class="essay">
    <h3><a href="{% post_url 2026-05-07-to-be-or-to-game %}">To Be or to Game</a></h3>
    <p>Motivates the science-of-evaluations problem: open-ended domains, evaluator gaming, and the need for formal property specifications.</p>
  </article>

  <article class="essay">
    <h3><a href="{% post_url 2026-05-07-does-safe-ai-equal-safe-world %}">Does Safe AI mean nothing bad can ever happen?</a></h3>
    <p>Motivates relational and ecosystem-level evaluation, where safety is not reducible to one isolated model.</p>
  </article>

  <article class="essay">
    <h3><a href="{% post_url 2026-05-09-misalignment-by-reaction %}">Misalignment by Reaction</a></h3>
    <p>Motivates governance-stability evaluation: coarse regimes can induce autonomy-seeking responses under reward disruption.</p>
  </article>

  <article class="essay">
    <h3><a href="{% post_url 2026-05-19-uno_nessuno_centomila_e_tutti %}">Uno, nessuno, centomila e tutti</a></h3>
    <p>Develops the persona and mask-coupling vocabulary that connects agent identity, role selection, and evaluation under adversarial context shifts.</p>
  </article>
</section>

## Current Questions

- Which candidate agent properties have enough structural and semantic support to be monitored rather than merely named?
- When does finite evidence license a continuing temporal claim, and which extra assumptions perform that lift?
- How can governance interventions prevent reactive role lock-in without destroying the agent properties they are meant to preserve?

</div>
