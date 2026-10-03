# Schimbă o bucată din final.json și mută textele în consecință. python3 retime.py N "<sufix fișier>" start end [file_nou]
import json, sys
n, suf, a, b = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
p = f"output/yeti-reel{n}/final.json"; d = json.load(open(p))
segs = d["segments"]; i = next(k for k, s in enumerate(segs) if s["file"].endswith(suf))
if len(sys.argv) > 5: segs[i]["file"] = sys.argv[5]
old_end = sum(s["end"] - s["start"] for s in segs[:i + 1]); old_start = old_end - (segs[i]["end"] - segs[i]["start"])
delta = (b - a) - (segs[i]["end"] - segs[i]["start"]); segs[i]["start"], segs[i]["end"] = a, b
for t in d["texts"]:
    for k in ("t0", "t1"):
        if t[k] >= old_end - 0.01: t[k] = round(t[k] + delta, 2)
json.dump(d, open(p, "w"), indent=1, ensure_ascii=False)
print(n, "total", round(sum(s["end"] - s["start"] for s in segs), 2))
