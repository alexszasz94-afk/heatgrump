#!/bin/bash
# 3-2-1 + B-roll ref4: $1=hook.mp4 $2=broll.mp4 $3=out.mp4 (480p). Vocea pe hook din h321-s3 (regula 20 oct), apoi Bublé cu drop-ul la B-roll.
M=/home/user/heatgrump/library/music/xmas/buble-beginning.mp3; V=/home/user/heatgrump/output/lot19/480/h321-s3.mp4
H=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $1); B=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $2)
D=$(python3 -c "print($H+$B)"); ms=$(python3 -c "print(int($H*1000))")
ffmpeg -v error -y -i $1 -i $2 -i $V -ss 35.38 -i $M -filter_complex "[0:v]scale=480:854,fps=30,setsar=1[a];[1:v]scale=480:854,fps=30,setsar=1[b];[a][b]concat=n=2:v=1:a=0[v];[2:a]atrim=0:$H,asetpts=PTS-STARTPTS,afade=t=out:st=$(python3 -c "print($H-0.15)"):d=0.15[h];[3:a]atrim=0:$B,asetpts=PTS-STARTPTS,volume=0.85,afade=t=out:st=$(python3 -c "print($B-0.8)"):d=0.8,adelay=$ms|$ms[m];[h][m]amix=inputs=2:duration=longest:normalize=0[x]" -map "[v]" -map "[x]" -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a aac -b:a 160k -ar 48000 -t $D -movflags +faststart $3
echo $3 $D
