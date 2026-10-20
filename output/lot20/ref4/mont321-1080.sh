#!/bin/bash
# 3-2-1 + B-roll ref4 la 1080p, 24 fps NATIV (fără conversie la 30 → fără cadre dublate / lag; Szasz 20 oct).
# $1=hook 1080 $2=broll 1080 $3=out. B-roll-ul se taie 0,2 s la început (cadre rătăcite). Vocea pe hook din h321-s3, apoi Bublé.
M=/home/user/heatgrump/library/music/xmas/buble-beginning.mp3; V=/home/user/heatgrump/output/lot19/480/h321-s3.mp4; T=${T:-0.2}   # tăietura de la începutul B-roll-ului (se poate da din afară, ex. T=0.85)
H=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $1); B=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $2)
BB=$(python3 -c "print($B-$T)"); D=$(python3 -c "print($H+$BB)"); ms=$(python3 -c "print(int($H*1000))")
ffmpeg -v error -y -i $1 -i $2 -i $V -ss 35.38 -i $M -filter_complex "[0:v]scale=1080:1920:flags=lanczos,setsar=1,fps=24,settb=1/24,setpts=N[a];[1:v]trim=start=$T,setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,setsar=1,fps=24,settb=1/24,setpts=N[b];[a][b]concat=n=2:v=1:a=0[v];[2:a]atrim=0:$H,asetpts=PTS-STARTPTS,afade=t=out:st=$(python3 -c "print($H-0.15)"):d=0.15[h];[3:a]atrim=0:$BB,asetpts=PTS-STARTPTS,volume=0.85,afade=t=out:st=$(python3 -c "print($BB-0.8)"):d=0.8,adelay=$ms|$ms[m];[h][m]amix=inputs=2:duration=longest:normalize=0[x]" -map "[v]" -map "[x]" -r 24 -c:v libx264 -crf 17 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k -ar 48000 -t $D -movflags +faststart $3
echo $3 $D
