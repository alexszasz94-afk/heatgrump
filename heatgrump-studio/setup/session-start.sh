#!/usr/bin/env bash
# Runs by itself at the start of every Claude Code session (see .claude/settings.json).
# On claude.ai/code it installs the tools the kit needs, so the creator never has to paste a setup script.
[ "$CLAUDE_CODE_REMOTE" = "true" ] || exit 0
command -v ffmpeg >/dev/null 2>&1 || { (apt-get update -qq && apt-get install -y -qq ffmpeg) >/dev/null 2>&1 || true; }
python3 -c "import yt_dlp, PIL, numpy, faster_whisper, librosa" >/dev/null 2>&1 || \
  pip install -q --break-system-packages yt-dlp pillow numpy faster-whisper librosa >/dev/null 2>&1 || \
  pip install -q yt-dlp pillow numpy faster-whisper librosa >/dev/null 2>&1 || true
python3 -c "import demucs" >/dev/null 2>&1 || \
  pip install -q --break-system-packages demucs >/dev/null 2>&1 || pip install -q demucs >/dev/null 2>&1 || true   # sound layers for audio3.py (rule 31 Oct)
echo "Robe Studio tools: ffmpeg $(command -v ffmpeg >/dev/null && echo ok || echo MISSING), yt-dlp $(command -v yt-dlp >/dev/null && echo ok || echo MISSING)"
exit 0
