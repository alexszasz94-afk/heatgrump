"""Montaj FINAL gata de postat: bucăți tăiate + texte pe ecran (cu emoji, stil Instagram) + muzică de Crăciun.
Folosire: python3 engine/final.py spec.json
spec.json:
{
  "out": "output/reel7/reel7-FINAL.mp4",
  "segments": [{"file": "...", "start": 0, "end": 2.5}, ...],      # în ordinea de montaj
  "texts":    [{"t0": 0, "t1": 4.0, "text": "The problem 😩❄️"}, ...], # pe timeline-ul final
  "music": "library/music/all-i-want.m4a", "music_start": 0, "music_vol": 1.0, "orig_vol": 0.15
}
"""
import sys, json, os, subprocess, tempfile, unicodedata
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = os.path.join(ROOT, "library/fonts/Montserrat-Bold.ttf")
EMOJI = os.path.join(ROOT, "library/fonts/NotoColorEmoji.ttf")
W, H = 1080, 1920

def is_emoji(ch):
    return ord(ch) >= 0x2190 and (unicodedata.category(ch) in ("So", "Sk") or ord(ch) >= 0x1F000) or ch in "️‍"

def runs(text):
    out = []
    for ch in text:
        e = is_emoji(ch)
        if out and out[-1][0] == e: out[-1][1] += ch
        else: out.append([e, ch])
    return out

def render_line(line, size):
    font = ImageFont.truetype(FONT, size)
    efont = ImageFont.truetype(EMOJI, 109)
    parts = []
    for e, s in runs(line):
        if e:
            for ch in s:
                if ch in "️‍": continue
                im = Image.new("RGBA", (136, 128), (0, 0, 0, 0))
                ImageDraw.Draw(im).text((0, 0), ch, font=efont, embedded_color=True)
                im = im.crop(im.getbbox() or (0, 0, 1, 1)).resize((int(size * 1.05), int(size * 1.05)))
                parts.append(im)
        else:
            bb = font.getbbox(s, stroke_width=6)
            im = Image.new("RGBA", (bb[2] + 12, int(size * 1.35)), (0, 0, 0, 0))
            ImageDraw.Draw(im).text((6, 0), s, font=font, fill="white", stroke_width=6, stroke_fill=(0, 0, 0, 170))
            parts.append(im)
    w = sum(p.width for p in parts) + 6 * (len(parts) - 1); h = max(p.height for p in parts)
    line_im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); x = 0
    for p in parts:
        line_im.paste(p, (x, (h - p.height) // 2), p); x += p.width + 6
    return line_im

def wrap(text, size, maxw):
    font = ImageFont.truetype(FONT, size); words = text.split(" "); lines = [""]
    for w_ in words:
        t = (lines[-1] + " " + w_).strip()
        if font.getlength(t) > maxw and lines[-1]: lines.append(w_)
        else: lines[-1] = t
    return lines

def text_png(text, path, size=58):
    lines = [render_line(l, size) for l in wrap(text, size, W * 0.8)]
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0)); y = int(H * 0.22)
    for l in lines:
        canvas.paste(l, ((W - l.width) // 2, y), l); y += l.height + 8
    canvas.save(path)

def main(spec_path):
    sp = json.load(open(spec_path)); tmp = tempfile.mkdtemp(); segs = []
    for i, s in enumerate(sp["segments"]):
        f = os.path.join(ROOT, s["file"]) if not os.path.isabs(s["file"]) else s["file"]
        o = os.path.join(tmp, f"s{i:02d}.mp4")
        has_a = subprocess.run(["ffprobe","-v","error","-select_streams","a","-show_entries","stream=index","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip()
        cmd = ["ffmpeg","-y","-loglevel","error","-ss",str(s["start"]),"-to",str(s["end"]),"-i",f]
        if not has_a: cmd += ["-f","lavfi","-i","anullsrc=r=48000:cl=stereo","-shortest"]
        cmd += ["-vf","scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,format=yuv420p","-c:v","libx264","-crf","16","-c:a","aac","-ar","48000","-ac","2",o]
        subprocess.run(cmd, check=True); segs.append(o)
    lst = os.path.join(tmp, "l.txt"); open(lst, "w").write("\n".join(f"file '{x}'" for x in segs))
    base = os.path.join(tmp, "base.mp4")
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",lst,"-c","copy",base], check=True)
    dur = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",base],capture_output=True,text=True).stdout)
    inputs = ["-i", base]; chain = "[0:v]"; filt = []
    for k, t in enumerate(sp.get("texts", [])):
        png = os.path.join(tmp, f"t{k}.png"); text_png(t["text"], png, t.get("size", 58)); inputs += ["-i", png]
        out = f"[v{k}]"; filt.append(f"{chain}[{k+1}:v]overlay=0:0:enable='between(t,{t['t0']},{t['t1']})'{out}"); chain = out
    n = len(sp.get("texts", [])) + 1
    if sp.get("music"):
        m = os.path.join(ROOT, sp["music"]) if not os.path.isabs(sp["music"]) else sp["music"]
        inputs += ["-ss", str(sp.get("music_start", 0)), "-i", m]
        filt.append(f"[0:a]volume={sp.get('orig_vol',0.15)}[oa];[{n}:a]volume={sp.get('music_vol',1.0)},afade=t=out:st={max(dur-0.8,0)}:d=0.8[ma];[oa][ma]amix=inputs=2:duration=first:normalize=0[a]")
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
