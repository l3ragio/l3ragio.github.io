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
        <div class="vs-thumb"
             style="--vs-thumb:url('{{ (s.hero | default: s.panels[0].img) | relative_url }}')"></div>
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
.vs-link{ display:block; color:inherit; text-decoration:none; }
.vs-thumb{
  width:100%;
  aspect-ratio:4/3;
  background-image:var(--vs-thumb);
  background-size:cover;
  background-position:center;
  background-repeat:no-repeat;
}
.vs-meta{ padding:12px; }
.vs-meta h3{ margin:.2rem 0 .1rem; font-size:1.05rem; }
.vs-meta p{ margin:0; color:var(--text-muted); }
</style>
