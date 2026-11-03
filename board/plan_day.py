"""Împarte videourile zilei pe 3 conturi, diversificat (tipuri de hook amestecate, fata nu se repetă pe același cont la rând,
ore decalate între conturi). Folosire: python3 board/plan_day.py 2026-11-02 grup:dir1,dir2 ...  -> board/days/<zi>.json"""
import json,sys,os,itertools,random
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAP={
 "storemug":["When the Grinch robe finally hits the shelves 🏃‍♀️🎄","Me speed-walking to aisle 12 like 🏃‍♀️💚"],
 "grinchmom":["Every Grinch mom needs this before Christmas 💚","She said she hates Christmas… then she put this on 🤩🎄","Stay warm. Stay grumpy. 💚"],
 "nogift":["Okay but this one IS perfect 😏🎁","Best gift ever and I'm not even sorry 😏💚"],
 "tray123":["1, 2, 3… and I'm never taking it off 💚","The unwrapping I've been waiting for all year 🎁"],
 "mallwindow":["I literally fell for it 😭💚","Saw it in the window and that was it 🫠🎄"],
 "mallrun":["The line was worth it 🏃‍♀️💚","Ran across the whole mall for this 😮‍💨🎄"],
 "twofriends":["Matching with my bestie this Christmas 💚💚","Bestie gift solved 🎁🎄"],
 "hmstore":["3, 2, 1… the Grinch drop is HERE 🤩🎄","They finally pulled the cover off 😭💚"],
 "mallcoffee":["Dropped my coffee for this and no regrets ☕💚","Saw the window and lost it 😭🎄"],
 "unroll":["Unrolling my new favorite thing 🥹💚","Mom is getting one too 😳❄️"],
 "rollcake":["Freshly baked Grinch robe, anyone? 🎂💚","Best thing I made all season 😂❄️"],
 "fbhook":["Christmas mode: ON 💚🎄","This is your sign to get cozy 🎄"]}
TAGS={"a":"#grinch #christmas #cozy #giftideas #heatedrobe","b":"#grinchmas #christmasgift #momlife #cozyvibes #wintervibes","c":"#grinchy #holidaygifts #cozyseason #giftsforher #christmas2026"}
CTA=['Type "GRINCH" if you want this 💚','Comment "GRINCH" and I\'ll send you the link 🎄','Type "GRINCH" if you need this 😏','Drop a "GRINCH" below if you want one 💚','Type "GRINCH" for the link 🎁','Comment "GRINCH" if this is so you 🤭']
POOL=["#grinch","#christmas","#cozy","#giftideas","#heatedrobe","#grinchmas","#christmasgift","#momlife","#cozyvibes","#wintervibes","#grinchy","#holidaygifts","#cozyseason","#giftsforher","#christmas2026","#wearableblanket","#christmasvibes","#giftsformom","#hoodedblanket","#christmasmorning","#cozyhome","#holidayseason","#stockingstuffer","#christmasshopping","#grinchlover","#xmasgifts","#cozyathome","#winterfashion","#giftguide","#merrychristmas"]
SLOTS=["07:40","09:10","10:40","12:10","13:40","15:10","16:40","18:10","19:30","20:30","21:30","22:30"]
OFF={"a":0,"b":20,"c":40}
def run(day,groups):
    vids=[]
    for g,dirs in groups:
        for d in dirs:
            st=d.split('-set')[-1] if '-set' in d else 'set27'
            vids.append({"type":g,"dir":d,"set":"set"+st if not st.startswith('set') else st})
    acc={"a":[],"b":[],"c":[]}; keys=list(acc)
    i=0
    for t in sorted({v['type'] for v in vids},key=lambda t:-sum(v['type']==t for v in vids)):
        for v in [x for x in vids if x['type']==t]:
            acc[keys[i%3]].append(v); i+=1
    out={"day":day,"accounts":{}}
    for k,lst in acc.items():
        random.seed(day+k); order=[]; pool=lst[:]
        while pool:
            last=order[-1] if order else None
            cand=[v for v in pool if not last or (v['type']!=last['type'] and v['set']!=last['set'])] or pool
            v=random.choice(cand); pool.remove(v); order.append(v)
        for j,v in enumerate(order):
            h,m=map(int,SLOTS[j%len(SLOTS)].split(':')); m+=OFF[k]; h+=m//60; m%=60
            v['time']=f"{h:02d}:{m:02d}"; c=CAP[v['type']]; rr=random.Random(day+k+v['dir']); tags=" ".join(rr.sample(POOL,6)); v['caption']=c[(j+keys.index(k))%len(c)]+"\n"+CTA[(j*3+keys.index(k))%len(CTA)]+"\n"+tags
            ed=json.load(open(f"{R}/output/videos/{v['dir']}/edit.json")); v['text']=ed['texts'][0]['text'] if ed.get('texts') else ''
            v['file']=f"output/videos/{v['dir']}/{os.path.basename(ed['out'])}"
        out["accounts"][k]=order
    json.dump(out,open(f"{R}/board/days/{day}.json","w"),ensure_ascii=False,indent=1); return out
if __name__=="__main__":
    day=sys.argv[1]; groups=[(a.split(':')[0],a.split(':')[1].split(',')) for a in sys.argv[2:]]
    o=run(day,groups)
    for k,l in o["accounts"].items(): print(k,[(v['time'],v['dir']) for v in l])
