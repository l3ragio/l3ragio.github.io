---
layout: page
title: About
permalink: /about/
---

<div class="medium-about">
  {% if site.data.medium_about.avatar_url %}
  <img src="{{ site.data.medium_about.avatar_url }}" alt="{{ site.data.medium_about.name }} avatar">
  {% endif %}
  <h1>{{ site.data.medium_about.name }}</h1>
  <div class="medium-bio">
    aaaa {{ site.data.medium_about_html | markdownify }}
  </div>
</div>
