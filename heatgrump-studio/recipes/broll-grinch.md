# Rețetă: B-roll Grinch (B1 + B2 + cozy) — se face O DATĂ per set, se refolosește la 7 videouri
Stare: înghețată pe metoda actuală din repo (Genjutsu motion control, prompturile din `../prompts/`). Varianta Kling 4.0 (v4/v5, „metoda C” din limitless `recipes/grinch-broll-classic-cozy.md`) — DE SINCRONIZAT când repo-ul limitless e accesibil, apoi se face clipul de referință Grinch.

## Intrări per set
personaj (Pinterest, latura mică ≥1080 px, aspect american obișnuit) · cameră 4K cu canapea (casă americană, Crăciun) · ținută din `outfit.txt` (stil american, aceeași în tot setul) · cele 4 referințe de halat (PRODUCT.md) · gen + piele (pentru clipurile fixe).

## Clipuri
| Clip | Mișcare (media.json) | Durată | Tăiere la montaj |
|---|---|---|---|
| B1 îmbracă halatul | `B1_x2` b1-b-x2 d8a474d2 / b1-a-x3 8391f616 (rotit) | 4 s | după ce pune gluga (~1,3 s) |
| B2 deschide halatul, fața la vedere | dB2 9896b250 / dB2f df7d7a2b (rotit) | 5 s | până închide halatul, accelerat x1,35 |
| Cozy pe canapea, filmat larg | 8042602c (bărbat) / 5f950f18 cozy-c (femeie, 0–1,2 s) | 4 s | ~2,5 s |
Prompturi: `../prompts/b1-motion-control.txt`, `b2-motion-control.txt`, `cozy-motion-control.txt` + `../prompts/blocks/light-ultra-real.txt`. Ținuta în `<OUTFIT>`.

## Setări
1080p (NU 480p — seturile us1-us3 existente sunt 480p, doar previzualizare), 9:16, `declined_preset_id`. Cozy: fără blitz, fără sursă de lumină din poziția camerei.

## Cost per set
Kling 4.0 1080p: 13 s × 3,25 = 42 credite (+ eventual 3 cadre de start gpt_image_2_5 = 13) → ~55-70 cu reîncercări. Împărțit la 7 videouri ≈ 10 credite/video.
