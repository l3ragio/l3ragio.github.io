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
