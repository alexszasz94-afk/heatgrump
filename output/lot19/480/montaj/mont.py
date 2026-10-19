"""Montaj de probă 480p: hook -> B-roll (B1+B2) -> conector -> telecomandă -> cozy, cu Bublé de la drop."""
import subprocess, sys, json
D = "/home/user/heatgrump/output/lot19/480"
FX = "/home/user/heatgrump/output/fixed"
MUSIC, DROP = "/home/user/heatgrump/library/music/xmas/buble-beginning.mp3", 35.38
def build(name, segs):
    args, fl = [], ""
    for i, (f, a, b) in enumerate(segs):
        args += ["-ss", str(a), "-t", str(b - a), "-i", f]
        fl += f"[{i}:v]scale=480:854:force_original_aspect_ratio=increase,crop=480:854,fps=30,setsar=1,setpts=PTS-STARTPTS[v{i}];"
    n = len(segs); total = sum(b - a for _, a, b in segs)
    args += ["-ss", str(DROP), "-i", MUSIC]
    fl += "".join(f"[v{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0[v];[{n}:a]atrim=0:{total},asetpts=PTS-STARTPTS,volume=0.85,afade=t=out:st={total-0.6}:d=0.6[a]"
    out = f"{D}/montaj/{name}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args, "-filter_complex", fl, "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest", out], check=True)
    print(name, round(total, 2))
CON, TEL = (f"{FX}/conector-femeie-taiat.mp4", 0, 1.5), (f"{FX}/telecomanda-femeie-taiat.mp4", 0, 2.2)
spec = json.loads(sys.argv[1])
build(spec["name"], [tuple(spec["hook"]), tuple(spec["broll"]), CON, TEL, tuple(spec["cozy"])])
