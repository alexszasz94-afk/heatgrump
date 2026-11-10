# Rețeta unică pentru toate halatele (9 nov, Szasz)

(Căi: `library/...` = `heatgrump-studio/library/...`; clipurile de mișcare sunt în `../library/motion/` = `library/motion/` din rădăcina repo-ului.)

Același sistem pentru Grinch, Snoopy și toate halatele Prințesă. Se schimbă doar: halatul (poze produs), camerele (tema) și clipurile fixe (conector/telecomandă) ale produsului.

## Structura videoului (în ordinea de montaj)
1. **Hook** – copiat din viral (Kling 4.0 video-edit), aceeași fată ca în B-roll.
2. **B-roll** – exact ca referința `../library/motion/broll-ref-DcV9I_yN57e.mp4` (reel https://www.instagram.com/p/DcV9I_yN57e/, 4,2–11,1 s):
   spate → își pune gluga → față, deschide halatul larg → bagă AMBELE picioare în săculeți → închide halatul.
   Se taie doar ce e în plus (pauze, gluga trasă de două ori); nu se taie a doua băgare a piciorului.
3. **Conector** – clip fix al produsului (`products/<produs>/fixed/`).
4. **Telecomandă** – clip fix al produsului (`products/<produs>/fixed/`).
5. **Cozy** – MEREU pe canapea, ca finalul reelurilor de referință:
   - principal: `../library/motion/cozy-sofa-hug-DcV9I_yN57e.mp4` (DcV9I_yN57e 14,9–17,1 s): cu gluga pe cap se așază pe canapea, se strânge în brațe în halat, mulțumită;
   - alternativ: `../library/motion/cozy-sofa-plop-Dc_2J9wNZPS.mp4` (Dc_2J9wNZPS 12,4–14,6 s): se lasă într-o parte pe canapea.
   Canapeaua = canapeaua frumoasă dintr-un living al temei (vezi mai jos), la apus.

## Camere pe temă (4K, apus, elegante, neîncărcate, fără personaje/logo)
| Produs | Dormitoare (hook + B-roll) | Living-uri (cozy pe canapea) |
|---|---|---|
| Prințesă | `library/rooms-theme/printesa/printesa-01..05.jpg` | `printesa-06..10.jpg` |
| Grinch | `library/rooms-theme/grinch/grinch-01..05.jpg` | `grinch-06..10.jpg` |
| Snoopy | `library/rooms-theme/snoopy/snoopy-01..05.jpg` | `snoopy-06..10.jpg` |
Rezervă: `library/living-sofa/`, `library/rooms-sunset/`, `library/rooms-grinch/`.
Un set = aceeași cameră-temă pentru hook și B-roll; cozy într-un living din aceeași temă.

## Halatele
- Grinch: `products/grinch/refs/` (front, back, side, hood, pockets_1/2, box).
- Prințesă – 4 variante (poze produs de la Szasz, 9 nov), `products/princess/variants/`:
  `ice-blue.jpg` (bleu cu broderie argintie), `golden-rose.jpg` (galben cu trandafiri), `snow-apple.jpg` (bleumarin sus / galben jos, fundă roșie), `green-lily.jpg` (verde cu nuferi).
  Telecomanda prințesei e cea cu ecran digital (86°F) din poze → clipurile fixe de telecomandă pentru prințesă trebuie să arate telecomanda asta.
- Snoopy: `products/snoopy/` (refs + fixed).

## Calitate (de verificat la fiecare clip, cadru cu cadru)
- aceeași fată în hook și B-roll; halatul = pozele produsului (culori, broderie, glugă, lungime până jos, săculeți);
- 9:16, 1080p, fără text ars, fără logo/branduri, fără personaje în decor;
- cozy: canapea mare frumoasă, gluga pe cap, se strânge în halat; fără gol/salturi la tăieturi (verificat la 30 fps).
