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
- (18 oct) REGULĂ NOUĂ, pentru toate videourile de acum înainte și pentru ORICE produs (Szasz):
  - Fiecare hook are undeva în cadru steagul american (pe perete, pe verandă, pe o pernă, pe o cană etc.), vizibil dar natural.
  - La B-roll-uri, îmbrăcămintea de dedesubt e în stil american (ex. pijama cu stele și dungi, hanorac de colegiu/varsity, tricou cu steag, flanel + jeans).
  - Folosim doar personaje care arată ca oameni obișnuiți din SUA (aspect, coafură, stil, casă americană), diverși ca înainte; camerele să arate ca locuințe americane.
- 2026-11-05 (Szasz): sunetul hook-urilor Kling se verifică pe spectrogramă (voce/muzică/tic/liniște) înainte de montaj; bucățile proaste se curăță (engine/fixa.py), se studiază fiecare video cadru cu cadru.
- 5 nov (Szasz): sunetul hook-ului = Kling, din analiza Higgsfield (`video_analysis`) + audio3; după generare spectrograma pe fiecare hook (fără voce/„woo”, fără muzică/beat, fără liniște). Hook-ul se oprește la sfârșitul scenei principale — fără cadrul de după (cutia deschisă) când în referință acela e deja B-roll-ul lor.
- 7 nov (Szasz): textele de pe montaj NU se inventează — se pune textul exact din referință (sau textul dat de Szasz), același pe toate videourile din grup. Regula veche cu ~jumătate texte variate e anulată.
- 7 nov (Szasz): start frame-urile/hook-urile se fac doar în camere de SEARĂ (afară întuneric, lumină de la lămpi, brad, șemineu). Start frame realist: nano_banana_pro 4k, prompt de poză iPhone reală (încadrare ușor imperfectă, piele reală, fără look AI).
- 8 nov (Szasz): piesa de la prințesă (`let-it-go.mp3`) NU se mai pune niciodată la videourile Grinch (fusese la zara-set29 și reveal-set32 pe 5 nov). Scoasă din rotația de melodii.
- 8 nov (Szasz): hook și B-roll = ACEEAȘI FATĂ, verificat cu fața mărită lângă poza personajului. Kling video-edit pe clipul de mișcare gv4 păstrează fața actriței din clip → scena din față (unde i se vede fața) se reface cu Kling motion control din poza ei îmbrăcată în halat (gpt_image_2).
- 8 nov (Szasz): în B-roll se taie DOAR ce e în plus: gluga trasă de două ori, statul nemișcat. La săculeți AMBELE picioare intră normal (nu se taie a doua băgare a piciorului); se taie doar pauza nemișcată de după, înainte să închidă halatul. Tăietura între cadre cu halatul în aceeași poziție, verificată la 30 fps.
- 8 nov (Szasz): conectorul și telecomanda = clipurile vechi (connector-sofa-close-1, remote-sofa-close-1), nu cele „peste halat”.
- 8 nov (Szasz): camerele preferate = dormitoare de seară în stilul referinței (brad, pat, ciorapi pe raft, lămpi calde, steag mic).
- 9 nov (Szasz): COZY se face MEREU ca finalul reel-ului https://www.instagram.com/p/Dc_2J9wNZPS/ (12,4–14,6 s): în halat, cu gluga pe cap, se lasă/aruncă într-o parte pe canapea, apoi se strânge în halat, mulțumită. Clip de mișcare: `library/motion/cozy-sofa-plop-Dc_2J9wNZPS.mp4` (2,2 s). Canapeaua = canapea mare și frumoasă dintr-un living în stil Princess (`heatgrump-studio/library/living-*`).
- 9 nov (Szasz): camerele să fie la apus (afară puțin întunecat, nu noapte), stil elegant Princess Comfort; fără să le încărcăm cu obiecte — doar canapele frumoase.
- 10 nov (Szasz): cozy-ul PERFECT = finalul reel-ului https://www.instagram.com/p/DcV9I_yN57e/ (14,9–17,1 s), pentru TOATE halatele; B-roll-ul ca același reel (4,2–11,1 s). Rețeta comună: `heatgrump-studio/RETETA-HALATE.md`. Prințesa are 4 halate (ice-blue, golden-rose, snow-apple, green-lily) în `heatgrump-studio/products/princess/variants/`.
- 10 nov (Szasz): la video, ținuta de sub halat = MEREU o pijama de Crăciun foarte drăguță, potrivită cu halatul: Prințesă → pijama de prințesă (satin roz/pastel, coronițe, fundițe), Grinch → pijama verde/roșie în stil Grinch, Snoopy → pijama cu cățeluși (roșu/alb). Aceeași pijama în hook, B-roll și cozy.
- 10 nov (Szasz): în montajele cu B-roll nu au voie cadre în plus la îmbinări — verificare la 30 fps la fiecare tăietură; săculeții din grinch-v4 se taie la 5,70 s.
- 10 nov (Szasz): la cozy promptul spune clar că picioarele sunt complet acoperite de halat (nu se vede pijama, genunchi, șosete, tălpi). Camerele nu se refac pentru cozy; canapeaua reală se descrie exact.
- 10 nov (Szasz): în B-roll nu se schimbă unghiul la aceeași mișcare; orice plan în plus pus de Kling se taie la montaj (verificare 10–30 fps).
- 10 nov (Szasz): la săculeți picioarele pornesc AFARĂ (desculță, pe podea, în spatele tivului) și le bagă pe rând, câte o dată fiecare; niciodată deja înăuntru și băgate iar; mereu un picior pe podea, nu stă în aer. Scris explicit în prompt (vezi heatgrump-studio/RETETA-HALATE.md).
- 10 nov (Szasz): săculeții NU se refac cu Kling (era mai bine originalul). Se rezolvă din montaj: tăietură de la ~2,5 s (începe să deschidă a doua parte) direct la ~3,1 s (piciorul al doilea sus, gata să intre). Vezi output/boards/grinch/montaj-v6.sh.
- **11 nov — hook rulou (prințesă):** ruloul NU e legat (fără cordon/fundă/curea); referința de halat = pozele fără cordon din `output/p11/ref-nobelt/` (`ref-nobelt.json`). Ruloul mare, pufos, coboară pe jumătate desfăcut, mâinile țin halatul tot timpul. Gluga se mișcă realist: cade moale, cu greutate, se leagănă natural — nu se ridică, nu se umflă, nu se deformează.
- 11 nov (Szasz): B-roll prințesă — piciorul ieșea din sac după ce intră (≈3,5–4,2 s). Se taie 3,4667→4,2 s în toate tail-urile (output/p11/tails/v/*-cut.mp4).
- 11 nov (Szasz): hook-ul rulou se face DOAR în varianta bună (P1-V3: rulou peste cap → ușa → gunoiul, cu muzica lui). Nu mai folosim varianta 3-2-1 frontală.
- 11 nov (Szasz): la hook-urile copiate unde apare produsul altcuiva (ex. grămada din magazin) se face ÎNTÂI fișa produsului (imagine gpt_image_2 cu halatul nostru în scena lor) și se dă ca Image 1 la Kling; altfel Kling doar recolorează produsul lor. La hook-ul rulou → ușă → gunoi la Grinch: audio = reel-ul 3-2-1 (DfcuAALjt2t), «one» la 2,25 s cade pe rulou.
- 11 nov (Szasz): audio mai scurt decât videoul → se repetă O PARTE din mijlocul piesei (nu reîncepe piesa), cu crossfade lung 1,5 s pe bătaie: heatgrump-studio/engine/pad_audio.py <ref> <out> <ieșire> <început_parte>. Ieșirea e ÎNAINTE de orice numărătoare de la final (r321 are un nou «three» la 13,7 s → ieșire 13,4). Fără piese generate.
- 12 nov (Szasz): hook rulou cu Seedance 2.5 (`video_edit` pe hook-ul referinței fără sunet, DcrmIaft5m-): mereu și pozele cu săculeții (pockets_1/2) ca referință, ca la desfacere să se vadă corect interiorul roșu/verde și săculeții. La unele, ruloul VERDE (rulat de la tiv, verdele la exterior) și gluga cu toate detaliile (bordură albă, fața verde cu ochii galbeni, vârf roșu cu moț). `ip_detected` → fără poza glugii. Montaj ca originalul: hook → spate → săculeți → conector → telecomandă → cozy, piesa originalului pe tot, textul lor. Scripturi în output/r17/.
- 12 nov (Szasz): telecomanda NOUĂ = verde HEAT SNUG (timer stânga 1H-8H, căldură dreapta 1-5, cablu împletit crem), ținută PESTE HALAT (nu pe fundal sherpa) — clip output/r17/remote-green-fixed.mp4 (luminițele corectate cu fix_green.py). Conectorul = library/motion/conector-telecomanda-alb.mp4 (0–2,66). La săculeți se așteaptă să se închidă complet halatul, chiar dacă la final rămâne puțin fără muzică.
