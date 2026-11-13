import sys;sys.path.insert(0,'/tmp/gen');sys.path.insert(0,'/tmp/a2')
from compact import *
from plan import P as PLAN
def A2(k,d):
    row=PLAN[k-1];title,city,npc,you,struct,sc=row
    nxt=PLAN[k][0] if k<len(PLAN) else 'Próxima etapa'
    L=[(('You' if w=='Y' else npc),e,p) for w,e,p in d['L']]
    gl=d['gl']; gloss=[(g[0],g[1]) for g in gl]; vocab=[(g[0],g[1],g[2],g[3],g[4]) for g in gl[:6]]
    ctx=[]
    for i in range(3):
        w,pt=gl[i][0],gl[i][1]; oth=[g[1] for g in gl[3:] if g[1]!=pt][:2]
        ctx.append((w.capitalize()+'.',w,[pt]+oth,w+' = '+pt+'.'))
    ex=d['ex']; exprs=[(e[0],e[1],L[e[2]][1],e[3]) for e in ex]
    chunks=[e[0] for e in ex[:5]]
    role=[]
    for i in (0,2,4,6):
        n_=L[i]; y=L[i+1]
        role.append([(n_[1],n_[2],y[1]),('Really?','Mesmo?','Yes, really.'),('I see.','Entendi.','Okay.')])
    m=dict(reg=k,title=title,city=city,npc=npc,you=you,face=d['face'],g=d['g'],yg=d['yg'],crole=d['crole'],sc=sc,pool=d.get('pool') or [sc,'street','cafe2','park'],
     story=d['story'],p=d['p'],mission=d['mission'],emo=d['emo'],teaser=nxt,teaser_d=d.get('td','Próxima situação'),badge=d['badge'],
     lines=L,open=d['O'],close=d['C'],rtitle=d['rt'],gloss=gloss,fast=d['fast'],scan=d['scan'],tf=d['tf'],order=d['order'],ctx=ctx,chunks=chunks,think=d['think'],
     cu=d['cu'],errors=d['err'],homework=d['hw'],hw=d['hwf'],lab=d['lab'],cards=d['cards'],key=d['key'],vocab=vocab,molds=d['mo'],sounds=d['so'],role=role,change=d['chg'],
     wtask=d['wt'][0],wmodel=d['wt'][1],kw=d['wt'][2],verbs=[tuple(x) if not isinstance(x,str) else vb_(x) for x in d['vb']],exprs=exprs,real=d['real'],swaps=d['sw'],mini=list(d['sw'])[:4])
    for i,s in d['sw'].items():
        if s[0] not in L[i][1] or s[2] not in L[i][2]: print('SWAP?',k,i,s[0] in L[i][1],s[2] in L[i][2])
    for g in gl:
        if g[0].lower() not in (' '.join(e for e,_ in sum([list(x) for x in [d['O'],d['C']]],[]))+' '.join(l[1] for l in L)).lower(): print('GLOSS?',k,g[0])
    for g in gl[:6]:
        if g[0].lower() not in g[4].lower(): print('VOCABEX?',k,g[0])
    for mo in d['mo']:
        f=mo[1]
        for key,opts in mo[2]: f=f.replace('{'+key+'}',opts[0])
        if f!=mo[3]: print('MOLD?',k,f,'|',mo[3])
    compact(2000+k,m)
def vb_(s):
    v,ic,pt,past,p1,p3,pp,pg=s.split('|')
    third=v+'es' if v.endswith(('s','sh','ch','x','o')) else (v[:-1]+'ies' if v.endswith('y') and v[-2] not in 'aeiou' else v+'s')
    ing=(v[:-1] if v.endswith('e') and not v.endswith('ee') else v)+'ing'
    if v in('run','stop','get','swim','sit','plan','shop'): ing=v+v[-1]+'ing'
    return (v,ic,pt,'%s = %s. Passado: %s.'%(v.capitalize(),pt,past),third,past,ing,p1,p3,pp,pg)
