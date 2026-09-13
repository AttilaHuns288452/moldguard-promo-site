#!/usr/bin/env python3
"""MoldGuard promo wireframes -> single import-safe HTML for Figma (html.to.design).

Reads index/features/how-it-works/contact.html + wireframe.css, emits
figma/MoldGuard_All_4.html: 4 desktop frames (1280px), shared inlined CSS,
review chrome stripped (1 site nav per frame), amber notes kept.
Import-safe: no var(), no absolute/fixed/transform, no rgba, no <use>, no external CSS.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "figma" / "MoldGuard_All_4.html"

# literal replacements for wireframe.css :root vars (import-safe: no var())
VARS = {
    "--ink": "#1c1c1c", "--ink-2": "#565656", "--ink-3": "#8f8f8f",
    "--line": "#d6d6d6", "--fill": "#f4f4f4", "--fill-2": "#eaeaea",
    "--accent": "#2563eb", "--accent-ink": "#1d4ed8",
    "--note": "#8a5a00", "--note-bg": "#fff7e0", "--note-line": "#e3b341",
}

PAGES = [("01 · Landing", "index.html"), ("02 · Features", "features.html"),
         ("03 · How it works", "how-it-works.html"), ("04 · Contact / Get started", "contact.html")]

def build_css() -> str:
    css = (ROOT / "wireframe.css").read_text()
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)  # strip comments
    css = re.sub(r":root\s*\{[^}]*\}", "", css)  # drop :root block
    for var, val in VARS.items():
        css = css.replace(f"var({var})", val)
    assert "var(" not in css, "unreplaced var() remains"
    for banned in ["absolute", "fixed", "rgba", "<use"]:
        assert banned not in css, f"banned '{banned}' in css"
    assert not re.search(r"(?<!text-)transform\s*:", css), "banned 'transform:' in css"
    # board + frame + label chrome (normal flow only, no absolute/transform)
    css += """
.board{background:#e8e8e8;padding:32px;display:flex;flex-direction:column;gap:32px;align-items:center;}
.frame-label{width:1280px;max-width:100%;font-family:ui-sans-serif,system-ui,Arial,sans-serif;font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#6b6b6b;}
.frame{width:1280px;max-width:100%;background:#fff;border:1px solid #d6d6d6;overflow:hidden;}
.frame .page{max-width:1080px;}
"""
    return css

def build_frame_body(src: str) -> str:
    """Extract <body> inner HTML, strip review chrome + inter-page links."""
    m = re.search(r"<body>(.*)</body>", src, flags=re.S)
    body = m.group(1)
    # drop review pagelabel + pagenav blocks (first .page div containing wf-pagelabel)
    body = re.sub(r'<div class="page">\s*<div class="wf-pagelabel">.*?</nav></div>', "", body, flags=re.S)
    body = body.replace('href="index.html"', 'href="#"').replace('href="features.html"', 'href="#"')
    body = body.replace('href="how-it-works.html"', 'href="#"').replace('href="contact.html"', 'href="#"')
    body = re.sub(r'style="([^"]*)var\(--ink\)([^"]*)"', r'style="\1#1c1c1c\2"', body)
    body = re.sub(r'style="([^"]*)var\(--ink-3\)([^"]*)"', r'style="\1#8f8f8f\2"', body)
    body = re.sub(r'style="([^"]*)var\(--fill\)([^"]*)"', r'style="\1#f4f4f4\2"', body)
    assert "var(" not in body, "unreplaced var() in body"
    assert "wireframe.css" not in body
    return body.strip()

def main() -> None:
    css = build_css()
    frames = []
    for label, fname in PAGES:
        body = build_frame_body((ROOT / fname).read_text())
        frames.append(f'<div class="frame-label">{label}</div>\n<div class="frame">\n{body}\n</div>')
    assert len(frames) == 4, f"expected 4 frames, got {len(frames)}"
    html = ("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=1280\">\n"
            "<title>MoldGuard promo wireframes · Figma import (4 frames)</title>\n"
            f"<style>\n{css}\n</style>\n</head>\n<body>\n<div class=\"board\">\n"
            + "\n".join(frames) + "\n</div>\n</body>\n</html>\n")
    for banned in ["position:absolute", "position:fixed", "rgba(", "<use", "var("]:
        assert banned not in html, f"banned '{banned}' in output"
    assert not re.search(r"(?<!text-)transform:", html), "banned 'transform:' in output"
    assert html.count('class="frame"') == 4
    assert css.count("{") == css.count("}"), "brace mismatch in css"
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(html)
    print(f"wrote {OUT} ({len(html)//1024}KB, 4 frames)")

if __name__ == "__main__":
    main()
