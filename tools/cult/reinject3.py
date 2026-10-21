#!/usr/bin/env python3
"""Atualiza cena (cultcena), linha do tempo (culttl) e cultx dos episódios já injetados, a partir de kb. Uso: reinject3.py CURSO"""
import json,glob,sys,collections
cid=sys.argv[1];kb={};st=collections.Counter()
for f in sorted(glob.glob('tools/cult/kb/%s_[0-9].json'%cid)): kb.update(json.load(open(f)))
for f in sorted(glob.glob('data/%s_*.json'%cid)):
    d=json.load(open(f));ch=False
    for e in d:
        for x in e.get('fr',[]):
            if x['k']=='cultcena' and x['work'] in kb:
                w=kb[x['work']];c=w['cena']
                x.update({'mode':c['mode'],'src':c.get('src',''),'ctx':c['ctx'],'lines':c.get('lines',[]),'hl':c.get('hl',[])})
                if c['mode']!='scene' and w.get('q'): x['q']=w['q']
                else: x.pop('q',None)
                if c['mode']!='scene':
                    for y in e['fr']:
                        if y['k']=='cultx':
                            y['tiles']=[t for t in y['tiles'] if not t.get('en')]
                ch=True;st['cena '+c['mode']]+=1
            elif x['k']=='culttl':
                for wk in x.get('works',[]):
                    w=kb.get(wk['n'])
                    if not w:continue
                    wk['y']=w['y1'];wk['t']=w['kind'].capitalize()
                    L=w['cena'].get('lines') or []
                    if w['cena']['mode']!='scene' and L and len(L[0][0].split())<=14: wk['q']=L[0][0];wk['qp']=L[0][1]
                    else: wk.pop('q',None);wk.pop('qp',None)
                    ch=True
    if ch: json.dump(d,open(f,'w'),ensure_ascii=False,separators=(',',':'))
print(dict(st))
