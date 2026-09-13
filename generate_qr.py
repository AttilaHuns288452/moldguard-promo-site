#!/usr/bin/env python3
"""Generate the placeholder (fake, non-scannable) QR code SVG for download.html.

Deterministic: same seed -> same SVG. Visually a plausible QR (finder patterns,
timing lines, module noise) but encodes nothing. Replace with a real app-store
QR before launch.
"""
import zlib

W = 29  # modules per side
SCALE = 8
QUIET = 2
TOTAL = (W + QUIET * 2) * SCALE
SEED = b"MOLDGUARD-V1-FAKE-QR-NOT-SCANNABLE"


def rng_byte(i: int) -> int:
    return zlib.crc32(SEED + i.to_bytes(4, "big")) & 0xFF


def in_finder(x: int, y: int) -> bool:
    for fx, fy in ((0, 0), (W - 7, 0), (0, W - 7)):
        if fx <= x < fx + 7 and fy <= y < fy + 7:
            lx, ly = x - fx, y - fy
            return lx in (0, 6) or ly in (0, 6) or (2 <= lx <= 4 and 2 <= ly <= 4)
    return False


def is_timing(x: int, y: int) -> bool:
    return x == 6 or y == 6


def main() -> None:
    rects = []
    n_modules = W * W
    for y in range(W):
        for x in range(W):
            if is_timing(x, y):
                on = (x % 2 == 0) if y == 6 else (y % 2 == 0)
            elif in_finder(x, y):
                on = True
            else:
                on = rng_byte(y * W + x) < 116  # ~45% fill
            if on:
                rects.append(
                    f'<rect x="{(x + QUIET) * SCALE}" y="{(y + QUIET) * SCALE}" '
                    f'width="{SCALE}" height="{SCALE}"/>'
                )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {TOTAL} {TOTAL}" '
        f'role="img" aria-label="Placeholder QR code (not scannable)">\n'
        f'<rect width="{TOTAL}" height="{TOTAL}" fill="#ffffff"/>\n'
        f'<g fill="#22334a">\n' + "\n".join(rects) + "\n</g>\n</svg>\n"
    )
    with open("download-qr.svg", "w") as f:
        f.write(svg)
    print(f"wrote download-qr.svg  viewBox 0 0 {TOTAL} {TOTAL}  modules {n_modules}")


if __name__ == "__main__":
    main()
