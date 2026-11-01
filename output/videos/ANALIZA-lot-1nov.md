# Analiza lot 1 nov (10 videouri Grinch) — dupa metoda din HOOKS.md / CLAUDE.md 9e-9o

## Ce spun originalele (audio3 + tools.py cuts)
| Link | Hook se termina la | Sunet original (cine ce spune, secunde) | Text original exact |
|---|---|---|---|
| r1 (tava pe halat) | 4.23 s | barbat: "three (0.10), two (1.17), one (1.61), let's see how it turns out (2.97-4.22)" | Imagine this on the first\nsnow day.. 😌❄️☃️ |
| r2 (mangaie halatul) | 5.00 s | voce: "Three (0.37), two (1.40), one (2.26), let's see how it turns out (3.16-4.95)" | I'm literally crying 😭 |
| r3 (desface cu piciorul) | 4.97 s | aceeasi voce: "3 (0.26), 2 (1.28), 1 (2.15), let's see how it turns out (3.05-4.96)" | "Moms are so hard to gift"\n🤶❄️🥹 |
| r4 (tava, bucatarie) | 5.33 s | barbat: "Three (0.30), two (1.48), one (2.13), let's see how it turns out (3.47-5.32)" | Imagine this on day 2\nof your period..😳🩸 |
| r5 (desface cu piciorul) | 5.40 s | femeie: "One (0.59), two (1.86), three (2.92)" | Christmas-holics this is\nfor YOU..🎄🎅 |
| r6 (rulou aruncat) | 4.07 s | femeie: "One (0.89), two (2.05), three! (3.43)" | DONT show this to\nyour mom😳❄️ |
| r7 (punga HEAT GRUMP) | 4.90 s | melodia "You're a mean one, Mr. Grinch" (cantec, nu vorbire) | "Babe you don't\nneed that..." 🙄  +  separat, stanga: Me: 🥺💚 |

## Greseli gasite in hook-urile noastre
1. SUNET (toate): am cerut "fara voce". In 6 din 7 originale se numara "3,2,1 / let's see how it turns out" sau "1,2,3" -> la noi lipseste complet (compare-audio: toate cuvintele "ours --"). Regula 9d: niciodata hook mut cand originalul vorbeste.
   - v01, v02: Kling a pus voci inventate ("What?", "Whites? Drooms?").
   - v03, v05: spectrograma arata tonuri continue (posibil fond muzical).
2. LUNGIMEA HOOK-ULUI (regula 9o): v08 taiat la 3.8 s in loc de 4.23; v09 la 4.2 in loc de 5.33 -> lipseste momentul in care tava e trasa si se vede halatul. v01/v02 4.0 vs 4.07, v03-v06 4.9 vs 5.0/4.97, v07 5.3 vs 5.4, v10 4.85 vs 4.9.
3. HARTA OBIECTELOR (9h): v08, v09 — in original tava e GOALA (fara gheata) pusa pe halatul IMPATURIT; la noi am inventat gheata/zapada pe tava, iar la v08 halatul e intins cu fata in sus (nu impaturit).
4. PERSONAJUL (regula 2 / 9i): in hook-urile POV (v05-v10) n-am dat poza personajului ca referinta. v08, v09 au maini de barbat (personajul e femeie). v10: maneca crem, dar in B-roll ea poarta hanorac bleumarin.
5. LOGICA HOOK -> B-ROLL: v01 hook-ul se termina cu ea deja IMBRACATA in halat, apoi B-roll-ul arata cum il imbraca -> se repeta. In original (r6) halatul doar cade desfacut in fata ei, nu il poarta.
6. TEXT (regula: cuvant cu cuvant, aceleasi emoji si randuri): v04, v02, v06 au texte inventate; emoji gresite la v05 (😩❄️ in loc de 🤶❄️🥹), v07 (lipsesc ".."), v08 (😮‍💨❄️ in loc de 😌❄️☃️), v09 (🩸😩 in loc de 😳🩸), v10 (😏 in loc de 🙄 si "Me: 🥺💚" trebuie separat, in stanga), v01/v02 fara rupere de rand.

## Ce e OK
- Miscarea (compare 10 fps) la v01-v07 si v10 urmeaza originalul.
- Halatul arata corect (gluga cu fata, rosu/verde, mansete lime).
- Camerele si hainele la v01-v07 continua din hook in B-roll.
- B-roll, conector, telecomanda, cozy, muzica pe drop: OK.

## Refacut (1 nov, seara)
- Toate 10 hook-urile regenerate cu Kling 4.0: vocea originalului (3-2-1 / let's see how it turns out, 1-2-3), poza fetei din set ca referinta, hainele setului, camera setului, cronologia la secunda, lungimea exacta a originalului (retime).
- v08 refacut a doua oara (tava goala pe halatul impaturit, ca in original).
- v05, v06, v07, v08, v09: Kling a pus vocea cu 0.5-1 s mai tarziu -> mutata doar vocea (stem demucs, `engine/vshift.py`), sunetele actiunii si fondul raman pe loc; dupa mutare toate cuvintele sunt la max 0.3 s de original (compare-audio).
- Golurile de liniste: `tools.py roomtone`. Fara muzica in hook (spectro); muzica noastra cu drop pe taietura.
- Textele: cuvant cu cuvant, aceleasi emoji si randuri; v10 are "Me: 🥺💚" separat, in stanga, ca in original.
