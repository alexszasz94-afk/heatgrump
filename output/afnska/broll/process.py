"""Descarca un B-roll generat, ii potriveste lumina/saturatia cu originalul r3 si face foaie QA.
Folosire: python3 process.py <nume> <url>"""
import subprocess, sys, statistics as st, os
HERE = os.path.dirname(os.path.abspath(__file__))
ORIG_Y, ORIG_SAT = 114.0, 9.5
name, url = sys.argv[1], sys.argv[2]
raw = os.path.join(HERE, f"{name}-raw.mp4"); out = os.path.join(HERE, f"{name}.mp4")
subprocess.run(["curl", "-sS", "-o", raw, url], check=True)
def stats(f):
    r = subprocess.run(["ffprobe", "-v", "error", "-f", "lavfi", "-i", f"movie={f},scale=360:-1,format=yuv420p,signalstats",
        "-show_entries", "frame_tags=lavfi.signalstats.YAVG,lavfi.signalstats.SATAVG", "-of", "csv=p=0"], capture_output=True, text=True).stdout
    v = [list(map(float, l.split(","))) for l in r.splitlines() if l.strip() and "" not in l.split(",")]
    return [st.mean(c) for c in zip(*v)]
y, sat = stats(raw)
br = max(-0.08, min(0.03, (ORIG_Y - y) / 255))
sf = max(0.72, min(1.0, (ORIG_SAT + 2) / sat))
vf = f"format=yuv420p,eq=brightness={br:.3f}:contrast=1.04:saturation={sf:.2f}:gamma=0.98,noise=alls=3:allf=t"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", raw, "-vf", vf, "-an", "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-movflags", "+faststart", out], check=True)
y2, s2 = stats(out)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", out, "-vf", "fps=2,scale=110:-1,tile=26x1", "-frames:v", "1", os.path.join(HERE, f"{name}-qa.png")], check=True)
print(f"{name}: inainte Y={y:.1f} sat={sat:.1f} -> dupa Y={y2:.1f} sat={s2:.1f} | {out}")
