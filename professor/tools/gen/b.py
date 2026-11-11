import sys;sys.path.insert(0,'/tmp/gen')
from compact import *
GEN=[[('Hello! Can I help you?','Olá! Posso ajudar?','Yes, please.'),('Hi! What do you need?','Oi! O que você precisa?','Okay.')],
[('Sure, one moment.','Claro, um momento.','Thank you.'),('Let me check.','Deixe-me ver.','Okay.')],
[('Here you go.','Aqui está.','Thanks.'),('No problem at all.','Sem problema.','Okay.')],
[('Is that all?','É só isso?','Yes, that is all.'),('Anything else?','Mais alguma coisa?','No, thanks.')]]
def run(N,reg,title,city,npc,you,face,g,yg,crole,sc,pool,story,p,mission,emo,teaser,teaser_d,badge,lines,open,close,rtitle,gloss,fast,scan,tf,order,ctx,chunks,think,cu,errors,homework,hw,lab,cards,molds,sounds,change,wtask,wmodel,kw,verbs,swaps,mini,vocab,ex_idx,real,key):
    L=lines
    ex=[(L[i][1],L[i][2],L[i][1],n) for i,n in zip(ex_idx[0],ex_idx[1])]
    role=[[(L[i][1],L[i][2],L[i+1][1])]+GEN[k] for k,i in enumerate((0,2,4,6))]
    m=dict(reg=reg,title=title,city=city,npc=npc,you=you,face=face,g=g,yg=yg,crole=crole,sc=sc,pool=pool,story=story,p=p,mission=mission,emo=emo,teaser=teaser,teaser_d=teaser_d,badge=badge,lines=L,open=open,close=close,rtitle=rtitle,gloss=gloss,fast=fast,scan=scan,tf=tf,order=order,ctx=ctx,chunks=chunks,think=think,cu=cu,errors=errors,homework=homework,hw=hw,lab=lab,cards=cards,key=key,vocab=vocab,molds=molds,sounds=sounds,role=role,change=change,wtask=wtask,wmodel=wmodel,kw=kw,verbs=verbs,exprs=ex,real=real,swaps=swaps,mini=mini)
    compact(N,m)
