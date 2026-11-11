import json,sys,subprocess,os
# mkfinal.py <vid> <hook.mp4> <hook_end> <tail.mp4> <audio|-> <text|-> [music_start]
vid,hook,he,tail,audio,text=sys.argv[1:7]; ms=float(sys.argv[7]) if len(sys.argv)>7 else 0
B='/home/user/heatgrump/output/g11'; os.makedirs(f'{B}/final',exist_ok=True)
td=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',tail]))
sp={"out":f"{B}/final/{vid}.mp4","fps":30,"segments":[{"file":os.path.abspath(hook),"start":0,"end":float(he),"audio":False},{"file":os.path.abspath(tail),"start":0,"end":round(td,2)}],
    "texts":([] if text=='-' else [{"segs":[0,-1],"text":text.replace('\\n','\n'),"size":int(os.environ.get('TSIZE','64')),"y":0.165}])}
if audio!='-': sp.update({"music":os.path.abspath(audio),"music_start":ms})
json.dump(sp,open(f'{B}/final/{vid}.json','w'),indent=1,ensure_ascii=False)
subprocess.check_call([sys.executable,'/home/user/heatgrump/heatgrump-studio/engine/montage.py',f'{B}/final/{vid}.json'],cwd='/home/user/heatgrump/heatgrump-studio')
print(vid, subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',sp['out']]).decode().strip())
