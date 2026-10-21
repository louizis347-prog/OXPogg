#!/usr/bin/env python3
"""Aplica tools/cult/kb/risk_audit_K.json: remove frases não confirmadas (ou troca pela versão corrigida) nos kb2 (A2+B1)."""
import json,glob,re,collections
A={}
for f in sorted(glob.glob('tools/cult/kb/risk_audit_[0-9]*.json')): A.update(json.load(open(f)))
st=collections.Counter();short=[]
files={}
for c in('en-a2','en-b1'):
    for f in sorted(glob.glob('tools/cult/kb2/%s_[0-9].json'%c)): files[f]=(c,json.load(open(f)))
def split(t): return [s for s in re.split(r'(?<=[.!?])\s+',t) if s.strip()]
def fix(t,rem,cor):
    out=[]
    for s in split(t):
        hit=next((p for p in cor if s.startswith(p) or p in s),None)
        if hit: out.append(cor[hit]);st['corrigida']+=1;continue
        if any(s.startswith(p) or p in s for p in rem): st['removida']+=1;continue
        out.append(s)
    return ' '.join(out)
for f,(c,d) in files.items():
    for w,r in d.items():
        a=A.get(c+'|'+w)
        if not a: continue
        rem=[p for p in a.get('remover',[]) if len(p)>20];cor=a.get('corrigir') or {}
        r['intro']=fix(r['intro'],rem,cor)
        r['leitura']=[fix(t,rem,cor) for t in r['leitura']]
        r['facts']=[x for x in (fix(t,rem,cor) for t in r['facts']) if x]
        if len(r['intro'])<200 or any(len(t)<120 for t in r['leitura']) or len(r['facts'])<1: short.append((c,w,len(r['intro']),[len(t) for t in r['leitura']],len(r['facts'])))
    json.dump(d,open(f,'w'),ensure_ascii=False,indent=1)
print(dict(st),'| itens que ficaram curtos:',len(short))
for s in short[:12]:print(s)
