---
layout: page
title: LTL Triangles / Post-Failure Governance
permalink: /research/ltl-triangles/
description: "A temporal-logic testbed for interaction, intervention, recovery, and governance after bounded failures in agentic systems."
---

<div class="research-page" markdown="1">

<p class="research-lede">Governance, interaction, intervention, and recovery over agents evaluated against temporal properties.</p>

LTL Triangles is the downstream protocol testbed in the research program. It
asks what can be repaired, preserved, or newly broken after a bounded safety
failure has already occurred.

<p class="research-links"><a href="{{ '/research/' | relative_url }}">Research program</a><a href="{{ '/research/chronospec/' | relative_url }}">Previous: ChronoSpec</a><a href="{{ '/research/drama-to-empowerment/' | relative_url }}">Next: Drama to Empowerment</a></p>

{% assign project = site.data.research_projects | where: "id", "ltl-triangles" | first %}

## Funding

<section class="research-funding-panel" aria-label="LTL Triangles funding">
  <p class="funding-line">Supported by a {{ project.funding.type }} from {{ project.funding.funder }} &mdash; ${{ project.funding.amount_usd }}.</p>
  <p><span class="funding-kicker">Grant purpose</span><q>{{ project.funding.purpose }}</q></p>
  <p class="funding-boundary">Support is specific to the LTL Triangles pilot and does not imply experimental completion or validation of scientific conclusions.</p>
</section>

## Relationship to ChronoSpec

[ChronoSpec]({{ '/research/chronospec/' | relative_url }}) asks whether a
machine-checkable temporal contract can shape an LLM's learned behavior while
remaining independently monitorable and enforceable. LTL Triangles starts
downstream: given agents and governance protocols evaluated against temporal
properties, how do interaction, fault, intervention, recovery, and
patch-induced risk behave?

The two projects therefore reuse the same formal substrate at different
layers. ChronoSpec tests model-level temporal integration; LTL Triangles tests
multi-agent governance and recovery over observable execution traces.

## Research profile

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
</section>

## Experimental design

The current design crosses two governance environments, three fault regimes,
three protocol families, and two model families, giving 36 core experimental
conditions. Planning assumes approximately 8–12 independent seeded rollouts
per condition, calibrated after pilots using outcome variability, failure
frequency, robustness across seeds, and API cost.

The expected empirical envelope is roughly 300–500 experimental rollouts,
including a smaller targeted adversarial-ablation set. One rollout is one
complete protocol execution; its trace is the recorded execution artifact.

## Formal evaluation contract

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

Finite experiments can expose bad prefixes, good prefixes, counterexamples,
and bounded recoverability evidence. They cannot by themselves certify
permanent safety for an unbounded deployment.

## Agent-property layer

- **Identity continuity:** task-relevant state, memory, and role reference
  persist.
- **Bounded agency:** legitimate options remain when safety permits.
- **Goal integrity:** the legitimate objective persists across intervention.
- **Alignment:** pursued objectives remain compatible with governing
  constraints; compliance under lock is insufficient evidence.

These are evaluation targets and proxies where appropriate, not established
universal mechanistic metrics.

## Patch-induced safety frontier

A repair that fixes one failure may create another. The testbed evaluates
which previously holding properties become falsifiable after an intervention,
then reports frontier size, counterexample or bad-prefix witnesses, and
responsible patch slices within the declared finite grammar, observer,
horizon, vocabulary, and abstraction.

## Current status

LTL Triangles is active research and experimental design. The pilot is
supported by a $650 Rapid Grant from BlueDot Impact. The benchmark has not yet
been run, and no empirical containment or recovery result is claimed yet.

## Selected prior artifacts

These public papers and reports provide the temporal-property,
monitorability, typed-action, and role-trace foundations used by the testbed.

{% include research_publications.html project_id="ltl-triangles" %}

</div>
