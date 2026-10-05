---
name: qa-check
description: Verifică vizual un frame sau clip generat pentru HeatGrump față de regulile din CLAUDE.md (halat, telecomandă, conector, unboxing, hook, format, text, lumină) și decide accept / regenerează cu motivul.
---
# qa-check
Input: URL sau fișier local (descarcă; pentru video extrage 6 cadre cu ffmpeg: 0%, 20%, 40%, 60%, 80%, 100%).
Verifică, în ordine, și răspunde cu JSON {pass: bool, issues: [...], fix: "..."}:
1. Format 9:16, fără text/emoji/watermark, fără logo de brand real.
2. Identitate: fața/părul = referința de personaj; camera = referința de cameră.
3. Halat (dacă apare): roșu sus + verde jos, glugă cu față verde, căptușeală verde, buzunare simple fără față, întreg până jos, manșete verzi pufoase.
4. Telecomandă: 5 luminițe vizibile; placă = toate stinse; video = una singură aprinsă, urcă 1→5.
5. Conector: gri, două părți; video = intră complet, fără gol, fără cut la final.
6. Unboxing: cutia pe podea; fața vizibilă; un singur produs; fereastra cutiei se golește când scoate halatul.
7. Hook: NICIUN halat/pătură cu glugă în cadru; acțiunea din frame corespunde ideii.
8. Lumină: o sursă motivată, umbre de contact, piele cu textură; fără „AI glow”, fără plastic, fără portocaliu excesiv.
Dacă pică: propune modificarea de prompt (bloc ABSOLUTE RULE) și regenerează; după 3 eșecuri raportează.
