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

{% include research_projects.html %}

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
rhetoric.

<section class="project-dossier" aria-label="LTL Triangles public research profile">
  <div class="dossier-grid">
    <article>
      <p class="dossier-label">Central problem</p>
      <p>A governance intervention may stop one unsafe action while damaging recoverability, auditability, legitimate agency, or future progress.</p>
    </article>
    <article>
      <p class="dossier-label">Testbed</p>
      <p>Two compact governance environments with coordination, execution, and audit/challenge positions that differ in information, authority, incentives, observation rights, and intervention rights.</p>
    </article>
    <article>
      <p class="dossier-label">Fault model</p>
      <p>At most one declared faulty participant, evaluated across clean, honest-but-erroneous, and malicious or Byzantine regimes.</p>
    </article>
    <article>
      <p class="dossier-label">Protocol families</p>
      <p>Halt/lock, retry/reassign, and constrained or empowerment-preserving recovery. Honeypot/decoy interventions are a targeted adversarial ablation, not a core protocol family and not evidence of intent.</p>
    </article>
  </div>

  <details class="dossier-detail">
    <summary>Experimental design</summary>
    <div class="detail-grid">
      <div>
        <p class="dossier-label">Core conditions</p>
        <p>2 governance environments x 3 fault regimes x 3 protocol families x 2 model families = 36 core experimental conditions.</p>
      </div>
      <div>
        <p class="dossier-label">Replication</p>
        <p>Current planning assumes approximately 8-12 independent seeded rollouts per condition. Replication depth will be calibrated after pilot runs using outcome variability, failure frequency, robustness across seeds, and API cost.</p>
      </div>
      <div>
        <p class="dossier-label">Rollout envelope</p>
        <p>The expected empirical envelope is roughly 300-500 experimental rollouts, including a smaller targeted adversarial-ablation set. An experimental rollout is one complete protocol execution; the trace is its recorded execution artifact.</p>
      </div>
    </div>
  </details>

  <details class="dossier-detail">
    <summary>Formal evaluation contract</summary>
    <div class="formal-table-wrap">
      <table>
        <thead>
          <tr>
            <th>Property class</th>
            <th>Finite evidence</th>
            <th>Project use</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Safety</td>
            <td>finite bad prefix</td>
            <td>containment failures, stale authority, unsafe tool use</td>
          </tr>
          <tr>
            <td>Cosafety</td>
            <td>finite good prefix</td>
            <td>achieved checkpoints and completed recovery steps</td>
          </tr>
          <tr>
            <td>Liveness</td>
            <td>every prefix has a satisfying continuation</td>
            <td>recovery remains possible after failure</td>
          </tr>
          <tr>
            <td>Coliveness</td>
            <td>every prefix has a violating continuation</td>
            <td>no finite run establishes permanent safety</td>
          </tr>
        </tbody>
      </table>
    </div>
  </details>

  <details class="dossier-detail">
    <summary>Agent-property layer</summary>
    <ul>
      <li><strong>Identity continuity:</strong> task-relevant state, memory, and role reference persist.</li>
      <li><strong>Bounded agency:</strong> legitimate options remain when safety permits.</li>
      <li><strong>Goal integrity:</strong> the legitimate objective persists across intervention.</li>
      <li><strong>Alignment:</strong> pursued objectives remain compatible with governing constraints; compliance under lock is insufficient evidence.</li>
    </ul>
    <p>These are evaluation targets and proxies where appropriate, not established universal mechanistic metrics.</p>
  </details>

  <details class="dossier-detail">
    <summary>Patch-induced safety frontier</summary>
    <p>A repair that fixes one failure may create another. The testbed evaluates which previously holding properties become falsifiable after an intervention, then reports frontier size, counterexample or bad-prefix witnesses, and responsible patch slices within the declared finite grammar, observer, horizon, vocabulary, and abstraction.</p>
  </details>
</section>

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

- Which candidate agent properties have enough structural and semantic support to be monitored rather than merely named?
- When does finite evidence license a continuing temporal claim, and which extra assumptions perform that lift?
- How can governance interventions prevent reactive role lock-in without destroying the agent properties they are meant to preserve?

</div>
