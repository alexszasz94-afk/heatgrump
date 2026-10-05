"""Research automat pe Instagram + Facebook + Meta Ad Library, prin Apify.
Rulare:  python3 engine/research.py [--light]
Output:  library/research/<data>.json  (postările găsite, cu scor de outlier)
         library/clips/<id>.mp4        (top clipuri descărcate cu yt-dlp)
Apoi Claude Code rulează skill-ul `analyze-clip` pe fiecare clip nou.
"""
import sys, subprocess, statistics, time, urllib.request, urllib.parse, json
from common import *

APIFY = "https://api.apify.com/v2"

def apify_run(actor, payload, token, timeout=900):
    """Pornește un actor Apify și întoarce rezultatele (listă de dict)."""
    url = f"{APIFY}/acts/{urllib.parse.quote(actor, safe='')}/run-sync-get-dataset-items?token={token}&timeout={timeout}"
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout + 60) as r:
        return json.loads(r.read())

def norm(p, platform):
    """Aduce o postare la un format comun."""
    views = p.get("videoViewCount") or p.get("videoPlayCount") or p.get("playsCount") or p.get("viewsCount") or p.get("views") or 0
    return {
        "platform": platform,
        "id": p.get("id") or p.get("shortCode") or p.get("postId") or p.get("url"),
        "url": p.get("url") or p.get("postUrl"),
        "video_url": p.get("videoUrl") or p.get("video_url"),
        "owner": p.get("ownerUsername") or p.get("pageName") or p.get("user", {}).get("username"),
        "followers": p.get("ownerFollowersCount") or p.get("followersCount") or 0,
        "views": int(views or 0),
        "likes": int(p.get("likesCount") or p.get("likes") or 0),
        "comments": int(p.get("commentsCount") or p.get("comments") or 0),
        "shares": int(p.get("sharesCount") or p.get("shares") or 0),
        "caption": (p.get("caption") or p.get("text") or "")[:500],
        "posted_at": p.get("timestamp") or p.get("time") or p.get("date"),
        "hashtags": p.get("hashtags") or [],
    }

def score(posts, min_ratio, min_views):
    """Outlier = views >= min_ratio x media contului; plus viteză (views/zi)."""
    by_owner = {}
    for p in posts:
        by_owner.setdefault(p["owner"], []).append(p["views"])
    now = time.time()
    for p in posts:
        med = statistics.median(by_owner[p["owner"]]) if p["owner"] in by_owner else 0
        p["ratio"] = round(p["views"] / med, 2) if med else 0
        try:
            ts = time.mktime(time.strptime(str(p["posted_at"])[:19], "%Y-%m-%dT%H:%M:%S"))
            days = max((now - ts) / 86400, 0.5)
        except Exception:
            days = 7
        p["views_per_day"] = int(p["views"] / days)
        p["engagement"] = round((p["likes"] + 3 * p["comments"] + 5 * p["shares"]) / max(p["views"], 1), 4)
        p["outlier"] = p["views"] >= min_views and (p["ratio"] >= min_ratio or p["followers"] and p["views"] >= 3 * p["followers"])
    return sorted(posts, key=lambda p: (p["outlier"], p["views_per_day"]), reverse=True)

def download(url, out):
    out.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(["yt-dlp", "-q", "-o", str(out), "-f", "mp4/best", url], capture_output=True, text=True)
    return r.returncode == 0

def main(light=False):
    load_env(); c = cfg(); token = os.environ.get("APIFY_TOKEN")
    if not token:
        log("Lipsește APIFY_TOKEN în .env"); sys.exit(1)
    r = c["research"]; posts = []
    # Instagram: competitori (zilnic) + hashtag-uri (doar la rularea completă)
    if c["instagram_competitors"]:
        log(f"Instagram competitori: {len(c['instagram_competitors'])}")
        posts += [norm(p, "instagram") for p in apify_run("apify~instagram-scraper",
            {"directUrls": [f"https://www.instagram.com/{u}/" for u in c["instagram_competitors"]],
             "resultsType": "posts", "resultsLimit": 20, "onlyPostsNewerThan": f"{r['days_back']} days"}, token)]
    if not light and c["instagram_hashtags"]:
        log(f"Instagram hashtag-uri: {len(c['instagram_hashtags'])}")
        posts += [norm(p, "instagram") for p in apify_run("apify~instagram-hashtag-scraper",
            {"hashtags": c["instagram_hashtags"], "resultsLimit": 50}, token)]
    if c["facebook_pages"]:
        log(f"Facebook pagini: {len(c['facebook_pages'])}")
        posts += [norm(p, "facebook") for p in apify_run("apify~facebook-posts-scraper",
            {"startUrls": [{"url": u if u.startswith("http") else f"https://www.facebook.com/{u}"} for u in c["facebook_pages"]],
             "resultsLimit": 30, "onlyPostsNewerThan": f"{r['days_back']} days"}, token)]
    if not light and c["ad_library_keywords"]:
        log("Meta Ad Library")
        for kw in c["ad_library_keywords"]:
            try:
                ads = apify_run("curious_coder~facebook-ads-library-scraper",
                    {"urls": [{"url": f"https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country={c['ad_library_country']}&q={urllib.parse.quote(kw)}&media_type=video"}],
                     "count": 40}, token)
                for a in ads:
                    posts.append({"platform": "ad_library", "id": a.get("adArchiveID") or a.get("id"), "url": a.get("adLibraryUrl") or a.get("url"),
                                  "video_url": (a.get("videos") or [{}])[0].get("videoHdUrl") if a.get("videos") else a.get("videoUrl"),
                                  "owner": a.get("pageName"), "followers": 0, "views": 0, "likes": 0, "comments": 0, "shares": 0,
                                  "caption": (a.get("bodyText") or a.get("text") or "")[:500], "posted_at": a.get("startDate"),
                                  "days_running": a.get("daysRunning") or 0, "hashtags": [], "keyword": kw})
            except Exception as e:
                log(f"Ad Library {kw}: {e}")
    posts = [p for p in posts if p.get("id")]
    social = score([p for p in posts if p["platform"] != "ad_library"], r["outlier_min_ratio"], r["min_views"])
    ads = sorted([p for p in posts if p["platform"] == "ad_library"], key=lambda p: p.get("days_running", 0), reverse=True)
    for a in ads: a["outlier"] = a.get("days_running", 0) >= 21   # reclamă care rulează de 3+ săptămâni = câștigătoare
    result = {"date": today(), "light": light, "count": len(posts), "posts": social + ads}
    jsave(LIB / "research" / f"{today()}{'-light' if light else ''}.json", result)
    # descarcă top clipuri noi
    seen = jload(STATE / "seen_clips.json", {})
    n = 0
    for p in [p for p in result["posts"] if p["outlier"]][: r["max_clips_to_download"]]:
        if p["id"] in seen: continue
        out = LIB / "clips" / f"{p['platform']}_{str(p['id']).replace('/', '_')}.mp4"
        ok = download(p.get("video_url") or p["url"], out)
        seen[p["id"]] = {"date": today(), "file": str(out) if ok else None, "url": p["url"]}
        n += ok
    jsave(STATE / "seen_clips.json", seen)
    log(f"Gata: {len(posts)} postări, {sum(1 for p in result['posts'] if p['outlier'])} outlier-e, {n} clipuri noi descărcate în library/clips/")
    log("Următorul pas: în Claude Code scrie `analizează clipurile noi`.")

if __name__ == "__main__":
    main(light="--light" in sys.argv)
