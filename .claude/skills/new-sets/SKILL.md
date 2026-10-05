---
name: new-sets
description: Creează seturi noi (personaj + cameră + B-roll) când rotația le cere: camere și personaje luate direct de pe Pinterest (pozele exacte), apoi B-roll-ul complet. Rulează la „seturi noi” sau când rotation.py spune „de creat”.
---
Metoda de căutare și alegere de pe Pinterest vine din skill-ul `product-video-recast`: citește `.claude/skills/product-video-recast/references/research-and-board.md` (§Research method, §Select images that meet the brief, §Candidate record). Ca în acel skill: pozele alese de pe Pinterest SUNT referințele (cameră și personaj) — nu le înlocui cu personaje generate sau „inspirate” (regula lui Szasz, 1 oct; videourile nu se postează). Fișierul `esteban-visual-standard.md` e al altui client și nu se aplică aici.

1. `python3 engine/rotation.py status` → câte seturi trebuie.
2. Adună candidați de pe Pinterest:
   - cu `APIFY_TOKEN`: `python3 engine/pinterest.py rooms 12` și `python3 engine/pinterest.py characters 12` → poze în `library/rooms/` și `library/char-inspiration/`;
   - fără token: caută direct pe Pinterest (browser Playwright/Chromium sau căutare web), deschide pin-urile la mărime utilizabilă, descarcă doar pozele alese în aceleași foldere și notează-le în `index.json` (pin URL, sursa originală dacă se vede, data).
   Dacă Pinterest e blocat de rețea, spune-i lui Szasz exact domeniile de adăugat la *Allowed domains* (`*.pinterest.com`, `*.pinimg.com`, plus `*.apify.com` pentru varianta cu token) — nu încerca ocolișuri.
   Căutările pornesc de la ce cere clipul (B1/B2/cozy: cameră luminoasă, podea vizibilă, loc pentru om în picioare și pe pat/canapea, brad sau pat vizibil), nu doar de la cuvântul „living room”. Dacă toate rezultatele au același defect, schimbă căutarea.
3. Alege cu tabelul din research-and-board.md (strong / usable cu limită concretă / reject). Cameră: luminoasă, culori vii semicalde, adâncime clară, fără persoane, fără text/logo, fără branduri, să nu pară generată AI. Un defect de bază = respinsă, oricât de frumoasă.
4. Cameră: încarcă poza aleasă în Higgsfield (media_upload → PUT → media_confirm) și folosește-o direct.
5. Personaj: folosește direct poza aleasă de pe Pinterest ca referință de personaj (media_upload → PUT → media_confirm). Alege după §Select images: o singură persoană, poză candid (nu ședință foto de modă), față mare, clară, neacoperită, unghi frontal/3-4, corp vizibil cât cere clipul, lumină bună, fără text/logo, să nu pară generată AI; băiat/fată clar. Nu genera un personaj nou; dacă nicio poză nu trece, spune ce lipsește și caută din nou. Alternează bărbați/femei și vârste.
6. Îmbrăcăminte pentru set: alege una (pijama de Crăciun / America / stil american / cozy), diferită de seturile active.
7. Arată-i lui Szasz o tablă scurtă cu imagini: camera aleasă + personajul ales, linkul fiecărui pin și de ce a fost aleasă; respinsele marcate ca respinse. Dacă i-a delegat alegerea, continuă fără să mai aștepți.
8. Rulează skill `make-reel` doar pentru B-roll (B1, B2, cozy, conector, telecomandă, unboxing), apoi `python3 engine/rotation.py add '<json set>'` cu ID-urile și link-urile clipurilor.
