import json,glob,sys
lv,start,cnt=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
ONLY_TODO=True
L=[]
for f in sorted(glob.glob('/home/user/OXPogg/data/en-%s_*.json'%lv)):L+=json.load(open(f))
done=set()
import importlib.util,os
for fn in glob.glob('/home/user/OXPogg/tools/draft/readings/b_*.py'):
    sp=importlib.util.spec_from_file_location('x',fn);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);done|=set(m.E)
for fn in glob.glob('/home/user/OXPogg/tools/draft/readings/b_*.txt'):
    for ln in open(fn,encoding='utf-8'):
        if ln.startswith('#'):done.add(int(ln[1:].split()[0]))
shown=0
for i in range(start,len(L)):
    if shown>=cnt:break
    e=L[i];a=e['a']
    if e['n'] in done or any(x['k']=='rdg' and x.get('obra') for x in e['fr']):continue
    shown+=1
    sc=next((x for x in e['fr'] if x['k']=='pgscene'),{})
    cast=list((sc.get('cast') or {}).keys())
    ex=[x.get('en') or x.get('x') for fr in e['fr'] if fr['k']=='pgexp' for x in fr['items']]
    vb=[x['v'] for fr in e['fr'] if fr['k']=='verbs' for x in fr['items']]
    v=[w[0] for w in e['v']]
    print('%d|%s|%s|%s (%s)|cast:%s|V:%s|X:%s|VB:%s|%s'%(i,e['n'],e['t'],a['w'],a['y'],','.join(cast),','.join(v),' / '.join(ex),','.join(vb),a.get('d','')[:150].replace('\n',' ')),'(JÁ FEITO)' if e['n'] in done else '')
