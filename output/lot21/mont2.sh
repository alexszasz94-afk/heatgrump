#!/bin/bash
# Lot 21 v2: hook cu SUNETUL lui (luat din Seedance video_edit 480p) + B-roll + muzică + texte pe momente.
# $1=hook 1080 $2=sunet hook (mp4 Seedance) $3=broll 1080 $4=muzică $5=drop (s, pică pe începutul B-roll-ului) $6=ieșire (fără .mp4) $7=texte JSON [[t0,t1,"text"],...] cu „H” = durata hook-ului
set -e; cd /home/user/heatgrump; T=0.2
H=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $1); B=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $3)
BB=$(python3 -c "print($B-$T)"); D=$(python3 -c "print($H+$BB)"); MS=$(python3 -c "print(max(0,$5-$H))")
ffmpeg -nostdin -v error -y -i $1 -i $3 -ss $MS -i $4 -i $2 -filter_complex "[0:v]scale=1080:1920:flags=lanczos,setsar=1,fps=24,settb=1/24,setpts=N[a];[1:v]trim=start=$T,setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,setsar=1,fps=24,settb=1/24,setpts=N[b];[a][b]concat=n=2:v=1:a=0[v];[3:a]atrim=0:$H,asetpts=PTS-STARTPTS,volume=1.0,afade=t=out:st=$(python3 -c "print($H-0.25)"):d=0.25[h];[2:a]atrim=0:$D,asetpts=PTS-STARTPTS,volume='if(lt(t,$H),0.22,0.85)':eval=frame,afade=t=out:st=$(python3 -c "print($D-0.8)"):d=0.8[m];[h][m]amix=inputs=2:duration=longest:normalize=0[x]" -map "[v]" -map "[x]" -r 24 -c:v libx264 -crf 17 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k -ar 48000 -t $D -movflags +faststart $6-GATA.mp4
ffmpeg -nostdin -v error -y -i $6-GATA.mp4 -vf "minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1" -c:v libx264 -crf 17 -preset medium -pix_fmt yuv420p -c:a copy -movflags +faststart $6-FLUID.mp4
python3 - "$7" <<PY
import json,sys
H=$H; E=round($D-0.03,3)
segs=json.loads(sys.argv[1])
ev=lambda x: min(E, eval(str(x),{"H":H,"E":E}))
json.dump({'out':'$6-FLUID-TEXT.mp4','fps':30,'segments':[{'file':'$6-FLUID.mp4','start':0,'end':E,'audio':True}],
 'texts':[{'t0':ev(a),'t1':ev(b),'text':t} for a,b,t in segs]},open('$6-TEXT.json','w'),ensure_ascii=False)
PY
python3 engine/final.py $6-TEXT.json | tail -1
