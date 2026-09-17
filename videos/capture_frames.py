#!/usr/bin/env python3
"""Capture MoldGuard frames (lazy-imgs forced) + spotlight rects for the walkthrough."""
import json, time
from playwright.sync_api import sync_playwright

URL = "http://localhost:8765/figma/MoldGuard_All_4.html"
OUT = "/home/attila/Documents/Projects/moldguard-promo-site/videos"

# frame idx -> {spotlight_name: selector}
TARGETS = {
    0: {"hero_h1": "h1", "showcase": ".showcase", "problist": ".problist",
        "meetwrap": ".meet-wrap", "flowsvg": ".flow-svg", "phoneui": ".phone-ui"},
    1: {"duo": ".duo", "dial": ".dial-wrap", "compare": ".compare"},
    2: {"loopline": ".loopline", "dial": ".dial-wrap", "statline": ".statline", "herostage": ".hero-stage"},
    3: {"formcard": ".form-card", "roster": ".roster", "ctaband": ".cta-band"},
    4: {"qr": ".qr-frame", "badges": ".store-badges", "dlhero": ".dl-hero"},
}

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 900}, device_scale_factor=2)
    pg.goto(URL, wait_until="networkidle"); time.sleep(1.5)
    frames = pg.query_selector_all("div.frame")
    manifest = []
    for i, fr in enumerate(frames):
        fb = fr.bounding_box()
        for frac in (0.08, 0.25, 0.45, 0.65, 0.85, 1.0):  # force lazy images
            pg.evaluate("y => window.scrollTo(0, y)", fb["y"] + fb["height"] * frac)
            time.sleep(0.25)
        pg.evaluate("window.scrollTo(0, 0)"); time.sleep(0.6)
        fb = fr.bounding_box()
        path = f"{OUT}/frame_{i}.png"
        fr.screenshot(path=path)
        rects = {}
        for name, sel in TARGETS.get(i, {}).items():
            el = fr.query_selector(sel)
            if not el:
                rects[name] = None; continue
            eb = el.bounding_box()
            rects[name] = [round(eb["x"]-fb["x"],1), round(eb["y"]-fb["y"],1),
                           round(eb["width"],1), round(eb["height"],1)]
        manifest.append({"frame": i, "file": path, "w": round(fb["width"]), "h": round(fb["height"]), "rects": rects})
        print(f"frame {i}: {fb['width']:.0f}x{fb['height']:.0f}")
        for k, v in rects.items(): print(f"   {k}: {v}")
    b.close()

json.dump(manifest, open(f"{OUT}/manifest.json", "w"), indent=1)
print("manifest saved")
