#!/usr/bin/env python3
"""Lista as obras distintas de um curso e divide em blocos: mk_chunks.py CURSO [N=8] -> tools/cult/work/CURSO_chunkK.json"""
import json,glob,sys
cid=sys.argv[1];N=int(sys.argv[2]) if len(sys.argv)>2 else 8
W={}
for f in sorted(glob.glob('data/%s_*.json'%cid)):
    raw=json.load(open(f));d=raw if isinstance(raw,list) else raw.get('eps',[])
    for e in d:
        if (e.get('o') or 0)%1: continue
        for x in e.get('fr',[]):
            if x.get('k')=='cultob':
                w=W.setdefault(x['work'],{'work':x['work'],'chips':x.get('chips',[]),'panel':' '.join(x.get('panels',[])),'eps':[]})
                w['eps'].append(e['t'])
L=sorted(W.values(),key=lambda w:w['work'].lower())
sz=-(-len(L)//N)
for k in range(N):
    c=L[k*sz:(k+1)*sz]
    if c: json.dump(c,open('tools/cult/work/%s_chunk%d.json'%(cid,k),'w'),ensure_ascii=False,indent=1)
print(len(L),'obras em',N,'blocos de',sz)
