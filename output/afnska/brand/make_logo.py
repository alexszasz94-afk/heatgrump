"""Frost Femme logo: fulg de zapada a carui raza de jos e un siret de corset + wordmark serif.
Folosire: python3 make_logo.py <folder_fonturi> <folder_iesire>
Fonturi: Cormorant-600.ttf (Cormorant Garamond, OFL) + Inter Medium (sistem).
"""
import math, os, sys
from PIL import Image, ImageDraw, ImageFont

FONTS, OUT = sys.argv[1], sys.argv[2]
SERIF = os.path.join(FONTS, "Cormorant-600.ttf")
SANS = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
IVORY, BURG, BLUE = (246, 243, 238), (110, 30, 46), (143, 166, 196)
S = 4096  # desenez mare, apoi micsorez (margini fine)


def emblem(d, cx, cy, r, col, w):
    def line(a, b):
        d.line([a, b], fill=col, width=w)
        for p in (a, b):
            d.ellipse([p[0] - w / 2, p[1] - w / 2, p[0] + w / 2, p[1] + w / 2], fill=col)
    # 5 raze de fulg (sus si diagonale); raza de jos devine siret de corset
    for deg in (90, 30, 150, 210, 330):
        a = math.radians(deg)
        end = (cx + r * math.cos(a), cy - r * math.sin(a))
        line((cx, cy), end)
        for frac, blen in ((0.55, 0.24), (0.8, 0.15)):
            bx, by = cx + r * frac * math.cos(a), cy - r * frac * math.sin(a)
            for side in (-1, 1):
                b = a + side * math.radians(42)
                line((bx, by), (bx + r * blen * math.cos(b), by - r * blen * math.sin(b)))
    # centru: romb mic
    k = r * 0.09
    d.polygon([(cx, cy - k), (cx + k, cy), (cx, cy + k), (cx - k, cy)], outline=col, width=w)
    # siretul (in jos)
    top, bot, gap, n = cy + r * 0.16, cy + r * 1.02, r * 0.17, 5
    ys = [top + i * (bot - top) / (n - 1) for i in range(n)]
    for i in range(n - 1):  # sireturi in X
        line((cx - gap, ys[i]), (cx + gap, ys[i + 1]))
        line((cx + gap, ys[i]), (cx - gap, ys[i + 1]))
    er = w * 1.5
    for y in ys:  # capse
        for x in (cx - gap, cx + gap):
            d.ellipse([x - er, y - er, x + er, y + er], fill=IVORY if col != IVORY else BURG, outline=col, width=max(2, int(w * 0.7)))
    # capetele siretului, usor in afara
    line((cx - gap, bot), (cx - gap * 1.6, bot + r * 0.22))
    line((cx + gap, bot), (cx + gap * 1.6, bot + r * 0.22))


def spaced(d, cx, y, text, font, track, col):
    widths = [font.getlength(c) for c in text]
    total = sum(widths) + track * (len(text) - 1)
    x = cx - total / 2
    for c, wd in zip(text, widths):
        d.text((x, y), c, font=font, fill=col)
        x += wd + track
    return total


def full_logo():
    im = Image.new("RGB", (S, S), IVORY)
    d = ImageDraw.Draw(im)
    emblem(d, S / 2, S * 0.33, S * 0.115, BURG, 22)
    f = ImageFont.truetype(SERIF, 400)
    tw = spaced(d, S / 2, S * 0.53, "FROST FEMME", f, 70, BURG)
    y = S * 0.53 + 470
    d.line([(S / 2 - tw * 0.18, y), (S / 2 + tw * 0.18, y)], fill=BLUE, width=8)
    spaced(d, S / 2, y + 70, "WINTER, WOMANLY.", ImageFont.truetype(SANS, 92), 34, BLUE)
    im.resize((2048, 2048), Image.LANCZOS).save(os.path.join(OUT, "frostfemme-logo.png"))


def icon():
    im = Image.new("RGB", (S, S), BURG)
    d = ImageDraw.Draw(im)
    emblem(d, S / 2, S * 0.40, S * 0.2, IVORY, 34)
    spaced(d, S / 2, S * 0.72, "FROST FEMME", ImageFont.truetype(SERIF, 250), 44, IVORY)
    im.resize((2048, 2048), Image.LANCZOS).save(os.path.join(OUT, "frostfemme-profile.png"))


full_logo(); icon()
print("ok")
