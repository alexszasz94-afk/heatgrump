#!/bin/sh
# Bublé drop (35.38 s) lands 1.2 s into the B-roll (she has the robe on): music starts at the hook end (4.0 s) from 34.18 s.
cd /home/user/heatgrump && python3 engine/final.py output/reel24-store/final.json && D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 output/reel24-store/nomusic.mp4) &&
ffmpeg -loglevel error -y -i output/reel24-store/nomusic.mp4 -ss 34.18 -i library/music/xmas/buble-beginning.mp3 -filter_complex "[1:a]atrim=0:$D,asetpts=PTS-STARTPTS,volume=0.85,afade=t=in:st=0:d=0.3,adelay=4000|4000,afade=t=out:st=$(python3 -c "print($D-0.6)"):d=0.6[m];[0:a][m]amix=inputs=2:duration=first:normalize=0[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k output/reel24-store/reel24-store-FINAL.mp4 && rm output/reel24-store/nomusic.mp4 && echo HG-DONE
