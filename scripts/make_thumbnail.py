"""Generate the social preview thumbnail for Humanize US.

The layout mirrors the original im-not-ai social card: a big wordmark, a
two-column BEFORE/AFTER table with strikethroughs and arrows, and a stats
strip across the bottom.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent.parent / "assets" / "social-preview.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

REGULAR_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
]
BOLD_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf",
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = BOLD_CANDIDATES if bold else REGULAR_CANDIDATES
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


W, H = 1280, 640
BG = (246, 242, 235)
INK = (28, 28, 28)
MUTED = (104, 100, 96)
DIVIDER = (210, 200, 186)
BAD = (184, 73, 58)
GOOD = (42, 101, 77)
GOOD_BG = (224, 232, 222)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

PAD = 72
COL_GAP_CENTER = 640
ARROW_X = 600
AFTER_X = 690


# ---------- header ----------
title_font = font(96, bold=True)
d.text((PAD, 40), "Humanize US", font=title_font, fill=INK)

subtitle = "natural American English, same meaning"
sub_font = font(26)
sub_w = d.textlength(subtitle, font=sub_font)
d.text((W - PAD - sub_w, 110), subtitle, font=sub_font, fill=MUTED)

d.line([(PAD, 188), (W - PAD, 188)], fill=DIVIDER, width=2)


# ---------- column labels ----------
label_font = font(20, bold=True)
d.text((PAD, 220), "BEFORE", font=label_font, fill=BAD)
d.text((PAD + 96, 220), "(AI-sounding)", font=label_font, fill=MUTED)

d.text((AFTER_X, 220), "AFTER", font=label_font, fill=GOOD)
d.text((AFTER_X + 86, 220), "(edited US English)", font=label_font, fill=MUTED)


# ---------- before / after rows ----------
rows = [
    ("It is important to note this.", "Note this."),
    ("We delve into the nuances.", "Here are the details."),
    ("A robust and seamless tool.", "Reliable and easy to use."),
]

row_font = font(30)
row_font_bold = font(30, bold=True)
arrow_font = font(36, bold=True)

y = 282
for before, after in rows:
    d.text((PAD, y), before, font=row_font, fill=INK)
    bbox = d.textbbox((PAD, y), before, font=row_font)
    mid = (bbox[1] + bbox[3]) // 2 + 2
    d.line([(bbox[0], mid), (bbox[2], mid)], fill=BAD, width=3)

    d.text((ARROW_X, y - 4), "→", font=arrow_font, fill=MUTED)

    d.text((AFTER_X, y), after, font=row_font_bold, fill=GOOD)
    y += 64


# ---------- stats strip ----------
d.line([(PAD, 482), (W - PAD, 482)], fill=DIVIDER, width=2)


# big "10 → 50+" headline-stat block, echoing the inspiration's score
big_font = font(64, bold=True)
small_label = font(18)

d.text((PAD, 514), "10", font=big_font, fill=INK)
ten_w = d.textlength("10", font=big_font)
d.text((PAD, 588), "categories", font=small_label, fill=MUTED)

d.text((PAD + ten_w + 24, 528), "→", font=arrow_font, fill=MUTED)

mid_x = PAD + ten_w + 24 + 60
d.text((mid_x, 514), "50+", font=big_font, fill=INK)
fifty_w = d.textlength("50+", font=big_font)
d.text((mid_x, 588), "patterns", font=small_label, fill=MUTED)


# A+ pill badge
pill_x = mid_x + fifty_w + 36
pill_y = 528
pill_text = "A+"
pill_font = font(34, bold=True)
pill_w = d.textlength(pill_text, font=pill_font) + 36
pill_h = 60
d.rounded_rectangle(
    [(pill_x, pill_y), (pill_x + pill_w, pill_y + pill_h)],
    radius=12,
    fill=GOOD,
)
d.text((pill_x + 18, pill_y + 8), pill_text, font=pill_font, fill=BG)


# fidelity-first tag next to the pill
tag_font = font(22, bold=True)
d.text(
    (pill_x + pill_w + 20, pill_y + 6),
    "fidelity-first",
    font=tag_font,
    fill=INK,
)
d.text(
    (pill_x + pill_w + 20, pill_y + 34),
    "no detector-bypass claims",
    font=font(18),
    fill=MUTED,
)


# bottom-right URL
url = "github.com/flrngel/im-not-ai-en-us"
url_font = font(20)
url_w = d.textlength(url, font=url_font)
d.text((W - PAD - url_w, H - 40), url, font=url_font, fill=MUTED)


img.save(OUT, "PNG", optimize=True)
print(f"saved: {OUT}")
