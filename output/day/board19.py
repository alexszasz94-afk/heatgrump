import json,re,subprocess
S='/tmp/claude-0/-home-user-heatgrump/ba0e85e6-8912-5a4f-80da-7fb8f525bf03/scratchpad/postg2'
D='/home/user/heatgrump/output/day'
items=[("G1","d19-1","Grinch mom (halatul ținut în brațe, se desface) – hook vechi\nText: Do NOT let a Grinch\nmom see this... 🤩🎄","Grinch mom energy all season 💚🎄 Comment \"GRINCH\" if you want one 🤩 #grinch #heatedrobe #christmas #grinchmom #giftideas"),
("G1","d19-4","Tava cu cadoul (1,2,3) – hook vechi\nText: DONT Show this to a\nGRINCH LOVER...🎄💚","The gift every Grinch lover needs 🎁💚 Comment \"GRINCH\" for the link 🎄 #grinch #heatedrobe #christmas #giftideas #cozyvibes"),
("G2","d19-2","Target, raftul cu cutii – hook vechi\nText: Moms DONT walk.. 🏃‍♀️\nRUN to target 🎯🎄","Moms, this is your sign 🏃‍♀️💚 Comment \"GRINCH\" if you want one 🎄 #grinch #heatedrobe #christmas #momsoftiktok #giftideas"),
("G2","d19-5","Raftul plin cu halate – hook vechi\nText: 👱: \"No gift is perfect\"\nMe: 😏","Found the perfect gift, sorry 😏💚 Comment \"GRINCH\" for the link 🎄 #grinch #heatedrobe #christmas #giftideas #cozyvibes"),
("G3","d19-3","Unboxing cutia HEAT GRUMP – hook vechi\nText: The best purchase I've\nEVER made...😍💖","Best purchase of the year, no contest 😍💚 Comment \"GRINCH\" if you want one 🎄 #grinch #heatedrobe #christmas #unboxing #giftideas")]
src=open(S+'/index.html',encoding='utf-8').read()
m=re.search(r'const VIDEOS = (\[.*?\]);\n',src,re.S); V=json.loads(m.group(1)); V=[v for v in V if v['day']!='19 nov']
cnt={}
for acc,vid,hook,cap in items:
    cnt[acc]=cnt.get(acc,0)+1; n=cnt[acc]
    V.append({"day":"19 nov","acc":acc,"accName":f"Grinch · contul {acc[1]}","id":vid,"label":f"Video {n}","robe":"Grinch","hook":hook,"caption":cap,"ready":True,"file":f"grinch-{acc}-video{n}-19nov.mp4"})
    subprocess.run(['ffmpeg','-v','error','-y','-ss','2.5','-i',f'{D}/{vid}.mp4','-frames:v','1','-vf','scale=540:-1','-q:v','4',f'{S}/t/{vid}.jpg'])
src=src[:m.start(1)]+json.dumps(V,ensure_ascii=False)+src[m.end(1):]
open(S+'/index.html','w',encoding='utf-8').write(src); print(len(V))
