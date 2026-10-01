"""Montaj: unește clipurile unui video în ordinea de montaj → output/videos/<id>.mp4 + <id>.txt (text CapCut, caption, muzică).
Rulare: python3 engine/assemble.py <plan.json>
plan.json = {"set":"set001","hook":{"key":"1101","kind":"problem","title":"...","line":"...","alt":"...","music":"...","caption":"..."},
             "clips":{"HOOK":"path/url","UNBOXING":"...","B1":"...","B2":"...","CONECTOR":"...","TELECOMANDA":"...","COZY":"..."}}
Clipurile pot fi URL-uri Higgsfield (se descarcă) sau fișiere locale.
"""
import sys, subprocess, urllib.request
from common import *
from rotation import register_video

def fetch(src, dst):
    if str(src).startswith("http"):
        urllib.request.urlretrieve(src, dst)
    else:
        dst.write_bytes(pathlib.Path(src).read_bytes())
    return dst

def duration(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)], capture_output=True, text=True)
    return float(r.stdout.strip() or 0)

def main(plan_path):
    c = cfg(); a = c["assemble"]; plan = jload(plan_path, None)
    if not plan: log("plan.json lipsă"); sys.exit(1)
    W, H = a["size"]; work = OUT / "work"; work.mkdir(parents=True, exist_ok=True)
    parts, timeline, t = [], [], 0.0
    for key in a["order"]:
        src = plan["clips"].get(key)
        if not src: continue
        raw = fetch(src, work / f"{key}.mp4")
        norm = work / f"{key}_n.mp4"
        # normalizează: 1080x1920, fps, audio -16 LUFS, AAC 48k
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(raw),
            "-vf", f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={a['fps']},format=yuv420p",
            "-af", f"loudnorm=I={a['loudness_lufs']}:TP=-1.5:LRA=11", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000", str(norm)], check=True)
        d = duration(norm); timeline.append((key, round(t, 2), round(t + d, 2))); t += d; parts.append(norm)
    lst = work / "list.txt"; lst.write_text("".join(f"file '{p}'\n" for p in parts))
    vids = jload(STATE / "videos.json", []); vid_id = f"v{len(vids)+1:04d}"
    out = OUT / "videos" / f"{vid_id}.mp4"; out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", "-movflags", "+faststart", str(out)], check=True)
    h = plan["hook"]
    notes = [f"VIDEO {vid_id} · set {plan['set']} · hook {h.get('key')} ({h.get('kind')}) · {h.get('title')}", "",
             "TIMELINE:"] + [f"  {k:<12} {s:>6.2f}s – {e:>6.2f}s" for k, s, e in timeline] + ["",
             "TEXT CAPCUT (EN):", f"  0.0–{timeline[0][2] if timeline else 4:.1f}s  {h.get('line','')}",
             f"  variantă: {h.get('alt','')}", "",
             "CAPTION (EN, o propoziție + hashtag-uri):", f"  {h.get('caption','')}", "",
             "MUZICĂ (idee):", f"  {h.get('music','')}", "",
             "TRECEREA: " + (h.get("bridge") or ""), ""]
    (OUT / "videos" / f"{vid_id}.txt").write_text("\n".join(notes))
    register_video(c, plan["set"], h.get("key"), h.get("kind"), out)
    log(f"Gata: {out} ({t:.1f}s) + {vid_id}.txt")

if __name__ == "__main__":
    main(sys.argv[1])
