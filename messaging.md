# MoldGuard Promo Site — Messaging Fact-Check Register

**Purpose:** every claim used in the promo wireframes, mapped to its source in
`moldguard-proposal.pdf` (Cabuntas' research/proposal document). If a claim isn't
in this register, it isn't on the site.

- **Source:** `moldguard-proposal.pdf` (12 pp., PDF kept at project root)
- **Wireframes:** `index.html`, `features.html`, `how-it-works.html`, `contact.html`
- **Owner:** Promotional Website Design Lead · reviewed with Palma (Frontend Dev / UI/UX)
- **Status legend:** ✅ verified verbatim/near-verbatim · 🔶 condensed paraphrase (no new claims) · ⚠️ draft — needs team confirmation before publish

---

## Claim register

| # | Claim as it appears on the site | Where used | Source (proposal §) | Status |
|---|---|---|---|---|
| C1 | Mold growth follows prolonged high humidity + poor ventilation, linked to structural damage and respiratory/allergy risks | index (problem lede, implied) | Exec Summary | ✅ |
| C2 | MoldGuard = compact IoT-based mold risk **prevention and detection** system; temperature + humidity + VOC sensing; proprietary Mold Risk Index; closed-loop Peltier dehumidification; web dashboard + mobile app | all pages (hero, how-it-works) | Exec Summary, §1 | ✅ |
| C3 | Mold Risk Index uses RH + temperature + **sustained exposure duration** — not a simple humidity threshold | index, features F01, how-it-works step 2 | §1 objective 1, System Features 1 | ✅ |
| C4 | Households can't see rising risk until visible growth or odor appears | index problem card 01 | §2 bullet 1, Exec Summary | ✅ |
| C5 | Existing dehumidifiers use simple threshold triggers that ignore exposure duration and temperature → delayed/ineffective response | index problem card 02 | §2 bullet 2 | ✅ |
| C6 | Passive moisture absorbers: no monitoring, no data, no automation | index problem card 03, features table | §2 bullet 3, §4 table | ✅ |
| C7 | Affordable, vendor-agnostic monitoring for renters/small property owners is missing vs. enterprise building systems | index problem card 04, FAQ "who is it for" | §2 bullet 4 | ✅ |
| C8 | VOC sensing detects microbial off-gassing indicative of **existing** growth, ahead of visible signs | features F02, how-it-works step 1 | §1 objective 2, Features 2 | ✅ |
| C9 | Closed-loop auto-dehumidification via TEC1-12706 Peltier module, triggered by the Mold Risk Index, no manual action | features F03, how-it-works step 3 | §1 objective 3, Features 3 | ✅ |
| C10 | Web dashboard: historical humidity/temperature/VOC trends, multi-room / multi-unit monitoring | features F04, index, how-it-works step 4 | §1 objective 4, Features 4 | ✅ |
| C11 | Mobile app: real-time push notifications, live device status, manual override from anywhere | features F05, how-it-works step 4 | §1 objective 5, Features 5 | ✅ |
| C12 | Comparison table: passive absorbers / commercial smart dehumidifiers / MoldGuard rows incl. drawbacks ("requires dedicated power source and periodic condensate tray emptying") | features (comparison) | §4 table verbatim | ✅ |
| C13 | Open hardware (ESP32, TEC1-12706, off-the-shelf sensors) + free/open-source software; single fixed-cost development; full client ownership; no recurring subscription fees | features bonus tile, contact step 2, FAQ cost | §5 | ✅ |
| C14 | Specs: SHT31-D ±2% RH / ±0.3 °C (DHT22 budget alt); BME680 rec. or MQ-135; ESP32-WROOM-32, 2.4 GHz WiFi, 4 MB flash local buffering; 15×10×12 cm enclosure, ~50–100 ml tray | features (under the hood), how-it-works chips | §6 hardware table | ✅ |
| C15 | Software stack: Next.js/React/TS/Tailwind dashboard; Flutter or React Native app; Node.js/Express; PostgreSQL; Socket.io real-time sync | features (software accordion) | §7 | ✅ |
| C16 | Placement: tabletop or wall-mounted near humidity-prone areas (bathroom, closet, basement); browser dashboard optimized for desktop + mobile | index (where it lives), how-it-works setup | §9 | ✅ |
| C17 | Deployment includes final user training, documentation handover, on-site or remote installation support | contact step 3 | §8 Deployment milestone | ✅ |
| C18 | Contact: moldguard.dev.team@gmail.com · 09925430608 · sign-and-return proposal flow | contact page, all footers | §12 | ✅ (phone reformatted "0992 543 0608" for readability) |
| C19 | Team roster: 8 members with names + roles | contact (team grid) | §12 | ✅ (personal emails deliberately **not** shown — see Q5) |
| C20 | Hero headline "Know mold is coming before it shows." + taglines ("Stop cleaning up. Start preventing.", "Sense. Score. Act.") | index, how-it-works | creative framing of C2–C4; no factual add-ons | 🔶 |
| C21 | "Real-time" / "low-latency" sync between device, dashboard, app | how-it-works step 4 chip | §3 technical obstacle 4, §7 event bus | ✅ |
| C22 | FAQ answers on replacement dehumidifiers, offline behavior, exact pricing | how-it-works FAQ | **not in proposal** | ⚠️ Q1, Q3, Q4 |

## Deliberate omissions (do not add without a source)

- **No numeric risk scale, formula, thresholds, or accuracy %** for the Mold Risk Index — the algorithm is proprietary and the proposal publishes no figures (rule R3).
- **No mold-species names, health statistics, or "kills mold" claims** — the proposal never makes them; prevention/detection language only.
- **No uptime, MTBF, coverage-area (m²), or water-extraction-rate figures** — not in the proposal.
- **No customer testimonials, case studies, or deployment counts** — none exist yet.
- **No pricing numbers** — proposal says "fixed development fee" only (Q4).

## Open questions for the team

| # | Question | Owner | Blocks |
|---|---|---|---|
| Q1 | Does automatic dehumidification run offline (device-local decision) or does it require backend connectivity? Firmware behavior needed. | Firmware (Banting/Litang) | FAQ "without internet" |
| Q2 | Public pricing posture: show "fixed fee, no subscription" only, or actual figures? | Palma + PM (Banting) | features bonus tile, FAQ |
| Q3 | Can MoldGuard *replace* a standalone dehumidifier, or complement one? | Whole team | FAQ "do I still need a dehumidifier" |
| Q4 | Quote/procurement flow for the "Get Started" CTA — what actually happens after form submit? | PM + Backend (Fajardo) | contact form build note |
| Q5 | Publish team members' personal emails on the site? Wireframe default: names + roles only. | Palma + team | contact team grid |
| Q6 | Keep the honest "drawbacks" column for MoldGuard in the public comparison table? (Recommendation: yes — credibility.) | Palma | features comparison table |

## Fact-check method

1. Extracted proposal text via `pdftotext -layout` (12 pp.); claims lifted from Executive
   Summary, §1–§9, and §12.
2. Every sentence of marketing copy traced to a register row before inclusion; creative
   headlines (C20) checked to introduce no factual add-ons.
3. Numbers copied exactly (accuracy %, voltages, dimensions, tray capacity); formatting-only
   changes noted (C18 phone spacing).
4. Anything the proposal doesn't support was either omitted (see list above) or marked
   ⚠️ [DRAFT] in the wireframes with an owning question.
