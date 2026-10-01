# HeatGrump Engine — instrucțiuni pentru Claude Code

Proiect: producție automată de reel-uri pentru **HeatGrump** (halat termic cu glugă, tip Grinch, vândut prin organic dropshipping). Proprietar: Szasz. Vorbește cu el în română; tot textul de marketing (replici, text CapCut, descrieri) e în engleză.

Citește în ordinea asta înainte de orice generare:
1. `docs/03-rules.md` — regulile absolute (au prioritate peste orice altceva).
2. `library/media.json` — ID-urile Higgsfield (produs, cutie, telecomandă, conector, clipuri de mișcare, personaje/camere).
3. `prompts/` — prompturile canonice. Se copiază cuvânt cu cuvânt; se schimbă doar ce e marcat `<...>` sau `[INSERT ...]`.
4. `docs/heatgrump-grinch-reel-spec.md` — specul complet + șabloanele lui de unboxing.
5. `docs/memory-export-heatgrump.md` — istoricul complet al regulilor, datat. Dacă două reguli se contrazic, câștigă cea mai recentă.

## Prima rulare și comenzile lui Szasz
Szasz nu e programator. Vorbește simplu, în română, fără jargon; nu-i cere comenzi de terminal decât dacă nu există altă cale, și atunci dă-i comanda exactă de copiat.
- La `start`: verifică serverul MCP `higgsfield` (dacă lipsește, explică pașii din START-AICI.md pasul 4), apelează `balance`, verifică `ffmpeg` și `yt-dlp` cu `which`, apoi arată meniul de comenzi din START-AICI.md.
- La `reel nou`: caută în `inbox/` perechile `reelN-personaj.*` + `reelN-camera.*`, încarcă-le în Higgsfield (`media_upload` → PUT pe upload_url → `media_confirm`), întreabă băiat/fată dacă nu e evident, apoi rulează skill-ul `make-reel`.
- La `planul zilei` → `python3 engine/rotation.py plan` și arată cele 15 sloturi (5 dovedite / 5 adaptate / 5 creative, vezi `library/proven-hooks.json` + `docs/03-rules.md` §Mix zilnic). La `hook-uri reel N` → skill `hook-ideas`. La `animează hook K la reel N` → seedance_2_5 omni_reference din frame-ul hook-ului, 4-5 s, apoi actualizează tabla.
- La `tabla` → `python3 board/build_html.py` și deschide fișierul.
- La `analizează <link|fișier>` → descarcă (yt-dlp) sau citește fișierul, extrage 8 cadre + audio, descrie hook-ul în formatul din `library/hooks-library.json` și adaugă-l cu sursa; dacă e link FB/IG și yt-dlp eșuează, cere-i să descarce clipul și să-l pună în `inbox/`.
- La `feedback <fișier>` → aceeași analiză + compară cu biblioteca + 3 lucruri concrete de schimbat.
- La `research` → skill `research`. La `analizează clipurile noi` → prepare_clip + skill `analyze-clip` pe fiecare clip nou.
- La `video nou` / `15 videouri` → skill `make-video` (respectă bugetul și rotația; un set = max 4 videouri, niciodată consecutive).
- La `seturi noi` → skill `new-sets` (camere și personaje luate direct de pe Pinterest, pozele exacte — regula din 1 oct).
- La `feedback` → skill `feedback` (cifre reale Meta) ; `feedback <fișier>` → analiză de clip.
- La `regula: ...` → adaugă linia datată în `docs/03-rules.md` și, dacă e regulă de producție, în `CLAUDE.md`.
Descarcă rezultatele Higgsfield în `output/reelN/` și verifică-le vizual (skill `qa-check`) înainte să le raportezi.

## Ce face Szasz și ce faci tu
Szasz face în CapCut: textul pe ecran, muzica, mici tăieturi. Tu îi dai MP4-ul montat + fișierul .txt cu propunerea de text (EN, pe secunde), caption (EN, o propoziție + hashtag-uri) și idee de muzică. Tu răspunzi de: hook-uri (originale, din research), calitatea vizuală (ultra-realist), analiză și feedback.

## Ce e un reel
Set de clipuri, în ordinea de montaj: **hook → unboxing → B1 (îmbracă halatul) → B2 (deschide halatul) → conector → telecomandă → cozy**. Hook-ul îl alege el din 3 propuneri; textul îl pune el în CapCut.

## Cum se produce fiecare clip
| Clip | Metodă | Prompt | Aprobare |
|---|---|---|---|
| B1, B2, cozy | Genjutsu `hf_mult_motion_control`, clip de mișcare din bibliotecă (ROTIT între reel-uri) + personaj + cameră + 4 ref. produs | `prompts/b1-…`, `b2-…`, `cozy-…` | direct |
| telecomandă | placă gpt_image_2 → video seedance_2_5 | `controller-plate.txt` → `controller-video.txt` | direct |
| conector | placă gpt_image_2 → video seedance_2_5 | `connector-plate.txt` → `connector-video.txt` | direct |
| unboxing | placă (cutia PE JOS) → video, cutie + 1-2 ref. produs | `unboxing-image.txt` → `unboxing-video.txt` | direct |
| hook | 3 idei per reel DOAR ca text detaliat în Studio, fără imagini (regula 1 oct); hook-ul video = clip viral tăiat + refăcut cu Genjutsu | — | el alege, apoi se face |

## Setări fixe (nu se coboară niciodată)
- Imagini: `gpt_image_2`, 9:16, quality high, resolution 4k.
- Video: `seedance_2_5`, `mode: "omni_reference"` când există start_image, `aspect_ratio "9:16"` **și** width 1080 / height 1920, resolution 1080p, bitrate_mode high, generate_audio true.
- Genjutsu motion control: 1080p, 4 s (B1, cozy) / 5 s (B2), roluri `image_references` / `video_references`.
- Mereu `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`.
- Fiecare start frame și video: culori vii, semicalde (nu auriu/portocaliu) + blocul `prompts/blocks/light-ultra-real.txt`.
- Fără text ars în imagine, fără zoom, fără branduri reale.

## Ce dă Szasz la fiecare reel
Personajul, camera (pereche), și dacă e băiat sau fată. Restul e în bibliotecă. Îmbrăcămintea de dedesubt o alegi tu: normală, diferită la fiecare personaj (pijama de Crăciun / ceva cu America / stil american / cozy), aceeași în toate clipurile reel-ului, și o spui la livrare.

## Livrare
După fiecare lot: regenerează `board/grinch-reel-board.html` (`python3 board/build_html.py`, date în `board/data.json` + `board/hooks.json`) și dă toate linkurile directe, în ordinea de montaj, pentru fiecare reel. După orice regenerare, lista completă din nou, nu doar clipul refăcut.

## Verificare (QA) înainte de livrare
Pe fiecare rezultat descărcat, verifică vizual (Claude cu vedere):
- 9:16, fără text, fără branduri; personajul = referința; camera = referința.
- Halat: căptușeală verde, buzunare simple fără față, halat întreg până jos, lumină ultra-realistă.
- Telecomandă: exact 5 luminițe, toate stinse pe placă; în video urcă 1→5, una singură aprinsă.
- Conector: gri, în două părți, în video intră complet, fără gol.
- Unboxing: cutia pe podea; în video fereastra cutiei se golește când scoate halatul; fața nu e acoperită; un singur produs.
- Hook NOU (adaptat/creativ): FĂRĂ halat în cadru; acțiunea se leagă de textul propus; 2 variante video, se alege cea mai bună.
- Hook DOVEDIT (din `library/proven-hooks.json`): se reface exact conceptul (halatul poate apărea, e conceptul validat), cu alt personaj + altă cameră; Genjutsu unde există clip de mișcare; o singură variantă; nu mai des de o dată la 3 zile.
Dacă pică, regenerează (max 3 încercări), apoi raportează.

## Capcane cunoscute
- `ip_detected` la unboxing video cu multe referințe de halat → retrimite cu 1 referință, apoi doar cutia. Cozy cu unele personaje poate fi respins de 2 ori: schimbă clipul de mișcare.
- Fără `aspect_ratio` explicit iese 16:9. Fără `resolution` iese 720p.
- `nano_banana_2` = flash (slab). Dacă e nevoie de Nano Banana, cere `nano_banana_pro`.
- Creditele: workspace shared; motion control 1080p ≈ 44 credite/clip, seedance ≈ 55, gpt_image_2 4k ≈ 15. Verifică `balance` înainte de loturi mari.

## Dacă rulezi în Claude Code pe web (claude.ai/code)
Nu e nimic de instalat local; `setup-cloud.sh` a rulat deja (ffmpeg, yt-dlp). Token-urile vin din variabilele mediului, nu din `.env`. După fiecare lot: `git add -A && git commit -m "lot <data>" && git push`, ca Szasz să-și descarce MP4-urile din GitHub. Dacă un domeniu e blocat (eroare de rețea la apify/facebook/cloudfront), spune-i exact ce domeniu să adauge în *Allowed domains* ale mediului — nu încerca ocolișuri.
