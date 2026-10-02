---
name: make-video
description: Face un video HeatGrump COMPLET, gata de postat (regula 2 oct): set din rotație, hook din viral refăcut cu Genjutsu, B-roll + clipurile fixe, QA, montaj cu tăieturile lui Szasz, texte pe ecran cu emoji și muzică de Crăciun. Rulează la „video nou” / „15 videouri”. Szasz doar zice „video nou”; tu faci tot.
---
Citește întâi `docs/03-rules.md` (secțiunile din 2 oct au prioritate).

1. Buget: `balance` (Higgsfield) + `python3 engine/budget.py check <credite>`. La STOP te oprești.
2. Set: `python3 engine/rotation.py plan` → primul slot nefăcut. Lipsesc seturi → skill `new-sets` (doar poze ≥1080 px latura mică). Notezi gen (bărbat/femeie) și tipul camerei (cu pat / fără pat).
3. B-roll pentru set (dacă nu există deja în `rotation`): skill `make-reel` doar pentru unboxing, B1, B2, cozy.
   - B1: clip de mișcare scurt multiplicat (`media.json` → `motion_clips.B1_x2`, rotit); se taie după ce pune gluga.
   - Cozy: cameră cu pat → `cozy-a-x2`; fără pat → `8042602c`.
   - Telecomanda și conectorul NU se generează: `media.json` → `fixed_clips` după gen (`output/fixed/*-taiat.mp4`).
4. Hook (din virale, fără halat dacă e hook nou):
   - Ia cel mai bun viral nefolosit din `library/style-ref/index.json` (sau research nou / artifactul prietenului): descarcă, uită-te la primele 6 s (fps 2), găsește tăieturile exacte (fps 10).
   - Taie DOAR partea de hook ca referință de mișcare (bucăți <1,8 s → dublate). Încarcă în Higgsfield.
   - `hf_mult_motion_control`, 1080p, 4 s, image_references = personaj + cameră (FĂRĂ referințe de halat), video_references = bucata; prompt: acțiunea din viral, hainele setului, NO PRODUCT, fără text. Mai multe tăieturi → mai multe joburi.
   - QA: fața lui, camera, fără halat, fără text. Pică → încă o încercare (max 3).
   - Textul hook-ului = textul viralului adaptat (ex. „The problem 😩❄️”, apoi „Vs…” pe produs).
5. QA pe tot (skill `qa-check`): unboxing (cutie pe podea, cutia se golește), B2 (până închide halatul), conector (ultimul cadru complet intrat).
6. Montaj FINAL: scrie `output/reelN/final.json` și rulează `python3 engine/final.py output/reelN/final.json`.
   Ordine și tăieturi (regulile din 2 oct): hook → unboxing ~2,5 s → B1 până pune gluga → B2 până închide halatul → conector fix 1,5 s → telecomandă fixă (pornește cu apăsarea, până la 3) → cozy ~3 s. Țintă 15-18 s.
   Texte (EN, cu emoji, stil merry.jammies/snuglore): implicit textul hook-ului rămâne pe TOT videoul (regula 2 oct); doar la hook-uri de tip „The concept / Vs…” se schimbă textul pe produs.
   Final: videoul se oprește odată cu muzica (automat în final.py); Reel 7 = referința aprobată.
   Sunet: B-roll, conector, telecomandă = mute (automat în final.py); doar hook-ul își păstrează sunetul.
   Muzică: `library/music/*.m4a` (All I Want For Christmas / It's Beginning to Look… / Last Christmas), rotită; sunet original la 0,15.
7. Verifică MP4-ul final (cadre la fiecare tăietură + că are text și muzică), urcă-l în Studio (asset + `clips/rN-REEL`), actualizează harta, `git add -A && commit && push`.
8. Livrează lui Szasz: linkul din Studio, calea MP4-ului, caption-ul (EN, o propoziție + hashtag-uri) și ce hook/viral/muzică ai folosit.
