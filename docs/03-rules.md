# Reguli absolute HeatGrump (Grinch) — consolidate la 30 sept 2026
Sursa: memoria Cowork + sesiunea 16–29 sept. Regula mai nouă bate regula mai veche.

## Produs (halatul)
- Design 1:1 după referințele reale (library/media.json → product_grinch_refs). Produsul nu „driftează” niciodată; mereu aceleași referințe.
- Căptușeala e VERDE (olive), niciodată albă.
- Buzunarele sunt SIMPLE: pluș verde cu bandă sherpa albă, fără față, fără print. Fața verde există DOAR pe panoul din față al glugii.
- Halatul se vede ÎNTREG, până jos, în toate cadrele. Mânecile rămân mâneci normale.
- Concept „pătură purtabilă”: tiv cu doi săculeți de picioare uniți la mijloc (W continuu), din același material verde; deschis, halatul e LAT sus.
- Plușul se descrie mereu ca mai gros, mai cozy, mai premium.
- Fără pink, fulgi, căsuțe, Moș Crăciun print, burgundy.

## Telecomandă și conector
- Telecomanda = referința reală cb73364c. Exact 5 luminițe, toate vizibile; pe placă toate STINSE. În video: urcă 1→5, o singură luminiță aprinsă odată, 4 apăsări, promptul LUI cuvânt cu cuvânt (prompts/controller-video.txt). Fără „-7 contrast, +3 exposure”.
- Conectorul = referința 2774615c + placa aprobată da68ee9d ca „Image 1, reproduce one to one”. Nu se descrie cu cuvinte proprii. În video cele două jumătăți intră COMPLET una în alta, fără gol.
- Plăcile de telecomandă și conector: close-up, lângă brad sau pat (recognoscibil în fundal blurat); doar manșeta verde pufoasă din halat în cadru.

## Flux
- B1, B2, cozy: DIRECT în Genjutsu (motion control) din clipurile de mișcare, fără start frame. Clipurile se ROTESC între reel-uri (B1 ×2, B2 ×3, cozy ×2).
- Conector, telecomandă, unboxing: se animează DIRECT, fără aprobarea plăcii (23 sept).
- Unboxing: cutia MEREU pe podea; placa după șablonul lui + blocul box-on-floor; video după șablonul lui, cu cutia + 1-2 referințe de halat; logica ferestrei transparente a cutiei trebuie să fie coerentă.
- Hook: 3 idei per reel, în tabla HTML, fiecare cu start frame (FĂRĂ halat), acțiunea de 4-5 s, textul CapCut (EN) + variantă, legătura cu B1, de ce merge. Originale; nu se repetă între reel-uri. El alege, apoi se animează.
- Îmbrăcăminte de dedesubt: normală, diferită la fiecare personaj (pijama de Crăciun / America / stil american / cozy), aceeași în tot reel-ul, aleasă de Claude și spusă la livrare.
- Personaj: băiat/fată se respectă în toate cadrele, inclusiv mâinile din macro-uri.
- Fără text ars, fără zoom (nici push-in/pull-out), fără branduri reale (magazin generic, fără logo).
- Toate clipurile cu audio diegetic (fără muzică, fără voce unde nu e replică).
- Setări maxime mereu: 4k la imagini, 1080p + bitrate high la video.
- Lumină: ultra-realistă (prompts/blocks/light-ultra-real.txt) + culori vii, semicalde, nu auriu/portocaliu. La cozy: fără blitz, fără sursă de lumină în poziția camerei.
- Tabla HTML după fiecare lot, cu personajul și camera lângă fiecare reel; linkuri directe complete după orice regenerare.

## Principii de prompt validate
- Referința-țintă pe poziția 1 cu „REPRODUCE ONE TO ONE” + listă numerotată cu exact ce se schimbă.
- Ce trebuie să iasă perfect e PRIMUL bloc, marcat „ABSOLUTE RULE, HIGHEST PRIORITY”.
- Multe referințe de produs (4-6), timeline pe secunde, cameră fixă, mișcarea descrisă prin greutate și material.

## Mix zilnic (30 sept)
- 15 videouri/zi = 5 hook-uri DOVEDITE (umplutură) + 5 ADAPTATE după cele mai bune virale din research + 5 CREATIVE noi. Intercalate, nu 5 la rând de același fel. Proporția se ajustează după 2 săptămâni de cifre (config `daily_mix`).
- Dovedite (pornire manuală, Szasz): 3-2-1 reveal; magazin – clienta cu coșul; magazin – lansare cu panglică; magazin – angajații dezvăluie raionul; gifting („I'm freezing" / „Take this"). Lista: `library/proven-hooks.json`.
- Un concept dovedit se reface cu alt personaj + altă cameră, nu mai des de o dată la 3 zile, niciodată cu același set; Genjutsu (motion control din clipul de mișcare) unde există; o singură variantă video.
- Adaptat = copiem STRUCTURA viralului (setup → surpriză etc.), nu clipul; max 2 folosiri per tipar.
- Hook-urile noi (adaptate + creative): 2 variante video din același start frame, se alege cea mai bună; fără halat în cadru.
- Promovare automată: un hook nou cu scor peste mediana contului după 72 h de la postare intră în lista de dovedite (`feedback.py score`).
- „A funcționat" = cifră (retenție/views peste mediană), nu impresie.

## Seturi noi (1 oct)
- Personajele se iau DIRECT de pe Pinterest: poza exactă e referința de personaj, nu se mai generează personaje „inspirate”. Camerele la fel. Înlocuiește regula veche „personaje sintetice, niciodată fețe reale”. (Videourile nu se postează public — decizia lui Szasz.)

## Hook-uri (1 oct)
- Nu se mai generează imagini (start frame-uri) pentru ideile de hook. Ideile se scriu doar ca text detaliat în Studio (ce se vede, acțiunea de 4-5 s, text CapCut + variantă, legătura cu B1, de ce merge). Hook-urile video vin din clipuri virale tăiate de la conturile date de Szasz și refăcute cu Genjutsu (personajul + camera noastră).

## Calitatea referințelor (2 oct)
- Personajul și camera se aleg DOAR din poze de calitate mare: latura mică ≥ 1080 px, clare, fără compresie vizibilă. Pozele de 736 px (miniaturile Pinterest) dau clipuri moi — se resping. `engine/pinterest.py` le filtrează automat.

## Montaj final (2 oct)
- Reelul livrat e GATA DE POSTAT: montat în stilul conturilor de referință (merry.jammies, snuglore, thecozykitty.us — `library/style-ref/index.json`), cu text pe ecran pe fiecare clip și muzică de Crăciun. Durată țintă 15-18 s (virale lor au 13-20 s).
- Textul pe montaj e voit (nu contrazice „fără text ars” — aceea e pentru generările Higgsfield).

## Conector și hook-uri (2 oct)
- Conectorul trebuie să intre COMPLET unul în altul în ultimul cadru, fără niciun gol sau parte interioară vizibilă. QA: se verifică obligatoriu ULTIMUL cadru mărit (nu doar banda de 4 cadre); dacă se vede gol → regenerare.
- Montajul final (text + muzică) se face abia când există hook-ul; până atunci se livrează doar clipurile verificate.
- Hook-urile le scrie Szasz (5-6 deocamdată) și se ROTESC prin videouri. Claude nu mai propune hook-uri până nu cere el; păstrează lista în `library/proven-hooks.json` / Studio.

## Clipuri fixe și B1 dublat (2 oct)
- Telecomanda ȘI conectorul se fac O SINGURĂ DATĂ (conectorul adăugat la cererea lui Szasz, 2 oct): un clip bun cu mână de bărbat și unul cu mână de femeie (`library/media.json` → `fixed_clips`) și se refolosesc la toate reel-urile, după genul personajului. Nu se mai generează telecomandă per reel.
- B1: clipurile de mișcare scurte (mai bune — pun halatul repede) se dublează (lipite de două ori) și se încarcă așa ca referință; la montaj se taie doar prima punere a halatului. Se rotesc ca să nu iasă același B1.
- Muzica: Szasz și-a asumat drepturile — se pune direct piesa de Crăciun (ca la conturile de referință).

## Tăieturi la montaj (2 oct)
- B1: se taie imediat după ce își pune gluga.
- Telecomandă: se taie după ce luminița ajunge la 3 (pentru clipul fix contează 1→2→3 corect, una singură aprinsă).
- Conector: doar mișcarea în care intră una în alta, ~1,5 s, și se termină cu ele COMPLET intrate (nu tăia înainte).
- B2: se lasă până își închide halatul.
- Mâna de femeie (conector, telecomandă): unghii lungi pictate roz-nude, la fel peste tot.
- Telecomandă: începe exact când începe să apese butonul (fără așteptare la început).
- Conectorul are fir pe AMBELE jumătăți (sus și jos) — QA.
- Unboxing: se taie la ~2,5 s (după ce scoate halatul din cutie).
- B1, conector, telecomandă și unboxing scurte în montaj.

## Cozy după tipul camerei (2 oct)
- Clipul de mișcare cozy `cozy-a-x2` (7da99c7a, întins / filmat de la picioare) merge DOAR în camere cu PAT. În living fără pat se folosește cozy `8042602c` (se cuibărește pe canapea). Alege clipul cozy după ce are camera setului.

## Hook-uri din virale (2 oct)
- Sursa: conturile de referință (merry.jammies, snuglore, thecozykitty.us + artifactul prietenului lui Szasz). Se descarcă clipul, se taie DOAR partea de hook (fără halat), se încarcă ca referință de mișcare și se reface cu Genjutsu cu personajul + camera setului. Bucățile sub ~1,8 s se dublează (ca la B1) și se taie la montaj.
- Textul CapCut al hook-ului se ia/adaptează din viral (ex. „The problem 😩❄️” → „Vs…”).

## Texte și muzică la montajul final (2 oct)
- Textele: fontul de Instagram/TikTok (TikTok Sans SemiBold, alb cu contur negru subțire) + emoji de iPhone (`library/fonts/apple-emoji`), ca la conturile de referință. `engine/final.py` le face automat.
- Hook-urile cu „cineva înfășurat pe canapea”: persoana trebuie să fie vizibilă (ex. o fată învelită până la bărbie, cu fața la vedere), nu un ghem de pături.
- Muzica: piesele întregi se iau de pe YouTube cu yt-dlp și se taie pe refren/partea recognoscibilă (necesită domeniile YouTube în Allowed domains).

## Planul zilnic (2 oct, Szasz)
- 10 videouri/zi: 5 cu hook-uri din cele mai virale clipuri (refăcute cu Genjutsu, complet automat) + 5 unde hook-ul îl gândește Szasz (Claude pregătește tot restul: B-roll, clipuri fixe, montaj, texte, muzică; lipsește doar hook-ul).
- ÎNAINTE de asta: reelul 7 se face perfect, ca referință pentru toate celelalte. `engine/rotation.py plan` se adaptează la noul mix după ce reelul 7 e aprobat.
- 2 oct: la montaj, toate clipurile în afară de hook sunt FĂRĂ sunet (Genjutsu pune muzică proprie pe B-roll); se aude doar muzica aleasă + sunetul hook-ului. (engine/final.py face asta automat)
- 2 oct: reelul se termină exact când se oprește muzica (ultimul cadru cu muzică), niciodată bucată fără muzică la final. Reel 7 aprobat ca REFERINȚĂ ("super fain făcut"). (engine/final.py taie automat)
- 2 oct (lot reel 8-12): clipul B2 „C_new” (e9a9ed00) filmează doar corpul, fără față → la B2 se folosește „B_face” (6731a06f). Dacă apare fața de Grinch pe buzunar, se refac cu regula buzunarelor pusă PRIMA în prompt.
- 2 oct: virale cu costum de Grinch ca clip de mișcare (ex. fața în glugă) → ip_detected. Hook-ul se face atunci din placă gpt_image_2 + seedance (doar start_image). La fel raftul din magazin: seedance îl respinge → apropiere din placa 4k cu ffmpeg (zoompan lent + mers).
- 2 oct: la hook-uri afară, hainele se scriu „fără logo, fără brand” (prima variantă a ieșit cu The North Face pe geacă).
- 2 oct: unboxing-ul cu seedance pică des la ip_detected → din start doar cutia + 1 referință de halat; dacă fereastra cutiei nu se golește, se adaugă regula „THE BOX WINDOW EMPTIES” prima în prompt.
- 2 oct: textul de pe ecran poate rămâne textul hook-ului pe TOT videoul (ca la virale); nu e obligatoriu să se schimbe pe bucăți („plug it in”, „5 heat levels”…). Se aplică videourilor viitoare.
- 2 oct (feedback reel 10): telecomanda și conectorul fixe se aleg după gen ȘI culoarea pielii. Personaj cu piele închisă → variantă fixă proprie (placă = placa aprobată, doar mâna schimbată după personaj), apoi se refolosește.
- 2 oct (feedback reel 8): la Genjutsu, părul personajului se scrie explicit („fără coc, fără păr lung”) — altfel copiază părul din clipul viral.
- 2 oct (feedback reel 9): cozy-a-x2 (pat) se repetă la 1,7 s și halatul arată ciudat; în dormitor cozy se face din placă (ea în pat, în halat, cu gluga) + seedance.
- 3 oct: clip nou de cozy de la Szasz (library/motion/cozy-c-orig.mp4, Higgsfield 5f950f18): pe canapea, se învelește până la față. Se rotește cu 8042602c; la montaj se folosește 0–1,2 s, cât fața se vede. Pe clip e text ars („DONT send this to your girlfriend”) — promptul cere scoaterea lui.
- 3 oct: la B2 fața NU trebuie să se vadă. Toate cele 3 clipuri de B2 (A_no_face 6243c22d, B_face 6731a06f, C_new e9a9ed00) sunt bune și se rotesc între reeluri; nu se mai refac B2-uri doar pentru că nu se vede fața.
- 3 oct: muzica = sunetul ORIGINAL al viralului din care e luat hook-ul (library/music/viral-<cod>.m4a), de la secunda 0, nu altă melodie de Crăciun. Reelul se termină odată cu sunetul (dacă viralul e scurt, se scurtează bucățile). La research se salvează și audioUrl (unele mp4-uri de la Apify vin fără sunet).
- 3 oct: hook-uri de pe princesscomfortt (top 5 după vizualizări, fără cel cu H&M/mall). Genjutsu dă ip_detected când viralul are costum de prințesă sau când robe-ul cu fața Grinch e foarte mare în cadru; atunci: placă gpt_image_2 + seedance doar cu start_image; dacă și seedance refuză, placa se reface cu gluga/fața ascunsă.
- 3 oct (feedback reel 13, 14, 17): la hook-urile în care halatul se desface deja în cadru (stil princesscomfortt) NU se mai pune unboxing; B2 se lasă întreg, până închide complet halatul. Halatul din hook: lung până la podea, foarte pufos, cu buzunarele (săculeții) vizibile.
- 3 oct (reel 15): un hook se caută după ACȚIUNE + AUDIO din viral (ex. „3, 2, 1… let's see how it comes out” = snuglore DdLiUc7t1Yb, tocător + tigaie), nu după textul de pe ecran. Replica din audio se verifică cu video_analysis Higgsfield (whisper e blocat). Textul de pe ecran îl punem noi, ca de obicei.
- (3 oct) Clipurile nu se taie prea scurt: hook-ul ține până se termină acțiunea (ex. ia tigaia de pe halat), B2 până se închide halatul, cozy ~2,5 s. Dacă audio-ul viralului e mai scurt decât videoul, se prelungește cu o buclă (`viral-<cod>-ext.m4a`, crossfade din secunda 4), nu se scurtează clipurile.
- (5 oct) Hook-uri NOI la fiecare lot (Szasz: „nu prea vom refolosi hookurile”): se iau virale încă nefolosite din conturile de referință (princesscomfortt, merry.jammies, snuglore, thecozykitty.us), cu acțiuni diferite între ele. Lot 18-22: termostat „The problem/Vs” (snuglore DdmI16ft-rc), fuga din magazin cu cutia (merry DdTC2suKD0l), POV halat rulat lovit cu piciorul (cozykitty DdSNI1ITcu6), selfie-recenzie în oglindă (merry DdK34IiqRx4), mâini care desfac halatul rulat pe pat (merry Dc-rr2WKSRR).
- (5 oct) Textul ars din viral trece în Genjutsu: înainte de upload se șterge din clipul de mișcare (ffmpeg delogo pe zona textului).
