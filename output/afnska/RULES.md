# afnska / Frost Femme - reguli (de la Szasz)
- 2026-11-12: videourile sunt COPII EXACTE ale reel-urilor lor (aceleasi miscari, unghiuri, timpi); schimbam doar fata si camera.
- 2026-11-12: fete blonde americane, frumoase, naturale; camere americane de Craciun, mai frumoase decat originalul, in stilul camerei lor.
- 2026-11-12: de acum fetele poarta PIJAMA DE CRACIUN DIN SATIN (sub haina).
- 2026-11-12: textul de pe ecran = textul lor (sau descrierea lor, tradusa, daca pe video nu au), cu fontul HeatGrump (montage.py), sa NU acopere fata.
- 2026-11-12: muzica de Craciun (heatgrump-studio/music/xmas), drop-ul pe momentul cheie.
- Video final: seedance_2_5 omni_reference, 1080p, 9:16, bitrate high, fara sunet generat.
- 2026-11-12: text reel 3: "DONT show this winter coat to your sister.. ❄️💙" (fontul HeatGrump, sub fata).
- 2026-11-12: text mic (size 62) si la mijlocul ecranului (y 0.46), fara sa acopere fata.
- Higgsfield: contul nou (user_3GmC...) - media urcate din nou: r3-mute 26c51ddf, ref_blue_front 9b336183, ref_blue_back 80432e82;
  camera 7b576141, fata (rochie) 2d116ee3, fata (pijama) 2bb7c78f. Video 1080p 13 s = 208 credite.
- 2026-11-12: prompturile de copiere descriu miscarile SECUNDA CU SECUNDA (vezi r3-1080/motion-breakdown.txt): taieturi, unghi, gesturi, numar de invartiri.
- 2026-11-12: calitatea/look-ul ca in original: dupa generare, corectie de culoare spre original (masurat cu signalstats: luminozitate, saturatie),
  plus corectie de nuanta pe albastruri (haina iese lila; selectivecolor blues/magentas). Filtrul folosit la r3 v2:
  selectivecolor=blues='0.15 -0.45 -0.05 0':magentas='0.2 -0.35 0 0':cyans='0 -0.1 0 0',eq=brightness=-0.07:contrast=1.08:saturation=0.7:gamma=0.97,colorbalance=rm=0.02:bm=-0.02,noise=alls=4:allf=t
- 2026-11-12: la FIECARE video punem si referintele de produs de pe site-ul Hourbelle (library/hourbelle/poze, fisa culorii potrivite + spate-corset).
- 2026-11-12: la FIECARE video livrat dam si CAPTION (EN), cu: Comment "COAT" ... link cu reducere speciala de Black Friday.
- 2026-11-12: la Genjutsu NU mai generam poza fata-in-camera; fata si camera se dau direct ca referinte separate. Nu generam nimic in plus fara sa fie cerut.
- 2026-11-12: la montaj din B-roll Genjutsu taiem DOAR in interiorul cadrelor; taieturile interne r3: 2.67, 3.54, 4.38, 5.29, 6.04, 7.5, 8.5, 11.17 s (verificat cu ffmpeg scene detect). Unboxing in hook = 1.5 s cu 'Vs..'. In parada: culorile, nu printese.

- 13 nov: hook5 "DONT show this to your mom" = start frame cu haina impaturata gros peste cap (fara detalii vizibile), numara 3-2-1, o lasa sa se desfaca natural in fata ei (fata nu se acopera), apoi B-roll Genjutsu cu aceeasi fata+camera.
- 13 nov: Frost Femme start frames FARA steag american. La hook-ul cu haina impaturata peste cap: mainile SUB rulou (il sustine de jos).
