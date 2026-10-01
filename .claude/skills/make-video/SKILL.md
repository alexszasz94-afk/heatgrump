---
name: make-video
description: Face un video final HeatGrump: alege setul din rotație, propune 3 hook-uri (fără halat), animează hook-ul ales (sau pe cel mai bun din bibliotecă), verifică asemănarea, montează MP4-ul și notele pentru CapCut. Rulează la „video nou” / „15 videouri”.
---
1. Buget: cere `balance` din Higgsfield și rulează `python3 engine/budget.py check <credite>`. La STOP te oprești și spui.
2. `python3 engine/rotation.py plan` → cele 15 sloturi ale zilei (kind = proven/adapted/creative + set). Dacă lipsesc seturi, skill `new-sets`. La „video nou” ia primul slot nefăcut din `state/plan-<azi>.json`.
3. Hook după slot:
   - proven → `library/proven-hooks.json`: concept, `lines` (rotește textul), method genjutsu (hf_mult_motion_control din `motion_clip` cu personajul/camera setului) sau frame; O variantă; hook_kind="proven", hook_key=cheia conceptului.
   - adapted → cel mai bun tipar din `library/hooks-library.json` → `research[]` (structura, nu clipul; max 2 folosiri); 2 variante; hook_kind="adapted".
   - creative → skill `hook-ideas` pentru setul ales (3 idei, prioritizează tiparele cu scor mare din `library/hooks-library.json` → `scores` și `research[]`). Dacă Szasz a cerut lot automat, alege tu ideea cu cel mai bun scor/pattern, altfel arată-i cele 3.
4. `python3 engine/similarity.py <set> <hook_key> <hook_kind>` → la AVERTISMENT alege alt hook/set.
5. Animează hook-ul: seedance_2_5 omni_reference, start_image = frame-ul (end_image dacă poziția finală contează), 4–5 s, 1080p, audio on, mișcarea scrisă PE SECUNDE (o singură acțiune), + blocul light-ultra-real. La hook-urile noi: 2 variante în același generate_video_batch, alegi cea mai bună. Descarcă și verifică cu `qa-check`.
6. Scrie `output/plans/<n>.json` (set, hook cu line/alt/caption/music/bridge, clips = link-urile: HOOK nou + B-roll din set) și rulează `python3 engine/assemble.py output/plans/<n>.json`.
7. Livrează: calea MP4-ului, conținutul .txt-ului (text CapCut, caption, muzică), și adaugă în tabla HTML.
Muzică (idei): descrie tipul (ex. „sunet trending cozy/lo-fi, sau un „oh no” comic la hook, apoi liniște pe B-roll”), nu fișiere; Szasz o alege în CapCut/la postare.
Caption: o propoziție în engleză + hashtag-uri, fără bullet-uri.
