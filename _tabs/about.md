---
layout: page
title: About
permalink: /about/
---

<div class="medium-about">
  <img src="{{ site.data.medium_about.avatar_url }}" alt="{{ site.data.medium_about.name }} avatar">
  <h1>{{ site.data.medium_about.name }}</h1>
  <p>{{ site.data.medium_about.bio }}</p>
  <p>{{ site.data.medium_about.full_bio | markdownify }}</p>

</div>
