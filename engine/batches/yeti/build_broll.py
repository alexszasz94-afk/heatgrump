# Lotul B-roll HeatYeti 1-5 (seturile reel 8-12 Grinch, alt clip de mișcare decât la Grinch).
import json, os
Y = json.load(open("yeti/media.json"))
REFS = Y["product_yeti_refs"]
P = lambda f: "\n".join(l for l in open(f"yeti/prompts/{f}").read().split("\n") if not l.startswith("#")).strip()
B1, B2, CZ = P("b1-motion-control.txt"), P("b2-motion-control.txt"), P("cozy-motion-control.txt")
SETS = {
 1: dict(char="866c23c9-a155-4fa8-8233-e79ec9884827", room="cce11644-a7b3-4d89-ae22-33cce899c145", g="m",
         outfit="a navy-and-grey plaid flannel pajama set (long-sleeve button shirt and matching pants) with white socks; his short dark curly hair exactly as in Image 1",
         b1="d8a474d2-e9b6-4a69-9d4c-5fabe1472435", b2="6243c22d-ed26-4df8-8a68-0d4ff29219bd", cozy="5f950f18-01c6-411c-81e6-16a13179cc05"),
 2: dict(char="fb33088d-cb17-4ee5-8db8-88fb9024caaa", room="9a114392-db4e-4d20-9344-9eab1dfff8b8", g="f",
         outfit="a cream-and-navy striped cotton pajama set (long-sleeve top and matching pants); her shoulder-length brown hair loose exactly as in Image 1, no bun",
         b1="8391f616-19ac-4af8-a80d-d7340f2027e2", b2="e9a9ed00-094d-4211-8b98-2cfdf6115920", cozy=None),
 3: dict(char="9f8ac5f2-99d1-4361-bc22-67a61f9ed1ba", room="bbaa476b-8a35-4ef4-ad9d-0dbd0374cf89", g="m",
         outfit="plain navy crewneck sweatshirt and soft pajama pants with a stars-and-stripes pattern, no text and no logos; his very short black hair exactly as in Image 1",
         b1="d8a474d2-e9b6-4a69-9d4c-5fabe1472435", b2="6731a06f-f6c0-48d9-a001-5047c85ca5d6", cozy="8042602c-c548-45de-aa77-6d42366e058e"),
 4: dict(char="1bb0e88e-0ffc-4239-a7f7-831b71173cd6", room="dcbd1956-9a92-48cc-9ec1-8046c458e43e", g="f",
         outfit="a cream cable-knit sweater and light-blue flannel pajama pants; her light-brown hair in the same loose messy updo as in Image 1",
         b1="8391f616-19ac-4af8-a80d-d7340f2027e2", b2="6243c22d-ed26-4df8-8a68-0d4ff29219bd", cozy="8042602c-c548-45de-aa77-6d42366e058e"),
 5: dict(char="d153a929-198a-4e1b-ae6a-18885d262e54", room="8c4704fd-7c4f-45ca-829d-aff912da31c0", g="f",
         outfit="a heather-grey waffle-knit lounge set (long-sleeve top and matching pants) with fluffy white socks; her wavy blonde shoulder-length hair loose exactly as in Image 1, no bun",
         b1="d8a474d2-e9b6-4a69-9d4c-5fabe1472435", b2="6731a06f-f6c0-48d9-a001-5047c85ca5d6", cozy="5f950f18-01c6-411c-81e6-16a13179cc05"),
}
base = {"model": "hf_mult_motion_control", "aspect_ratio": "9:16", "resolution": "1080p", "bitrate_mode": "high",
        "declined_preset_id": "24bae836-2c4a-48e0-89b6-49fcc0b21612"}
def req(idx, s, prompt, clip, dur):
    med = [{"value": s["char"], "role": "image_references"}, {"value": s["room"], "role": "image_references"}] + \
          [{"value": r, "role": "image_references"} for r in REFS] + [{"value": clip, "role": "video_references"}]
    return {"index": idx, "params": dict(base, duration=dur, medias=med, prompt=prompt.replace("<OUTFIT>", s["outfit"]))}
out = []
for n, s in SETS.items():
    out.append(req(n*10+1, s, B1, s["b1"], 4))
    out.append(req(n*10+2, s, B2, s["b2"], 5))
    if s["cozy"]: out.append(req(n*10+3, s, CZ, s["cozy"], 4))
json.dump(SETS, open("engine/batches/yeti/sets.json", "w"), indent=1)
json.dump(out, open("engine/batches/yeti/broll.json", "w"), indent=1, ensure_ascii=False)
print(len(out), [o["index"] for o in out], len(json.dumps(out)))
