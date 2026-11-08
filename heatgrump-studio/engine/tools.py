"""Helper commands Claude uses while making a video. Run from the kit folder:

  python3 engine/tools.py download <url | inbox/file.mp4> <folder>       -> <folder>/reference.mp4 (+ prints length and cuts); a local file (inbox/) is copied
  python3 engine/tools.py sheet <video> <out.jpg> [fps]                 -> contact sheet of frames (default 2 fps) to look at
  python3 engine/tools.py frame <video> <seconds> <out.jpg>             -> one full-size frame
  python3 engine/tools.py cuts <video>                                   -> times where the shot changes
  python3 engine/tools.py safe-end <video>                               -> last safe second before Kling appends a reference image / fades out
  python3 engine/tools.py fetch <url> <out-file>                          -> download a Higgsfield result (png results are saved as jpg)
  python3 engine/tools.py drop <song.mp3>                                 -> candidate drop seconds to LISTEN to (the kit songs have fixed, checked drops in XMAS_SONGS)
  python3 engine/tools.py fanwipe <in.mp4> <out.mp4> <t1> [<t2> ...]       -> ceiling-fan blade wipe centred on each cut time
  python3 engine/tools.py next-set <robe> [--new]                         -> character (sharpest free) + room (in order) + B-roll v4/v5 + fixed connector/remote + song; run twice without `log` = the SAME pick (rule 31 Oct, Alex)
  python3 engine/tools.py cutjerk <broll.mp4> <out.mp4>                   -> B-roll v4 ONLY: cuts 3.10-3.40 s out (the robe-opening jerk); everything after comes 0.30 s earlier (rule 31 Oct, Alex)
  python3 engine/tools.py add-rooms <rooms.zip>                           -> Alex's rooms zip (the ONLY source of rooms, rule 28 Oct) -> library/rooms/room-NN.jpg (next free numbers)
  python3 engine/tools.py photo-ok <photo>                               -> True/False + reason: short side >= 1080 (4K preferred) and sharp (rule 29 Oct)
  python3 engine/tools.py reject <library/characters/x.jpg | library/rooms/x.jpg>  -> photo breaks the rules: moves ONLY that file to library/rejected/; the next next-set re-picks only that kind (rule 31 Oct, Alex)
  python3 engine/tools.py crop <in.jpg> <out.jpg> <left> <top> <right> <bottom>   -> crop (fractions 0-1), e.g. character head+shoulders for the B-roll
  python3 engine/tools.py compare <original.mp4> <ours.mp4> <from_s> <to_s> <out.jpg>   -> original (top) vs ours (bottom), 10 frames/s, to check the motion is identical
  python3 engine/tools.py log <video-name> key=value ...                 -> remembers what this video used (hook, outfit, music, text, motion, robe)
  python3 engine/tools.py cleantext <video> <clean.jpg> <out.mp4> <l> <t> <r> <b> [...more boxes]  -> covers their on-screen text with the same spot from a clean photo (static camera only) - no blur for Kling to copy
  python3 engine/tools.py broll-check <broll.mp4> <motion.mp4> <out-folder>   -> B-roll safety check: shot count vs the motion clip, glitch spikes inside shots, safe segments, one sheet per shot to look at
  python3 engine/tools.py retime <our-hook.mp4> <reference-hook.mp4> <out.mp4> [hook end s] -> ends our hook EXACTLY on the original's hook end (trim / hold last frame), keeps the sound, never changes speed; prints cut differences (rule 31 Oct, Alex)
  python3 engine/tools.py hold <hook.mp4> <out.mp4> <action start in ours> <action start in original> [our a3 folder] -> action EARLY: lengthens the still part before it (forward/back/forward, sound mirrored); LATE (negative shift): removes still part; refuses if words would be cut (rule 31 Oct, Alex)
  python3 engine/tools.py hookinput <reference.mp4> <hook end> <out.mp4>   -> Kling input of a copied hook: 0..hook end, silent, last frame frozen to the next whole second (min 3) - never the next scene (rule 31 Oct, Alex)
  python3 engine/tools.py roomtone <hook.mp4> <out.mp4>                   -> fills dead-silent gaps of a hook with a quiet bed made from its own quietest part (rule 31 Oct, Alex)
  python3 engine/tools.py still <video> [start] [end]                     -> YES/NO: is the camera still? Run it BEFORE making a clean frame for cleantext (rule 31 Oct, Alex)
  python3 engine/tools.py spectro <audio-or-video> <out.jpg> [seconds]    -> picture of the sound: check MUSIC by eye (horizontal note lines + regular beat) (rule 31 Oct, Alex)
  python3 engine/tools.py put <file> <upload_url>                         -> the upload PUT for Higgsfield (prints 200), instead of a curl line (rule 31 Oct, Alex)
  python3 engine/tools.py compare-audio <original a3 folder> <our-hook.mp4> <hook end> <our a3 folder>  -> ADVICE ONLY: runs audio3 on OUR hook, word starts side by side, extra/missing words, dead-silent gaps; no music verdict (use spectro); never decides a redo (rule 31 Oct, Alex)
  python3 engine/tools.py history [n]                                     -> what the last n videos used (default 5), so the next one is different

  HOOK SOUND ANALYSIS (the ONE way, rule 31 Oct, Alex):
  python3 engine/audio3.py <hook part.mp4> <hook end s> <out folder> "<line from Higgsfield video_analysis>" [--no-voice]   (--no-voice when the analysis says nobody speaks)
      -> 3 parts: VOICE (every word with its start/end second, tone), ACTION SOUNDS (+ events.jpg), BACKGROUND (music / room tone)
  (`tools.py hook-audio` and `tools.py audit-sound` are only old names: they run audio3 / compare-audio.)
"""
import json, math, os, subprocess, sys, tempfile, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def duration(f):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).stdout.strip() or 0)


def cuts(f, thr=0.2):
    out = run(["ffmpeg", "-i", f, "-vf", f"select='gt(scene,{thr})',showinfo", "-f", "null", "-"]).stderr
    return [round(float(x.split(":")[1]), 2) for x in out.split() if x.startswith("pts_time:") and float(x.split(":")[1]) > 0.1]


def download(url, folder):
    os.makedirs(folder, exist_ok=True)
    out = os.path.join(folder, "reference.mp4")
    if os.path.exists(url):   # a file the creator put in inbox/ (when the link download fails)
        import shutil; shutil.copy(url, out); print(out, "length", round(duration(out), 2), "cuts", cuts(out, 0.25)); return
    for _ in range(3):
        run(["yt-dlp", "-q", "-f", "mp4/best", "-o", out, url])
        if os.path.exists(out):
            break
    if not os.path.exists(out):
        sys.exit("Download failed. Ask the user to save the video and put it in inbox/.")
    print(out, "length", round(duration(out), 2), "cuts", cuts(out, 0.25))


def sheet(f, out, fps="2"):
    d = duration(f); n = max(1, int(d * float(fps)))
    cols = min(n, 8); rows = math.ceil(n / cols)
    run(["ffmpeg", "-v", "error", "-y", "-i", f, "-vf", f"fps={fps},scale=200:-1,tile={cols}x{rows}", "-frames:v", "1", out])
    print(out, f"({n} frames, {fps} per second, left to right, top to bottom)")


def frame(f, t, out):
    run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", f, "-frames:v", "1", "-q:v", "2", out]); print(out)


def safe_end(f):
    """Kling image-to-video often ends with a jump to one of the reference images or a fade.
    Returns the last second before the first cut in the second half or before brightness collapses."""
    d = duration(f)
    late = [c for c in cuts(f, 0.12) if c > d * 0.4]   # sensitive: also catches zoom jumps
    out = run(["ffmpeg", "-i", f, "-vf", "signalstats,metadata=print:key=lavfi.signalstats.YAVG", "-f", "null", "-"]).stderr
    ys = [float(x.split("=")[1]) for x in out.split() if x.startswith("lavfi.signalstats.YAVG=")]
    fps = len(ys) / d if d else 24
    fade = None
    for i in range(int(len(ys) * 0.4), len(ys)):
        if ys[i] < ys[0] * 0.8:
            fade = i / fps; break
    ends = [x for x in late + ([fade] if fade else [])]
    end = round(min(ends) - 0.1, 2) if ends else round(d, 2)
    print("length", round(d, 2), "late cuts", late, "fade", round(fade, 2) if fade else None, "-> use end", end)
    return end


def fetch(url, out):
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    if url.lower().split("?")[0].endswith(".png") and out.lower().endswith(".jpg"):
        tmp = out + ".png"
        run(["curl", "-s", "-o", tmp, url]); run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-q:v", "2", out]); os.remove(tmp)
    else:
        run(["curl", "-s", "-o", out, url])
    print(out, os.path.getsize(out) if os.path.exists(out) else "FAILED")


def drop(f):
    """Candidates for the drop: the biggest steps in loudness (median of 4 s after vs 4 s before, every 0.1 s), first 5 s
    skipped. Only a list to LISTEN to (rule 31 Oct, Alex): the kit songs have fixed, checked drops in XMAS_SONGS - use those."""
    import numpy as np
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-ac", "1", "-ar", "8000", "-f", "s16le", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, dtype=np.int16).astype(float); w = 800
    d = 20 * np.log10(np.sqrt(np.array([np.mean(a[i:i + w] ** 2) for i in range(0, len(a) - w, w)])) + 1)
    sc = sorted(((float(np.median(d[i:i + 40]) - np.median(d[i - 40:i])), i / 10) for i in range(50, len(d) - 40)), reverse=True)
    picks = []
    for v, t in sc:
        if all(abs(t - p) > 4 for _, p in picks): picks.append((round(v, 1), t))
        if len(picks) >= 6: break
    known = XMAS_SONGS.get(os.path.basename(f))
    print("biggest loudness steps (dB, second) - LISTEN around them:", picks, f"| kit value for this song: {known} s" if known is not None else "")


def hookinput(ref, end, out):
    """rule 31 Oct (Alex): the Kling video-edit input of a copied hook: the reference from 0 to the hook end, SILENT,
    the last frame frozen up to the next whole second (min 3 s) - never the next scene."""
    end = float(end); n = max(3, math.ceil(end - 0.001))
    run(["ffmpeg", "-v", "error", "-y", "-i", ref, "-vf", f"trim=0:{end:.3f},setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration={n - end + 0.2:.3f}",
         "-an", "-t", str(n), "-c:v", "libx264", "-crf", "17", "-pix_fmt", "yuv420p", out])
    print(out, f"- {duration(out):.2f} s silent (hook {end:.2f} s + last frame frozen to {n} s) -> Kling duration {n}")


def roomtone(f, out, gap_db="-50"):
    """rule 31 Oct (Alex): Kling sometimes leaves dead-silent gaps in a hook. Builds a quiet bed from the hook's own
    quietest non-silent 0.5 s (looped, mirrored joins) and mixes it under the hook sound, so the room tone never stops."""
    import numpy as np
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
    x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768; n = len(x) // 160
    if n < 60: sys.exit("roomtone: the clip has no usable sound")
    e = 20 * np.log10(np.sqrt((x[:n * 160].reshape(n, 160) ** 2).mean(1)) + 1e-9)
    win = [(float(np.mean(e[i:i + 50])), i) for i in range(0, n - 50, 5) if e[i:i + 50].min() > float(gap_db)]
    if not win: sys.exit("roomtone: no non-silent 0.5 s in the hook to make a bed from - regenerate the hook sound instead")
    lv, i0 = min(win); t0 = i0 / 100; d = duration(f)
    fc = (f"[0:a]aresample=48000,asplit[m][s];[s]atrim={t0:.3f}:{t0 + 0.5:.3f},asetpts=PTS-STARTPTS,asplit[p][q];[q]areverse[r];[p][r]concat=n=2:v=0:a=1,"
          f"aloop=loop=-1:size=48000,atrim=0:{d:.3f},asetpts=N/SR/TB,volume=0.9[bed];[m][bed]amix=inputs=2:duration=first:normalize=0[a]")
    run(["ffmpeg", "-v", "error", "-y", "-i", f, "-filter_complex", fc, "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", out])
    gaps = int((e < float(gap_db)).sum())
    print(out, f"- room-tone bed from {t0:.2f}-{t0 + 0.5:.2f} s ({lv:.0f} dB) under the whole hook; it had {gaps / 100:.2f} s of dead silence before")


def still(f, start="0", end=None, px="2"):
    """rule 31 Oct (Alex): is the CAMERA still between start and end? (cleantext only works on a still camera - run this
    BEFORE making any clean frame.) Phase correlation of every frame against the first one (128 px wide, 15 fps):
    a total drift of >= 2 px (~1.5 % of the width), or the top third of the picture (background, where captions sit)
    changing by > 6 grey levels on average = moving."""
    import numpy as np
    end = float(end) if end else duration(f); w, h = 128, 228
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(start), "-to", f"{end:.3f}", "-i", f, "-vf", f"fps=15,scale={w}:{h},format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(float)
    if len(fr) < 2: sys.exit("still: too short")
    win = np.outer(np.hanning(h), np.hanning(w)); A = np.fft.fft2((fr[0] - fr[0].mean()) * win); drift = []
    for k in range(1, len(fr)):
        R = A * np.conj(np.fft.fft2((fr[k] - fr[k].mean()) * win)); R /= np.abs(R) + 1e-9
        y, x = np.unravel_index(np.abs(np.fft.ifft2(R)).argmax(), (h, w))
        y = y - h if y > h // 2 else y; x = x - w if x > w // 2 else x
        drift.append((round(float(start) + k / 15, 2), int(abs(x) + abs(y))))
    top = [(round(float(start) + k / 15, 2), float(np.abs(fr[k][:h // 3] - fr[0][:h // 3]).mean())) for k in range(1, len(fr))]
    moving = sorted(set([t for t, d in drift if d >= int(px)] + [t for t, v in top if v > 6]))   # + the top third (where captions sit) changes
    print(("YES - the camera is still" if not moving else f"NO - the camera/background moves from {moving[0]} s (drift up to {max(d for _, d in drift)} px, top-third change up to {max(v for _, v in top):.0f})")
          + ". " + ("cleantext can work; still LOOK that nothing (a hand, the product) crosses the caption box." if not moving else "Do NOT use cleantext for this part: leave the caption in and write `remove the caption text completely` in the Kling prompt."))
    return not moving


def spectro(f, out, end=None):
    """rule 31 Oct (Alex): picture of the sound to check MUSIC by eye: music = long horizontal lines (held notes) and a
    regular vertical beat; room tone = even grey haze; a thump = one short vertical stripe."""
    run(["ffmpeg", "-v", "error", "-y"] + (["-t", str(end)] if end else []) + ["-i", f, "-lavfi", "showspectrumpic=s=1200x500:legend=1:scale=log:fscale=log", out])
    print(out, "- music = horizontal lines (notes) + a regular vertical beat across the whole width; room tone = even haze; a thump = one short vertical stripe")


def fanwipe(f, out, times):
    from PIL import Image, ImageDraw, ImageFilter
    W, H = 1080, 1920; tmp = tempfile.mkdtemp(); hub = (-120, -160); L, w, n = 2600, 520, 12
    for i in range(n):
        a = math.radians(100 - i * (105 / (n - 1)))
        im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        dx, dy = math.cos(a), math.sin(a); px, py = -dy, dx
        p0 = (hub[0] + px * w * .25, hub[1] + py * w * .25); p1 = (hub[0] - px * w * .25, hub[1] - py * w * .25)
        q1 = (hub[0] + dx * L - px * w / 2, hub[1] + dy * L - py * w / 2); q0 = (hub[0] + dx * L + px * w / 2, hub[1] + dy * L + py * w / 2)
        d.polygon([p0, q0, q1, p1], fill=(92, 88, 84, 255))
        im.filter(ImageFilter.GaussianBlur(28)).save(f"{tmp}/b{i:02d}.png")
    inputs, chain, filt = ["-i", f], "[0:v]", []
    for k, t in enumerate(times):
        inputs += ["-framerate", "30", "-i", f"{tmp}/b%02d.png"]
        filt.append(f"[{k+1}]setpts=PTS+{float(t)-0.2}/TB[b{k}]")
        filt.append(f"{chain}[b{k}]overlay=eof_action=pass[x{k}]"); chain = f"[x{k}]"
    filt[-1] = filt[-1].replace(f"[x{len(times)-1}]", ",format=yuv420p[v]")
    run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(filt), "-map", "[v]", "-map", "0:a?", "-c:v", "libx264", "-crf", "18", "-c:a", "copy", out])
    print(out)


BROLL_VARIANTS = {   # rule 31 Oct (Alex): ONLY the 2 proven B-roll variants per robe, rotating (never the same twice in a row).
    # key: (motion file = OUR finished silent reference B-roll, duration for Kling, edit note). Prompt = PRODUCT.md section "B-roll v4" / "B-roll v5".
    "v4": ("motion/{robe}-v4.mp4", 8, "put on (back, hood) + foot pockets + cozy sitting WIDE on the real sofa; AFTER generating ALWAYS run `tools.py cutjerk` (cuts 3.10-3.40 s)"),
    "v5": ("motion/{robe}-v5.mp4", {"princess": 6, "snoopy": 7, "grinch": 6}, "sleeves + back + lying on the sofa + cozy lying WIDE on the real sofa; no foot-pocket shot"),
}

XMAS_SONGS = {   # rule 30 Oct (Alex): rotating Christmas songs, shared pool for both robes - file in music/xmas/, drop second (the full-band/chorus entry, LISTEN-checked)
    "mariah-all-i-want.mp3": 53.4,
    "buble-beginning.mp3": 35.35,
    "wham-last-christmas.mp3": 0.0,   # steady from the start, no clear drop
    # "let-it-go.mp3": 58.5,  # SCOASĂ (Szasz 8 nov): piesa de la prințesă NU se mai pune la Grinch
}


def next_song(robe):
    """rule 30 Oct (Alex): next-set also rotates the Christmas song - never the same as the last 2 videos (any robe)."""
    f = os.path.join(ROOT, "state/used.json")
    vids = (json.load(open(f)) if os.path.exists(f) else {}).get("videos", [])
    recent = [v.get("song", "") for v in vids[-2:]]
    keys = list(XMAS_SONGS)
    for k in keys:
        if k not in recent:
            return k
    return keys[0]


def broll_variants(robe):
    return list(BROLL_VARIANTS)


def broll_info(robe, key):
    mf, dur, how = BROLL_VARIANTS[key]
    return mf.format(robe=robe.lower()), (dur[robe.lower()] if isinstance(dur, dict) else dur), how


def _used():
    f = os.path.join(ROOT, "state/used.json")
    u = json.load(open(f)) if os.path.exists(f) else {}
    for k in ("characters", "rooms", "videos"): u.setdefault(k, [])
    return u


def _save_used(u):
    json.dump(u, open(os.path.join(ROOT, "state/used.json"), "w"), indent=1)


def next_motion(robe):
    """rule 31 Oct (Alex): the B-roll alternates v4 / v5 per robe - never the same twice in a row (old keys -> start with v4)."""
    keys = broll_variants(robe)
    vids = [v for v in _used().get("videos", []) if v.get("robe", "").lower() == robe.lower()]
    last = vids[-1].get("motion", "") if vids else ""
    return keys[(keys.index(last) + 1) % len(keys)] if last in keys else keys[0]


def fixed_clips(robe, kind):
    """rule 31 Oct (Alex): connector and remote are ALWAYS the fixed clips. The fabric close-ups (fixed/<kind>-fabric-N.mp4)
    are used in every video; the old tree close-ups (fixed/<kind>-tree-N.mp4) are only alternates (e.g. a fabric clip fails the check)."""
    d = os.path.join(ROOT, "products", robe.lower(), "fixed")
    fab = [os.path.basename(h) for h in sorted(glob.glob(os.path.join(d, f"{kind}-sofa-close-*.mp4"))) + sorted(glob.glob(os.path.join(d, f"{kind}-sofa-[0-9]*.mp4")))]   # Grinch 1 Nov: sofa versions first
    fab += [os.path.basename(h) for h in sorted(glob.glob(os.path.join(d, f"{kind}-fabric-*.mp4")))]
    tree = [os.path.basename(h) for h in sorted(glob.glob(os.path.join(d, f"{kind}-tree-*.mp4")))]
    return fab, tree


def next_fixed(robe, kind):
    fab, tree = fixed_clips(robe, kind)
    names = fab or tree
    if not names:
        return None
    vids = [v for v in _used().get("videos", []) if v.get("robe", "").lower() == robe.lower()]
    last = vids[-1].get(kind, "") if vids else ""
    return names[(names.index(last) + 1) % len(names)] if last in names else names[0]


def next_remote(robe):
    return next_fixed(robe, "remote")


def photo_ok(f, min_side=1080, min_sharp=150):
    """rule 29 Oct (Alex): rooms/characters ALWAYS high quality - short side >= 1080 (4K preferred), sharp. Returns (ok, reason)."""
    from PIL import Image, ImageFilter, ImageStat
    try: im = Image.open(f).convert("L")
    except Exception: return False, "broken file"
    w, h = im.size
    if min(w, h) < min_side: return False, f"low resolution {w}x{h} (needs short side >= {min_side}, 4K preferred)"
    im = im.resize((1080, max(2, round(1080 * h / w))))
    var = ImageStat.Stat(im.filter(ImageFilter.Kernel((3, 3), (0, -1, 0, -1, 4, -1, 0, -1, 0), 1, 128))).var[0]
    if var < min_sharp: return False, f"blurry (sharpness {var:.0f} < {min_sharp})"
    return True, f"{w}x{h}" + (" 4K" if min(w, h) >= 2160 else " full HD")


FIXED_TIMES = {   # rule 31 Oct (Alex): checked frame by frame at 24 fps - princess connector: another hand 0-0.12 s; both: 1 flash frame at 1.67 s
    ("grinch", "connector-sofa-close-1.mp4"): "0.05 -> 1.70 (fully joined)",
    ("grinch", "remote-sofa-close-1.mp4"): "0.3 -> 3.0 (one light climbing)",
    ("grinch", "connector-sofa-1.mp4"): "0.05 -> 1.70 (fully joined; another shot from 1.79 s)",
    ("grinch", "remote-sofa-1.mp4"): "0.3 -> 3.0 (all off, then ONE light climbing)",
    ("grinch", "connector-fabric-1.mp4"): "0.05 -> 1.70 (checked 1 Nov at 24 fps: fully joined, no gap; a different shot starts at 1.77 s)",
    ("grinch", "remote-fabric-1.mp4"): "0.3 -> 3.0 (all off, then ONE light climbing, never two)",
    ("princess", "connector-fabric-1.mp4"): "0.15 -> 1.63 (clean range: another hand before 0.13 s, a flash frame at 1.67 s)",
    ("snoopy", "connector-fabric-1.mp4"): "0.05 -> 1.63 (clean range: a flash frame at 1.67 s)",
    ("princess", "remote-fabric-1.mp4"): "0.3 -> 3.0 (one light climbing, never two)", ("snoopy", "remote-fabric-1.mp4"): "0.3 -> 3.0 (one light climbing, never two)",
    "connector": "1.2 -> 4.0 (tree clip: fully joined at ~3.0 s)", "remote": "the whole clip (tree clip)"}


def sharpness(f):
    from PIL import Image, ImageFilter, ImageStat
    im = Image.open(f).convert("L"); w, h = im.size
    im = im.resize((1080, max(2, round(1080 * h / w))))
    return ImageStat.Stat(im.filter(ImageFilter.Kernel((3, 3), (0, -1, 0, -1, 4, -1, 0, -1, 0), 1, 128))).var[0]


def next_set(robe="", new=False):
    """Picks a character + room (rule 31 Oct, Alex):
    - run twice without `log` in between -> the SAME pick again (nothing is burned); `--new` forces a fresh pick;
    - after `reject` of one photo only that kind is picked again, the other photo is kept;
    - characters: only ones passing photo_ok (full HD + sharp), the SHARPEST free one first; failing ones -> library/rejected;
    - rooms: in file-name order from library/rooms (Alex's 4K rooms with a sofa first)."""
    used = _used(); cur = {} if new else (used.get("current") or {})
    keep = {k: cur[k] for k in ("characters", "rooms") if cur.get(k) and os.path.exists(os.path.join(ROOT, "library", k, cur[k]))}
    if len(keep) == 2:
        print("(same pick as before - it was not logged yet; `next-set <robe> --new` for a different one)")
    pick = {}
    for kind in ("characters", "rooms"):
        if kind in keep:
            pick[kind] = os.path.join(ROOT, "library", kind, keep[kind]); continue
        free = [p for p in sorted(glob.glob(os.path.join(ROOT, "library", kind, "*.jpg"))) if os.path.basename(p) not in used[kind]]
        for p in list(free):
            ok, why = photo_ok(p, min_sharp=150)
            if not ok: free.remove(p); reject(p, quiet=True); print(f"REJECTED {os.path.basename(p)}: {why}")
        if kind == "characters":
            free.sort(key=lambda p: -sharpness(p))   # the clearest photo first (Alex: "the character must be clear")
        if not free:
            print(f"NO_{kind.upper()}_LEFT: " + ("ask the creator for Alex's new rooms (zip) and run `tools.py add-rooms <zip>`." if kind == "rooms" else "run the skill find-sets now (Pinterest search, you pick the good ones), then run next-set again. Ask the creator for photos ONLY if Pinterest fails."))
            if pick: used["current"] = {k: os.path.basename(v) for k, v in pick.items()}; _save_used(used)
            return
        pick[kind] = free[0]; used[kind].append(os.path.basename(free[0]))
    used["current"] = {"characters": os.path.basename(pick["characters"]), "rooms": os.path.basename(pick["rooms"])}
    _save_used(used)
    print("character:", os.path.relpath(pick["characters"], ROOT), "(kept from the last pick)" if "characters" in keep else "")
    print("room:", os.path.relpath(pick["rooms"], ROOT), "(kept from the last pick)" if "rooms" in keep else "")
    print("LOOK at both now: character = real photo, LIGHT SKIN only (rule 31 Oct), face visible; room = real photo with a SOFA clearly visible "
          "(the v4/v5 cozy shot is filmed on the room's real sofa) and free floor in front. Bad one -> `tools.py reject <that file>` and next-set again (only that one is re-picked).")
    if robe:
        m = next_motion(robe)
        mf, dur, how = broll_info(robe, m)
        print(f"B-roll: {m} -> motion clip {mf} (video_references), duration {dur}; prompt = products/{robe.lower()}/PRODUCT.md section \"B-roll {m}\", word for word; {how}; log it with motion={m}")
        for kind in ("connector", "remote"):
            r = next_fixed(robe, kind)
            fab, tree = fixed_clips(robe, kind)
            alt = [x for x in fab + tree if x != r]
            if r: print(f"{kind}: products/{robe.lower()}/fixed/{r} use {FIXED_TIMES.get((robe.lower(), r), FIXED_TIMES[kind])}; log it with {kind}={r}" + (f" (alternates only if it fails the check: {', '.join(alt)})" if alt else ""))
        song = next_song(robe)
        drop = XMAS_SONGS[song]
        start = f"{drop} - <hook end>" if drop else "0"
        print(f"song: music/xmas/{song} (drop at {drop} s; log it with song={song}) -> edit.json: \"music\": \"music/xmas/{song}\", \"music_start\": {start}, \"music_duck\": <hook end>")
    for kind in ("characters", "rooms"):
        left = len([p for p in glob.glob(os.path.join(ROOT, "library", kind, "*.jpg")) if os.path.basename(p) not in used[kind]])
        if left < 5:
            print(f"ONLY {left} {kind.upper()} LEFT: " + ("ask the creator for Alex's next rooms zip (`tools.py add-rooms <zip>`)." if kind == "rooms" else "after this video run the skill find-sets to add new ones (automatic Pinterest search)."))


def cutjerk(f, out, a="3.10", b="3.40"):
    """rule 31 Oct (Alex): B-roll v4 - the robe-opening jerk is removed in the EDIT, never in the input: cut 3.10-3.40 s
    out (half-open robe -> fully open robe, a clean cut). Everything after 3.40 s comes 0.30 s earlier. Exact command of the recipe."""
    run(["ffmpeg", "-v", "error", "-y", "-i", f, "-filter_complex",
         f"[0:v]split[x][y];[x]trim=0:{a},setpts=PTS-STARTPTS[a];[y]trim={b},setpts=PTS-STARTPTS[b];[a][b]concat=n=2:v=1[v]",
         "-map", "[v]", "-an", "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", out])
    d0, d1 = duration(f), duration(out)
    print(out, f"length {d0:.2f} -> {d1:.2f} s (cut {float(b) - float(a):.2f} s). Check 2.7-3.5 s at 15 fps: robe half open, then fully open, no jerk frame.")


def add_rooms(z):
    """rule 28 Oct (Alex): rooms come from the zips Alex gives (real phone photos of real American homes, picked by him)."""
    import zipfile, io
    from PIL import Image
    d = os.path.join(ROOT, "library/rooms"); os.makedirs(d, exist_ok=True)
    nums = [int(os.path.basename(p)[5:7]) for p in glob.glob(os.path.join(d, "room-*.jpg")) + glob.glob(os.path.join(ROOT, "library/rejected/*room-*.jpg")) if os.path.basename(p)[5:7].isdigit()]
    nums += [int(x[-6:-4]) for x in glob.glob(os.path.join(ROOT, "library/rejected/*room-[0-9][0-9].jpg"))]
    n = max(nums + [0]) + 1; added = []
    with zipfile.ZipFile(z) as zf:
        for name in sorted(zf.namelist()):
            if not name.lower().replace("\\", "/").rsplit(".", 1)[-1] in ("jpg", "jpeg", "png", "webp"): continue
            try: im = Image.open(io.BytesIO(zf.read(name))).convert("RGB")
            except Exception: continue
            out = os.path.join(d, f"room-{n:02d}.jpg"); im.save(out, quality=95)
            ok, why = photo_ok(out)
            if not ok: reject(out, quiet=True); print(f"REJECTED {name}: {why}"); n += 1; continue
            added.append((os.path.basename(out), im.size)); n += 1
    for a, sz in added: print(a, f"{sz[0]}x{sz[1]}")
    print(len(added), "rooms added - LOOK at each one (real, sharp, tree, floor free); reject only a broken file")


def reject(f, quiet=False):
    """Moves ONLY this photo to library/rejected/. rule 31 Oct (Alex): it also leaves the current pick, so the next
    next-set re-picks only this kind and keeps the other photo (a bad room never burns the character)."""
    d = os.path.join(ROOT, "library/rejected"); os.makedirs(d, exist_ok=True)
    kind, name = os.path.basename(os.path.dirname(os.path.abspath(f))), os.path.basename(f)
    os.replace(f, os.path.join(d, kind + "-" + name))
    if not quiet:
        used = _used(); cur = used.get("current") or {}
        if name in used.get(kind, []): used[kind].remove(name)
        if cur.get(kind) == name:
            cur.pop(kind); used["current"] = cur
        _save_used(used)
        print("moved to library/rejected/ - run next-set again: it re-picks only the", kind, "and keeps the other photo")
    else:
        print("moved to library/rejected/")


def crop(f, out, l, t, r, b):
    from PIL import Image
    im = Image.open(f).convert("RGB"); w, h = im.size
    im.crop((int(float(l) * w), int(float(t) * h), int(float(r) * w), int(float(b) * h))).save(out, quality=95); print(out)


def compare(ref, ours, t0, t1, out):
    tmp = tempfile.mkdtemp(); n = max(1, round((float(t1) - float(t0)) * 10)); strips = []
    for i, f in enumerate((ref, ours)):
        s = os.path.join(tmp, f"{i}.jpg"); strips.append(s)
        run(["ffmpeg", "-v", "error", "-y", "-ss", str(t0), "-t", str(float(t1) - float(t0)), "-i", f, "-vf", f"fps=10,scale=110:-1,tile={n}x1", "-frames:v", "1", s])
    run(["ffmpeg", "-v", "error", "-y", "-i", strips[0], "-i", strips[1], "-filter_complex", "[0][1]scale2ref=iw:ih[a][b];[a][b]vstack", out])
    print(out, "- top = original, bottom = ours, one frame every 0.1 s from", t0, "s. Same action must be in the same column.")


def log(name, pairs):
    used = _used()
    rec = {"video": name}
    for p in pairs:
        k, _, v = p.partition("="); rec[k] = v
    used.setdefault("videos", []).append(rec); used.pop("current", None); _save_used(used); print("logged", rec)


def retime(ours, ref, out, end=None):
    """rule 31 Oct (Alex): the hook in the edit ends EXACTLY on the original's hook end. retime only TRIMS (or, when ours
    is shorter, holds the last frame) - it never changes speed, so the lips stay in sync - and it KEEPS the hook's sound.
    It prints our cuts next to the original's; an action that is early/late is fixed with `tools.py hold`, not here."""
    rc, oc = cuts(ref), cuts(ours)
    end = float(end) if end else duration(ref)
    od = duration(ours)
    print("cuts original:", [c for c in rc if c < end], " ours:", [c for c in oc if c < end + 0.5])
    for o in oc:
        if o >= end - 0.05: continue
        c = min(rc, key=lambda x: abs(x - o)) if rc else None
        if c is not None and abs(c - o) <= 1.0:
            print(f"  our cut {o:.2f} s vs original {c:.2f} s: {o - c:+.2f} s" + ("  -> off by more than 0.1 s: move it with `tools.py hold` on the still part before it" if abs(o - c) > 0.1 else "  OK"))
    has_a = run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index", "-of", "csv=p=0", ours]).stdout.strip()
    pad = max(0.0, end - od)
    vf = f"tpad=stop_mode=clone:stop_duration={pad + 0.1:.3f}" if pad > 0 else "null"
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", ours, "-vf", vf]
    cmd += (["-af", f"apad=pad_dur={pad + 0.1:.3f}", "-c:a", "aac", "-b:a", "192k"] if has_a else ["-an"])
    run(cmd + ["-t", f"{end:.3f}", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", out])
    print(out, f"- {duration(out):.2f} s (original hook end {end:.2f} s), speed x1.00, sound " + ("kept" if has_a else "none (the clip had none)")
          + (f"; last frame held {pad:.2f} s" if pad > 0 else ""))


def hold(f, out, ours_t, orig_t, words_json=None):
    """rule 31 Oct (Alex): Kling often makes the main action (unroll, reveal) EARLY. This lengthens the still part right
    before the action (forward / backward / forward of the calm frames, no visible jump) so the action starts on the
    original's second. A NEGATIVE shift (action LATE) removes that much of the still part instead. Sound: the room tone
    of the same frames is mirrored the same way (continuous, no click). Words are never cut: if a word (from
    <a3 folder>/audio3.json of OUR hook, or a loud sound) is inside the part that would change, it refuses."""
    t, T0 = float(ours_t), float(orig_t); delta = round(T0 - t, 3); d = duration(f)
    if abs(delta) < 0.04:
        print("already on time (|shift| < 0.04 s) - nothing to do"); return
    has_a = run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index", "-of", "csv=p=0", f]).stdout.strip()
    if delta > 0:
        w = min(t - 0.04, max(0.4, delta / 2))   # calm window just before the action
        if w < 0.15: sys.exit(f"REFUSED: the action starts at {t:.2f} s - not enough still picture before it to hold. Use a start frame + Kling image-to-video (HOOKS.md \"Start frame\").")
        zone = (t - w, t)
    else:
        w = -delta; zone = (t - w - 0.05, t - 0.05)
        if zone[0] < 0.05: sys.exit(f"REFUSED: only {t:.2f} s of picture before the action - cannot remove {w:.2f} s. Trim the start of the hook instead.")
    # words / loud sounds inside the zone -> refuse
    if words_json:
        js = json.load(open(os.path.join(words_json, "audio3.json")) if os.path.isdir(words_json) else open(words_json))
        hit = [x for x in js.get("part1_voice", {}).get("words", []) if x["start"] < zone[1] and x["end"] > zone[0]]
        if hit: sys.exit(f"REFUSED: words inside {zone[0]:.2f}-{zone[1]:.2f} s ({' '.join(x['word'] for x in hit)}) - holding would cut them. Regenerate the hook or move the action with a start frame.")
    elif has_a:
        import numpy as np
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
        x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768; n = len(x) // 160
        e = 20 * np.log10(np.sqrt((x[:n * 160].reshape(n, 160) ** 2).mean(1)) + 1e-9)
        z = e[int(zone[0] * 100):int(zone[1] * 100)]
        if len(z) and z.max() > np.median(e) + 18:
            sys.exit(f"REFUSED: a loud sound inside {zone[0]:.2f}-{zone[1]:.2f} s (a word?). Run audio3 on our hook and pass its folder as the 5th argument, or fix the hook another way.")
    a0, a1 = zone
    if delta > 0:
        pieces = [("f", 0, t)]; left = delta
        while left > 0.005:
            r = min(w, left / 2)
            pieces += [("r", t - r, t), ("f", t - r, t)]; left -= 2 * r
        pieces.append(("f", t, d))
    else:
        pieces = [("f", 0, a0), ("f", a1, d)]
    fc, vs, as_ = [], "", ""
    for i, (k, s0, s1) in enumerate(pieces):
        rv = ",reverse" if k == "r" else ""; ra = ",areverse" if k == "r" else ""
        fc.append(f"[0:v]trim={s0:.3f}:{s1:.3f},setpts=PTS-STARTPTS{rv}[v{i}]"); vs += f"[v{i}]"
        if has_a: fc.append(f"[0:a]atrim={s0:.3f}:{s1:.3f},asetpts=PTS-STARTPTS{ra}[a{i}]"); as_ += f"[a{i}]"
    fc.append(vs + f"concat=n={len(pieces)}:v=1:a=0,fps=30[v]")
    if has_a: fc.append(as_ + f"concat=n={len(pieces)}:v=0:a=1[a]")
    run(["ffmpeg", "-v", "error", "-y", "-i", f, "-filter_complex", ";".join(fc), "-map", "[v]"] + (["-map", "[a]", "-c:a", "aac", "-b:a", "192k"] if has_a else ["-an"])
        + ["-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", out])
    print(out, f"- {d:.2f} s -> {duration(out):.2f} s; the action now starts at {t + delta:.2f} s (was {t:.2f} s, original {T0:.2f} s); "
          + (f"held {delta:.2f} s of the calm part {a0:.2f}-{a1:.2f} s (forward/back/forward)" if delta > 0 else f"removed {-delta:.2f} s of the still part {a0:.2f}-{a1:.2f} s")
          + ". Check: `tools.py compare <original> " + out + "` around the action and a 10 fps sheet of the held part (no visible jump).")


def put(f, url):
    """rule 31 Oct (Alex): the upload PUT of the Higgsfield 'Uploading a local file' step, so nobody pastes curl lines."""
    ext = os.path.splitext(f)[1].lower()
    ctype = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp", ".mp4": "video/mp4", ".mov": "video/quicktime", ".mp3": "audio/mpeg", ".wav": "audio/wav"}.get(ext, "application/octet-stream")
    r = run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-X", "PUT", "-H", f"Content-Type: {ctype}", "--data-binary", "@" + f, url])
    print(r.stdout.strip() or "FAILED", "(200 = uploaded; now media_confirm)")


def cleantext(f, clean, out, boxes):
    if not still(f):   # rule 31 Oct (Alex): the patch would sit in the wrong place
        sys.exit("cleantext stopped: the camera moves (see above).")
    w, h = map(int, run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=width,height", "-of", "csv=p=0", f]).stdout.strip().split(","))
    fc, last = [f"[1:v]scale={w}:{h},split={len(boxes) // 4}" + "".join(f"[c{i}]" for i in range(len(boxes) // 4))], "0:v"
    for i in range(len(boxes) // 4):
        l, t_, r, b = (float(x) for x in boxes[i * 4:i * 4 + 4])
        cw, ch, cx, cy = int((r - l) * w) // 2 * 2, int((b - t_) * h) // 2 * 2, int(l * w), int(t_ * h)
        fc.append(f"[c{i}]crop={cw}:{ch}:{cx}:{cy}[p{i}]"); fc.append(f"[{last}][p{i}]overlay={cx}:{cy}[o{i}]"); last = f"o{i}"
    d = duration(f)
    if d <= 0: sys.exit("cleantext: cannot read the length of " + f)
    # -t = the clip's own length: with a looped photo and no sound track ffmpeg otherwise never stops (filled the disk, REPARATII #15)
    run(["ffmpeg", "-v", "error", "-y", "-i", f, "-loop", "1", "-t", f"{d:.3f}", "-i", clean, "-filter_complex", ";".join(fc), "-map", f"[{last}]", "-map", "0:a?", "-c:a", "copy", "-t", f"{d:.3f}", out], timeout=600)
    print(out, "- look at a frame: the text must be gone and nothing else covered (faces move into the box? make the box smaller)")


def frame_diffs(f):
    """mean absolute difference between consecutive frames (0-255), with times"""
    import numpy as np
    w, h = 96, 170
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-vf", f"scale={w}:{h},format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(np.int16)
    fps = len(fr) / duration(f)
    return [(round((i + 1) / fps, 2), float(np.abs(fr[i + 1] - fr[i]).mean())) for i in range(len(fr) - 1)], fps


def broll_check(f, motion, folder):
    os.makedirs(folder, exist_ok=True)
    ours, ref = cuts(f), cuts(motion)
    d = duration(f)
    diffs, fps = frame_diffs(f)
    rdiffs, _ = frame_diffs(motion)
    rv = sorted(v for _, v in rdiffs); rmed = rv[len(rv) // 2]
    ref_jumps = [t_ for t_, v in rdiffs if v > max(rmed * 3.5, rmed + 8)]
    scale = d / duration(motion)
    bounds = [0.0] + ours + [d]
    problems, safe = [], []
    if len(ours) != len(ref):
        problems.append(f"SHOT COUNT: ours has {len(ours) + 1} shots, the motion clip {len(ref) + 1} -> Kling merged/added a shot; look at the sheets, redo if a shot is missing or invented")
    for i in range(len(bounds) - 1):
        a, b = bounds[i], bounds[i + 1]
        inside = [v for t_, v in diffs if a + 0.12 < t_ < b - 0.12]
        if inside:
            med = sorted(inside)[len(inside) // 2]
            spikes = [t_ for t_, v in diffs if a + 0.12 < t_ < b - 0.12 and v > max(med * 3.5, med + 12)
                      and not any(abs(t_ - rt * scale) < 0.2 for rt in ref_jumps)]   # jumps the motion clip also has = their own jump cuts, fine
            if spikes:
                problems.append(f"shot {i + 1} ({a:.2f}-{b:.2f}s): sudden jump at {', '.join(str(s) for s in spikes[:5])}s -> possible glitch/morph, look at the sheet")
        sa, sb = round(a + 0.12, 2), round(b - 0.12, 2)
        safe.append((sa, sb))
        sheet_f = os.path.join(folder, f"shot{i + 1}.jpg")
        run(["ffmpeg", "-v", "error", "-y", "-ss", str(a), "-t", str(b - a), "-i", f, "-vf", "fps=6,scale=150:-1,tile=8x3", "-frames:v", "1", sheet_f])
    print("cuts ours:", ours, " motion clip:", ref)
    print("SAFE SEGMENTS (use only these in edit.json, 0.12 s away from every cut):", "  ".join(f"{a}-{b}" for a, b in safe))
    print("sheets:", ", ".join(f"{folder}/shot{i + 1}.jpg" for i in range(len(safe))))
    print("PROBLEMS:" if problems else "no automatic problems found - still LOOK at every sheet (person in every frame, face, hands, robe, pouches)")
    for p_ in problems: print(" -", p_)


def compare_audio(orig_folder, ours, end, out_folder):
    """rule 31 Oct (Alex): ADVISORY only. Runs audio3 on OUR hook and prints the original's and our word starts side
    by side, extra/missing words and dead-silent gaps (no music verdict - use spectro). It never decides a regeneration: YOU listen and look, and
    regenerate only for a real problem (wrong / missing / extra words you can hear, music, a word clearly > 0.3 s off)."""
    import re
    o = json.load(open(os.path.join(orig_folder, "audio3.json")))
    nv = o.get("no_voice") or not o["part1_voice"]["words"]
    subprocess.run([sys.executable, os.path.join(ROOT, "engine", "audio3.py"), ours, str(end), out_folder, ""] + (["--no-voice"] if nv else []), check=True)
    u = json.load(open(os.path.join(out_folder, "audio3.json")))
    norm = lambda w: {"3": "three", "2": "two", "1": "one"}.get(re.sub(r"[^a-z0-9']", "", w.lower()), re.sub(r"[^a-z0-9']", "", w.lower()))
    notes = []
    if nv:
        print("WORDS: the original has no speech (--no-voice) - nothing to compare; listen that ours has no voice either.")
    else:
        ow = [(norm(x["word"]), x["start"]) for x in o["part1_voice"]["words"]]; uw = [(norm(x["word"]), x["start"]) for x in u["part1_voice"]["words"]]
        used, rows = set(), []
        for w, t in ow:
            j = next((k for k, (w2, _) in enumerate(uw) if k not in used and w2 == w), None)
            if j is None: notes.append(f'"{w}" not found in ours'); rows.append(f"  {w:<10} original {t:5.2f}  ours  --"); continue
            used.add(j); dt = uw[j][1] - t
            rows.append(f"  {w:<10} original {t:5.2f}  ours {uw[j][1]:5.2f}  {dt:+.2f} s" + ("" if abs(dt) <= 0.15 else ("  later" if dt > 0 else "  earlier")))
            if abs(dt) > 0.3: notes.append(f'"{w}" {dt:+.2f} s')
        print("WORD STARTS (the tool can be wrong by ~0.1-0.2 s; Whisper may mishear words):"); print("\n".join(rows) or "  (no words)")
        extra = [w for k, (w, _) in enumerate(uw) if k not in used]
        if extra: notes.append(f"words only in ours: {extra}")
    gaps = [m["t"] for m in u["part3_background"] if m["kind"].startswith("SILENT")]
    if gaps: notes.append(f"dead-silent parts in ours at {gaps} s (fill with `tools.py roomtone`)")
    print("MUSIC: not judged by this tool (rule 31 Oct, Alex) - look at `tools.py spectro <our hook> <out.jpg>`: long horizontal lines + a regular beat = music.")
    print("ADVICE ONLY (rule 31 Oct, Alex): " + ("nothing stands out." if not notes else "; ".join(notes) + ".")
          + " LISTEN to our hook next to the original before you decide anything; regenerate only if YOU hear/see a real problem.")


def history(n="5"):
    f = os.path.join(ROOT, "state/used.json")
    vids = (json.load(open(f)) if os.path.exists(f) else {}).get("videos", [])
    if not vids:
        print("no videos yet - anything goes"); return
    for r in vids[-int(n):]:
        print(" | ".join(f"{k}: {v}" for k, v in r.items()))
    print("The next video must NOT repeat the hook concept, outfit, music cue or on-screen text of the last 3 above.")


if __name__ == "__main__":
    import signal
    if hasattr(signal, "SIGPIPE"): signal.signal(signal.SIGPIPE, signal.SIG_DFL)   # `| head` must not crash a command
    a = sys.argv[1:]
    if not a:
        print(__doc__); sys.exit()
    c = a[0]
    if c == "download": download(a[1], a[2])
    elif c == "sheet": sheet(a[1], a[2], a[3] if len(a) > 3 else "2")
    elif c == "frame": frame(a[1], a[2], a[3])
    elif c == "cuts": print(cuts(a[1]))
    elif c == "safe-end": safe_end(a[1])
    elif c == "fetch": fetch(a[1], a[2])
    elif c == "drop": drop(a[1])
    elif c == "fanwipe": fanwipe(a[1], a[2], a[3:])
    elif c == "next-set": next_set(next((x for x in a[1:] if not x.startswith("--")), ""), "--new" in a)
    elif c == "reject": reject(a[1])
    elif c == "photo-ok": print(*photo_ok(a[1]))
    elif c == "add-rooms": add_rooms(a[1])
    elif c == "crop": crop(*a[1:7])
    elif c == "compare": compare(*a[1:6])
    elif c == "log": log(a[1], a[2:])
    elif c == "retime": retime(a[1], a[2], a[3], a[4] if len(a) > 4 else None)
    elif c == "cleantext": cleantext(a[1], a[2], a[3], a[4:])
    elif c == "broll-check": broll_check(a[1], a[2], a[3])
    elif c == "cutjerk": cutjerk(a[1], a[2])
    elif c == "hold": hold(a[1], a[2], a[3], a[4], a[5] if len(a) > 5 else None)
    elif c == "put": put(a[1], a[2])
    elif c == "hookinput": hookinput(a[1], a[2], a[3])
    elif c == "roomtone": roomtone(a[1], a[2])
    elif c == "still": still(a[1], a[2] if len(a) > 2 else "0", a[3] if len(a) > 3 else None)
    elif c == "spectro": spectro(a[1], a[2], a[3] if len(a) > 3 else None)
    elif c == "compare-audio": compare_audio(a[1], a[2], a[3], a[4])
    elif c == "hook-audio":   # old name -> the ONE way: audio3
        print("hook-audio is an old name: running engine/audio3.py"); subprocess.run([sys.executable, os.path.join(ROOT, "engine", "audio3.py"), *a[1:5]])
    elif c == "audit-sound":   # old name -> compare-audio
        print("audit-sound is an old name: use compare-audio <original a3 folder> <our-hook.mp4> <hook end> <our a3 folder>")
    elif c in ("transcribe", "onsets", "speech-times", "vocals", "voice-mix", "place-voice", "voice-to-lips", "blur-for-sound", "cozy"):
        print(f"'{c}' was removed (rule 31 Oct, Alex): hook sound = Kling in the same generation; analysis = engine/audio3.py; check = compare-audio.")
    elif c == "history": history(a[1] if len(a) > 1 else "5")
    else: print(__doc__)
