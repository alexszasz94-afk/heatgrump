import json
A='/home/user/heatgrump/output/afnska/'
B={'bleu':A+'r3-1080/v-genjutsu-graded.mp4','roz':A+'r3-1080/v-genjutsu-roz-graded.mp4','visiniu':A+'broll/broll-visiniu.mp4','lapte':A+'broll/broll-lapte.mp4','negru':A+'broll/broll-negru.mp4','ciocolatiu':A+'broll/broll-ciocolatiu.mp4'}
N={'bleu':'Light Blue 🩵','roz':'Pink 🩷','visiniu':'Burgundy ❤️','lapte':'Milk 🤍','negru':'Black 🖤','ciocolatiu':'Chocolate 🤎'}
SOL=[(2.72,3.50),(4.42,5.25),(7.55,8.45),(11.22,12.50)]
PAR=[(8.58,9.63),(8.58,9.63),(6.10,7.15),(11.22,12.57)]
H=[('hook8',2.7,'hook1','bleu',['roz','visiniu','lapte','negru'],'The problem 🥶😣','The solution 🥹💙'),
   ('hook9',2.25,'hook4','lapte',['ciocolatiu','roz','bleu','negru'],'The problem 🥶😩','The solution 🥹🤍'),
   ('hook10',1.7,'hook2','roz',['bleu','visiniu','ciocolatiu','lapte'],'The problem.. 😩','The solution 🥹🩷')]
for h,P,ub,sol,par,t1,t2 in H:
    seg=[{'file':A+h+'/gen-hook.mp4','start':0,'end':P},{'file':A+ub+'/gen-unbox.mp4','start':0.75,'end':2.25}]
    seg+=[{'file':B[sol],'start':a,'end':b} for a,b in SOL]
    seg+=[{'file':B[c],'start':a,'end':b} for c,(a,b) in zip(par,PAR)]
    tx=[{'text':t1,'segs':[0,0],'y':0.46,'size':62},{'text':'Vs..','segs':[1,1],'y':0.46,'size':62},{'text':t2,'segs':[2,5],'y':0.46,'size':62}]
    tx+=[{'text':N[c],'segs':[6+i,6+i],'y':0.46,'size':62} for i,c in enumerate(par)]
    tx+=[{'text':'Comment COAT for the link '+N[par[-1]].split()[-1],'segs':[9,9],'y':0.56,'size':54}]
    json.dump({'segments':seg,'texts':tx,'music':A+h+'/audio.m4a','music_start':0,'music_vol':1.0,'out':A+h+f'/frostfemme-{h}.mp4'},open(A+h+'/spec.json','w'),indent=1,ensure_ascii=False)
print('ok')
