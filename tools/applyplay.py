# -*- coding: utf-8 -*-
# Aplica o formato lúdico (rdgplay) e a nova sequência aos episódios de regras listados em tools/rdg/play_a1.py
import json,glob,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'rdg'))
import reg3 as r,play_a1 as pl
cid='en-a1'
ORDER=['cover','rdgplay','soundlab','pat','wlat','vplay','scenebuild','ctxv','xpr','cexp','scene']
it=[]
for f in sorted(glob.glob('/home/user/OXPogg/data/%s_*.json'%cid)): it+=json.load(open(f))
n=0
for x in it:
    d=pl.P.get(x.get('xof'))
    if not d: continue
    title,turns,rule=d
    cast={0:[pl.M[1],pl.M[2]],1:[pl.S[1],pl.S[2]]}
    step={'k':'rdgplay','title':title,'cast':cast,'turns':turns,'rule':rule,'say':'Complete a conversa tocando na resposta certa. Eu mostro a regra depois!'}
    fr=[s for s in x['fr'] if s['k'] not in('rdg','follow','rdgplay')]
    fr.append(step)
    out=[];used=set()
    for k in ORDER:
        for i,s in enumerate(fr):
            if s['k']==k and i not in used: out.append(s);used.add(i);break
    out+= [s for i,s in enumerate(fr) if i not in used]
    x['fr']=out;x['play']=1;n+=1
tmp='/tmp/_play.json';json.dump(it,open(tmp,'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
r.data(cid,tmp);print('aplicado',n)
