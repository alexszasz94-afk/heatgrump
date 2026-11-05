"""fixa.py picture.mp4 audio_src.mp4 out.mp4 [T bed]   -> picture + audio of audio_src; if T given, audio 0..T replaced by bed
bed = file:start:end (looped with crossfades, level-matched) | noise:<dB>"""
import sys,subprocess,numpy as np
SR=48000
def dec(f,ss=0,t=None):
    c=["ffmpeg","-v","error","-ss",str(ss),"-i",f]+(["-t",str(t)] if t else [])+["-vn","-ac","2","-ar",str(SR),"-f","f32le","-"]
    return np.frombuffer(subprocess.run(c,capture_output=True).stdout,np.float32).reshape(-1,2).copy()
pic,asrc,out=sys.argv[1:4]
a=dec(asrc)
dur=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",pic]))
n=int(dur*SR); a=np.pad(a,((0,max(0,n-len(a))),(0,0)))[:n]
if len(sys.argv)>4:
    T=float(sys.argv[4]); bed=sys.argv[5]; nt=int(T*SR); xf=int(0.15*SR)
    if bed.startswith("noise"):
        db=float(bed.split(":")[1]); w=np.cumsum(np.random.default_rng(1).normal(0,1,(nt+xf,2)),0); w-=np.convolve(w[:,0],np.ones(4801)/4801,'same')[:,None]
        w/=np.sqrt((w**2).mean()); b=w*10**(db/20)
    else:
        _,f,s,e=bed.split(":",3) if bed.count(":")==3 else (None,)+tuple(bed.split(":"))
        seg=dec(f,float(s),float(e)-float(s)); L=len(seg); fx=int(0.1*SR)
        b=np.zeros((nt+xf,2),np.float32); pos=0; ramp=np.linspace(0,1,fx)[:,None]
        while pos<len(b):
            s2=seg.copy()
            if pos>0: s2[:fx]*=ramp; b[pos:pos+fx]*=(1-ramp[:len(b[pos:pos+fx])])
            k=min(L,len(b)-pos); b[pos:pos+k]+=s2[:k]; pos+=L-fx
    r=np.linspace(0,1,xf)[:,None]
    newa=a.copy(); newa[:nt-xf]=b[:nt-xf]; newa[nt-xf:nt]=b[nt-xf:nt]*(1-r)+a[nt-xf:nt]*r
    a=newa
p=subprocess.Popen(["ffmpeg","-v","error","-y","-i",pic,"-f","f32le","-ar",str(SR),"-ac","2","-i","-","-map","0:v","-map","1:a","-c:v","copy","-c:a","aac","-b:a","192k","-shortest",out],stdin=subprocess.PIPE)
p.communicate(a.astype(np.float32).tobytes()); print(out,"ok")
