---
name: hook-ideas
description: Propune 3 hook-uri originale per reel (fără halat în cadru), fiecare cu start frame gpt_image_2, acțiunea de 4-5 s, textul CapCut în engleză + variantă, legătura cu B1 și motivul. Folosește și actualizează library/hooks-library.json.
---
# hook-ideas
1. Citește `library/hooks-library.json` (ce s-a folosit deja) și `library/playbook-esteban.md` dacă există.
2. Pentru reel-ul dat, scrie 3 idei, câte una de fiecare tip: problem-vs-solution, reacție/surpriză, neașteptat. Reguli: un singur start frame + o singură acțiune, cameră fixă, FĂRĂ halat, fără branduri reale, relatabil pentru public american iarna, comic sau „imposibil vizual”.
3. Pentru fiecare: `scene` (EN, 2-3 propoziții), `frame_desc` (RO), `motion` (RO), `line` (EN, text CapCut), `alt` (EN), `bridge` (cum taie în B1), `why` (RO).
4. Generează frame-ul cu `prompts/hook-image-template.txt` (medias: personaj, cameră; fără referințe de halat), 9:16, 4k.
5. Salvează în `board/hooks.json` sub reel-ul respectiv și adaugă cheile în `library/hooks-library.json`. Nu repeta idei între reel-uri.
