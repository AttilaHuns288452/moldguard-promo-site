#!/usr/bin/env python3
"""Dump per-frame structure: headings + presence of candidate spotlight selectors."""
import time
from playwright.sync_api import sync_playwright

URL = "http://localhost:8765/figma/MoldGuard_All_4.html"
CANDS = [".dash", ".loopline", ".phone-ui", ".feat-grid", ".compare", ".threshold",
         ".flow-svg", ".steps3", ".meet-stages", ".form-card", ".cta-band",
         ".qr-frame", ".store-badges", ".dl-hero", ".hero-stage", ".showcase",
         ".problist", ".statline", ".duo", ".roster", ".device-svg", ".dial-wrap"]

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 900}, device_scale_factor=2)
    pg.goto(URL, wait_until="networkidle"); time.sleep(1.5)
    frames = pg.query_selector_all("div.frame")
    for i, fr in enumerate(frames):
        # force lazy imgs by scrolling the whole frame through the viewport
        box = fr.bounding_box()
        for frac in (0.1, 0.3, 0.5, 0.7, 0.9):
            pg.evaluate("y => window.scrollTo(0, y)", box["y"] + box["height"] * frac)
            time.sleep(0.15)
        fr.scroll_into_view_if_needed(); time.sleep(0.4)
        fb = fr.bounding_box()
        heads = fr.eval_on_selector_all("h1,h2", "els => els.map(e => e.textContent.trim().slice(0,60))")
        present = []
        for sel in CANDS:
            el = fr.query_selector(sel)
            if el:
                eb = el.bounding_box()
                present.append(f"{sel}: [{eb['x']-fb['x']:.0f},{eb['y']-fb['y']:.0f} {eb['width']:.0f}x{eb['height']:.0f}]")
        print(f"== frame {i} ({fb['width']:.0f}x{fb['height']:.0f})")
        print("   H:", heads[:10])
        for s in present: print("   ", s)
    b.close()
