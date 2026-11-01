# PLAN — 175 videouri / săptămână (25 / zi), low cost
Prețuri reale verificate pe 1 nov 2026 (`get_cost`): **Kling 4.0 = 3,25 credite/s la 1080p, 2,25 credite/s la 720p** (mai ieftin decât cele 4/s estimate); gpt_image_2_5 4k = 4,25. Sold la 1 nov: **4.256 credite**.

## Ce costă și ce e gratis într-un video (~15 s)
| Bucată | Sursă | Credite |
|---|---|---|
| Hook 3-4 s | Kling 4.0 video-edit, NOU la fiecare video | 9 (720p) / 13 (1080p) |
| B1 + B2 + cozy | set de B-roll refolosit la 7 videouri | ~10 / video |
| Conector + telecomandă | clipuri fixe | 0 |
| Montaj, text, muzică | ffmpeg local (`engine/studio.py montaj`) | 0 |
**~70% din fiecare video e deja făcut.** Singurul cost real e hook-ul.

## Variante (`python3 heatgrump-studio/engine/cost.py`, cu 30% reîncercări incluse)
| Variantă | credite/video | /zi (25) | /săptămână (175) |
|---|---|---|---|
| A 1080p tot, hook 4 s, B-roll ×5 | 31 | 780 | 5.460 |
| B 1080p tot, hook 3 s, B-roll ×7 | 23 | 572 | 4.006 |
| **C hook 720p 4 s, B-roll 1080p ×7 (RECOMANDAT)** | **22** | **548** | **3.835** |
| D 720p tot, hook 3 s, B-roll ×7 | 17 | 414 | 2.901 |
| E 720p tot, hook 3 s, B-roll ×10 | 14 | 356 | 2.491 |

**Recomandare: C.** Hook-ul la 720p se vede aproape la fel pe telefon (e o acțiune scurtă, mișcată), iar B-roll-ul — unde trebuie să se vadă halatul perfect — rămâne 1080p. Sub C (720p la B-roll) halatul iese moale; nu recomand.
Soldul de azi (4.256) ajunge pentru ~1 săptămână pe varianta C. Credite pe lună ≈ 16.500.

## Structura săptămânii
- **Seturi B-roll**: 175 / 7 = **25 seturi pe săptămână** (~4 pe zi). Fiecare set = personaj nou + cameră nouă + ținută americană. Rezervă: 47 camere și 48 personaje ≥1080 px deja în `library/` (destul pentru ~2 săptămâni), apoi `new-sets` (Pinterest).
- **Hook-uri**: 175 hook-uri video pe săptămână, dar din **~25 concepte** (fiecare viral bun refăcut pe 5-7 seturi diferite, nu în aceeași zi pe același set). Concepte: 5 dovedite + virale din `HOOKS.md` + linkurile lui Szasz.
- **Clipuri fixe**: lipsește doar varianta femeie piele închisă (~41 credite, o singură dată).

## Ziua (lot zilnic, automat)
| Pas | Ce | Timp |
|---|---|---|
| 1 | `balance` + `studio.py plan 25` | 1 min |
| 2 | 4 seturi B-roll noi (12 joburi Kling într-un batch) | ~20 min așteptare |
| 3 | 25 hook-uri: tăiere + upload local, apoi 3 batch-uri de câte 12/12/1 | ~30-40 min |
| 4 | QA cadru cu cadru (Claude) + reîncercări | ~30 min |
| 5 | 25 montaje (ffmpeg, ~20 s fiecare) | ~10 min |
| 6 | commit + push, trimitere fișiere | 5 min |
Total ≈ 2 ore de rulare pe zi, fără muncă manuală, în afară de alegerea linkurilor (opțional).

## Ce trebuie aprobat de Szasz înainte de lot
1. **Set refolosit de 7 ori** (regula veche din `engine/config.yaml`: max 4). Cu 4 → 44 seturi/săpt., costul urcă la ~26 credite/video.
2. **Hook-uri la 720p.**
3. **Kling 4.0 în loc de Seedance/Genjutsu** pentru halate (CLAUDE.md din rădăcină spune încă Seedance/Genjutsu).
4. Același concept de hook refolosit pe 5-7 seturi (regula din 5 oct spunea „hook-uri noi la fiecare lot”).
