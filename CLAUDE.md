# CLAUDE.md - l3ragio.github.io

Operating notes for AI assistants editing this Jekyll blog. Read this
file end-to-end before touching anything; it captures the conventions
and the Windows-specific gotchas that are not obvious from the code.

## What this repo is

The personal blog of **Davide Bragetti** at <https://l3ragio.github.io>,
built with Jekyll + the [Chirpy] theme and deployed to GitHub Pages.

[Chirpy]: https://github.com/cotes2020/jekyll-theme-chirpy

Two content streams coexist:

1. **Medium-synced posts** under `_posts/zmediumtomarkdown/`, pulled
   monthly from <https://medium.com/@dbragetti> by the
   [`ZMediumToMarkdown`](.github/workflows/ZMediumToMarkdown.yml)
   action. **Never hand-edit these files.** Use `_data/post_overrides.yml`
   to override fields the sync wipes (categories, pin, custom tags).
2. **Native posts and Visual Stories** under `_posts/` and
   `_visual_stories/`, written here directly.

The full convention for each is in `docs/CONVENTIONS.md` and
`docs/VISUAL_STORIES.md` - those are the documents to treat as
authoritative.

## Where things live (one-liner index)

| Path                                 | Purpose                                            |
|--------------------------------------|----------------------------------------------------|
| `_config.yml`                        | Site-wide configuration                             |
| `_data/authors.yml`                  | Author metadata for jekyll-seo-tag                  |
| `_data/contact.yml`                  | Sidebar contact icons                               |
| `_data/post_overrides.yml`           | **Source of truth** for Medium-post categories etc. |
| `_drafts/.template.md`               | Canonical scaffold for new native posts             |
| `_drafts/<slug>.md`                  | Drafts (not built)                                  |
| `_posts/YYYY-MM-DD-<slug>.md`        | Native published posts                              |
| `_posts/zmediumtomarkdown/`          | Auto-synced Medium posts (do not hand-edit)         |
| `_visual_stories/.template.md`       | Canonical scaffold for new Visual Stories           |
| `_visual_stories/YYYY-MM-DD-<slug>.md` | Published Visual Stories                          |
| `_layouts/visual_story.html`         | Layout for the Visual Stories collection            |
| `_includes/head-custom.html`         | OG / Twitter meta for Visual Stories                |
| `_tabs/about.md`                     | /about page                                         |
| `assets/img/posts/<slug>/`           | Per-post images (hero + inline)                     |
| `assets/visual-stories/<slug>/`      | Per-story panel images                              |
| `assets/og/<slug>.jpg`               | Auto-generated OG previews (do not commit by hand)  |
| `scripts/apply_post_overrides.rb`    | Runs in CI after Medium sync                        |
| `scripts/generate_visual_story_og.rb`| Runs in CI; needs ImageMagick                       |
| `tools/new_post.sh`                  | Scaffold a new draft                                |
| `tools/new_visual_story.sh`          | Scaffold a new Visual Story                         |
| `tools/run.sh` `tools/test.sh` `tools/deploy.sh` | Local dev / CI helpers                  |
| `.github/workflows/`                 | `ZMediumToMarkdown.yml`, `pages-deploy.yml`         |

## Common tasks

### Write a new post

```bash
bash tools/new_post.sh "post-slug"
# edit _drafts/post-slug.md
# add hero.jpg to assets/img/posts/post-slug/
# when ready:
mv _drafts/post-slug.md _posts/$(date +%Y-%m-%d)-post-slug.md
```

Required front matter and the closed category set are spelled out in
`docs/CONVENTIONS.md`.

### Write a new Visual Story

```bash
bash tools/new_visual_story.sh "story-slug"
# drop panel-01.png, panel-02.png, ... into assets/visual-stories/story-slug/
# fill in the YAML in the created _visual_stories/<date>-story-slug.md
```

Schema in `docs/VISUAL_STORIES.md`.

### Change the category of a Medium-synced post

Edit `_data/post_overrides.yml` (key = the Medium post slug, the ID
after the date in the filename) - **do not edit the post file**, the
next sync would overwrite you. The post-sync step
`scripts/apply_post_overrides.rb` re-applies overrides automatically
in CI; for a local check run it manually:

```bash
ruby scripts/apply_post_overrides.rb
```

### Build / preview locally

```bash
bundle install        # one-time
bash tools/run.sh     # http://127.0.0.1:4000
bash tools/test.sh    # build + html-proofer (what CI runs)
```

## Hard rules

- **Do not hand-edit `_posts/zmediumtomarkdown/*.md`.** Use the
  override file. The next monthly sync resets your changes otherwise.
- **Do not commit `assets/og/*.jpg`.** They are CI-generated.
- **Do not introduce a category outside the closed set** in
  `docs/CONVENTIONS.md` without updating that document.
- **Always set `alt` on images.** html-proofer in CI fails the build
  on missing alt text (configured to ignore *empty* alt only).
- **Slugs are kebab-case.** No spaces, no accents, no uppercase. The
  scaffold scripts validate this.
- **Date format**: posts use ISO 8601 with timezone
  (`2026-05-12T10:00:00+01:00`); Visual Stories use plain `YYYY-MM-DD`.

## Soft rules

- One `##` per major section; the theme builds the TOC from `##`/`###`.
- Hero images: 1200×630 JPEG, ≤ 200 KB.
- Tags: 1-5, lowercase, kebab-case. Prefer existing tags.
- A post's TL;DR (first paragraph) becomes the home-page excerpt - keep
  it tight.

## Windows-specific clone

This repo contains 60+ Medium-imported PNG assets whose filenames start
with `1*` (a Medium CDN convention). The `*` is **illegal in NTFS**, so
a plain `git clone` cannot create the working tree on Windows.

Use sparse-checkout cone mode to skip those directories. The local copy
under `Programmazione_Scientifica/subprojects/l3ragio.github.io/` was
set up as follows:

```bash
git clone --branch main --no-checkout --filter=blob:none \
  https://github.com/l3ragio/l3ragio.github.io.git
cd l3ragio.github.io
git sparse-checkout init --cone --sparse-index
git sparse-checkout set \
  .devcontainer .github .vscode \
  _data _includes _layouts _plugins _posts _tabs _visual_stories \
  scripts tools \
  assets/img assets/lib assets/og assets/visual-stories
git checkout main
```

The excluded `assets/<medium-hash>/` directories remain in the git
object database and serve correctly from GitHub Pages (Linux); they
just cannot be materialized on Windows.

To extend the local checkout later:

```bash
git sparse-checkout add <path>
```

## CI

| Workflow                     | Trigger                          | What it does                                              |
|------------------------------|----------------------------------|-----------------------------------------------------------|
| `ZMediumToMarkdown.yml`      | push, monthly cron, manual       | Pull Medium → re-apply overrides → regen OG → push        |
| `pages-deploy.yml`           | push to `main`, after the above  | Build with Jekyll → html-proofer → deploy to GitHub Pages |

If `pages-deploy.yml` fails on `htmlproofer`, the most common causes
are: missing `alt` on a new image, a broken internal link, a draft
left with `image.path` pointing to a non-existent file.

## Authoritative state

This file is a navigational summary. When in doubt, the authoritative
source is:

- `docs/CONVENTIONS.md` for posts
- `docs/VISUAL_STORIES.md` for Visual Stories
- `_data/post_overrides.yml` for Medium-post field overrides
- `_config.yml` for site-wide settings

If those documents disagree with this file, fix this file.
