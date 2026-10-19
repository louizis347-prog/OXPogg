# -*- coding: utf-8 -*-
import json,glob,sys,copy,os,re
sys.path.insert(0,'/tmp/claude-0/-home-user-OXPogg/097f2c11-a1d9-5802-aa7c-396fb7b01940/scratchpad')
import reg3 as r
A_MAIN=['cover','review','read','words','wsent','verbs','scene','dquiz','pat','sbuild','lplay','tdlg','convo','produce']
B_MAIN=['cult1','cover','scene','words','tapimg','match','cquiz','build','grammar','convo','produce','wrap']
XBASE=7000000
def split(fr,fam):
    order=A_MAIN if fam=='A' else B_MAIN
    used=set();main=[]
    for k in order:
        i=next((j for j,s in enumerate(fr) if s['k']==k and j not in used),None)
        if i is not None: used.add(i);main.append(fr[i])
    extras=[s for j,s in enumerate(fr) if j not in used]
    return main,extras
def run(cid):
    it=[]
    for f in sorted(glob.glob('/home/user/OXPogg/data/%s_*.json'%cid)): it+=json.load(open(f))
    if any(x.get('ex') for x in it): print(cid,'ja convertido');return
    out=[];nm=nx=0
    for x in it:
        fr=x.get('fr')
        if not isinstance(fr,list) or len(fr)<15 or x.get('pl'): out.append(x);continue
        ks=[s['k'] for s in fr]
        fam='A' if 'read' in ks and 'words' in ks else ('B' if 'cult1' in ks else None)
        if not fam: out.append(x);continue
        main,extras=split(fr,fam)
        if len(extras)<2: out.append(x);continue
        o=x.get('o',x['n'])
        c=copy.deepcopy(x);c['n']=XBASE+x['n'];c['t']=x['t']+' · Mais treino';c['s']='Regras, sons e expressões do episódio'
        c['o']=o+0.5;c['ex']=1;c['xof']=x['n'];c['en']='＋'
        cov=next((s for s in fr if s['k']=='cover'),None)
        steps=[]
        if cov:
            cc=copy.deepcopy(cov);cc['sub']='Mais treino · regras, sons e padrões';cc['say']='Mais treino! Aqui reforçamos as regras, os sons e os padrões do episódio.';cc.pop('cw',None);steps.append(cc)
        steps+=[s for s in extras if s['k']!='cover']
        c['fr']=steps;c['p']='Mais treino: regras, sons e padrões de '+x['t']+'.'
        x['fr']=main;x['xn']=c['n'];x['lean']=1
        out.append(x);out.append(c);nm+=1;nx+=len(steps)
    tmp='/tmp/_lean_%s.json'%cid;json.dump(out,open(tmp,'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    n=r.data(cid,tmp)
    cn=json.load(open('/home/user/OXPogg/data/counts.json'));cn[cid]=sum(1 for x in out if not x.get('ex'));json.dump(cn,open('/home/user/OXPogg/data/counts.json','w'),ensure_ascii=False)
    print(cid,'convertidos',nm,'itens',n,'passos extras',nx)
if __name__=='__main__':
    for c in sys.argv[1:]: run(c)
