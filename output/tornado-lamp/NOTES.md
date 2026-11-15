# Tornado vortex lamp — note (15 nov)
- Camera "problema": Pinterest (căutare "boys bedroom ideas real home"), poză originală în ref/camera-copil-pinterest.jpg, Higgsfield media e5d8f6e1-8e22-4241-93ac-48cd20d31a14.
- Start frame problemă: gpt_image_2_6_flare 2k 9:16, job 69ce1902-c280-4e69-adda-14fdd2c65860 → problem-start.png (băiat care nu poate dormi, noaptea, lumină de lună).
- Test video 480p 5 s: seedance_2_5 omni_reference, job 325a461c-6cb1-429d-a3a1-bc884d154814 → problem-480p.mp4 (nu e în git).
- QA: cameră fixă, camera identică, copilul se foiește; de îmbunătățit: cadru mai aproape de pat, lumină puțin mai deschisă.
- v2 (cadru aproape): cameră Pinterest ref/camera-copil-aproape-pinterest.jpg (pin img bf68b1ac…), media 82a02442-753e-4e33-bf14-9e5c85cf5961.
  Start frame ef1d3c06 → corectat (fără litere pe puzzle, ursuleț generic în loc de jucărie de brand) 3fe2bc58-4838-445c-9257-0b052819c23f = problem-start-v3.png.
  Video 480p 5 s: ec4e65b4-3177-4981-9fb5-ff85e61ac392 (problem-480p-v2.mp4, local). QA: cameră fixă, copilul se întoarce, trage pătura, se freacă la ochi; videoul iese mai întunecat decât cadrul.
- Lampa (temporar, până trimite Szasz pozele modelului exact): Pinterest, ref/lampa-pinterest-produs.jpg (media 78ff4614-a75d-486b-94b6-db22abcb4cef) + ref/lampa-pinterest-noptiera.jpg (0e1ce9d2-1e24-4a17-8d76-a6b8ff1acd7e).
- Soluție: start frame f565bedd-7c21-42a1-993f-2346c500c1af (mâna pune lampa lângă copil) = solution-start.png.
  v1 c8c25578 (lampa frumoasă, dar fața copilului tăiată), v2 9a9b0691 și v3 d543745b (copilul în cadru, dar tornada pare clepsidră de la distanță),
  MULTISHOT 67cde5d1-dcd3-487a-9997-f875f9b06fe1 (12 s, 4 cadre: mâna+buton cu zoom, close-up tornadă stânga→dreapta, fața care adoarme, cadru larg) = cel mai bun.
  Fizica reală: motor în bază, se rotește toată apa, pâlnia de aer coboară de sus în jos, sclipiciul se învârte în tot cilindrul.
- Unboxing POV de sus pe masă: f7f8fe6e-1ac5-4f5a-bd3e-b572cf3ede9a = unboxing-start.png (cutie neagră fără scris).
- 15 nov seara — LAMPA EXACTĂ a lui Szasz (poza AliExpress: ref/lampa-szasz-aliexpress.png; decupaje lampa-scena 61961736-d924-404a-98a1-40e00b1fe2f7, lampa-alb 84efcb16-4b50-4560-927a-4a1a013f3e7a, accesorii c434fa6a-ff4d-4c0c-b10c-5fe25a9ee55b).
  Cum funcționează: elice în bază învârte apa; pâlnie LARGĂ sus care se îngustează în jos; BILE MICI COLORATE (nu sclipici) + bule de aer; inel de lumină sub bază; în cutie: punga cu bile, instrucțiuni, cablu USB-C.
  Soluție start (lampa exactă, stinsă) 62e983b1-4f4f-4d12-9bcf-0aba7d5771f0; varianta LUMINOASĂ 84bb5cef-dd35-4c5f-b6f6-5441343dbdbf (cerută: camera era prea întunecată).
  Multishot întunecat a722d238 / LUMINOS a0662d8f-700f-422a-90c9-d71633b4e62c (cadrele 3-4 ies iar mai întunecate).
  Unboxing start 832b6632-39dc-4c45-834d-b88541e0abdf; UNBOXING + SETUP POV 12 s dbc159e2-1919-4356-93eb-2b0041f248b1 (scoate, toarnă apă, bile, capac, USB-C, buton → tornadă) — foarte bun.
- HERO lampă (unghi jos, la nivelul noptierei, copilul în spate): start 8b287428-24a0-48d2-81de-16c55e795897 (stinsă, deget pe buton), end 21f704cc-dbf3-460b-8778-2e4f72bcb8fe (pornită ca în poza produsului).
  METODA CARE MERGE pentru tornadă: seedance_2_5 cu start_image + end_image (cadrul final arată exact produsul) → 3af0b7f7-2a72-4642-83f7-5914b0c54e92 = hero-seedance.mp4 ⭐ (bilele urcă și se învârt prin pâlnie).
  Kling 3.0 cu aceleași cadre: 6015f276 (pâlnie ok, dar bilele dispar).
- HERO v2 PERFECT: end frame refăcut din start (9cde4f65-cead-47a4-9311-5aa544a0e6c3 = hero-end-v2.png) + prompt pe secunde (prompts/hero-lamp-video.txt) → 7d344937-b1cf-40ee-8444-e250a1217fc3 = hero-v2.mp4: copilul stă pe loc, bilele urcă și se învârt prin tornadă.
