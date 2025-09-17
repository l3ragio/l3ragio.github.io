---
title: Visual Stories
icon: 📚
order: 5
permalink: /visual-stories/
---

<div class="visual-stories-grid">
  {% assign stories = site.visual_stories | sort: 'date' | reverse %}
  {% for s in stories %}
  <a class="vs-card" href="{{ s.url | relative_url }}">
    <img src="{{ s.hero | default: s.panels[0].img | relative_url }}" alt="{{ s.title }} cover">
    <div class="vs-meta">
      <h3>{{ s.title }}</h3>
      {% if s.subtitle %}<p>{{ s.subtitle }}</p>{% endif %}
      <small>{{ s.date | date: "%Y-%m-%d" }}</small>
    </div>
  </a>
  {% endfor %}
</div>

<style>
.visual-stories-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:18px}
.vs-card{display:block;border:1px solid var(--border-color);border-radius:12px;overflow:hidden;text-decoration:none;background:var(--card-bg)}
.vs-card img{width:100%;display:block;aspect-ratio:4/3;object-fit:cover}
.vs-meta{padding:12px}
.vs-meta h3{margin:.2rem 0 .1rem}
.vs-meta p{margin:0;color:var(--text-muted)}
</style>
