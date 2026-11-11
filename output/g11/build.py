import json,subprocess,sys
T=json.load(open('texts.json'))
for s in sys.argv[1:]:
    h,end,txt=T[s]
    r=subprocess.run(['python3','mkfinal.py',s,f'h/{s}.mp4',str(end),f'/home/user/heatgrump/output/boards/grinch/fix/{s}.mp4',f'ref/pad_{h}.m4a',txt],capture_output=True,text=True)
    print(s,(r.stdout+r.stderr).strip().splitlines()[-1],flush=True)
