# START AICI

Sistem automat de reel-uri pentru halatul tău termic. Tu dai comenzi în română; Claude face clipurile în Higgsfield, le verifică, le montează și îți dă MP4-ul gata.

## Ce îți trebuie (o singură dată)
- **Claude** cu abonament Pro sau Max, aplicația de calculator (claude.ai/download).
- **Higgsfield** cu credite (higgsfield.ai). Un reel complet consumă cam 300-500 de credite.
- **Apify**, cont gratuit pe apify.com. Opțional: e folosit pentru pozele de pe Pinterest și pentru research.

## Pornire (≈10 minute)
1. **Dezarhivează** zip-ul undeva ușor de găsit (ex. Desktop). Iese folderul `heatrobe-engine`.
2. **Conectează Higgsfield** la Claude: în aplicația Claude → *Settings* → *Connectors* → caută **Higgsfield** → *Connect* → te loghezi în contul tău Higgsfield.
3. Deschide aplicația Claude → tabul **Code** → alege folderul `heatrobe-engine` (*Open folder* / *Select folder*).
   - Dacă te întreabă de serverul „higgsfield” din folder → **da** (sau ignoră-l, dacă ai făcut pasul 2).
   - Dacă te întreabă dacă are voie să ruleze comenzi / să modifice fișiere în folder → **da / allow**.
4. Scrie **`start`**.
   La prima pornire, Claude face singur instalarea: încarcă toate referințele (pozele halatului, cutia, telecomanda, conectorul, clipurile de mișcare și 15 seturi personaj + cameră) în contul tău Higgsfield și te întreabă cum e halatul tău. Dacă e alt model, îți cere câteva poze cu el și adaptează totul.
5. **(Opțional) Apify**: pe apify.com → *Settings* → *API & Integrations* → copiezi token-ul. În folderul `heatrobe-engine` copiezi fișierul `.env.example` ca `.env` și pui token-ul după `APIFY_TOKEN=` (sau îi spui lui Claude „pune token-ul de Apify” și te ghidează). Nu-l trimite în chat.

Dacă lipsesc programe (ffmpeg, yt-dlp, python), spune-i lui Claude „instalează ce lipsește”; are scriptul `setup.sh` pentru asta.

## Comenzi (le scrii exact așa)
- `start` — verificare + meniu.
- `video nou` / `15 videouri` — face videouri complete, gata de postat.
- `reel nou` — un reel din perechea personaj + cameră pusă în `inbox/` (`reel1-personaj.jpg` + `reel1-camera.jpg`).
- `seturi noi` — personaje + camere noi de pe Pinterest (cu Apify).
- `planul zilei` — cele 15 videouri ale zilei.
- `hook-uri reel 3` / `animează hook 2 la reel 3` — idei de hook și animarea celui ales.
- `tabla` — tabla cu toate clipurile.
- `analizează <link sau fișier>` — analizează un reel viral și îl pune în biblioteca de hook-uri.
- `research` — caută reel-uri virale din nișă (cu Apify).
- `regula: ...` — îi dai o regulă nouă, o ține minte pentru totdeauna.

## Dacă se blochează
- „higgsfield not connected” → reconectează Higgsfield din *Settings* → *Connectors*.
- „out of credits” → încarcă credite în Higgsfield.
- Orice altceva → scrie `ce s-a întâmplat?` și Claude explică în română.
