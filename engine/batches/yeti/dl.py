# usage: python3 dl.py IDX=URL ...  -> descarcă în output/yeti-reelN/<clip>
import sys, subprocess, os
NAMES = {1: "b1.mp4", 2: "b2.mp4", 3: "cozy.mp4", 4: "placa-unboxing.png", 5: "unboxing.mp4", 6: "b1.mp4", 7: "cozy.mp4"}
HOOKS = {61: (2, "hooks/hook-v1.mp4"), 62: (2, "hooks/hook-v2.mp4"), 63: (3, "hooks/hook-v1.mp4"), 64: (3, "hooks/hook-v2.mp4"),
         65: (5, "hooks/hook-v1.mp4"), 66: (5, "hooks/hook-v2.mp4"), 67: (1, "hooks/placa-magazin.png"), 68: (4, "hooks/placa-hook.png"),
         69: (4, "hooks/hook-v1.mp4"), 70: (4, "hooks/hook-v2.mp4")}
for a in sys.argv[1:]:
    i, url = a.split("=", 1); i = int(i)
    if i in HOOKS: n, f = HOOKS[i]
    else: n, f = i // 10, NAMES[i % 10]
    out = f"output/yeti-reel{n}/{f}"; os.makedirs(os.path.dirname(out), exist_ok=True)
    subprocess.run(["curl", "-sSf", "-o", out, url], check=True); print(out)
