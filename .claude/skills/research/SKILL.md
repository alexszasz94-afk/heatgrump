---
name: research
description: Research automat pe Instagram, Facebook și Meta Ad Library (Apify): găsește reel-urile outlier din nișă, descarcă top clipuri și le pregătește pentru analiză. Rulează la „research” sau săptămânal.
---
1. Verifică `.env` are APIFY_TOKEN; dacă nu, explică-i lui Szasz pașii din START-AICI.md.
2. `python3 engine/research.py` (luni sau la cerere) / `python3 engine/research.py --light` (zilnic).
3. Dacă `instagram_competitors` / `facebook_pages` din `engine/config.yaml` sunt goale, completează-le din rezultatele hashtag-urilor: conturile cu cele mai multe outlier-e (max 10 fiecare) și spune-i lui Szasz ce ai adăugat.
4. Pentru fiecare clip nou din `library/clips/`: `python3 engine/prepare_clip.py <clip>` apoi skill `analyze-clip`.
5. Raportează: câte outlier-e, top 5 cu link + de ce au mers, ce s-a adăugat în bibliotecă.
