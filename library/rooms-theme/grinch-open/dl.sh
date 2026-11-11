cd /home/user/heatgrump/library/rooms-theme/grinch-open
while read n u; do f=room$(printf %02d $n).jpg; [ -f $f ] && continue; curl -s -f "$u" -o /tmp/pp/r_$n.png && python3 -c "
from PIL import Image;im=Image.open('/tmp/pp/r_$n.png').convert('RGB');im.thumbnail((1080,1920));im.save('$f',quality=90)" && rm /tmp/pp/r_$n.png; done < urls.txt
