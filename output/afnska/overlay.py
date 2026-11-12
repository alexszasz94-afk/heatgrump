"""afnska: pune textul original (acelasi text, acelasi loc, aceleasi secunde) + sunetul original peste videoul generat.
Folosire: python3 overlay.py spec.json
spec: {"video": "...", "audio": "...", "out": "...", "y": 0.12, "texts": [{"t": "Winter coats in 1955 \U0001F92E", "from": 0, "to": 2}, ...]}
"""
import json, os, subprocess, sys, tempfile, unicodedata
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
EMOJI_DIR = os.path.join(REPO, "heatgrump-studio/engine/fonts/apple-emoji")
FONT = "/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf"   # aproape de fontul "Classic" din Instagram
W, H = 1080, 1920
SIZE = 61


def is_emoji(ch):
    return ord(ch) >= 0x2190 and (unicodedata.category(ch) in ("So", "Sk") or ord(ch) >= 0x1F000)


def runs(text):
    out = []
    for ch in text:
        if ch in "️‍":
            continue
        if is_emoji(ch):
            out.append(("e", ch))
        elif out and out[-1][0] == "t":
            out[-1] = ("t", out[-1][1] + ch)
        else:
            out.append(("t", ch))
    return out


def text_png(text, path, y_center):
    font = ImageFont.truetype(FONT, SIZE)
    parts = runs(text)
    es = int(SIZE * 0.92)
    widths = [font.getlength(s) if k == "t" else es + 4 for k, s in parts]
    tw = int(sum(widths))
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x = (W - tw) // 2
    y = int(H * y_center - SIZE * 0.6)
    for (k, s), w in zip(parts, widths):
        if k == "t":
            d.text((x, y), s, font=font, fill="white")
        else:
            f = os.path.join(EMOJI_DIR, f"{ord(s):x}.png")
            if os.path.exists(f):
                im = Image.open(f).convert("RGBA").resize((es, es), Image.LANCZOS)
                layer.paste(im, (int(x) + 2, y + int(SIZE * 0.2)), im)
        x += w
    # umbra fina, ca la textul Instagram
    a = layer.split()[3].filter(ImageFilter.GaussianBlur(3))
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    shadow.putalpha(a.point(lambda v: int(v * 0.55)))
    out = Image.alpha_composite(shadow, layer)
    out.save(path)


def main(spec_path):
    sp = json.load(open(spec_path))
    tmp = tempfile.mkdtemp()
    inputs = ["-i", sp["video"], "-i", sp["audio"]]
    chain = f"[0:v]scale={W}:{H}:flags=lanczos,setsar=1[v0]"
    last = "v0"
    for i, t in enumerate(sp["texts"]):
        p = os.path.join(tmp, f"t{i}.png")
        text_png(t["t"], p, sp.get("y", 0.12))
        inputs += ["-i", p]
        chain += f";[{last}][{i + 2}:v]overlay=0:0:enable='between(t,{t['from']},{t['to']})'[v{i + 1}]"
        last = f"v{i + 1}"
    cmd = ["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", chain, "-map", f"[{last}]", "-map", "1:a",
           "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
           "-shortest", sp["out"]]
    subprocess.run(cmd, check=True)
    print(sp["out"])


if __name__ == "__main__":
    main(sys.argv[1])
