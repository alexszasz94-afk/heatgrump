#!/bin/bash
# dl18.sh <url> <out.mp4>  — descarcă cu reîncercări și verifică că mp4-ul e întreg
for i in 1 2 3 4; do curl -sS --retry 3 -o "$2" "$1" && ffprobe -v error -show_entries format=duration -of csv=p=0 "$2" >/dev/null 2>&1 && ffmpeg -v error -i "$2" -f null - 2>&1 | grep -q . || { echo "ok $2 $(ffprobe -v error -show_entries format=duration -of csv=p=0 $2)"; exit 0; }; sleep 2; done; echo "FAIL $2"
