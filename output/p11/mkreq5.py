import json,re,copy
d=json.load(open('req_hooks4.json')); NB=json.load(open('ref-nobelt/ref-nobelt.json'))
P=[r['params'] for r in d]
def seg(p,a,b):
    i=p.index(a); j=p.index(b,i); return p[i:j+len(b)]
def person(p): return seg(p,'PERSON = ','print.')
def robe(p):  return seg(p,'ROBE = ','with its hood;')
def imgs(p): return [m['value'] for m in p['medias'] if m['role']=='image_references']
ROBE_OF={'ice-blue':0,'snow-apple':1,'golden-rose':2,'green-lily':3}
EXTRA=(" NO BELT ANYWHERE: the robe has no belt, no sash, no cord and no bow at the waist, nothing tied at the waist and nothing hanging, exactly like Image 3, in every shot."
       " HOOD MOTION: the hood is soft heavy plush; as the robe unrolls it flops down naturally with gravity and swings slightly, then hangs still at the TOP of the robe just under her hands; it never lifts, inflates, stiffens, changes shape or slides to the middle of the robe.")
def fix(prompt,robe_name):
    r=robe(P[ROBE_OF[robe_name]]['prompt']).replace('cuffs and belt','cuffs').replace('Images 3-5 (front, back, hood up)','Images 3-4 (Image 3 front, Image 4 hood up)').replace('Images 3-5','Images 3-4')
    prompt=prompt.replace(robe(prompt),r.replace('the red belt, ',''))
    prompt=prompt.replace('Silent.', EXTRA.strip()+' Silent.')
    return prompt
def medias(video,girl,room,robe_name):
    ri=imgs(P[ROBE_OF[robe_name]])
    return [{"role":"video_references","value":video},{"role":"image_references","value":girl},{"role":"image_references","value":room},
            {"role":"image_references","value":NB[robe_name]},{"role":"image_references","value":ri[4]}]
C=P[2]['prompt']; RC_VIDEO=P[2]['medias'][0]['value']
jobs={}
# r321 redo (same girl/room/robe)
for vid,i,robe_name in [('P1-V1',0,'ice-blue'),('P2-V1',3,'green-lily'),('P3-V1',6,'snow-apple')]:
    p=P[i]; g,rm=imgs(p)[:2]
    jobs[vid]=dict(duration=4,medias=medias(p['medias'][0]['value'],g,rm,robe_name),prompt=fix(p['prompt'],robe_name))
# rC: person/room from source index
for vid,src,robe_name in [('P1-V2',1,'snow-apple'),('P2-V2',4,'ice-blue'),('P2-V3',5,'golden-rose'),('P3-V2',7,'green-lily'),('P3-V3',3,'golden-rose')]:
    s=P[src]; g,rm=imgs(s)[:2]
    if vid=='P3-V3': rm='f3165b45-'  # placeholder fixed below
    pr=C.replace(person(C),person(s['prompt']))
    jobs[vid]=dict(duration=7,medias=medias(RC_VIDEO,g,rm,robe_name),prompt=fix(pr,robe_name))
# full uuid for room f3165b45
full=[m for p in P for m in imgs(p) if m.startswith('f3165b45')][0]
for m in jobs['P3-V3']['medias']:
    if m['value']=='f3165b45-': m['value']=full
out=[]
for k,(vid,j) in enumerate(jobs.items()):
    out.append({"index":k,"vid":vid,"params":{"model":"kling4_0","mode":"video-edit","duration":j['duration'],"resolution":"1080p","aspect_ratio":"9:16","declined_preset_id":"24bae836-2c4a-48e0-89b6-49fcc0b21612","use_unlim":False,"medias":j['medias'],"prompt":j['prompt']}})
json.dump(out,open('req_hooks5.json','w'),indent=1,ensure_ascii=False)
for o in out: print(o['vid'],o['params']['duration'],[m['value'][:8] for m in o['params']['medias']],len(o['params']['prompt']))
print(out[3]['params']['prompt'])
