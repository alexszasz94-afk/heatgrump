---
name: product-video-recast
description: Recast a supplied product or UGC video with Genjutsu using product-aware shot analysis, the user's visual benchmark, and carefully selected Pinterest avatar and background references. Preserve the requested asset source and execute authorized production. Research-only requests stop at the board; exclude ordinary model questions and unrelated editing.
---

# Product video recast

Turn source footage into a product-aware recasting plan and, when requested, a tested finished video. Match the user's visual standard as well as the scene's physical requirements. Read [research-and-board.md](references/research-and-board.md) for sourcing and candidate selection, and [genjutsu-production.md](references/genjutsu-production.md) for execution. For Esteban's work, read [esteban-visual-standard.md](references/esteban-visual-standard.md), which records his Miro benchmark and explicit sourcing preference; a newer brief overrides that profile.

## Scope and intake

Determine whether the user requested research, a review board, or production. Building or installing this skill does not itself authorize running it or spending generation credits. Preserve existing user choices, approval, and budgets; do not repeatedly ask about settled decisions.

Use the supplied source video and any existing product/brand assets. Ask only for information that materially changes the work: an unreadable product, intended replacement product, required avatar, or whether the dialogue must change. Continue independent visual research while a needed answer is pending. If no video is supplied, research can proceed from a product brief, but do not invent a shot analysis.

Resolve what the references are meant to be: exact photographs from Pinterest, user-supplied images, or newly generated assets. "Take them from Pinterest" means select and use those actual images, not generate substitutes inspired by them. Do not silently switch sourcing modes or carry rejected references into a later prompt. A request to update this skill does not itself request a new video generation.

Resolve the text policy separately from motion preservation. For Esteban, default to **no captions, subtitles, hook text, emoji stickers or other editorial text overlays**, including overlays already burned into the source. Do not carry forward an older prompt that says to preserve source captions. Add text only when a newer explicit request calls for it; see the text handling in [genjutsu-production.md](references/genjutsu-production.md).

When the user provides a Miro board or other visual benchmark, inspect its examples and annotations before choosing assets. Translate them into a short visual brief: creator presentation, light, camera/framing, background organization, product placement and hook. Distinguish visible evidence from the board author's opinions. If access fails, say what is missing rather than claiming to have absorbed the board.

## Inspect the source

Inspect actual footage using available video tools or local frame extraction and playback. Read duration, dimensions, frame rate, and audio streams with a media probe when available. Sample every shot and inspect transitions and interactions closely; contact sheets alone do not establish motion, speech, or exact cut times. Distinguish visible observations from inferred actions and unchecked audio.

Identify product category, readable brand/model, use context, and confidence. Use packaging, visible application, and user-provided product pages; do not infer ingredients, benefits, audience demographics, or claims from appearance. A generic category can support provisional research while exact identity is unresolved.

Create a shot map with stable IDs and measured time ranges. For each shot record:

- Source setting, framing, camera movement, person(s), and action.
- Product visibility, hand contact, support surfaces, occlusions, mirrors, and physical requirements.
- Target location ID, avatar ID, reference IDs, and intended replacements.
- What must remain: product, motion, timing, camera, clothing, dialogue, music, and captions only when explicitly requested.
- Source text overlays to remove or exclude under the agreed text policy.
- Uncertainties and likely failure points.

One location can span several shots. Different camera angles do not automatically require different environments. Record editorial cuts independently from location changes, including close-ups within the same location. Preserve the original video and master audio.

## Research and art direction

Use Pinterest for actual visual discovery when requested; inspect candidate pins and follow original sources where useful. Search from product use, source geometry AND the user's visual benchmark. A matching category such as "warehouse," "woman" or "car interior" is insufficient. Judge the actual image at usable size for photographic quality, subject placement, face readability, lighting, depth, clutter and shot compatibility. Apply the selection rubric in the research reference before presenting a recommendation.

Treat “viral” as a claim requiring evidence. Separate aesthetic inspiration, visible popularity signals, and documented video performance. Do not attribute success to a background merely because it appears in a successful video.

Follow the requested identity and sourcing route. For a photographed creator, choose a clear, usable identity reference that fits the desired creator presentation, not merely the right clothing color. Generate an avatar or background only when that mode is requested or already agreed. Keep source and use records accurate: a Pinterest pin is not proof of authorship, a license, photographic origin, or performance. Uncertainty about those facts must not become an unannounced switch to generated assets.

## Make the direction reviewable

Deliver an image-led board: source frame beside proposed avatar/location, short concrete fit notes, exact source links, and shot assignments. Lead with the opening-shot avatar/background pairing so the creative direction can be judged immediately. Include relevant benchmark comparisons; do not bury weak images beneath polished layout or extensive explanations. Present provisional or rejected candidates as such, not as production-ready choices.

When direction selection is unresolved, present the completed board before asking the user to choose. If the user has delegated art direction and authorized production, select the strongest supported direction and continue within scope. Do not add a mandatory approval gate to an already authorized workflow.

For a corrected board, use a visibly new versioned filename, embed or locally package authorized images, and inspect the exact final file in its viewer. Link that new file. Confirm that old rejected images and media IDs are absent from active inputs. A renamed page or successful file write alone is not evidence the visual correction worked.

## Produce and learn

Prepare consistent references within the requested source mode and run a representative Genjutsu test within the authorized budget. Keep avatar identity and wardrobe stable across shots unless changes were requested. Match environment geometry, camera height, lighting, and contact surfaces. Consider an integrated still only when its preparation method is within the agreed scope.

Compare source and output before scaling up. Check the agreed text policy and compare every cut frame by frame; a background must not switch to the next location while the current shot's action is still happening. Diagnose the actual defect and change a relevant variable. Preserve prompt, references/order, settings, job IDs, estimated/actual costs when available, and review findings. Stop retries when the test passes, the authorized cost/attempt limit is reached, or repeated results show no meaningful improvement. Do not silently expand the budget. When the user approves the overall result but reports a local defect, retain the accepted references, avatar and art direction and target that defect.

Deliver the playable result and a short account of changes and remaining defects, or the board alone when that was the requested output. Do not claim exact identity, audio, timing, or pixel preservation without checking it.

State production status plainly: references prepared, job submitted, rendered but unreviewed, or reviewed output. A reference board is not a replicated video. If an allowance choice is genuinely missing, finish the concrete preparation and ask once; retain the answer across turns.
