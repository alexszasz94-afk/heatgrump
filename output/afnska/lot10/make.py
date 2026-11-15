import json,subprocess
A='/home/user/heatgrump/output/afnska/'; X='/home/user/heatgrump/heatgrump-studio/music/xmas/'
V=[
 ("v01","broll/broll-lapte.mp4","Main character energy this winter ❄️🤍","🤍",A+"blana-alb-edit/skyfall.mp3",80.73),
 ("v02","broll/s3-negru-fata21.mp4","Tell me this isn't the prettiest coat 🖤","🖤",X+"mariah-all-i-want.mp3",48.4),
 ("v03","broll/s3-ciocolatiu-fata22.mp4","He said it's \"just a coat\".. 🙄🤎","🤎",X+"wham-last-christmas.mp3",0),
 ("v04","broll/s3-roz-fata24.mp4","Every girl needs this coat 🎀🩷","🩷",X+"buble-beginning.mp3",0),
 ("v05","r3-1080/v-genjutsu-roz-graded.mp4","A coat that fits like a dress 😍","🩷",A+"src/r3-audio.m4a",0),
 ("v06","r3-1080/v-genjutsu-graded.mp4","It's giving winter princess 👑🩵","🩵",A+"refs5/audio.m4a",0),
 ("v07","broll/broll-negru.mp4","POV: no more freezing for fashion 🥶","🖤",A+"refs4/audio.m4a",0),
 ("v08","broll/broll-ciocolatiu.mp4","Black Friday wishlist: this coat ✅","🤎",A+"refs7/audio.m4a",0),
 ("v09","broll/s3-gri-fata25.mp4","Warm AND cute? Finally.. 🩶❄️","🩶",A+"hook8/audio.m4a",0),
 ("v10","broll/s3-bleu-fata23.mp4","Snow day outfit = sorted ☃️💙","💙",A+"hook10/audio.m4a",0),
]
cap=open('captions.txt','w')
for n,b,t,e,m,ms in V:
    s={"segments":[{"file":A+b,"start":0.05,"end":13.0}],
       "texts":[{"text":t,"t0":0,"t1":10.6,"y":0.46,"size":60},{"text":f"Comment COAT for the link {e}","t0":10.6,"t1":12.95,"y":0.56,"size":54}],
       "music":m,"music_start":ms,"music_vol":1.0,"orig_vol":0.0,"out":A+f"lot10/frostfemme-{n}.mp4"}
    json.dump(s,open(f"{n}.json","w"),ensure_ascii=False,indent=1)
    c=f"{t}\nComment \"COAT\" and I'll send you the link with a special Black Friday discount ❄️\n#wintercoat #corsetcoat #blackfriday #christmasoutfit #winterfashion #pufferdress\n"
    open(f"{n}-caption.txt","w").write(c); cap.write(f"== {n}\n{c}\n")
    subprocess.run(["python3","/home/user/heatgrump/heatgrump-studio/engine/montage.py",f"{n}.json"],check=True)
