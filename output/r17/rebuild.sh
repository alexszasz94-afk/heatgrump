set -e
cd /home/user/heatgrump/output/r17
U=https://d8j0ntlcm91z4.cloudfront.net/user_3LswZFi3bwZ0V3rYUwLSMwk6kIB/hf_20261112_
get(){ [ -f h/$1.mp4 ] || curl -s -o h/$1.mp4 "$U$2.mp4"; }
trim(){ ffmpeg -v error -y -ss $2 -i h/$1.mp4 -an -vf "tpad=start_duration=$2:start_mode=clone" -c:v libx264 -crf 14 -pix_fmt yuv420p h/$1t.mp4 && rm h/$1.mp4; }
[ -f h/s02t.mp4 ] || { get s02 073423_ef59fdcc-c132-4709-90ac-501fa73805a2; trim s02 0.17; }
[ -f h/s03t.mp4 ] || { get s03 074242_a09887a2-744f-4ab3-90ba-420662f2d977; trim s03 0.09; }
[ -f h/s05t.mp4 ] || { get s05 073422_ba734648-f846-4e93-8f9a-3aaf218c267e; trim s05 0.17; }
get s04 073422_d7e0b787-812f-4980-a706-fd266b6aef02
get s08 073422_5ad5380c-ae18-48d8-b4c2-5109b471c9c1
export REMOTE=/home/user/heatgrump/output/r17/remote-green-fixed.mp4 RS=0 RE=3.7
for p in "S00 g00 00" "S01 g01 01" "S02 s02t 02" "S03 s03t 03" "S04 s04 04" "S05 s05t 05" "S06 g06 06" "S07 g07 07" "S08 s08 08"; do
  set -- $p
  echo "== $1"
  ls broll/grinch-$3.mp4 >/dev/null 2>&1 || echo "NEED broll $3"
  [ -f broll/grinch-$3.mp4 ] && python3 mk.py $1 h/$2.mp4 broll/grinch-$3.mp4 4.0 full 2>&1 | grep -v "^cuts at" | tail -2 && rm broll/grinch-$3.mp4
done
