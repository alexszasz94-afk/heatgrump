"""pad_audio.py <ref(mp4|m4a)> <out.m4a> <exit_s> <min_loop_start_s> [total=30]
Lungește audio-ul referinței repetând O PARTE din mijlocul piesei (nu de la început):
original 0..exit, apoi crossfade lung (1,5 s, equal-power) într-un punct din mijloc
(>= min_loop_start, pe bătaie — multiplu de măsuri față de exit), și tot așa până la total.
exit = înainte de orice numărătoare/voce de la finalul originalului."""
import sys,subprocess,numpy as np
inp,out=sys.argv[1],sys.argv[2]; E=float(sys.argv[3]); smin=float(sys.argv[4]); total=float(sys.argv[5]) if len(sys.argv)>5 else 30
SR=44100
a=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',inp,'-vn','-ac','2','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout,np.float32).reshape(-1,2).copy()
mono=a.mean(1); hop=441; fps=SR/hop
fr=np.lib.stride_tricks.sliding_window_view(mono,1024)[::hop]
flux=np.maximum(np.diff(np.log1p(np.abs(np.fft.rfft(fr*np.hanning(1024),axis=1))),axis=0),0).sum(1)
flux=(flux-flux.mean())/(flux.std()+1e-9)
ac=np.correlate(flux,flux,'full')[len(flux)-1:]; lo,hi=int(0.3*fps),int(1.2*fps); P=lo+int(np.argmax(ac[lo:hi]))
e=int(E*fps); W=int(2.5*fps); bar=4*P; best=None; k=1
while e-k*bar>int(smin*fps):
    for s in range(e-k*bar-3,e-k*bar+4):
        if s-W<0: continue
        c=float(np.dot(flux[s-W:s],flux[e-W:e]))/W
        if (E-s/fps)>=5 and (best is None or c>best[0]): best=(c,s)
    k+=1
S=best[1]/fps if best else smin
print(f'beat={P/fps:.3f}s  ies la {E:.2f}s  -> repet partea {S:.2f}–{E:.2f}s')
xf=int(1.5*SR); r=np.sin(np.linspace(0,np.pi/2,xf))[:,None]
res=a[:int(E*SR)].copy(); seg=a[int(S*SR)-xf:int(E*SR)]   # seg începe cu 1,5 s înainte de S ca să se suprapună pe bătaie
while len(res)/SR<total:
    res[-xf:]=res[-xf:]*np.cos(np.linspace(0,np.pi/2,xf))[:,None]+seg[:xf]*r
    res=np.concatenate([res,seg[xf:]])
res=res[:int(total*SR)]
subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','2','-i','-','-c:a','aac','-b:a','192k',out],input=res.astype(np.float32).tobytes(),check=True)
