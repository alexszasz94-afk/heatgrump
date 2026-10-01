#!/bin/bash
# Instalare într-un singur pas (Mac / Linux). Rulează:  bash setup.sh
set -e
echo "== HeatGrump Engine — instalare =="
if ! command -v brew >/dev/null 2>&1 && [[ "$OSTYPE" == darwin* ]]; then
  echo "Instalez Homebrew (o singură dată)..."; /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi
if ! command -v node >/dev/null 2>&1; then echo "Instalez Node..."; brew install node 2>/dev/null || sudo apt-get install -y nodejs npm; fi
if ! command -v claude >/dev/null 2>&1; then echo "Instalez Claude Code..."; npm install -g @anthropic-ai/claude-code; fi
if ! command -v ffmpeg >/dev/null 2>&1; then echo "Instalez ffmpeg..."; brew install ffmpeg 2>/dev/null || sudo apt-get install -y ffmpeg; fi
if ! command -v yt-dlp >/dev/null 2>&1; then echo "Instalez yt-dlp..."; brew install yt-dlp 2>/dev/null || pip3 install -U yt-dlp; fi
pip3 install -q pyyaml 2>/dev/null || true
echo
echo "Gata. Acum scrie:   claude"
echo "Prima dată Claude o să te întrebe dacă aprobi serverul MCP 'higgsfield' din acest folder → zi da,"
echo "apoi scrie /mcp și apasă Enter pe 'higgsfield' ca să te loghezi în contul Higgsfield (se deschide browserul)."
echo "După login scrie:   start"
