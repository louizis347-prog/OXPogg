#!/usr/bin/env python3
"""Enxuga os episódios de CONTINUAÇÃO (o = N.5) do inglês: tira exercícios redundantes (mesmo vocabulário em 14 telas) e
remove o quadro 'Por dentro da obra' das originais que já têm 'Cena da obra' (evita contar a mesma coisa 3 vezes).
Uso: python3 tools/cult/trim_cont.py [--dry]"""
import json,glob,re,sys,collections
dry='--dry' in sys.argv
DROP={'soundlab','vplay','cexp','ctxv','wlat','lexpack','balloons'}
st=collections.Counter()
for f in sorted(glob.glob('data/en-*_*.json')):
    d=json.load(open(f));ch=False
    for e in d:
        fr=e.get('fr');o=e.get('o')
        if not fr: continue
        cont=isinstance(o,(int,float)) and (o%1)>0.4
        if cont and len(fr)>=12:
            new=[x for x in fr if x['k'] not in DROP]
            if len(new)>=7 and len(new)<len(fr):
                st['cont enxuta']+=1;st['frames removidos']+=len(fr)-len(new);e['fr']=new;ch=True
        elif not cont and any(x['k']=='cultcena' for x in fr) and any(x['k']=='cultx' for x in fr):
            e['fr']=[x for x in fr if x['k']!='cultx'];st['orig sem cultx']+=1;ch=True
    if ch and not dry: json.dump(d,open(f,'w'),ensure_ascii=False,separators=(',',':'))
print(dict(st))
