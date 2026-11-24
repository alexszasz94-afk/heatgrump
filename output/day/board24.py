import json,re,subprocess
S='/tmp/claude-0/-home-user-heatgrump/ba0e85e6-8912-5a4f-80da-7fb8f525bf03/scratchpad/postg3'
D='/home/user/heatgrump/output/day'
H="Rulou peste cap care se desface (hook-ul 3, 2, 1; scenele cu ușa și gunoiul scoase), apoi direct B-roll-ul; sunetul original 3-2-1 pe tot videoul\nFata {n} + B-roll grinch-{n}\nText: {t}"
items=[("G1","d24-51","Don't show this to a\nGrinch mom...🥹💚","Grinch mom approved 🥹💚 Comment \"GRINCH\" if you want one 🎄 #grinch #heatedrobe #christmas #grinchmom #giftideas"),
("G1","d24-57","Grinch girlies, pls\ndon't hate... 🥺💚","Sorry not sorry 🥺💚 Comment \"GRINCH\" for the link 🎄 #grinch #heatedrobe #christmas #giftideas #cozyvibes"),
("G2","d24-53","DONT show this to your\nsister 😳🎄","Tag your sister... or don't 😳🎄 Comment \"GRINCH\" if you want one 💚 #grinch #heatedrobe #christmas #giftideas #sisters"),
("G2","d24-62","Imagine this on the first\nsnow day.. 😌❄️☃️","First snow day plans ❄️💚 Comment \"GRINCH\" for the link 🎄 #grinch #heatedrobe #christmas #winter #cozyseason"),
("G3","d24-54","Christmas-holics this is\nfor YOU..🎄🎅","For every Christmas-holic 🎄💚 Comment \"GRINCH\" if you want one 🎅 #grinch #heatedrobe #christmas #giftideas #cozyvibes")]
src=open(S+'/../postg2/index.html',encoding='utf-8').read()
m=re.search(r'const VIDEOS = (\[.*?\]);\n',src,re.S)
V=[];cnt={}
for acc,vid,t,cap in items:
    cnt[acc]=cnt.get(acc,0)+1; n=cnt[acc]
    V.append({"day":"24 nov","acc":acc,"accName":f"Grinch · contul {acc[1]}","id":vid,"label":f"Video {n}","robe":"Grinch","hook":H.format(n=vid[-2:],t=t),"caption":cap,"ready":True,"file":f"grinch-{acc}-video{n}-24nov.mp4"})
    subprocess.run(['ffmpeg','-v','error','-y','-ss','2.5','-i',f'{D}/{vid}.mp4','-frames:v','1','-vf','scale=540:-1','-q:v','4',f'{S}/t/{vid}.jpg'])
src=src[:m.start(1)]+json.dumps(V,ensure_ascii=False)+src[m.end(1):]
src=src.replace('Postări Grinch 2','Postări Grinch 3')
open(S+'/index.html','w',encoding='utf-8').write(src); print(len(V))
