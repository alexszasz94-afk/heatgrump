---
name: make-reel
description: Produce un lot de reel-uri HeatGrump (B1, B2, cozy, conector, telecomandă, unboxing + 3 hook-uri) din perechi personaj+cameră, cu rețetele canonice din prompts/ și regulile din docs/03-rules.md.
---
# make-reel
Input: lista de perechi {personaj, cameră, gen} (media_id Higgsfield). Output: clipuri + `board/grinch-reel-board.html` + lista de linkuri.

1. Citește `CLAUDE.md`, `docs/03-rules.md`, `library/media.json`.
2. Pentru fiecare reel alege: clip de mișcare B1/B2/cozy prin rotație (nu repeta combinația reel-ului anterior), îmbrăcămintea de dedesubt (normală, diferită), și notează-le în `board/data.json`.
3. Trimite în paralel (batch, max 12/lot):
   - B1/B2/cozy: `hf_mult_motion_control`, medias = [char, room, 4 product refs, clip], prompturile din `prompts/`, 1080p, 9:16, 4/5/4 s.
   - Plăci: `gpt_image_2` 9:16 4k pentru telecomandă (`controller-plate.txt`), conector (`connector-plate.txt`), unboxing (`unboxing-image.txt` + box-on-floor).
4. După plăci: videourile de telecomandă, conector, unboxing cu `seedance_2_5` omni_reference, 1080p, bitrate high, audio on.
5. Hook-uri: rulează skill-ul `hook-ideas` (3 per reel).
6. QA: rulează skill-ul `qa-check` pe fiecare rezultat; regenerează ce pică (max 3).
7. Actualizează `board/data.json` + `board/hooks.json`, rulează `python3 board/build_html.py`, livrează linkurile complete în ordinea de montaj.
