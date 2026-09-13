# MoldGuard — Promotional Website Wireframes

Low-fidelity wireframes for the MoldGuard V1.0 promo site: landing, features,
how-it-works, and contact/get-started. Messaging is grounded in the team's
research proposal (`moldguard-proposal.pdf`) and fact-checked in
[`messaging.md`](messaging.md).

**Status:** v0.1 — ready for review with Palma (Frontend Dev / UI/UX) before
any visual design pass.

## Pages

| File | Page | Sections |
|---|---|---|
| `index.html` | Landing | hero · problem (4 cards) · solution trio · how-it-works teaser · features teaser · placement · CTA |
| `features.html` | Features | 5 system features + ownership tile · comparison table · specs accordion · CTA |
| `how-it-works.html` | How it works | closed-loop diagram · 4 alternating steps · setup & placement · FAQ · CTA |
| `contact.html` | Contact / Get started | lead form · direct channels · next-steps · team grid · CTA |

Supporting files: `wireframe.css` (shared gray-box styles, no build step) ·
`messaging.md` (fact-check register C1–C22 + open questions Q1–Q6) ·
`review-email.md` (send-ready review request to Palma) ·
`moldguard-proposal.pdf` (source document — the site may not claim anything it doesn't support).

## How to review

1. Open `index.html` in a browser (links between pages work).
2. Read the amber **✎ notes** — they carry the review questions for Palma.
3. Cross-check any claim against `messaging.md` (register C1–C22).
4. Leave feedback inline (HTML comments, Figma, or annotated screenshots).
5. Not sure what to ask her first? `review-email.md` lists the four highest-priority
   decisions in a copy-paste email.

## Palma review checklist

- [ ] **Brand direction** — placeholder accent (`--accent` in `wireframe.css`) is not a
      brand decision; confirm palette/typography direction so the site matches the
      mobile-app design language.
- [ ] **Hero treatment** — pick (a) product shot, (b) device + phone composite, or
      (c) animated risk dial (note on `index.html` hero).
- [ ] **Dashboard/app thumbnails** — promo site should preview the real UI once her
      UI kit settles (note on index "solution" trio).
- [ ] **Comparison table tone** — keep the honest "drawbacks" column for MoldGuard?
      (messaging.md Q6, note on features.html)
- [ ] **"Under the hood" depth** — keep the specs accordion on the features page or
      demote to a footer block? (note on features.html)
- [ ] **Loop diagram rendering** — icons vs. animation vs. static (note on
      how-it-works.html)
- [ ] **FAQ drafts** — three answers are ⚠️ DRAFT pending team answers
      (messaging.md Q1, Q3, Q4)
- [ ] **Team section** — publish names/roles? Personal emails excluded by default
      (messaging.md Q5, note on contact.html)
- [ ] **Pricing posture** — "fixed fee, no subscription" wording only, or figures?
      (messaging.md Q2)
- [ ] **"From message to mold-free" heading** — tone check on contact.html next-steps
- [ ] **Footer scope** — socials, privacy page, other links TBD (noted on index footer)

## Acceptance criteria status

- **Wireframes completed for all core website pages** — ✅ 4/4 pages, desktop-first with
  mobile stacking behavior in the shared CSS.
- **Messaging fact-checked against Cabuntas' research** — ✅ register C1–C22 in
  `messaging.md`; every claim traced to the proposal; unsupported claims omitted or
  flagged ⚠️ with an owner.
- **Reviewed with Palma for alignment with overall product vision** — ⏳ blocked on the
  checklist above; the wireframes carry targeted questions at the exact decision points.
  Send the ready-made request in `review-email.md` to kick this off.

## Source of truth

`moldguard-proposal.pdf` — MoldGuard V1.0 software development proposal (12 pp.).
The promo site may not claim anything the proposal doesn't support; additions go
through the register in `messaging.md` first.
