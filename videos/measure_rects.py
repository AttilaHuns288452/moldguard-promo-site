#!/usr/bin/env python3
"""Measure spotlight rects atomically via one page.evaluate per frame."""
import json, time
from playwright.sync_api import sync_playwright

URL = "http://localhost:8765/figma/MoldGuard_All_4.html"
TARGETS = {
    0: {"hero_h1": "h1", "showcase": ".showcase", "problist": ".problist",
        "meetwrap": ".meet-wrap", "flowsvg": ".flow-svg", "phoneui": ".phone-ui"},
    1: {"duo": ".duo", "dial": ".dial-wrap", "compare": ".compare"},
    2: {"loopline": ".loopline", "dial": ".dial-wrap", "statline": ".statline", "herostage": ".hero-stage"},
    3: {"formcard": ".form-card", "roster": ".roster", "ctaband": ".cta-band"},
    4: {"qr": ".qr-frame", "badges": ".store-badges", "dlhero": ".dl-hero"},
}

JS = """(arg) => {
  const fr = document.querySelectorAll('div.frame')[arg.i];
  const fb = fr.getBoundingClientRect();
  const out = {frame: [fb.left, fb.top, fb.width, fb.height].map(v => Math.round(v*10)/10)};
  for (const [name, sel] of Object.entries(arg.sels)) {
    const el = fr.querySelector(sel);
    if (!el) { out[name] = null; continue; }
    const eb = el.getBoundingClientRect();
    out[name] = [eb.left-fb.left, eb.top-fb.top, eb.width, eb.height].map(v => Math.round(v*10)/10);
  }
  return out;
}"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 900}, device_scale_factor=2)
    pg.goto(URL, wait_until="networkidle"); time.sleep(1.5)
    manifest = json.load(open("/home/attila/Documents/Projects/moldguard-promo-site/videos/manifest.json"))
    for i in range(len(manifest)):
        res = pg.evaluate(JS, {"i": i, "sels": TARGETS.get(i, {})})
        rects = {k: v for k, v in res.items() if k != "frame"}
        manifest[i]["rects"] = rects
        print(f"frame {i} {res['frame']}:")
        for k, v in rects.items(): print(f"   {k}: {v}")
    b.close()

json.dump(manifest, open("/home/attila/Documents/Projects/moldguard-promo-site/videos/manifest.json", "w"), indent=1)
print("manifest updated")
