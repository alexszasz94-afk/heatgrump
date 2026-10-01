# START AICI — 5 pași, fără cunoștințe de Claude Code

1. **Dezarhivează** `heatgrump-engine.zip` undeva ușor de găsit (ex. Desktop).
2. **Deschide Terminal** (Mac: Cmd+Space → „Terminal”) și scrie `cd ` (cu spațiu), apoi trage folderul `heatgrump-engine` în fereastră și apasă Enter.
3. Scrie `bash setup.sh` și Enter. Instalează singur ce lipsește (Claude Code, ffmpeg, yt-dlp). Durează câteva minute prima dată.
4. Scrie `claude` și Enter.
   - Te întreabă dacă aprobi serverul MCP „higgsfield” din folder → **da**.
   - Scrie `/mcp`, alege **higgsfield**, apasă Enter → se deschide browserul → loghează-te în Higgsfield. Gata, o singură dată.
5. Scrie **`start`**. Claude verifică singur că totul merge (Higgsfield conectat, credite, ffmpeg) și îți spune ce poate face.

## Comenzi pe care le înțelege (scrii exact așa, în română)
- `start` — verificare + meniu.
- `reel nou` — îți cere perechile personaj + cameră (le pui în folderul `inbox/`), apoi face tot lotul.
- `hook-uri reel 3` — 3 idei de hook cu start frame pentru reel-ul 3.
- `animează hook 2 la reel 3` — animează hook-ul ales.
- `tabla` — regenerează și deschide tabla HTML.
- `analizează <link sau fișier>` — analizează un reel viral (FB/IG) și îl bagă în biblioteca de hook-uri.
- `feedback <fișier>` — analizează un reel de-al tău postat și spune ce să schimbi.
- `regula: ...` — adaugă o regulă nouă în `docs/03-rules.md` și `CLAUDE.md`.

## Dacă se blochează
- „higgsfield not connected” → scrie `/mcp` și loghează-te din nou.
- „out of credits” → încarcă credite în Higgsfield.
- Orice altceva → scrie `ce s-a întâmplat?` și Claude explică în română.


## Varianta și mai scurtă (dacă ai deja Claude Code instalat)
Dezarhivezi zip-ul, deschizi un terminal în folderul `heatgrump-engine` și scrii `claude`. Prima comandă pe care i-o dai: **„citește START-AICI.md și instalează tot ce lipsește, apoi rulează start”**. Claude Code citește singur `CLAUDE.md`, rulează `setup.sh`, îți cere token-ul de Apify și te duce pas cu pas. Nu trebuie să știi nicio comandă.


## Dacă NU poți instala nimic (ex. calculatorul de la muncă)
Totul merge și din browser, pe **claude.ai/code** — vezi `docs/05-claude-code-pe-web.md` (10 minute o singură dată: repo privat pe GitHub + un mediu cloud cu `setup-cloud.sh` și lista de domenii).
