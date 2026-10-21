#!/usr/bin/env python3
"""Aplica a verificação independente (kb/verify_K.json) sobre a base (kb/CURSO_K.json). Uso: apply_verify.py CURSO"""
import json,glob,sys,collections
cid=sys.argv[1];st=collections.Counter();log=[];kb2fix={}
for f in sorted(glob.glob('tools/cult/kb/%s_[0-9].json'%cid)):
    k=f.split('_')[-1].split('.')[0];vf='tools/cult/kb/verify_%s_%s.json'%(cid,k)
    import os
    if not os.path.exists(vf): vf='tools/cult/kb/verify_%s.json'%k
    try: V=json.load(open(vf))
    except Exception: print('sem verificação para',f);continue
    kb=json.load(open(f))
    for n,w in kb.items():
        v=V.get(n)
        if not v: st['sem veredito']+=1;continue
        if v.get('y1') and isinstance(v['y1'],int) and v['y1']!=w['y1']: log.append('ano %s: %s -> %s'%(n,w['y1'],v['y1']));w['y1']=v['y1']
        if v['v']=='drop':
            c=w['cena'];c['mode']='scene';c['lines']=[];c['hl']=[];c.pop('src',None);w.pop('q',None);st['drop']+=1;log.append('drop %s: %s'%(n,v.get('why','')))
        elif v['v']=='fix':
            if v.get('lines'): w['cena']['lines']=v['lines']
            st['fix']+=1;log.append('fix %s: %s'%(n,v.get('why','')))
        else: st['ok']+=1
        if v.get('kb2'): kb2fix[n]=v['kb2']
    json.dump(kb,open(f,'w'),ensure_ascii=False,indent=1)
print(dict(st));open('tools/cult/verify_log_%s.txt'%cid,'w').write('\n'.join(log));print('\n'.join(log[:15]))

# correções do texto rico (kb2): aplicadas por tools/cult/apply_kb2fix.py
json.dump(kb2fix,open('tools/cult/kb2/fix_%s.json'%cid,'w'),ensure_ascii=False,indent=1)
