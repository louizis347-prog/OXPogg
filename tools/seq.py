# -*- coding: utf-8 -*-
import json,glob,sys,os,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import reg3 as r
RDG='/tmp/rdg'
def words(x):
    out=[];seen=set()
    for v in x.get('v') or []:
        w=v[0].strip() if isinstance(v,list) and v else ''
        if re.fullmatch(r"[A-Za-zÀ-ÿ']{3,9}",w) and w.lower() not in seen:
            seen.add(w.lower());out.append({'w':w,'m':v[1] if len(v)>1 else '','s':w})
    return out[:3]
def run(cid):
    it=[]
    for f in sorted(glob.glob('/home/user/OXPogg/data/%s_*.json'%cid)): it+=json.load(open(f))
    rd={}
    p=os.path.join(RDG,cid+'.json')
    if os.path.exists(p): rd={int(k):v for k,v in json.load(open(p)).items()}
    nx=nr=nw=0
    for x in it:
        x.pop('en',None)
        if not x.get('ex'): continue
        x.pop('ex');nx+=1
        x['t']=x['t'].replace('· Mais treino','· Regras e padrões')
        x['s']='Regras, sons e padrões do episódio anterior'
        x['p']='Regras e padrões de '+x['t'].split(' · ')[0]+': leitura, sons, expressões e escrita na tela.'
        fr=x['fr'];cov=[s for s in fr if s['k']=='cover'];rest=[s for s in fr if s['k']!='cover']
        if cov: cov[0]['sub']='Regras e padrões';cov[0].setdefault('hook',[(x.get('h') or {}).get('l') or (x.get('v') or [['','']])[0][0],(x.get('h') or {}).get('tr') or (x.get('v') or [['','']])[0][1]]);cov[0]['say']='Episódio de regras e padrões! Aqui você entende o porquê do que acabou de aprender.'
        new=[]
        m=rd.get(x['xof'])
        if m: new.append(m);nr+=1
        # ordem: som, expressões, curinga, padrão ... escrita ... resto
        pri=['soundlab','sound','cexp','xpr','grammar','pat']
        first=[s for k in pri for s in rest if s['k']==k]
        others=[s for s in rest if s not in first]
        w=words(x)
        wl={'k':'wlat','title':'Escreva na tela','items':w,'say':'Vamos escrever com o dedo? Trace e depois escreva de memória.'} if len(w)>=2 else None
        steps=cov+new+first+([wl] if wl else [])+others
        if wl: nw+=1
        x['fr']=steps;x['xsteps']=len(steps)
    tmp='/tmp/_seq_%s.json'%cid;json.dump(it,open(tmp,'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    n=r.data(cid,tmp)
    cn=json.load(open('/home/user/OXPogg/data/counts.json'));cn[cid]=len(it);json.dump(cn,open('/home/user/OXPogg/data/counts.json','w'),ensure_ascii=False)
    print(cid,'episódios de regras',nx,'leituras',nr,'escrita',nw,'itens',n,'counts',cn[cid])
if __name__=='__main__':
    for c in sys.argv[1:]: run(c)
