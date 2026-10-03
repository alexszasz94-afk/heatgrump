"""Scrie output/reelN/final.json din lista de bucăți cu textul fiecăreia; timpii textelor se calculează singuri.
Folosire: python3 engine/build_final.py <N>   (planurile sunt în PLANS mai jos; reel nou = încă o intrare)
Bucăți consecutive cu același text = un singur text pe ecran.
"""
import sys, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FX = "output/fixed/"
# muzica = sunetul ORIGINAL al viralului din care e hook-ul (library/music/viral-<cod>.m4a), regula 3 oct
PLANS = {
 8: dict(music="library/music/viral-DdQw1jyKI63.m4a", parts=[
    ("hooks/hook.mp4", 0, 3.0, "The concept 🤮"),
    ("unboxing.mp4", 0, 2.4, "Vs…"), ("b1.mp4", 0, 0.75, "Vs…"),
    ("b2.mp4", 0.5, 4.7, "a hooded blanket you can WEAR 🧸"),
    (FX+"conector-barbat-taiat.mp4", 0, 1.5, "plug it in 🔌"),
    (FX+"telecomanda-barbat-taiat.mp4", 0, 2.4, "5 heat levels 🔥"),
    ("cozy.mp4", 0, 2.5, "never taking it off ❄️🎄")]),
 9: dict(music="library/music/viral-DdM8MhjyQwF.m4a", parts=[
    ("hooks/hook.mp4", 0, 2.6, "DO NOT show this to your mom 😳❄️"),
    ("unboxing.mp4", 0, 2.4, "DO NOT show this to your mom 😳❄️"), ("b1.mp4", 0, 1.3, "DO NOT show this to your mom 😳❄️"),
    ("b2.mp4", 0.6, 4.6, "DO NOT show this to your mom 😳❄️"),
    (FX+"conector-femeie-taiat.mp4", 0, 1.5, "plug it in 🔌"),
    (FX+"telecomanda-femeie-taiat.mp4", 0, 2.2, "5 heat levels 🔥"),
    ("cozy.mp4", 0, 2.5, "she'll never take it off 🥹")]),
 10: dict(music="library/music/viral-DdPQK-CPQ6r.m4a", parts=[
    ("hooks/magazin.mp4", 0, 2.4, "🧑: \"No gift is perfect\"\nMe: 😏"),
    ("unboxing.mp4", 0, 2.3, "🧑: \"No gift is perfect\"\nMe: 😏"), ("b1.mp4", 0, 0.8, "🧑: \"No gift is perfect\"\nMe: 😏"),
    ("b2.mp4", 0.6, 4.4, "🧑: \"No gift is perfect\"\nMe: 😏"),
    (FX+"conector-barbat-inchis-taiat.mp4", 0, 1.5, "plug it in 🔌"),
    (FX+"telecomanda-barbat-inchis-taiat.mp4", 0, 2.16, "5 heat levels 🔥"),
    ("cozy.mp4", 0, 2.2, "best gift ever 🎁")]),
 11: dict(music="library/music/viral-DdpIYs0trT0.m4a", parts=[
    ("hooks/hook.mp4", 0, 3.4, "DONT send this to your mom… 🎅🎄"),
    ("unboxing.mp4", 0, 2.3, "DONT send this to your mom… 🎅🎄"), ("b1.mp4", 0, 0.8, "DONT send this to your mom… 🎅🎄"),
    ("b2.mp4", 0.6, 4.4, "she'll never be cold again ❄️"),
    (FX+"conector-femeie-taiat.mp4", 0, 1.5, "plug it in 🔌"),
    (FX+"telecomanda-femeie-taiat.mp4", 0, 2.2, "5 heat levels 🔥"),
    ("cozy.mp4", 0, 2.5, "hood, sherpa inside & it heats up 🥹")]),
 12: dict(music="library/music/viral-DdX3q9kzIls.m4a", parts=[
    ("hooks/hook.mp4", 0, 2.6, "DONT show this to a Grinch girl 😳🎄"),
    ("unboxing.mp4", 0, 2.0, "DONT show this to a Grinch girl 😳🎄"), ("b1.mp4", 0, 1.0, "DONT show this to a Grinch girl 😳🎄"),
    ("b2.mp4", 0.8, 3.4, "DONT show this to a Grinch girl 😳🎄"),
    (FX+"conector-femeie-taiat.mp4", 0, 1.5, "plug it in 🔌"),
    (FX+"telecomanda-femeie-taiat.mp4", 0, 2.2, "5 heat levels 🔥"),
    ("cozy.mp4", 0, 1.4, "she's never taking it off 🥹")]),
 13: dict(music="library/music/viral-DeAepvaSfSf.m4a", parts=[
    ("hooks/hook.mp4", 0, 3.6, "Do NOT let a Grinch mom see this… 😩🎄"),
    ("unboxing.mp4", 0, 2.2, "Do NOT let a Grinch mom see this… 😩🎄"), ("b1.mp4", 0, 0.85, "Do NOT let a Grinch mom see this… 😩🎄"),
    ("b2.mp4", 0.8, 3.8, "Do NOT let a Grinch mom see this… 😩🎄"),
    (FX+"conector-femeie-taiat.mp4", 0, 1.5, "Do NOT let a Grinch mom see this… 😩🎄"),
    (FX+"telecomanda-femeie-taiat.mp4", 0, 2.2, "Do NOT let a Grinch mom see this… 😩🎄"),
    ("cozy.mp4", 0, 1.8, "Do NOT let a Grinch mom see this… 😩🎄")]),
 14: dict(music="library/music/viral-DeAgPjvyBF1.m4a", parts=[
    ("hooks/hook.mp4", 0, 4.3, "DO NOT show this to your sister 😳🎄"),
    ("unboxing.mp4", 0, 2.2, "DO NOT show this to your sister 😳🎄"), ("b1.mp4", 0, 1.2, "DO NOT show this to your sister 😳🎄"),
    ("b2.mp4", 0.6, 3.8, "DO NOT show this to your sister 😳🎄"),
    (FX+"conector-femeie-taiat.mp4", 0, 1.5, "DO NOT show this to your sister 😳🎄"),
    (FX+"telecomanda-femeie-taiat.mp4", 0, 2.2, "DO NOT show this to your sister 😳🎄"),
    ("cozy.mp4", 0, 1.2, "DO NOT show this to your sister 😳🎄")]),
 15: dict(music="library/music/viral-Dd9h35Ly2Ca.m4a", parts=[
    ("hooks/hook.mp4", 0, 3.5, "DO NOT let a cold-aholic see this 💚😳"),
    ("unboxing.mp4", 0, 2.3, "DO NOT let a cold-aholic see this 💚😳"), ("b1.mp4", 0, 0.85, "DO NOT let a cold-aholic see this 💚😳"),
    ("b2.mp4", 0.5, 3.8, "DO NOT let a cold-aholic see this 💚😳"),
    (FX+"conector-barbat-taiat.mp4", 0, 1.5, "DO NOT let a cold-aholic see this 💚😳"),
    (FX+"telecomanda-barbat-taiat.mp4", 0, 2.4, "DO NOT let a cold-aholic see this 💚😳"),
    ("cozy.mp4", 0, 2.5, "DO NOT let a cold-aholic see this 💚😳")]),
 16: dict(music="library/music/viral-DeAgyTpyKYj.m4a", parts=[
    ("hooks/hook.mp4", 0, 2.2, "DO NOT show this to a Grinch lover 😳🎄"),
    ("unboxing.mp4", 0, 1.8, "DO NOT show this to a Grinch lover 😳🎄"),
    ("b2.mp4", 1.0, 3.2, "DO NOT show this to a Grinch lover 😳🎄"),
    (FX+"conector-femeie-taiat.mp4", 0.1, 1.5, "DO NOT show this to a Grinch lover 😳🎄"),
    (FX+"telecomanda-femeie-taiat.mp4", 0, 2.2, "DO NOT show this to a Grinch lover 😳🎄"),
    ("cozy.mp4", 0, 1.3, "DO NOT show this to a Grinch lover 😳🎄")]),
 17: dict(music="library/music/viral-Dd6Ik80yLIE.m4a", parts=[
    ("hooks/hook.mp4", 1.8, 4.8, "Don't show this to a Grinch fan… 🥹💚"),
    ("unboxing.mp4", 0, 1.8, "Don't show this to a Grinch fan… 🥹💚"), ("b1.mp4", 0, 0.85, "Don't show this to a Grinch fan… 🥹💚"),
    ("b2.mp4", 1.0, 3.2, "Don't show this to a Grinch fan… 🥹💚"),
    (FX+"conector-femeie-taiat.mp4", 0, 1.5, "Don't show this to a Grinch fan… 🥹💚"),
    (FX+"telecomanda-femeie-taiat.mp4", 0, 2.2, "Don't show this to a Grinch fan… 🥹💚"),
    ("cozy.mp4", 0, 1.5, "Don't show this to a Grinch fan… 🥹💚")]),
}
def build(n):
    p = PLANS[n]; segs, texts, t = [], [], 0.0
    for f, a, b, txt in p["parts"]:
        f = f if f.startswith("output/") else f"output/reel{n}/{f}"
        segs.append({"file": f, "start": a, "end": b}); d = round(b - a, 3)
        if texts and texts[-1]["text"] == txt: texts[-1]["t1"] = round(t + d, 3)
        else: texts.append({"t0": round(t, 3), "t1": round(t + d, 3), "text": txt})
        t += d
    spec = {"out": f"output/reel{n}/reel{n}-FINAL.mp4", "segments": segs, "texts": texts, "music": p["music"], "music_start": 0, "orig_vol": 0.12}
    out = os.path.join(ROOT, f"output/reel{n}/final.json"); json.dump(spec, open(out, "w"), ensure_ascii=False, indent=1)
    print(out, round(t, 2), "s")
if __name__ == "__main__":
    for a in sys.argv[1:]: build(int(a))
