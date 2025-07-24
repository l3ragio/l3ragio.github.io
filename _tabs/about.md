---
layout: page
title: About
permalink: /about/
---

<div class="medium-about">
  {% if site.data.medium_about_html %}
    {{ site.data.medium_about_html }}
  {% else %}
    <p>Unable to fetch Medium About content.</p>
  {% endif %}
</div>
