#!/usr/bin/env python3
"""Regenerate figma/MoldGuard_All_4.html from current pages (import-safe for html.to.design).

Per frame: <body> inner, review chrome stripped, site.css inlined with :root vars
flattened, photos base64-inlined, animation/transition/sticky/backdrop removed.
"""
import base64, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "figma" / "MoldGuard_All_4.html"
PAGES = [("01 · Landing", "index.html"), ("02 · Features", "features.html"),
         ("03 · How it works", "how-it-works.html"), ("04 · Contact / Get started", "contact.html"),
         ("05 · Download", "download.html")]

css = (ROOT / "site.css").read_text()
css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)                     # comments first (kills commented var() strays)
root_vars = dict(re.findall(r"(--[\w-]+)\s*:\s*([^;}]+)", re.search(r":root\s*\{([^}]*)\}", css).group(1)))
css = re.sub(r":root\s*\{[^}]*\}", "", css)
for name, val in root_vars.items():
    css = css.replace(f"var({name})", val.strip())
css = re.sub(r"@keyframes[^{]+\{(?:[^{}]*\{[^}]*\})*[^}]*\}", "", css)  # keyframes incl. nested blocks
for pat in [r"animation[^;]*;", r"transition[^;]*;", r"backdrop-filter[^;]*;",
            r"scroll-behavior[^;]*;", r"prefers-reduced-motion[^{]*\{\s*\}"]:
    css = re.sub(pat, "", css)
css = css.replace("position: sticky", "position: static").replace("position:sticky", "position:static")
css = re.sub(r"\n\s*\n+", "\n", css)
assert "var(" not in css, "unreplaced var() in css"
assert "@keyframes" not in css and "animation" not in css and "transition" not in css
assert "sticky" not in css
assert css.count("{") == css.count("}"), "brace mismatch"

def frame_body(fname: str) -> str:
    src = (ROOT / fname).read_text()
    body = re.search(r"<body[^>]*>(.*)</body>", src, flags=re.S).group(1)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)              # direction contract + review notes
    body = re.sub(r'<div class="page">\s*<div class="wf-pagelabel">.*?</nav></div>', "", body, flags=re.S)
    for name, val in root_vars.items():
        body = body.replace(f"var({name})", val.strip())
    def img_data(m):
        path = ROOT / m.group(1)
        mime = "image/svg+xml" if path.suffix == ".svg" else "image/jpeg" if path.suffix == ".jpg" else "image/png"
        data = path.read_bytes()
        return f"data:{mime};base64,{base64.b64encode(data).decode()}"
    body = re.sub(r'(assets/[\w-]+\.(?:jpg|png|svg)|download-qr\.svg)', img_data, body)
    body = body.replace('href="index.html"', 'href="#"').replace('href="features.html"', 'href="#"')
    body = body.replace('href="how-it-works.html"', 'href="#"').replace('href="contact.html"', 'href="#"')
    body = body.replace('href="download.html"', 'href="#"')
    assert "var(" not in body, f"unreplaced var() in {fname}"
    return body.strip()

frames = []
for label, fname in PAGES:
    # index.html scopes page overrides via <body class="page-index"> — carry the class onto its frame
    frame_cls = "frame page-index" if fname == "index.html" else "frame"
    frames.append(f'<div class="frame-label">{label}</div>\n<div class="{frame_cls}">\n{frame_body(fname)}\n</div>')
assert len(frames) == 5

html = ("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=1280\">\n"
        "<title>MoldGuard promo site · Figma import (5 frames)</title>\n"
        "<link href=\"https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,650;12..96,700&family=Figtree:wght@400;500;600;700&family=Spline+Sans+Mono:wght@450;600&display=swap\" rel=\"stylesheet\">\n"
        "<style>\n* { box-sizing: border-box; margin: 0; padding: 0; }\n"
        "body { font-size: 16px; background: #e6e9ec; }\n"
        ".board { padding: 40px; display: flex; flex-direction: column; gap: 48px; align-items: center; }\n"
        ".frame-label { width: 1280px; max-width: 100%; font-size: 12px; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; color: #5b6b78; }\n"
        ".frame { width: 1280px; max-width: 100%; background: #fff; overflow: hidden; }\n"
        + css +
        "\n</style>\n</head>\n<body>\n<div class=\"board\">\n" + "\n".join(frames) + "\n</div>\n</body>\n</html>\n")

for banned in ["position:sticky", "position:fixed", "@keyframes", "animation:", "var(", "backdrop-filter"]:
    assert banned not in html, f"banned '{banned}' in output"
assert html.count('class="frame"') + html.count('class="frame page-index"') == 5
assert html.count("{") == html.count("}")
OUT.write_text(html)
print(f"wrote {OUT} ({len(html)//1024}KB, 5 frames, {len(root_vars)} tokens flattened)")
