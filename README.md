# MoldGuard — Promo Site

Promotional website for **MoldGuard**, an IoT mold-risk prevention and detection
system: a compact sensor unit, web dashboard, and companion app that score a live
Mold Risk Index and activate a connected dehumidifier automatically.

Live: https://attilahuns288452.github.io/moldguard-promo-site/

## Pages

| File | Page | Sections |
|---|---|---|
| `index.html` | Landing | hero · problem · Meet MoldGuard · Sense/Score/Act · features · ownership · placement · CTA |
| `features.html` | Features | flagship MRI + dial · feature rows · comparison · specs accordion · CTA |
| `how-it-works.html` | How it works | closed loop · stages · placement · FAQ (centered, ~660px) · CTA |
| `contact.html` | Contact | lead form · direct channels · next steps · team roster · CTA |
| `download.html` | Get the app | centered app-download handoff: QR · scan instruction · official store badges |

## System

Static HTML + one shared stylesheet (`site.css`), no build step, no JavaScript.
Figma-safe by construction: static layouts, authored SVG, no animation-dependent
content. The import-ready board is regenerated with:

```
python3 build-figma-board.py    # -> figma/MoldGuard_All_4.html (5 frames, 1280px)
```

## Design system

`DESIGN.md` is the contract: 17-token palette (warm off-white foundation,
deep blue-green `#183B43`, teal `#2D9A91` as the single accent, neutral gray
borders/ink), Bricolage Grotesque display / Figtree text / Spline Sans Mono for
measurements and row numbers only, flat elevation, editorial lists over card
grids. Severity and state are communicated with typography and contrast, never
color-coded lamps.

## Content governance

All claims trace to `moldguard-proposal.pdf` via the register in
[`messaging.md`](messaging.md) (C1–C22). Nothing goes on the site that the
proposal doesn't support. Demo numbers shown in mockups are labeled illustrative.

## QR / store links

`generate_qr.py` generates a real, decode-verified QR code. Its destination is
the `APP_DOWNLOAD_URL` constant; store-listing URLs get wired into the badges
at launch (marked in `download.html`). Regenerate after changing:

```
python3 generate_qr.py
```

## Status

Presentation-ready prototype. Footer disclaimers (prototype build, not a mold
diagnostic) are deliberate and stay.
