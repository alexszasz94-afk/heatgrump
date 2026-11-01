"""HeatGrump Studio — rotație seturi + montaj automat.
  python3 heatgrump-studio/engine/studio.py next              -> următorul set + clipuri fixe + melodie
  python3 heatgrump-studio/engine/studio.py plan 25           -> planul unei zile (25 sloturi)
  python3 heatgrump-studio/engine/studio.py montaj <id> <hook.mp4> "<text>" [set]
"""
import sys, json, os, subprocess, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STATE = os.path.join(ROOT, "heatgrump-studio/sets.json")
FIXED = {("barbat", "deschis"): ("conector-barbat-taiat", "telecomanda-barbat-taiat"),
         ("femeie", "deschis"): ("conector-femeie-taiat", "telecomanda-femeie-taiat"),
         ("barbat", "inchis"): ("conector-barbat-inchis-taiat", "telecomanda-barbat-inchis-taiat")}

def load(): return json.load(open(STATE))
def save(s): json.dump(s, open(STATE, "w"), indent=2, ensure_ascii=False)

def dur(f):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).decode())

def pick(s, last=None):
    ok = [x for x in s["sets"] if len(x["uses"]) < s["max_uses"] and x["id"] != last]
    if not ok: return None
    return min(ok, key=lambda x: len(x["uses"]))

def fixed(st):
    k = (st["gender"], st["skin"])
    if k not in FIXED: raise SystemExit(f"Lipsește varianta fixă pentru {k} — se face o dată din placa aprobată (PRODUCT.md).")
    return [os.path.join("output/fixed", n + ".mp4") for n in FIXED[k]]

def cmd_next():
    s = load(); last = s["videos"][-1]["set"] if s["videos"] else None
    st = pick(s, last)
    if not st: print("Toate seturile sunt consumate → fă seturi noi (recipes/broll-grinch.md)."); return
    m = s["music"][len(s["videos"]) % len(s["music"])]
    print(json.dumps({"set": st["id"], "dir": st["dir"], "gender": st["gender"], "skin": st["skin"],
                      "fixed": fixed(st), "music": m, "quality": st["quality"]}, indent=2, ensure_ascii=False))

def cmd_plan(n):
    s = load(); last = s["videos"][-1]["set"] if s["videos"] else None
    used = {x["id"]: len(x["uses"]) for x in s["sets"]}; out = []
    for i in range(n):
        ok = [x for x in s["sets"] if used[x["id"]] < s["max_uses"] and x["id"] != last]
        if not ok: out.append({"slot": i + 1, "set": "DE CREAT"}); last = None; continue
        st = min(ok, key=lambda x: used[x["id"]]); used[st["id"]] += 1; last = st["id"]
        out.append({"slot": i + 1, "set": st["id"]})
    new = sum(1 for o in out if o["set"] == "DE CREAT")
    for o in out: print(f"{o['slot']:2}. set {o['set']}")
    print(f"\nSeturi de B-roll noi necesare azi: ~{-(-new // s['max_uses'])}")

def cmd_montaj(vid, hook, text, set_id=None):
    s = load(); last = s["videos"][-1]["set"] if s["videos"] else None
    st = next((x for x in s["sets"] if x["id"] == set_id), None) if set_id else pick(s, last)
    m = s["music"][len(s["videos"]) % len(s["music"])]
    con, tel = fixed(st); d = st["dir"]; hd = dur(os.path.join(ROOT, hook))
    segs = [{"file": hook, "start": 0, "end": hd, "audio": True},
            {"file": f"{d}/b1.mp4", "start": 0, "end": 1.3},
            {"file": f"{d}/b2fast.mp4", "start": 0, "end": dur(os.path.join(ROOT, d, "b2fast.mp4"))},
            {"file": con, "start": 0, "end": dur(os.path.join(ROOT, con))},
            {"file": tel, "start": 0, "end": dur(os.path.join(ROOT, tel))},
            {"file": f"{d}/cozy.mp4", "start": 0, "end": 2.5}]
    total = sum(x["end"] - x["start"] for x in segs)
    out = f"output/studio/{vid}/{vid}-FINAL.mp4"; os.makedirs(os.path.join(ROOT, os.path.dirname(out)), exist_ok=True)
    spec = {"out": out, "segments": segs, "texts": [{"t0": 0, "t1": total, "text": text}],
            "music": m["file"], "music_start": max(0.0, m["drop"] - hd), "music_vol": 0.85, "orig_vol": 0.9}
    sp = os.path.join(ROOT, f"output/studio/{vid}/final.json"); json.dump(spec, open(sp, "w"), indent=2, ensure_ascii=False)
    subprocess.check_call([sys.executable, os.path.join(ROOT, "engine/final.py"), sp], cwd=ROOT)
    st["uses"].append(vid)
    s["videos"].append({"id": vid, "set": st["id"], "hook": hook, "text": text, "music": m["file"], "date": str(datetime.date.today())})
    save(s); print("GATA:", out)

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "next": cmd_next()
    elif a[0] == "plan": cmd_plan(int(a[1]) if len(a) > 1 else 25)
    elif a[0] == "montaj": cmd_montaj(*a[1:5])
    else: print(__doc__)
