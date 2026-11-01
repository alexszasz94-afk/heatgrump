# HeatGrump Studio — kitul de producție (doar halatul Grinch)

Vorbește cu Szasz în română, simplu. Textele de marketing (text pe ecran, caption) în engleză.
Ordinea de citire: `../docs/03-rules.md` (regulile lui Szasz, câștigă mereu) → `PRODUCT.md` → `HOOKS.md` → `recipes/` → `PLAN-175.md`.

## Comanda principală: `video nou <link>`
1. **Buget**: `balance` (Higgsfield). Un video costă ~22 credite (`python3 engine/cost.py`). Sub 300 credite → oprește-te și spune-i lui Szasz.
2. **Set**: `python3 engine/studio.py next` → alege setul de B-roll (personaj + cameră + ținută), varianta fixă de conector/telecomandă (gen + piele) și melodia, din rotație. Nu pune același set la două videouri la rând.
3. **Hook** (singura generare nouă per video) — `recipes/hook-copy-kling4.md`:
   descarcă linkul (`yt-dlp`), găsește tăietura hook-ului (fps 10), scoate sunetul și textul ars, apoi Kling 4.0 `video-edit` cu personajul + camera setului (fără halat dacă hook-ul e nou), 720p, 3-4 s, sunetul din aceeași generare (blocul SOUND în 3 straturi). Steagul american vizibil în cadru (regula 18 oct).
4. **B-roll**: din setul ales (deja făcut, refolosit). Dacă setul nu există → `recipes/broll-grinch.md` (o singură dată per set).
5. **Clipuri fixe**: conector + telecomandă din `../output/fixed/*-taiat.mp4` (după gen și piele). Nu se generează.
6. **QA cadru cu cadru**: `../.claude/skills/qa-check` + ultimul cadru mărit la conector. Pică → max 3 încercări.
7. **Montaj**: `python3 engine/studio.py montaj <id>` scrie spec-ul și rulează `../engine/final.py` (text TikTok Sans, muzică de Crăciun cu drop-ul pe tăietura hook→B-roll, se termină cu muzica).
8. **Livrare**: MP4 în `../output/studio/<id>/`, trimite fișierul direct în chat + caption (EN, o propoziție + hashtag-uri) + ce hook/melodie/set s-a folosit. `git add -A && git commit && git push`.

## Comanda `lot zilnic` (25 videouri)
`python3 engine/studio.py plan 25` → 25 sloturi (hook-uri din `HOOKS.md` + linkuri noi), apoi pașii 3–8 în lot: toate hook-urile trimise odată cu `generate_video_batch` (max 12 pe lot), `jobs_wait`, QA, montaj în serie. Vezi `PLAN-175.md`.

## Setări fixe
- Video: **Kling 4.0** (`kling4_0`), 9:16. Hook 720p; B-roll 1080p. *(Seedance nu se mai folosește pentru halate — a se confirma de Szasz, vezi KIT-NOTES.md.)*
- Imagini: `gpt_image_2_5`, quality high, 9:16, 4k.
- Mereu `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`.
- Lumină foarte moale, naturală (`../prompts/blocks/light-ultra-real.txt`), culori vii semicalde, fără auriu/portocaliu. Fără text ars, fără zoom, fără branduri reale.
