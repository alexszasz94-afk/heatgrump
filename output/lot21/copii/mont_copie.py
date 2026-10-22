"""Montaj pentru copiile reel-urilor lui Szasz (22 oct): Genjutsu (fără conector/telecomandă) + clipurile noastre fixe,
cu tăieturile, textul și audio-ul reel-ului original.
Folosire: python3 mont_copie.py spec.json
spec: {"gen": genjutsu.mp4, "split": secunda din gen unde se termină prima parte, "orig": reel.mp4 (audio),
       "conn": [start, dur], "tele": [start, dur], "texts": [[t0, t1, "text"], ...], "out": ...}
"""
import sys, json, os, subprocess, tempfile
sys.path.insert(0, "/home/user/heatgrump/engine")
import final

FIX = "/home/user/heatgrump/output/fixed/"
sp = json.load(open(sys.argv[1])); tmp = tempfile.mkdtemp()
gen, split = sp["gen"], sp["split"]
split2 = sp.get("split2", split)     # de unde reîncepe gen după telecomandă (sare peste cadre stricate)
gdur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", gen]))
cd, td = sp["conn"][1], sp["tele"][1]
conn_ss = max(0, 1.5 - cd)           # conectorul: păstrăm finalul (fișa intră complet)
segs = [(gen, 0, split), (FIX + "conector-femeie-taiat.mp4", conn_ss, cd), (FIX + "telecomanda-femeie-taiat.mp4", 0, td), (gen, split2, gdur - split2)]
parts = []
for i, (f, ss, d) in enumerate(segs):
    o = f"{tmp}/p{i}.mp4"
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(ss), "-t", str(d), "-i", f, "-an",
                    "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1,format=yuv420p",
                    "-c:v", "libx264", "-crf", "16", o], check=True)
    parts.append(o)
open(f"{tmp}/l.txt", "w").write("\n".join(f"file '{p}'" for p in parts))
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{tmp}/l.txt", "-c", "copy", f"{tmp}/v.mp4"], check=True)
inputs, chain, last = ["-i", f"{tmp}/v.mp4", "-i", sp["orig"]], "", "[0:v]"
for k, (t0, t1, txt) in enumerate(sp["texts"]):
    png = f"{tmp}/t{k}.png"; final.text_png(txt, png); inputs += ["-i", png]
    chain += f"{last}[{k + 2}:v]overlay=0:0:enable='between(t,{t0},{t1})'[o{k}];"; last = f"[o{k}]"
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", *inputs, "-filter_complex", chain.rstrip(";"), "-map", last, "-map", "1:a",
                "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", sp["out"]], check=True)
print(sp["out"])
