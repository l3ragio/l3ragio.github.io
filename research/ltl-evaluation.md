---
layout: page
title: LTL / Property-Class Evaluation
permalink: /research/ltl-evaluation/
description: "Temporal property classes, finite evidence, observation-relative monitorability, and refinement conditions."
---

<div class="research-page" markdown="1">

<p class="research-lede">What can finite observations justify about temporal claims over an infinite or continuing trace?</p>

This line supplies the evaluation language of the research program: temporal
property classes, prefix verdicts, observation-relative monitorability, and
the assumptions required to carry finite evidence into a continuing system.

<p class="research-links"><a href="{{ '/research/' | relative_url }}">Research program</a><a href="{{ '/research/mck-properties/' | relative_url }}">Previous: MCK Properties</a><a href="{{ '/research/chronospec/' | relative_url }}">Next: ChronoSpec</a></p>

## Evaluation problem

Safety-relevant claims about sequential agents are trace claims. Some can be
refuted by a finite bad prefix, some confirmed by a finite good prefix, and
some remain undecided under every finite observation. A useful evaluation
must therefore state both the temporal property and the observation regime.

<div class="formal-table-wrap">
  <table>
    <thead>
      <tr>
        <th>Property class</th>
        <th>Finite evidence</th>
        <th>Evaluation role</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Safety</td>
        <td>finite bad prefix</td>
        <td>detect a witnessed violation</td>
      </tr>
      <tr>
        <td>Cosafety</td>
        <td>finite good prefix</td>
        <td>detect a witnessed achievement</td>
      </tr>
      <tr>
        <td>Liveness</td>
        <td>no finite confirmation in general</td>
        <td>represent continuing progress obligations</td>
      </tr>
      <tr>
        <td>Coliveness</td>
        <td>no finite refutation in general</td>
        <td>represent persistent possibility of violation</td>
      </tr>
    </tbody>
  </table>
</div>

## Research profile

<section class="project-dossier" aria-label="LTL Evaluation research profile">
  <div class="dossier-grid">
    <article>
      <p class="dossier-label">Formal substrate</p>
      <p>Linear Temporal Logic, omega-regular properties, prefix quantifiers, verdict alphabets, and property-class intersections.</p>
    </article>
    <article>
      <p class="dossier-label">Observation model</p>
      <p>Bounded or delayed observation, drift, jitter, finite resolution, and the monitor's access to typed action traces.</p>
    </article>
    <article>
      <p class="dossier-label">Main distinction</p>
      <p>Formula-level truth is separated from the verdict a particular monitor can justify under its declared observation class.</p>
    </article>
    <article>
      <p class="dossier-label">Refinement question</p>
      <p>Finite verdicts require explicit refinement and environment assumptions before they support claims about continuing executions.</p>
    </article>
  </div>
</section>

## Dependency role

[MCK Properties]({{ '/research/mck-properties/' | relative_url }}) supplies
candidate observer-relative properties. This line determines how they can be
expressed and evaluated over traces. [ChronoSpec]({{ '/research/chronospec/' |
relative_url }}) uses that temporal substrate for a model-level feasibility
question; [LTL Triangles]({{ '/research/ltl-triangles/' | relative_url }}) uses
it independently for governance and recovery over observable traces.

## Current status and claim boundary

The line consists of a public working paper and preprints and remains active
formal-methods research. Finite experiments may provide witnesses,
counterexamples, or bounded verdicts; they do not by themselves certify
permanent safety for an unbounded deployment.

## Selected publications

{% include research_publications.html project_id="ltl-evaluation" %}

</div>
