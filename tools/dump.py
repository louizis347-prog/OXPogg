import json,glob,sys
cid=sys.argv[1];a=int(sys.argv[2]);b=int(sys.argv[3])
it=[]
for f in sorted(glob.glob('data/%s_*.json'%cid)): it+=json.load(open(f))
mains=[x for x in it if not x.get('xof')]
for x in mains[a:b]:
    pat=next((s.get('title') for s in x.get('fr',[]) if s['k']=='pat'),'')
    print(x['n'],'|',x['t'],'|',', '.join(v[0] for v in x.get('v',[])),'|',(x.get('g') or {}).get('t',''),'|',pat)
