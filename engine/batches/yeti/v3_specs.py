"""HeatYeti v3 (9 oct): reel 12-15 — hook Genjutsu de pe cele mai populare reel-uri + B-roll nou (referințe v2), look iPhone 17 Pro Max.
Folosire: python3 engine/batches/yeti/v3_specs.py 12 13 14 15   (clipurile în output/yeti-reelN/v3/: hook.mp4, b1.mp4, b2.mp4, cozy.mp4)"""
import json, sys, subprocess
FX = "output/yeti-fixed/"
MUSIC = {"wham": ("library/music/xmas/wham-last-christmas.mp3", 0.43),
         "mariah": ("library/music/xmas/mariah-all-i-want.mp3", 42.4),
         "buble": ("library/music/xmas/buble-beginning.mp3", 32.43)}
REELS = {
 12: dict(g="m", music="mariah", text="Him: *sets the heat to 60°* 🥶\nMe: 😏"),
 13: dict(g="f", music="wham",   text="Do NOT let a Yeti mom see this… 😳❄️"),
 14: dict(g="f", music="buble",  text="The concept 🤮… vs. this 😏❄️"),
 15: dict(g="f", music="mariah", text="Christmas-holics don't walk… they RUN 🏃‍♀️❄️"),
}
CUTS = json.load(open("engine/batches/yeti/v3_cuts.json"))   # tăieturile per reel, după QA
for n in map(int, sys.argv[1:]):
    r = REELS[n]; d = f"output/yeti-reel{n}/v3/"; c = CUTS[str(n)]
    who = "barbat" if r["g"] == "m" else "femeie"
    segs = [{"file": d + "hook.mp4", "start": c["hook"][0], "end": c["hook"][1], "audio": True},
            {"file": d + "b1.mp4", "start": c["b1"][0], "end": c["b1"][1]},
            {"file": d + "b2.mp4", "start": c["b2"][0], "end": c["b2"][1]},
            {"file": FX + f"conector-{who}-taiat.mp4", "start": 0, "end": 1.8},
            {"file": FX + f"telecomanda-{who}-taiat.mp4", "start": 0, "end": 2.2},
            {"file": d + "cozy.mp4", "start": c["cozy"][0], "end": c["cozy"][1]}]
    total = sum(s["end"] - s["start"] for s in segs)
    m, ms = MUSIC[r["music"]]
    spec = {"out": f"output/yeti-reel{n}/yeti-reel{n}-v3-FINAL.mp4", "segments": segs,
            "texts": [{"t0": 0, "t1": round(total, 2), "text": r["text"]}],
            "music": m, "music_start": ms, "orig_vol": 0.9, "music_vol": 0.85}
    p = f"output/yeti-reel{n}/final-v3.json"; json.dump(spec, open(p, "w"), ensure_ascii=False, indent=1)
    subprocess.run(["python3", "engine/final.py", p], check=True)
