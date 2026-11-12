import json,sys,subprocess,os
# mk.py <name> <hook.mp4> <broll.mp4> [hook_end=4.25] [sacks_end=5.4]
B='/home/user/heatgrump/output/r17'
name,hook,br=sys.argv[1:4]; he=float(sys.argv[4]) if len(sys.argv)>4 else 4.25; se=float(sys.argv[5]) if len(sys.argv)>5 else 5.4
out=subprocess.run(['ffmpeg','-v','info','-i',br,'-vf',"select='gt(scene,0.12)',showinfo",'-an','-f','null','-'],capture_output=True,text=True).stderr
cuts=[float(x.split(':')[1]) for x in out.split() if x.startswith('pts_time:')]
def near(t,w=0.35): c=[x for x in cuts if abs(x-t)<w]; return min(c,key=lambda x:abs(x-t)) if c else None
c_front=near(2.4,0.3); c_conn=near(6.6); c_ctrl=near(7.4); c_cozy=near(9.4)
print(name,'cuts',cuts,'->',c_front,c_conn,c_ctrl,c_cozy)
f=1/24
cozy=f'{B}/final/{name}-cozy.mp4'
subprocess.check_call(['ffmpeg','-v','error','-y','-ss',str(c_cozy+f),'-i',br,'-an','-vf','setpts=1.4*PTS,fps=30','-c:v','libx264','-crf','14','-pix_fmt','yuv420p',cozy])
segs=[{"file":os.path.abspath(hook),"start":0,"end":he,"audio":False},
 {"file":os.path.abspath(br),"start":0.5,"end":round(c_front-f,3)},
 {"file":os.path.abspath(br),"start":round(c_front+f,3),"end":se},
 {"file":os.path.abspath(br),"start":round(c_conn+f,3),"end":round(c_ctrl-f,3)},
 {"file":os.path.abspath(br),"start":round(c_ctrl+f,3),"end":round(c_cozy-f,3)},
 {"file":cozy,"start":0,"end":round(float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',cozy]))-0.05,2)}]
sp={"out":f"{B}/final/{name}.mp4","fps":30,"segments":segs,
 "texts":[{"segs":[0,-1],"text":"DONT show this to\nyour mom... 😳❄️","size":int(os.environ.get('TSIZE','64')),"y":0.165}],
 "music":"/tmp/pp/r17/music.m4a","music_start":0}
json.dump(sp,open(f'{B}/final/{name}.json','w'),indent=1,ensure_ascii=False)
subprocess.check_call([sys.executable,'/home/user/heatgrump/heatgrump-studio/engine/montage.py',f'{B}/final/{name}.json'],cwd='/home/user/heatgrump/heatgrump-studio')
os.remove(cozy)
