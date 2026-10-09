# Pipeline-ul: fiecare pas manual → modul automat

Stare: ✅ automat în HeatGrump Engine · 🟡 parțial / cu Szasz în buclă · ⬜ de construit

| # | Pas | Cum se face azi (HeatGrump) | Modul LIMITLESS | Stare |
|---|---|---|---|---|
| 1 | Research virale | Apify IG/FB/Ad Library, outlier ≥ 3× media contului | `engine/research` | ✅ |
| 2 | Analiză viral | 8 cadre + audio, hook descris în format standard | `engine/analyze` | ✅ |
| 3 | Alegere hook | virale nefolosite din conturile de referință + hook-urile lui Szasz | `engine/hooks` (scor + rotație) | 🟡 |
| 4 | Seturi (personaj + cameră) | Pinterest, poze ≥ 1080 px | `engine/sets` | ✅ |
| 5 | Producție B-roll | Genjutsu motion control, clipuri de mișcare rotite | `engine/produce` | ✅ |
| 6 | Clipuri fixe | telecomandă / conector, după gen și piele | `library/fixed` | ✅ |
| 7 | Hook video | viral tăiat → Genjutsu cu setul nostru; fallback placă + seedance | `engine/produce` | ✅ |
| 8 | QA vizual | Claude cu vedere, reguli per clip, max 3 regenerări | `engine/qa` | ✅ |
| 9 | Montaj | tăieturi, text TikTok Sans, emoji, muzică de la secunda competitorului | `engine/edit` | ✅ |
| 10 | Postare | manual | `engine/publish` (IG/FB/TikTok programat) | ⬜ |
| 11 | Multi-cont | un cont | `engine/accounts` (variații per cont) | ⬜ |
| 12 | Feedback cifre | Meta Graph API, scor hook la 72 h | `engine/feedback` | 🟡 |
| 13 | Promovare hook | scor > mediană → dovedit | `engine/hooks` | 🟡 |
| 14 | Conversie | — | `engine/store` (pagina, oferta, A/B) | ⬜ |
| 15 | Produse noi | — | `products/` + `engine/product-scout` | ⬜ |
| 16 | Raport zilnic | tabla HTML | `engine/report` (dashboard + Telegram) | 🟡 |
