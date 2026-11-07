"""Board-ul zilei: python3 board/build_day.py <zi> <out_dir>  -> <out_dir>/index.html + thumbs/"""
import json,sys,os,subprocess,html
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
day,out=sys.argv[1],sys.argv[2]; os.makedirs(f"{out}/thumbs",exist_ok=True)
D=json.load(open(f"{R}/board/days/{day}.json"))
RAW="https://github.com/alexszasz94-afk/heatgrump/raw/heatgrump-studio/"
NAMES={"storemug":"Magazin – cana","grinchmom":"Grinch mom","nogift":"No gift is perfect","tray123":"Tava 1-2-3","mallwindow":"Vitrina mall","mallrun":"Mall run","twofriends":"Două prietene","hmstore":"H&M dezvelire","mallcoffee":"Mall cafea + vitrină","unroll":"Rulou desfăcut","rollcake":"Rulou cu tava","fbhook":"Hook Facebook","unbox":"Unboxing mailer","zara":"Grinch x ZARA","costco":"Costco rush","reveal":"Dezvelire cu pânză","rollup":"Rulou deasupra capului"}
ACC={"a":"Cont 1","b":"Cont 2","c":"Cont 3"}
cols=[]
for k,lst in D["accounts"].items():
    cards=[]
    for v in lst:
        th=f"thumbs/{v['dir']}.jpg"
        if not os.path.exists(f"{out}/{th}"):
            subprocess.run(["ffmpeg","-loglevel","error","-y","-ss","1.2","-i",f"{R}/{v['file']}","-frames:v","1","-vf","scale=240:-2","-q:v","5",f"{out}/{th}"])
        cid=f"c-{k}-{v['dir']}"
        cards.append(f'''<article class="card" data-key="{day}_{k}_{v['dir']}"><video src="v/{v['dir']}.mp4" poster="{th}" controls playsinline preload="none" aria-label="{html.escape(NAMES[v['type']])}"></video>
<div class="meta"><div class="top"><time>{v['time']}</time><span class="tag t-{v['type']}">{NAMES[v['type']]}</span></div>
<p class="ost">{html.escape(v['text']).replace(chr(10),'<br>')}</p>
<p class="cap" id="{cid}">{html.escape(v['caption'])}</p>
<label class="post"><input type="checkbox" data-post="{day}_{k}_{v['dir']}"> Postat</label><div class="act"><button type="button" data-copy="{cid}">Copiază caption</button><a class="dl" href="v/{v['dir']}.mp4" download="{v['dir']}.mp4">Descarcă MP4</a><span class="set">{v['set']}</span></div></div></article>''')
    cols.append(f'<section class="acc"><h2>{ACC[k]} <small><b class="cnt" data-acc="{k}">0</b>/{len(lst)} postate</small></h2>{"".join(cards)}</section>')
tpl=open(f"{R}/board/day_template.html").read()
open(f"{out}/index.html","w").write(tpl.replace("__DAY__",day).replace("__COLS__","".join(cols)).replace("__NC__",str(len(D["accounts"]))).replace("__N__",str(sum(len(l) for l in D['accounts'].values()))))
print(out)
