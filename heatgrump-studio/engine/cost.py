"""Calculator de cost HeatGrump Studio (prețuri reale verificate cu get_cost pe 1 nov 2026).
Folosire: python3 heatgrump-studio/engine/cost.py            -> tabel variante pentru 175/săptămână
          python3 heatgrump-studio/engine/cost.py 25 720p    -> cost pe zi pentru 25 videouri la 720p
"""
import sys

KLING = {"1080p": 3.25, "720p": 2.25}   # credite / secundă, Kling 4.0 (5 s 1080p = 16,25; 5 s 720p = 11,25)
GPT_IMAGE = 4.25                        # gpt_image_2_5, high, 9:16, 4k
RETRY = 1.3                             # ~30% regenerări (QA pică) — din istoricul reel 7-26

def per_video(res="1080p", hook_s=4, broll_res=None, reuse=5, broll_s=(4, 5, 4), frames=3):
    """hook nou per video + B-roll (B1, B2, cozy) refolosit la `reuse` videouri.
    Conector + telecomandă = clipuri fixe (0 credite). Montaj = ffmpeg local (0 credite)."""
    broll_res = broll_res or res
    hook = KLING[res] * hook_s * RETRY
    broll_set = (KLING[broll_res] * sum(broll_s) + GPT_IMAGE * frames) * RETRY
    return hook + broll_set / reuse, hook, broll_set

def table():
    print(f"{'varianta':44} {'cr/video':>8} {'cr/zi(25)':>10} {'cr/săpt(175)':>13}")
    rows = [
        ("A  1080p tot, hook 4 s, B-roll x5", dict(res="1080p", hook_s=4, reuse=5)),
        ("B  1080p tot, hook 3 s, B-roll x7", dict(res="1080p", hook_s=3, reuse=7)),
        ("C  hook 720p 4 s, B-roll 1080p x7 (RECOM.)", dict(res="720p", hook_s=4, broll_res="1080p", reuse=7)),
        ("D  720p tot, hook 3 s, B-roll x7", dict(res="720p", hook_s=3, reuse=7)),
        ("E  720p tot, hook 3 s, B-roll x10", dict(res="720p", hook_s=3, reuse=10)),
    ]
    for name, kw in rows:
        v, _, _ = per_video(**kw)
        print(f"{name:44} {v:8.1f} {v*25:10.0f} {v*175:13.0f}")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        n = int(sys.argv[1]); res = sys.argv[2] if len(sys.argv) > 2 else "720p"
        v, h, b = per_video(res=res, broll_res="1080p", hook_s=4, reuse=7)
        print(f"{n} videouri: ~{v*n:.0f} credite (hook {h:.1f}/video, set B-roll {b:.0f} refolosit x7)")
    else:
        table()
