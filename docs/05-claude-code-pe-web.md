# Claude Code pe web (fără să instalezi nimic pe calculator)

Totul rulează în browser, la **claude.ai/code**, pe un calculator din cloud al Anthropic (Pro/Max/Team). Pe calculatorul de la muncă nu se instalează nimic.

## O singură dată (≈10 minute)
1. **GitHub** (github.com, cont gratuit): *New repository* → nume `heatgrump-engine`, **Private** → *Create*. Apoi *uploading an existing file* → trage în pagină DOAR fișierul `heatgrump-engine.zip` (un singur fișier, nu folderul) → *Commit changes*. Dezarhivarea o face Claude Code în cloud, la primul mesaj (pasul 5).
2. **claude.ai/code** → conectează GitHub și alege repo-ul `heatgrump-engine`.
3. Apasă iconița de nor (mediul cloud) → **Add cloud environment**:
   - *Name*: `heatgrump`
   - *Network access*: **Custom**, bifează *Also include default list of common package managers*, și în *Allowed domains* lipește lista de mai jos.
   - *Environment variables*: `APIFY_TOKEN=...` (opțional și `META_PAGE_ID`, `META_IG_USER_ID`, `META_ACCESS_TOKEN`). Pe Pro/Max poți pune token-ul și la *API credentials*, mai sigur.
   - *Setup script*: conținutul fișierului `setup-cloud.sh`.
4. Activează conectorul **Higgsfield** pe sesiune (același pe care îl folosești în chat) — merge fără să adaugi domenii.
5. Pornește o sesiune și lipește ca prim mesaj:
   > dezarhivează heatgrump-engine.zip în rădăcina repo-ului (cu tot cu fișierele ascunse .claude și .mcp.json), șterge zip-ul, fă commit și push, apoi citește CLAUDE.md și rulează start
   De a doua oară scrii direct **`start`**.

## Allowed domains (lipește tot)
```
api.apify.com
*.apify.com
*.cloudfront.net
*.higgsfield.ai
*.facebook.com
*.fbcdn.net
*.instagram.com
*.cdninstagram.com
graph.facebook.com
*.pinterest.com
*.pinimg.com
*.youtube.com
*.googlevideo.com
*.ytimg.com
```

## Zilnic
- Deschizi sesiunea (sau o pornești din nou — repo-ul și tot ce ai salvat în el rămân; sesiunea se oprește când o închizi).
- `planul zilei` → `15 videouri` (sau `video nou` câte vrei). Claude cere soldul Higgsfield, verifică bugetul, generează, montează MP4-urile în `output/videos/` și face commit în repo. Le descarci din GitHub (sau din sesiune) și le termini în CapCut.
- `feedback` după ce ai postat (când avem token-urile Meta).

## Research automat, fără tine
În claude.ai/code → **Routines**: o rutină pe acest repo, zilnic la ora aleasă, cu promptul `research` (luni: research complet). Rulează singură în mediul `heatgrump` și face commit cu clipurile noi analizate; dimineața vezi rezultatul.

## Limite de știut
- O sesiune cloud nu stă pornită la nesfârșit: lucrul lung (generări, montaj) se face în sesiune, iar ce trebuie să ruleze singur se pune ca rutină.
- Fișierele mari (MP4-urile) e mai bine să le descarci regulat și să le ștergi din repo când nu le mai vrei, ca să nu umfle repo-ul.
