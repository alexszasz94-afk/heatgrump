import numpy as np, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter
src,dst=sys.argv[1],sys.argv[2]; W,H=1080,1920; FPS=24
DOTS=[(580,822),(580,864),(580,906),(580,947),(580,988)]  # 5,4,3,2,1
Y0,Y1,X0,X1=700,1010,380,660
dec=subprocess.Popen(['ffmpeg','-v','error','-i',src,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-c:v','libx264','-crf','14','-pix_fmt','yuv420p',dst],stdin=subprocess.PIPE)
ref=None;k=0;prev=(0,0)
def gray(a): return a[...,0]*.3+a[...,1]*.59+a[...,2]*.11
while True:
    buf=dec.stdout.read(W*H*3)
    if len(buf)<W*H*3: break
    a=np.frombuffer(buf,np.uint8).reshape(H,W,3)
    g=gray(a.astype(np.float32))
    if ref is None: ref=g[Y0:Y1,X0:X1].copy(); off=(0,0)
    else:
        best=None
        for dy in range(prev[1]-12,prev[1]+13,2):
            for dx in range(prev[0]-12,prev[0]+13,2):
                p=g[Y0+dy:Y1+dy:2,X0+dx:X1+dx:2]; d=np.mean((p-ref[::2,::2])**2)
                if best is None or d<best[0]: best=(d,dx,dy)
        b2=None
        for dy in range(best[2]-2,best[2]+3):
            for dx in range(best[1]-2,best[1]+3):
                p=g[Y0+dy:Y1+dy,X0+dx:X1+dx]; d=np.mean((p-ref)**2)
                if b2 is None or d<b2[0]: b2=(d,dx,dy)
        off=(b2[1],b2[2]); prev=off
    t=k/FPS; act=1 if t<0.5 else 2 if t<1.3 else 3 if t<2.1 else 4 if t<2.9 else 5
    im=Image.fromarray(a.copy()).convert('RGBA'); d=ImageDraw.Draw(im)
    glow=Image.new('RGBA',(W,H),(0,0,0,0)); gd=ImageDraw.Draw(glow)
    for i,(x,y) in enumerate(DOTS):
        n=5-i; x+=off[0]; y+=off[1]
        d.ellipse([x-12,y-12,x+12,y+12],fill=(96,98,84,255)); d.ellipse([x-10,y-10,x+10,y+10],fill=(74,76,64,255))
        if n==act: gd.ellipse([x-24,y-24,x+24,y+24],fill=(255,120,70,150))
    glow=glow.filter(ImageFilter.GaussianBlur(8)); im=Image.alpha_composite(im,glow); d=ImageDraw.Draw(im)
    x,y=DOTS[5-act]; x+=off[0]; y+=off[1]
    d.ellipse([x-13,y-13,x+13,y+13],fill=(240,110,70,255)); d.ellipse([x-8,y-8,x+8,y+8],fill=(255,215,190,255))
    enc.stdin.write(im.convert('RGB').tobytes()); k+=1
enc.stdin.close(); enc.wait(); print('frames',k)
