# HeatGrump Engine (handover din Cowork, 30 sept 2026)

Tot ce știe Claude despre producția de reel-uri HeatGrump, împachetat pentru Claude Code.

## Cum îl folosești
1. Dezarhivează folderul, deschide terminalul în el și rulează `claude`. Claude Code citește automat `CLAUDE.md`.
2. Serverul MCP Higgsfield e deja configurat în `.mcp.json`; la prima pornire aprobi și te loghezi cu `/mcp`.
3. Spune: „fă un lot de 5 reel-uri cu perechile din library/media.json” sau „propune hook-uri pentru reel 3”. Skill-urile din `.claude/skills/` știu pașii.

## Structura
- `CLAUDE.md` — regulile de lucru, citite automat.
- `docs/` — reguli consolidate, lecții tehnice, fluxul, produsul, specul, exportul brut din memorie.
- `library/` — ID-urile Higgsfield (produs, cutie, telecomandă, conector, clipuri de mișcare, personaje/camere) și biblioteca de hook-uri.
- `prompts/` — prompturile canonice (se copiază cuvânt cu cuvânt) + blocuri reutilizabile.
- `board/` — generatorul tablei HTML + datele lotului de 5 reel-uri din 23–29 sept.
- `state/jobs.json` — job ID-urile lotului curent.
- `.claude/skills/` — make-reel, hook-ideas, qa-check.

## Ce urmează (planul „motor”)
research (yt-dlp/Apify + analiză video) → playbook Esteban → hook-uri din bibliotecă cu scor → producție → QA vizual automat → feedback cu Meta Graph API → cron + Telegram.
