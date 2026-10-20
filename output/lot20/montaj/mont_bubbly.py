"""Montaj Bubblywarm (Szasz 20 oct): hook -> unboxing -> B-roll de Crăciun tăiat la telecomandă (sare direct la bule).
Sunet: pe hook sunetul hook-ului; după hook Bublé (drop-ul la începutul unboxing-ului) + sunetul clipurilor încet dedesubt.
Folosire: python3 mont_bubbly.py '{"name":..,"res":480,"segs":[[fișier,start,end],...]}'"""
import subprocess, sys, json
MUSIC, DROP = "/home/user/heatgrump/library/music/xmas/buble-beginning.mp3", 35.38
spec = json.loads(sys.argv[1]); R = spec.get("res", 480); W, H = (480, 854) if R == 480 else (1080, 1920)
segs = spec["segs"]; n = len(segs)
args, fl = [], ""
for i, (f, a, b) in enumerate(segs):
    args += ["-ss", str(a), "-t", str(b - a), "-i", f]
    fl += f"[{i}:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps=30,setsar=1,setpts=PTS-STARTPTS[v{i}];"
    fl += f"[{i}:a]aresample=48000,asetpts=PTS-STARTPTS,volume={1.0 if i == 0 else 0.45}[a{i}];"
total = sum(b - a for _, a, b in segs); hd = segs[0][2] - segs[0][1]
fl += "".join(f"[v{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0[v];"
fl += "".join(f"[a{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1[ca];"
args += ["-ss", str(DROP), "-i", MUSIC]; ms = int(hd * 1000)
fl += f"[{n}:a]atrim=0:{total - hd},asetpts=PTS-STARTPTS,volume=0.8,afade=t=out:st={max(0, total - hd - 0.8)}:d=0.8,adelay={ms}|{ms}[m];"
fl += "[ca][m]amix=inputs=2:duration=first:normalize=0[a]"
out = spec["out"]
subprocess.run(["ffmpeg", "-v", "error", "-y", *args, "-filter_complex", fl, "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-t", str(total), "-movflags", "+faststart", out], check=True)
print(out, round(total, 2))
