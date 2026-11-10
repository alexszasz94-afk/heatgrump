# gm.sh <id> <bkey> <ckey> <cozy_start>
S=/tmp/claude-0/-home-user-heatgrump/ba0e85e6-8912-5a4f-80da-7fb8f525bf03/scratchpad/gb
U=https://d8j0ntlcm91z4.cloudfront.net/user_3LswZFi3bwZ0V3rYUwLSMwk6kIB/hf_20261110_
N="scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1,format=yuv420p"
T=/tmp/pp/tmp_$1; mkdir -p $T
curl -s --retry 3 -o $T/b.mp4 "$U$2.mp4"; curl -s --retry 3 -o $T/c.mp4 "$U$3.mp4"
ffmpeg -nostdin -v error -y -i $T/b.mp4 -i /home/user/heatgrump/library/motion/conector-telecomanda-alb.mp4 -i $T/c.mp4 -filter_complex "[0:v]trim=0:4.97,setpts=PTS-STARTPTS,$N[a];[1:v]trim=0:3.97,setpts=PTS-STARTPTS,$N[b];[2:v]trim=$4:2.97,setpts=PTS-STARTPTS,$N[c];[a][b][c]concat=n=3:v=1:a=0[v]" -map "[v]" -c:v libx264 -crf 27 -preset medium -movflags +faststart -an $S/v/$1.mp4
ffmpeg -nostdin -v error -y -ss 2.0 -i $S/v/$1.mp4 -frames:v 1 -vf scale=360:-2 -q:v 5 $S/t/$1.jpg
rm -rf $T
echo "$1 $(ffprobe -v error -show_entries format=duration -of csv=p=0 $S/v/$1.mp4) $(du -k $S/v/$1.mp4|cut -f1)K"
