#!/bin/bash
# Folosire: engine/qa_strip.sh <url> <fisier_local.mp4> <strip.jpg> [cadre]
# Descarcă rezultatul și face o bandă de cadre (cu timpul pe fiecare) pentru verificarea vizuală.
set -e
curl -s -o "$2" "$1"
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$2")
N=${4:-10}
FPS=$(python3 -c "print($N/$D)")
ffmpeg -y -loglevel error -i "$2" -vf "fps=$FPS,scale=216:-1,drawtext=text='%{pts\:flt}':x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black,tile=${N}x1" -frames:v 1 "$3"
echo "$2 $D s"
