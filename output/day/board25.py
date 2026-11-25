import json,re,subprocess
S='/tmp/claude-0/-home-user-heatgrump/ba0e85e6-8912-5a4f-80da-7fb8f525bf03/scratchpad/postg3'
D='/home/user/heatgrump/output/day'
items=[("G1","d25-1","POV ruloul pe covor, îl împinge cu piciorul și se desface (copiat 1:1 DczwBh1uRo7, Kling 4.0); B-roll 59\nText: DO NOT show this to\nyour mom 🤫💚","Your mom NEEDS this 🤫💚 Comment \"GRINCH\" if you want one 🎄 #grinch #heatedrobe #christmas #giftideas #momgift"),
("G2","d25-2","Afară în zăpadă, trage pătura Grinch → cutia HEAT GRUMP (copiat 1:1 DgBFiFRsP1y, Kling 4.0); B-roll 65\nText: Christmas idea for your\ngrandparents 🎄🥹","The gift grandma will actually use 🥹💚 Comment \"GRINCH\" for the link 🎄 #grinch #heatedrobe #christmas #giftideas #grandparents"),
("G3","d25-4","De sus, taie punga cu Grinch (copiat 1:1 DgBSFOkBo2M, Kling 4.0); B-roll 61\nText: Every Grinch lover\nneeds this.. 💚🎄","Every Grinch lover needs this 💚🎄 Comment \"GRINCH\" if you want one 🎅 #grinch #heatedrobe #christmas #giftideas #cozyvibes")]
src=open(S+'/index.html',encoding='utf-8').read()
m=re.search(r'const VIDEOS = (\[.*?\]);\n',src,re.S); V=[v for v in json.loads(m.group(1)) if v['day']!='25 nov']
cnt={}
for acc,vid,hook,cap in items:
    cnt[acc]=cnt.get(acc,0)+1; n=cnt[acc]
    V.append({"day":"25 nov","acc":acc,"accName":f"Grinch · contul {acc[1]}","id":vid,"label":f"Video {n}","robe":"Grinch","hook":hook,"caption":cap,"ready":True,"file":f"grinch-{acc}-video{n}-25nov.mp4"})
    subprocess.run(['ffmpeg','-v','error','-y','-ss','2.5','-i',f'{D}/{vid}.mp4','-frames:v','1','-vf','scale=540:-1','-q:v','4',f'{S}/t/{vid}.jpg'])
src=src[:m.start(1)]+json.dumps(V,ensure_ascii=False)+src[m.end(1):]
open(S+'/index.html','w',encoding='utf-8').write(src); print(len(V))
