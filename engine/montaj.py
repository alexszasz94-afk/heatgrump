"""Montaj rapid: lipește bucăți (fișier, start, sfârșit) într-un MP4 1080x1920 30fps, cu sunet.
Folosire: python3 engine/montaj.py out.mp4 file1:0:2.5 file2:0:1.3 ...
"""
import sys, subprocess, tempfile, os
out, parts = sys.argv[1], sys.argv[2:]
tmp = tempfile.mkdtemp(); lst = []
for i, p in enumerate(parts):
    f, a, b = p.rsplit(":", 2)
    seg = os.path.join(tmp, f"{i:02d}.mp4")
    has_a = subprocess.run(["ffprobe","-v","error","-select_streams","a","-show_entries","stream=index","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip()
    cmd = ["ffmpeg","-y","-loglevel","error","-ss",a,"-to",b,"-i",f]
    if not has_a: cmd += ["-f","lavfi","-i","anullsrc=r=48000:cl=stereo","-shortest"]
    cmd += ["-vf","scale=1080:1920,fps=30,format=yuv420p","-c:v","libx264","-crf","16","-preset","medium","-c:a","aac","-ar","48000","-ac","2",seg]
    subprocess.run(cmd, check=True); lst.append(f"file '{seg}'")
open(os.path.join(tmp,"l.txt"),"w").write("\n".join(lst))
subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",os.path.join(tmp,"l.txt"),"-c","copy",out], check=True)
print(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",out],capture_output=True,text=True).stdout.strip())
