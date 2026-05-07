# l3ragio.github.io

Personal blog of **Davide Bragetti** - notes on AI safety, formal methods,
and adversarial security. Published at <https://l3ragio.github.io>.

Built with [Jekyll] and the [Chirpy] theme. Posts authored on
[Medium](https://medium.com/@dbragetti) are pulled in automatically by
[ZMediumToMarkdown]; posts written natively live alongside them.

[Jekyll]: https://jekyllrb.com/
[Chirpy]: https://github.com/cotes2020/jekyll-theme-chirpy
[ZMediumToMarkdown]: https://github.com/ZhgChgLi/ZMediumToMarkdown

## Repository layout

```
_config.yml                        Site configuration
_data/                             Authors, contact links, post overrides
_drafts/                           Unpublished drafts (.template.md inside)
_includes/head-custom.html         Open Graph / Twitter card meta
_layouts/visual_story.html         Layout for the Visual Stories collection
_posts/                            Native posts: YYYY-MM-DD-slug.md
_posts/zmediumtomarkdown/          Auto-synced Medium posts (do not edit)
_tabs/                             Sidebar tabs (about, archives, …)
_visual_stories/                   Visual Stories collection (.template.md inside)
assets/img/                        Theme images, avatar, per-post hero images
assets/visual-stories/<slug>/      Per-story panel images
assets/og/                         Auto-generated Open Graph previews
docs/CONVENTIONS.md                Article writing conventions (read this)
docs/VISUAL_STORIES.md             Visual Stories writing conventions
scripts/                           Build-time helpers (Ruby)
tools/                             Local dev scripts (run, test, deploy, scaffold)
.github/workflows/                 CI: Medium sync + Pages deploy
CLAUDE.md                          Instructions for AI assistants editing this repo
```

## Writing a new post

The full convention lives in [`docs/CONVENTIONS.md`](docs/CONVENTIONS.md).
Quick start:

```bash
bash tools/new_post.sh "my-new-post-slug"
# → creates _drafts/my-new-post-slug.md and assets/img/posts/my-new-post-slug/
```

Edit the draft, drop `hero.jpg` (1200×630) into the asset folder, then
move the file from `_drafts/` to `_posts/` with a date prefix when ready
to publish.

## Writing a new Visual Story

The full convention lives in [`docs/VISUAL_STORIES.md`](docs/VISUAL_STORIES.md).
Quick start:

```bash
bash tools/new_visual_story.sh "my-story-slug"
# → creates _visual_stories/YYYY-MM-DD-my-story-slug.md
#   and assets/visual-stories/my-story-slug/
```

Drop `panel-01.png`, `panel-02.png`, … into the asset folder and fill in
the YAML front matter.

## Local development

The fastest path is the included devcontainer (Jekyll preinstalled):

```bash
# inside the devcontainer or any environment with Ruby + bundler
bundle install
bash tools/run.sh           # http://127.0.0.1:4000
bash tools/test.sh          # build + html-proofer
```

## Continuous integration

Two workflows run on GitHub:

- **`ZMediumToMarkdown`** - monthly cron + on push. Pulls new Medium
  posts, re-applies per-post overrides from `_data/post_overrides.yml`,
  regenerates Open Graph previews for Visual Stories.
- **`Build and Deploy`** - on push to `main`. Builds with Jekyll, runs
  html-proofer, deploys to GitHub Pages.

## Note for Windows clones

Some Medium-imported PNG assets contain `*` in their filename (illegal
on NTFS). The repo can still be cloned on Windows using sparse-checkout
to skip those directories - see [`CLAUDE.md`](CLAUDE.md) for the exact
recipe.
