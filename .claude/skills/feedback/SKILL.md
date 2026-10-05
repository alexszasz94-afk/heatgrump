---
name: feedback
description: Trage cifrele reale de pe pagina de Facebook și Instagram (Meta Graph API), leagă reel-urile postate de videourile noastre, dă scor hook-urilor și spune ce funcționează. Rulează la „feedback” sau zilnic.
---
1. `.env` are META_PAGE_ID, META_IG_USER_ID, META_ACCESS_TOKEN? Dacă nu, explică-i pașii (Meta for Developers → app → Graph API Explorer → token cu pages_read_engagement, read_insights, instagram_basic, instagram_manage_insights; ID-urile din Business Suite).
2. `python3 engine/feedback.py pull`.
3. Leagă reel-urile de videourile din `state/videos.json`: Szasz postează cu caption-ul din .txt; potrivește după caption/dată și completează `posted: {"ig": id, "fb": id}`.
4. `python3 engine/feedback.py score` → top hook-uri. Spune-i în română: ce hook-uri câștigă, ce tip de hook, ce set a obosit, ce faci diferit mâine. Pentru top 3 videouri și bottom 3 rulează și `analyze-clip` (feedback) pe fișierele din `output/videos/`.
