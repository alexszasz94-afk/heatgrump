import json, subprocess, sys
P='/home/user/heatgrump/output/afnska/princess/'
BR='/home/user/heatgrump/output/afnska/broll/'
H='/home/user/heatgrump/output/afnska/v1955/'
ENG='/home/user/heatgrump/heatgrump-studio/engine/montage.py'
END='Black Friday sale ❄️ link in bio'
def seg(f,a,b): return {"file":f,"start":a,"end":b}
V={
 'v1':dict(audio='DgETW5RH',heart='🖤',name='Midnight 🖤',segs=[seg(H+'hook-v1.mp4',0.5,2.53),seg(P+'gj-v1.mp4',2.70,6.0),seg(BR+'s3-negru-fata21.mp4',2.67,5.5),seg(P+'gj-v1.mp4',10.08,14.0)]),
 'v2':dict(audio='DgETW5RH',heart='🩷',name='Rose 🩷',segs=[seg(P+'gj-v2.mp4',0.0,2.62),seg(P+'gj-v2.mp4',2.66,6.0),seg(BR+'s3-roz-fata24.mp4',2.67,5.5),seg(P+'gj-v2.mp4',10.12,14.0)]),
 'v3':dict(audio='DgETW5RH',heart='🩶',name='Storm 🩶',segs=[seg(P+'gj-v3.mp4',0.0,2.62),seg(P+'gj-v3.mp4',2.70,6.0),seg(BR+'s3-gri-fata25.mp4',2.67,5.5),seg(P+'gj-v3.mp4',10.08,14.0)]),
 'v4':dict(audio='DgAp5s',heart='🩵',name='Frost 🩵',segs=[seg(P+'pc-p1.mp4',0.0,3.1),seg(P+'gj-v4.mp4',3.17,7.05),seg(BR+'s3-bleu-fata23.mp4',2.67,5.5),seg(P+'gj-v4.mp4',10.33,15.0)]),
 'v8':dict(audio='Df2GeK',heart='🖤',name='Midnight 🖤',segs=[seg(P+'pc-p5.mp4',0.0,4.8),seg(P+'gj-v8.mp4',4.87,7.96),seg(BR+'broll-negru.mp4',2.67,5.5),seg(P+'gj-v8.mp4',11.25,16.0)]),
 'v5':dict(audio='DgAp5s',heart='🤎',name=None,segs=[seg(P+'pc-p2.mp4',0.0,4.0),seg(BR+'s3-ciocolatiu-fata22.mp4',0.05,2.62),seg(BR+'s3-ciocolatiu-fata22.mp4',2.67,12.9)]),
 'v6':dict(audio='DgAp5s',heart='❤️',name='Cherry ❤️',segs=[seg(P+'pc-p3.mp4',0.0,4.0),seg(BR+'broll-visiniu.mp4',0.05,2.62),seg(BR+'broll-visiniu.mp4',2.67,6.0),seg(P+'pc-s16.mp4',0.0,4.9)]),
 'v7':dict(audio='Df4sjm',heart='🤍',name='Snow 🤍',segs=[seg(P+'pc-p4.mp4',0.0,4.0),seg(BR+'broll-lapte.mp4',0.05,2.62),seg(BR+'broll-lapte.mp4',2.67,6.0),seg(P+'pc-s17.mp4',0.0,4.9)]),
}
def T(t,a,b,y=0.09,size=62): return {"text":t,"segs":[a,b],"y":y,"size":size}
for k in (sys.argv[1:] or V):
    v=V[k]; n=len(v['segs'])
    if k in ('v5','v6','v7'):
        texts=[T('The princess problem.. 😩',0,0),T('So I made my own.. ✂️🧵',1,1),T(f"The solution 🤩{v['heart']}",2,2)]
        if v['name']: texts.append(T(v['name'],3,3))
    else:
        texts=[T('The princess problem.. 😩',0,0),T('So I started making these.. 🪡✂️🧵',1,1),T(f"The solution 🤩{v['heart']}",2,2),T(v['name'],3,3)]
    texts.append(T(END,n-1,n-1,y=0.80,size=58) if k!='v5' else {"text":END,"t0":11.2,"t1":15.3,"y":0.80,"size":58})
    sp={"segments":v['segs'],"texts":texts,"music":P+f"audio-{v['audio']}.m4a","music_start":0,"music_vol":1.0,"orig_vol":0.0,"out":P+f"frostfemme-princess-{k}.mp4"}
    json.dump(sp,open(P+f'spec-{k}.json','w'),ensure_ascii=False,indent=1)
    r=subprocess.run(['python3',ENG,P+f'spec-{k}.json'],capture_output=True,text=True); print(k,r.returncode,r.stderr[-300:])
