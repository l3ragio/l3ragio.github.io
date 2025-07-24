---
layout: page
title: About
permalink: /about/
---

{% if site.data.medium_about %}
  <article class="medium-about">
    {{ site.data.medium_about.content }}
  </article>
{% else %}
  <p>Unable to fetch Medium About content.</p>
{% endif %}
