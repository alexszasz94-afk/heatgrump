# Husa de volan încălzită cu prințese — reguli (de la Szasz)

- 2026-11-15: produs = husă de volan încălzită, pluș roz, 2 prințese în stil animație 3D (bruneta în rochie roz + blonda cu împletitură) pe partea de sus; restul: coroane, castele, stele. Szasz a ales designul v6/v7.
- 2026-11-15: FĂRĂ fir care atârnă (arată urât, volanul se rotește). Fără baterie inclusă: husa merge pe USB, cu BUZUNAR CU FERMOAR PE SPATELE volanului (partea dinspre bord), la ora 6, unde clientul pune un power bank.
- 2026-11-15: în FAȚĂ, la ora 6, doar BUTONUL rotund + 3 luminițe roz (3 trepte). În față nu se văd niciodată buzunarul, bateria sau firul.
- 2026-11-15: tot ce se generează în mașină trebuie să fie identic cu fișa produsului (aceeași husă, același buton, buzunarul doar pe spate). Se folosește mereu ca referință imaginea din fișă (job 7a48dd7f) sau cea de pe volan (job 0a1230e0).
- 2026-11-15: husa trebuie să fie subțire, cât un volan normal, la fel de groasă peste tot.
- 2026-11-15: FOLOSEȘTE ANALIZA MEREU: fiecare imagine/clip se verifică vizual (logica produsului + grosime + poziția butonului/buzunarului) înainte să fie trimis; ce pică se regenerează.
- Mărime: universal 15 in (37–38 cm), elastic; pick-up-uri mari = mărime L mai târziu.
- Higgsfield: gpt_image_2_6_flare, 2k, 9:16, quality high.
- 2026-11-15: NU ȘTERGE NIMIC fără permisiunea lui Szasz (fișiere, variante, detalii din imagini — inclusiv logo-uri). Întreabă întâi.
- 2026-11-15: reel 1 = mașina roz cu interior negru-roz (ref/ref-mustang-interior.jpg), stradă americană iarna (ref/ref-strada-iarna.jpg). Start frame-ul cu fata care intră în mașină NU e bun; vrea cadru din interior, din mers, cu mâinile ei pe volan.
- 2026-11-15: SETĂRI DE REALISM în toate prompturile (Szasz): poză reală de iPhone, NU render; fără blur, fără bokeh, fără depth-of-field, totul clar; texturi reale (piele, tricot, piele de volan, praf, zăpadă). Mersul mașinii se arată prin detalii (urme, ștergătoare, vitezometru), nu prin blur.
- 2026-11-15: reel 1 hook = start frame C (reel1/drum-C-pov-iphone.png, job af98d475), animat Seedance 480p (test): îi e frig, își freacă mâinile, suflă în ele, se vede aburul.
- 2026-11-15: parcarea pe strada din oraș (ref/ref-strada-oras.jpg) = dreptunghiurile de asfalt FĂRĂ zăpadă de lângă trotuarul din stânga (acolo au stat mașinile). Mașina roz stă într-un astfel de loc. Start frame ales: reel1/oras-J1-loc-parcare.png (job 4401201a).
- 2026-11-15: la animații NU mai pune ref/ref-mustang-interior.jpg ca referință pentru mâini: fata din poză are unghii roz APRINS și Seedance le copiază (la noi sunt roz pal). Fără tăieturi: 'one single continuous take' + 8 s merge (hook4).
- 2026-11-15: ARATĂ AI = problema. Pentru ORICE cadru se caută întâi poze REALE pe Pinterest (personaj, peisaj, unghi, mâini) și start frame-ul copiază poza reală (stil de telefon, lumină naturală, grain). Pozele: output/husa-volan/pinterest/<cadru>/ (index.json are linkul pin-ului). Alese pentru reel2: fata 1/09, mâini 2/08 + 2/06, pus husa 3/01, condus 4/09.
- 2026-11-15: CONSISTENȚĂ între imagini: același detaliu (ex. eticheta) trebuie să aibă aceeași poziție și mărime în toate cadrele; la fiecare imagine nouă se dă ca referință și prim-planul cu detaliul.
- 2026-11-15: MEREU cadre cu referință de la POZE REALE (Pinterest sau pozele lui Szasz) pentru compoziție/unghi; totul natural, UGC, fără mișcări nerealiste.
- 2026-11-15: CONSISTENȚĂ ÎN VIDEO (greșeli găsite la video2): aceeași mașină în TOATE cadrele (Mustang negru-roz, cu logo-ul lui), aceeași stradă/oraș în geamuri, aceeași oră (seara albastră), aceleași haine (pulover crem + pantaloni gri), aceleași unghii roz pal. Montajul husei se arată pas cu pas pornind de la volanul GOL. La condus: acul de viteză se mișcă (nu 0), mașina pe bandă, mai multe cadre de condus (POV, geam lateral, selfie la volan). Analizează singur tot videoul cadru cu cadru și repară fără să aștepți să ți se spună.
