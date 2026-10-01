"""Referințe de camere și de personaje de pe Pinterest, prin Apify (fără cont Pinterest).
Rulare: python3 engine/pinterest.py rooms|characters [cate]
Output: library/rooms/<data>_<n>.jpg  sau  library/char-inspiration/<data>_<n>.jpg  + index.json cu sursa fiecărei poze
Apoi Claude Code (skill new-sets) alege pozele bune, le încarcă în Higgsfield și:
 - camerele și personajele le folosește direct, pozele exacte, ca referință de cameră / de personaj (regula 1 oct).
"""
import sys, urllib.request, urllib.parse, json
from common import *
from research import apify_run

ACTOR = "fatihtahta~pinterest-scraper-search"   # vechiul apify~pinterest-scraper nu mai există (1 oct); ~0,004 $/pin, fără taxă de pornire

def image_url(p):
    """Cea mai mare poză pinimg din rezultat, oricum ar fi numite câmpurile."""
    urls = []
    def walk(x):
        if isinstance(x, dict): [walk(v) for v in x.values()]
        elif isinstance(x, list): [walk(v) for v in x]
        elif isinstance(x, str) and "pinimg.com" in x and x.split("?")[0].lower().endswith((".jpg", ".jpeg", ".png", ".webp")): urls.append(x)
    walk(p)
    rank = lambda u: (0 if "/originals/" in u else 1 if "/736x/" in u else 2)
    return sorted(urls, key=rank)[0] if urls else None

def main(kind, n=12):
    load_env(); c = cfg(); token = os.environ["APIFY_TOKEN"]
    queries = c["pinterest_queries"][kind]; out = LIB / ("rooms" if kind == "rooms" else "char-inspiration"); out.mkdir(parents=True, exist_ok=True)
    idx = jload(out / "index.json", []); got = 0
    for q in queries:
        try:
            pins = apify_run(ACTOR, {"queries": [q], "type": "all-pins", "limit": n}, token)
        except Exception as e:
            log(f"Pinterest {q}: {e}"); continue
        for p in pins:
            url = image_url(p)
            if not url or any(i["img"] == url for i in idx): continue
            f = out / f"{today()}_{len(idx)+1:03d}.jpg"
            try:
                urllib.request.urlretrieve(url, f); idx.append({"file": f.name, "query": q, "source": p.get("url") or p.get("link"), "img": url}); got += 1
            except Exception: pass
    jsave(out / "index.json", idx); log(f"{got} poze noi în {out}/ — Claude Code: alege-le pe cele bune (skill new-sets).")

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 12)
