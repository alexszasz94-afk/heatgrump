# HeatYeti — copia HeatGrump cu halatul Yeti

Același motor, aceleași reguli, aceeași ordine de montaj (hook → unboxing → B1 → B2 → conector → telecomandă → cozy). Se schimbă doar produsul.

| Ce | Grinch (HeatGrump) | Yeti (HeatYeti) |
|---|---|---|
| Referințe halat | `library/media.json` → `product_grinch_refs` | `yeti/media.json` → `product_yeti_refs` (poze: `yeti/refs/yeti-ref1..4.png`) |
| Cutie | `5e8840d4` | `yeti/media.json` → `box` (poză: `yeti/refs/cutie-heatyeti.png`) |
| Descriere halat în prompturi | `prompts/blocks/robe.txt` | `yeti/prompts/blocks/robe.txt` |
| Prompturi | `prompts/` | `yeti/prompts/` (aceleași, cu halatul și manșeta Yeti) |
| Telecomandă / conector (clipuri fixe) | `library/media.json` → `fixed_clips` | `yeti/media.json` → `fixed_clips`, fișiere în `output/yeti-fixed/` |
| Rezultate reel-uri | `output/reelN/` | `output/yeti-reelN/` |

Comenzi: aceleași ca la Grinch, cu „yeti” în față — `yeti reel nou`, `yeti video nou`, `yeti 15 videouri`. Personajele, camerele și clipurile de mișcare sunt comune (din `library/`), dar un set folosit la Grinch nu se refolosește la Yeti în aceeași zi.

Descrierea produsului și QA: `yeti/01-product-yeti.md`.
`yeti/prompts/sleeve-swap.txt` — promptul folosit o dată ca să facem plăcile fixe Yeti din cele aprobate la Grinch (se schimbă doar manșeta).
