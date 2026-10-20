#!/usr/bin/env python3
"""Enriquece o 'Você sabia?' (culttl) das continuações do inglês com contexto (a regra do episódio) e exemplos reais da leitura."""
import json,glob,re,collections
st=collections.Counter()
strip=lambda s:re.sub(r'\{\{|\}\}|\[\[|\]\]','',s)
def iscont(e):
    o=e.get('o');return isinstance(o,(int,float)) and (o%1)>0.4
for f in sorted(glob.glob('data/en-*_*.json')):
    d=json.load(open(f));ch=False
    for e in d:
        if not iscont(e): continue
        fr=e['fr'];t=next((x for x in fr if x['k']=='culttl'),None)
        if not t: continue
        rd=next((x for x in fr if x['k']=='rdg'),None);rp=next((x for x in fr if x['k']=='rdgplay'),None)
        ex=[]
        if rd and rd.get('s'): ex=[[strip(a),b] for a,b in rd['s'] if len(a.split())>=3][:3]
        elif rp: ex=[[strip(x['t']),x['pt']] for x in rp['turns'] if x.get('t') and x.get('pt')][:3]
        rule=(rd or rp or {}).get('rule')
        if rule: t['ctx']=rule
        if ex: t['ex']=ex
        if rule or ex: ch=True;st['culttl enriquecido']+=1
    if ch: json.dump(d,open(f,'w'),ensure_ascii=False,separators=(',',':'))
print(dict(st))
