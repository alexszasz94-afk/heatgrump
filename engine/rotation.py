"""Rotația seturilor (personaj + cameră + B-roll) și registrul videourilor.
Un set = {"id","char","room","gender","outfit","clips":{B1,B2,CONECTOR,TELECOMANDA,COZY,UNBOXING}, "uses":[video_ids]}
Rulare:
  python3 engine/rotation.py next            → ce set urmează (respectă gap și max_uses)
  python3 engine/rotation.py add <json>      → adaugă un set
  python3 engine/rotation.py status          → seturi active / obosite / de creat
  python3 engine/rotation.py plan            → planul zilei: 15 sloturi (5 dovedite / 5 adaptate / 5 creative) cu setul fiecăruia → state/plan-<data>.json
"""
import sys
from common import *

SETS = STATE / "sets.json"; VIDEOS = STATE / "videos.json"

def status(c):
    sets = jload(SETS, []); vids = jload(VIDEOS, [])
    mx = c["rotation"]["max_uses_per_set"]
    active = [s for s in sets if len(s["uses"]) < mx and s.get("clips")]
    tired = [s for s in sets if len(s["uses"]) >= mx]
    need = max(0, c["rotation"]["videos_per_day"] // 3 - len(active))
    return sets, vids, active, tired, need

def next_set(c):
    sets, vids, active, tired, need = status(c)
    gap = c["rotation"]["min_gap_between_uses"]
    recent = [v["set"] for v in vids[-gap:]]
    cands = [s for s in active if s["id"] not in recent]
    if not cands: return None
    # cel mai puțin folosit, apoi cel mai vechi folosit
    cands.sort(key=lambda s: (len(s["uses"]), s["uses"][-1] if s["uses"] else ""))
    return cands[0]

def register_video(c, set_id, hook_key, hook_kind, out_file):
    sets = jload(SETS, []); vids = jload(VIDEOS, [])
    vid = {"id": f"v{len(vids)+1:04d}", "date": today(), "set": set_id, "hook": hook_key, "hook_kind": hook_kind, "file": str(out_file), "posted": None, "metrics": {}}
    vids.append(vid)
    for s in sets:
        if s["id"] == set_id: s["uses"].append(vid["id"])
    jsave(SETS, sets); jsave(VIDEOS, vids); return vid

def plan_day(c):
    """Planul celor 15 sloturi de azi: 5 dovedite (concept + set), 5 adaptate, 5 creative — intercalate, seturile alternează, un concept dovedit nu se repetă."""
    import datetime
    mix = c["daily_mix"]; pv = jload(LIB / "proven-hooks.json", {"concepts": []})["concepts"]; vids = jload(VIDEOS, [])
    gap_days = c["proven"]["min_gap_days"]; today_d = datetime.date.today()
    def fresh(x):
        used = [v for v in vids if v["hook"] == x["key"]]
        return not used or (today_d - datetime.date.fromisoformat(used[-1]["date"])).days >= gap_days
    proven_ok = sorted([x for x in pv if fresh(x)], key=lambda x: len(x["uses"]))
    buckets = {"proven": [proven_ok[i % len(proven_ok)]["key"] if proven_ok else None for i in range(mix["proven"])],
               "adapted": [None] * mix["adapted"], "creative": [None] * mix["creative"]}
    order = []
    while any(buckets.values()):                      # dovedit, adaptat, creativ, dovedit, ... nu 5 la rând de același fel
        for k in ("proven", "adapted", "creative"):
            if buckets[k]: order.append((k, buckets[k].pop(0)))
    # alocarea seturilor, simulată în memorie (nu scrie în state/)
    sets = [dict(x, uses=list(x["uses"])) for x in jload(SETS, [])]; mx = c["rotation"]["max_uses_per_set"]; gap = c["rotation"]["min_gap_between_uses"]
    recent = [v["set"] for v in vids[-gap:]]; plan = []
    for i, (kind, key) in enumerate(order, 1):
        cands = [x for x in sets if len(x["uses"]) < mx and x.get("clips") and x["id"] not in recent[-gap:]]
        cands.sort(key=lambda x: (len(x["uses"]), x["uses"][-1] if x["uses"] else ""))
        sid = cands[0]["id"] if cands else None
        if sid: cands[0]["uses"].append(f"plan-{i}"); recent.append(sid)
        plan.append({"slot": i, "kind": kind, "hook": key, "set": sid,
                     "variants": c["proven"]["variants_proven_hooks"] if kind == "proven" else c["proven"]["variants_new_hooks"]})
    jsave(STATE / f"plan-{today()}.json", plan); return plan

if __name__ == "__main__":
    c = cfg(); cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "next":
        s = next_set(c); print(json.dumps(s, ensure_ascii=False) if s else "NICIUN SET DISPONIBIL — creează seturi noi (skill new-sets)")
    elif cmd == "plan":
        for p in plan_day(c): print(f"  {p['slot']:>2}. {p['kind']:<8} hook={p['hook'] or '(de propus)':<24} set={p['set'] or 'LIPSĂ'}  variante={p['variants']}")
    elif cmd == "add":
        sets = jload(SETS, []); s = json.loads(sys.argv[2]); s.setdefault("uses", []); s.setdefault("id", f"set{len(sets)+1:03d}"); sets.append(s); jsave(SETS, sets); print(s["id"])
    else:
        sets, vids, active, tired, need = status(c)
        print(f"seturi: {len(sets)} | active: {[s['id'] for s in active]} | obosite: {[s['id'] for s in tired]} | videouri: {len(vids)} | de creat: {need}")
