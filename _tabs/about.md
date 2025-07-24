---
layout: page
title:About
permalink:/about/
---

<div class="medium-about">
  {% if site.data.medium_about_full.avatar_url %}
    <img src="{{ site.data.medium_about_full.avatar_url }}" alt="{{ site.data.medium_about_full.name }} avatar" />
  {% endif %}
  <h1>{{ site.data.medium_about_full.name }}</h1>
  <div class="medium-bio">
    {{ site.data.medium_about_full.html | markdownify }}
  </div>
</div>
