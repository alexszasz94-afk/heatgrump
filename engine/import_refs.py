"""Instalarea referințelor în contul Higgsfield al noului proprietar (folosit de skill-ul `instalare`).
  python3 engine/import_refs.py lista            → ce mai e de încărcat (fișier, tip, old_id), câte 20
  python3 engine/import_refs.py set <old> <new>  → notează ID-ul nou primit după media_confirm (se poate repeta: set a1 b1 a2 b2 ...)
  python3 engine/import_refs.py aplica <url_poza> → înlocuiește peste tot ID-urile vechi cu cele noi; <url_poza> = URL-ul unei poze încărcate
                                                   (din el se ia prefixul CDN pentru tablă)
  python3 engine/import_refs.py stare            → câte sunt încărcate / rămase
"""
import sys, json, re, pathlib
from common import ROOT, jload, jsave
MAN = ROOT / "referinte/manifest.json"
TEXT = (".json", ".md", ".txt", ".py", ".yaml", ".html")
SKIP = {"referinte/manifest.json"}

def items(): return jload(MAN, {"items": []})["items"]

def lista():
    rest = [i for i in items() if i.get("file") and not i.get("new_id")]
    for i in rest[:20]: print(json.dumps({"file": i["file"], "type": i["type"], "old_id": i["old_id"]}, ensure_ascii=False))
    print(f"# rămase: {len(rest)}")

def setid(pairs):
    d = jload(MAN, {}); by = {i["old_id"]: i for i in d["items"]}
    for old, new in zip(pairs[::2], pairs[1::2]): by[old]["new_id"] = new
    jsave(MAN, d); stare()

def stare():
    it = [i for i in items() if i.get("file")]; done = sum(1 for i in it if i.get("new_id"))
    print(f"încărcate {done}/{len(it)}")

def aplica(url):
    mp = {i["old_id"]: i["new_id"] for i in items() if i.get("new_id")}
    n = 0
    for f in ROOT.rglob("*"):
        rel = f.relative_to(ROOT).as_posix()
        if not f.is_file() or f.suffix not in TEXT or rel in SKIP or rel.startswith(("library/style-ref/", "library/fonts/")): continue
        s = f.read_text(errors="ignore"); t = s
        for old, new in mp.items(): t = t.replace(old, new)
        if t != s: f.write_text(t); n += 1
    m = re.match(r"(https://[^/]+/[^/]+/)", url or "")
    if m:
        b = jload(ROOT / "board/data.json", {"reels": []}); b["base_media"] = m.group(1); jsave(ROOT / "board/data.json", b)
        med = jload(ROOT / "library/media.json", {}); med.setdefault("higgsfield", {})["media_url_pattern"] = m.group(1) + "<media_id>.jpg"
        med["higgsfield"]["workspace"] = "contul proprietarului"; jsave(ROOT / "library/media.json", med)
    med = jload(ROOT / "library/media.json", {}); med["_instalare"] = "gata"; jsave(ROOT / "library/media.json", med)
    print(f"{len(mp)} ID-uri înlocuite în {n} fișiere")

if __name__ == "__main__":
    c = sys.argv[1] if len(sys.argv) > 1 else "stare"
    {"lista": lista, "stare": stare}.get(c, lambda: None)() if c in ("lista", "stare") else setid(sys.argv[2:]) if c == "set" else aplica(sys.argv[2] if len(sys.argv) > 2 else "")
