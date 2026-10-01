# Genjutsu execution and verification

## Refresh capabilities

Known connector routes from September 23, 2026:

- `hf_mult_motion_control`: use a driving video to recast the performance.
- `hf_mult_replace_object`: targeted changes to characters, products, wardrobe, or locations.

Discover the current Higgsfield tools and inspect `models_get` for the selected route before submitting. These names are connector model IDs, not public API endpoint names. Do not infer parameters from another video model.

At the research date, the connector exposed 480p, 720p, and 1080p. Official website and API pages disagreed on image counts and minimum duration. Use the active route's validated limits; do not freeze a universal limit into this workflow. No dedicated seed, identity-strength, frame-rate, masking, or structured per-shot reference controls were established by that metadata.

Sources for rechecking: [product FAQ](https://higgsfield.ai/genjutsu), [official guide](https://higgsfield.ai/blog/higgsfield-genjutsu), [public API](https://open.higgsfield.ai/models/higgsfiled/genjutsu/motion-transfer/v1.0).

## Source inspection and upload

Prefer local analysis when practical for a supplied local file. If using Higgsfield video analysis, follow its upload requirements and explain that longer-video scene summaries can be less accurate. A queued analysis is not an analysis result. Retain its ID and inspect status rather than submitting duplicates; if delayed, continue local inspection and report any unresolved coverage.

Read upload tool instructions carefully: local files, OpenAI attachments, and sandbox-generated outputs may require different supported upload flows. A Desktop path is not automatically a remote attachment or media ID. Confirm uploads before using returned media IDs.

For the known direct generation interface, provide one source video with role `video` and ordered references with role `image`. Reuse confirmed IDs. Do not treat an integrated composition still as a guaranteed `start_image` constraint unless the current route explicitly supports that role.

## Prompt and references

Use the selected source assets, not substitute reference sheets. Record whether each reference is an exact sourced image, a crop/composite, or generated; any preparation must preserve the chosen sourcing mode. An integrated still is optional and must not silently replace requested photographs. After a creative correction, rebuild the active reference list and prompt from the current selection; exclude rejected media IDs and invalidate stale estimates. Keep older records only as clearly rejected history.

Specify the source subject, replacement reference, scope, and essential preservation requirements. Map multiple people using stable source descriptions across cuts. Keep upload order and prompt references aligned. Example wording, to adapt rather than copy mechanically:

> Replace the presenter in the blue shirt with the adult in reference image 1. Use image 2 for the kitchen setting. Preserve the source gestures, camera framing, timing, and product interaction. Keep the bottle and its packaging unchanged. The images define appearance and environment; the video supplies the performance. Match the new room's perspective and lighting.

Do not add new actions to a preservation task. Treat timestamp instructions as soft guidance, not an API timeline feature. Choose full-avatar versus face-only scope explicitly. Product swaps need the replacement product's physical dimensions and interaction considered; a different shape may invalidate the original grasp.

## Text handling

Apply the user's text policy explicitly; Esteban's default is a clean video without editorial text overlays. Preserve the source performance, not its burned-in caption pixels. Do not ask Genjutsu to spell, redraw or preserve captions, subtitles, hook lines or emoji stickers for a text-free recast. Use a caption-free source if one is already available. Otherwise explicitly request removal of the source overlays and check the result for residual or invented glyphs. Omitting text from the prompt is insufficient when it is visible in the source.

Adapt this prompt clause to the source:

> Remove all source caption and emoji overlays. Produce clean footage with no captions, subtitles, hook text, floating letters or emoji stickers. The source supplies the actions, camera and cuts, but not its editorial overlays. Keep the product and its physical label unchanged.

Distinguish editorial overlays from actual packaging labels or scene signage; do not erase product information under a generic "no text" instruction. If a user later requests captions, render the exact approved wording in a separate editing pass after the visual generation. Do not rely on generative letter shapes. Residual captions fail a text-free brief: use an authorized cleanup or targeted retry, or report the defect when the allowance does not cover correction. Do not silently crop the composition or blur over the subject/product to hide text.

## Montage strategy

Use the shot map to choose between a short whole-montage test and separate-shot generations. A whole sequence may preserve context; separate shots give more control over different locations and isolate retries. Neither is guaranteed superior.

When splitting, preserve exact editorial boundaries and use handles where supported. For shots below a route's duration minimum, assess supported grouping or extra source handles; do not silently duplicate frames, slow motion, or cut dialogue. Reassemble and check identity, scale, lighting, and audio across boundaries.

Keep an edit map with source cut times and frame indices, separate from the location map. A close-up of a button in the stadium still belongs to the stadium until the real location cut. Explicitly tell the model to hold each background through the last frame of its assigned shot: no early location swap, added insert, blended transition or invented cut. Timestamp prompting remains soft guidance and must be verified.

If a whole-montage test introduces an extra cut or an early background switch, prefer isolating the affected source shot for an authorized correction and assembling at the source boundaries. Keep the accepted surrounding shots. Simply deleting the bad interval is not a valid fix when it removes a product action or changes the music timing.

## Cost and execution

Prepare the concrete test and obtain its current estimate before generation. Include image-reference preparation and retries in the budget when applicable. Estimate calls that import HTTPS images can create uploads, so prefer already confirmed media IDs. Respect existing production authorization. If no spending allowance covers the work, ask about the prepared test's cost/attempt limit after completing research and the board.

Start with one representative test when production is authorized. A lower resolution can assess composition and movement; facial or label fidelity may require inspection at the intended final resolution. Do not assume a successful low-resolution result will reproduce identically at a higher resolution.

Free Genjutsu runs and unlimited allowances are distinct. Follow the current tool contract and explicit user choice. Never interpret a returned allowance-choice prompt as submission success. On uncertain submission, resolve the original job status before retrying to prevent duplicate spending. Follow the generator's own display/wait behavior rather than creating duplicate result widgets.

Record source and output IDs, shot IDs, reference IDs/order, exact prompt, model/settings, estimate, actual charged amount if available, and review. A successful tool response means the job was accepted or completed, not that visual quality passed.

## Review and retry

Inspect the moving output, key frames around cuts, and occlusion/reappearance. Check:

- Avatar identity independently from wardrobe/accessories.
- Product shape, label, hand contact, and preserved application.
- Background geometry, perspective, shadows, reflections, and feet/surface contact.
- Gesture timing, framing, cuts, final action, output duration and frame rate.
- Editorial text policy: no retained source captions, garbled letters, new captions or emoji overlays in a text-free deliverable. Inspect all shots, including brief frames around cuts.
- Audio existence, content, lip synchronization, ending and music; captions only when requested.

Use automated scene-change detection to nominate boundaries, then visually compare the frames on both sides with the source; camera movement can produce false detections and subtle cuts can be missed. Check the full shot sequence for added or missing cuts as well as each expected boundary. Compare timecodes, not raw frame numbers when frame rates differ. Allow only the necessary output-frame rounding; do not excuse an early location change as frame-rate conversion. Inspect several frames before and after each cut and the end of each product interaction for next-scene background leakage.

Retain original audio separately. If it must be reattached, align against measured output timing first; do not assume equality. Do not add captions to a text-free deliverable.

Choose a targeted correction: clearer reference, better assignment, narrower edit, separate shot, or an integrated composition if that preparation mode is authorized. Check the result against the user's visual benchmark as well as technical continuity; correct timing does not compensate for artificial skin, poor light or a mismatched setting. Return to the original source for independent retries unless deliberately continuing an edit. End when accepted, at the user's budget/attempt cap, or after repeated attempts fail to improve the same defect. Explain any remaining limitation and provide the best reviewable result.

## Research basis and uncertainty

[Human Academy](https://www.youtube.com/watch?v=tEz0ImlNEtQ&t=504) reports that an edited source-frame reference improved environment integration, with residual distortion. [AI BORDER](https://www.youtube.com/watch?v=wM9S_iyuRUo&t=205) demonstrates character-sheet preparation for parkour. [Choigpt's production record](https://aisolutions.kr/about/higgsfield-genjutsu-3/) reports incomplete identity replacement and changes in output duration/frame rate. These are case reports, not universal benchmarks. Prompt instructions requesting preservation are not proof it occurred.
