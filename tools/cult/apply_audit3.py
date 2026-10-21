#!/usr/bin/env python3
"""Aplica tools/cult/kb/audit3_K.json (A2+B1) sobre kb e kb2, validando o esquema. Uso: apply_audit3.py"""
import json,glob,re,collections
V={}
for f in sorted(glob.glob('tools/cult/kb/audit3_[0-9]*.json')):
    try: V.update(json.load(open(f)))
    except Exception as e: print('ERRO lendo',f,e)
files={}
for c in('en-a2','en-b1'):
    for f in sorted(glob.glob('tools/cult/kb/%s_[0-9].json'%c)):
        files[f]=(c,json.load(open(f)),json.load(open(f.replace('/kb/','/kb2/'))))
st=collections.Counter();log=[]
def okcena(c):
    m=c.get('mode');L=c.get('lines') or []
    if m not in('scene','quote','page'):return 'modo'
    if m=='scene':return None if not L else 'scene com linhas'
    if m=='quote' and not 1<=len(L)<=2:return 'quote linhas'
    if m=='page' and not 2<=len(L)<=6:return 'page linhas'
    for l in L:
        if len(l)<2 or not l[0] or not l[1]:return 'linha malformada'
        if m=='quote' and len(l[0].split())>18:return 'fala longa'
    if not c.get('ctx') or not c.get('src'):return 'sem ctx/src'
    for h in c.get('hl') or []:
        if not any(h.lower() in l[0].lower() for l in L):return 'hl fora'
    return None
def okq(q):
    return isinstance(q,dict) and q.get('q') and isinstance(q.get('o'),list) and len(q['o'])==3 and isinstance(q.get('a'),int) and 0<=q['a']<3 and q.get('why')
def ok2(r):
    return isinstance(r,dict) and 330<=len(r.get('intro',''))<=470 and len(r.get('leitura',[]))==2 and all(320<=len(t)<=440 for t in r['leitura']) and len(r.get('facts',[]))>=2
for f,(c,kb,kb2) in files.items():
    for w in kb:
        v=V.get(c+'|'+w)
        if not v: st['sem veredito']+=1;continue
        x=kb[w]
        if isinstance(v.get('y1'),int): x['y1']=v['y1']
        for k in('by','blurb'):
            if v.get(k) and (k!='blurb' or len(v[k])<=130): x[k]=v[k]
        if v.get('cena'):
            e=okcena(v['cena'])
            if not e and v['cena']['mode']!='scene' and not okq(v.get('q')): e='q ruim'
            if e: st['cena rejeitada']+=1;log.append('cena rejeitada %s: %s'%(w,e))
            else:
                x['cena']=v['cena']
                if v['cena']['mode']=='scene': x.pop('q',None)
                else: x['q']=v['q']
                st['cena '+v['cena']['mode']]+=1
        if v.get('kb2'):
            if ok2(v['kb2']): kb2[w].update({k:v['kb2'][k] for k in('intro','leitura','facts')});st['kb2 ok']+=1
            else: st['kb2 rejeitado']+=1;log.append('kb2 rejeitado %s (tamanhos)'%w)
        st['v '+v.get('v','?')]+=1
    json.dump(kb,open(f,'w'),ensure_ascii=False,indent=1);json.dump(kb2,open(f.replace('/kb/','/kb2/'),'w'),ensure_ascii=False,indent=1)
print(dict(st));open('tools/cult/audit3_log.txt','w').write('\n'.join(log));print('\n'.join(log[:12]))
# repetição entre variantes
base=lambda w:re.split(r':| - ',w)[0].strip()
G=collections.defaultdict(list)
for f,(c,kb,kb2) in files.items():
    for w in kb: G[base(w)].append((c,w,kb2[w]))
dup=0
for b,v in G.items():
    if len(v)<2:continue
    seen=collections.Counter()
    for c,w,r in v:
        ss=set()
        for t in [r['intro']]+r['leitura']+r['facts']:
            for s in re.split(r'(?<=[.!?])\s+',t):
                if len(s)>25:ss.add(s.strip())
        seen.update(ss)
    if any(n>1 for n in seen.values()):dup+=1
print('bases com frases repetidas entre variantes:',dup)
