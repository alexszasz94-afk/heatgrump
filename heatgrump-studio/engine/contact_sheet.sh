# zz.sh out.jpg v:t1,t2,.. ...
out=$1; shift; python3 - "$out" "$@" <<'PY'
import sys,subprocess
from PIL import Image
out=sys.argv[1]; rows=[]
for a in sys.argv[2:]:
  v,ts=a.split(':'); ims=[]
  for t in ts.split(','):
    p=f'/tmp/pp/zz_{v}_{t}.jpg'; subprocess.run(['ffmpeg','-nostdin','-v','error','-y','-ss',t,'-i',f'{v}','-frames:v','1','-vf','scale=200:-1',p]); ims.append(Image.open(p))
  r=Image.new('RGB',(200*len(ims),ims[0].height))
  for i,im in enumerate(ims): r.paste(im,(i*200,0))
  rows.append(r)
o=Image.new('RGB',(max(r.width for r in rows),sum(r.height for r in rows)));y=0
for r in rows:o.paste(r,(0,y));y+=r.height
o.save(out)
PY
