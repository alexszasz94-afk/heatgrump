# Metoda „un click” — cum iese un video perfect de fiecare dată (30 oct)

Sinteza a tot ce am învățat din teste (lot29–lot33, kit-test, testul Kling vs Seedance). Asta e metoda; kitul creatorilor o aplică pas cu pas.

## Principii (de ce iese perfect)
1. **Nimic din ghicit.** Totul pleacă din analiza originalului, cadru cu cadru + analiza Higgsfield (obligatorie, salvată în `ref/analysis-<id>.json`): cine vorbește și ce cuvinte la ce secunde (sau doar melodie), fiecare tăietură, încotro e întoarsă persoana, ce parte a produsului se vede, cine ține ce.
2. **Prompturi înghețate.** Fiecare tip de clip are rețeta lui în `recipes/` — promptul cuvânt cu cuvânt, ordinea referințelor, setările. Se schimbă doar `<...>`. O corectură nouă intră întâi în rețetă, datată.
3. **Un singur model video: Kling 4.0, 1080p, 9:16.** `video-edit` pe originalul FĂRĂ sunet (mișcarea și secundele vin din clip, nu din prompt). Vocea, când există, o face Kling în aceeași generare (cuvintele + secundele în prompt; propozițiile cerute cu ~0,4 s mai devreme). Fără Seedance, fără Genjutsu, fără start frame la hook (strică ritmul la Kling).
4. **Imagini doar GPT Image 2.5** (high, 9:16, 4k): camere, variante de cameră, cutii cu logo.
5. **Produsul doar din referințe.** Halatul/cutia nu se descriu în cuvinte: „REPRODUCE IT ONE TO ONE from Images N–M”, cu toate referințele. Poza personajului e mereu referință directă.
6. **Verificare în detaliu, mereu** (regula 30 oct): înainte de prompt — originalul la 4 fps; după generare — rezultatul lângă original (primele secunde la 4 fps, tăieturile la 10 fps, săculeții la 6 fps). Refacere automată, max 2–3 încercări; nimic nu se livrează neverificat.

## Pașii „click-ului” (ce face Claude singur la un link de reel)
1. Descarcă originalul → analiza Higgsfield + transcriere → fișa reel-ului (scene pe secunde, voce/melodie, obiecte și roluri: produs / cutie / recuzită).
2. Alege setul prin rotație (`next-set`): fată nouă (reală, ≥ Full HD, verificată cu photo-ok + ochii), cameră nouă din setul 4K (podea liberă în față, canapea pentru cozy), varianta de B-roll (1 din 4, niciodată aceeași de 2 ori la rând), conectorul/telecomanda, melodia (alta decât la ultimele 2).
3. Hook: originalul tăiat la secunde întregi, fără sunet → Kling video-edit cu rețeta + fișa (persoana = Image 1, camera = Image 2, produsul = referințele, textul lor șters). Verificare lângă original → refacere dacă nu e geamăn.
4. B-roll: rețeta fixă a variantei, cuvânt cu cuvânt (doar `<OUTFIT>`, `<rug|floor>` schimbate). Verificare: picioare ÎN săculeți (6 fps), interiorul halatului, gluga în toate cadrele.
5. Montaj standard: hook → îmbrăcat → săculeți → conector → telecomandă → cozy, pe secundele originalului. Sunet: DOAR muzica (originale doar cu melodie) — melodia de la secunda `drop − secunda reveal-ului`, volum egalizat, fade la final; la hook cu voce, vocea Kling rămâne deasupra, muzica încet sub ea până la tăietură. Fără sunetele de cameră ale lui Kling.
6. Text pe ecran: al originalului, cuvânt cu cuvânt, cu produsul/personajul schimbat pe al nostru; pe tot videoul, sus. (În kit: fără text ars — creatorul îl pune în CapCut; la noi: ars în montaj.)
7. QA final pe videoul întreg (tăieturi, sunet transcris, lungime ca originalul) → livrare cu lista a ce s-a verificat → commit + push.

## Costuri de referință (ca să știm când ceva e anormal)
Kling 1080p = 4 credite/s (hook 4 s ≈ 16, B-roll 7 s ≈ 28); GPT 4k ≈ 4/poza; video complet ≈ 50–70; cu o refacere ≈ 90–100.

## Capcane știute (se verifică mereu)
- Kling desface ruloul prea devreme → încetinește începutul până cade pe secunda originalului.
- Degete/ciorapi sub săculeți → blocul FEET REALLY INSIDE + verificare la 6 fps; dacă scapă, zoom 1.18x ancorat sus sau refacere.
- Propozițiile vorbite ies cu ~0,4 s întârziere → se cer mai devreme în prompt.
- Snoopy/Grinch pot da ip_detected la alte modele — încă un motiv pentru „doar Kling”.
- Uneltele locale de sunet „aud” voce în melodii → vocea există doar dacă o confirmă analiza Higgsfield.
