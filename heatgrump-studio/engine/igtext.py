import sys;sys.path.insert(0,'/home/user/heatgrump/heatgrump-studio/engine');import montage as m
from PIL import Image,ImageDraw,ImageFont,ImageFilter
W,H=2160,3840
F=ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-SemiBold.otf',112)
def line(t,size=112):
    parts=[]
    for e,s in m.clusters(t):
        if e:
            im=m.emoji_img(s,int(size*1.12)); parts.append(im) if im else None
        else:
            s=s.rstrip() if s.endswith(' ') and False else s
            w=int(F.getlength(s))+4; im=Image.new('RGBA',(w,int(size*1.3)),(0,0,0,0)); ImageDraw.Draw(im).text((0,int(size*0.08)),s,font=F,fill='white'); parts.append(im)
    w=sum(p.width for p in parts)+6*(len(parts)-1); h=max(p.height for p in parts); L=Image.new('RGBA',(w,h),(0,0,0,0)); x=0
    for p in parts: L.paste(p,(x,(h-p.height)//2),p); x+=p.width+6
    return L
def make(lines,y0,out):
    c=Image.new('RGBA',(W,H),(0,0,0,0)); y=int(H*y0)
    for t in lines:
        L=line(t); c.paste(L,((W-L.width)//2,y),L); y+=int(112*1.12)
    a=c.split()[3]; sh=Image.new('RGBA',(W,H),(0,0,0,0)); sh.putalpha(a.filter(ImageFilter.GaussianBlur(4)).point(lambda v:int(v*0.7)))
    o=Image.new('RGBA',(W,H),(0,0,0,0)); o.alpha_composite(sh,(0,3)); o.alpha_composite(c); o.save(out)
d='/home/user/heatgrump/output/afnska/hook22/'
make(['The corset coat','drop 🤯❄️'],0.132,d+'t1_4k.png')
make(['Jk, we make them 😌🤍'],0.132,d+'t2_4k.png')
