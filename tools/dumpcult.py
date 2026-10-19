# -*- coding: utf-8 -*-
# Lista obras ainda sem texto à mão: dumpcult.py cid [ini] [fim]
import json,glob,sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'rdg'))
cid=sys.argv[1];ini=int(sys.argv[2]) if len(sys.argv)>2 else 0;fim=int(sys.argv[3]) if len(sys.argv)>3 else 10**9
import importlib,glob as g
done=set()
for f in g.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)),'rdg','cult_*.py')):
    mod=importlib.import_module(os.path.basename(f)[:-3]);done|=set(mod.C)
it=[]
for f in sorted(glob.glob('data/%s_*.json'%cid)): it+=json.load(open(f))
ms=[x for x in it if not x.get('xof') and x['fr'] and x['fr'][0].get('cw') and x['n'] not in done]
print('faltam',len(ms))
for x in ms[ini:fim]:
    c=x['fr'][0]['cw'];print(x['n'],'|',c['work'],'|',c.get('kind'),'|',c.get('year'),'|',c.get('by'),'|',c['intro'].replace('**','')[:230])
