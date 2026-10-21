#!/usr/bin/env python3
"""Monta os lotes da auditoria 3 (A2+B1): agrupa variantes da mesma obra-base num mesmo lote.
Uso: build_audit3.py [N=17] -> tools/cult/work/audit3_lotK.json"""
import json,glob,re,sys
N=int(sys.argv[1]) if len(sys.argv)>1 else 17
base=lambda w:re.split(r':| - ',w)[0].strip()
items={}
for c in ('en-a2','en-b1'):
    ch={}
    for f in sorted(glob.glob('tools/cult/work/%s_chunk[0-9].json'%c)):
        for w in json.load(open(f)): ch[w['work']]=w
    kb={};kb2={}
    for f in sorted(glob.glob('tools/cult/kb/%s_[0-9].json'%c)): kb.update(json.load(open(f)))
    for f in sorted(glob.glob('tools/cult/kb2/%s_[0-9].json'%c)): kb2.update(json.load(open(f)))
    for w,x in kb.items():
        items['%s|%s'%(c,w)]={'id':'%s|%s'%(c,w),'curso':c,'obra':w,'base':base(w),'chips':ch.get(w,{}).get('chips'),'episodios':ch.get(w,{}).get('eps'),'kb':x,'kb2':kb2[w]}
G={}
for k,v in items.items(): G.setdefault(v['base'],[]).append(v)
groups=sorted(G.values(),key=lambda g:-len(g))
lots=[[] for _ in range(N)];sz=[0]*N
for g in groups:
    i=sz.index(min(sz));lots[i]+=g;sz[i]+=len(g)
for i,l in enumerate(lots): json.dump(l,open('tools/cult/work/audit3_lot%d.json'%i,'w'),ensure_ascii=False,indent=1)
print(len(items),'chaves em',N,'lotes:',sz)
