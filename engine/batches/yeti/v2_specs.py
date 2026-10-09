"""HeatYeti v2 (regulile princesscomfortt, 5 oct): construiește final.json pentru fiecare reel și îl randează.
Folosire: python3 engine/batches/yeti/v2_specs.py 1 2 7"""
import json, sys, subprocess, os
FX = "output/yeti-fixed/"
MUSIC = {"wham": ("library/music/xmas/wham-last-christmas.mp3", 0.43),
         "mariah": ("library/music/xmas/mariah-all-i-want.mp3", 42.4),
         "buble": ("library/music/xmas/buble-beginning.mp3", 32.43)}
# set B-roll per reel: (dir, b1 file, b1 end, conector, telecomanda, cozy end)
BROLL = {1: ("output/yeti-reel1/v2/", "b1.mp4", 1.2, "conector-barbat-taiat.mp4", "telecomanda-barbat-taiat.mp4", 1.5),
         2: ("output/yeti-reel2/", "b1-yeti-driving-443.mp4", 1.2, "conector-femeie-taiat.mp4", "../yeti-reel2/telecomanda-zoom.mp4", 2.5),
         3: ("output/yeti-reel3/v2/", "b1.mp4", 1.2, "conector-barbat-inchis-taiat.mp4", "telecomanda-barbat-inchis-taiat.mp4", 2.5),
         4: ("output/yeti-reel4/v2/", "b1.mp4", 1.2, "conector-femeie-taiat.mp4", "telecomanda-femeie-taiat.mp4", 2.5),
         5: ("output/yeti-reel5/v2/", "b1.mp4", 1.2, "conector-femeie-taiat.mp4", "telecomanda-femeie-taiat.mp4", 2.5)}
REELS = {
 1: dict(hook="output/yeti-reel1/v2/hook.mp4", hook_end=4.6, set=1, music="wham",   text="Don't let your girlfriend know 🤫❄️"),
 2: dict(hook="output/yeti-reel2/v2/hook.mp4", hook_start=1.0, hook_end=4.0, set=2, music="mariah", text="POV: you finally found it 🥹❄️"),
 3: dict(hook="output/yeti-reel3/v2/hook-c.mp4", hook_start=1.0, hook_end=5.0, set=3, music="buble", text="Best gift for him this year 🎁❄️"),
 4: dict(hook="output/yeti-reel4/v2/hook.mp4", hook_end=5.0, set=4, music="mariah", text="DO NOT show this to your mom 😳❄️"),
 5: dict(hook="output/yeti-reel5/v2/hook.mp4", hook_end=4.6, set=5, music="wham",   text="Meet the coziest thing you'll wear all winter 🎄"),
 6: dict(hook="output/yeti-reel6/hook.mp4", hook_end=5.0, set=4, music="buble",  text="3… 2… 1… 🥶➡️🥰"),
 7: dict(hook="output/yeti-reel7/hook.mp4", hook_end=5.0, set=2, music="mariah", text="They finally restocked it 😱❄️"),
 9: dict(hook="output/yeti-reel9/hook.mp4", hook_end=3.85, set=1, music="mariah", text="When it's -10° outside but you have this 🥶❄️"),
 10: dict(hook="output/yeti-reel10/hook.mp4", hook_end=4.0, set=5, music="buble", text="DO NOT show this to a cold-aholic 🥶💙"),
 11: dict(hook="output/yeti-reel11/hook.mp4", hook_end=5.0, set=2, music="wham", text="Employees said it sells out by noon 😳❄️"),
 8: dict(hook="output/yeti-reel8/hook.mp4", hook_end=5.0, set=3, music="wham",   text="Send this to someone who's always cold 🥶"),
}
def b2dir(s):  # B2 cu fața e în v2/ la fiecare set
    return f"output/yeti-reel{s}/v2/"
for n in map(int, sys.argv[1:]):
    r = REELS[n]; d, b1, b1e, con, tel, cze = BROLL[r["set"]]
    tel = os.path.normpath(FX + tel) if not tel.startswith("../") else os.path.normpath("output/yeti-reel2/telecomanda-zoom.mp4")
    segs = [{"file": r["hook"], "start": r.get("hook_start", 0), "end": r["hook_end"], "audio": True},
            {"file": d + b1, "start": 0, "end": b1e},
            {"file": b2dir(r["set"]) + "b2.mp4", "start": 0, "end": 5.0},
            {"file": FX + con, "start": 0, "end": 1.8},
            {"file": tel, "start": 0, "end": 2.2},
            {"file": b2dir(r["set"]) + "cozy.mp4", "start": 0, "end": cze}]
    total = sum(s["end"] - s["start"] for s in segs)
    m, ms = MUSIC[r["music"]]
    spec = {"out": f"output/yeti-reel{n}/yeti-reel{n}-v2-FINAL.mp4", "segments": segs,
            "texts": [{"t0": 0, "t1": round(total, 2), "text": r["text"]}],
            "music": m, "music_start": ms, "orig_vol": 0.9, "music_vol": 0.85}
    p = f"output/yeti-reel{n}/final-v2.json"; json.dump(spec, open(p, "w"), ensure_ascii=False, indent=1)
    subprocess.run(["python3", "engine/final.py", p], check=True)
