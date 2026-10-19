# -*- coding: utf-8 -*-
# uso: python3 chk_arc.py <arquivo sem .py> <EPSnn> ; lista TODOS os problemas de uma vez
import sys,re,importlib
sys.path.insert(0,'.')
mod,name=sys.argv[1],sys.argv[2]
eps=getattr(importlib.import_module(mod),name)
ja=mod.startswith('j')
def n(x): return re.sub(r"[¡!¿?.,:;«»“”\"'’‘\s。、！？]","",x).lower()
bad=0
def P(*a):
    global bad;bad+=1;print(*a)
for e in eps:
    N=e['n']
    if len(e['v'])!=6:P(N,'v!=6')
    if len(e['chat'])!=11:P(N,'chat!=11',len(e['chat']))
    if len(e['chat2'])!=6:P(N,'chat2!=6',len(e['chat2']))
    if len(e['slang'][2])!=6:P(N,'slang!=6')
    if len(e['tap'])!=3:P(N,'tap!=3')
    if not e['chat'][0].startswith('P:') or not e['chat'][-1].startswith('P:'):P(N,'chat deve começar/terminar com P')
    for i,l in enumerate(e['chat']):
        if not l.startswith('P: ' if i%2==0 else 'Y: '):P(N,'chat alternância linha',i,l[:20])
        if l.count(' | ')!=(2 if ja else 1):P(N,'segmentos chat',i,l[:40])
    for i,l in enumerate(e['chat2']):
        if not l.startswith('Y: ' if i%2==0 else 'P: '):P(N,'chat2 alternância',i)
        if l.count(' | ')!=(2 if ja else 1):P(N,'segmentos chat2',i,l[:40])
    for i,l in enumerate(e['slang'][2]):
        if l.count(' | ')!=(2 if ja else 1):P(N,'segmentos slang',i,l[:40])
    for t in e['tap']:
        q,qp,o,a,li,why=t
        if a!=0 or not(0<=li<9) or len(o)!=3:P(N,'tap campos',t[:2])
        quote=re.findall(r"“(.+?)”",why)
        line=e['chat'][li].split(' | ')[0].lower()
        w2=re.findall(r"\w+"," ".join(quote).lower())[:2]
        if not any(w in line for w in w2):P(N,'tap why não bate com a linha',li,why,'|',e['chat'][li][:60])
    tip,pages=e['swap']
    if len(pages)!=2:P(N,'swap páginas')
    for p in pages:
        if len(p[1])!=3 or len(p[2])!=3:P(N,'swap 3x3',p[0])
        if not re.fullmatch(r"[\s.,!?¡¿:;…。！？、]*",p[3] or ''):P(N,'swap fim não é pontuação',p[3])
    gl=e['slang'][3];lines=[l.split(' | ')[0].lower() for l in e['slang'][2]]
    spans=[[] for _ in lines]
    for k in gl:
        ok=False
        for c in [k,re.sub(r"\s*[!?.,？！。]+\s*$","",k)]:
            if ok or not c:continue
            for i,l in enumerate(lines):
                j=l.find(c.lower())
                if j<0:continue
                a,b=j,j+len(c)
                if any(not(b<=x or a>=y) for x,y in spans[i]):continue
                spans[i].append((a,b));ok=True;break
        if not ok:P(N,'glosa não aparece',repr(k))
    if len(gl)!=5:P(N,'gl!=5',len(gl))
    for k in e['slang'][4]:
        if k not in gl:P(N,'chave final fora do dicionário',k)
    if e['real'][0]==e['real'][1]:P(N,'real igual')
    if len(e['mission'])<5 or '|' not in e['hook']:P(N,'hook/mission')
print('PROBLEMAS:',bad,'em',len(eps),'episódios')
