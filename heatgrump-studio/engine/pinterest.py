"""Finds new people and rooms on Pinterest (public search, no account, no API key).

  python3 engine/pinterest.py characters [how_many]   -> library/candidates/characters/
  python3 engine/pinterest.py rooms [how_many]        -> library/candidates/rooms/
  python3 engine/pinterest.py search "<your words>" characters|rooms [how_many]   -> custom search

Only big original photos (short side >= 1080 px) are kept. Every photo is listed in
library/candidates/<kind>/index.json with its pin link. Claude then LOOKS at them and moves only the
good ones to library/characters/ or library/rooms/ (skill find-sets).
If Pinterest blocks the search, the script says so: then ask the creator to add ~20 photos of each by hand.
"""
import json, os, sys, subprocess, urllib.parse, urllib.request, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUERIES = {
    "characters": [
        "natural selfie woman at home",
        "my christmas pajamas photo by the tree iphone",
        "candid photo woman no makeup cozy sweater",
        "christmas morning pajamas real photo woman living room",
    ],
    "rooms": [
        "our living room christmas tree ceiling fan sectional",
        "real home christmas living room photo before decorating sectional tv",
        "christmas tree up living room family home iphone photo",
        "my living room christmas decor tv stand sectional couch",
    ],
}
MIN_SHORT_SIDE = 720   # Alex's real phone photos are often 736-1200 px wide
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36",
           "Accept": "application/json", "X-Requested-With": "XMLHttpRequest", "X-Pinterest-PWS-Handler": "www/search/[scope].js"}


def search(q, want):
    """Returns [(pin_link, original_image_url)] for a Pinterest search, following pages until `want` results."""
    out, bookmarks = [], []
    while len(out) < want:
        data = {"options": {"query": q, "scope": "pins", "page_size": 25, "bookmarks": bookmarks}, "context": {}}
        url = ("https://www.pinterest.com/resource/BaseSearchResource/get/?source_url=" + urllib.parse.quote("/search/pins/?q=" + q)
               + "&data=" + urllib.parse.quote(json.dumps(data)))
        r = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=30).read())
        resp = r.get("resource_response", {})
        res = (resp.get("data") or {}).get("results") or []
        for p in res:
            img = ((p.get("images") or {}).get("orig") or {}).get("url")
            if img:
                out.append(("https://www.pinterest.com/pin/" + str(p.get("id")) + "/", img))
        bookmarks = [resp.get("bookmark")] if resp.get("bookmark") else []
        if not res or not bookmarks:
            break
    return out[:want]


def size(f):
    try:
        w, h = map(int, subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=width,height", "-of", "csv=p=0", f], capture_output=True, text=True).stdout.split(",")[:2])
        return min(w, h)
    except Exception:
        return 0


def run(kind, queries, n):
    out = os.path.join(ROOT, "library", "candidates", kind); os.makedirs(out, exist_ok=True)
    idx_f = os.path.join(out, "index.json"); idx = json.load(open(idx_f)) if os.path.exists(idx_f) else []
    got, blocked = 0, 0; day = datetime.date.today().isoformat()
    for q in queries:
        try:
            pins = search(q, n)
        except Exception as e:
            print("search failed:", q, e); blocked += 1; continue
        for pin, img in pins:
            if any(i["img"] == img for i in idx): continue
            f = os.path.join(out, f"{day}_{len(idx)+1:03d}.jpg")
            try:
                urllib.request.urlretrieve(img, f)
                if size(f) < MIN_SHORT_SIDE: os.remove(f); continue
                idx.append({"file": os.path.basename(f), "query": q, "pin": pin, "img": img}); got += 1
            except Exception:
                if os.path.exists(f): os.remove(f)
    json.dump(idx, open(idx_f, "w"), indent=1)
    if blocked == len(queries):
        print("PINTEREST_BLOCKED: ask the creator to add about 20 high-quality photos of women to library/characters/ and 20 of cozy Christmas rooms to library/rooms/ by hand.")
    else:
        print(f"{got} new photos in library/candidates/{kind}/ - now look at them and keep only the good ones.")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "search":
        run(a[2], [a[1]], int(a[3]) if len(a) > 3 else 30)
    elif a and a[0] in QUERIES:
        run(a[0], QUERIES[a[0]], int(a[1]) if len(a) > 1 else 15)
    else:
        print(__doc__)
