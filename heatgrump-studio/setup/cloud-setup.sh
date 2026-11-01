#!/usr/bin/env bash
# Setup script for Claude Code on the web (claude.ai/code). Paste this whole file into the cloud environment's "Setup script" box.
set -e
apt-get update -qq && apt-get install -y -qq ffmpeg >/dev/null
pip install -q --break-system-packages yt-dlp pillow numpy faster-whisper librosa demucs || pip install -q yt-dlp pillow numpy faster-whisper librosa demucs
echo "cloud setup ok: ffmpeg $(ffmpeg -version | head -1 | cut -d' ' -f3), yt-dlp $(yt-dlp --version)"
