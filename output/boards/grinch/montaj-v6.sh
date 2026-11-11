id=$1; O=/home/user/heatgrump/output/boards/grinch/fix; mkdir -p $O
U=https://d8j0ntlcm91z4.cloudfront.net/user_3LswZFi3bwZ0V3rYUwLSMwk6kIB/hf_20261110_
read _ fx b c < <(grep "^$id " $(dirname "$0")/fixkeys.txt)
cs=0.6; [ $id = G3-2 -o $id = G5-3 ] && cs=1.0
t2=3.10; [ $id = G2-1 -o $id = G5-1 ] && t2=3.04
H="[0:v]trim=0:1.125,setpts=PTS-STARTPTS"; [ $id = G5-3 ] && H="[0:v]trim=0:1.5,setpts=(PTS-STARTPTS)/1.3333"
N="scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1,format=yuv420p"
ffmpeg -nostdin -v error -y -i "$U$fx.mp4" -i "$U$b.mp4" -i /home/user/heatgrump/library/motion/conector-telecomanda-alb.mp4 -i "$U$c.mp4" -filter_complex "$H,$N[s1];[1:v]split[x][y];[x]trim=1.134:2.5,setpts=PTS-STARTPTS,$N[a1];[y]trim=$t2:4.97,setpts=PTS-STARTPTS,$N[a2];[2:v]trim=0:3.97,setpts=PTS-STARTPTS,$N[b];[3:v]trim=$cs:2.97,setpts=PTS-STARTPTS,$N[c];[s1][a1][a2][b][c]concat=n=5:v=1:a=0[v]" -map "[v]" -c:v libx264 -crf 27 -preset medium -movflags +faststart -an $O/$id.mp4
d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $O/$id.mp4); exp=$(python3 -c "print(round(1.125+(2.5-1.134)+(4.97-$t2)+3.97+2.97-$cs,2))")
python3 -c "import sys;sys.exit(0 if abs($d-$exp)<0.07 else 1)" && echo "OK $id $d" || { echo "BAD $id $d exp $exp"; exit 1; }
