# -*- coding: utf-8 -*-
# Cultura em 2 quadros no original ("Dentro da obra" + perguntas) e "Quem fez?" na continuação.
import json,glob,sys,os,re,random,importlib
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,os.path.join(HERE,'rdg'))
import reg3 as r,cult_a1
ENTER={'🎬':"Procure o trailer ou uma cena curta com legendas em inglês. Depois, assista ao filme inteiro com pipoca!",'📺':"Assista ao primeiro episódio com legendas em inglês e anote 3 expressões que você ouviu.",'🎶':"Ouça a música lendo a letra e cante o refrão em voz alta.",'📖':"Leia a primeira página em voz alta, mesmo sem entender tudo: o ritmo já ensina.",'🖼️':"Olhe a imagem por um minuto e descreva três coisas que você vê, em inglês.",'🎨':"Olhe a imagem por um minuto e descreva três coisas que você vê, em inglês.",'🎭':"Procure um trecho encenado e preste atenção no ritmo das falas.",'📜':"Ouça o texto lido em voz alta e acompanhe com os olhos.",'🏛️':"Procure fotos e visitas virtuais e repare nos detalhes."}
def emo(k): return str(k).split(' ')[0]
def run(cid):
    it=[]
    for f in sorted(glob.glob('/home/user/OXPogg/data/%s_*.json'%cid)): it+=json.load(open(f))
    mains={x['n']:x for x in it if not x.get('xof')}
    kinds=sorted({m['fr'][0]['cw']['kind'] for m in mains.values() if m['fr'][0].get('cw') and m['fr'][0]['cw'].get('kind')})
    auth={}
    for m in mains.values():
        c=m['fr'][0].get('cw')
        if c and c.get('by'): auth.setdefault(emo(c.get('kind','')),set()).add(str(c['by']).split(' · ')[0].strip())
    allauth=sorted({a for v in auth.values() for a in v})
    nx=0
    for m in mains.values():
        fr=m['fr'];cov=fr[0];cw=cov.get('cw')
        if not cw or any(s['k']=='cultx' for s in fr): continue
        rnd=random.Random(m['n']*7+3)
        A=cult_a1.C.get(m['n'])
        k=emo(cw.get('kind',''))
        if A:
            tiles=[{'ic':'📖','l':'A história','t':A['story']},{'ic':'🗣️','l':'Uma frase da obra','en':A['quote'][0],'pt':A['quote'][1]},{'ic':'💡','l':'Curiosidade','t':A['curio']},{'ic':'🎯','l':'Como entrar','t':A['enter']}]
        else:
            tiles=[{'ic':'📖','l':'A obra','t':cw['intro']},{'ic':'💡','l':'Curiosidade','t':cw['fact'][2]},{'ic':'🎯','l':'Como entrar','t':ENTER.get(k,"Procure um trecho curto e curta os primeiros cinco minutos.")}]
        cx={'k':'cultx','title':'Dentro da obra','pa':cw.get('pa'),'work':cw['work'],'tag':cw.get('kind'),'tiles':tiles,'say':'Vamos conhecer a obra por dentro? Abra cada cartão!'}
        cq=next((s for s in fr if s['k']=='cultq'),None)
        qs=[]
        if cq:
            au=str(cw['by']).split(' · ')[0].strip();same=sorted(a for a in auth.get(k,[]) if a!=au);oth=sorted(a for a in allauth if a!=au and a not in same)
            ds=rnd.sample(same,min(2,len(same)));ds+=rnd.sample(oth,2-len(ds)) if len(ds)<2 else []
            oo=[au]+ds;rnd.shuffle(oo)
            qs=[{'q':'Quem criou “%s”?'%cw['work'],'o':oo,'a':oo.index(au),'why':cq['q']['why']}]
        if A:
            q,o,why=A['q'];oo=list(o);rnd.shuffle(oo);qs.append({'q':q,'o':oo,'a':oo.index(o[0]),'why':why})
        else:
            cands=[x for x in kinds if emo(x)!=k and x!=cw.get('kind')];ds={}
            for x in cands: ds.setdefault(emo(x),x)
            if len(ds)>=2 and cw.get('kind'):
                d=rnd.sample(sorted(ds.values()),2);oo=[cw['kind']]+d;rnd.shuffle(oo)
                qs.append({'q':'“%s” é…'%cw['work'],'o':oo,'a':oo.index(cw['kind']),'why':'“%s” é %s.'%(cw['work'],cw['kind'].split(' ',1)[-1].lower())})
        if cq:
            cq['qs']=qs;cq['title']='Cultura em %d toque%s'%(len(qs),'s' if len(qs)>1 else '');cq.pop('q',None)
        # inserir "Dentro da obra" depois da abertura
        fr.insert(1,cx);nx+=1
        # continuação: "Quem fez?"
        x=next((y for y in it if y.get('xof')==m['n']),None)
        if x:
            c=next((s for s in x['fr'] if s['k']=='cult'),None)
            if c:
                y=str(cw.get('year','')).strip();ago=''
                if re.fullmatch(r'\d{3,4}',y): ago=' (há %d anos)'%(2025-int(y))
                c['title']='👤 Quem fez?';c['fact']='**%s** · %s, **%s**%s.'%(cw.get('by','Tradição popular'),cw.get('kind','').split(' ',1)[-1].lower(),y or 'data incerta',ago)
    tmp='/tmp/_cult_%s.json'%cid;json.dump(it,open(tmp,'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    r.data(cid,tmp);print(cid,'cultx em',nx)
if __name__=='__main__':
    for c in sys.argv[1:]: run(c)
