import json,re,subprocess
S='/tmp/claude-0/-home-user-heatgrump/ba0e85e6-8912-5a4f-80da-7fb8f525bf03/scratchpad/postg2'
D='/home/user/heatgrump/output/day'
items=[("G1","d21-1","Perna în folie: rolă, taie un X, scoate halatul (după DfsXmqHTT0B, refăcut de la zero în Seedance 2.5, covor alb)\nText: \"its just a blanket\" 😒🎄","It's NOT just a blanket 😒💚 Comment \"GRINCH\" if you want one 🎄 #grinch #heatedrobe #christmas #giftideas #cozyvibes"),
("G1","d21-4","Halatul înghețat în gheață, spart (după De4-RNdTln4, refăcut de la zero în Seedance 2.5, pe zăpadă)\nText: \"The perfect Grinch robe\ndoesn't exi-\" 😳💚","It exists and it's heated 😳💚 Comment \"GRINCH\" for the link 🎄 #grinch #heatedrobe #christmas #giftideas #winter"),
("G2","d21-3","Punga HEAT GRUMP tăiată și deschisă (după DfPjq3kTDZa, refăcut de la zero în Seedance 2.5, blat de marmură)\nText: \"Babe you don't\nneed that...\" 😑\nMe: 🥹🎄","Me adding it to cart anyway 🥹💚 Comment \"GRINCH\" if you want one 🎄 #grinch #heatedrobe #christmas #giftideas #couplegoals"),
("G2","d21-5","Halatul înghețat în gheață, spart (după De4-RNdTln4, refăcut de la zero în Seedance 2.5, pe verandă)\nText: \"The perfect Grinch robe\ndoesn't exi-\" 🤭❄️","Found it 🤭❄️ Comment \"GRINCH\" for the link 🎄 #grinch #heatedrobe #christmas #giftideas #cozyseason"),
("G3","d21-2","Băiatul cu tava de brioșe pe halat (copiat DfvmqoMzJtc, Seedance 2.5, sufragerie nouă)\nText: I'm literally crying 🥹🎄","Literally crying over a robe 🥹💚 Comment \"GRINCH\" if you want one 🎄 #grinch #heatedrobe #christmas #giftideas #cozyvibes")]
src=open(S+'/index.html',encoding='utf-8').read()
m=re.search(r'const VIDEOS = (\[.*?\]);\n',src,re.S); V=json.loads(m.group(1)); V=[v for v in V if v['day']!='22 nov']
cnt={}
for acc,vid,hook,cap in items:
    cnt[acc]=cnt.get(acc,0)+1; n=cnt[acc]
    V.append({"day":"22 nov","acc":acc,"accName":f"Grinch · contul {acc[1]}","id":vid,"label":f"Video {n}","robe":"Grinch","hook":hook,"caption":cap,"ready":True,"file":f"grinch-{acc}-video{n}-22nov.mp4"})
    subprocess.run(['ffmpeg','-v','error','-y','-ss','2.5','-i',f'{D}/{vid}.mp4','-frames:v','1','-vf','scale=540:-1','-q:v','4',f'{S}/t/{vid}.jpg'])
src=src[:m.start(1)]+json.dumps(V,ensure_ascii=False)+src[m.end(1):]
open(S+'/index.html','w',encoding='utf-8').write(src); print(len(V))
