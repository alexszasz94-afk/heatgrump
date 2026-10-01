"""Referințe de camere și de personaje de pe Pinterest, prin Apify (fără cont Pinterest).
Rulare: python3 engine/pinterest.py rooms|characters [cate]
Output: library/rooms/<data>_<n>.jpg  sau  library/char-inspiration/<data>_<n>.jpg  + index.json cu sursa fiecărei poze
Apoi Claude Code (skill new-sets) alege pozele bune, le încarcă în Higgsfield și:
 - camerele și personajele le folosește direct, pozele exacte, ca referință de cameră / de personaj (regula 1 oct).
"""
import sys, urllib.request, urllib.parse, json
from common import *
from research import apify_run

def main(kind, n=12):
    load_env(); c = cfg(); token = os.environ["APIFY_TOKEN"]
    queries = c["pinterest_queries"][kind]; out = LIB / ("rooms" if kind == "rooms" else "char-inspiration"); out.mkdir(parents=True, exist_ok=True)
    idx = jload(out / "index.json", []); got = 0
    for q in queries:
        try:
            pins = apify_run("apify~pinterest-scraper", {"searchQueries": [q], "maxItems": n}, token)
        except Exception as e:
            log(f"Pinterest {q}: {e}"); continue
        for p in pins:
            url = (p.get("images") or {}).get("orig", {}).get("url") or p.get("imageUrl") or p.get("image")
            if not url: continue
            f = out / f"{today()}_{len(idx)+1:03d}.jpg"
            try:
                urllib.request.urlretrieve(url, f); idx.append({"file": f.name, "query": q, "source": p.get("url") or p.get("link"), "img": url}); got += 1
            except Exception: pass
    jsave(out / "index.json", idx); log(f"{got} poze noi în {out}/ — Claude Code: alege-le pe cele bune (skill new-sets).")

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 12)
