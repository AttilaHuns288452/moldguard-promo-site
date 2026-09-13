# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML/CSS, no build step. The incumbent repo ships plain HTML pages with one shared stylesheet; the user asked to keep this structure and get a high-fidelity visual pass, not a framework migration.

## Users

Primary: Filipino homeowners, renters, dormitory and small-property managers evaluating an IoT mold-prevention device. Secondary: the eight-student capstone team and evaluators, for whom this promo site is the product's public face.

## Product Purpose

MoldGuard is a compact IoT device plus web dashboard plus mobile app that senses humidity, temperature, and VOCs; scores a proprietary Mold Risk Index (humidity + temperature + sustained exposure duration, not a single threshold); and automatically runs a Peltier dehumidifier when risk rises — closing the loop before mold is visible. Success for this site: a visitor understands the problem, the loop, and requests a quote.

## Positioning

Mold-specific closed-loop prevention — sense, score, act, report — at a fixed development fee with full ownership and no subscription, for renters and small property owners priced out of building-grade systems. A competitor could copy the sensors; it could not copy the risk model or the price posture.

## Operating Context

Philippine homes: ~30°C and 80% RH indoor air; mold colonizes above 75% surface humidity; dew point ~26.2°C at 80% RH. Placement: tabletop or wall-mounted in bathrooms, closets, basements. All site claims are governed by `messaging.md` — every sentence traces to `moldguard-proposal.pdf` via the C1–C22 register; draft claims are flagged ⚠️ with owning open questions Q1–Q6.

## Capabilities and Constraints

No backend on this site yet (contact form build note pending, Q4). No numeric risk scale, formula, or thresholds published (rule R3). No testimonials, case studies, deployment counts, or pricing numbers. Comparison table keeps the honest drawbacks column for MoldGuard itself (Q6, recommendation: keep). Team shown as names + roles only (Q5 default). FAQ answers marked [DRAFT] need team confirmation (Q1, Q3, Q4).

## Brand Commitments

User-pinned palette: the cold icy-blue world of the reference image — dominant icy white-blue ≈ #dfe7ec (65%), steel blue ≈ #567b8d (16%), deep navy-slate ≈ #2f4157 (15%). User-pinned: keep the four-page structure (Landing / Features / How it works / Contact) and the existing messaging verbatim. "Get Started" must lead to a download page offering the mobile app with a QR code (fake for now). Fake/placeholder photography is user-approved for this build.

## Evidence on Hand

- `moldguard-proposal.pdf` — 12-page source of every claim (C1–C22).
- `messaging.md` — claim register, deliberate omissions, open questions.
- Contact facts: moldguard.dev.team@gmail.com · 0992 543 0608 · team roster §12.
- Real photography: none. All imagery must be authored synthetic placeholder material (stock photos of the *category* — interiors, humidity, devices — are user-approved as fake photos), labeled internally as replaceable.
- Reference palette image: `/home/attila/Downloads/491024461_1075338854405101_5701765375661750483_n.jpg` (736×1104, 65.6% #dfe7ec / 16% #567b8d / 14.7% #2f4157, mean luminance 183, high contrast).

## Product Principles

1. Honest prevention, not miracle claims — the drawbacks column stays.
2. The closed loop (Sense → Score → Act → Report) is the story every page retells.
3. Claim discipline: nothing on the site outside the C-register without a ⚠️ flag.
4. Fixed-fee ownership is the trust differentiator — never bury it.
