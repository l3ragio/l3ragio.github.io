# Telegram Instant View

Telegram supports a native in-app reader called **Instant View** (IV).
When a user shares a link in Telegram and an IV template exists for
that URL, Telegram displays an "Instant View" button under the link
preview. Tapping it opens the article inside Telegram with a clean,
fast-loading reader UI — no browser, no scripts, no JavaScript.

This document defines the IV template for posts on this blog
(`l3ragio.github.io/posts/*`) and explains how to submit it to
Telegram for review.

WhatsApp has no equivalent feature. WhatsApp link previews are
read-only cards; tapping them opens the device browser. There is no
way to make a post readable inside the WhatsApp app. The Instant View
approach below is Telegram-only.

---

## The template

Paste this verbatim into Telegram's IV editor (see submission steps
below). Tested against the HTML structure Chirpy 7.2 emits for the
default `post` layout used by this blog.

```iv
# Telegram Instant View template v2.1
# For: l3ragio.github.io (Jekyll/Chirpy v7.2 blog)
# Applies to: /posts/<slug>/ URLs only.

~version: "2.1"

# Only apply to actual blog posts, not the index / categories / tags.
?path: /posts/.+

# ── Title ─────────────────────────────────────────────────────────
# Chirpy emits the post title as <h1 data-toc-skip> inside
# <article><header>. data-toc-skip is the marker that distinguishes
# the title H1 from any H1 the user might write inside the body.
title: //article//h1[@data-toc-skip]

# ── Subtitle ──────────────────────────────────────────────────────
# The lead paragraph beneath the title (Chirpy class "post-desc").
subtitle: //article//p[has-class("post-desc")]

# ── Author + author URL ───────────────────────────────────────────
# Byline is rendered as: By <em><a href="...">Davide Bragetti</a></em>
# inside the post-meta block.
$author_link: //article//header//div[has-class("post-meta")]//em//a
author:       $author_link
author_url:   $author_link/@href

# ── Published date ────────────────────────────────────────────────
# Chirpy sets data-ts on the <time> element to the Unix timestamp.
# IV will format this as a localised date in the reader.
published_date: //article//time/@data-ts

# ── Site name ─────────────────────────────────────────────────────
# Literal string — shown above the article in the IV reader.
site_name: "Davide Bragetti"

# ── Cover image ───────────────────────────────────────────────────
# The hero <a class="preview-img"> wraps the inline post image; its
# href points to the full-resolution JPG asset.
cover: //article//header//a[has-class("preview-img")]/@href

# ── Body ──────────────────────────────────────────────────────────
# Everything inside <div class="content">. This already excludes
# <article><header> (title + meta + hero) which IV consumes from the
# dedicated properties above, so the body starts clean at the TL;DR
# blockquote and the first <h2>.
body: //article//div[has-class("content")]

# ── Strip UI scaffolding that snuck into <article> ────────────────
# These elements are siblings of <div.content> inside <article> but
# would otherwise leak through IV's article rendering if it included
# the whole <article>. Removing defensively in case future Chirpy
# versions change the nesting.
@remove: //*[@id="toc-bar"]
@remove: //*[@id="toc-popup"]
@remove: //*[@id="toc-solo-trigger"]
@remove: //*[@id="toc-wrapper"]
@remove: //div[has-class("post-tail-wrapper")]

# ── Strip the figcaption duplication ──────────────────────────────
# Chirpy renders the hero's alt-text as a <figcaption> beneath the
# preview-img anchor. IV uses the alt attribute on the cover image
# directly so the figcaption is redundant in the reader.
@remove: //article//header//figcaption
```

---

## How to submit it to Telegram

1. **Open the IV editor** at <https://instantview.telegram.org/>.
   Click *"My Templates"* in the top-right.

2. **Log in** with the Telegram account you want to own the template.
   You authorise via the desktop Telegram app or the Telegram Web QR
   scan. The account that submits the template will be the listed
   maintainer; templates are visible to all Telegram users globally
   once approved, regardless of who submitted them.

3. **Create a new template**. Click *"My Templates" → "+"* or open
   <https://instantview.telegram.org/my> and click *"Add Template"*.

4. **Paste a sample post URL** when prompted. Recommended:
   `https://l3ragio.github.io/posts/uno_nessuno_centomila_e_tutti/`
   (the longest current post — better stress-test of the template).

5. **The editor opens** with the rendered page on the left and a
   text editor on the right. The editor starts empty (or with a
   minimal scaffold). Paste the template above, replacing whatever
   is there.

6. **Click *"Track Changes"*** in the toolbar. The reader preview on
   the right updates to show what Telegram users would see. Verify:
   title appears, subtitle appears, author byline renders, date is
   formatted, cover image appears, body starts at the TL;DR
   blockquote, no TOC scaffolding leaks through.

7. **Test on additional URLs**. The editor has a *"Sample URLs"*
   panel. Add at least 3–5 URLs from different posts on the blog:
   `/posts/misalignment-by-reaction/`,
   `/posts/does-safe-ai-equal-safe-world/`,
   `/posts/to-be-or-to-game/`,
   and the new post above. The preview should render correctly for
   all of them. If a particular post breaks the template, refine the
   XPath selectors (the cause is almost always a structural quirk in
   that post — e.g., a hand-rolled `<h1>` inside the body).

8. **Save the template**. Click *"Save"* in the toolbar. This stores
   the template under your account but does NOT make it active for
   Telegram users yet.

9. **Submit for review**. Click *"Submit Template"* or *"Make
   Public"* (button name varies). Telegram's review team checks
   templates for correctness, completeness, and that they don't
   strip important content. Review typically takes 3–14 days. You
   may be asked for refinements.

10. **Once approved**, the template applies automatically to all
    URLs matching `?path: /posts/.+` on `l3ragio.github.io`. Any
    Telegram user who shares a post URL will see the *"Instant
    View"* button under the link preview. Tapping it opens the
    article inside Telegram.

---

## Testing the template before submission

The IV editor's live preview is the authoritative test. But you
can also use Telegram's bot `@previews` (or the IV bot if it's
been renamed):

1. Open Telegram, search for `@previews` or `@InstantViewBot`.
2. Send the bot a post URL.
3. If your template is saved (even before review), the bot replies
   with the IV preview using your draft template.
4. Forward / share the bot's reply to any chat — that chat will see
   the live IV button.

---

## Maintenance

The template depends on Chirpy's HTML structure. If we upgrade Chirpy
to a major new version (e.g., 7 → 8) and the post template changes
(`<h1 data-toc-skip>` becomes something else, or `<div
class="content">` becomes `<main class="post-content">`), the
Instant View template will break and need re-submission.

To catch this early, after any Chirpy upgrade open one post in the
IV editor with this template loaded and verify the preview still
renders correctly before redeploying.

---

## What about WhatsApp?

WhatsApp does not have an in-app reader equivalent to Telegram's
Instant View. There is no template format, no plugin, no API call,
and no meta-tag-based mechanism that makes a link openable inside
the WhatsApp app rather than the device browser.

The WhatsApp "rich preview" we render for shared links — title,
description, og:image, og:site_name — is already the maximum content
WhatsApp surfaces in-app. Tapping the preview always sends the user
to their browser.

If you want WhatsApp users to read the post quickly, the only levers
available are page weight and load time. The current post HTML is
~75 KB compressed, the CSS bundle is ~110 KB, fonts load async, and
there is no client-side JavaScript on the critical path — the page
should be readable on mobile networks within ~1 second of the
browser opening. That's the best we can do for WhatsApp users.
