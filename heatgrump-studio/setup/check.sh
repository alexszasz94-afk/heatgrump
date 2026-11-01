#!/bin/bash
# Checks everything the kit needs. Prints OK / MISSING for each item.
ok(){ echo "OK       $1"; }; miss(){ echo "MISSING  $1"; M=1; }
PY=python3; command -v python3 >/dev/null || PY=py
command -v ffmpeg  >/dev/null && ok ffmpeg  || miss "ffmpeg"
command -v ffprobe >/dev/null && ok ffprobe || miss "ffprobe (comes with ffmpeg)"
command -v yt-dlp  >/dev/null && ok yt-dlp  || miss "yt-dlp"
command -v curl    >/dev/null && ok curl    || miss "curl"
command -v $PY     >/dev/null && ok "$PY"   || miss "python3"
$PY -c "import PIL" 2>/dev/null && ok "python pillow" || miss "python pillow (pip install pillow)"
$PY -c "import numpy" 2>/dev/null && ok "python numpy" || miss "python numpy (pip install numpy)"
$PY -c "import faster_whisper" 2>/dev/null && ok "python faster-whisper (hook words, audio3)" || miss "python faster-whisper (pip install faster-whisper)"
# rule 31 Oct (Alex): really run a 1-second transcription (audio as a numpy array, never a file path - the file path crashes with some PyAV versions); first run downloads the speech model
$PY -c "import numpy as n;from faster_whisper import WhisperModel as W;s,_=W('small.en',device='cpu',compute_type='int8').transcribe(n.zeros(16000,dtype=n.float32),language='en');list(s)" >/dev/null 2>&1 && ok "speech model runs (1 s test)" || miss "speech model test failed (needs huggingface.co reachable; pip install -U faster-whisper)"
$PY -c "import demucs" 2>/dev/null && ok "python demucs (hook sound layers, audio3)" || miss "python demucs (pip install demucs)"
$PY -c "import librosa" 2>/dev/null && ok "python librosa (hook sound analysis, audio3)" || miss "python librosa (pip install librosa)"
cd "$(dirname "$0")/.."
for f in motion/grinch-v4.mp4 motion/grinch-v5.mp4 products/grinch/refs/front.jpg engine/fonts/TikTokSans-w700-semicond.ttf; do [ -f "$f" ] && ok "$f" || miss "$f (the zip was not fully extracted)"; done
[ -z "$M" ] && echo "ALL GOOD" || echo "SOMETHING IS MISSING"
