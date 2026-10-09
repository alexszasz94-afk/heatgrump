# LIMITLESS — instrucțiuni pentru Claude Code

Proprietar: Szasz. Vorbește cu el în română, simplu, fără jargon. Textul de marketing (replici, text pe ecran, caption-uri) e în engleză.

Citește în ordinea asta:
1. `docs/00-viziune.md` — ținta și cifrele.
2. `docs/01-pipeline.md` — fiecare pas și modulul care îl face.
3. `docs/02-reguli.md` — regulile absolute (cea mai recentă câștigă).
4. `playbooks/` — metodele dovedite, cu sursa.
5. `products/<produs>.md` — produsul pe care lucrăm.

Reguli de lucru:
- Orice regulă nouă de la Szasz (`regula: ...`) → linie datată în `docs/02-reguli.md`.
- Orice afirmație de tip „merge” trebuie legată de o cifră (retenție, views, CTR, comenzi). Fără cifră e ipoteză și se marchează ca atare.
- Nu inventa date despre competitori: în `playbooks/` intră doar ce e observat (link, captură, cifră) sau spus explicit de Szasz.
- După fiecare lot: commit + push, ca Szasz să-și ia fișierele din GitHub.
