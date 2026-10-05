"""Montaj FINAL gata de postat: bucăți tăiate + texte pe ecran (cu emoji, stil Instagram) + muzică de Crăciun.
Folosire: python3 engine/final.py spec.json
spec.json:
{
  "out": "output/reel7/reel7-FINAL.mp4",
  "segments": [{"file": "...", "start": 0, "end": 2.5}, ...],      # în ordinea de montaj; doar hook-urile (hooks/) păstrează sunetul, altfel "audio": true
  "texts":    [{"t0": 0, "t1": 4.0, "text": "The problem 😩❄️"}, ...], # pe timeline-ul final
  "music": "library/music/all-i-want.m4a", "music_start": 0, "music_vol": 1.0, "orig_vol": 0.15
}
"""
import sys, json, os, subprocess, tempfile, unicodedata
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = os.path.join(ROOT, "library/fonts/TikTokSans-Bold.woff")   # fontul ca la competitori (Instagram „Classic”): TikTok Sans Bold, litere strânse
TRACK = -0.05   # spațierea literelor, în em (5 oct, după reel-ul competitorului DeAepvaSfSf)
EMOJI_DIR = os.path.join(ROOT, "library/fonts/apple-emoji")         # emoji de iPhone (emoji-datasource-apple, 64 px)
W, H = 1080, 1920

def is_emoji(ch):
    return ord(ch) >= 0x2190 and (unicodedata.category(ch) in ("So", "Sk") or ord(ch) >= 0x1F000) or ch in "️‍"

def clusters(text):
    """Împarte textul în bucăți: text normal / un emoji (cu FE0F, ZWJ, ton de piele)."""
    out, i = [], 0
    while i < len(text):
        ch = text[i]
        if is_emoji(ch) and ch not in "\ufe0f\u200d":
            seq = ch; i += 1
            while i < len(text) and (text[i] in "\ufe0f" or 0x1F3FB <= ord(text[i]) <= 0x1F3FF or (text[i] == "\u200d" and i + 1 < len(text))):
                if text[i] == "\u200d": seq += text[i] + text[i + 1]; i += 2
                else: seq += text[i]; i += 1
            out.append((True, seq))
        else:
            if out and not out[-1][0]: out[-1] = (False, out[-1][1] + ch)
            else: out.append((False, ch))
            i += 1
    return out

def emoji_img(seq, size):
    codes = [f"{ord(c):x}" for c in seq]
    for name in ("-".join(codes), "-".join(c for c in codes if c != "fe0f")):
        f = os.path.join(EMOJI_DIR, name + ".png")
        if os.path.exists(f):
            return Image.open(f).convert("RGBA").resize((int(size * 0.98), int(size * 0.98)), Image.LANCZOS)
    return None

def tlen(font, s, size):
    return sum(font.getlength(c) for c in s) + TRACK * size * max(len(s) - 1, 0)

def render_line(line, size):
    font = ImageFont.truetype(FONT, size); stroke = max(2, size // 28)
    parts = []
    for e, s in clusters(line):
        if e:
            im = emoji_img(s, size)
            if im: parts.append(im)
        else:
            s = s.rstrip() if s.endswith(" ") else s
            pad = stroke * 2 + 4
            im = Image.new("RGBA", (int(tlen(font, s, size)) + pad * 2, int(size * 1.3)), (0, 0, 0, 0))
            sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); d, ds = ImageDraw.Draw(im), ImageDraw.Draw(sh); x = pad
            for c in s:
                ds.text((x + 1, int(size * 0.05) + 2), c, font=font, fill=(0, 0, 0, 110))
                d.text((x, int(size * 0.05)), c, font=font, fill="white", stroke_width=stroke, stroke_fill=(20, 20, 20))
                x += font.getlength(c) + TRACK * size
            sh = sh.filter(ImageFilter.GaussianBlur(size / 18)); sh.alpha_composite(im); im = sh
            parts.append(im.crop((pad - stroke, 0, im.width - pad + stroke + 2, im.height)))
    gap = max(2, size // 16)
    w = sum(p.width for p in parts) + gap * (len(parts) - 1); h = max(p.height for p in parts)
    line_im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); x = 0
    for p in parts:
        line_im.paste(p, (x, (h - p.height) // 2), p); x += p.width + gap
    return line_im

def wrap(text, size, maxw):
    if "\n" in text:   # rânduri forțate (ex. replica + „Me: 😏”)
        return [l for part in text.split("\n") for l in wrap(part, size, maxw)]
    font = ImageFont.truetype(FONT, size); words = text.split(" "); lines = [""]
    for w_ in words:
        t = (lines[-1] + " " + w_).strip()
        if tlen(font, t, size) > maxw and lines[-1]: lines.append(w_)
        else: lines[-1] = t
    return lines

def text_png(text, path, size=70, ypos=0.148):
    lines = [render_line(l, size) for l in wrap(text, size, W * 0.84)]
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0)); y = int(H * ypos)   # "y" în spec = poziția textului (implicit 14,8% de sus, ca la competitori)
    for l in lines:
        canvas.paste(l, ((W - l.width) // 2, y), l); y += int(size * 1.07)
    canvas.save(path)

def main(spec_path):
    sp = json.load(open(spec_path)); tmp = tempfile.mkdtemp(); segs = []
    for i, s in enumerate(sp["segments"]):
        f = os.path.join(ROOT, s["file"]) if not os.path.isabs(s["file"]) else s["file"]
        o = os.path.join(tmp, f"s{i:02d}.mp4")
        has_a = subprocess.run(["ffprobe","-v","error","-select_streams","a","-show_entries","stream=index","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip()
        keep = s.get("audio", "hooks/" in s["file"])   # sunetul rămâne doar la hook (B-roll-ul Genjutsu are muzică proprie)
        cmd = ["ffmpeg","-y","-loglevel","error","-ss",str(s["start"]),"-to",str(s["end"]),"-i",f]
        if not has_a or not keep: cmd += ["-f","lavfi","-i","anullsrc=r=48000:cl=stereo","-shortest"]
        cmd += ["-vf","scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,format=yuv420p","-c:v","libx264","-crf","16","-c:a","aac","-ar","48000","-ac","2"]
        cmd += (["-map","0:v","-map","1:a"] if not has_a or not keep else []) + [o]
        subprocess.run(cmd, check=True); segs.append(o)
    lst = os.path.join(tmp, "l.txt"); open(lst, "w").write("\n".join(f"file '{x}'" for x in segs))
    base = os.path.join(tmp, "base.mp4")
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",lst,"-c","copy",base], check=True)
    dur = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",base],capture_output=True,text=True).stdout)
    inputs = ["-i", base]; chain = "[0:v]"; filt = []
    for k, t in enumerate(sp.get("texts", [])):
        png = os.path.join(tmp, f"t{k}.png"); text_png(t["text"], png, t.get("size", 70), t.get("y", 0.148)); inputs += ["-i", png]
        out = f"[v{k}]"; filt.append(f"{chain}[{k+1}:v]overlay=0:0:enable='between(t,{t['t0']},{t['t1']})'{out}"); chain = out
    n = len(sp.get("texts", [])) + 1
    if sp.get("music"):
        m = os.path.join(ROOT, sp["music"]) if not os.path.isabs(sp["music"]) else sp["music"]
        mlen = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",m],capture_output=True,text=True).stdout)
        dur = min(dur, mlen - sp.get("music_start", 0) - 0.05)   # videoul se termină când se oprește muzica (regula 2 oct)
        inputs += ["-ss", str(sp.get("music_start", 0)), "-i", m]
        filt.append(f"[0:a]volume={sp.get('orig_vol',0.15)}[oa];[{n}:a]volume={sp.get('music_vol',1.0)},afade=t=out:st={max(dur-0.5,0)}:d=0.5[ma];[oa][ma]amix=inputs=2:duration=first:normalize=0[a]")
        amap = "[a]"
    else:
        amap = "0:a"
    vmap = chain if sp.get("texts") else "0:v"
    out = os.path.join(ROOT, sp["out"])
    cmd = ["ffmpeg","-y","-loglevel","error",*inputs]
    if filt: cmd += ["-filter_complex", ";".join(filt)]
    cmd += ["-map", vmap, "-map", amap, "-c:v","libx264","-crf","18","-preset","medium","-c:a","aac","-b:a","192k","-t",str(dur),out]
    subprocess.run(cmd, check=True); print(out, round(dur, 2))

if __name__ == "__main__":
    main(sys.argv[1])
