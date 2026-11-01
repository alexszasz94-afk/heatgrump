"""Grinch — videoul final dintr-un hook + un set de B-roll gata (fara generari noi la B-roll).
Folosire:
  python3 engine/grinch_video.py next                      -> ce set urmeaza (rotatie: cel mai putin folosit, niciodata acelasi de 2 ori la rand)
  python3 engine/grinch_video.py make <nume> <hook.mp4> <setNN> "<text pe ecran>" [melodie.mp3]
     hook.mp4 = hook-ul generat (cu sunetul lui); textul ramane pe tot videoul (sus), stil TikTok, cu emoji.
Rezultat: output/videos/<nume>/<nume>-FINAL.mp4 (+ edit.json). Seturile si folosirile: state/broll-sets.json."""
import sys, os, json, subprocess, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(ROOT)
SETS = os.path.join(ROOT, "state/broll-sets.json")
SONGS = {"mariah-all-i-want.mp3": 53.4, "buble-beginning.mp3": 35.35, "wham-last-christmas.mp3": 0.0, "let-it-go.mp3": 58.5}

def dur(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).decode())
def load(): return json.load(open(SETS))
def save(s): json.dump(s, open(SETS, "w"), indent=2, ensure_ascii=False)

def next_set():
    s = load(); hist = [u for x in s for u in x.get("uses", [])]
    last = max(hist, key=lambda u: u["date"])["set"] if hist else None
    ok = [x for x in s if x["set"] != last and x.get("status") == "ok"]
    return min(ok, key=lambda x: (len(x.get("uses", [])), x["set"]))

def next_song():
    s = load(); hist = sorted([u for x in s for u in x.get("uses", [])], key=lambda u: u["date"])
    recent = [u.get("song") for u in hist[-2:]]
    for k in SONGS:
        if k not in recent: return k
    return list(SONGS)[0]

def make(name, hook, set_id, text, song=None):
    text = text.replace("\\n", "\n"); s = load(); st = next(x for x in s if x["set"] == set_id)
    song = song or next_song(); drop = SONGS.get(os.path.basename(song), 0.0)
    tail = os.path.join(REPO, st["tail"]); hook = os.path.abspath(hook); hd = round(dur(hook), 2)
    out_dir = os.path.join(REPO, "output/videos", name); os.makedirs(out_dir, exist_ok=True)
    spec = {"out": os.path.join(out_dir, f"{name}-FINAL.mp4"), "fps": 30,
            "segments": [{"file": hook, "start": 0, "end": hd, "audio": True}, {"file": tail, "start": 0, "end": round(dur(tail), 2)}],
            "texts": [{"segs": [0, -1], "text": text, "size": 80, "y": 0.12}],
            "music": f"music/xmas/{os.path.basename(song)}", "music_start": max(0.0, round(drop - hd, 2)), "music_duck": hd}
    sp = os.path.join(out_dir, "edit.json"); json.dump(spec, open(sp, "w"), indent=1, ensure_ascii=False)
    subprocess.check_call([sys.executable, os.path.join(ROOT, "engine/montage.py"), sp], cwd=ROOT)
    st.setdefault("uses", []).append({"video": name, "date": datetime.datetime.now().isoformat(timespec="seconds"), "song": os.path.basename(song), "text": text, "set": set_id})
    save(s); print("GATA:", spec["out"])

if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "next":
        x = next_set(); print(json.dumps({k: x[k] for k in ("set", "variant", "character", "character_id", "room", "room_id", "outfit")}, indent=1), "\nsong:", next_song())
    elif a and a[0] == "make": make(*a[1:6])
    else: print(__doc__)
