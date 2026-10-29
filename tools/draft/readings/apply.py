import json,glob,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from pilot import R
n=0
for fn in sorted(glob.glob('data/en-*.json')):
    d=json.load(open(fn));ch=False
    for e in d:
        if e['n'] in R and not any(x['k']=='rdg' and x.get('obra') for x in e['fr']):
            s,(q,o,a,why)=R[e['n']]
            hs=next(x for x in e['fr'] if x['k']=='hotscene')
            f={'k':'rdg','obra':True,'title':'Conheça a obra: '+e['a']['w'],'s':[[a_,b_] for a_,b_ in s],
               'q':{'q':q,'o':o,'a':a,'why':why},'rs':hs.get('rs'),'chars':hs.get('chars'),
               'say':'Leia a resenha. Toque em uma frase para ouvir e ver a tradução.'}
            i=next(i for i,x in enumerate(e['fr']) if x['k']=='hotscene')+1
            e['fr'].insert(i,f);ch=True;n+=1
    if ch:json.dump(d,open(fn,'w'),ensure_ascii=False,separators=(',',':'))
print(n)
