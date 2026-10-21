#!/bin/bash
# Lot 21 oct: hook viral Genjutsu + B-roll snugglore, gata de postat (24 fps nativ → fluid 30 fps → text).
# $1=hook 1080 $2=broll 1080 $3=muzică $4=secunda „drop”-ului (pică pe începutul B-roll-ului) $5=nume ieșire (fără .mp4) $6=text
# $7 (opțional)=al doilea text, pe B-roll (ex. „Vs… 💚”); atunci $6 stă doar pe hook
set -e; cd /home/user/heatgrump; T=0.2
H=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $1); B=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $2)
BB=$(python3 -c "print($B-$T)"); D=$(python3 -c "print($H+$BB)"); MS=$(python3 -c "print(max(0,$4-$H))")
ffmpeg -v error -y -i $1 -i $2 -ss $MS -i $3 -filter_complex "[0:v]scale=1080:1920:flags=lanczos,setsar=1,fps=24,settb=1/24,setpts=N[a];[1:v]trim=start=$T,setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,setsar=1,fps=24,settb=1/24,setpts=N[b];[a][b]concat=n=2:v=1:a=0[v];[2:a]atrim=0:$D,asetpts=PTS-STARTPTS,volume=0.85,afade=t=out:st=$(python3 -c "print($D-0.8)"):d=0.8[m]" -map "[v]" -map "[m]" -r 24 -c:v libx264 -crf 17 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k -ar 48000 -t $D -movflags +faststart $5-GATA.mp4
ffmpeg -v error -y -i $5-GATA.mp4 -vf "minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1" -c:v libx264 -crf 17 -preset medium -pix_fmt yuv420p -c:a copy -movflags +faststart $5-FLUID.mp4
E=$(python3 -c "print(round($D-0.03,3))")
python3 -c "
import json,sys
json.dump({'out':'$5-FLUID-TEXT.mp4','fps':30,'segments':[{'file':'$5-FLUID.mp4','start':0,'end':$E,'audio':True}],'texts':([{'t0':0,'t1':$H,'text':sys.argv[1]},{'t0':$H,'t1':$E,'text':sys.argv[2]}] if sys.argv[2] else [{'t0':0,'t1':$E,'text':sys.argv[1]}])},open('$5-TEXT.json','w'),ensure_ascii=False)" "$6" "$7"
python3 engine/final.py $5-TEXT.json | tail -1
