# DESIGN.md — MoldGuard promo site

<!-- impeccable:documented-from-build 1 · seed c4ef9450 · 2026-09-13 -->

Recorded from the built pages, not intentions. Any new page or section on this
site inherits this system; changes here are system changes.

## World

**Coastal instrument station.** The site reads like the device's own station
log: a navy instrument world sitting on icy white-blue paper. The reference
palette (Attila's pinned image, `~/Downloads/491024461_*.jpg`) is law:
dominant icy white-blue ~65%, steel blue ~16%, deep navy-slate ~15%.
Assigned by concept-seed (marine-meteorological instrument world, seed
`c4ef9450`, challenger "brick build-instruction book" fused into the numbered
stage/setup diagrams).

## Color tokens (site.css `:root`)

| Token | Value | Role |
|---|---|---|
| `--paper` | `#e9eff3` | page ground |
| `--paper-deep` | `#dfe7ec` | alternating bands, icon tiles |
| `--surface` | `#f6fafc` | inputs, chips, statline |
| `--card` | `#ffffff` | cards |
| `--line` / `--line-strong` | `#cdd9e0` / `#aebfca` | hairlines, borders |
| `--steel` / `--steel-deep` | `#567b8d` / `#3e5f70` | secondary buttons, chip ink |
| `--deep` / `--deeper` | `#2f4157` / `#22334a` | panels, ticker, footer, primary buttons |
| `--accent` / `--accent-ink` | `#2e8fa3` / `#1d6b7c` | glacial teal — live dots, lamps, focus rings |
| `--sky` | `#8ec7dd` | sky blue — charts, environmental graphics, Wi-Fi/cloud nodes, secondary accents (pinned 5-color system) |
| `--beige` | `#f0e8da` | warm home-context section bands, used sparingly — max 2 bands per page (pinned 5-color system) |
| `--amber` / `--coral` | `#d9973b` / `#c25a41` | elevated / high risk lamps — **retired from index.html** (legacy pages only) |
| `--ok` | `#3d8f6a` | low-risk lamp — **retired from index.html** (legacy pages only) |

**Pinned 5-color system (index.html, binding):** NAVY (`--deep`/`--deeper`) ·
TEAL (`--accent`) · SKY (`--sky`) · WHITE (`--card`) · BEIGE (`--beige`).
Steel `--steel`/`--steel-deep` stays as a navy-tint for secondary chrome only.
**Severity-via-typography rule:** risk severity (LOW/MODERATE/HIGH/CRITICAL) is
communicated only through type weight, label text, border weight, background
intensity, and contrast — never through amber/coral/green lamps. Ladder:
LOW = teal chip · MODERATE = sky chip · HIGH/CRITICAL = navy treatment
(white-on-navy chip, heavier border, bolder label). Teal is the primary accent
(CTAs, active states, key numbers); sky complements it for charts/lines/env
data, never competing.
| `--on-dark` / `--on-dark-2` | `#e7f0f5` / `#a9c0cf` | text on navy |

Elevation: **flat by default**. Borders carry structure; the only shadow is
`--shadow-pop` on the few raised panels (hero stage, statement bands, floats).
No CTA glow, no per-card shadows. Radii: 9–10px controls, 12–16px panels.

## Typography

- **Display:** Bricolage Grotesque 650–700, tracking −.03em, clamp(2.5→4.1rem) h1.
- **Text:** Figtree 400–700, body 16.5px/1.6 — humanist and warm; the page must
  read like a product site, not a terminal.
- **Readouts:** Spline Sans Mono, 10–12.5px, uppercase, +.1–.16em tracking.
  Mono is for **data** (statline, badges, captions, lamps, row indices,
  step letters) — never for kickers above headings (banned by craft floor;
  data-bearing readouts are fine).
- **Chrome:** no top ticker bar — the site opens with a clean sticky nav
  (logo + wordmark, links, one CTA). Favicon + meta description on every page.

## Components (all in site.css)

Ticker (navy live-status bar) · sticky blurred header · logo (shield-wave
mark + wordmark/sub-label) · buttons (`--deep` primary, steel secondary,
ghost, on-dark light; 9–10px radius; labels name the action: "Get the app") ·
mono spec lines (`.specline` — the only annotation device) · **tide-table
rows** (`.rows`/`.row`: 2px navy top rule, mono index · title · text, hairline
separators — features, steps, channels, perks all use this one grammar) ·
trio (`.trio`: one strip, three hairline columns) · duo (`.duo`: two-column
instrument panel) · statement band (`.statement`: flat navy, big claim + mono
tag — used once per page at most) · station-log rows (WK ## · title · text ·
coral lamp) · threshold ruler (authored SVG: 60–100% RH scale, 75%
colonization marker, 80% PH-average marker) · loop nodes with clip-path
arrow connectors · risk dial SVG (animated needle; reduced-motion respected)
· dashboard/phone mocks (`.dash`, `.phone-ui`) · device render SVG · hero
benefit chips (`.chip`: white pill, hairline border, teal dot — hero only,
the three headline capabilities; never as section decoration) · photo
cards with mono figcaption + `.float-card` status · comparison table
(`.ours-tag` pill) · accordions (plus/minus circle) · forms (46px fields,
teal focus ring) · roster (`.roster`: 4-col hairline team grid, small
gradient avatars) · flat navy CTA with 7px inset outline (instrument bezel,
no gradient, no glow) · footer (navy, mono fine print).

**Anti-slop rules baked in:** no equal-card grids (rows/duo/trio instead),
no icon tiles, chips confined to the hero benefit trio, no decorative
eyebrows, one statement band per page, shadows only on pop panels, honest
button labels.

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
- **Device/UI:** authored SVG (device render, dial, dashboard, phone) — never
  photos of other brands' devices.
- **QR:** `download-qr.svg`, generated by `generate_qr.py` (deterministic,
  fake, non-scannable). Replace before launch; store pills are
  `aria-disabled` placeholders.

## Voice & claims

Messaging is frozen to `messaging.md` C-register. Draft FAQ answers carry
inline `[Team note: … Q#]` markers instead of silent claims. Numbers shown on
mocks (38 ELEVATED, 82% RH) are illustrative demo data, consistent across all
pages.

## Page inventory

index (hero composite, threshold ruler, station log, solution trio, loop,
feature rows, own-it statement, placement, CTA) · features (duo: dial
flagship + VOC, rows 03–05, bonus statement, comparison, spec accordions) ·
how-it-works (loop diagram, 4 stages alternating, setup rows A/B/C, wide
photo, FAQ) · contact (real mailto form, channel row-grid, 3-step rows,
roster of 8) · **download** (Get Started destination: QR card, store pills,
phone stage, perk rows). Every "Get Started" leads to `download.html`.

## Motion

Two authored moments only: live-dot pulse (2.4s) and dial needle sweep on
load. Exponential ease-out; everything else static. Reduced-motion kills both.

## Accessibility floor

Body text ≥4.5:1 (ink on paper ≈ 9:1; on-dark-2 on deep ≈ 7:1). Focus-visible
2.5px teal ring everywhere. Decorative SVGs `aria-hidden`; photos carry real
alt text; QR labeled as placeholder. Forms use real labels + required.
