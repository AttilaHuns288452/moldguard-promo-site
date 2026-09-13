# DESIGN.md — MoldGuard promo site

Recorded from the built pages, not intentions. Any new page or section on this
site inherits this system; changes here are system changes.

## World

**Clean, clinical, trustworthy, domestic.** The site should read like a real
consumer IoT product company, with the clarity of Google-Nest-style product
sites. Navy-green + white dominant; **MoldGuard teal is the only loud accent**.
Severity (risk states) is communicated through typography and contrast only,
never colored lamps. Precision is kept; the instrument-station theme is gone.

## Color tokens (site.css `:root`)

| Token | Value | Role |
|---|---|---|
| `--paper` | `#F7F8F6` | warm off-white page ground |
| `--paper-deep` | `#EDF1F0` | subtle alternating band tint |
| `--surface` | `#F2F4F2` | inputs, subtle fills |
| `--card` | `#ffffff` | cards, showcase panels |
| `--line` / `--line-strong` | `#DDE5E5` / `#C7D4D3` | hairlines, borders |
| `--deep` / `--deeper` | `#183B43` / `#122C33` | navy-green dark: CTA band, footer, phone chrome (`--deeper` = footer/phone-inset only) |
| `--accent` | `#2D9A91` | **MoldGuard teal — THE accent:** primary CTA, key data, active states |
| `--accent-ink` | `#1E6E68` | teal on light backgrounds; CTA fill (white text ≈ 6:1) |
| `--ink` / `--ink-2` / `--ink-3` | `#213132` / `#465754` / `#687979` | body text / secondary / muted |
| `--ink-soft` / `--ink-strong` | `#687979` / `#465754` | aliases of the muted grays — kept for token-name compatibility with the other pages |
| `--sky` | `#8FBDB8` | LEGACY ALIAS, muted teal-gray; only existing chart-bar/state rules reference it — no new uses |
| `--beige` | `#F7F8F6` | LEGACY ALIAS = `--paper`; existing band rules collapse into the foundation |
| `--amber` / `--coral` / `--ok` | `#d9973b` / `#c25a41` / `#3d8f6a` | RETIRED — definitions kept only for token history; no rule may reference them |

**Simplified 4-role palette:** PAPER (`--paper`/`--paper-deep`/`--card`) ·
DARK (`--deep`/`--deeper`) · INK (text grays) · TEAL (`--accent`/`--accent-ink`).
The page must read navy-green + white dominant, teal as the only loud accent.
No color carries a "narrative" role: no beige warmth bands, no sky environment
graphics.

**Severity-via-typography rule:** risk severity (Steady / Watch / Low /
Elevated / High) is communicated only through label text, type weight, and
background intensity in the neutral/teal range — never through amber/coral/green
lamps.

Contrast (measured): ink on paper 12.7:1 · ink-2 on paper 7.2:1 · accent-ink on
paper 5.7:1 · white on accent-ink (CTA) 6.0:1 · on-dark-2 on deep 6.1:1.

Elevation: **flat by default**. Borders carry structure; the only shadow is on
the hero showcase panel (`--shadow-card`) and raised phone mocks
(`--shadow-pop`). Radii: 8px controls, 12px cards, one 20px hero showcase panel.

## Typography

- **Display:** Bricolage Grotesque 650–700, tracking −.03em, clamp(2.5→4.1rem) h1.
- **Text:** Figtree 400–700, body 16.5px/1.6.
- **Mono:** Spline Sans Mono, **measurements and row indices only** — risk
  readouts (38/100), RH %, °C, and the 01/02/03 step numbers. Everything else
  (labels, captions, fine print, tags) is Figtree. No mono eyebrows/kickers.

## Components (all in site.css)

Sticky blurred header · logo (shield-arc mark + wordmark) · buttons
(`--accent-ink` primary, ghost, light-on-dark; 9–10px radius; labels name the
action: "Get Started") · editorial numbered lists (`.problist`: 2-col hairline
grid, mono index + title + one sentence) · alternating solution rows
(`.solrow`: large visual + number + title + one line, left/right alternating) ·
numbered steps (`.steps3`: hairline top rule, 01/02/03 columns) · features
list (`.featlist`: two-column numbered rows) · tide-table rows (`.rows`/
`.row`, shared grammar) · dashboard mock (`.dash`: trend line + plain-text
room states, Low/Elevated labels via typography) · phone mocks (`.phone-ui`,
`.showcase-phone`: app name, risk index, one-line status, plain-text room
list) · simplified device SVG (clean body, grille, single teal status LED —
no control-panel readout, no gauge) · photos with plain figcaption (no float
status cards) · statement band (`.statement`, features page) · comparison
table (`.ours-tag` pill, features page) · accordions · forms · roster · navy
CTA band (`.cta-band`, no bezel ornament) · footer (navy, Figtree fine print).

**No chips, no lamps, no speclines, no kickers, no floating status labels.**
Nothing decorative survives: every element either carries data or structures
content.

## Distribution (treat it like a real website)

Every page ships: canonical URL, full Open Graph + Twitter `summary_large_image`
card pointing at `assets/og-card.png` (1200×630, rendered from the site's own
palette/type — regenerate by re-screenshotting if the hero story changes),
per-page meta description, favicon. Repo root: `robots.txt` + `sitemap.xml`
(listing the bare directory URL as home), `404.html` (on-brand, noindex),
`.nojekyll`. Canonical home = `.../moldguard-promo-site/` (no `index.html`).

## Imagery

- **Photography:** real category photos, downloaded to `assets/` (no
  hotlinking): bathroom, window/bathroom, purifier/bath, condensation, living
  room. All are **placeholder** material — footer says so on every page;
  replace with product/team photography when it exists.
- **Device/UI:** authored SVG (clean device render, dashboard, phone) — never
  photos of other brands' devices.
- **QR:** `download-qr.svg`, generated by `generate_qr.py` — REAL and
  decode-verified. Payload = `APP_DOWNLOAD_URL` constant (currently the
  download page itself as smart-link placeholder; retarget + regenerate when
  store listings go live). One place to change.
- **Store badges:** official artwork only — `assets/appstore-badge.svg`
  (Apple badge API) + `assets/google-play-badge.png` (Google Play badge).
  Never redraw, recolor, or rename them.

## Voice & claims

Messaging is frozen to `messaging.md` C-register. Numbers shown on mocks
(38/100 risk index, room states) are illustrative demo data. No em dashes in
visible copy; sentences are short, benefit-first, plain product-team voice.

## Page inventory

index — the 8 content sections: (1) light editorial hero (category line, h1,
one paragraph, Get Started + See how it works, showcase panel with device SVG
+ phone app screen), (2) problem (4-item editorial numbered list), (3) solution
"Meet MoldGuard." (3 alternating rows: device / dashboard / app), (4) "Sense.
Score. Act." 3-step section, (5) features (6-item editorial two-column list),
(6) own-it band, (7) where-it-lives photo section, (8) navy final CTA. The
Mold Risk Index panel moved to features.html; the ecosystem/system diagram
moved to how-it-works.html.

features (duo: dial flagship + VOC, rows, statement, comparison, spec
accordions) · how-it-works (loop diagram, 4 stages alternating, setup rows,
wide photo, FAQ) · contact (real mailto form, channel rows, 3-step rows,
roster of 8) · **download** (Get Started destination: QR card, store pills,
phone stage, perk rows). Every "Get Started" leads to `download.html`.

## Motion

Live-dot pulse (2.4s) only; reduced-motion kills it. Everything else static.

## Accessibility floor

Body text ≥4.5:1 (measured ratios above). Focus-visible 2.5px teal ring
everywhere. Decorative SVGs `aria-hidden`; photos carry real alt text; QR
labeled as placeholder. Forms use real labels + required. Skip link on every
page.
