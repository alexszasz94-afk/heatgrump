# Rețeta unică pentru toate halatele (9 nov, Szasz)

(Căi: `library/...` = `heatgrump-studio/library/...`; clipurile de mișcare sunt în `../library/motion/` = `library/motion/` din rădăcina repo-ului.)

Același sistem pentru Grinch, Snoopy și toate halatele Prințesă. Se schimbă doar: halatul (poze produs), camerele (tema) și clipurile fixe (conector/telecomandă) ale produsului.

## Structura videoului (în ordinea de montaj)
1. **Hook** – copiat din viral (Kling 4.0 video-edit), aceeași fată ca în B-roll.
2. **B-roll (cozy inclus)** – MEREU clipul NOSTRU de mișcare `motion/grinch-v4.mp4` (8 s), ca la toate seturile Grinch:
   spate → își pune gluga → față, deschide halatul larg → bagă AMBELE picioare în săculeți → închide halatul → **cozy pe canapea** (6–8 s în clip).
   Kling 4.0 video-edit pe grinch-v4: schimbă doar fata, camera și halatul (pozele halatului: față, spate, glugă, deschis cu săculeți).
   Se taie doar ce e în plus (pauze, gluga trasă de două ori); nu se taie a doua băgare a piciorului.
3. **Conector** – clip fix al produsului (`products/<produs>/fixed/`).
4. **Telecomandă** – clip fix al produsului (`products/<produs>/fixed/`).
5. **Cozy = partea finală a B-roll-ului, MEREU PE CANAPEA (Szasz 10 nov).** În promptul B-roll-ului scrie mereu: „in the last shot she sits on the big beautiful sofa of the living room, hood up, and hugs herself inside the warm robe, smiling”. Stilul dorit = finalul reel-ului DcV9I_yN57e (14,9–17,1 s, `../library/motion/cozy-sofa-hug-DcV9I_yN57e.mp4`); alternativ Dc_2J9wNZPS. Dacă partea cozy din B-roll iese slab, se reface doar cozy-ul (video-edit pe clipul de cozy), tot pe canapea.

## Camere pe temă (4K, apus, elegante, neîncărcate, fără personaje/logo)
| Produs | Dormitoare (hook) | Living-uri cu canapea (B-roll întreg + cozy pe canapea) |
|---|---|---|
| Prințesă | `library/rooms-theme/printesa/printesa-01..05.jpg` | `printesa-06..10.jpg` |
| Grinch | `library/rooms-theme/grinch/grinch-01..05.jpg` | `grinch-06..10.jpg` |
| Snoopy | `library/rooms-theme/snoopy/snoopy-01..05.jpg` | `snoopy-06..10.jpg` |
Rezervă: `library/living-sofa/`, `library/rooms-sunset/`, `library/rooms-grinch/`.
B-roll-ul (cu cozy-ul pe canapea) se face într-un living al temei, ca grinch-v4 (se îmbracă în living, apoi cozy pe canapeaua aceluiași living). Hook-ul poate fi în dormitorul temei sau în același living.

## Halatele
- Grinch: `products/grinch/refs/` (front, back, side, hood, pockets_1/2, box).
- Prințesă – referințe curate per halat în `products/princess/refs/` (`<halat>-front/back/hood/open.jpg`, 1080p), făcute din pozele produsului.
- Prințesă – 4 variante (poze produs de la Szasz, 9 nov), `products/princess/variants/`:
  `ice-blue.jpg` (bleu cu broderie argintie), `golden-rose.jpg` (galben cu trandafiri), `snow-apple.jpg` (bleumarin sus / galben jos, fundă roșie), `green-lily.jpg` (verde cu nuferi).
  Telecomanda prințesei e cea cu ecran digital (86°F) din poze → clipurile fixe de telecomandă pentru prințesă trebuie să arate telecomanda asta.
- Snoopy: `products/snoopy/` (refs + fixed).

## Calitate (de verificat la fiecare clip, cadru cu cadru)
- aceeași fată în hook și B-roll; halatul = pozele produsului (culori, broderie, glugă, lungime până jos, săculeți);
- 9:16, 1080p, fără text ars, fără logo/branduri, fără personaje în decor;
- cozy: canapea mare frumoasă, gluga pe cap, se strânge în halat; fără gol/salturi la tăieturi (verificat la 30 fps).

## Ținuta de sub halat (10 nov, Szasz)
MEREU o pijama de Crăciun foarte drăguță, potrivită cu halatul, aceeași în hook, B-roll și cozy:
- Prințesă: pijama de satin roz/pastel cu coronițe mici și fundițe (sau culorile halatului);
- Grinch: pijama verde lime cu roșu, carouri/dungi, stil Grinch (fără personaj);
- Snoopy: pijama roșie/albă cu cățeluși mici și oscioare.

## Montaj fără cadre în plus (10 nov, Szasz)
La fiecare montaj de B-roll se verifică LA 30 FPS fiecare îmbinare (6 cadre înainte + 6 după): niciun cadru dintr-un alt plan (ex. primul cadru din cozy-ul propriu al B-roll-ului, un flash, alt unghi). Partea cu săculeții din grinch-v4 se taie la **5,70 s** (la 5,73 s apare deja cozy-ul B-roll-ului). Conector Snoopy 0,05–1,63, telecomandă 0,3–3,0.

## Cozy – picioarele acoperite (10 nov, Szasz)
În promptul de cozy scrie MEREU: „Her legs and feet are COMPLETELY covered by the long closed robe: the robe is wrapped closed over her knees and its hem falls down over her feet to the floor; no pajama pants, no knee, no sock and no foot is visible at any moment.”
Canapeaua = cea reală din camera originală (NU se refac camerele), descrisă exact în prompt: culoare, perne, pled, ce e în spatele ei.
- **Fără unghi în plus (10 nov, Szasz):** în B-roll nu are voie să se schimbe unghiul în timpul aceleiași mișcări. Kling mai bagă uneori un al doilea unghi (alt plan) peste aceeași mișcare → se caută la 10–30 fps și se TAIE din montaj; rămân doar planurile din clipul de referință, în ordinea lor.

## B-roll alternativ în rotație: reel DfdeJPkjuE4 (test 10 nov)
- Clip de mișcare: `../library/motion/broll-DfdeJPkjuE4.mp4` (5,0 s, mut; din reel 5,13–10,13): spate, își pune halatul (0–1,13) → față, gluga pe cap, deschide, piciorul drept în săculet, halatul larg deschis, piciorul stâng, închide. Kling video-edit, duration 5. Media: video, fata, livingul, halat front/back/hood (+ hood-up).
- Conector + telecomandă noi: `../library/motion/conector-telecomanda-DfdeJPkjuE4.mp4` (4,0 s; 0–1,33 conector alb în două părți, 1,33–2,67 mufa în sherpa, 2,67–4 telecomanda albă cu ecran 86°). Video-edit: mâinile fetei (scrie explicit „very fair, pale skin… no dark skin”, altfel rămân mâinile din original), stofa verde → stofa halatului.
- Halatul REAL de prințesă (din reel): interior alb pufos (sherpa), UN SINGUR săculet larg alb pe toată lățimea tivului, glugă mare ROTUNJITĂ cu bordură albă groasă și emblema sus deasupra frunții.
- Referințe glugă purtată (10 nov): `products/princess/refs/<halat>-hood-up.jpg` (job-uri: golden 1fcb438b, ice c63f81fd, snow 0e5c7675, green 7ac84995). Se atașează MEREU la B-roll și cozy. Grinch: `products/grinch/refs/hood.jpg`; Snoopy: kit `refs/hood.jpg` (ambele deja cu gluga purtată).

## Board Prințesă (10 nov) — 5 conturi × 4 halate, B-roll nou la toate
- Board: https://claude.ai/artifact/11pR6oHUpYqkZWPaz2XP4T (video + fata + camera la fiecare set). Planul și promptumile exacte: `output/boards/printesa/plan.json`.
- Montaj: B-roll nou DfdeJ (0–4,97) → conector + telecomandă de la ei, curățate de text (`../library/motion/conector-telecomanda-DfdeJ-curat.mp4`, 0–3,97) → cozy (0–2,97).
- Formulări care au rezolvat greșelile (se păstrează în toate prompturile):
  - săculet: „ONE single wide pouch … one piece from the left edge of the robe to the right edge; never two separate pouches, never booties, never slippers, never boots” (altfel ies 2 botoșei);
  - cozy pe canapea: „She sits ON THE LONG … SOFA OF IMAGE 2 … the sofa's seat cushion is under her, the sofa's backrest is directly behind her back … There is no pouf, no ottoman, no stool, no armchair and no round seat anywhere” (altfel inventează un taburet în mijlocul camerei — mai ales livingul printesa-08);
  - picioare: „At the bottom of the frame there is ONLY the robe and its white hem resting on the floor: no toes, no feet, no slippers, no socks and no pajama below the hem”.
- Verificare obligatorie pe fiecare set: cadre mari (jumătatea de jos) la 3,0 / 3,5 / 4,0 s (săculet) și 9,3 / 10,3 / 11,5 s (cozy) + fața la 2,2 s.
- Disc: videourile NU se mai urcă în git (umplu discul); merg direct în board.

## 10 nov (Szasz) — spatele glugii + conector unic
- Pe SPATELE glugii trebuie să fie emblema halatului (ca în reel, unde nufărul e pe spatele glugii): golden = tiara cu trandafir, ice = tiara cu cristal, snow = funda roșie cu volute aurii, green = nufărul. În prompt: „THE BACK OF THE HOOD: the <emblem> is clearly embroidered on the BACK of the hood, centred, big and visible when the hood hangs down her back” + în SHOT 1 „the hood down on her back with its embroidered emblem clearly visible”. Verificare: cadrele 10/20/30 (0,3–1,0 s) mărite.
- Gluga nu are voie să acopere ochii: „The hood sits back on her head: its front edge is ABOVE her eyebrows, her eyes, eyebrows and whole face are always clearly visible”.
- Conector + telecomandă UNIC pentru toate halatele: `../library/motion/conector-telecomanda-alb.mp4` (mână albă, doar sherpa albă în cadru, telecomanda cu ecran 86°), 0–3,97 în montaj.

## 10 nov — Grinch 5 conturi × 3 seturi (tabla https://claude.ai/artifact/2bDAHZ7a6YjVe7RfGu3JMZ)
- Plan + prompturi: `output/boards/grinch/plan.json` (generat de `make_plan.py`), joburi finale: `jobs.json` → `final`. Camere: dormitoare Grinch 01-05, living Grinch 06-10, living prințesă P06-P10.
- Ce a stricat Kling cel mai des și formula care a reparat:
  - gluga pe spate doar roșie (fără ochi): „From 0.5 s to 1.13 s the hood lies on her upper back with its GREEN GRINCH-FACE PANEL ON TOP, facing the camera … never folded with only its red side showing”.
  - gluga peste ochi: „the hood sits back on her head … white sherpa border at her hairline” (B-roll) / „pushed far back … border on top of her head, well above her forehead” (cozy). Fără descriere grea a glugii.
  - degete sub săculeți (mai ales camerele roz de prințesă): „the bottoms of both pockets … completely contain her feet: the floor around and in front of the pockets is empty”. Verifică MEREU banda de jos 2.6–5 s la 4 fps, mărit.
- Cozy: tăiem primele 0,6 s (stă aplecată, fața ascunsă). Montaj 11,37 s.
- Rată: ~1 din 3 B-roll-uri trece din prima; buget ~2,5 încercări / set.
- CORECTURĂ 10 nov seara (Szasz): fața Grinch e DOAR pe exteriorul glugii; interiorul glugii e verde simplu. Formula „GREEN GRINCH-FACE PANEL ON TOP … on the back” a făcut Kling să pună fața pe interior la TOATE cele 15 → anulată. Nouă: „THE INSIDE OF THE HOOD is plain green plush with NO face … WHEN THE HOOD HANGS DOWN HER BACK it looks exactly like Image 4 (red outside + pompom)”. QA: în shot 1 NU trebuie să apară ochi Grinch pe căptușeală.
