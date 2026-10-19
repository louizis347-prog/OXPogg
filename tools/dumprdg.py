# -*- coding: utf-8 -*-
# Lista as continuações de regras de um curso (xof, título, gramática, regra do 'pat', palavras) para escrever as leituras. Uso: dumprdg.py en-a2 ini fim
import json,glob,sys,re
cid,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
it=[]
for f in sorted(glob.glob('/home/user/OXPogg/data/%s_*.json'%cid)): it+=json.load(open(f))
M={x['n']:x for x in it if not x.get('xof')}
cs=[x for x in it if x.get('xof')]
for x in cs[a:b]:
    m=M.get(x['xof'],{})
    pat=next((s for s in x['fr'] if s['k']=='pat'),{})
    tip=re.sub(r'[*]','',pat.get('tip','') or '')[:230]
    ex=[]
    for s in x['fr']:
        if s['k']=='xpr': ex=[i['x'] if 'x' in i else i['ex'][0] for i in s.get('items',[])][:3]
    print('%s|%s|%s|%s|%s|%s'%(x['xof'],x['t'],(m.get('t') or ''),(x.get('g') or {}).get('t',''),tip,'; '.join(ex)+' || '+', '.join(v[0] for v in x['v'][:6])))
