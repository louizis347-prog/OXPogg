#!/usr/bin/env python3
"""Insere o quadro cultpg (Página da obra) nos episódios de um curso a partir de tools/cult/work/pg_CURSO_outK.json.
Uso: inject_pg.py CURSO [--dry]   (ex.: en-a1). Originais: depois de cultcena. Continuações: depois de culttl. Idempotente."""
import json,glob,sys,collections
cid=sys.argv[1];dry='--dry' in sys.argv
short=cid.replace('en-','')
OUT={}
for f in sorted(glob.glob('tools/cult/work/pg_%s_out[0-9]*.json'%short)): OUT.update(json.load(open(f)))
kb={}
for f in sorted(glob.glob('tools/cult/kb/%s_[0-9].json'%cid)): kb.update(json.load(open(f)))
# mapa episódio -> (obra, dados)
EPS={}
for w,x in OUT.items():
    for n,e in (x.get('episodios') or {}).items(): EPS[str(n)]=(w,x.get('fonte'),e)
files=sorted(glob.glob('data/%s_*.json'%cid));allep={}
raw={}
for f in files:
    d=json.load(open(f));raw[f]=d
    for e in d: allep[e['o']]=e
st=collections.Counter()
for f,d in raw.items():
    ch=False
    for e in d:
        k=str(e['n'])
        if k not in EPS: continue
        w,fo,p=EPS[k]
        par=allep[int(e['o'])]
        ob=next((x for x in par['fr'] if x['k']=='cultob'),{})
        cc=next((x for x in par['fr'] if x['k']=='cultcena'),{})
        e['fr']=[x for x in e['fr'] if x['k']!='cultpg']
        fr={'k':'cultpg','title':'Página da obra','work':w,'tag':cc.get('tag') or (ob.get('chips') or [''])[0],'part':1 if e['o']%1==0 else 2,
            'about':kb[w]['blurb'] if w in kb else '', 'form':p['form'],'src':p.get('src',''),'ctx':p.get('ctx',''),'lines':p['lines'],'qs':p['qs']}
        if ob.get('pa'): fr['pa']=ob['pa']
        if fo and p['form'] in('page','dialogue'): fr['ref']=fo
        ks=[x['k'] for x in e['fr']]
        if e['o']%1==0:
            i=(ks.index('cultcena')+1) if 'cultcena' in ks else (ks.index('cultob')+1 if 'cultob' in ks else 1)
        else:
            i=(ks.index('culttl')+1) if 'culttl' in ks else 1
        e['fr'].insert(i,fr);ch=True;st[p['form']]+=1
    if ch and not dry: json.dump(d,open(f,'w'),ensure_ascii=False,separators=(',',':'))
print(dict(st),'episódios com página:',sum(st.values()))
