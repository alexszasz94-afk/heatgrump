---
name: instalare
description: Prima pornire a sistemului la un proprietar nou: încarcă toate referințele din folderul referinte/ (produs, cutie, telecomandă, conector, clipuri de mișcare, seturi personaj+cameră) în contul lui Higgsfield, pune ID-urile noi peste tot și află cum e halatul lui. Rulează singur la `start` cât timp library/media.json are "_instalare" diferit de "gata", sau la `instalare`.
---
Vorbește cu proprietarul în română, simplu, fără jargon. Nu-i cere comenzi de terminal.

## 1. Cunoaște-l
- Întreabă-l cum îl cheamă și cum se numește brandul/pagina lui. Scrie numele în `CLAUDE.md` la „Proprietar:”. În toate fișierele, „Szasz” = proprietarul (sistemul a fost construit de Szasz).
- Verifică Higgsfield: apelează `balance`. Dacă nu merge, explică-i pașii din `START-AICI.md` (conectarea Higgsfield) și oprește-te până e conectat.

## 2. Încarcă referințele în Higgsfield-ul lui
Toate fișierele sunt în `referinte/` și sunt descrise în `referinte/manifest.json`.
1. `python3 engine/import_refs.py lista` → următoarele max 20 fișiere de încărcat (file, type, old_id).
2. `media_upload` cu `files: [{filename: <numele fișierului>}, ...]` pentru acel grup → primești câte un `upload_url` și `media_id`.
3. Pentru fiecare: `curl -sS -X PUT -H "Content-Type: <image/png | image/jpeg | video/mp4>" --data-binary @<file> "<upload_url>" -o /dev/null -w "%{http_code}"` — trebuie 200.
4. `media_confirm` cu `media_ids` (separat `type: "image"` pentru poze și `type: "video"` pentru clipuri).
5. `python3 engine/import_refs.py set <old_id> <media_id> <old_id> <media_id> ...` pentru tot grupul.
6. Repetă de la 1 până scrie „rămase: 0”. Dacă un fișier eșuează, reîncearcă o dată, apoi spune-i care.
7. `python3 engine/import_refs.py aplica <URL-ul unei poze încărcate>` (URL-ul îl iei din `show_medias` sau din răspunsul la confirm). Asta pune ID-urile noi în `library/media.json`, în documente și în tablă.
Spune-i scurt: „Am încărcat N poze și M clipuri în contul tău Higgsfield.”

## 3. Halatul lui
Arată-i pozele din `referinte/produs/` (halatul, cutia, telecomanda, conectorul) și întreabă: „Halatul tău e exact acesta, cu aceeași cutie, telecomandă și conector?”
- **Da, identic** → nu schimbi nimic. Clipurile fixe din `output/fixed/` (telecomandă, conector) se folosesc direct.
- **Seamănă, dar alt brand / altă cutie** → cere-i 1-3 poze cu cutia lui (le pune în `inbox/`), încarcă-le, pune ID-ul nou la `box` în `library/media.json`. Restul rămâne.
- **Alt halat** → cere-i 4-6 poze clare cu halatul lui (față, spate, gluga, căptușeala, deschis/închis, fundal simplu), plus telecomanda și conectorul dacă are. Încarcă-le și înlocuiește în `library/media.json`: `product_grinch_refs`, `box`, `controller_real`, `connector_ref`. Rescrie `docs/01-product-grinch.md` cu descrierea halatului lui (culori, căptușeală, glugă, buzunare, telecomandă: câte luminițe), apoi caută în `prompts/` și `docs/03-rules.md` descrierile vechi (roșu cu alb, căptușeală verde olive, 5 luminițe, conector gri, Grinch) și adaptează-le la halatul lui. Spune-i că telecomanda și conectorul din `output/fixed/` arată halatul vechi și că le refaci la primul `reel nou` (placă gpt_image_2 → video seedance_2_5, prompturile controller-/connector-). Dacă halatul lui n-are telecomandă sau conector, scoate acele clipuri din ordinea de montaj în `CLAUDE.md`.
Notează decizia, datată, în `docs/03-rules.md`.

## 4. Restul
- Apify (pentru Pinterest și research): dacă nu are `APIFY_TOKEN`, explică-i pașii din `START-AICI.md`; fără el merge totul în afară de `seturi noi` automat și `research`.
- Seturile din `referinte/seturi/` (15 perechi personaj + cameră) sunt gata de folosit: le poate folosi la `reel nou` (copiază perechea în `inbox/` ca `reelN-personaj` / `reelN-camera`), ID-urile lor sunt în manifest (`new_id`).
- La final arată-i meniul de comenzi din `START-AICI.md` și întreabă-l cu ce începe.
