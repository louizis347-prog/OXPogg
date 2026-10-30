import json,glob,sys,os,importlib.util
D=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,D)
E_={}
from pilot import R as PR
for n,(s,q) in PR.items():E_[n]={'r':s,'q':q}
for fn in sorted(glob.glob(D+'/d_*.py'))+sorted(glob.glob(D+'/b_*.py')):
    sp=importlib.util.spec_from_file_location('m',fn);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
    for n,v in m.E.items():E_.setdefault(n,{}).update(v)
def load_txt(fn):
    out={};cur=None
    for ln in open(fn,encoding='utf-8'):
        ln=ln.rstrip('\n')
        if not ln.strip():continue
        if ln.startswith('#'):
            cur=int(ln[1:].split()[0]);out[cur]={'r':[],'d':[]};continue
        k,_,rest=ln.partition(':');f=[x.strip() for x in rest.split(' // ')]
        if k=='r':out[cur]['r'].append((f[0],f[1]))
        elif k=='q':out[cur]['q']=(f[0],[f[1],f[2],f[3]],int(f[4]),f[5])
        elif k=='d':out[cur]['d'].append((f[0],f[1],f[2]))
    for v in out.values():
        if not v['d']:del v['d']
        if not v['r']:del v['r']
    return out
for fn in sorted(glob.glob(D+'/b_*.txt')):
    for n,v in load_txt(fn).items():E_.setdefault(n,{}).update(v)
RS=['library','cafe','park','street','office','kitchen','living','bedroom','desk','lobby1','cafe2']
nr=nd=0
for fn in sorted(glob.glob(D+'/../../../data/en-*.json')):
    d=json.load(open(fn));ch=False
    for e in d:
        v=E_.get(e['n'])
        if not v:continue
        fr=e['fr']
        if 'r' in v and not any(x['k']=='rdg' and x.get('obra') for x in fr):
            q,o,a,why=v['q']
            hs=next(x for x in fr if x['k']=='hotscene')
            i=fr.index(hs)+1
            near={fr[j].get('rs') for j in (i-1,i,i+1) if 0<=j<len(fr)}
            f={'k':'rdg','obra':True,'title':'Conheça a obra: '+e['a']['w'],'s':[list(t) for t in v['r']],'q':{'q':q,'o':o,'a':a,'why':why},
               'rs':next(r for r in RS if r not in near),'chars':hs.get('chars'),'say':'Leia a resenha. Toque em uma frase para ouvir e ver a tradução.'}
            fr.insert(i,f);ch=True;nr+=1
        if 'r' in v:
            ex=next((x for x in fr if x['k']=='rdg' and x.get('obra')),None)
            if ex and ex['s']!=[list(t) for t in v['r']]:
                ex['s']=[list(t) for t in v['r']];ch=True;nr+=1
        if 'd' in v and not any(x['k']=='pgdlg' for x in fr):
            vp=next((i for i,x in enumerate(fr) if x['k']=='vplay'),None)
            if vp is None:continue
            sc=next(x for x in fr if x['k']=='pgscene')
            near={fr[j].get('rs') for j in (vp-1,vp,vp+1,vp+2) if 0<=j<len(fr)}
            f={'k':'pgdlg','title':'Diálogo relâmpago','lines':[list(t) for t in v['d']],'rs':next(r for r in RS if r not in near),'chars':sc.get('chars'),'avatar':1,'say':'Troque as peças e ouça a conversa mudar!'}
            fr.insert(vp+1,f)
            lab=next((i for i,x in enumerate(fr) if x['k']=='pglab'),None)
            if lab is not None and lab+1<len(fr) and fr[lab+1]['k']=='pgsheet':del fr[lab+1]
            for j in range(1,len(fr)-1):
                if fr[j-1].get('rs') and fr[j-1].get('rs')==fr[j].get('rs')==fr[j+1].get('rs'):
                    other={fr[k].get('rs') for k in range(max(0,j-2),min(len(fr),j+3))}
                    fr[j]['rs']=next(r for r in RS if r not in other)
            ch=True;nd+=1
    if ch:json.dump(d,open(fn,'w'),ensure_ascii=False,separators=(',',':'))
print('leituras',nr,'diálogos',nd)
