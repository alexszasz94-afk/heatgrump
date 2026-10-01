# Export brut din memoria Cowork — /areas/heatgrump-dropshipping.md (29 sept 2026)
# Sursa de adevăr pentru reguli. Liniile [stated] = spuse de Szasz. Notele tehnice = constatate de Claude.

---
name: heatgrump-dropshipping
description: HeatGrump dropshipping product (Grinch-themed heated robe) — product details, content workflow, and tooling preferences. Read when working on HeatGrump ads, copy, or video generation.
sources: [cowork]
aliases: [heatgrump, halat termic grinch]
---

# HeatGrump

[stated] does organic dropshipping; HeatGrump is one of the products
[stated] product is a Grinch-themed hooded heated robe (red top / green skirt, corded remote with timer)
[stated] wants Instagram and Facebook descriptions for the product

[stated] 5 sept 2026: pagina Facebook „Heat Grump Official" a primit restricția „Your Page is no longer recommended" pentru conținut neoriginal/repurposed — status „In review", pas 2 din 3

## Content workflow

[stated] REGULĂ ACTUALIZATĂ (16 sept, înlocuiește regula din 1 sept cu Seedance 2.5 + nano_banana_pro): video pe Seedance 2.0, imagini pe GPT Image 2. Kling nu se mai folosește deloc
[stated] folosim skill-urile lui: reel-replicator + video-frame-extractor. Defaults din reel-replicator: imagini 9:16 (de la 16 sept pe GPT Image 2, nu mai pe nano_banana_pro), fiecare prompt se termină cu "candid iPhone photo, natural window light, photorealistic, no text overlays"; video 1080p mode std cu start_image = frame-ul aprobat, durata clipului = durata cadrului din sursă; niciodată text ars în frame sau video
[stated] flux reel-replicator: extrage frame-urile din sursă → importă referințe reale în Higgsfield (produs cu 3-4 poze REALE, niciodată inventate AI, plus fundal și avatar) → generează UN hero frame și îl aprobă el → hero-ul devine ancoră pentru toate celelalte frame-uri → stop pentru aprobare înainte de orice video
[stated] going with: one frame generated per reel concept, approved by him before moving to the next; no "just in case" regenerations without his explicit approval of the prompt first
[stated] căptușeala interioară a halatului HeatGrump e VERDE (nu albă) — de respectat în orice frame unde se vede interiorul
[stated] the corded remote/controller must NOT show any lit electronic display when it's not plugged in — keep it logically consistent
[stated] makes short videos so more cuts/frames fit in
[stated] copies a chosen reference video first, then adapts it
[stated] adds the on-screen text himself afterwards — only wants the raw frames/clips generated
[stated] the product must look identical in every single generation — always reuse the same product reference, never let it drift
[stated] wants to see generated start frames and approve them before any video is generated
[stated] REGULĂ STRICTĂ ȘI GENERALĂ (4 sept, după hook-ul 3-2-1 declarat "a ieșit perfect"): rețeta validată se salvează integral în /home/claude/heatgrump_hook_templates.md — referințe cu ordinea lor, promptul de imagine și promptul de video, cuvânt cu cuvânt — și de acolo se copiază, fără modificări; la alt reel se schimbă DOAR camera și personajul
[stated] principiile validate ale rețetei: referința-țintă a lui pe poziția 1 cu "reproduce one to one" + listă numerotată cu exact ce se schimbă; ce trebuie să iasă perfect se scrie ca PRIMUL bloc, marcat "ABSOLUTE RULE, HIGHEST PRIORITY"; la produs se pun MULTE referințe din unghiuri diferite (6, nu 2-3); timeline pe secunde cu ultimul beat dedicat produsului și camera fixă; mișcarea se descrie prin greutate și material, nu prin coregrafie de membre
[stated] REGULĂ audio ACTUALIZATĂ (4 sept): TOATE clipurile se fac cu generate_audio TRUE, fără excepție — inclusiv B-roll-urile (B1, B2, cozy, unboxing, conector, telecomandă); sunetul se descrie diegetic în prompt (doar sunetele a căror sursă se vede mișcându-se), fără muzică și fără voce acolo unde nu e replică. Anulează regula veche „b-roll fără sunet"
[stated] telecomanda halatului are trepte de căldură cu O SINGURĂ luminiță aprinsă odată — când trece pe treapta următoare, luminița anterioară se stinge; nu se acumulează
[stated] referințele validate NU se schimbă niciodată cu altceva asemănător — dacă nu găsesc referința corectă, întreb, nu improvizez

## Produs nou: halat termic cu buzunar pentru câine (varianta Santa)

[stated] al treilea produs: halat/pătură cu glugă oversized, bleumarin, căptușeală sherpa albă, buzunar-cangur uriaș în față cu clapă cu capse în care încape câinele, buton de încălzire pe buzunar dreapta jos
[stated] vrea o variantă Santa Claus a acestui produs, făcută la fel ca la Grinch
[stated] lucrează în două chat-uri Cowork separate pe același flux (Grinch + produsul nou) și vrea ca amândouă să știe exact aceleași reguli — memoria e sursa comună, nu fișierele din sesiune
[stated] produsul real Santa (poza trimisă): pluș roșu vin, glugă cu tiv sherpa alb + vârf de căciulă de Moș cu pompon alb, manșete late albe, buzunar-cangur uriaș cu clapă din aceeași țesătură roșie și 5 capse albe perlate (FĂRĂ centură neagră, FĂRĂ cataramă aurie), tiv roșu simplu fără blăniță, buton negru pătrat dreapta jos pe buzunar, interior sherpa alb
[stated] mecanismul de încălzire (ca la competitori, ex. ToastyHoody): perne de încălzire micro impermeabile integrate în toată țesătura halatului — o singură apăsare de buton încălzește tot halatul
[stated] referința de produs Santa în Higgsfield: media_id a44c5101-a697-4958-908f-baa0782ccbab
[stated] REGULĂ buton: butonul de pe buzunar e stins înainte de apăsare, iar DUPĂ ce e atins se luminează VERDE — de respectat în orice frame/clip de după apăsare
[stated] referința de produs cu SĂCULEȚUL DESCHIS trebuie inclusă în FIECARE generare unde punga se deschide, și trebuie respectată mereu — ea decide cum arată clapa care închide/deschide săculețul și cât din căptușeala ei albă se vede
[stated] capsele de pe clapă nu se văd când săculețul e deschis — clapa e întoarsă, deci fără capse în cadru
[stated] buzunarul-săculeț al halatului Santa trebuie desenat mai MARE și mai încăpător decât în poza originală — modificarea se face direct în referința de produs, ca să se propage în toate cadrele
[stated] la B-roll-uri, cadrul static îl arată ținând câinele în brațe deasupra săculețului, iar băgatul efectiv în săculeț se face din animație — nu se forțează în imaginea statică
[stated] primul B-roll (B1): bagă câinele în săculeț — câinele stă pe spate rezemat de pieptul ei ca un bebeluș ținut cu fața în față, mâinile îl prind de coaste de o parte și de alta, gluga trasă complet peste față (fața nu se vede deloc), canapea de piele închisă, decor de Crăciun sus-stânga
[stated] REGULĂ cameră: NICIODATĂ zoom în clipuri (fără push-in, fără pull-out) — cameră statică sau handheld natural, mișcarea vine din subiect, nu din obiectiv

## Produs nou: halat termic ren (Rudolph)

[stated] al doilea produs: halat termic lung cu glugă tip ren — maro cu blană crem, coarne, nas roșu, fular roșu-crem cu ciucuri, clopoței, codiță pompon în spate, telecomandă cu fir și display
[stated] îl vinde organic și face videouri 1 la 1 după competitori (îmi dă video-ul de referință, apoi copiem)

## Produs nou: halat termic Santa lung (varianta roșie simplă) — 5 sept

[stated] produs nou, „practic același ca la Grinch doar că e tot roșu, fără modelul de Grinch": halat lung până în podea, roșu vin uni, glugă tip căciulă de Moș cu vârf lung și pompon alb, tiv sherpa alb la glugă/margini/tiv, manșete late albe, două buzunare aplicate cu bandă albă, cordon negru legat fundă cu capete aurii, căptușeală sherpa albă, telecomandă cu fir și display digital
[stated] media_id-uri Higgsfield confirmate (5 sept): produs Santa lung = d32a0984-7c55-47c9-a34c-eecde527ed35; personaj B-roll = 3ccdbd6c-420b-484a-80c7-8323cc9a19f0; cameră/decor = bf87d88a-7926-49fb-b46f-d23951e287b7; cutia HeatGrump (de modificat) = 5e8840d4-d514-4016-9fa3-e0893a13bdee
[stated] pozele de concept pentru setul de referință al produsului: fundal alb ca poza reală, purtate de un model neutru (nu de personajul lui)
[stated] cutia trebuie modificată — exact ca cea de la HeatGrump, dar în varianta Santa
[stated] REGULĂ B-roll produs nou: se folosesc EXACT aceleași referințe ca la HeatGrump, se schimbă DOAR referința de produs și cea de cutie
[stated] REGULĂ STRICTĂ: telecomanda ȘI conectorul trebuie să fie EXACT ca la HeatGrump în orice frame/clip — nu se folosește telecomanda din poza furnizorului produsului nou
[stated] definiția B-roll-urilor (aceeași ca la HeatGrump): B1 = când ÎMBRACĂ halatul; B2 = stă simplu în halat, cu halatul semi-desfăcut
[stated] cutia Santa generată 5 sept e aprobată și se păstrează (job 2c35b8a7-d7f9-4a0f-9409-6d3a336032b0) — brandingul HeatGrump rămâne integral pe cutie, se schimbă doar halatul desenat
[stated] lucrează în două chat-uri Cowork; când greșește chat-ul, vrea un fișier de predare (brief complet cu media_id-uri, reguli și prompturi cuvânt cu cuvânt) pe care să-l încarce în celălalt chat
[stated] REGULĂ glugă halat Santa lung: gluga are o COADĂ lungă de căciulă de Moș care, cu gluga pusă, cade ÎN FAȚĂ peste umăr, cu pomponul alb la nivelul pieptului — niciodată ascunsă în spate, niciodată ciot scurt
[stated] B1 se face CLOSE-UP (nu cadru întreg)
[stated] 7 sept: chatul Santa = halatul Santa LUNG roșu simplu (nu cel cu buzunar de câine); setul de referințe de produs Santa există deja și se refolosește, nu se regenerează
[stated] vrea ca acest chat să fie geamănul chatului Grinch: același mod de lucru, aceleași setări, aceeași structură de prompt — se schimbă doar referințele Santa, ca să nu le mai schimbe el de fiecare dată

### Referințe Higgsfield recuperate din istoricul de generări (nu declarate de el — reconstituite 7 sept, fișierele de sesiune se pierd odată cu containerul)

Santa lung — set de studio 5 sept: poza reală produs d32a0984-7c55-47c9-a34c-eecde527ed35; master față 5dfbbb9b-dea2-4c8d-ad1b-76f0fbcc5b08; spate 2381e60b-e858-4393-b3cc-97920501c7e5; macro glugă 0e125cf2-8b5e-4cd5-8e17-6fa582e54ed6; purtat deschis (căptușeală + manșete) d47af17e-b421-4c58-a110-9a44d9505016; detaliu talie/cordon 38822fe8-65eb-44cf-9f83-d0b614b341cb; telecomandă 8b6d32e4-8f40-40fa-a2a1-58de54c227f4. Cutia Santa aprobată: job 2c35b8a7-d7f9-4a0f-9409-6d3a336032b0.
Telecomandă reală cb73364c-9cc0-4420-82dc-5e1269cae33c; conector gri 2774615c-3876-49c9-81e3-43e965688bae (aceleași ca la HeatGrump).
Personaj/cameră perechea curentă Grinch (7 sept): femeia 0c3ee167-2fc3-4d59-9f8a-c24cf103b580, camera 82ee7f9b-d6c5-4ae4-bfa4-ed291760747f. Perechea Santa din 5 sept: 3ccdbd6c-420b-484a-80c7-8323cc9a19f0 + bf87d88a-7926-49fb-b46f-d23951e287b7.
Produs Grinch (7 sept): 3d796f4b, 2003f0f1, 5918350c, ff699c0e, 8e070e9a, 2e60ab93, 422be037, 9c8f69c1, beaafb05, 3ff9efad; magazin 156609b6.
Setări curente: imagine nano_banana_2, 9:16, 4k (3072x5504); video seedance_2_5, 9:16, 1080p, bitrate high, generate_audio true.
[stated] 7 sept, Santa lung: cutia curentă e cea NOUĂ, media_id a42434ee-83a3-46b0-92c7-b0ae906a2a49 (cutia din 5 sept, job 2c35b8a7, e depășită); referința-țintă pentru conector e 64da16fa-d5f7-4868-b261-76f209a47ddd, se reproduce 1:1 și se schimbă doar materialul (roșu vin + sherpa alb, fără verde)
[stated] telecomanda la Santa = cea de la HeatGrump (cb73364c-9cc0-4420-82dc-5e1269cae33c); plăcuța de telecomandă din setul Santa de studio (8b6d32e4) era greșită și s-a înlocuit cu generarea nouă 98e9824f-3ad0-45ab-a6e7-b253fdb02a0e
[stated] 7 sept, Santa lung: personaj nou 55de9190-22c7-4629-bc63-d4ee01ab9529 și cameră nouă 5b60f4e1-276a-4fa8-a2d1-7727fcb56217 (încărcate de el pentru B-roll-uri; înlocuiesc perechile vechi)
[stated] REGULĂ referință halat: se pune referința în care se vede halatul ÎNTREG, ca să iasă lung până jos — plăcile de corp întreg merg primele în lista de referințe
[stated] REGULĂ glugă Santa lung (7 sept, corectură): coada glugii e SCURTĂ și bondoacă, cam o palmă, cu pompon mare — nu coadă lungă până în talie; cu gluga pusă cade în față peste umăr cu pomponul la piept
[stated] referința de poză pentru hook-ul 3-2-1 (cum stă cu ruloul deasupra capului) = 2c4c8d12-e02d-46b5-9fa4-b8cd525f30f3, încărcată 7 sept

Notă tehnică Higgsfield (constatată 7 sept, nu declarată de el): la generate_image se cere modelul `nano_banana_pro` ca să iasă calitatea bună (`nano_banana_2` e rutat pe flash); la generate_video cu seedance_2_5 trebuie `mode: "omni_reference"`, altfel backendul refuză start_image cu eroare t2v. Presetul „IN THE DARK" trebuie refuzat cu declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612.
[stated] reel nou Santa (7 sept seara), referințe încărcate de el: femeia 04054c94-bd4b-4607-b591-042118207962; bărbatul da6d709c-2106-4160-8d74-6333af13d54d; intrarea casei d8477c20-ba5d-4be3-9a08-c0662cd75d7e; camera 4b876021-781f-4565-ab68-e608df69549c
[stated] hook-ul reel-ului nou: ea vine spre intrare doar cu o bluză de Crăciun pe ea, i se vede că îi e foarte frig, zice „Oh my God, I'm freezing!"; iese bărbatul cu halatul și zice „Take this."
[stated] B-roll-urile reel-ului nou se fac cu femeia, în modul clasic: B1, B2, telecomandă, conector și cozy
[stated] REGULĂ absolută de încadrare: halatul trebuie să se vadă întreg, până jos la podea, în TOATE cadrele — niciodată tăiat, inclusiv la B1
[stated] REGULĂ permanentă telecomandă: se folosește MEREU promptul lui de video pentru telecomandă (cel cu „THE FRAME NEVER CHANGES / THE LIGHTS CLIMB FROM THE BOTTOM UPWARDS / patru apăsări, 1→5, o singură luminiță aprinsă odată"), cuvânt cu cuvânt de fiecare dată; la Santa se schimbă doar blocul de mânecă (roșu vin cu sherpa alb, fără verde)
[stated] REGULĂ permanentă culoare: coada glugii e din același pluș ca halatul, un singur burgundy mat — nu roșu aprins; singurul alb pe ea e pomponul
[stated] reel Santa #4 (9 sept), referințe încărcate de el (personaj + cameră): 41826377-e4c8-4029-a588-c764749c7f0f și 827ac95c-26f8-432e-96b0-67f02e2aca29
[stated] setul „clasic" de frame-uri = B1, B2, telecomandă, conector, cozy + unboxing cu cutia noastră
[stated] REGULĂ B2: clipul B2 se face FĂRĂ SUNET (generate_audio false) — excepție de la regula generală de audio; mișcarea trebuie să fie lină, nu bruscă; săculeții de la tiv sunt din același material ca halatul (la Santa = roșu vin, niciodată verde — referințele de construcție edf080f5/c8b8fbf3 se folosesc DOAR pentru formă, nu pentru culoare)
[stated] reel Santa #7 (11 sept), referințe încărcate de el: personaj ad7f1bc4-3b26-43a0-9776-7d4211a124bd, cameră 2a23ea0c-e9db-4386-b5cd-c03869a9c927; hook-ul = cadrul din magazin cu femeia cu coșul care se uită la raion (referința-țintă f0c26e9c-8c61-4ec9-9454-dbf32cdc66af)
[stated] reel Santa #6 (10 sept), referințe încărcate de el: personaj 276809df-dfe2-4e4b-997d-e429b9ec65b5, cameră 860d047e-67cc-4b61-a75c-50d292b9b8f8
[stated] REGULĂ: reel-urile din chatul Santa sunt EXCLUSIV Santa (halatul roșu simplu) — nu se amestecă niciodată cu materiale Grinch; Grinch apare aici doar dacă cere explicit poze de site
[stated] REGULĂ lumină cozy: fără blitz — nicio sursă de lumină în poziția camerei, lumină ambientală caldă de seară de la brad + veioză, fără pată de lumină pe ea, contrast scăzut
[stated] REGULĂ DEFINITIVĂ B2 (nu se mai schimbă niciodată): START FRAME-ul e cadrul normal, ea stând în picioare cu halatul semi-desfăcut, corp întreg până jos; VIDEO-ul e secvența cu SĂCULEȚII (buzunarele de picioare de la tiv), cu referințele de săculeți în prompt

## Produs nou (11 sept): papuci încălziți Santa Claus (Heated Slipper Santa Claus)
[stated] 11 sept: produsul nou preia TOATE regulile HeatGrump; primul pas = setul de poze de concept făcut exact ca poza trimisă, ca referințe în Higgsfield (poza o încarcă și în chat, și în Higgsfield)
[stated] poza trimisă (infografic): papuci-botoșei din pluș roșu cu fața lui Moș Crăciun 3D în vârf (ochi, nas, barbă și mustață albe pufoase), căciulă cu pompon alb, dungă verticală albă pe lateral, curea neagră cu cataramă aurie pătrată, guler de blăniță albă, talpă neagră antiderapantă; panou de control pe lateralul exterior (buton power + 3 LED-uri: amber/albastru/roșu = low/medium/high); baterie reîncărcabilă 7.4V + cablu USB-C; elemente de încălzire în vârf și talpă; cutie cadou roșie „Heated Slipper Santa Claus"
[stated] papuci Santa — referința lui (infograficul) în Higgsfield: media_id 651b7c47-9253-4a69-8ea2-c0fd46a56703; vrea întâi papucii inițial (Master), apoi decide restul
[stated] papuci Santa — setul de referințe = DOAR unghiurile papucilor (fără cutie, fără purtat, fără interior); „ajunge ca referințe". Master 3/4 față = job a70394f2-94bf-496f-8b35-93c6fae61467; unghiuri (11 sept): față 43532b32-56bc-41ff-bdf2-5528d4614314, profil lateral cu panou 75b828bf-09d4-4c4f-8e72-0d6326d71053, de sus a0e37138-c3d0-421d-badb-ce5bb0d7a1e8, spate a0ffee3b-4e14-4e7d-9786-189851195c2d, 3/4 spate 889ef858-2631-445d-a360-d7266885a74a, talpă b5955c7a-063d-4ae2-aad2-d534565ee9ea
[stated] REGULĂ DEFINITIVĂ UNBOXING (11 sept, „așa le facem toate"): unboxing-ul se face MEREU după șabloanele lui — „Unboxing - Image" pentru frame și „Unboxing - Video" pentru clip, cuvânt cu cuvânt (@Image 1 = avatarul, @Image 2 = cutia produsului, @Image 3 = camera/fundalul); cameră fixă, 4 s, o singură mișcare — scoate halatul din cutie, fața ei niciodată acoperită, un singur produs în cadru, fără voce, doar un oftat mic de încântare. În plus, logica ferestrei transparente a cutiei trebuie să fie coerentă: la început se vede plușul prin fereastră, pe măsură ce îl ridică fereastra se golește, niciodată cutie plină în timp ce ține halatul în mână
[stated] reel Santa #8 (11 sept), referințe încărcate de el: personaj 4fdaa325-c5ba-47ba-b853-0764d0a8f125, cameră 53cfab50-d735-47e3-ba86-efff44a68098; lumina camerei rămâne exact ca în referință (nu se forțează zi/seară); îmbrăcămintea pe dedesubt = tricou cu baschet + pantaloni de pijama de Crăciun
[stated] reel Santa #9 (12 sept), referințe încărcate de el: personaj 07017f88-5f4e-4a28-9e9d-ea3e0c889194, cameră 9bc0da6c-8c19-45bf-8140-108bafc9eea2
[stated] REGULĂ B1 (11 sept, „ia din 7 sept unul care l-am și animat"): promptul canonic de imagine B1 = job 6871458d (7 sept) și promptul de video pereche = job 3d00ccfc — se copiază cuvânt cu cuvânt, se schimbă doar camera, personajul, ce poartă pe dedesubt și lumina; salvate în /home/claude/santa_templates.md §9
[stated] REGULĂ telecomandă video: promptul LUI (job e8649b3c — „THE FRAME NEVER CHANGES / THE LIGHTS CLIMB FROM THE BOTTOM UPWARDS") se rulează cuvânt cu cuvânt, fără bloc de mânecă adăugat, fără nicio modificare; salvat în /home/claude/santa_templates.md §10
[stated] hook nou (11 sept, copiat după clipul „Send this to a Cat Mom"): ea merge spre cameră într-un magazin de Crăciun cu o cană de Crăciun cu cafea în mână, zice „oh my God", scapă cana care se sparge și curge cafeaua pe jos, iar camera trece pe raftul cu cutiile noastre
[stated] REGULĂ 3-2-1 REVEAL LA CUTIE (12 sept): se folosesc șabloanele LUI „321 - image" și „321 - Video", cuvânt cu cuvânt (@Image 1 = camera/locația, @Image 2 = personajul, @Image 3 = cutia); salvate în /home/claude/santa_templates.md §11. Poziția corectă: o mână SUB cutia acoperită, cealaltă prinde pânza de la MIJLOC; cutia sub pânză trebuie să aibă mărimea reală a cutiei; îmbrăcămintea = aceeași ca la unboxing
[stated] setul complet al unui reel (12 sept) = B1, B2, telecomandă, conector, cozy, unboxing, oglindă (se filmează în oglindă purtând halatul, arată halatul și e fericită) + hook-ul
[stated] reel Santa #10 (12 sept), referințe încărcate de el: personaj 7c285f81-33b5-480c-9e03-b178e471b1fa, cameră 95909593-b4a9-48c7-bb7f-c2702280e3c8
[stated] reel Santa #11 (16 sept), referințe încărcate de el: personaj aa23a463-9f3c-40df-a780-eacf4ad89e97, cameră 038639ef-3e99-475a-8a02-9bd57e3b2afc
[stated] hook nou (12 sept, copiat după clipul de lansare BTS la H&M): lansare de magazin tip MiniSo într-un mall — arcadă de baloane, panglică, angajați în tricouri roșii, manechine cu halatul nostru pe un podium; cele două femei de la panglică numără „3, 2, 1", taie panglica și toată lumea din spate strigă „yeee" și aplaudă. Mărcile reale (H&M, MiniSo) nu se reproduc — magazin generic, fără nume și fără logo

## Concept nou (16 sept): HeatGrump ca pătură purtabilă uriașă

[stated] decizie 16 sept: conceptul halatului Grinch se REFACE ca pătură purtabilă uriașă, ca la competitor — volum de pătură, tiv cu doi săculeți de picioare (foot pouches) cu capse, ca să se poată copia 1:1 reel-ul de referință
[stated] referințele-țintă de siluetă încărcate de el: halat purtat ÎNCHIS (con uriaș până în podea) = e46c4249-a39f-4ea4-830b-fc50c67ff86b; halat DESCHIS (interior integral pluș, săculeți de picioare la tiv) = 5eefa24d-682c-46be-b9d9-bd4c6056304c
[stated] 5eefa24d rămâne referința pentru B2 — așa arată halatul deschis
[stated] referințele de produs Grinch reîncărcate 16 sept: a9ebff95-7b4e-4a10-92f5-4c9377d01fd4, b3adf7e2-adcd-4ffc-9989-1fa0c822c78f, 28a3d14b-3578-4569-bcf2-33a84d478cc0, 71882d2b-aeab-4cc1-afa3-4f9d1a1951c5
[stated] conceptul de pătură purtabilă e DOAR pentru chatul Grinch — salvările și referințele lui nu se duc în chatul Santa
[stated] referință B2 cu piciorul afară din săculeț (cum se deschide săculețul): a102be5c-2dbf-485f-a3d2-90205079a23b
[stated] ordinea plăcilor de referință pentru conceptul nou: 1) halat închis, 2) deschis, 3) spate, 4) 3/4, 5) glugă
[stated] referințe B1 (conceptul pătură, 16 sept): poziția de START 78072f44-fbd6-43ab-b25b-bfbe3e56b5ca (din spate, ține halatul deschis în spatele ei, gata să-l îmbrace); poziția de FINAL e82766da-2896-4a54-982c-eb6e91109125 (din spate, îmbrăcat cu gluga pusă, vârful căciulii în sus cu pompon)
[stated] referință B2 poziția de final (halat închis, mâinile pe marginile glugii): 40bfeea8-291c-45b2-9e43-59ae64955ba8
[stated] vrea referințe pentru absolut orice mișcare — cu cât mai multe, cu atât mai puțin ghicește modelul
[stated] set referințe de mișcare B2 (deschiderea halatului, picioarele în săculeți, lateral închis) — 16 sept: 8e9e3445-df04-4785-93bc-5b6f7e46b968, 01c3e660-e48e-449d-8b42-438f0cf32696, bfaa8621-67ea-4d45-a9b3-c35ced91a180, 179d4dc3-0829-4e17-aedb-1ba4aa2b9def, 4ae225b7-03d8-4bac-9afc-e2edc4ab6cc2
[stated] construcția tivului (din referințe): colțurile de jos formează doi săculeți care ies în față, cu bandă sherpa pe margine și decupaj în V la mijloc; săculeții sunt din materialul exterior al halatului (la Grinch = verde), cu căptușeala la fel
[stated] plăcile de referință produs generate 16 sept (concept pătură): închis db7979bb, deschis 11dfc610 (refăcut; 5fc054b5 e depășit), spate 47489906, 3/4 daf2a33b, glugă 2be2a9d7
[stated] REGULĂ săculeți: cei doi săculeți de picioare se UNESC la mijloc, la o singură cusătură — nu sunt două pungi separate cu gol între ele; tivul face un W lat continuu
[stated] REGULĂ halat deschis: când se deschide, halatul trebuie să fie LAT în partea de sus — bandă orizontală lată la nivelul umerilor, mult mai lată decât umerii, marginile cad aproape drept în jos; niciodată triunghi strâns sus
[stated] REGULĂ GENERALĂ: la orice generare se pun CÂT MAI MULTE referințe, la toate cadrele — nu doar plăcile de produs, ci și toate referințele de construcție și de mișcare
[stated] referință halat deschis văzut de sus: 31e4aa58-7a75-4eed-b271-cfd58d76fc71
[stated] partea cea mai problematică la generări sunt săculeții de picioare — acolo se pun mereu toate referințele de construcție
[stated] REGULĂ FLUX (16 sept, „de acum"): B-roll-urile (B1, B2, cozy, 3-2-1, hookul cu tava) se fac DIRECT în Genjutsu din clipurile lui tăiate, fără start frame, la 480p — el zice ce se înlocuiește plus detaliile; restul cadrelor rămân pe fluxul normal cu start frame aprobat înainte de video. El dă doar referința de personaj și cea de cameră; referințele de produs și construcție se refolosesc din memorie
[stated] BIBLIOTECA DE CLIPURI DE REFERINȚĂ DE MIȘCARE (Genjutsu motion control, se refolosesc la fiecare reel — se schimbă doar personajul și camera): B1 = 5133a653-d5e3-4077-a102-43818fb736c0; B2 = 6243c22d-ed26-4df8-8a68-0d4ff29219bd; cozy = 8042602c-c548-45de-aa77-6d42366e058e; reelul întreg de 15,8 s = 93fb9535-f17f-4d78-a1c3-795daaa40dfe
[stated] B1 rulat cu motion control 480p pe 17 sept = job 3d40f6d1-fd57-41cf-9880-52948b6e191a (26 credite); se păstrează ca referință de flux
Notă tehnică (constatată 17 sept, nu declarată de el): hf_mult_replace_object refuză clipurile scurte cu 422 (B1 respins, clipul de 15,8 s acceptat la 104 credite) — pentru B-roll-uri scurte merge doar hf_mult_motion_control (~26 credite la 480p). Costuri: motion control pe 15,8 s = 144 credite.
[stated] clip de referință de mișcare pentru hookul 3-2-1 = bcdaebd7-18e4-43fc-89a8-59294ceb0fcb (mai lipsește doar hookul cu tava)
[stated] clip de referință de mișcare pentru hookul cu tava = 673624ef-1edb-478e-b8e9-9b51d6dacba1 — biblioteca de mișcare e COMPLETĂ (B1, B2, cozy, 3-2-1, tava)
[stated] 17 sept: NU se mai folosesc referințele de săculeți din runda a doua — se revine la setul de referințe de dinainte (plăcile de produs), pentru că de acum se lucrează cu Genjutsu
[stated] 17 sept: NU se mai face reel-ul întreg de 15,8 s dintr-o bucată — doar clipuri separate
[stated] 17 sept: toate clipurile se generează FĂRĂ TEXT — niciun overlay, niciun subtitlu, niciun emoji ars în imagine
[stated] reel Grinch nou (17 sept), referințe încărcate de el: personaj 3bf814c6-9fd7-466f-bc75-7702b931f0c3, cameră 2c382217-5ac1-4970-8832-dda74034ed2f
[stated] REGULĂ: îmi spune de fiecare dată dacă personajul reel-ului e BĂIAT sau FATĂ — se respectă în toate cadrele, inclusiv la macro-uri (mâna de pe telecomandă, de pe conector). Reel-ul din 17 sept = BĂIAT
[stated] 17 sept: placa de oglindă nu se face la reel-ul ăsta

### PROMPTUL CANONIC DE TELECOMANDĂ (video), dat de el 17 sept — se rulează CUVÂNT CU CUVÂNT, 5 secunde, fără modificări
THE FRAME NEVER CHANGES: one locked macro camera, one continuous take, no zoom, no cut, no re-frame. The controller, the hand, the printed labels, the background blur and the exposure stay exactly as in the start frame. The controller keeps the same shape, the same white plastic and the same printing throughout — nothing morphs, no label ever changes.
THE LIGHTS CLIMB FROM THE BOTTOM UPWARDS — ABSOLUTE RULE, HIGHEST PRIORITY: there is a vertical row of five small indicator lights. The BOTTOM one is number 1 and the TOP one is number 5. The lit light travels UPWARD along that row, one step at a time: 1 to 2, 2 to 3, 3 to 4, 4 to 5. It only ever moves UP, never down, never sideways, never skips a step, never jumps back to the bottom.
EXACTLY ONE LIGHT IS LIT AT ANY MOMENT: when the next light comes on, the previous one goes dark in the same instant. Two are NEVER lit together, not for a single frame. The row NEVER fills up like a battery bar, never lights progressively, never stays lit behind the moving one.
ACTION, PACED FOR FIVE SECONDS: the clip starts with the BOTTOM light lit and the four above it dark. The thumb presses the button four times, evenly spaced across the five seconds — at roughly 0.6s, 1.7s, 2.8s and 3.9s. On each press the lit light steps one place UP the row. After the fourth press the TOP light is the only one lit and it stays lit while the thumb rests for the remaining second. The thumb visibly travels down and back up on each press — the button movement is readable. The presses are brisk but never rushed or blurred.
AUDIO: one short dry button CLICK at exactly the frame of each press, four clicks total, matching the thumb exactly. Quiet indoor room tone otherwise. No music.
Human-paced movement, correct number of fingers, no extra limbs, no morphing.
Candid raw iPhone 12, film grain, no AI glow, no smoothing.
(ultima linie actualizată 17 sept seara: setările „-7 contrast, +3 exposure" au fost scoase la cererea lui — nu se mai pun în niciun prompt)
[stated] reel Grinch #2 (17 sept), personaj FATĂ: personaj 34c8ae32-f372-43e2-a692-825a5a6bd4b7, cameră 68df18a3-8a81-44be-a0ac-e500b925b37c; set de cadre = la fel ca reel-ul precedent DAR fără hookul cu tava și fără 3-2-1 (deci B1, B2, cozy, conector, telecomandă, unboxing)
[stated] REGULĂ PERMANENTĂ conector: în clipul de conector cele două jumătăți trebuie MEREU să intre una în alta, complet, fără gol rămas — nu se ating și se opresc
[stated] REGULĂ telecomandă (placă): se face „clasic", ca placa aprobată din reel-ul #1 (job 4e7a126c) — telecomanda ținută frontal, umple cadrul, degetul mare pe buton, cablul iese pe jos, TOATE luminile stinse; se schimbă doar mâna (bărbat/femeie)
Notă tehnică (17 sept): unboxing-ul cu halatul Grinch + cutia brand-uită a fost respins de Higgsfield cu status `ip_detected` (filtru de proprietate intelectuală)
[stated] REGULĂ de acum (17 sept): clipurile Genjutsu se fac la 720p, nu 480p
[stated] REGULĂ ACTUALIZATĂ (17 sept seara, „folosim 1080p de acum" — înlocuiește regula de 720p de mai devreme în aceeași zi): 1080p la TOATE clipurile, inclusiv Genjutsu și Seedance 2.0
[stated] reel Grinch #4 — cameră schimbată de el: f71261e7-2e87-4df2-bc61-acaf840888ce (înlocuiește d7e995db); personajul rămâne c41a3f84
[stated] B2 are DOUĂ variante de clip de referință, se alternează de la un reel la altul ca să nu pară toate la fel: varianta A (fără față) = 6243c22d-ed26-4df8-8a68-0d4ff29219bd; varianta B (i se vede fața) = 6731a06f-f6c0-48d9-a001-5047c85ca5d6
[stated] reel Grinch #3 (17 sept), personaj FEMEIE MAI ÎN VÂRSTĂ: personaj ca758a49-ae7d-4c74-b840-93498cb4b017, cameră 3ce50ece-94d1-47f1-8ff5-cbe330dff81b
[stated] hook „concept vs product": ea poartă un halat verde subțire, prototip făcut de mână, cu perne de încălzire, sârme, folie și bandă lipite pe căptușeală; stă pe marginea patului cu o cană de Crăciun, tremură de frig, bea o gură, apoi închide halatul — și tot îi e frig
[stated] REGULĂ îmbrăcăminte ACTUALIZATĂ (29 sept, înlocuiește regula din 17 sept „exclusiv din referința de personaj"): pe dedesubt mereu îmbrăcăminte NORMALĂ și DIFERITĂ la fiecare personaj/reel — pijama de Crăciun, ceva cu America / stil american sau ceva cozy; eu aleg. Rămâne aceeași în toate cadrele aceluiași reel
[stated] REGULĂ produs Grinch: buzunarele halatului NU au fața de Grinch pe ele — sunt buzunare simple, pluș verde cu bandă sherpa albă, fără print, fără logo; fața verde apare DOAR pe panoul din față al glugii
[stated] 17 sept: mi-a dat din nou șabloanele „Unboxing - Image" și „Unboxing - Video" (cuvânt cu cuvânt) — salvate în /mnt/user-data/outputs/heatgrump-grinch-reel-spec.md; @Image 1 = avatar, @Image 2 = cutia, @Image 3 = camera. Rulate așa, unboxing-ul Grinch a trecut (placă 215b0c6f, video 35150f11) — nu a mai fost respins cu ip_detected
[stated] la B2 din reel #3 îmbrăcămintea de dedesubt = bluză gri simplă
[stated] REGULĂ PERMANENTĂ (17 sept, „de acum"): plăcile de conector și de telecomandă se fac un pic mai CLOSE-UP și lângă brad sau lângă pat — bradul/patul se văd recognoscibil în fundalul blurat
[stated] reel Grinch #4 (17 sept), personaj FATĂ: personaj c41a3f84-78d5-46e0-a451-5134a3e92c22, cameră d7e995db-0517-4f74-b9bc-e1b64a2f498d
[stated] REGULĂ conector: placa de conector se face 1:1 după placa validată din reel-ul precedent (referința-țintă pe poziția 1), nu se descrie conectorul cu cuvinte proprii — descrierile inventate (pini/găuri) îl fac să iasă alt tip de mufă
[stated] REGULĂ PERMANENTĂ (17 sept, „de acum"): NU se mai pun setările de contrast/expunere în prompturi (fără „-7 contrast, +3 exposure")
[stated] REGULĂ telecomandă (placă): telecomanda are EXACT cinci luminițe indicatoare, toate cinci vizibile — cea de JOS lipsea și trebuie desenată explicit, neacoperită de degetul mare și netăiată de marginea cadrului
[stated] REGULĂ 3-2-1 în chatul Grinch: NU se folosește cutia în cadru — singurul produs vizibil e halatul (diferit de regula 3-2-1 de la Santa, care e reveal la cutie)
[stated] REGULĂ FLUX (23 sept, „de acum"): conectorul, telecomanda ȘI unboxing-ul se ANIMEAZĂ DIRECT, fără pasul de aprobare a plăcii (unboxing-ul cu condiția ca placa să se facă mereu cu cutia pe jos)
[stated] REGULĂ unboxing (23 sept): cutia stă MEREU pe jos, pe podea — niciodată în aer sau pe mobilă
[stated] 23 sept: face reel-urile în serie (5 deodată — el încarcă 5 personaje + 5 camere în ordine perechi) și vrea la final o pagină HTML cu clipurile fiecărui reel în ordinea de montaj, cu personajul și camera folosite lângă fiecare reel
[stated] lot de 5 reel-uri Grinch (23 sept), perechi personaj/cameră: 1) aab1395b + 7e28b0e7; 2) 072acc6a + 1f7246b1; 3) 8306bd0e + 165f1e6e; 4) 3e1308e8 + 12f88af7; 5) 5caa961a + b9c86778

[stated] REGULĂ unboxing video (27 sept): la animarea unboxing-ului se pun MEREU cel puțin 1-2 referințe de produs cu halatul (cum arată), pe lângă cutie — nu doar cutia
[stated] REGULĂ rotație (29 sept): clipurile de mișcare Genjutsu pentru B1, B2 și cozy se ROTESC de la un reel la altul, ca reel-urile să nu semene între ele; a încărcat câte un clip nou în plus pentru fiecare (B1, B2, cozy) ca alternative în bibliotecă. Clipuri noi (29 sept, confirmate): B1 = ba61dc06-bf41-4176-ba31-d5de0e6c38bb; B2 = e9a9ed00-094d-4211-8b98-2cfdf6115920 (9d119c02 a fost dublura lui B1, se ignoră); cozy = 12959b84-23a0-42ee-b00a-8970d51a59c7
[stated] REGULĂ HOOK-URI (29 sept, „de fiecare dată"): la fiecare reel din tabla HTML se pun 3 idei de hook, fiecare cu start frame-ul generat direct în tablă (hook-ul trebuie să iasă dintr-un singur start frame, animat după ce alege el) plus explicația ideii lângă; ideile trebuie să fie originale
[stated] 29 sept: nu pornește nimic până nu spune el explicit — deocamdată se lucrează la modul de lucru
[stated] REGULĂ HOOK-URI completată (29 sept): în hook NU se vede halatul; ideile trebuie să fie cele mai bune hook-uri posibile; se gândește acțiunea dinainte și se leagă de textul pe care îl pune el în CapCut — îi dau și idei de text pentru CapCut
[stated] REGULĂ PERMANENTĂ (29 sept): fiecare start frame și fiecare video trebuie să aibă lumină ultra-realistă și să arate foarte frumos — totul ultra-realist; eu aleg cum se formulează asta în prompturile Higgsfield
