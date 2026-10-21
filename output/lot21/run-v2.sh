#!/bin/bash
# Lot 21 v2: aceleași 9 videouri, cu sunet pe hook și texte pe momentele montajului
# (hook → își pune halatul → conector+telecomandă „HEATED” → cadrul cozy).
cd /home/user/heatgrump/output/lot21; X=library/music/xmas; M=$X/mariah-all-i-want.mp3; U=$X/buble-beginning.mp3; O=output/lot21/v2; K=output/lot21/hooks; R=output/lot21/broll
mkdir -p v2
A='"H+3.05"'; C='"H+6.05"'
v(){ ./mont2.sh $K/$1 $K/snd-$2.mp4 $R/$3 $4 $5 $O/$6 "$7"; }
v hook-n-1080.mp4 n1 broll-n-1080.mp4 $M 53.48 video1-N "[[0,$A,\"POV: the robe every Grinch mom wants 🎄😱\"],[$A,$C,\"Wait… it's HEATED 🔌🔥\"],[$C,\"E\",\"Never taking it off 😌💚\"]]"
v hook-i-1080.mp4 i2 broll-i-1080.mp4 $M 53.48 video2-I "[[0,$A,\"When the Grinch robe finally arrives 🥳🎄\"],[$A,$C,\"Plug it in… it's HEATED 🔌🔥\"],[$C,\"E\",\"Cozy level: 100 😌💚\"]]"
v hook-h-1080.mp4 h3 broll-h-1080.mp4 $U 35.38 video3-H "[[0,$A,\"Cold-aholics, this one's for you 🥶🎄\"],[$A,$C,\"It's HEATED 🔌🔥\"],[$C,\"E\",\"Bye bye cold 😌💚\"]]"
v hook-l-1080.mp4 l4 broll-l-1080.mp4 $U 35.38 video4-L "[[0,$A,\"Found the perfect winter robe 🥶🎄\"],[$A,$C,\"And it's HEATED 🔌🔥\"],[$C,\"E\",\"Never taking it off 😌💚\"]]"
v hook2-n-store-1080.mp4 n6 broll-n-1080.mp4 $U 35.38 video6-N-store "[[0,$A,\"Me spotting the Grinch robes in store 😱🎄\"],[$A,$C,\"Got it home… it's HEATED 🔌🔥\"],[$C,\"E\",\"Best buy this winter 💚\"]]"
v hook2-i-plane-1080.mp4 i7 broll-i-1080.mp4 $M 53.48 video7-I-plane "[[0,$A,\"My travel must-have this winter ✈️🎄\"],[$A,$C,\"At home it plugs in 🔌🔥\"],[$C,\"E\",\"Cozy everywhere 😌💚\"]]"
v hook2-h-stairs-1080.mp4 h8 broll-h-1080.mp4 $M 53.48 video8-H-stairs "[[0,\"H\",\"Winter in 2025 🥶😒\"],[\"H\",$A,\"Vs… 💚\"],[$A,$C,\"It's HEATED 🔌🔥\"],[$C,\"E\",\"Never going back 😌💚\"]]"
v hook2-l-concept-1080.mp4 l9 broll-l-1080.mp4 $U 35.38 video9-L-concept "[[0,3.125,\"The concept 🤢\"],[3.125,$A,\"Vs… 💚\"],[$A,$C,\"It's HEATED 🔌🔥\"],[$C,\"E\",\"Never going back 😌💚\"]]"
v hook2-j-cake-1080.mp4 j10 broll-j-1080.mp4 $M 53.48 video10-J-cake "[[0,$A,\"When your bestie serves you THIS 😂🎄\"],[$A,$C,\"It's a HEATED robe 🔌🔥\"],[$C,\"E\",\"Best gift ever 💚\"]]"
