#!/usr/bin/env python3
"""Generate the download QR code (REAL, scannable) for download.html.

Destination: APP_DOWNLOAD_URL below. No published app-store listing exists yet,
so the code resolves to the MoldGuard site (smart-link placeholder). When store
listings go live, point APP_DOWNLOAD_URL at a router/smart-link (or the Play
listing) and regenerate — this file is the single place to change.

Verify after any change: python3 -m venv /tmp/qrvenv && /tmp/qrvenv/bin/pip install qrcode[pil] zxing-cpp
  /tmp/qrvenv/bin/python generate_qr.py   (self-check decodes the PNG and asserts the payload)
"""
import qrcode

APP_DOWNLOAD_URL = "https://attilahuns288452.github.io/moldguard-promo-site/download.html"
OUT_SVG = "download-qr.svg"
OUT_PNG = "/tmp/qr-check.png"          # scratch raster used only for the decode self-check
FILL = "#22334a"                        # brand deep navy
BACK = "#ffffff"


def main() -> None:
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q, border=4, box_size=10)
    qr.add_data(APP_DOWNLOAD_URL)
    qr.make(fit=True)
    matrix = qr.get_matrix()
    n = len(matrix)
    quiet = 4
    total = (n + quiet * 2) * 8

    rects = [
        f'<rect x="{(x + quiet) * 8}" y="{(y + quiet) * 8}" width="8" height="8"/>'
        for y, row in enumerate(matrix) for x, on in enumerate(row) if on
    ]
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total} {total}" '
        f'role="img" aria-label="QR code linking to the MoldGuard app download page">\n'
        f'<rect width="{total}" height="{total}" fill="{BACK}"/>\n'
        f'<g fill="{FILL}">\n' + "\n".join(rects) + f"\n</g>\n</svg>\n"
    )
    with open(OUT_SVG, "w") as f:
        f.write(svg)

    # self-check: same matrix rasterized to PNG, decoded back, payload asserted
    try:
        from PIL import Image
        import zxingcpp
    except ImportError:
        print(f"wrote {OUT_SVG} ({n}x{n} modules, payload {APP_DOWNLOAD_URL}) — decode check skipped (pip install qrcode[pil] zxing-cpp)")
        return
    img = qr.make_image(fill_color=FILL, back_color=BACK).convert("RGB")
    img.save(OUT_PNG)
    results = zxingcpp.read_barcodes(Image.open(OUT_PNG))
    assert results, "decode failed"
    assert results[0].text == APP_DOWNLOAD_URL, f"payload mismatch: {results[0].text}"
    print(f"wrote {OUT_SVG} ({n}x{n} modules) — decode-verified: {results[0].text}")


if __name__ == "__main__":
    main()
