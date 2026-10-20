#!/usr/bin/env python3
"""Injeta o quadro cultcena e enriquece a linha do tempo (culttl) com a base de obras.
Uso: python3 tools/cult/inject.py CURSO [--dry]   (ex.: en-a1; lê tools/cult/kb/CURSO_*.json)"""
import json,glob,sys,re,collections
cid=sys.argv[1];dry='--dry' in sys.argv
kb={}
for f in sorted(glob.glob('tools/cult/kb/%s_*.json'%cid)): kb.update(json.load(open(f)))
print('obras na base',len(kb))
st=collections.Counter()
for f in sorted(glob.glob('data/%s_*.json'%cid)):
    raw=json.load(open(f));isl=isinstance(raw,list);d=raw if isl else raw.get('eps',[])
    ch=False
    for e in d:
        fr=e.get('fr') or []
        ob=next((x for x in fr if x.get('k')=='cultob'),None)
        cx=next((x for x in fr if x.get('k')=='cultx'),None)
        if ob and ob['work'] in kb and not any(x.get('k')=='cultcena' for x in fr):
            w=kb[ob['work']];c=w['cena']
            link=None
            if cx:
                for t in list(cx['tiles']):
                    if t.get('l')=='Ligação com a lição': link=t.get('t');cx['tiles'].remove(t)
                    elif t.get('en') and c['mode']!='scene': cx['tiles'].remove(t)  # a fala agora tem quadro próprio
            fc={'k':'cultcena','title':'Cena da obra','work':ob['work'],'tag':(cx or {}).get('tag') or (ob['chips'][0] if ob.get('chips') else ''),
                'mode':c['mode'],'src':c.get('src',''),'ctx':c['ctx'],'lines':c.get('lines',[]),'hl':c.get('hl',[]),'q':w['q']}
            if link: fc['link']=link
            if ob.get('pa'): fc['pa']=ob['pa']
            i=fr.index(cx)+1 if cx else fr.index(ob)+1
            fr.insert(i,fc);ch=True;st['cultcena '+c['mode']]+=1
        for x in fr:
            if x.get('k')=='culttl':
                for wk in x.get('works',[]):
                    w=kb.get(wk['n'])
                    if not w: st['culttl obra sem base']+=1;continue
                    wk['y']=w['y1'];wk['d']=w['blurb'];wk['t']=(wk['k']+' '+w['kind'].capitalize())
                    L=w['cena'].get('lines') or []
                    if w['cena']['mode']!='scene' and L and len(L[0][0].split())<=14: wk['q']=L[0][0];wk['qp']=L[0][1]
                    else: wk.pop('q',None);wk.pop('qp',None)
                    ch=True;st['culttl obra ok']+=1
    if ch and not dry:
        json.dump(raw,open(f,'w'),ensure_ascii=False,separators=(',',':'))
print(dict(st))
