"""Generate social preview thumbnail for Humanize US.

No fonts are bundled. The script uses common system fonts when available.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent.parent / "assets" / "social-preview.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
]
BOLD_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf",
]


def font(size: int, bold: bool = False):
    candidates = BOLD_CANDIDATES if bold else FONT_CANDIDATES
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


W, H = 1280, 640
BG = (246, 242, 235)
INK = (28, 28, 28)
MUTED = (104, 100, 96)
DIVIDER = (220, 211, 198)
BAD = (184, 73, 58)
GOOD = (42, 101, 77)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
PAD = 72

# Header
d.text((PAD, 58), "Humanize US", font=font(76, True), fill=INK)
subtitle = "natural American English, same meaning"
d.text((PAD, 138), subtitle, font=font(28), fill=MUTED)
d.line([(PAD, 190), (W - PAD, 190)], fill=DIVIDER, width=2)

# Labels
d.text((PAD, 230), "BEFORE  (AI-sounding)", font=font(19, True), fill=BAD)
d.text((W // 2 + 50, 230), "AFTER  (edited US English)", font=font(19, True), fill=GOOD)

rows = [
    ("It is important to note that AI can leverage data.", "AI can use data."),
    ("This post will delve into a wide range of benefits.", "This post explains the benefits."),
    ("First, it is robust. Second, it is seamless.", "It is reliable and easy to use."),
]

y = 270
for before, after in rows:
    d.text((PAD, y), before, font=font(29), fill=INK)
    # strike approximate line
    bbox = d.textbbox((PAD, y), before, font=font(29))
    d.line([(bbox[0], (bbox[1]+bbox[3])//2+2), (bbox[2], (bbox[1]+bbox[3])//2+2)], fill=BAD, width=3)
    d.text((W // 2 - 35, y - 2), "→", font=font(38, True), fill=MUTED)
    d.text((W // 2 + 50, y), after, font=font(29, True), fill=GOOD)
    y += 74

# Stats
d.line([(PAD, 490), (W - PAD, 490)], fill=DIVIDER, width=1)
d.text((PAD, 520), "10 categories", font=font(30, True), fill=INK)
d.text((PAD + 260, 520), "50+ patterns", font=font(30, True), fill=INK)
d.text((PAD + 510, 520), "fidelity audit", font=font(30, True), fill=INK)
d.text((PAD + 790, 520), "not detector-bypass", font=font(30, True), fill=BAD)

d.text((W - PAD - 330, H - 48), "github-ready Claude Code skill", font=font(22), fill=MUTED)

img.save(OUT, "PNG", optimize=True)
print(f"saved: {OUT}")
