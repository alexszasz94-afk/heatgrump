import json
S = json.load(open("engine/batches/yeti/sets.json"))
Y = json.load(open("yeti/media.json"))
strip = lambda f: "\n".join(l for l in open(f).read().split("\n") if not l.startswith("#")).strip()
tpl = strip("yeti/prompts/unboxing-image.txt")
tpl = tpl.replace("(dat 17 sept, se rulează CUVÂNT CU CUVÂNT)", "").strip()
box_floor = open("yeti/prompts/blocks/box-on-floor.txt").read().strip()
light = open("yeti/prompts/blocks/light-ultra-real.txt").read().strip()
robe = open("yeti/prompts/blocks/robe.txt").read().strip()
out = []
for n, s in S.items():
    p = tpl.replace("[INSERT prompts/blocks/box-on-floor.txt]", "").strip()
    first = "just-opened box. Candid phone photo style."
    p = p.replace(first, first + "\n\n" + box_floor)
    # rule 23 sept: box-on-floor block goes after the first sentence
    p = p.replace("hair and outfit, zero deviation", "hair, zero deviation")
    p += f"\n\nTHEIR CLOTHES — ABSOLUTE RULE: they wear {s['outfit']}. These clothes replace the clothes in @Image 1.\n\n" + light
    out.append({"index": int(n) * 10 + 4, "params": {"model": "gpt_image_2", "aspect_ratio": "9:16", "quality": "high", "resolution": "4k",
        "medias": [{"value": s["char"], "role": "image"}, {"value": Y["box"], "role": "image"}, {"value": s["room"], "role": "image"}], "prompt": p}})
s = S["2"]
bed = ("Photorealistic candid phone photo, vertical 9:16. IMAGE ROLES: Image 1 is the PERSON — her face, hair, age and build exactly as in Image 1. Image 2 is the ROOM — the same bed, bedding, window, Christmas tree and decor. Images 3-6 are THE ROBE.\n\n"
       "SCENE: she is lying in the bed from Image 2, propped up on the pillows, wearing the robe from Images 3-6 with the HOOD UP on her head, the Yeti face of the hood above her forehead, the shaggy white fur all around her, snuggled in, a soft content smile, eyes open, looking slightly past the camera. Her face is fully visible. The robe is open at the chest just enough to show "
       + s["outfit"] + " underneath. One Yeti-foot pocket peeks out from under the duvet at the end of the bed. Framing: from the end of the bed, slightly above, her whole upper body and the hood clearly visible.\n\n"
       + robe.replace("The robe is visible full length, down to the floor, never cropped.", "") + "\n\n" + light + "\n\nNo text, no logos, no watermark. No flash, no light source at the camera position.")
out.append({"index": 23, "params": {"model": "gpt_image_2", "aspect_ratio": "9:16", "quality": "high", "resolution": "4k",
    "medias": [{"value": s["char"], "role": "image"}, {"value": s["room"], "role": "image"}] + [{"value": r, "role": "image"} for r in Y["product_yeti_refs"]], "prompt": bed}})
json.dump(out, open("engine/batches/yeti/plates.json", "w"), indent=1, ensure_ascii=False)
print(json.dumps(out, ensure_ascii=False))
