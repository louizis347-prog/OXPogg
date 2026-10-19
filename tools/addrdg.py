# -*- coding: utf-8 -*-
# Insere leituras ("rdg") escritas em tools/rdg/<prefixo>_NN.py nos episódios de regras (xof = n do principal).
import json,glob,sys,os,importlib
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import reg3 as r
cid,prefix=sys.argv[1],sys.argv[2]
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'rdg'))
D={}
for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)),'rdg',prefix+'_*.py'))):
    D.update(importlib.import_module(os.path.basename(f)[:-3]).D)
it=[]
for f in sorted(glob.glob('/home/user/OXPogg/data/%s_*.json'%cid)): it+=json.load(open(f))
n=0
for x in it:
    d=D.get(x.get('xof'))
    if not d or x.get('play'): continue
    title,rule,lines,q,opts,a,why=d
    step={'k':'rdg','title':'Leitura: '+title,'s':[[e,p] for e,p in lines],'rule':rule,'q':{'q':q,'o':opts,'a':a,'why':why},'say':'Leia, toque nas frases para ouvir e ver a tradução. Depois, uma perguntinha!'}
    x['fr']=[s for s in x['fr'] if s['k']!='rdg']
    ks=[t['k'] for t in x['fr']]
    i=(ks.index('culttl')+1) if 'culttl' in ks else (1 if ks and ks[0]=='cover' else 0)
    x['fr'].insert(i,step);x['rdg']=1;n+=1
tmp='/tmp/_rdg_%s.json'%cid;json.dump(it,open(tmp,'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
r.data(cid,tmp);print(cid,'leituras',n,'de',len(D))
