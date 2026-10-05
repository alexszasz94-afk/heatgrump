"""Feedback cu cifre reale de pe pagina ta (Meta Graph API): reels de pe Facebook Page + Instagram.
Rulare: python3 engine/feedback.py pull      → trage metricile ultimelor 50 de reel-uri în state/metrics.json
        python3 engine/feedback.py score     → leagă reel-urile de videourile noastre (după titlu/id) și dă scor hook-urilor
Cere în .env: META_PAGE_ID, META_IG_USER_ID, META_ACCESS_TOKEN.
"""
import sys, urllib.request, urllib.parse, json
from common import *

G = "https://graph.facebook.com/v21.0"

def get(path, params):
    params = dict(params); params["access_token"] = os.environ["META_ACCESS_TOKEN"]
    with urllib.request.urlopen(f"{G}/{path}?{urllib.parse.urlencode(params)}", timeout=60) as r: return json.loads(r.read())

def pull():
    load_env(); m = jload(STATE / "metrics.json", {"facebook": {}, "instagram": {}})
    # Facebook Page reels
    try:
        vids = get(f"{os.environ['META_PAGE_ID']}/video_reels", {"fields": "id,description,created_time,post_id", "limit": 50}).get("data", [])
        for v in vids:
            ins = get(f"{v['id']}/video_insights", {"metric": "blue_reels_play_count,fb_reels_total_plays,post_impressions_unique,post_video_avg_time_watched,post_video_social_actions,fb_reels_replay_count"})
            m["facebook"][v["id"]] = {"description": v.get("description"), "created": v.get("created_time"), "insights": {d["name"]: d["values"][0]["value"] for d in ins.get("data", []) if d.get("values")}}
    except Exception as e: log(f"Facebook: {e}")
    # Instagram reels
    try:
        media = get(f"{os.environ['META_IG_USER_ID']}/media", {"fields": "id,caption,media_type,media_product_type,timestamp,permalink", "limit": 50}).get("data", [])
        for x in [x for x in media if x.get("media_product_type") == "REELS"]:
            ins = get(f"{x['id']}/insights", {"metric": "plays,reach,saved,shares,comments,likes,total_interactions,ig_reels_avg_watch_time,ig_reels_video_view_total_time"})
            m["instagram"][x["id"]] = {"caption": x.get("caption"), "created": x.get("timestamp"), "permalink": x.get("permalink"), "insights": {d["name"]: d["values"][0]["value"] for d in ins.get("data", []) if d.get("values")}}
    except Exception as e: log(f"Instagram: {e}")
    jsave(STATE / "metrics.json", m); log(f"Metrici: FB {len(m['facebook'])} reels, IG {len(m['instagram'])} reels → state/metrics.json")

def score():
    """Scor per hook = medie ponderată (retenție, share-uri, save-uri per view) pe videourile care au folosit hook-ul."""
    m = jload(STATE / "metrics.json", {}); vids = jload(STATE / "videos.json", []); lib = jload(LIB / "hooks-library.json", {})
    def s(ins):
        plays = ins.get("plays") or ins.get("fb_reels_total_plays") or ins.get("blue_reels_play_count") or 0
        if not plays: return None
        watch = ins.get("ig_reels_avg_watch_time") or ins.get("post_video_avg_time_watched") or 0
        shares = ins.get("shares") or 0; saved = ins.get("saved") or 0
        return {"plays": plays, "avg_watch_ms": watch, "share_rate": shares / plays, "save_rate": saved / plays,
                "score": round(0.5 * min(watch / 8000, 1) + 0.3 * min(shares / plays * 100, 1) + 0.2 * min(saved / plays * 100, 1), 3)}
    by_hook = {}
    for v in vids:
        if not v.get("posted"): continue   # Claude Code completează v["posted"] = {"ig": id, "fb": id} după postare
        for plat, key in (("instagram", "ig"), ("facebook", "fb")):
            mid = v["posted"].get(key)
            if mid and mid in m.get(plat, {}):
                r = s(m[plat][mid]["insights"])
                if r: v["metrics"][plat] = r; by_hook.setdefault(v["hook"], []).append(r["score"])
    lib["scores"] = {k: {"n": len(x), "avg": round(sum(x) / len(x), 3)} for k, x in by_hook.items()}
    jsave(STATE / "videos.json", vids); jsave(LIB / "hooks-library.json", lib)
    top = sorted(lib["scores"].items(), key=lambda kv: kv[1]["avg"], reverse=True)[:10]
    print("TOP hook-uri (scor 0–1):"); [print(f"  {k}: {v['avg']} (n={v['n']})") for k, v in top]
    promote(vids, lib)

def promote(vids, lib):
    """Un hook nou (adapted/creative) devine DOVEDIT dacă, după promote_after_hours de la postare, scorul lui e peste mediana tuturor videourilor cu scor."""
    import datetime, statistics
    c = cfg()["proven"]; pv = jload(LIB / "proven-hooks.json", {"concepts": []}); have = {x["key"] for x in pv["concepts"]}
    scored = [(v, max(r["score"] for r in v["metrics"].values())) for v in vids if v.get("metrics")]
    if len(scored) < 4: return
    median = statistics.median(s for _, s in scored); now = datetime.datetime.now()
    for v, s in scored:
        old = (now - datetime.datetime.fromisoformat(v["date"])).total_seconds() / 3600 >= c["promote_after_hours"]
        if v["hook_kind"] in ("adapted", "creative") and old and s > median and v["hook"] not in have:
            h = (lib.get("used_in_reels") or {}).get(v["hook"], {})
            pv["concepts"].append({"key": v["hook"], "title": h.get("title", v["hook"]), "status": "promoted", "source": f"feedback {today()} (scor {s} > mediana {round(median,3)})",
                                   "method": "genjutsu", "motion_clip": h.get("video_id"), "template": "prompts/hook-image-template.txt",
                                   "scene": h.get("scene", ""), "lines": [h.get("line", ""), h.get("alt", "")], "robe_visible": False, "uses": []})
            have.add(v["hook"]); log(f"PROMOVAT la dovedite: {v['hook']} (scor {s})")
    jsave(LIB / "proven-hooks.json", pv)

if __name__ == "__main__":
    pull() if sys.argv[1] == "pull" else score()
