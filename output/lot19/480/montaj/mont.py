"""Montaj de probă 480p: hook -> B-roll (B1+B2) -> conector -> telecomandă -> cozy.
Sunet (Szasz 19 oct): pe hook se aude sunetul hook-ului ("hook_audio": "self" = sunetul generat de Seedance,
sau [fișier, start] = sunetul original al viralului copiat); Bublé pornește după hook, cu drop-ul la final de hook."""
import subprocess, sys, json
D = "/home/user/heatgrump/output/lot19/480"
FX = "/home/user/heatgrump/output/fixed"
MUSIC, DROP = "/home/user/heatgrump/library/music/xmas/buble-beginning.mp3", 35.38
def build(name, segs, hook_audio):
    args, fl = [], ""
    for i, (f, a, b) in enumerate(segs):
        args += ["-ss", str(a), "-t", str(b - a), "-i", f]
        fl += f"[{i}:v]scale=480:854:force_original_aspect_ratio=increase,crop=480:854,fps=30,setsar=1,setpts=PTS-STARTPTS[v{i}];"
    n = len(segs); total = sum(b - a for _, a, b in segs); hd = segs[0][2] - segs[0][1]
    fl += "".join(f"[v{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0[v];"
    args += ["-ss", str(DROP), "-i", MUSIC]; mi = n
    ms = int(hd * 1000)
    fl += f"[{mi}:a]atrim=0:{total - hd},asetpts=PTS-STARTPTS,volume=0.85,afade=t=out:st={max(0, total - hd - 0.6)}:d=0.6,adelay={ms}|{ms}[m];"
    if hook_audio:
        if hook_audio == "self":
            ha = "[0:a]"
        else:
            args += ["-ss", str(hook_audio[1]), "-i", hook_audio[0]]; ha = f"[{mi + 1}:a]"
        fl += f"{ha}atrim=0:{hd},asetpts=PTS-STARTPTS,afade=t=out:st={max(0, hd - 0.15)}:d=0.15[h];[h][m]amix=inputs=2:duration=longest:normalize=0[a]"
    else:
        fl += "[m]anull[a]"
    out = f"{D}/montaj/{name}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args, "-filter_complex", fl, "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-t", str(total), "-movflags", "+faststart", out], check=True)
    print(name, round(total, 2))
CON, TEL = (f"{FX}/conector-femeie-taiat.mp4", 0, 1.5), (f"{FX}/telecomanda-femeie-taiat.mp4", 0, 2.2)
spec = json.loads(sys.argv[1])
build(spec["name"], [tuple(spec["hook"]), tuple(spec["broll"]), CON, TEL, tuple(spec["cozy"])], spec.get("hook_audio"))
