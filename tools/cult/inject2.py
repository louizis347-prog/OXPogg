#!/usr/bin/env python3
"""Aplica a apresentação rica (tools/cult/kb2) nos episódios: cultob.panels/facts, cultcena.leitura e cartões da linha do tempo.
Uso: python3 tools/cult/inject2.py CURSO"""
import json,glob,sys,collections
cid=sys.argv[1];kb2={};kb={}
for f in sorted(glob.glob('tools/cult/kb2/%s_*.json'%cid)): kb2.update(json.load(open(f)))
for f in sorted(glob.glob('tools/cult/kb/%s_[0-9].json'%cid)): kb.update(json.load(open(f)))
st=collections.Counter();print('obras ricas',len(kb2))
for f in sorted(glob.glob('data/%s_*.json'%cid)):
    d=json.load(open(f));ch=False
    for e in d:
        for x in e.get('fr',[]):
            if x['k']=='cultob' and x['work'] in kb2:
                r=kb2[x['work']];x['panels']=[r['intro']];x['facts']=r['facts'];ch=True;st['cultob']+=1
            elif x['k']=='cultcena' and x['work'] in kb2:
                lt=list(kb2[x['work']]['leitura'])
                if x.get('mode')=='scene' and lt:
                    import re
                    sents=re.split(r'(?<=[.!?])\s+',lt[-1]);
                    if sents and re.search(r'trecho|leia|ler ',sents[-1],re.I): sents[-1]='Repare como a história usa palavras simples do dia a dia.'
                    lt[-1]=' '.join(sents)
                x['leitura']=lt;ch=True;st['cultcena']+=1
            elif x['k']=='culttl':
                for w in x.get('works',[]):
                    r=kb2.get(w['n'])
                    if r: w['d']=r['intro'];w['facts']=r['facts'];ch=True;st['culttl obra']+=1
    if ch: json.dump(d,open(f,'w'),ensure_ascii=False,separators=(',',':'))
print(dict(st))
