# Inventar zilnic (5 videouri/zi) — hook-uri × B-roll-uri

Montaj: `python3 output/day/mkday.py <nume> <hook.mp4> <sfârșit hook> <broll.mp4> '<text>' [0=text doar pe B-roll când hook-ul are textul ars]`
Ordine: hook → spate → săculeți (până se închide) → conector alb → telecomanda din B-roll → cozy. Mariah cu refrenul pe tăietură, sunetul hook-ului oprit.
Hook COPIAT (din reel) → sunetul ORIGINAL al reel-ului pe tot videoul: `MUSIC=<music-ref-pad.m4a> python3 output/day/mkday.py ...`. Hook propriu → Mariah cu refrenul pe tăietură.
Board: Postări Grinch 2 (https://claude.ai/artifact/AgQChUwSfeJEu7C63uPbNW) — cel vechi (GQBWVctvWyWWDxunr37Wd2) e plin (256 MB) dar ține sursele hook-urilor g11. Model: `board19.py`. Max 64 MB per publicare.

## Hook-uri fără față (merg cu orice B-roll)
| hook | sursă | sfârșit | text |
|---|---|---|---|
| POV rulou pe podea (buline) | board vechi v/g11-G1-2.mp4 (text ars) | 4.6 | DO NOT show this to a / mom😱😳... (pad_g2) |
| POV rulou pe podea (carouri) | board vechi v/g11-G3-2.mp4 (text ars) | 4.6 | Christmas-holics this / is for YOU..🎄🎅 (pad_g2) |
| Rulou în folie | board vechi v/g11-G2-1.mp4 (text ars) | 3.97 | DO NOT show this to a / Christmas LOVER😱😳 (pad_g3) |
| Rulou în folie, mâneci verzi | board vechi v/g11-G3-3.mp4 | 3.97 | Imagine this on the / first snow day.. 😌☃️ (pad_g3) |
| Punga HEAT GRUMP | board vechi v/g11-G2-3.mp4 | 5.0 | Grinch girlies, pls / don't hate... 🥺💚 (pad_up) |
| POV zăpadă | output/snow/hook.mp4 | 6.0 | Best Christmas gift 2026? 💚🎄 (Mariah) |

## Hook-uri cu fața fetei (doar cu B-roll-ul ei)
| hook | fata | sfârșit | text |
|---|---|---|---|
| Piñata cu familia | 13 (grinch-00), output/pinata/hook1.mp4 | 5.8 | Is this the best Christmas / gift ever?? 🎁😍 (Mariah) |
| Rulou desfăcut (DcrmIaft5m-) | 13,1,2,3,4,5,6,7,8 → output/r17/h | 4.0 | DONT show this to / your mom... 😳❄️ |

## B-roll-uri (artifact „Clipuri Grinch Seedance” AmBqmsUzQkszJBqdAhxuD2): grinch-00..08
Bune: 00, 03 (brunetă), 06, 07, 08 (blonde). Cu probleme: 01 (pulover), 02 (cap ieșit/cozy altă cameră), 04 (altă cameră), 05 (cozy altă cameră).
Hook vechi cu față → B-roll cu fată de aceeași culoare a părului (brunetă → 03, blondă → 00/06/07/08).

## Folosite
- 12 nov: rulou × 00–08 (9 videouri)
- 15 nov: piñata×00, zăpadă×00, POV-buline×03, POV-carouri×07, folie×08
- 18 nov: folie-verde×06, punga HEAT GRUMP×03, POV-buline×08, POV-carouri×00, zăpadă×07
- 19 nov (hook-uri vechi): grinchmom×03 (ref), storemug×07 (Mariah), unbox×06 (Mariah), tray123×08 (Mariah), nogift×00 (ref)

## Hook-uri VECHI (2–8 nov), curate (fără text), la 1080p, în git: `git show HEAD:<sursă> > fișier`
Un exemplu pe tip (fiecare tip are variante pe set26–set37: `git ls-files output/videos/<tip>/`). Muzica: `<tip>/ref/music-ref-pad.m4a` = sunetul reel-ului copiat; altfel piesa noastră (Mariah cu drop).
| tip | hook | sfârșit | muzică | text | față |
|---|---|---|---|---|---|
| costco | output/videos/costco/fin-30.mp4 | 1.66 | Wham | Christmas mums.. dont walk RUN to Costco 😱🏃‍♀️ | ? |
| fbhook | output/videos/fbhook/raw-set28.mp4 | 7.7 | fbhook/ref | "Babe you don't / need that..." 🙄 | da |
| grinchmom | output/videos/grinchmom/hook-set26.mp4 | 3.97 | grinchmom/ref | Do NOT let a Grinch / mom see this... 🤩🎄 | brunetă |
| hmstore | output/videos/hmstore/raw-set26.mp4 | 4.45 | let-it-go (NU la Grinch) | H&M X GRINCH / 🤩🎄 | ? |
| mallcoffee | output/videos/mallcoffee/raw-set29.mp4 | 4.28 | Mariah | Christmas lovers, this is / for you! 🥰🎄 | blondă |
| mallrun | output/videos/mallrun/hook-set27-orig.mp4 | 6.25 | mallrun/ref | DONT Show this to a / GRINCH LOVER...💚🎄 | ? |
| mallwindow | output/videos/mallwindow/hook-set26-orig.mp4 | 3.75 | mallwindow/ref | DONT Show this to a / GRINCH LOVER...🎄💚 | brunetă |
| nogift | output/videos/nogift/hook-set26-orig.mp4 | 2.46 | nogift/ref | 👱: "No gift is perfect" / Me: 😏 | nu |
| reveal | output/videos/reveal/v3-32.mp4 | 4.07 | Mariah | DO NOT show this to a Christmas-aholic😱🤫... | blondă |
| rollcake | output/videos/rollcake/raw2-set27.mp4 | 5.0 | rollcake/ref | Christmas aholics this / one's for you.. 😭❄️🎅 | brunetă |
| rollup | output/videos/rollup/hook-set34b.mp4 | 3.57 | rollup/ref | DONT send this to an aunt... ❄️😏 | blondă (spate) |
| storemug | output/hooks/store-mug/hook6-b-trim.mp4 | 4.21 | Mariah | Moms DONT walk.. 🏃‍♀️ / RUN to target 🎯🎄 | blondă |
| tray123 | output/videos/tray123/hook-set32-cut.mp4 | 2.85 | Mariah | DONT Show this to a / GRINCH LOVER...🎄💚 | blondă |
| twofriends | output/videos/twofriends/hook-set26-orig.mp4 | 4.67 | twofriends/ref | DO NOT Show this to a / GRINCH LOVER...💚🎄 | 2 fete |
| unbox | output/videos/unbox/fin-26.mp4 | 7.96 | Mariah | The best purchase I've / EVER made...😍💖 | nu (POV) |
| unroll | output/videos/unroll/pk-set32.mp4 | 4.0 | unroll/ref | DONT show this to / your mom...😳❄️ | ? |
| zara | output/videos/zara/v4-28.mp4 | 4.2 | Mariah | GRINCH X ZARA 🤭 | magazin |
| dorm | output/videos/r8nov/hooks/hook-set50.mp4 (set50–59) | 3.97 | r7nov/ref | Do NOT let a Grinch mom see this...🤩🎄 | ? |
| v01–v10 | output/videos/vNN/hook-*.mp4 | 4–7.6 | Mariah/Wham/Bublé | vezi edit.json | ? |
