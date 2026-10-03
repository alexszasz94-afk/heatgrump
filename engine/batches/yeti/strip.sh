# strip.sh <video> <out.jpg> [fps]  -> bandă de cadre pentru QA
ffmpeg -loglevel error -y -i "$1" -vf "fps=${3:-1.5},scale=200:-1,tile=8x1" -frames:v 1 "$2"
