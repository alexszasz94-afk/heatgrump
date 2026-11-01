# Sunetul hook-ului copiat — analiza în 3 părți (31 oct, Szasz)

Szasz, 31 oct: „ideea la audio e să fie analizat în trei părți diferite ca să facem prompt exact ca să iasă în Kling perfect”.

## Unealta
`python3 creator-kit/engine/audio3.py <hook-original.mp4> <sfârșitul hook-ului, s> <folder> "<replica din analiza Higgsfield>"`

Sunetul se desparte cu Demucs, iar fiecare strat se măsoară separat:
1. **VOCEA** (stratul de voce). Pentru fiecare cuvânt: secunda de START, lipită pe începutul real al vocii (Whisper greșește cu 0,1–0,5 s), sfârșitul, tăria (strigat / normal / încet), lungimea (cuvânt tărăgănat), înălțimea (voce de femeie sau de bărbat) și pauzele. START-ul e precis (±0,05 s). SFÂRȘITUL e aproximativ, mai ales în clipurile Kling.
2. **SUNETELE ACȚIUNILOR**:
   - mișcările mari din imagine (secundă cu secundă, cu un cadru la fiecare în `events.jpg`);
   - sunetele scurte din stratul fără voce și fără tobe.

   Fiecare mișcare primește în prompt sunetul ei, numit de mine după cadru (foșnet de pânză, bătaie în carton, pași).
3. **FUNDALUL**: pe bucăți de 0,5 s spune dacă e muzică (bas și tobe), zgomotul camerei sau liniște, și la ce nivel. Dacă originalul are muzică, la noi Kling face doar zgomotul camerei. Muzica o punem noi la montaj.

Analiza Higgsfield (`video_analysis`) rămâne OBLIGATORIE: ea decide CE se spune și CINE vorbește, iar `audio3` dă SECUNDELE și felul în care e spus.

## Blocul SOUND în promptul Kling (în locul vechiului „SOUND” dintr-o bucată)
```
SOUND - made by you, with the picture, in three layers.
VOICE (layer 1): <who, voice>, <tone>, lips in perfect sync. She says ONLY these words, each word starting exactly on its second: "<w1>" from <s> s to <e> s; "<w2>" from <s> s to <e> s; ... <how it is said: pauses, pace, which word is longer>. After "<last word>" nobody says anything else. No other words, no other voice, no narrator, no whisper.
ACTION SOUNDS (layer 2), exactly when they happen in the picture: at <s>-<e> s <sound> as <action>; ...
BACKGROUND (layer 3): from 0 s to the end only the quiet room tone of <OUR place> (<details>), continuous, never silent, never louder than the voice. ABSOLUTELY NO MUSIC: no song, no beat, no melody, no instruments, no jingle bells, no humming.
```

## Verificare după generare
Rulez `audio3.py` pe hook-ul nostru și compar START-ul fiecărui cuvânt cu originalul (toleranță ±0,1 s). Verific și că nu apare muzică și că nu sunt cuvinte în plus.

## Test 1 — countdown (Prințesă, reel DdGwGMEx-Uj), products/hook-audio3/countdown/
- Originalul (audio3): Three 0,24 · two 1,22 · one 2,12 · Let's 3,17 · see 3,33 · how 3,59 · it 3,74 · comes 3,80 · out 3,94. Sub numărătoare e muzică cu tobe (analiza veche nu o prinsese). Acțiuni: prinde pânza la 2,38, trage pânza la 2,67–2,77, împinge cutia spre cameră la 3,53–4,03. Tăietură la 4,07.
- Hook-ul vechi (30 oct, propoziția dintr-o bucată): Three 0,29 · two 1,26 · one 2,16 · Let's 3,56 (cu 0,39 s întârziere) … out 4,52.
- A = secundele exacte cuvânt cu cuvânt; B = aceleași, cu propoziția cerută cu 0,4 s mai devreme. Rezultatele sunt mai jos.
- Rezultate test 1 (1080p, ~40 credite), START-ul cuvintelor măsurat cu audio3:

| | original | vechi (30 oct) | A (exact) | B (−0,4 s) |
|---|---|---|---|---|
| Three | 0,24 | 0,29 | 0,32 | 0,28 |
| two | 1,22 | 1,26 | 1,27 | 1,27 |
| one | 2,12 | 2,16 | 2,10 | 2,25 |
| Let's | 3,17 | 3,56 | 3,39 | **3,12** |
| sfârșitul propoziției | ~4,0 | 4,84 | 4,83 | 4,60 |
| pânza trasă (imagine) | 2,75 | 2,75 | ~2,1 (devreme) | ~2,1 (devreme) |

  Muzică: niciuna, la ambele (doar zgomotul camerei). Cutia „Princess” se citește la ambele. Concluzie: numărătoarea iese la secundă cu secundele exacte; propoziția începe corect DOAR dacă e cerută cu 0,4 s mai devreme (B), dar Kling o spune mai rar (se termină cu ~0,6 s mai târziu). În ambele variante imaginea a tras pânza cu ~0,6 s mai devreme decât originalul (la hook-ul vechi era la secundă).
