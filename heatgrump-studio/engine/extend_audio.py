"""extend_audio.py <in(mp4|m4a)> <out.m4a> <min_loop_start_s> [total_s=30]
Lungește audio-ul referinței DOAR din muzică: după ~finalul originalului continuă
dintr-un punct din mijlocul muzicii (>= min_loop_start, deci fără numărătoare/voce de hook),
ales pe potrivirea de ritm (corelație pe anvelopa de onset), cu crossfade 0.4 s."""
import sys,subprocess,numpy as np
inp,out,smin=sys.argv[1],sys.argv[2],float(sys.argv[3]); total=float(sys.argv[4]) if len(sys.argv)>4 else 30
SR=44100
a=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',inp,'-vn','-ac','2','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout,np.float32).reshape(-1,2).copy()
L=len(a)/SR
mono=a.mean(1); hop=441
fr=np.lib.stride_tricks.sliding_window_view(mono[:len(mono)//hop*hop+0],1024)[::hop] if len(mono)>1024 else None
spec=np.abs(np.fft.rfft(fr*np.hanning(1024),axis=1))
flux=np.maximum(np.diff(np.log1p(spec),axis=0),0).sum(1); flux=(flux-flux.mean())/(flux.std()+1e-9)
fps=SR/hop
E=L-1.0                                  # punctul de ieșire din original
W=int(3*fps); e=int(E*fps)
tmpl=flux[e-W:e]
ac=np.correlate(flux,flux,'full')[len(flux)-1:]
lo,hi=int(0.3*fps),int(1.2*fps); P=lo+int(np.argmax(ac[lo:hi]))
# bară = 4 bătăi; candidați doar la multipli de bară față de ieșire (ritmul rămâne în fază)
bar=4*P; cands=[]
k=1
while e-k*bar-W>0:
    c0=e-k*bar
    if c0>=int((smin+3)*fps): cands+=list(range(c0-3,c0+4))
    k+=1
if not cands: cands=list(range(int((smin+3)*fps), int((E-2.5)*fps)))
print(f'beat={P/fps:.3f}s')
best=None
for s in cands:
    c=float(np.dot(flux[s-W:s],tmpl))/W
    # potrivire și de nivel (volum)
    lv=abs(np.log((np.abs(mono[int(s/fps*SR)-SR//2:int(s/fps*SR)]).mean()+1e-6)/(np.abs(mono[int(E*SR)-SR//2:int(E*SR)]).mean()+1e-6)))
    sc=c-0.5*lv
    if best is None or sc>best[0]: best=(sc,s)
S=best[1]/fps
print(f'L={L:.2f} exit={E:.2f} -> continuă de la {S:.2f}s (score {best[0]:.2f})')
xf=int(0.4*SR); res=a[:int(E*SR)].copy()
seg=a[int(S*SR):int(E*SR)]   # bucla: S..E se repetă cât e nevoie
while len(res)/SR<total:
    r=np.linspace(1,0,xf)[:,None]
    res[-xf:]=res[-xf:]*r+seg[:xf]*(1-r)
    res=np.concatenate([res,seg[xf:]])
res=res[:int(total*SR)]
subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','2','-i','-','-c:a','aac','-b:a','192k',out],input=res.astype(np.float32).tobytes(),check=True)
