---
name: new-sets
description: Creează seturi noi (personaj + cameră + B-roll) când rotația le cere: camere de pe Pinterest, personaje sintetice inspirate de Pinterest, apoi B-roll-ul complet. Rulează la „seturi noi” sau când rotation.py spune „de creat”.
---
1. `python3 engine/rotation.py status` → câte seturi trebuie.
2. `python3 engine/pinterest.py rooms 12` și `python3 engine/pinterest.py characters 12`. Privește pozele din `library/rooms/` și `library/char-inspiration/`; alege camere luminoase, cu brad sau pat vizibil, fără persoane, fără text/logo.
3. Cameră: încarcă poza aleasă în Higgsfield (media_upload → PUT → media_confirm) și folosește-o direct.
4. Personaj: NU folosi fața reală. Generează cu gpt_image_2 (9:16, 4k) un personaj NOU inspirat de poză: aceeași vârstă/stil/vibe, ALTĂ față, poză candid la el acasă, fără text; plus blocul light-ultra-real. Salvează job-ul ca referință de personaj. Alternează bărbați/femei și vârste.
5. Îmbrăcăminte pentru set: alege una (pijama de Crăciun / America / stil american / cozy), diferită de seturile active.
6. Rulează skill `make-reel` doar pentru B-roll (B1, B2, cozy, conector, telecomandă, unboxing), apoi `python3 engine/rotation.py add '<json set>'` cu ID-urile și link-urile clipurilor.
