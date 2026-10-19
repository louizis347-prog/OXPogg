# -*- coding: utf-8 -*-
# Lista as continuações ainda sem leitura em tools/rdg/<prefixo>_*.py. Uso: dumpmiss.py en-c1 c1 [n] [largura]
import json,glob,sys,os,importlib,re
cid,prefix=sys.argv[1],sys.argv[2];n=int(sys.argv[3]) if len(sys.argv)>3 else 60;w=int(sys.argv[4]) if len(sys.argv)>4 else 200
H=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,os.path.join(H,'rdg'))
D={}
for f in sorted(glob.glob(os.path.join(H,'rdg',prefix+'_*.py'))): D.update(importlib.import_module(os.path.basename(f)[:-3]).D)
it=[]
for f in sorted(glob.glob(os.path.join(H,'..','data','%s_*.json'%cid))): it+=json.load(open(f))
miss=[x for x in it if x.get('xof') and x['xof'] not in D]
print('faltam',len(miss))
for x in miss[:n]:
    pat=next((s for s in x['fr'] if s['k']=='pat'),{})
    tip=re.sub(r'[*]','',pat.get('tip','') or '')[:w]
    ex=[]
    for s in x['fr']:
        if s['k']=='xpr': ex=[i['x'] if 'x' in i else i['ex'][0] for i in s.get('items',[])][:3]
    print('%s|%s|%s|%s|%s'%(x['xof'],x['t'],(x.get('g') or {}).get('t',''),tip,'; '.join(ex)))
