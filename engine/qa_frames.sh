#!/bin/bash
# Descarcă un rezultat Higgsfield și face o bandă de 4 cadre pentru verificare vizuală.
# Folosire: engine/qa_frames.sh <url> <fișier_local.mp4> <bandă.jpg>
set -e
curl -s -o "$2" "$1"
d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$2")
ffmpeg -y -loglevel error -i "$2" -vf "fps=4/$d,scale=300:-1,tile=4x1" -frames:v 1 "$3"
ffprobe -v error -select_streams v -show_entries stream=width,height -of csv=p=0 "$2"
