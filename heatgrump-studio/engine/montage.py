"""Final edit, ready to post: cut pieces + on-screen text (Instagram style, with iPhone emoji) + music.
Usage: python3 engine/montage.py output/<name>/edit.json
edit.json:
{
  "out": "output/<name>/<name>-FINAL.mp4",
  "fps": 30,
  "segments": [{"file": "output/<name>/hook.mp4", "start": 0, "end": 2.5, "audio": true}, ...],   # in edit order; "audio": true keeps the clip sound (hooks)
  "texts":    [{"segs": [0, 2], "text": "Line one\nLine two 🐶", "size": 76, "y": 0.08}, ...],   # "segs": [first, last] = from the start of segment `first` to the end of segment `last` (0 = first segment; -1 = last) — ALWAYS use this, it lands exactly on the cuts. ("t0"/"t1" in seconds also works.) y = top of text as share of height
  "music": "music/xmas/mariah-all-i-want.mp3", "music_start": <drop> - <hook end>, "music_duck": <hook end>
}
Sound (rule 31 Oct, Alex - REPARATII #6): every "audio": true clip (the hook voice) is loudness-normalised (-16 LUFS), the song too
(-14 LUFS); the song plays quiet under the hook (music_hook_vol 0.2) and at full level from the drop, which lands exactly on the
hook -> B-roll cut (music_drop_vol 1.0, about as loud as the hook voice); the WHOLE final mix is then normalised to -14 LUFS, so the
video never gets quieter after the hook. The video ends when the music ends; the music fades out in the last 0.5 s.
It prints the real start of every segment in the final video ("cuts at ...") — use those numbers when you check the final sheet.
"""
import shutil, sys, json, os, subprocess, tempfile, unicodedata
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = os.path.join(ROOT, "engine/fonts/TikTokSans-w700-semicond.ttf")   # Reels/TikTok caption font
STROKE, TRACK, Y0 = 6, -0.01, 0.18   # thick black outline, slightly tight letters, default text top at 18% of height
EMOJI_DIR = os.path.join(ROOT, "engine/fonts/apple-emoji")         # iPhone emoji images
W, H = 1080, 1920

def is_emoji(ch):
    return ord(ch) >= 0x2190 and (unicodedata.category(ch) in ("So", "Sk") or ord(ch) >= 0x1F000) or ch in "️‍"

def clusters(text):
    """Split text into plain-text runs and single emoji (with FE0F, ZWJ, skin tone)."""
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
            return Image.open(f).convert("RGBA").resize((int(size * 1.12), int(size * 1.12)), Image.LANCZOS)
    return None

def render_line(line, size):
    font = ImageFont.truetype(FONT, size); stroke = STROKE
    parts = []
    for e, s in clusters(line):
        if e:
            im = emoji_img(s, size)
            if im: parts.append(im)
        else:
            s = s.rstrip()
            if not s: continue
            w = sum(font.getlength(c) for c in s) + TRACK * size * (len(s) - 1) + stroke * 2
            im = Image.new("RGBA", (int(w) + 4, int(size * 1.3)), (0, 0, 0, 0)); d = ImageDraw.Draw(im); x = stroke
            for c in s:   # letter by letter to tighten spacing like Reels
                d.text((x, int(size * 0.04)), c, font=font, fill="white", stroke_width=stroke, stroke_fill="black"); x += font.getlength(c) + TRACK * size
            parts.append(im)
    gap = max(2, size // 18)
    w = sum(p.width for p in parts) + gap * (len(parts) - 1); h = max(p.height for p in parts)
    line_im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); x = 0
    for p in parts:
        line_im.paste(p, (x, (h - p.height) // 2), p); x += p.width + gap
    return line_im

def wrap(text, size, maxw):
    if "\n" in text:   # forced line breaks
        return [l for part in text.split("\n") for l in wrap(part, size, maxw)]
    font = ImageFont.truetype(FONT, size); words = text.split(" "); lines = [""]
    for w_ in words:
        t = (lines[-1] + " " + w_).strip()
        if font.getlength(t) > maxw and lines[-1]: lines.append(w_)
        else: lines[-1] = t
    return lines

def text_png(text, path, size=88, y0=None):
    lines = [render_line(l, size) for l in wrap(text, size, W * 0.8)]
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0)); y = int(H * (Y0 if y0 is None else y0))
    for l in lines:
        canvas.paste(l, ((W - l.width) // 2, y), l); y += int(size * 1.08)
    canvas.save(path)

def main(spec_path):
    # rule 31 Oct (Alex): temp files go to <output folder>/_tmp (or $TMPDIR if set), segments at crf 20, and the temp
    # folder is deleted even when something fails - the disk is small.
    sp = json.load(open(spec_path))
    outdir = os.path.dirname(os.path.join(ROOT, sp["out"])) or ROOT
    tmp = tempfile.mkdtemp(prefix="_tmp-", dir=os.environ.get("TMPDIR") or outdir)
    try:
        _run(sp, tmp)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _run(sp, tmp):
    segs = []
    fps = str(sp.get("fps", 30))
    for i, s in enumerate(sp["segments"]):
        f = os.path.join(ROOT, s["file"]) if not os.path.isabs(s["file"]) else s["file"]
        o = os.path.join(tmp, f"s{i:02d}.mp4")
        has_a = subprocess.run(["ffprobe","-v","error","-select_streams","a","-show_entries","stream=index","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip()
        keep = s.get("audio", False)   # keep clip sound only where "audio": true
        cmd = ["ffmpeg","-y","-loglevel","error","-ss",str(s["start"]),"-to",str(s["end"]),"-i",f]
        if not has_a or not keep: cmd += ["-f","lavfi","-i","anullsrc=r=48000:cl=stereo","-shortest"]
        else: cmd += ["-af","loudnorm=I=-16:TP=-1.5:LRA=11,apad","-shortest"]   # hook voice at a fixed loudness (rule 31 Oct, REPARATII #6); sound exactly as long as the picture, so cuts don't drift
        cmd += ["-vf",f"scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps={fps},format=yuv420p","-c:v","libx264","-crf","20","-c:a","aac","-ar","48000","-ac","2"]
        cmd += (["-map","0:v","-map","1:a"] if not has_a or not keep else []) + [o]
        subprocess.run(cmd, check=True); segs.append(o)
    lst = os.path.join(tmp, "l.txt"); open(lst, "w").write("\n".join(f"file '{x}'" for x in segs))
    base = os.path.join(tmp, "base.mp4")
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",lst,"-c","copy",base], check=True)
    dur = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",base],capture_output=True,text=True).stdout)
    lens = [float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",x],capture_output=True,text=True).stdout) for x in segs]
    bounds = [round(sum(lens[:i]), 3) for i in range(len(lens) + 1)]   # real start of each segment + end
    print("cuts at", bounds[1:-1], "| segment starts:", {i: bounds[i] for i in range(len(lens))})
    for t in sp.get("texts", []):
        if "segs" in t:
            a, b = t["segs"]; b = b % len(lens)
            t["t0"], t["t1"] = bounds[a], (bounds[b + 1] if b + 1 < len(lens) else 999)
    inputs = ["-i", base]; chain = "[0:v]"; filt = []
    for k, t in enumerate(sp.get("texts", [])):
        png = os.path.join(tmp, f"t{k}.png"); text_png(t["text"], png, t.get("size", 88), t.get("y")); inputs += ["-i", png]
        out = f"[v{k}]"; filt.append(f"{chain}[{k+1}:v]overlay=0:0:enable='between(t,{t['t0']},{t['t1']})'{out}"); chain = out
    n = len(sp.get("texts", [])) + 1
    if sp.get("music"):
        m = os.path.join(ROOT, sp["music"]) if not os.path.isabs(sp["music"]) else sp["music"]
        mlen = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",m],capture_output=True,text=True).stdout)
        dur = min(dur, mlen - sp.get("music_start", 0) - 0.05)   # video ends when the music ends
        inputs += ["-ss", str(sp.get("music_start", 0)), "-i", m]
        duck = sp.get("music_duck")   # rule 28 Oct (updated): music QUIET under the hook (voice on top), a bit LOUDER from the drop at the cut hook -> B-roll
        if duck:
            lo, hi = sp.get("music_hook_vol", 0.2), sp.get("music_drop_vol", 1.0)
            mv = f"volume='if(lt(t,{duck}),{lo},if(lt(t,{duck}+0.12),{lo}+({hi}-{lo})*(t-{duck})/0.12,{hi}))':eval=frame"
        else:
            mv = f"volume={sp.get('music_vol',1.0)}"
        # rule 31 Oct (Alex, REPARATII #6): song normalised first, whole mix normalised last -> never quieter after the hook
        filt.append(f"[0:a]volume={sp.get('orig_vol',1.0)}[oa];[{n}:a]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000,{mv},afade=t=out:st={max(dur-0.5,0)}:d=0.5[ma];[oa][ma]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]")
        amap = "[a]"
    else:
        amap = "0:a"
    vmap = chain if sp.get("texts") else "0:v"
    out = os.path.join(ROOT, sp["out"])
    cmd = ["ffmpeg","-y","-loglevel","error",*inputs]
    if filt: cmd += ["-filter_complex", ";".join(filt)]
    cmd += ["-map", vmap, "-map", amap, "-c:v","libx264","-profile:v","high","-pix_fmt","yuv420p","-r",fps,"-crf","18","-preset","medium","-c:a","aac","-b:a","192k","-ar","48000","-movflags","+faststart","-t",str(dur),out]   # Reels/TikTok spec: 1080x1920, H.264 high, AAC 48 kHz, faststart
    subprocess.run(cmd, check=True); print(out, round(dur, 2))

if __name__ == "__main__":
    main(sys.argv[1])
