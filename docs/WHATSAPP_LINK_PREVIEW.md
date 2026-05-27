# Social link previews (WhatsApp, Telegram, Slack, Facebook)

Operational notes on how link-preview cards are generated for this
blog, the bugs that prevented WhatsApp from rendering them, and the
fixes applied. Companion to `TELEGRAM_INSTANT_VIEW.md` (which covers
the in-app reader, a separate feature).

This file is for maintainers. It is excluded from the Jekyll build
(`docs` is in `_config.yml`'s `exclude` list) so it never ships to
the site.

---

## How previews work, per platform

| Platform | Who scrapes | Cache behaviour |
|---|---|---|
| **Facebook / Messenger** | `facebookexternalhit/1.1` (server-side) | Meta CDN cache; refreshable via Sharing Debugger |
| **WhatsApp** | Mobile app scrapes client-side; WhatsApp Web scrapes server-side via the same Meta backend | Per-device client cache (mobile) + Meta CDN (web). No official refresh endpoint. Keyed on canonical URL. |
| **Telegram** | `TelegramBot` server-side | Telegram cache; aggressive but eventually expires |
| **Slack** | `Slackbot-LinkExpanding` server-side | Slack cache |

Key consequence: **WhatsApp mobile generates previews on the user's
phone, not on a central server.** A failed scrape (bad markup, slow
network, client cache) shows no preview, and there is no way to force
a refresh remotely. WhatsApp Web, by contrast, uses the Meta backend
(same crawler as Facebook), so a Facebook Sharing Debugger re-scrape
fixes WhatsApp Web.

---

## The bug chain (2026-05-26/27)

Symptom: post URL shared on WhatsApp showed no preview, or later only
the bare domain (`l3ragio.github.io`) as title with no description and
no image — while Telegram and the Facebook Sharing Debugger rendered
the preview correctly.

Diagnosed and fixed in this order. Each was a real, independent
defect; the last one was the dominant cause.

### 1. Hero image too large (PNG, 2.9 MB)

The hero was a 1535x1024 PNG at 2.9 MB. WhatsApp silently drops
preview images above roughly 300 KB (some reports say lower).

**Fix:** convert to JPEG. Final asset is 1200x801, baseline DCT,
q≈72-82, chroma 4:2:0, sRGB, no ICC, no EXIF, **~190 KB**. Generated
with:

```bash
magick the-mask-is-the-person.png \
  -resize 1200x -strip -interlace none \
  -quality 82 -sampling-factor 4:2:0 -colorspace sRGB \
  -define jpeg:extent=200KB \
  the-mask-is-the-person-v2.jpg
```

`-interlace none` is important — see defect 3.

### 2. Duplicate `og:image:width` / `og:image:height`

`jekyll-seo-tag` emits `og:image:width` and `og:image:height`
automatically when `page.image.width` and `page.image.height` are set
in the post front matter. `_includes/metadata-hook.html` had been
edited to *also* emit them, producing duplicate tags in the head.
WhatsApp can silently drop a preview when `og:*` tags are duplicated.

**Fix:** removed the dimension emission from `metadata-hook.html`;
let `jekyll-seo-tag` own them via front matter. The hook now emits
only the tags `jekyll-seo-tag` does not (`og:image:secure_url`,
`og:image:type`), plus the standalone `og:description` (defect 5).

### 3. Progressive JPEG

The first JPEG conversion was Progressive DCT. Community reports
attribute WhatsApp preview-image drops specifically to progressive
JPEGs: the preview scraper bails before the progressive frame is
fully reconstructed.

**Fix:** re-encoded as baseline DCT (`-interlace none`). The asset is
`the-mask-is-the-person-v2.jpg`. A fresh filename also acts as a
cache buster for any scraper keyed on the old image URL.

### 4. Missing `</head>`, `</body>`, `</html>` — the dominant cause

`_config.yml` had `compress_html: { endings: all }`, which strips
every optional HTML5 closing tag, including `</head>`, `</body>`,
`</html>`. The deployed pages had **no `</head>` tag at all**
(`IndexOf('</head>')` returned `-1` on the live HTML). HTML5 permits
this; browsers recover. But WhatsApp's preview scraper abandons head
parsing when `</head>` never appears, producing the "bare domain
only" card.

**Fix:** restricted the `endings` list to inline-content optional
closers, preserving the structural closers:

```yaml
compress_html:
  clippings: all
  comments: all
  endings: [dt, dd, optgroup, option, colgroup, caption, thead, tbody, tfoot, tr, td, th, li]
  profile: false
  blanklines: false
```

After this fix the live HTML has `<head>` … `</head>` (byte ~48 to
~10532), `<body>` opening right after, and `</body></html>` at the
end. This is the change that made WhatsApp parse the OG tags at all.

### 5. Combined `twitter:description` + `og:description` tag

`jekyll-seo-tag` emits the description as a *single* element with
both attributes:

```html
<meta name="twitter:description" property="og:description" content="..." />
```

The Facebook Sharing Debugger flags this as "og:description missing"
(while still parsing the value via a lenient pass), and WhatsApp's
scraper appears to read only the `name=` attribute, dropping the
description from the card.

**Fix:** `metadata-hook.html` now emits a clean standalone
`<meta property="og:description" content="..." />` for posts (in
addition to the combined tag). Strict parsers find a property-only
tag; the combined one stays for parsers that take the first
occurrence.

---

## Current emitted tag set (per post)

From `jekyll-seo-tag` + `_includes/metadata-hook.html`:

```
og:title              (standalone)
og:locale
og:description        (combined twitter+og — from jekyll-seo-tag)
og:description        (standalone — from metadata-hook, defect 5 fix)
og:url
og:site_name
og:type = article
og:image              (-> the-mask-is-the-person-v2.jpg)
og:image:width 1200   (from front matter via jekyll-seo-tag)
og:image:height 801   (from front matter via jekyll-seo-tag)
og:image:alt
og:image:secure_url   (from metadata-hook)
og:image:type         (from metadata-hook, derived from extension)
twitter:card = summary_large_image
twitter:image / twitter:image:alt / twitter:title / twitter:site
```

`metadata-hook.html` derives `og:image:type` from the image path
extension (jpg→image/jpeg, png→image/png, webp→image/webp,
gif→image/gif) and only emits the post branch when
`page.layout == "post"` and `page.image` is set. A separate branch
handles `page.layout == "visual_story"`.

---

## How to verify after a change

1. **Deploy, then wait for CDN.** GitHub Pages (Fastly) caches HTML
   with `max-age=600`. Poll `Last-Modified` until it changes:

   ```bash
   curl -sI "https://l3ragio.github.io/posts/<slug>/?cb=$(date +%s%N)" \
     -A 'facebookexternalhit/1.1' -H 'Cache-Control: no-cache' \
     | grep -i last-modified
   ```

2. **Check closing tags exist:**

   ```bash
   curl -sS "https://l3ragio.github.io/posts/<slug>/?cb=$(date +%s%N)" \
     -A 'facebookexternalhit/1.1' | grep -c '</head>'   # must be >= 1
   ```

3. **Check the image is reachable + small + baseline:**

   ```bash
   curl -sI "https://l3ragio.github.io/assets/img/heroes/<img>.jpg" \
     -A 'WhatsApp/2.23.20.0'   # expect 200, image/jpeg, < ~250KB
   ```

4. **Facebook Sharing Debugger** (also refreshes WhatsApp Web's
   backend): <https://developers.facebook.com/tools/debug/sharing/>.
   Paste the canonical URL, "Scrape Again" twice. Confirm
   `og:title`, `og:description`, `og:image` are all parsed and the
   preview renders.

5. **WhatsApp Web in an incognito browser** (bypasses its local
   cache): web.whatsapp.com → Saved Messages → paste URL → wait ~10s.

---

## Caveats that are NOT bugs

- **WhatsApp mobile client cache.** Once the user's phone has cached
  "no preview" for a URL, only clearing the app cache fixes it
  (iOS: Offload App; Android: Clear Cache). Cache is keyed on the
  *canonical* URL, so `?v=2` query-param busting does NOT work — the
  `og:url` tag points scrapers back to the canonical, which is the
  cache key. Testing with a contact who has never received the link
  is the cleanest way to see a fresh fetch.
- **HTTP 206 in the Facebook Debugger.** Normal: the debugger sends a
  `Range` request and GitHub Pages responds 206 Partial Content.
- **`og:temporal:twitter:*` prefix in the debugger.** Normal: Meta's
  parser marks twitter tags it does not treat as native OG. WhatsApp
  uses the `og:*` tags, so this is harmless.
- **Node.js 20 deprecation warning in the Actions build.** Unrelated
  to previews; a workflow-maintenance item for `actions/checkout` and
  `actions/configure-pages`.

---

## Image spec that works for WhatsApp

- Format: **baseline** JPEG (not progressive)
- Size: **under ~250 KB** (aim ~190 KB)
- Dimensions: 1200px wide is safe; aspect 1.5:1 (1200x801) works,
  though 1.91:1 (1200x630) is WhatsApp's canonical card aspect if a
  future image needs to be maximally conservative
- Colorspace: sRGB, no ICC profile, no EXIF
- Served over HTTPS with `Content-Type: image/jpeg`

---

## Commit trail (2026-05-26/27)

- `a873a3e` social preview JPG + reading-time WPM
- `c11b6cb` read-time include override (site.words_per_minute)
- `62d4883` og:image dimensions / type / secure_url for posts
- `649caf3` remove duplicate og:image:width / og:image:height
- `b47da8f` hero JPEG tighter compression (192 KB)
- `ff084c2` hero v2 baseline (non-progressive) JPEG
- `8153baa` restore </head> </body> </html> (compress_html endings)
- `cbc452d` standalone og:description for strict parsers
