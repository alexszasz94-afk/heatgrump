# Sarcină pentru sesiunea LOCALĂ (pe laptopul lui Szasz): 50 B-roll-uri Frost Femme, 720p, Higgsfield UNLIMITED

Vorbește cu Szasz în română, simplu. El vrea să lase laptopul să lucreze singur.

## Regula de bani (cea mai importantă)
- Se lucrează DOAR în browserul lui (Claude in Chrome / browserul din Claude), pe higgsfield.ai, unde e logat.
- Înainte de PRIMA generare verifică că Seedance 2.5 la 720p arată **Unlimited** / cost 0 credite.
  Dacă arată credite → OPREȘTE și spune-i lui Szasz. Nu cheltui niciun credit. Nu folosi MCP-ul Higgsfield (acela plătește credite).
- Verifică soldul de credite la început și după primele 2 videouri: trebuie să rămână la fel.

## Ce ai în folderul ăsta (output/afnska/kit-local/)
- `miscare-r3.mp4` – reelul original (fără sunet), referința de mișcare (13 s, 9 tăieturi).
- `fete/` 25 fete (pijamale de Crăciun din satin), `camere/` 20 camere de Crăciun.
- `*-fisa.jpg` fișa hainei pe culori (Hourbelle) + `03-black-spate-corset.jpg` (spatele cu șiret corset – pune-l MEREU).
- `prompt-seedance.txt` – promptul pe secunde. Se înlocuiesc doar <FATA>, <PIJAMA>, <CAMERA>, <CULOARE> (descrie-le scurt, în engleză, uitându-te la poze).
- `lista-50.csv` – cele 50 de combinații (fată + cameră + culoare + nume fișier).

## Setări pe higgsfield.ai
Seedance 2.5 · referințe (omni reference): video = `miscare-r3.mp4`; imagini în ordine: fata, camera, fișa culorii, spate-corset ·
9:16 · 720p · 13 s · fără sunet generat · Unlimited.
(Dacă pozele sunt deja în Assets-ul contului Higgsfield, folosește-le de acolo; altfel încarcă-le din folder.)
Fără text în imagine, fără zoom, fără branduri.

## Flux
1. Pornește câte generări în paralel permite unlimited; ține evidența în `progres.csv` (nr, stare, link).
2. Când e gata, descarcă MP4-ul în `~/Downloads/FrostFemme-broll/` cu numele din `lista-50.csv`.
3. QA rapid (uită-te la 4 cadre): haina = culoarea cerută, corset la spate, fata = referința, camera = referința, fără text, mișcări ca originalul. Dacă pică → refă o dată.
4. Dacă există ffmpeg: rulează `bash grade.sh <out.mp4> <fișier>` pentru culoarea ca în original (opțional).
5. La final: raport scurt pentru Szasz (câte gata, câte refăcute, unde sunt). MP4-urile NU se pun pe GitHub; doar `progres.csv`.
