#!/usr/bin/env bash
# Setup script pentru Claude Code pe web (claude.ai/code) — se lipește în câmpul „Setup script” al mediului cloud.
# Rulează ca root pe Ubuntu, înainte să pornească Claude. Instalează ce lipsește; se păstrează în cache între sesiuni.
set -e
apt-get update -qq && apt-get install -y -qq ffmpeg >/dev/null
pip install -q --break-system-packages yt-dlp pyyaml || pip install -q yt-dlp pyyaml
mkdir -p state output/videos output/plans library/clips library/analysis inbox
echo "setup-cloud: ok (ffmpeg $(ffmpeg -version | head -1 | cut -d' ' -f3), yt-dlp $(yt-dlp --version))"
