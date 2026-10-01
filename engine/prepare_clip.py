"""Pregătește un clip pentru analiză (Claude Code se uită apoi la cadre și scrie hook-ul în bibliotecă).
Rulare: python3 engine/prepare_clip.py <fisier.mp4 | link>
Output: library/analysis/<nume>/  → frames (10 cadre + primele 3 secunde cadru cu cadru), audio.wav, transcript.txt (dacă e instalat faster-whisper), info.json
"""
import sys, subprocess, json, shutil
from common import *

def run(cmd): return subprocess.run(cmd, capture_output=True, text=True)

def main(src):
    src = str(src)
    if src.startswith("http"):
        out = LIB / "clips" / (src.rstrip("/").split("/")[-1].split("?")[0] or "clip") ; out = out.with_suffix(".mp4")
        r = run(["yt-dlp", "-q", "-o", str(out), "-f", "mp4/best", src])
        if r.returncode != 0:
            log("yt-dlp nu a putut descărca. Descarcă tu clipul și pune-l în inbox/, apoi rulează din nou cu fișierul."); sys.exit(1)
        src = str(out)
    src = pathlib.Path(src); d = LIB / "analysis" / src.stem; d.mkdir(parents=True, exist_ok=True)
    probe = json.loads(run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=width,height,r_frame_rate", "-of", "json", str(src)]).stdout)
    dur = float(probe["format"]["duration"])
    # 10 cadre uniform + primele 3 secunde la 2 fps (hook-ul)
    run(["ffmpeg", "-y", "-v", "error", "-i", str(src), "-vf", f"fps=10/{dur},scale=540:-1", str(d / "frame_%02d.jpg")])
    run(["ffmpeg", "-y", "-v", "error", "-t", "3", "-i", str(src), "-vf", "fps=2,scale=540:-1", str(d / "hook_%02d.jpg")])
    run(["ffmpeg", "-y", "-v", "error", "-i", str(src), "-vf", f"fps=12/{dur},scale=270:-1,tile=4x3", str(d / "sheet.jpg")])
    run(["ffmpeg", "-y", "-v", "error", "-i", str(src), "-vn", "-ac", "1", "-ar", "16000", str(d / "audio.wav")])
    transcript = ""
    try:
        from faster_whisper import WhisperModel
        segs, _ = WhisperModel("base").transcribe(str(d / "audio.wav"))
        transcript = "\n".join(f"[{s.start:.1f}-{s.end:.1f}] {s.text.strip()}" for s in segs)
    except Exception:
        transcript = "(faster-whisper neinstalat: pip3 install faster-whisper)"
    (d / "transcript.txt").write_text(transcript)
    jsave(d / "info.json", {"source": str(src), "duration": round(dur, 2), "streams": probe.get("streams"), "prepared": today()})
    log(f"Gata: {d}. Cadre: {len(list(d.glob('frame_*.jpg')))} + hook {len(list(d.glob('hook_*.jpg')))}, durata {dur:.1f}s")
    log("Următorul pas (Claude Code): uită-te la sheet.jpg, hook_*.jpg și transcript.txt și scrie intrarea în library/hooks-library.json (skill analyze-clip).")

if __name__ == "__main__":
    main(sys.argv[1])
