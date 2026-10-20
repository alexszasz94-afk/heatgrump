#!/bin/bash
# Mișcare fluidă fără regenerare (Szasz 20 oct, „au un pic de lag”): interpolare de cadre 24→30 fps pe varianta fără text,
# apoi textul se pune din nou cu final.py (fps 30). $1 = litera setului (a b d e f g).
k=$1; cd /home/user/heatgrump/output/lot20/ref4
ffmpeg -v error -y -i 321-ref4-$k-GATA-1080.mp4 -vf "minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1" -c:v libx264 -crf 17 -preset medium -pix_fmt yuv420p -c:a copy -movflags +faststart 321-ref4-$k-FLUID-1080.mp4
python3 - $k <<'P'
import json,sys
k=sys.argv[1]; j=json.load(open(f'321-ref4-{k}-TEXT.json')); j['fps']=30
j['out']=f'output/lot20/ref4/321-ref4-{k}-FLUID-TEXT.mp4'; j['segments'][0]['file']=f'output/lot20/ref4/321-ref4-{k}-FLUID-1080.mp4'
json.dump(j,open(f'321-ref4-{k}-FLUID.json','w'),ensure_ascii=False)
P
cd /home/user/heatgrump && python3 engine/final.py output/lot20/ref4/321-ref4-$k-FLUID.json | tail -1
