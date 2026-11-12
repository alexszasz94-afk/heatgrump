import json,re,subprocess,os,shutil
S='/tmp/claude-0/-home-user-heatgrump/ba0e85e6-8912-5a4f-80da-7fb8f525bf03/scratchpad/postg'
F='/home/user/heatgrump/output/r17/final'
TXT="DONT show this to\nyour mom... 😳❄️"
plan=[("G1",["S00","S04","S08"]),("G2",["S06","S01","S05"]),("G3",["S07","S02","S03"])]
green={"S00","S06","S07"}
caps=["Rolled it out and never took it off 😳💚 Comment \"GRINCH\" if you want one 🎄 #grinch #heatedrobe #christmas #cozyvibes #giftideas",
"Mom can't know about this one 🤫💚 Comment \"GRINCH\" and we'll send you the link 🎄 #grinch #heatedrobe #christmas #cozyvibes #giftideas",
"The heated Grinch robe with foot pockets 🥶➡️🔥 Comment \"GRINCH\" if you need it 💚 #grinch #heatedrobe #christmas #cozyvibes #giftideas",
"Unrolling the coziest thing I own 😌❄️ Comment \"GRINCH\" if you want one 💚 #grinch #heatedrobe #christmas #cozyvibes #giftideas",
"She'd steal it in two seconds 😈💚 Comment \"GRINCH\" for the link 🎄 #grinch #heatedrobe #christmas #cozyvibes #giftideas",
"Heated, hooded and Grinchy 🔥💚 Comment \"GRINCH\" if you want it 🎄 #grinch #heatedrobe #christmas #cozyvibes #giftideas",
"Cold feet? Not anymore 🥶💚 Comment \"GRINCH\" if you want one 🎄 #grinch #heatedrobe #christmas #cozyvibes #giftideas",
"POV: you finally found the perfect gift 🎁💚 Comment \"GRINCH\" for the link 🔥 #grinch #heatedrobe #christmas #cozyvibes #giftideas",
"Winter mode: activated ❄️💚 Comment \"GRINCH\" if you want one 😈 #grinch #heatedrobe #christmas #cozyvibes #giftideas"]
src=open(S+'/index.html',encoding='utf-8').read()
m=re.search(r'const VIDEOS = (\[.*?\]);\n',src,re.S); V=json.loads(m.group(1))
V=[v for v in V if v['day']!='12 nov']
os.makedirs(S+'/v12',exist_ok=True); os.makedirs(S+'/t',exist_ok=True)
k=0
for acc,vids in plan:
    for j,s in enumerate(vids):
        vid=f"r12-{acc}-{j+1}"; ready=os.path.exists(f"{F}/{s}.mp4")
        hook="Rulou VERDE care se desface (gluga cu fața)" if s in green else "Rulou care se desface, se văd săculeții"
        V.append({"day":"12 nov","acc":acc,"accName":f"Grinch · contul {acc[1]}","id":vid,"label":f"Video {j+1}","robe":"Grinch",
          "hook":hook+"\nText: "+TXT,"caption":caps[k],"ready":ready,"file":f"grinch-{acc}-video{j+1}-12nov.mp4"}); k+=1
        if ready:
            shutil.copy(f"{F}/{s}.mp4",f"{S}/v12/{vid}.mp4")
            subprocess.run(['ffmpeg','-v','error','-y','-ss','3.9','-i',f"{F}/{s}.mp4",'-frames:v','1','-vf','scale=540:-1','-q:v','4',f"{S}/t/{vid}.jpg"])
src=src[:m.start(1)]+json.dumps(V,ensure_ascii=False)+src[m.end(1):]
open(S+'/index.html','w',encoding='utf-8').write(src)
print([ (v['id'],v['ready']) for v in V if v['day']=='12 nov'])
