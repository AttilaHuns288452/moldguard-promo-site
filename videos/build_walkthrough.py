#!/usr/bin/env python3
"""
MoldGuard — Figma-frame walkthrough video (1920x1080, ~55.5s + fades).
Source: figma/MoldGuard_All_4.html renders (frame_0..4.png @2x) + manifest rects.
Pipeline: PIL compose per frame -> stdin pipe -> ffmpeg (video+audio one pass).
Modes: preview (still JPGs for vision check) | render (full MP4).
"""
import asyncio, json, subprocess, sys, time
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

BASE = Path("/home/attila/Documents/Projects/moldguard-promo-site/videos")
W, H = 1920, 1080
BASE_W = 1160           # on-canvas width of a page at scale 1.0
IMG_W = 2240            # all page images normalized to this width
FPS = 30
FADE = 0.5
TEAL = (45, 154, 145)
DARKC = (18, 44, 51)

FONT_DIR = Path.home() / ".local/share/fonts"
def font(name, size, weight=None):
    f = ImageFont.truetype(str(FONT_DIR / name), size)
    if weight:
        try: f.set_variation_by_name(weight)
        except Exception: pass
    return f

manifest = json.load(open(BASE / "manifest.json"))
IMGS = [Image.open(BASE / f"frame_{i}.png").convert("RGB") for i in range(5)]

def rect_center(img, name):
    r = manifest[img]["rects"][name]
    return (r[0] + r[2] / 2, r[1] + r[3] / 2)

def R(img, name):
    return manifest[img]["rects"][name]

# ---------------- outro card (pre-rendered, normalized to IMG_W) ----------------
def make_outro():
    img = Image.new("RGB", (W, H), (24, 59, 67))
    d = ImageDraw.Draw(img)
    d.text((960, 430), "MoldGuard", font=font("BricolageGrotesque[opsz,wdth,wght].ttf", 120, "Bold"),
           fill=(233, 241, 240), anchor="mm")
    d.rectangle([760, 540, 1160, 545], fill=TEAL)
    d.text((960, 620), "Know mold is coming before it shows.",
           font=font("Figtree[wght].ttf", 42, "SemiBold"), fill=(166, 189, 186), anchor="mm")
    d.text((960, 740), "moldguard.dev.team@gmail.com  ·  0992 543 0608",
           font=font("SplineSansMono[wght].ttf", 24), fill=(143, 208, 204), anchor="mm")
    d.text((960, 810), "IoT MOLD RISK PREVENTION & DETECTION",
           font=font("SplineSansMono[wght].ttf", 18), fill=(120, 150, 150), anchor="mm")
    return img.resize((IMG_W, int(IMG_W * H / W)), Image.LANCZOS)  # 2240x1260

OUTRO = make_outro()
ALL_IMGS = IMGS + [OUTRO]
OUTRO_IDX = 5

# ---------------- scenes ----------------
# kf = (u, img, scale, cx, cy, darken, hl)   cx,cy in CSS px (img_width/2 = 1120 center)
C = lambda img, name: rect_center(img, name)
SCENES = [
    dict(t0=0.0, dur=5.0, label="IoT mold risk prevention", kfs=[
        (0.0, OUTRO_IDX, 1.655, 560, 315, 0.0, None),
        (1.0, 0, 1.00, 560, 540, 0.0, None)]),
    dict(t0=5.0, dur=6.0, label="The problem", kfs=[
        (0.0, 0, 1.00, 560, 540, 0.0, None),
        (0.35, 0, 1.45, *C(0, "problist"), 0.55, (0, "problist")),
        (1.0, 0, 1.45, *C(0, "problist"), 0.55, (0, "problist"))]),
    dict(t0=11.0, dur=6.5, label="Meet MoldGuard", kfs=[
        (0.0, 0, 1.00, 560, 540, 0.0, None),
        (0.35, 0, 1.40, *C(0, "meetwrap"), 0.50, (0, "meetwrap")),
        (1.0, 0, 1.40, *C(0, "meetwrap"), 0.50, (0, "meetwrap"))]),
    dict(t0=17.5, dur=7.0, label="Sense · Score · Act", kfs=[
        (0.0, 0, 1.00, 560, 540, 0.0, None),
        (0.30, 0, 1.55, *C(0, "flowsvg"), 0.50, (0, "flowsvg")),
        (1.0, 0, 1.55, *C(0, "flowsvg"), 0.50, (0, "flowsvg"))]),
    dict(t0=24.5, dur=7.0, label="Live dashboard", kfs=[
        (0.0, 1, 1.00, 560, 540, 0.0, None),
        (0.30, 1, 1.40, *C(1, "duo"), 0.50, (1, "duo")),
        (0.55, 1, 1.40, *C(1, "duo"), 0.50, (1, "duo")),
        (0.75, 1, 1.90, *C(1, "dial"), 0.55, (1, "dial")),
        (1.0, 1, 1.90, *C(1, "dial"), 0.55, (1, "dial"))]),
    dict(t0=31.5, dur=6.0, label="Built for mold", kfs=[
        (0.0, 1, 1.00, 560, 540, 0.0, None),
        (0.35, 1, 1.50, *C(1, "compare"), 0.50, (1, "compare")),
        (1.0, 1, 1.50, *C(1, "compare"), 0.50, (1, "compare"))]),
    dict(t0=37.5, dur=7.0, label="Set up in minutes", kfs=[
        (0.0, 2, 1.00, 560, 540, 0.0, None),
        (0.28, 2, 1.50, *C(2, "loopline"), 0.50, (2, "loopline")),
        (0.50, 2, 1.50, *C(2, "loopline"), 0.50, (2, "loopline")),
        (0.68, 2, 1.60, *C(2, "herostage"), 0.50, (2, "herostage")),
        (1.0, 2, 1.60, *C(2, "herostage"), 0.50, (2, "herostage"))]),
    dict(t0=44.5, dur=5.5, label="Get in touch", kfs=[
        (0.0, 3, 1.00, 560, 540, 0.0, None),
        (0.35, 3, 1.60, *C(3, "formcard"), 0.50, (3, "formcard")),
        (1.0, 3, 1.60, *C(3, "formcard"), 0.50, (3, "formcard"))]),
    dict(t0=50.0, dur=7.5, label="Get the app", kfs=[
        (0.0, 4, 1.00, 560, 540, 0.0, None),
        (0.30, 4, 2.00, *C(4, "qr"), 0.65, (4, "qr")),
        (0.55, 4, 2.00, *C(4, "qr"), 0.65, (4, "qr")),
        (0.70, 4, 1.00, 560, 460, 0.0, None),
        (0.75, OUTRO_IDX, 1.655, 560, 315, 0.0, None),
        (1.0, OUTRO_IDX, 1.655, 560, 315, 0.0, None)]),
]
TOTAL = SCENES[-1]["t0"] + SCENES[-1]["dur"]  # 55.5

# ---------------- background gradient ----------------
BG_BIG = Image.new("RGB", (4200, 2400))
_bd = ImageDraw.Draw(BG_BIG)
for y in range(2400):
    t = y / 2400
    r = int(251 + (226 - 251) * t); g = int(251 + (238 - 251) * t); b = int(249 + (236 - 249) * t)
    teal = max(0.0, 1 - abs(t - 0.5) * 2) * 0.05
    _bd.line([(0, y), (4200, y)], fill=(int(r * (1 - teal) + 224 * teal),
                                        int(g * (1 - teal) + 242 * teal),
                                        int(b * (1 - teal) + 248 * teal)))

def ease(u):
    u = min(1.0, max(0.0, u))
    return 4 * u * u * u if u < 0.5 else 1 - pow(-2 * u + 2, 3) / 2

def kf_state(kf_a, kf_b, e):
    """Lerped state between two keyframes; if img changes, both states + blend factor."""
    a, b = kf_a, kf_b
    if a[1] != b[1]:
        return dict(img=b[1], scale=b[2], cx=b[3], cy=b[4], darken=b[5], hl=b[6],
                    img_a=a[1], s_a=a[2:6], hl_a=a[6], blend=e)
    return dict(img=b[1],
                scale=a[2] + (b[2] - a[2]) * e,
                cx=a[3] + (b[3] - a[3]) * e,
                cy=a[4] + (b[4] - a[4]) * e,
                darken=a[5] + (b[5] - a[5]) * e,
                hl=b[6] if (b[6] and e > 0.5) else (a[6] if (a[6] and e <= 0.5) else
                    (b[6] if b[6] and a[6] == b[6] else (b[6] or a[6]))))

def scene_state(scene, t):
    u = min(1.0, max(0.0, (t - scene["t0"]) / scene["dur"]))
    kfs = scene["kfs"]
    for i in range(len(kfs) - 1):
        if kfs[i][0] <= u <= kfs[i + 1][0]:
            span = kfs[i + 1][0] - kfs[i][0] or 1
            return kf_state(kfs[i], kfs[i + 1], ease((u - kfs[i][0]) / span))
    return kf_state(kfs[-1], kfs[-1], 0)

def render_state(img_idx, scale, cx, cy, darken, hl):
    k = (BASE_W * scale) / ALL_IMGS[img_idx].width
    src_cx, src_cy = cx * 2, cy * 2
    win_w, win_h = W / k, H / k
    wx0, wy0 = src_cx - win_w / 2, src_cy - win_h / 2
    bgx0 = 2100 - win_w / 2; bgy0 = 1200 - win_h / 2
    canvas = BG_BIG.crop((int(bgx0), int(bgy0), int(bgx0 + win_w), int(bgy0 + win_h)))
    page_w, page_h = ALL_IMGS[img_idx].width, ALL_IMGS[img_idx].height
    sx0, sy0 = max(0, int(wx0)), max(0, int(wy0))
    sx1, sy1 = min(page_w, int(wx0 + win_w)), min(page_h, int(wy0 + win_h))
    if sx1 > sx0 and sy1 > sy0:
        canvas.paste(ALL_IMGS[img_idx].crop((sx0, sy0, sx1, sy1)),
                     (sx0 - int(wx0), sy0 - int(wy0)))
    frame = canvas.resize((W, H), Image.LANCZOS)

    px0 = 960 - src_cx * k; py0 = 540 - src_cy * k
    pw, ph = page_w * k, page_h * k
    rad = max(2, int(36 * k))
    d = ImageDraw.Draw(frame, "RGBA")
    d.rounded_rectangle([px0 - 1, py0 - 1, px0 + pw + 1, py0 + ph + 1], radius=rad,
                        outline=(120, 140, 140, 60), width=6)
    d.rounded_rectangle([px0, py0, px0 + pw, py0 + ph], radius=rad,
                        outline=(199, 212, 211, 255), width=2)

    if darken > 0.01 and hl:
        hl_img, hl_name = hl
        rx, ry, rw, rh = [v * 2 * k for v in R(hl_img, hl_name)]
        pad = int(10 * scale)
        hx0 = px0 + max(0, rx - pad); hy0 = py0 + max(0, ry - pad)
        hx1 = px0 + min(pw, rx + rw + pad); hy1 = py0 + min(ph, ry + rh + pad)
        hr = max(4, int(28 * k))
        ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(ov).rounded_rectangle([px0, py0, px0 + pw, py0 + ph], radius=rad,
                                             fill=DARKC + (int(150 * darken),))
        hole = Image.new("L", (W, H), 0)
        ImageDraw.Draw(hole).rounded_rectangle([hx0, hy0, hx1, hy1], radius=hr, fill=255)
        hole = hole.filter(ImageFilter.GaussianBlur(2))
        alpha = ov.split()[3]
        ov.putalpha(ImageChops.multiply(alpha, hole.point(lambda v: 255 - v)))
        frame.paste(ov, (0, 0), ov)
        d.rounded_rectangle([hx0, hy0, hx1, hy1], radius=hr, outline=TEAL + (200,),
                            width=max(2, int(2 * scale)))
        d.rounded_rectangle([hx0 + 3, hy0 + 3, hx1 - 3, hy1 - 3], radius=max(2, hr - 2),
                            outline=(255, 255, 255, 80), width=1)
    return frame

def render_dict(st):
    if "blend" not in st:
        return render_state(st["img"], st["scale"], st["cx"], st["cy"], st["darken"], st["hl"])
    a = render_state(st["img_a"], *st["s_a"], st["hl_a"])
    b = render_state(st["img"], st["scale"], st["cx"], st["cy"], st["darken"], st["hl"])
    return Image.blend(a, b, st["blend"])

def label_frame(frame, t, label):
    d = ImageDraw.Draw(frame, "RGBA")
    d.rectangle([0, H - 3, int(W * (t / TOTAL)), H], fill=TEAL + (220,))
    f = font("SplineSansMono[wght].ttf", 15)
    txt = f"MoldGuard  ·  {label}"
    bb = d.textbbox((0, 0), txt, font=f)
    pw_, ph_ = bb[2] - bb[0] + 28, 30
    x0, y0 = (W - pw_) // 2, H - 24 - ph_
    d.rounded_rectangle([x0, y0, x0 + pw_, y0 + ph_], radius=15, fill=(18, 44, 51, 205))
    d.text((x0 + 14, y0 + 6), txt, fill=(233, 241, 240, 235), font=f)
    return frame

def active_scene(t):
    for s in SCENES:
        if s["t0"] <= t < s["t0"] + s["dur"]:
            return s
    return SCENES[-1]

def compose(t):
    s = active_scene(t)
    st = scene_state(s, t)
    frame = render_dict(st)
    label_frame(frame, t, s["label"])
    if s["t0"] > 0 and t - s["t0"] < FADE:
        prev = SCENES[SCENES.index(s) - 1]
        pst = scene_state(prev, prev["t0"] + prev["dur"])
        pf = render_dict(pst)
        label_frame(pf, t, prev["label"])
        frame = Image.blend(pf, frame, ease((t - s["t0"]) / FADE))
    if t < 0.5:
        frame = Image.eval(frame, lambda v: int(v * (t / 0.5)))
    if t > TOTAL - 0.6:
        frame = Image.eval(frame, lambda v: int(v * max(0.0, (TOTAL - t) / 0.6)))
    return frame

# ---------------- narration ----------------
LINES = [
    (0,   0.40, "Meet MoldGuard — it knows mold is coming, before it shows."),
    (1,   5.30, "Mold grows silently for weeks before you ever see it."),
    (2,  11.30, "Humidity, temperature, and air quality become one number: the Mold Risk Index."),
    (3,  17.80, "Sense. Score. Act. The dehumidifier runs before mold ever starts."),
    (4,  24.80, "The dashboard scores every room in real time, and flags elevated risk automatically."),
    (5,  31.80, "Unlike a simple humidity trigger, MoldGuard is built for mold — end to end."),
    (6,  37.80, "Plug it in, connect to Wi-Fi, and watch every room from your phone."),
    (7,  44.80, "Want one? Leave a message, and the team will set you up."),
    (8,  50.30, "Scan to get the app — and protect your space before mold appears."),
]

def gen_narrations():
    import edge_tts
    out = []
    for i, (scene, start, text) in enumerate(LINES):
        span = SCENES[scene]["dur"]
        rate = "+0%"
        path = BASE / f"narr_{i}.mp3"
        for attempt in range(4):
            async def go():
                c = edge_tts.Communicate(text, "en-US-AriaNeural", rate=rate)
                await c.save(str(path))
            asyncio.run(go())
            dur = float(subprocess.run(
                ["ffprobe", "-v", "error", "-show_entries", "format=duration",
                 "-of", "default=nw=1:nk=1", str(path)],
                capture_output=True, text=True).stdout.strip())
            print(f"  narr {i} rate={rate} dur={dur:.2f}s (budget {span - 0.9:.1f}s)")
            if dur <= span - 0.9:
                break
            rate = f"+{8 * (attempt + 1)}%"
        out.append((start, path))
    return out

def build_audio_filter(narrs, bgm):
    inputs = ["-i", str(bgm)]
    for _, p in narrs:
        inputs += ["-i", str(p)]
    fc = [f"[1:a]volume=0.07,atrim=0:{TOTAL},asetpts=PTS-STARTPTS[bg]"]
    for n, (start, _) in enumerate(narrs):
        fc.append(f"[{n + 2}:a]adelay={int(start * 1000)}:all=1[n{n}]")
    fc.append("[bg]" + "".join(f"[n{n}]" for n in range(len(narrs))) +
              f"amix=inputs={len(narrs) + 1}:normalize=0:duration=longest[aout]")
    return inputs, ";".join(fc)

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "preview"
    if mode == "preview":
        times = [0.3, TOTAL - 0.3] + [s["t0"] + s["dur"] * f for s in SCENES for f in (0.5,)]
        for t in times:
            compose(t).save(BASE / f"preview_{t:.1f}.jpg", quality=88)
            print("preview", round(t, 1))
        return

    bgm = Path.home() / "Documents/Projects/dental-practice-management/videos/bgm_full.m4a"
    narrs = gen_narrations()
    inputs, fc = build_audio_filter(narrs, bgm)
    out = BASE / "MoldGuard-Demo-Walkthrough.mp4"
    cmd = (["ffmpeg", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
            "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-"] + inputs +
           ["-filter_complex", fc, "-map", "0:v", "-map", "[aout]",
            "-c:v", "libx264", "-preset", "medium", "-crf", "18",
            "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
            "-t", str(TOTAL), "-movflags", "+faststart", str(out)])
    print("encoding:", out.name)
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE,
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    t0 = time.time()
    n_frames = int(TOTAL * FPS)
    for i in range(n_frames):
        proc.stdin.write(compose(i / FPS).tobytes())
        if i % 300 == 0:
            print(f"  frame {i}/{n_frames}  {time.time() - t0:.0f}s")
    proc.stdin.close()
    proc.wait()
    print(f"done {out} exists={out.exists()} size={out.stat().st_size if out.exists() else 0} render={time.time()-t0:.0f}s")

if __name__ == "__main__":
    main()
