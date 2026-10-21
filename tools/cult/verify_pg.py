#!/usr/bin/env python3
"""Confere se as linhas EN de cada trecho literal existem no texto-fonte. Uso: verify_pg.py ARQUIVO.json  (formato: {obra:{fonte:{repo,id},episodios:{n:{form,lines}}}})"""
import sys,json,re
sys.path.insert(0,'tools/cult')
from pg_extract import fetch,body,norm
def flat(t): return re.sub(r'\s+',' ',norm(t)).strip()
bad=0;ok=0
for w,x in json.load(open(sys.argv[1])).items():
    fo=x.get('fonte')
    for n,e in (x.get('episodios') or {}).items():
        if e.get('form') not in('page','dialogue'):continue
        if not fo:print('SEM FONTE',w,n);bad+=1;continue
        fn,t=fetch(fo['repo'],str(fo['id']))
        if not t:print('FONTE NAO ABRE',w);bad+=1;continue
        src=flat(body(t))
        for l in e['lines']:
            en=flat(l[1])
            if en not in src:print('NAO LITERAL',w,n,en[:80]);bad+=1
            else:ok+=1
print('linhas literais conferidas:',ok,'| problemas:',bad)
