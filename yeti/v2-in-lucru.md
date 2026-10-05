# HeatYeti v2 — în lucru (5 oct 2026)
Regulile princesscomfortt aplicate pe toate 5 reel-urile Yeti.

## Joburi Higgsfield trimise (workspace Revive Root)
- 451 replace_object dB2 → halat Yeti (B2 cu fața): 83372b3e-34ac-486b-b3b2-cb2086148e6f
- Plăci hook (gata, în output/yeti-reelN/v2/placa-hook.png): 452 0289f994 · 453 7b9130f6 · 454 bf49ac5a · 455 c51f5b7f · 456 ed01efbb
- Video hook (seedance, cu sunet propriu):
  - reel1 tavă cuptor 22aa43bb-84ea-45ca-852a-1be7854075af
  - reel2 desfăcut pe pat 61df14fc-2675-4dbf-bf53-f9588ac12011
  - reel3 rulou cu fundă 9498b8e0-d144-4507-9732-1bc6f6896ae3
  - reel4 rulou aruncat 69ce2c15-07f2-465e-a43e-3d92beb3838a
  - reel5 aruncat ca pelerină 5cfda35a-7648-4827-a69c-fac08b5b8aef

## Pași rămași
1. Trimite B1 reel 1,3,4,5 (engine/batches/yeti/v2-b1-requests.json, indici 471/473/474/475). Reel 2 are deja b1-yeti-driving-443.mp4.
2. QA 451 → Genjutsu B2 cu fața pe toate 5 (5 s, video_references = 451; reel 5 cu mâneci albe simple).
3. QA hook/B1/B2 cadru cu cadru.
4. Montaj final.py (origin/main): hook → B1 → B2 întreg → conector → telecomandă → cozy ~2,5 s; fără unboxing; un singur text; muzică: r1 Wham 0.43, r2 Mariah 42.4, r3 Bublé 32.43, r4 Mariah, r5 Wham.
5. Tabla + commit + push.
