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
Set de clipuri, în ordinea de montaj: **hook → (unboxing DOAR când hook-ul o cere, regula 19 oct) → B1 (îmbracă halatul) → B2 (deschide halatul) → conector → telecomandă → cozy**. Hook-ul îl alege el din 3 propuneri; textul îl pune el în CapCut.

## Cum se produce fiecare clip
| Clip | Metodă | Prompt | Aprobare |
|---|---|---|---|
| B1, B2, cozy | UN SINGUR CLIP per set (regula 19 oct): clipurile de mișcare B1+B2+cozy lipite într-un video, o generare Genjutsu `hf_mult_motion_control`, probă 480p apoi 1080p; clip de mișcare din bibliotecă (ROTIT între reel-uri) + personaj + cameră + 4 ref. produs | `prompts/b1-…`, `b2-…`, `cozy-…` | direct |
| conector + telecomandă (regula 24 oct) | CLIPURILE REALE ale lui Szasz: `output/fixed/conector-real.mp4`, `output/fixed/telecomanda-reala.mp4` — nu se mai generează | — | — |
| telecomandă | CLIP FIX refolosit (bărbat / femeie, `media.json` → `fixed_clips`); se generează doar dacă lipsește: placă gpt_image_2 → video seedance_2_5 | `controller-plate.txt` → `controller-video.txt` | direct |
| conector | CLIP FIX refolosit (bărbat / femeie, `media.json` → `fixed_clips`); se generează doar dacă lipsește: placă gpt_image_2 → video seedance_2_5 | `connector-plate.txt` → `connector-video.txt` | direct |
| unboxing | placă (cutia PE JOS) → video, cutie + 1-2 ref. produs | `unboxing-image.txt` → `unboxing-video.txt` | direct |
| hook | le scrie Szasz (5-6), se rotesc prin videouri (regula 2 oct); montajul final cu text + muzică se face doar când există hook-ul | — | el |

## Setări fixe (nu se coboară niciodată)
- HALATUL DOAR DUPĂ REFERINȚE (regula 18 oct, întărită 20 oct): la orice clip cu halat se pun TOATE cele 4 referințe Grinch (`product_grinch_refs`), niciodată 2 sau 1, nici la ip_detected; halatul nu se descrie niciodată în cuvinte, doar „REPRODUCE IT ONE TO ONE from Images N–M”. ID lipsă → reîncarci pozele, nu descrii.
- PERSONAJUL DOAR DUPĂ POZA LUI (regula 24 oct): la orice generare cu personaj (start frame, variantă, corectură, video) poza personajului se pune MEREU ca referință directă, chiar dacă pornim de la un frame deja generat; niciodată doar din frame-ul anterior.
- Imagini: `nano_banana_pro`, 9:16, resolution 4k (regula 23 oct; înainte gpt_image_2 — ieșea prea procesat).
- Video: **DOAR Kling 4.0 (`kling4_0`), 1080p** (24 oct, înlocuiește 720p) (regula 24 oct, Szasz: „folosim doar Kling 4.0 de acum, 720p, e foarte ieftin”): `video-edit` pe clipurile noastre de mișcare (B-roll, conector, telecomandă, hook copiat), `image-to-video` din start frame (hook, unboxing). `aspect_ratio "9:16"`. Seedance și Genjutsu nu se mai folosesc (rămân doar ca istoric).
- Genjutsu motion control: 1080p, 4 s (B1, cozy) / 5 s (B2), roluri `image_references` / `video_references`.
- Mereu `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`.
- Fiecare start frame și video: culori vii, semicalde (nu auriu/portocaliu) + blocul `prompts/blocks/light-store-premium.txt` (stilul aprobat 20 oct, „perfect”; înlocuiește light-ultra-real.txt). Mereu „UGC style, natural, shot on an iPhone 17 Pro Max” (regula 19 oct, actualizată).
- LUMINA, regulă pe viață (23 oct): MEREU foarte moale și foarte naturală, la orice imagine/video — blocul `prompts/blocks/light-soft-natural.txt` în fiecare prompt; fără lumină dură, contrast dramatic, HDR, glow sau aspect CGI.
- Fiecare video: blocul `prompts/blocks/motion-natural.txt` (regula 20 oct) — mișcări naturale, fără mișcări bruște, acțiunea rapidă; ce apare când se întoarce camera trebuie să fie acolo unde se uită personajul.
- Prompturi LUNGI și DESCRIPTIVE, analizate critic înainte de trimitere (natural, logic, fizică, direcția privirii, fără cuvinte care declanșează filtre) — regula 20 oct. Aplic singur tot ce e în reguli, fără să mi se repete.
- Fără text ars în imagine, fără zoom (logo-urile din clipul de referință rămân — regula 26 oct; nu inventăm branduri noi).

## Stil american (regula 18 oct)
- Fiecare hook are steagul american undeva în cadru; la B-roll hainele de dedesubt sunt în stil american; doar personaje care arată americane.

## Ce dă Szasz la fiecare reel
Personajul, camera (pereche), și dacă e băiat sau fată. Restul e în bibliotecă. Îmbrăcămintea de dedesubt o alegi tu: normală, diferită la fiecare personaj (pijama de Crăciun / ceva cu America / stil american / cozy), aceeași în toate clipurile reel-ului, și o spui la livrare.

## Livrare
După fiecare lot: regenerează `board/grinch-reel-board.html` (`python3 board/build_html.py`, date în `board/data.json` + `board/hooks.json`) și dă toate linkurile directe, în ordinea de montaj, pentru fiecare reel. După orice regenerare, lista completă din nou, nu doar clipul refăcut.

## Verificare (QA) înainte de livrare
Pe fiecare rezultat descărcat, verifică vizual (Claude cu vedere):
- 9:16, fără text, fără branduri; personajul = referința; camera = referința.
- Halat: căptușeală verde, buzunare simple fără față, halat întreg până jos, lumină ultra-realistă. GLUGA (regula 19 oct): verde, cu fața Grinch, margine albă și ciucure, în toate cadrele, inclusiv prim-planul din spate.
- Telecomandă: exact 5 luminițe, toate stinse pe placă; în video urcă 1→5, una singură aprinsă.
- Conector: gri, în două părți, în video intră COMPLET, fără gol — verifică ULTIMUL cadru mărit (regula 2 oct).
- Unboxing: cutia pe podea; în video fereastra cutiei se golește când scoate halatul; fața nu e acoperită; un singur produs.
- Hook NOU (adaptat/creativ): FĂRĂ halat în cadru; acțiunea se leagă de textul propus; UN SINGUR video de test la 480p (regula 19 oct; înainte erau 2 variante).
- Hook DOVEDIT (din `library/proven-hooks.json`): se reface exact conceptul (halatul poate apărea, e conceptul validat), cu alt personaj + altă cameră; Genjutsu unde există clip de mișcare; o singură variantă; nu mai des de o dată la 3 zile.
- Analiză critică proprie la FIECARE start frame/video înainte de livrare (regula 19 oct): ce nu pare real (mâini, priviri, fizică, efecte, logică) → refac singur, apoi trimit cu lista a ce am verificat.
Dacă pică, regenerează (max 3 încercări), apoi raportează.

## Halate noi — metoda Kling 4.0 (regula 24 oct, Szasz: „e genial”)
Pentru orice halat nou (ex. HeatPup), B-roll-ul și conector+telecomandă se fac cu **Kling 4.0 `video-edit`** pe clipurile noastre de mișcare (`library/motion/broll-standard-3-sofa-heatpup.mp4`, `library/motion/conector-telecomanda-ref4.mp4`), fără sunet, după șablonul `limitless/products/snoopy-robe/prompts/broll-kling4.txt`. Detalii complete: `limitless/docs/02-reguli.md` (24 oct). Direct 1080p, fără upscale (Szasz 24 oct). Genjutsu rămâne pentru HeatGrump unde merge; unde dă `ip_detected`, se trece pe Kling.

## Capcane cunoscute
- `ip_detected` la orice generare cu halat → NU se scad referințele (regula 20 oct: MEREU toate cele 4); te oprești și îl întrebi pe Szasz. Cozy cu unele personaje poate fi respins de 2 ori: schimbă clipul de mișcare.
- Clipurile de mișcare sub 2 s pică în Genjutsu (fără motiv afișat): B1 `ba61dc06` (0,9 s) și cozy `12959b84` (1,7 s) — scoase din rotație (2 oct). Folosește B1 `5133a653`, cozy `8042602c`.
- Fără `aspect_ratio` explicit iese 16:9. Fără `resolution` iese 720p.
- `nano_banana_2` = flash (slab). Dacă e nevoie de Nano Banana, cere `nano_banana_pro`.
- Creditele: workspace shared; motion control 1080p ≈ 44 credite/clip, seedance ≈ 55, gpt_image_2 4k ≈ 15. Verifică `balance` înainte de loturi mari.

## Dacă rulezi în Claude Code pe web (claude.ai/code)
Nu e nimic de instalat local; `setup-cloud.sh` a rulat deja (ffmpeg, yt-dlp). Token-urile vin din variabilele mediului, nu din `.env`. După fiecare lot: `git add -A && git commit -m "lot <data>" && git push`, ca Szasz să-și descarce MP4-urile din GitHub. Dacă un domeniu e blocat (eroare de rețea la apify/facebook/cloudfront), spune-i exact ce domeniu să adauge în *Allowed domains* ale mediului — nu încerca ocolișuri.
