#!/bin/bash
# Folosire: engine/qa_final.sh output/reelN/final.json strip.jpg — un cadru din mijlocul fiecărei bucăți din reelul final + ultimul cadru.
python3 - "$1" "$2" <<'PY'
import json,sys,subprocess
sp=json.load(open(sys.argv[1])); out=sp["out"]; t=0; ts=[]
for s in sp["segments"]:
    d=s["end"]-s["start"]; ts.append(t+d/2); t+=d
dur=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",out],capture_output=True,text=True).stdout)
ts.append(dur-0.05); fs=[]
for i,x in enumerate(ts):
    f=f"/tmp/qa_{i}.png"; subprocess.run(["ffmpeg","-y","-loglevel","error","-ss",str(min(x,dur-0.05)),"-i",out,"-frames:v","1","-vf","scale=270:-1",f]); fs.append(f)
subprocess.run(["ffmpeg","-y","-loglevel","error"]+sum([["-i",f] for f in fs],[])+["-filter_complex",f"hstack=inputs={len(fs)}",sys.argv[2]])
print(out, round(dur,2))
PY
