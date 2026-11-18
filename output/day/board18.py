import json,re,subprocess
S='/tmp/claude-0/-home-user-heatgrump/ba0e85e6-8912-5a4f-80da-7fb8f525bf03/scratchpad/postg2'
D='/home/user/heatgrump/output/day'
items=[("G1","d18-1","Rulou în folie (mâneci verzi)\nText: Imagine this on the\nfirst snow day.. 😌☃️","First snow day essential ☃️💚 Comment \"GRINCH\" if you want one 🔥 #grinch #heatedrobe #christmas #cozyvibes #giftideas"),
("G1","d18-4","POV rulou pe podea (carouri)\nText: Christmas-holics this\nis for YOU..🎄🎅","Made for the always-cold girlies 🥶💚 Comment \"GRINCH\" for the link 🎄 #grinch #heatedrobe #christmas #cozyvibes #giftideas"),
("G2","d18-2","Punga HEAT GRUMP\nText: Grinch girlies, pls\ndon't hate... 🥺💚","Sorry not sorry, it's heated 🥺💚 Comment \"GRINCH\" if you want one 🔥 #grinch #heatedrobe #christmas #cozyvibes #giftideas"),
("G2","d18-5","POV: găsește halatul în zăpadă\nText: Best Christmas gift 2026? 💚🎄","Dug this out of the snow and never took it off ❄️💚 Comment \"GRINCH\" if you want it 🎄 #grinch #heatedrobe #christmas #snowday #giftideas"),
("G3","d18-3","POV rulou pe podea (buline)\nText: DO NOT show this to a\nmom😱😳...","Mom would steal this in 2 seconds 😳💚 Comment \"GRINCH\" and we'll send you the link 🎄 #grinch #heatedrobe #christmas #giftideas #cozyvibes")]
# Adăugă ziua în pagina boardului (VIDEOS) și face miniaturile; apoi se publicează pagina cu v/<id>.mp4 + t/<id>.jpg (max 64 MB per publicare).
src=open(S+'/index.html',encoding='utf-8').read()
m=re.search(r'const VIDEOS = (\[.*?\]);\n',src,re.S); V=json.loads(m.group(1)); V=[v for v in V if v['day']!='18 nov']
cnt={}
for acc,vid,hook,cap in items:
    cnt[acc]=cnt.get(acc,0)+1; n=cnt[acc]
    V.append({"day":"18 nov","acc":acc,"accName":f"Grinch · contul {acc[1]}","id":vid,"label":f"Video {n}","robe":"Grinch","hook":hook,"caption":cap,"ready":True,"file":f"grinch-{acc}-video{n}-18nov.mp4"})
    subprocess.run(['ffmpeg','-v','error','-y','-ss','2.5','-i',f'{D}/{vid}.mp4','-frames:v','1','-vf','scale=540:-1','-q:v','4',f'{S}/t/{vid}.jpg'])
src=src[:m.start(1)]+json.dumps(V,ensure_ascii=False)+src[m.end(1):]
open(S+'/index.html','w',encoding='utf-8').write(src); print(len(V))
