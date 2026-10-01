---
name: analyze-clip
description: Analizează un reel (viral sau al nostru) cadru cu cadru și scrie hook-ul în library/hooks-library.json în formatul standard; la „feedback” compară cu biblioteca și spune ce să schimbăm.
---
Input: folderul `library/analysis/<clip>/` (făcut de `engine/prepare_clip.py`).
1. Privește `sheet.jpg`, apoi `hook_01..06.jpg` (primele 3 s) și citește `transcript.txt` + `info.json`.
2. Scrie intrarea (EN pentru text, RO pentru explicații):
   {"source": url/fișier, "platform", "views", "ratio", "hook": {"first_frame": ce se vede în primul cadru, "action_0_3s": ce se întâmplă, "on_screen_text": textul de pe ecran, "spoken": replica, "sound": muzică/voce/diegetic, "kind": problem|reaction|twist|other, "product_visible": bool, "transition_to_product": cum trece la produs, "why_it_works": 2 propoziții}, "pattern": o propoziție generală reutilizabilă (ex. „obiect casnic folosit greșit ca sursă de căldură”), "adaptable_to_heatgrump": idee concretă fără halat în cadru}
3. Adaugă în `library/hooks-library.json` → `research[]`. Nu dubla aceeași sursă.
4. La „feedback <fișier>” (video de-al nostru): aceeași analiză + compară primele 3 s cu top 10 din bibliotecă (după scor) și dă exact 3 schimbări concrete (cadru, acțiune, text), cu motivul.
