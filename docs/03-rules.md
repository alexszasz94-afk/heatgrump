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
- (5 oct, Szasz) STILUL NOU, după reel-ul de referință princesscomfortt DeDAprJSrPO:
  - B2 doar cu fața mereu la vedere: clip de mișcare `inbox/up4/dB2.mp4` (Higgsfield 9896b250), stă cu fața la cameră, deschide halatul ca niște aripi, ridică un genunchi, îl închide. Se folosește la TOATE videourile de acum.
  - Hook-urile se iau de pe contul princesscomfortt (cele mai populare, nefolosite). Viralele cu halate de prințesă dau ip_detected în Genjutsu → placă gpt_image_2 + seedance FĂRĂ referință de halat (doar start_image).
  - Sunet: doar hook-ul are sunet propriu, făcut de noi pe acțiunea hook-ului (seedance generate_audio sau mirelo_text_to_audio pentru Genjutsu), NU audio-ul competitorului. Restul fără sunet.
  - Muzică: melodiile lui Szasz din `library/music/xmas/`, peste tot videoul, de la secunda folosită de competitori: Mariah 42,4 s (princesscomfortt), Wham 0,43 s (merry.jammies), Bublé 32,43 s (merry.jammies, intrarea orchestrei). orig_vol 0.9, music_vol 0.85.
  - Text: TikTok Sans bold semi-condensat (`library/fonts/TikTokSans-w700-semicond.ttf`), mărime 88, contur negru 6 px, la 18% din înălțime (engine/final.py).
  - Fără unboxing dacă viralul nu are.
- (5 oct) B2-ul nou (cu fața) se accelerează la montaj x1.35 (b2fast.mp4, ~4,4 s) — Szasz: „un pic mai rapid b2”. Cozy cu bărbat: clipul 8042602c (se așază pe canapea), nu cozy-c.
- (5 oct) Al doilea clip de B2 cu fața la vedere: Dd9h35Ly2Ca 4,5–10 s (inbox/up4/dB2f.mp4, Higgsfield df7d7a2b) — filmat din cap până în picioare, iese foarte bine; FĂRĂ delogo (textul acoperă fața în original; prompt-ul cere scoaterea textului). DeCsbOaSJAY (gluga pusă, Albă-ca-Zăpada) dă ip_detected. Hook-ul cu numărătoare 3-2-1: vocea noastră (inworld TTS, Ashley) pusă pe secundele din referință (library/audio/countdown/).
- (6 oct) Szasz: TOATE hook-urile se fac cu Genjutsu și trebuie să aibă sens (acțiunea se leagă de text). Cozy-urile sunt MEREU cele aprobate (clipurile de mișcare 8042602c canapea / 5f950f18 cozy-c), nu cozy-ul viralului.
- (6 oct) Stil: structura și hook-urile princesscomfortt + atmosfera snuglore (brad, luminițe, ciorapi la șemineu, camere de Crăciun, oameni diverși). Test: 3 virale princesscomfortt refăcute cadru cu cadru 100% în Genjutsu (DeAepvaSfSf, DeAgPjvyBF1, DeDFKhASW-w) — lot 24, engine/batches/jobs24.json.
- (6 oct) Telecomanda și conectorul: MEREU clipurile noastre fixe (output/fixed, după gen și culoarea pielii), nu Genjutsu — Szasz: „ia le ale noastre ca e mai bine”.
- (6 oct) Reel 26: textul de pe ecran „H&M X GRINCH 🎄🎅”, apoi la cozy „JK we sell them 💕🎄” (cerut de Szasz, ca la competitor).
- **2026-10-18 — STIL AMERICAN (Szasz, pentru toate videourile de acum, la orice produs):** (1) fiecare HOOK are undeva în cadru steagul american (pe perete, pe verandă, pe o pernă, pe o cană etc. — natural, nu forțat); (2) la B-roll-uri îmbrăcămintea de dedesubt e în stil american (ex. pijama/hanorac cu steag, stars & stripes, varsity, Americana); (3) folosim doar personaje care arată americane (look de creator UGC din SUA, case americane). Se verifică la QA.

- 18 oct (Szasz, REGULĂ ABSOLUTĂ): halatul se face DOAR după referințe — la ORICE clip cu halat (B-roll, hook, unboxing, cozy) se pun TOATE cele 4 referințe Grinch (`library/media.json` → `product_grinch_refs`, sau pozele lor reîncărcate în workspace-ul curent). Halatul NU se descrie în cuvinte: în prompt doar „the robe of Images N–M — REPRODUCE IT ONE TO ONE from these references”. Gluga cu fața Grinch iese greșit fără toate referințele. Dacă un ID nu se găsește (alt workspace), se reîncarcă pozele, nu se trece la descriere. Dacă Seedance dă nsfw/ip pe referințe, se raportează lui Szasz, nu se înlocuiește cu text.
- 19 oct (Szasz, REGULĂ): B-roll-ul se face ÎNTR-UN SINGUR CLIP per set, ca la videourile cu prințesa/Grinch (output/princess-copy b4g/b5g): clipurile de mișcare B1 + B2 + cozy se lipesc într-un singur video de referință (~9-10 s, 720x1280, ffmpeg concat) și se face O singură generare Genjutsu (mai ieftin decât 3). Proba se face întâi la 480p, apoi varianta aprobată la 1080p. La montaj se taie pe bucăți. Cozy-ul rămâne cel clasic (cozy-c / 8042602c) — nu clipuri de pat de pe Pinterest. Clipurile cu halate de prințesă (ex. x_cozy) dau ip_detected.
- 19 oct (Szasz): B-roll-ul NU se inventează din clipuri de mișcare amestecate — se COPIAZĂ B-roll-ul din clipurile noastre de referință (library/media.json → broll_standard: ref1 = reel FB 1091684610405387, canapea; ref2 = upload 19 oct, cozy pe pat), o singură generare per set, și se rotesc ref1/ref2/ref3 în ciclu între videouri (ref3 = snuglore DdpIYs0trT0, două cadre de cozy pe canapea). În dormitor, cozy-ul se poate face și din placă (ea citește în pat, în halat) + Seedance.
- 19 oct (Szasz): hook-urile se COPIAZĂ cu Genjutsu (clipul viral = referință de mișcare), nu cu placă + Seedance. Dacă Genjutsu dă ip_detected, se reîncearcă tot cu Genjutsu cu mai puține referințe de halat (2, apoi 1), nu se trece la Seedance.
- 19 oct (Szasz): hook-ul 3-2-1 (ruloul) se face cu Seedance 2.5 omni_reference (video_references = clipul original FĂRĂ sunet, image_references = fata + camera + 4 ref. halat, generate_audio: numărătoarea „Three, two, one!” + reacția, fără muzică) — ca să aibă sunetul lui. Hook-ul cu tocătorul + tigaia: imaginea cu Genjutsu, iar la montaj sunetul ORIGINAL al viralului copiat (snuglore DdLiUc7t1Yb, library/music/viral-DdLiUc7t1Yb-ext.m4a) pe TOT montajul, fără altă muzică (Szasz 19 oct).
- 19 oct (Szasz): „gata de postat” NU se regenerează la 1080p — se face UPSCALE (Higgsfield upscale_video, bytedance, preset aigc, 1080p) pe montajul 480p aprobat, apoi se pune înapoi sunetul montajului. Ieșire 1080×1920, 30 fps, H.264, AAC.
- 19 oct (Szasz, REGULĂ): MEREU la toate start frame-urile și videourile: „UGC ultra-realism, shot on an iPhone 18 Pro Max” (intră în blocul prompts/blocks/light-ultra-real.txt). La scenele cu familie: și copii, iar unii oameni stau pe telefon (natural, ca acasă).
- 19 oct (Szasz, REGULĂ): la testele cerute de Szasz se generează CÂTE UN SINGUR video la 480p (nu 2 variante). Înlocuiește „2 variante video” de la hook-urile noi.
- 19 oct (Szasz, REGULĂ): la start frame-urile de hook se folosesc CAMERELE NOASTRE exact cum sunt: poza camerei = fundal neatins (același unghi, aceleași obiecte), GPT Image 2 (high, 4k) doar ADAUGĂ oamenii („EDIT IMAGE 1, do not redraw it”). Nu se cere cameră din alt unghi — modelul o redesenează și iese de calitate proastă.
- 19 oct (Szasz, REGULĂ, înlocuiește iPhone 18): la toate pozele și videourile: „UGC style, natural, shot on an iPhone 17 Pro Max”.
- 19 oct (Szasz): format „The problem vs the solution”: „The problem 😩❄️” pe hook, „Vs…” pe tot B-roll-ul (cât se îmbracă), „The solution 🥹🎄” de la conector până la final (soluția = încălzirea cu halatul).
- 19 oct (Szasz, REGULĂ): înainte să trimit orice start frame sau video, îl analizez critic SINGUR (mărit) ca un om care se uită pe TikTok: pare filmat de un om real? poziția mâinilor/brațelor (selfie = UN braț), privirile, ușile/prizele logice, fizica (cutii, foc, căderi), abur/efecte exagerate, lumină, cameră = a noastră, haine american style. Spun ce aș schimba și, dacă e ceva clar greșit, refac ÎNAINTE să-i trimit — nu aștept să-mi spună el.
- 19 oct (Szasz, REGULĂ): unboxing-ul se pune în montaj DOAR când hook-ul o cere (ex. hook-ul cu tirul care aruncă cutia). În general NU se pune unboxing: hook → B-roll → conector → telecomandă → cozy.
- 19 oct (Szasz): „grijă la glugă, să fie mereu bine” — gluga e mereu cea din referințe: VERDE, cu fața Grinch brodată, margine albă și ciucure alb, în TOATE cadrele (inclusiv prim-planul din spate și halatul rulat). Glugă roșie / fără față / ciucure lipsă = pică QA și se reface. În prompt se adaugă blocul „THE HOOD — ALWAYS EXACTLY AS IN THE REFERENCES”.
- 19 oct (Szasz): „trebuie să nu aibă fundă albă” — gluga NICIODATĂ cu fundă/panglică. La Genjutsu, dacă viralul are un cadru cu gluga din spate cu fundă (sau alt detaliu care se copiază greșit), se TAIE acel cadru din clipul de referință (imagine + sunet) ÎNAINTE de Genjutsu; nu se încearcă doar din prompt. Cuvântul „Grinch” NU se pune în prompturile Genjutsu (dă ip_detected).
- 19 oct (Szasz): produs nou Bubblywarm (covoraș jacuzzi). B-roll-ul se face MEREU cu Genjutsu pe clipul cu baia (research/spamat/BUBBLYWARM.md), schimbând de fiecare dată baia (culori, faianță etc.) doar din prompt, fără poză de referință pentru baie. Cutia Bubblywarm e referința pentru unboxing.
- 20 oct (Szasz, REGULĂ ABSOLUTĂ): la ORICE generare cu halat se pun MEREU TOATE cele 4 referințe ale halatului. Nu există variantă cu 2 sau cu 1 referință și nu se scad referințele la ip_detected. Dacă dă ip_detected cu toate referințele → NU se retrimite cu mai puține; se oprește și se întreabă Szasz. Înlocuiește regulile vechi „retrimite cu 2, apoi 1 referință” (2 oct, 19 oct, CLAUDE.md capcane, prompts/unboxing-video.txt). Camera/încăperea la Genjutsu se poate schimba doar din prompt, fără poză de referință, când cere Szasz.
- 20 oct (Szasz, REGULĂ): lumina și calitatea din start frame-ul de magazin cu set3 și cana de Crăciun (output/lot20/store-cana-set3-1.png, varianta editată de el: store-cana-set3-szasz.png) sunt „perfecte” → MEREU acest stil: lumină de sus curată + strălucirea luminițelor ca rim light pe păr/față, umbre moi dar clare, reflexii lucioase, catchlights în ochi, fundal cu bokeh din luminițe, persoana și obiectul principal foarte clare. Blocul canonic: prompts/blocks/light-store-premium.txt (se pune la orice start frame și video).
- 20 oct (Szasz, REGULĂ): în FIECARE video toate mișcările sunt naturale — fără mișcări bruște, fără sărituri, fără obiecte care dispar, fără slow motion sau accelerări; camera se mișcă lin. Acțiunea se întâmplă RAPID, fără timp mort la început. Blocul canonic: prompts/blocks/motion-natural.txt (se pune în orice prompt video). Când camera se întoarce spre ceva (ex. raftul cu halate), poziția lui trebuie să aibă sens cu direcția în care se uită personajul.
- 20 oct (Szasz, REGULĂ): ORICE prompt (imagine sau video) e LUNG și DESCRIPTIV: cine, unde, ce face secundă cu secundă, cum se mișcă corpul/obiectele/camera, lumina (light-store-premium), mișcarea (motion-natural), sunetul. ÎNAINTE să-l trimit îl citesc critic: e natural? are sens fizic și logic (direcția privirii ↔ unde e obiectul, unde cade lichidul, ce ține în mâini, ce se vede după întoarcerea camerei)? ar declanșa filtre (cuvinte ambigue)? Corectez și abia apoi trimit. Szasz: „ar trebui să nu te mai învăț eu” — aplic singur tot ce am învățat din reguli și din greșelile trecute, fără să aștept să-mi spună.
- 20 oct (Szasz): căderile/accidentele se întâmplă DINTR-O DATĂ, în timp real (~0,5 s), NICIODATĂ în slow motion. În prompt: „real time, normal 1x speed, no slow motion, no speed ramps”, plus durata exactă a căderii.
- 20 oct (Szasz, REGULĂ, Bubblywarm): la B-roll, după ce apasă pe telecomandă se taie DIRECT la partea cu bule — fără cadrele cu cada nemișcată dintre ele. Tăieturi pe B-roll-urile de Crăciun: c1 0–4,2 s + 6,75 s–final; c2 0–4,2 s + 6,75 s–final; c3 0–5,9 s + 6,75 s–final. Video Bubblywarm complet = hook → unboxing (unboxing-bubblywarm-1080.mp4) → B-roll de Crăciun tăiat așa.
- 20 oct (Szasz): la căderi de tip „leșin de șoc” cade DIRECT pe spate (nu se așază întâi pe fund) și după cădere rămâne nemișcată, fără să râdă.
- 20 oct (Szasz, REGULĂ, Bubblywarm): la montaj B-roll-ul se pune FĂRĂ sunet (doar muzica peste). Implementat în output/lot20/montaj/mont_bubbly.py.
- 20 oct (Szasz): B-roll NOU (ref4, library/motion/broll-ref4-b.mp4 = clipul lui Szasz 5,25 s–final): o singură generare Genjutsu cu tot (îmbracă din spate → oglindă → deschide → conector → telecomandă → cozy), cu referințele produsului + plăcile de conector și telecomandă (library/sets-ref4/). Personaje și camere noi de pe Pinterest (library/sets-ref4/pick.json). În prompt: căptușeala roșu sus / verde jos (altfel copiază căptușeala crem din clip) și oglindă reală în cameră. La personaj bărbat telecomanda iese cu mână de femeie → se înlocuiește cu clipul fix telecomanda-barbat-taiat.
- 20 oct (Szasz): la 3-2-1 se aude MEREU vocea pe hook (numărătoarea). Genjutsu nu mai scoate sunet → se pune sunetul hook-ului din output/lot19/480/h321-s3.mp4 (același clip de mișcare, aceeași sincronizare), apoi muzica. Textul pe ecran NU e „3 2 1”, ci unul din textele noastre obișnuite (ex. „Don't show this to a Christmas lover... 🎄🎅”, „I made this for the cold-aholics.. 🤩💕”, „Every Christmas lover needs this 🎄😍”).
- 20 oct (Szasz, REGULĂ): DOAR personaje FEMEI (fără bărbați) la seturile noi. 3-2-1 cu B-roll-ul ref4 (blonda) „a ieșit foarte bine” = formatul de urmat.
- 20 oct (Szasz): B-roll-ul ref4 iese din Genjutsu cu 1-2 cadre rătăcite la început (cutia din clipul original) → se taie 0,2 s din începutul B-roll-ului la montaj. Clipul de referință e acum tăiat de la 5,35 s.
- 20 oct (Szasz: „au lag videourile”): cauza = clipurile AI sunt 24 fps, montajul le forța la 30 fps (cadre dublate). REGULĂ: montajul rămâne la 24 fps nativ; fiecare clip se mărește separat la 1080p (upscale bytedance fps 24) și abia apoi se montează (output/lot20/ref4/mont321-1080.sh); final.py primește "fps": 24 în JSON. Nu se mai face upscale pe montajul gata făcut.
- 20 oct: Genjutsu dă des ip_detected pe 3-2-1 (fără motiv clar). Pași, fără să scad referințele halatului: 1) retrimit identic (merge de obicei a doua oară); 2) dacă tot pică, folosesc ca referință de personaj un cadru cu fața ei din B-roll-ul ei care a trecut (a mers la setul F). Dacă B-roll-ul iese cu piele goală (spate gol la îmbrăcat), tai începutul până acoperă halatul (T=0.85 în mont321-1080.sh) în loc să regenerez.
- 20 oct (Szasz, REGULĂ): NICIO generare video (Seedance/Genjutsu) fără acordul lui Szasz — întâi start frame-ul, el aprobă, abia apoi video. Personajele se iau MEREU de pe Pinterest (poza reală), camerele normale/naturale, luminoase, cu lumini puternice.
- 22 oct (Szasz, REGULĂ): muzica de acum = „You're a Mean One, Mr. Grinch” (în locul Mariah/Wham/Bublé), fișierul în library/music/xmas/mean-one-grinch.* . YouTube/SoundCloud sunt blocate din cloud (bot-check / proxy) → Szasz pune piesa în inbox/.
- 22 oct (Szasz, REGULĂ): orice rezultat (start frame, video, corectură) i se trimite INSTANT, imediat ce e gata și verificat — nu se strâng în lot — ca să poată corecta din timp.
- 22 oct (Szasz): start frame-urile trebuie să arate „top”, cu lumini NATURALE (lumina zilei, fără glow/AI). Hook-urile pe stradă: poză REALĂ de telefon, ziua (nu poze AI de pe Pinterest); camerele mereu decorate de Crăciun; obiectele la mărimea reală (halatul împăturit = pachet mare).
- 23 oct (Szasz, REGULĂ PE VIAȚĂ): lumina e MEREU foarte moale și foarte naturală, la orice imagine sau video, la orice produs. Se adaugă în fiecare prompt blocul `prompts/blocks/light-soft-natural.txt` (pe lângă light-store-premium). Fără lumină dură, fără contrast dramatic, fără HDR / glow / aspect CGI. Se verifică la QA.
- 23 oct (Szasz, REGULĂ): imaginile (start frame-uri, poze de produs) se fac cu `nano_banana_pro` (9:16, 4k) — GPT Image 2 iese prea procesat. Video rămâne Seedance 2.5 / Genjutsu.
- 24 oct (Szasz): halate noi → B-roll + conector/telecomandă cu Kling 4.0 video-edit pe clipurile noastre (fără sunet), șablon limitless/products/snoopy-robe/prompts/broll-kling4.txt; hook animat cu Kling image-to-video. Detalii în limitless/docs/02-reguli.md.
- 24 oct (Szasz, REGULĂ): video DOAR cu Kling 4.0 la 720p (video-edit pe clipurile noastre / image-to-video din start frame). Seedance și Genjutsu nu se mai folosesc. Fără upscale.
- 24 oct (Szasz): Kling 4.0 direct la 1080p (înlocuiește 720p).
- 24 oct (Szasz, REGULĂ): poza personajului se pune MEREU ca referință directă la orice generare cu personaj (start frame, variantă, corectură, video), chiar și când pornim de la un frame deja generat — niciodată doar din frame-ul anterior.
- 24 oct (Szasz, REGULĂ): la conector și telecomandă se folosesc de acum clipurile REALE filmate de Szasz — `output/fixed/conector-real.mp4` și `output/fixed/telecomanda-reala.mp4` (înlocuiesc clipurile fixe generate).
- 24 oct (Szasz): piesa Mr. Grinch e în library/music/xmas/mean-one-grinch.mp3; drop-ul (intră vocea) la 9,1 s → music_start 9.1, ca videoul să înceapă pe drop.
- 25 oct (Szasz, REGULĂ): la hook-uri se transcrie MEREU ce zic personajele din videoul competitorului (Whisper, `limitless/creator-kit/engine/tools.py transcribe`), iar hook-ul nostru zice aceeași replică — vocea se face în Higgsfield (`seed_audio`) și se pune peste clip.
- 26 oct (Szasz, REGULĂ): la fiecare hook audioul (vocea/replica) se face DOAR în Seedance, ca în hook-ul original: `seedance_2_5` t2v fără imagine de start, `generate_audio: true`, replica exactă în prompt; se păstrează doar sunetul, se aliniază pe mișcări și se lipește în montaj.
- 26 oct (Szasz, REGULĂ): personajul MEREU în prim-plan, niciodată în spatele obiectelor (masă/plante/canapea în fața ei = se reface).
- 26 oct (Szasz): hook copiat = Kling video-edit pe clipul original + replica în prompt cu secundele ei („perfect”, hook-ul 3-2-1 la prințesă). Mișcarea identică cu originalul, nu grăbită (halatul cade la fel, tăietura la aceeași secundă) — verificat pe benzi de 10 cadre/s.
- 26 oct (Szasz): la hook copiat, în prompt fiecare acțiune cu secunda și viteza din original (analizat la 10 cadre/s), „never faster” — Kling grăbește căderea halatului.
- 26 oct (Szasz): „nu mai ștergem logouri niciodată” — logo-urile/firmele din clipul de referință rămân exact cum sunt; se blurează doar textul pus peste video. Înlocuiește „fără branduri reale” la hook-urile copiate.
- 26 oct (Szasz): fără blur pe textul concurenței înainte de Kling — se scoate cu o poză curată (Nano Banana Pro) lipită peste zona textului; Kling copiază pata de blur.
- 26 oct (Szasz): textul pe ecran = textul original al referinței, cuvânt cu cuvânt; la hook copiat personajele mereu altele decât în original; în B-roll persoana nu dispare niciodată.
