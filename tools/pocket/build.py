#!/usr/bin/env python3
"""Pocket: gera data/pk-<nivel>_NN.json a partir de tools/pocket/<nivel>_arcoNN.py e atualiza manifest/counts."""
import json,glob,importlib.util,os,sys,re
R=os.path.dirname(os.path.abspath(__file__));D=os.path.join(R,'..','..','data')
GR=[('#FF8A5B','#FFC857'),('#2EC4B6','#3A86FF'),('#B388FF','#FF6FB5'),('#43D17A','#2EC4B6'),('#FF7A7A','#FFB84D')]
BASE={'a1':950000,'a2':951000,'b1':952000,'b2':953000,'c1':954000,'c2':955000}
def load(fn):
    sp=importlib.util.spec_from_file_location('m',fn);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def episode(lv,arc_i,k,x,base,order):
    n=base+order;g=GR[arc_i%len(GR)];who=x['who']
    name,gender,face,role=who
    face=face.replace('🧑','👨' if gender=='m' else '👩')
    fr=[
     dict(k='pkhero',g=list(g),num=order,lvl=lv.upper(),face=face,name=name,city=x['city'],sub=x['s'],mission=x['mission'],hook=list(x['key']),boss=bool(x.get('boss'))),
     dict(k='pkdlg',g=list(g),title='Diálogo',lines=[list(l) for l in x['dlg']],vocab=[list(v) for v in x['vocab']],cast={name:[face,g[0]],'You':['🙂','#e85d75']}),
     dict(k='pkbuild',g=list(g),title='Monte a frase',items=[dict(en=b['en'],pt=b['pt'],opts=[list(o) for o in b['opts']]) for b in x['build']]),
     dict(k='pkspeak',g=list(g),title='Fale',items=[dict(who=s['who'],line=list(s['line']),target=s['target'],pt=s['pt']) for s in x['speak']]),
     dict(k='wrap',title='Mochila do episódio',recap=[list(r) for r in x['recap']],expr=list(x['expr']),culture=x['culture'],teaser=dict(t=x['teaser'],d=''),
          sticker=dict(name=name,face=face,role=role,city=x['city'],boss=bool(x.get('boss')))),
    ]
    return dict(n=n,o=n,t=x['t'],s=x['s'],sc=x['sc'],lv=lv.upper(),a=dict(k='Situação',w=x['t'],y='',d=x['culture']),
      h=dict(l=x['dlg'][0][1],src='Pocket',tr=x['dlg'][0][2]),p=x['mission'],g=dict(t=x['key'][0]),v2=True,
      v=[[v[0],v[1],''] for v in x['vocab']],presentation='pocket-v1',pocket=1,
      character=dict(id='pk_'+name.lower(),name=name,gender=gender,role=role,city=x['city'],recurring=True),
      arc=dict(i=arc_i+1,pos=k+1,of=10),fr=fr)
def main():
    out={}
    for lv in BASE:
        files=sorted(glob.glob(os.path.join(R,lv+'_arco*.py')))
        if not files:continue
        eps=[];order=0
        for ai,fn in enumerate(files):
            m=load(fn)
            for k,x in enumerate(m.EPS):
                order+=1;eps.append(episode(lv,ai,k,x,BASE[lv],order))
        # 1 arquivo por 50 episódios
        names=[]
        for bi in range(0,len(eps),50):
            nm='pk-%s_%02d.json'%(lv,bi//50+1);names.append(nm)
            json.dump(eps[bi:bi+50],open(os.path.join(D,nm),'w'),ensure_ascii=False,separators=(',',':'))
        out['pk-'+lv]=(names,len(eps))
    man=json.load(open(os.path.join(D,'manifest.json')));cnt=json.load(open(os.path.join(D,'counts.json')))
    for lv in BASE:man.setdefault('pk-'+lv,[]);cnt.setdefault('pk-'+lv,0)
    for c,(names,n) in out.items():man[c]=names;cnt[c]=n
    json.dump(man,open(os.path.join(D,'manifest.json'),'w'),ensure_ascii=False,separators=(',',':'))
    json.dump(cnt,open(os.path.join(D,'counts.json'),'w'),ensure_ascii=False,separators=(',',':'))
    print({c:v[1] for c,v in out.items()})
main()
