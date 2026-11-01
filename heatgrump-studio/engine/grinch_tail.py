"""Grinch: pregătește partea de după hook (B-roll + conector + telecomandă + cozy), fără sunet.
Folosire: python3 engine/grinch_tail.py <folder-set>   (în folder: broll.mp4; variantă din state/broll-sets.json)
Scrie <folder>/tail.mp4 + <folder>/tail.json (secundele folosite)."""
import sys, os, json, subprocess
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "engine"))
import tools
d = os.path.abspath(sys.argv[1]); name = os.path.basename(d)
sets = {s["set"]: s for s in json.load(open(os.path.join(ROOT, "state/broll-sets.json")))}
var = sets[name]["variant"]
src = os.path.join(d, "broll.mp4")
if var == "v4":
    cut = os.path.join(d, "broll-cut.mp4"); tools.cutjerk(src, cut)
    c = tools.cuts(cut); cozy = [x for x in c if x > 4.5][0]
    segs = [(cut, 0.10, round(cozy - 0.12, 2))]
    tailcozy = (cut, round(cozy + (0.05 if cozy > 6.5 else 0.12), 2), 7.6 if cozy < 6.5 else 7.72)
else:
    c = tools.cuts(src); cozy = [x for x in c if x > 3.0][0]
    segs = [(src, 0.10, round(cozy - 0.12, 2))]
    tailcozy = (src, round(cozy + 0.12, 2), 5.9)
fx = os.path.join(ROOT, "products/grinch/fixed")
segs += [(os.path.join(fx, "connector-sofa-close-1.mp4"), 0.05, 1.70), (os.path.join(fx, "remote-sofa-close-1.mp4"), 0.3, 3.0), tailcozy]
F = "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1,format=yuv420p"
ZOOM_FIXED = 0.06   # Szasz 1 Nov: conector + telecomanda = zoom-in usor, lin (6% pe toata bucata)
COZY_CLOSE = 1.30   # Szasz 1 Nov: cozy mai de aproape (crop 1.30x, centrat pe ea)
args, fl = [], []
for i, (f, a, b) in enumerate(segs):
    args += ["-ss", str(a), "-to", str(b), "-i", f]
    d_ = b - a
    if i in (1, 2):   # conector, telecomanda: zoom-in lin, ease-out
        z = f"(1+{ZOOM_FIXED}*(1-pow(1-t/{d_:.3f},2)))"
        pre = f"fps=30,scale=w='2*trunc(540*{z})':h='2*trunc(960*{z})':eval=frame:flags=lanczos,crop=1080:1920,"
    elif i == 3:      # cozy: mai aproape (v5: ea e culcata in dreapta cadrului -> crop spre dreapta)
        fx_, fy_ = (0.95, 0.55) if var == "v5" else (0.5, 0.62)
        pre = f"crop=iw/{COZY_CLOSE}:ih/{COZY_CLOSE}:(iw-iw/{COZY_CLOSE})*{fx_}:(ih-ih/{COZY_CLOSE})*{fy_},"
    else:
        pre = ""
    fl.append(f"[{i}:v]{pre}{F}[v{i}]")
fl.append("".join(f"[v{i}]" for i in range(len(segs))) + f"concat=n={len(segs)}:v=1:a=0[v]")
subprocess.check_call(["ffmpeg", "-v", "error", "-y", *args, "-filter_complex", ";".join(fl), "-map", "[v]", "-an", "-c:v", "libx264", "-crf", "17", "-preset", "medium", os.path.join(d, "tail.mp4")])
json.dump({"variant": var, "cuts": c, "segments": [[os.path.relpath(f, ROOT), a, b] for f, a, b in segs]}, open(os.path.join(d, "tail.json"), "w"), indent=1)
print(name, var, "cuts", c, "-> tail.mp4", round(tools.duration(os.path.join(d, "tail.mp4")), 2), "s")
