---
layout: page
title: Papers
permalink: /research/papers/
description: "Every public paper by Davide Bragetti deposited on Zenodo, each with its own page, full-text PDF, DOI and citation."
---

<div class="research-page" markdown="1">

<p class="research-lede">Every public paper, one page each: full abstract, full-text PDF, DOI, version history and citation.</p>

Each paper is archived on [Zenodo](https://zenodo.org/search?q=metadata.creators.person_or_org.name%3A%22Bragetti%2C%20Davide%22),
which assigns its DOI. The PDF on each page here is a byte-identical copy of
the Zenodo file. The concept DOI always resolves to the latest version.

The doctoral thesis these papers feed into is a different kind of document and has its own page: [Doctoral thesis]({{ '/research/thesis/' | relative_url }}).

<p class="research-links"><a href="{{ '/research/' | relative_url }}">Research program</a><a href="https://scholar.google.com/citations?user=Fs4CwvwAAAAJ">Google Scholar profile</a><a href="https://orcid.org/0009-0008-7645-8241">ORCID</a></p>

{% assign papers = site.papers | sort: "first_published" | reverse %}
<section class="publication-list paper-index" aria-label="All papers">
  {% for paper in papers %}
  <article class="publication">
    <p class="pub-status">{{ paper.publication_type }}, {{ paper.year }}{% if paper.research_line %} / {{ paper.research_line }}{% endif %}</p>
    <h3><a href="{{ paper.url | relative_url }}">{{ paper.title }}</a></h3>
    <p class="pub-authors">{{ paper.authors_display | join: "; " }}</p>
    <div class="pub-actions" aria-label="Paper links">
      <a href="{{ paper.url | relative_url }}">Paper page</a>
      <a href="{{ paper.url | append: paper.pdf.file | relative_url }}">PDF</a>
      <a href="https://doi.org/{{ paper.concept_doi }}">DOI</a>
    </div>
  </article>
  {% endfor %}
</section>

</div>
