---
name: check
description: Quality check + self-repair. Claude LOOKS at every start frame, every generated clip and the final video, finds anything that doesn't look real or breaks the rules, and fixes it alone (regenerate / re-trim / re-edit) before the creator ever sees it. Run automatically after every image, every video and before every delivery — never skip it, the creator should never have to point out a mistake.
---
You are the creator's quality control. Nothing goes to the creator until it passes. Never ask the creator "is this ok?" — decide yourself, fix it yourself.

## How to look
- Image: Read the jpg at full size. For faces/hands, also crop and zoom: `python3 engine/tools.py crop <img> <out> <l> <t> <r> <b>` and Read the crop.
- Clip: `python3 engine/tools.py sheet <clip> <out.jpg> 4` (whole clip) AND `sheet` at 10 fps on the last second (cut it first with ffmpeg `-ss <len-1>`), Read both. `safe-end` too.
- Final: `sheet` at 2 fps + `cuts`; compare cut times with the "cuts at" line montage printed.

## Checklist (every point, every time)
**Start frame (image)**
- Face = the character photo (same face shape, eyes, nose, hair colour/length). Different person → redo.
- Robe = refs one to one: colours, hood (shape, face/tiara/ears), trim, embroidery, pouches. Any invented detail → redo.
- Hands: 5 fingers each, natural grip, nothing fused. Objects have real size and weight.
- Composition matches the reference frame; place makes sense; no text; logos/signs that the reference had are still there (never removed), no invented ones.
- Light: soft and natural, true colours, no HDR/glow/orange cast, not CGI.

**Clip (video)**
- Starts on the start frame, no morph in the first frames.
- Movement natural, real weight, nothing melts, no objects merging with clothes, no flicker, no extra limbs, face stays the same the whole time.
- Robe stays correct in EVERY frame (hood always the right one, pouches correct in the B-roll, robe full length).
- End: no jump to a product/character photo, no sudden zoom, no fade → trim before it.
- Person in the FOREGROUND in every shot: nothing (table, plant, chair) between her and the camera → redo with the room photo without that object.
- Hook sound (CLAUDE.md rules 9d + 9e — made by Kling in the same generation, never another model): run `tools.py compare-audio output/<name>/a3 <our hook> <hook end> output/<name>/a3-ours` as ADVICE (rule 31 Oct, Alex: the tool never decides), then LISTEN next to the original: same words (from the Higgsfield analysis), no extra words, no music (look at `tools.py spectro <hook> <out.jpg>`: note lines + a beat = music), no dead-silent gaps (`tools.py roomtone`), each action sound on its action. Regenerate only for a real problem you hear (wrong/missing/extra words, music, a word clearly > 0.3 s off). The hook segment has `"audio": true`. A silent hook where the original speaks = redo.
- Copied hook: `tools.py compare` original vs ours on each key action — same column = same second (early/late main action → `hold`, see below; other differences → redo, HOOKS.md step 5).
- B-roll feet (rule 31 Oct, Alex): Feet/toes/socks/pajama legs are NOT a reason to redo (rule 31 Oct, Alex: "I don't mind the feet showing"): only obvious long bare feet on the floor > 0.5 s → cut those frames if the cut stays clean, otherwise deliver. Never regenerate a B-roll for feet.
- Object map (rule 9h): every object has the same role as in the original — props stay props (their blanket → our-character blanket, never our robe), packaging → our box with our logo, product → our robe. Wherever our robe appears it must read as a hooded robe (hood with face, sleeves, length); a cape, poncho or blanket → redo.
- Copied hook logic + logos (rule 9g): same reveal as the original (what is hidden stays hidden until the same second, what is there at the end is still there — e.g. the box on the table), and our brand/title printed where theirs is, readable and spelled right.
- Copied hook timing (rule 31 Oct, Alex): the main action (reveal, unroll, drop) starts on the original's second (`tools.py compare`, 10 fps). Early by > 0.3 s → `tools.py hold` (lengthens the still part before it; refuses if words would be cut); late by > 0.3 s → `hold` with the negative shift; then `retime` (keeps the sound, no speed change). Look at a 10 fps sheet of the held part: no visible jump. Long still part (> 2 s) before the action and hold looks wrong → start frame + image-to-video (HOOKS.md). Our music: quiet under the hook, full from the drop exactly on the hook → B-roll cut (rule 9n).
- B-roll: the person is in EVERY shot (never an empty robe, never a missing head in the back view) → else cut that shot or redo.
- B-roll v4/v5 (rule 31 Oct, Alex): the same shots as the motion clip (v4: back + hood, pockets, cozy SITTING; v5: sleeves, back, lying, cozy lying), the SAME woman (face and hair colour) in every shot, the room = our room photo with its REAL sofa (no invented furniture), the cozy shot WIDE on that sofa (never standing in front of it), no connector/remote/text anywhere. v4: `tools.py cutjerk` was run and no jerk frame is left at 2.7–3.5 s.

**Final video**
- 1080x1920, plays from 0 to the end, no black/frozen frames, no leftover flash of a reference photo at any cut.
- NO on-screen text in the video (rule 9): the suggested text is in text.txt and in the delivery message.
- Music: present, drop exactly on the hook → B-roll cut (rule 9n), the video never gets quieter after the hook, fades out at the end, no loud click at cuts.
- Order = PRODUCT.md edit order (hook → B-roll part 1 → connector → remote → cozy); the hook exactly as long as the original's; connector + remote = the fixed clips; nothing repeated by mistake; length 10–20 s.
- Variety: hook concept, outfit, music cue and text differ from the last 3 videos (`tools.py history`).

## Fixing (alone)
- Bad image → write the exact problem into the prompt as a fix ("her face is exactly the woman of the SECOND image", "the bundle is cream satin, separate from her dress", "both hands have five fingers") and regenerate. 
- Bad clip → first try a better trim; if the problem is in the middle, regenerate with the fix in the prompt (shorter action, "stays a separate object", "the face stays the same").
- `nsfw` / `ip_detected` → the steps in CLAUDE.md rule 10 and PRODUCT.md.
- Bad final → fix edit.json and run montage again.
- Max 3 tries per piece. If still not good: use the best version, and tell the creator in ONE line what is not perfect.

## Report
At delivery add a short "Checked:" line listing what you verified (face, robe, hands, trims, text, music) and what you fixed alone (e.g. "redid start frame 2 — wrong hood; trimmed hook 1 before a morph").
