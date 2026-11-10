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
