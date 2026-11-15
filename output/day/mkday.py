"""mkday.py <name> <hook.mp4> <hook_end> <broll.mp4> <text> [text_on_hook=1]
Montaj zilnic: hook -> spate -> săculeți (până se închide) -> conector alb -> telecomanda din B-roll -> cozy.
Mariah Carey cu refrenul (53.4 s) exact pe tăietura hook -> B-roll; sunetul hook-ului oprit."""
import json,sys,subprocess,os
name,hook,he,br,text=sys.argv[1:6]; he=float(he); on_hook=(sys.argv[6]!='0') if len(sys.argv)>6 else True
D=os.path.dirname(os.path.abspath(__file__)); f=1/24
out=subprocess.run(['ffmpeg','-v','info','-i',br,'-vf',"select='gt(scene,0.12)',showinfo",'-an','-f','null','-'],capture_output=True,text=True).stderr
cuts=[float(x.split(':')[1]) for x in out.split() if x.startswith('pts_time:')]
def near(t,w=0.4): c=[x for x in cuts if abs(x-t)<w]; return min(c,key=lambda x:abs(x-t)) if c else None
cf,cc,ck,cz=near(2.4),near(6.6),near(7.4),near(9.4)
print(name,'cuts',cf,cc,ck,cz)
cozy=f'{D}/{name}-cozy.mp4'
subprocess.check_call(['ffmpeg','-v','error','-y','-ss',str(cz+f),'-i',br,'-an','-vf','setpts=1.4*PTS,fps=30','-c:v','libx264','-crf','14','-pix_fmt','yuv420p',cozy])
cd=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',cozy]))
segs=[{"file":os.path.abspath(hook),"start":0,"end":he,"audio":False},
 {"file":br,"start":0.5,"end":round(cf-f,3)},
 {"file":br,"start":round(cf+f,3),"end":round(cc-f,3)},
 {"file":"/home/user/heatgrump/library/motion/conector-telecomanda-alb.mp4","start":0,"end":2.66},
 {"file":br,"start":round(ck+f,3),"end":round(cz-f,3)},
 {"file":cozy,"start":0,"end":round(cd-0.05,2)}]
sp={"out":f"{D}/{name}.mp4","fps":30,"segments":segs,
 "texts":[{"segs":[0 if on_hook else 1,-1],"text":text.replace('\\n','\n'),"size":64,"y":0.165}],
 "music":"/home/user/heatgrump/heatgrump-studio/music/xmas/mariah-all-i-want.mp3","music_start":round(53.4-he,2),
 "music_duck":he,"music_hook_vol":0.7,"music_drop_vol":1.0}
if os.environ.get('MUSIC'):   # hook copiat -> sunetul ORIGINAL al referinței pe tot videoul (pad_*.m4a), fără Mariah
    sp.update({"music":os.environ['MUSIC'],"music_start":0})
    for k in ('music_duck','music_hook_vol','music_drop_vol'): sp.pop(k)
json.dump(sp,open(f'{D}/{name}.json','w'),indent=1,ensure_ascii=False)
subprocess.check_call([sys.executable,'/home/user/heatgrump/heatgrump-studio/engine/montage.py',f'{D}/{name}.json'],cwd='/home/user/heatgrump/heatgrump-studio')
os.remove(cozy)
