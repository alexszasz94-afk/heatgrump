"""Scrie output/reelN/final.json din lista de bucăți cu textul fiecăreia; timpii textelor se calculează singuri.
Folosire: python3 engine/build_final.py <N>   (planurile sunt în PLANS mai jos; reel nou = încă o intrare)
Bucăți consecutive cu același text = un singur text pe ecran.
"""
import sys, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FX = "output/fixed/"
# 5 oct: muzica = melodie de Crăciun de la Szasz (library/music/xmas), de la secunda folosită de competitori; doar hook-ul are sunet propriu (orig_vol 0.9)
# înainte (3 oct): muzica = sunetul ORIGINAL al viralului din care e hook-ul (library/music/viral-<cod>.m4a), regula 3 oct
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
    ("b1.mp4", 0, 0.85, "Do NOT let a Grinch mom see this… 😩🎄"),
    ("b2.mp4", 0, 5.0, "Do NOT let a Grinch mom see this… 😩🎄"),
    (FX+"conector-femeie-taiat.mp4", 0, 1.5, "Do NOT let a Grinch mom see this… 😩🎄"),
    (FX+"telecomanda-femeie-taiat.mp4", 0, 2.2, "Do NOT let a Grinch mom see this… 😩🎄"),
    ("cozy.mp4", 0, 1.8, "Do NOT let a Grinch mom see this… 😩🎄")]),
 14: dict(music="library/music/viral-DeAgPjvyBF1-ext.m4a", parts=[
    ("hooks/hook.mp4", 0, 5.0, "DO NOT show this to your sister 😳🎄"),
    ("b1.mp4", 0, 1.2, "DO NOT show this to your sister 😳🎄"),
    ("b2.mp4", 0.4, 4.8, "DO NOT show this to your sister 😳🎄"),
    (FX+"conector-femeie-taiat.mp4", 0, 1.5, "DO NOT show this to your sister 😳🎄"),
    (FX+"telecomanda-femeie-taiat.mp4", 0, 2.2, "DO NOT show this to your sister 😳🎄"),
    ("cozy.mp4", 0, 2.6, "DO NOT show this to your sister 😳🎄")]),
 15: dict(music="library/music/viral-DdLiUc7t1Yb-ext.m4a", parts=[
    ("hooks/hook-tigaie.mp4", 0, 4.85, "Every Grinch lover NEEDS this 😳🎄"),
    ("b1.mp4", 0, 0.85, "Every Grinch lover NEEDS this 😳🎄"),
    ("b2.mp4", 0, 4.0, "Every Grinch lover NEEDS this 😳🎄"),
    (FX+"conector-barbat-taiat.mp4", 0, 1.5, "Every Grinch lover NEEDS this 😳🎄"),
    (FX+"telecomanda-barbat-taiat.mp4", 0, 2.4, "Every Grinch lover NEEDS this 😳🎄"),
    ("cozy.mp4", 0, 2.2, "Every Grinch lover NEEDS this 😳🎄")]),
 16: dict(music="library/music/viral-DeAgyTpyKYj-ext.m4a", parts=[
    ("hooks/hook.mp4", 0, 2.2, "DO NOT show this to a Grinch lover 😳🎄"),
    ("unboxing.mp4", 0, 1.8, "DO NOT show this to a Grinch lover 😳🎄"),
    ("b2.mp4", 1.0, 5.0, "DO NOT show this to a Grinch lover 😳🎄"),
    (FX+"conector-femeie-taiat.mp4", 0.1, 1.5, "DO NOT show this to a Grinch lover 😳🎄"),
    (FX+"telecomanda-femeie-taiat.mp4", 0, 2.2, "DO NOT show this to a Grinch lover 😳🎄"),
    ("cozy.mp4", 0, 2.6, "DO NOT show this to a Grinch lover 😳🎄")]),
 17: dict(music="library/music/viral-Dd6Ik80yLIE.m4a", parts=[
    ("hooks/hook.mp4", 2.5, 4.8, "Don't show this to a Grinch fan… 🥹💚"),
    ("b1.mp4", 0, 0.85, "Don't show this to a Grinch fan… 🥹💚"),
    ("b2.mp4", 0, 5.0, "Don't show this to a Grinch fan… 🥹💚"),
    (FX+"conector-femeie-taiat.mp4", 0, 1.5, "Don't show this to a Grinch fan… 🥹💚"),
    (FX+"telecomanda-femeie-taiat.mp4", 0, 2.2, "Don't show this to a Grinch fan… 🥹💚"),
    ("cozy.mp4", 0, 1.5, "Don't show this to a Grinch fan… 🥹💚")]),
 18: dict(music="library/music/viral-DdmI16ft-rc-ext.m4a", parts=[
    ("hooks/hook-a2.mp4", 0, 1.4, "The problem 😩❄️"),
    ("hooks/hook-b.mp4", 0, 2.2, "The problem 😩❄️"),
    ("hooks/hook-b.mp4", 2.5, 4.0, "The problem 😩❄️"),
    ("unboxing.mp4", 0, 2.8, "Vs…"),
    ("b1.mp4", 0, 0.85, "Vs…"),
    ("b2.mp4", 0.3, 4.8, "Vs…"),
    (FX+"conector-femeie-taiat.mp4", 0, 1.5, "Vs…"),
    (FX+"telecomanda-femeie-taiat.mp4", 0, 2.2, "Vs…"),
    ("cozy.mp4", 0, 2.0, "Vs…")]),
 19: dict(music="library/music/viral-DdTC2suKD0l-ext.m4a", parts=[
    ("hooks/hook.mp4", 0, 2.3, "Christmas-holics don't walk… they RUN 🏃‍♀️🎄"),
    ("unboxing.mp4", 0, 2.6, "Christmas-holics don't walk… they RUN 🏃‍♀️🎄"),
    ("b1.mp4", 0, 1.3, "Christmas-holics don't walk… they RUN 🏃‍♀️🎄"),
    ("b2.mp4", 0, 3.8, "Christmas-holics don't walk… they RUN 🏃‍♀️🎄"),
    (FX+"conector-femeie-taiat.mp4", 0, 1.5, "Christmas-holics don't walk… they RUN 🏃‍♀️🎄"),
    (FX+"telecomanda-femeie-taiat.mp4", 0, 2.2, "Christmas-holics don't walk… they RUN 🏃‍♀️🎄"),
    ("cozy.mp4", 0, 2.0, "Christmas-holics don't walk… they RUN 🏃‍♀️🎄")]),
 20: dict(music="library/music/viral-DdSNI1ITcu6-ext.m4a", parts=[
    ("hooks/hook.mp4", 0, 3.4, "DON'T show this to a Grinch girl… 😳🎄"),
    ("b1.mp4", 0, 1.3, "DON'T show this to a Grinch girl… 😳🎄"),
    ("b2.mp4", 0, 4.8, "DON'T show this to a Grinch girl… 😳🎄"),
    (FX+"conector-femeie-taiat.mp4", 0, 1.5, "DON'T show this to a Grinch girl… 😳🎄"),
    (FX+"telecomanda-femeie-taiat.mp4", 0, 2.2, "DON'T show this to a Grinch girl… 😳🎄"),
    ("cozy.mp4", 0, 2.6, "DON'T show this to a Grinch girl… 😳🎄")]),
 21: dict(music="library/music/viral-DdK34IiqRx4-ext.m4a", parts=[
    ("hooks/hook.mp4", 0, 4.9, "POV: my boyfriend reviews the viral heated Grinch robe 😏🎄"),
    ("b1.mp4", 0, 1.3, "POV: my boyfriend reviews the viral heated Grinch robe 😏🎄"),
    ("b2.mp4", 0, 5.0, "POV: my boyfriend reviews the viral heated Grinch robe 😏🎄"),
    (FX+"conector-barbat-inchis-taiat.mp4", 0, 1.5, "POV: my boyfriend reviews the viral heated Grinch robe 😏🎄"),
    (FX+"telecomanda-barbat-inchis-taiat.mp4", 0, 2.16, "POV: my boyfriend reviews the viral heated Grinch robe 😏🎄"),
    ("cozy.mp4", 0, 2.0, "POV: my boyfriend reviews the viral heated Grinch robe 😏🎄")]),
 22: dict(music="library/music/viral-Dc-rr2WKSRR-ext.m4a", parts=[
    ("hooks/hook.mp4", 0, 3.9, "\"The perfect gift doesn't exi-\" 😳🎄"),
    ("b1.mp4", 0, 0.85, "\"The perfect gift doesn't exi-\" 😳🎄"),
    ("b2.mp4", 0, 3.8, "\"The perfect gift doesn't exi-\" 😳🎄"),
    (FX+"conector-femeie-taiat.mp4", 0, 1.5, "\"The perfect gift doesn't exi-\" 😳🎄"),
    (FX+"telecomanda-femeie-taiat.mp4", 0, 2.2, "\"The perfect gift doesn't exi-\" 😳🎄"),
    ("cozy.mp4", 0, 3.0, "\"The perfect gift doesn't exi-\" 😳🎄")]),
 190: dict(music="library/music/xmas/mariah-all-i-want.mp3", music_start=42.4, orig_vol=0.9, music_vol=0.85, parts=[
    ("hooks/hook-v2.mp4", 0, 4.0, "GRINCH ROBE DROP 😳🎄"),
    ("b1.mp4", 0, 1.3, "GRINCH ROBE DROP 😳🎄"),
    ("b2fast.mp4", 0, 4.37, "GRINCH ROBE DROP 😳🎄"),
    (FX+"conector-femeie-taiat.mp4", 0, 1.5, "GRINCH ROBE DROP 😳🎄"),
    (FX+"telecomanda-femeie-taiat.mp4", 0, 2.2, "GRINCH ROBE DROP 😳🎄"),
    ("cozy.mp4", 0, 2.4, "GRINCH ROBE DROP 😳🎄")]),
 200: dict(music="library/music/xmas/wham-last-christmas.mp3", music_start=0.43, orig_vol=1.0, music_vol=0.6, parts=[
    ("hooks/hook-v3b-321.mp4", 0, 4.6, "I made this for the cold-aholics.. 🤩💕"),
    ("b1.mp4", 0, 1.3, "I made this for the cold-aholics.. 🤩💕"),
    ("b2f-fast.mp4", 0, 4.4, "I made this for the cold-aholics.. 🤩💕"),
    (FX+"conector-femeie-taiat.mp4", 0, 1.5, "I made this for the cold-aholics.. 🤩💕"),
    (FX+"telecomanda-femeie-taiat.mp4", 0, 2.2, "I made this for the cold-aholics.. 🤩💕"),
    ("cozy.mp4", 0, 2.6, "I made this for the cold-aholics.. 🤩💕")]),
 210: dict(music="library/music/xmas/buble-beginning.mp3", music_start=32.43, orig_vol=0.9, music_vol=0.85, parts=[
    ("hooks/hook-v2.mp4", 0, 4.0, "Don't let your girlfriend know about this 🤭💕"),
    ("b1.mp4", 0, 1.3, "Don't let your girlfriend know about this 🤭💕"),
    ("b2fast.mp4", 0, 4.37, "Don't let your girlfriend know about this 🤭💕"),
    (FX+"conector-barbat-inchis-taiat.mp4", 0, 1.5, "Don't let your girlfriend know about this 🤭💕"),
    (FX+"telecomanda-barbat-inchis-taiat.mp4", 0, 2.16, "Don't let your girlfriend know about this 🤭💕"),
    ("cozy-v2.mp4", 0.8, 3.4, "Don't let your girlfriend know about this 🤭💕")]),
 220: dict(music="library/music/xmas/mariah-all-i-want.mp3", music_start=42.4, orig_vol=0.9, music_vol=0.85, parts=[
    ("hooks/hook-v2.mp4", 0, 3.3, "DO NOT show this to your mom 😱😬…"),
    ("b1.mp4", 0, 0.85, "DO NOT show this to your mom 😱😬…"),
    ("b2fast.mp4", 0, 4.37, "DO NOT show this to your mom 😱😬…"),
    (FX+"conector-femeie-taiat.mp4", 0, 1.5, "DO NOT show this to your mom 😱😬…"),
    (FX+"telecomanda-femeie-taiat.mp4", 0, 2.2, "DO NOT show this to your mom 😱😬…"),
    ("cozy.mp4", 0, 3.0, "DO NOT show this to your mom 😱😬…")]),
 180: dict(music="library/music/xmas/buble-beginning.mp3", music_start=32.43, orig_vol=0.9, music_vol=0.85, parts=[
    ("hooks/hook-v2.mp4", 0, 3.6, "Don't show this to a Grinch mom… 🥺✨"),
    ("b1.mp4", 0, 0.85, "Don't show this to a Grinch mom… 🥺✨"),
    ("b2fast.mp4", 0, 4.37, "Don't show this to a Grinch mom… 🥺✨"),
    (FX+"conector-femeie-taiat.mp4", 0, 1.5, "Don't show this to a Grinch mom… 🥺✨"),
    (FX+"telecomanda-femeie-taiat.mp4", 0, 2.2, "Don't show this to a Grinch mom… 🥺✨"),
    ("cozy.mp4", 0, 2.4, "Don't show this to a Grinch mom… 🥺✨")]),
}
def build(n):
    p = PLANS[n]; segs, texts, t = [], [], 0.0
    v2 = n >= 100; r = n // 10 if v2 else n   # planurile 180..220 = varianta 2 (5 oct) a reel-urilor 18..22
    for f, a, b, txt in p["parts"]:
        f = f if f.startswith("output/") else f"output/reel{r}/{f}"
        segs.append({"file": f, "start": a, "end": b}); d = round(b - a, 3)
        if texts and texts[-1]["text"] == txt: texts[-1]["t1"] = round(t + d, 3)
        else: texts.append({"t0": round(t, 3), "t1": round(t + d, 3), "text": txt})
        t += d
    spec = {"out": f"output/reel{r}/reel{r}-FINAL" + ("-v2" if v2 else "") + ".mp4", "segments": segs, "texts": texts, "music": p["music"], "music_start": p.get("music_start", 0), "orig_vol": p.get("orig_vol", 0.12), "music_vol": p.get("music_vol", 1.0)}
    out = os.path.join(ROOT, f"output/reel{r}/final" + ("-v2" if v2 else "") + ".json"); json.dump(spec, open(out, "w"), ensure_ascii=False, indent=1)
    print(out, round(t, 2), "s")
if __name__ == "__main__":
    for a in sys.argv[1:]: build(int(a))
