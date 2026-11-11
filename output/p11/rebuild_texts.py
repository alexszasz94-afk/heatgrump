import json,subprocess
T=json.load(open('texts.json')); V=json.load(open('videos.json'))
for vid,(h,txt) in T.items():
    if vid=='P1-V3': continue
    v=V[vid]; end='3.97' if h=='r321' else '6.58'; au='ref/pad_r321.m4a' if h=='r321' else 'ref/pad_rC.m4a'
    r=subprocess.run(['python3','mkfinal.py',vid,v['hook_file'],end,f"tails/v/{v['set']}-cut.mp4",au,txt],capture_output=True,text=True)
    print(vid,(r.stdout+r.stderr).strip().splitlines()[-1],flush=True)
