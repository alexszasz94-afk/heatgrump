# usage: vshift.py in.mp4 out.mp4 "s:e:shift,s:e:shift"  -> moves only the VOICE (demucs vocals stem) earlier/later, action sounds + room tone stay
import sys, subprocess, os, numpy as np, soundfile as sf, tempfile
src, out, spec = sys.argv[1:4]
t = tempfile.mkdtemp(dir='/tmp/g'); wav = os.path.join(t, 'a.wav')
subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-vn','-ac','2','-ar','44100',wav], check=True)
subprocess.run([sys.executable,'-m','demucs','--two-stems','vocals','-n','htdemucs','-o',t,wav], check=True, capture_output=True)
d = os.path.join(t,'htdemucs','a'); voc, sr = sf.read(os.path.join(d,'vocals.wav')); rest, _ = sf.read(os.path.join(d,'no_vocals.wav'))
new = np.zeros_like(voc)
for seg in spec.split(','):
    s, e, sh = map(float, seg.split(':')); a, b = int(s*sr), min(int(e*sr), len(voc)); o = int((s+sh)*sr)
    piece = voc[a:b].copy(); f = min(int(0.02*sr), len(piece)//2)
    if f: piece[:f] *= np.linspace(0,1,f)[:,None]; piece[-f:] *= np.linspace(1,0,f)[:,None]
    if o < 0: piece = piece[-o:]; o = 0
    n = min(len(piece), len(new)-o); new[o:o+n] += piece[:n]
mix = new + rest; sf.write(os.path.join(t,'m.wav'), mix, sr)
subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-i',os.path.join(t,'m.wav'),'-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k',out], check=True)
subprocess.run(['rm','-rf',t]); print('ok', out)
