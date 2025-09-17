---
title: Visual Stories
icon: 📚
order: 5
permalink: /visual-stories/
---

<div class="visual-stories-grid">
  {% assign stories = site.visual_stories | sort: 'date' | reverse %}
  {% for s in stories %}
    <article class="vs-card">
      <a class="vs-link" href="{{ s.url | relative_url }}">
        <img class="vs-thumb"
             src="{{ (s.hero | default: s.panels[0].img) | relative_url }}"
             alt="{{ s.title }} cover"
             loading="lazy" decoding="async" />
        <div class="vs-meta">
          <h3>{{ s.title }}</h3>
          {% if s.subtitle %}<p>{{ s.subtitle }}</p>{% endif %}
          <small>{{ s.date | date: "%Y-%m-%d" }}</small>
        </div>
      </a>
    </article>
  {% endfor %}
</div>

<style>
.visual-stories-grid{
  display:grid;
  grid-template-columns:repeat(auto-fill,minmax(260px,1fr));
  gap:18px
}
.vs-card{
  border:1px solid var(--border-color);
  border-radius:12px;
  background:var(--card-bg);
  overflow:hidden;
}
.vs-link{ display:block; text-decoration:none; color:inherit; }
.vs-thumb{
  display:block;
  width:100%;
  aspect-ratio:4/3;
  object-fit:cover;
}
.vs-meta{ padding:12px; }
.vs-meta h3{ margin:.2rem 0 .1rem; font-size:1.05rem; }
.vs-meta p{ margin:0; color:var(--text-muted); }
</style>
