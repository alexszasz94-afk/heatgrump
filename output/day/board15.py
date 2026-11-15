import json,re,subprocess
S='/tmp/claude-0/-home-user-heatgrump/ba0e85e6-8912-5a4f-80da-7fb8f525bf03/scratchpad/postg'
D='/home/user/heatgrump/output/day'
items=[("G1","d15-1","Piñata cu familia (3,2,1, go!) → iese halatul\nText: Is this the best Christmas\ngift ever?? 🎁😍","Family piñata, but make it Grinch 🎁💚 Comment \"GRINCH\" if you want one 🎄 #grinch #heatedrobe #christmas #giftideas #cozyvibes"),
("G1","d15-4","POV rulou pe podea (lovit cu piciorul)\nText: Christmas-holics this\nis for YOU..🎄🎅","For everyone who's always cold 🥶💚 Comment \"GRINCH\" if you want it 🎄 #grinch #heatedrobe #christmas #cozyvibes #giftideas"),
("G2","d15-2","POV: găsește halatul rulat în zăpadă\nText: Best Christmas gift 2026? 💚🎄","Found the best gift in the snow ❄️💚 Comment \"GRINCH\" for the link 🎄 #grinch #heatedrobe #christmas #snowday #giftideas"),
("G2","d15-5","Rulou în folie\nText: DO NOT show this to a\nChristmas LOVER😱😳","The heated Grinch robe you didn't know you needed 🔥💚 Comment \"GRINCH\" if you want one 😈 #grinch #heatedrobe #christmas #cozyvibes #giftideas"),
("G3","d15-3","POV rulou pe podea\nText: DO NOT show this to a\nmom😱😳...","Mom would steal this in 2 seconds 😳💚 Comment \"GRINCH\" and we'll send you the link 🎄 #grinch #heatedrobe #christmas #giftideas #cozyvibes")]
src=open(S+'/index.html',encoding='utf-8').read()
m=re.search(r'const VIDEOS = (\[.*?\]);\n',src,re.S); V=json.loads(m.group(1)); V=[v for v in V if v['day']!='15 nov']
cnt={}
for acc,vid,hook,cap in items:
    cnt[acc]=cnt.get(acc,0)+1; n=cnt[acc]
    V.append({"day":"15 nov","acc":acc,"accName":f"Grinch · contul {acc[1]}","id":vid,"label":f"Video {n}","robe":"Grinch","hook":hook,"caption":cap,"ready":True,"file":f"grinch-{acc}-video{n}-15nov.mp4"})
    subprocess.run(['ffmpeg','-v','error','-y','-ss','2.5','-i',f'{D}/{vid}.mp4','-frames:v','1','-vf','scale=540:-1','-q:v','4',f'{S}/t/{vid}.jpg'])
src=src[:m.start(1)]+json.dumps(V,ensure_ascii=False)+src[m.end(1):]
open(S+'/index.html','w',encoding='utf-8').write(src); print(len(V))
