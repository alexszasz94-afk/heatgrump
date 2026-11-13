#!/bin/bash
# descarca un clip generat, corectie usoara de culoare, fara sunet: getclip.sh <iesire.mp4> <url>
set -e
curl -sS -o "${1%.mp4}-raw.mp4" "$2"
ffmpeg -v error -y -i "${1%.mp4}-raw.mp4" -vf "format=yuv420p,eq=brightness=-0.03:contrast=1.03:saturation=0.85,noise=alls=3:allf=t" -an -c:v libx264 -crf 16 "$1"
echo "ok $1"
