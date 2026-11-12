import numpy as np, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter
src,dst=sys.argv[1],sys.argv[2]; W,H=1080,1920; FPS=24
T=[(484,575),(486,651),(488,729),(490,805),(492,881)]  # dots 5..1 in frame 1
dec=subprocess.Popen(['ffmpeg','-v','error','-i',src,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-c:v','libx264','-crf','14','-pix_fmt','yuv420p',dst],stdin=subprocess.PIPE)
k=0; off=(0,0)
while True:
    buf=dec.stdout.read(W*H*3)
    if len(buf)<W*H*3: break
    a=np.frombuffer(buf,np.uint8).reshape(H,W,3)
    reg=a[530:930,430:550].astype(int); m=reg.mean(2)<90
    ys,xs=np.nonzero(m)
    # dot clusters (big)
    found=[]
    for (tx,ty) in T:
        sel=(abs(ys+530-(ty+off[1]))<18)&(abs(xs+430-(tx+off[0]))<18)
        if sel.sum()>120: found.append((xs[sel].mean()+430-tx, ys[sel].mean()+530-ty))
    if found: off=(float(np.median([f[0] for f in found])),float(np.median([f[1] for f in found])))
    t=k/FPS; act=1 if t<0.5 else 2 if t<1.3 else 3 if t<2.1 else 4 if t<2.9 else 5
    im=Image.fromarray(a.copy()); d=ImageDraw.Draw(im)
    glow=Image.new('RGBA',(W,H),(0,0,0,0)); gd=ImageDraw.Draw(glow)
    for i,(tx,ty) in enumerate(T):
        n=5-i; x=tx+off[0]; y=ty+off[1]
        if n==act:
            gd.ellipse([x-17,y-17,x+17,y+17],fill=(120,255,140,110))
            d.ellipse([x-10,y-10,x+10,y+10],fill=(205,255,200))
        else:
            d.ellipse([x-11,y-11,x+11,y+11],fill=(42,42,45))
    glow=glow.filter(ImageFilter.GaussianBlur(6))
    im=Image.alpha_composite(im.convert('RGBA'),glow).convert('RGB')
    d=ImageDraw.Draw(im)
    x=T[5-act][0]+off[0]; y=T[5-act][1]+off[1]; d.ellipse([x-8,y-8,x+8,y+8],fill=(150,240,150))
    enc.stdin.write(im.tobytes()); k+=1
enc.stdin.close(); enc.wait(); print('frames',k)
