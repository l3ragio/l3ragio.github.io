# Blog Style Recovery

Internal note for the public research page implementation. This file is
under `docs/`, which is excluded from the Jekyll build.

## Site Architecture

- Generator: Jekyll.
- Theme: `jekyll-theme-chirpy` 7.2.x.
- Route model: top-level pages live in `_tabs/` and are emitted through
  the `tabs` collection with `permalink: /:title/`.
- Main content layouts: Chirpy defaults, with local overrides in
  `_layouts/home.html`, `_includes/home-post-card.html`, and the
  `_sass/dragetti/` layer.
- Navigation: sidebar tabs ordered by front matter `order`.
- Styling: `assets/css/jekyll-theme-chirpy.scss` imports the theme,
  then local Sass modules.
- Build: `bundle exec jekyll b`; CI uses production Jekyll build plus
  html-proofer with external links disabled.
- Local preview: `bash tools/run.sh` serves at `http://127.0.0.1:4000`.
- Deploy: GitHub Actions builds on `main`, then `tools/deploy.sh`
  publishes `_site` to `gh-pages`.

## Visual Language

- Dark-first site, with light-mode parity.
- Background is atmospheric but content remains readable through a
  translucent article surface.
- Accent is cyan in dark mode and deeper teal in light mode.
- Serif is used for long-form titles and prose; mono is used for labels,
  metadata, tags, and status-like information.
- Cards are quiet raised surfaces with hairline borders, mild hover lift,
  and no heavy decoration.
- Page body width is deliberately constrained. Existing prose sits in an
  `article > .content` panel with an 800px cap; special pages can opt
  into a wider page-specific wrapper.
- Existing page-specific styles use local classes such as `.about-page`
  and are scoped in Sass rather than adding a new frontend system.

## Writing Style

Representative public posts inspected:

- `To Be or to Game`
- `Does Safe AI mean nothing bad can ever happen?`
- `Misalignment by Reaction`
- `Uno, nessuno, centomila e tutti`

Recurring traits:

- The opening paragraph is usually a compressed thesis or TL;DR.
- The prose is structural and argumentative, not promotional.
- Claims are often framed as problem shapes, distinctions, and failure
  modes.
- AI-safety claims are connected to formal methods, governance, runtime
  monitoring, mechanistic interpretability, and multi-agent systems.
- Mathematical notation appears where it does conceptual work, but the
  prose usually gives the ordinary-language reading first.
- Tables are used for compact taxonomies.
- Citations and links are explicit but not styled as formal bibliography
  widgets.
- Status distinctions matter: conjecture, current work, published
  working paper, preprint, technical report, and essay should not be
  collapsed.

## Research Page Style Decisions

- Use native Chirpy tab page route `/research/`.
- Keep the page compact and academic: no hero image, no marketing
  metrics, no grant language.
- Make the center of the page a dependency map rather than a dashboard.
- Use local status pills only as metadata labels.
- Keep publications separate from essays.
- Use cautious phrasing for active work, especially around the exact
  project names "LTL Triangles" and "Drama to Empowerment".
