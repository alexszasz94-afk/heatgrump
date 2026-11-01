# Rețetă: hook copiat cu Kling 4.0 video-edit (singura generare per video)
Stare: DE TESTAT pe Grinch (metoda vine din kitul Snoopy/Princess, unde a mers; varianta exactă din limitless `recipes/hook-audio-3parts.md` trebuie sincronizată când repo-ul e accesibil).

## Pregătire (gratuit, local)
1. `yt-dlp -o inbox/hook-<cod>.mp4 <link>`
2. Cadre fps 10 pe primele 6 s → tăietura exactă unde se termină hook-ul (înainte să apară halatul / produsul competitorului).
3. Taie 3-4 s: `ffmpeg -ss <t0> -t <d> -i in.mp4 -an -vf "scale=720:1280" hook-src.mp4` (FĂRĂ sunet; textul ars → `delogo` pe zona textului).
4. Upload: `media_upload` → PUT → `media_confirm`.

## Generare
```
model: kling4_0, mode: video-edit, resolution: 720p, aspect_ratio: 9:16
medias: video_references = hook-src ; image_references = personajul setului, camera setului
declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612
```
Prompt (se schimbă doar `<...>`):
```
REPRODUCE THE ACTION OF THE SOURCE VIDEO ONE TO ONE — same timing, same gestures, same camera position.
CHANGE ONLY: 1) the person becomes Image 1 (same face, hair, age, gender, skin) wearing <OUTFIT>, plain clothes with no logo and no brand;
2) the place becomes the room in Image 2 (American home), with a small American flag visible but natural (<WHERE: on the wall / porch / pillow / mug>).
NO ROBE, NO PRODUCT in frame. NO TEXT anywhere — remove any captions from the source.
LIGHT: very soft natural daylight, bright, vivid semi-warm colours, no gold/orange grade, phone UGC look, no zoom.
SOUND — three layers, generated with this video: 1) room tone of <ROOM>; 2) the diegetic sounds of the action (<SOUNDS>); 3) <VOICE LINE or "no voice">. No music.
```
## QA
Fața = Image 1 · camera = Image 2 · steag vizibil · fără halat · fără text · acțiunea se leagă de text. Pică → încă o încercare (max 3).
## Cost
4 s × 2,25 = 9 credite (720p). La 1080p 13 credite.
