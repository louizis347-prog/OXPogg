# -*- coding: utf-8 -*-
# Cultura (original): "A obra" (cultob) + "Por dentro" (cultx) + "Missão da obra" (cultgame). Continuação: "Você sabia?" + linha do tempo (culttl).
import json,glob,sys,os,re,random
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,os.path.join(HERE,'rdg'))
import reg3 as r,cult_a1
import importlib
for _f in sorted(glob.glob(os.path.join(HERE,'rdg','cult_a1_*.py'))): cult_a1.C.update(importlib.import_module(os.path.basename(_f)[:-3]).C)
ENTER={'🎬':"Procure o trailer ou uma cena curta com legendas em inglês. Depois, assista ao filme inteiro com pipoca!",'📺':"Assista ao primeiro episódio com legendas em inglês e anote 3 expressões que você ouviu.",'🎶':"Ouça a música lendo a letra e cante o refrão em voz alta.",'📖':"Leia a primeira página em voz alta, mesmo sem entender tudo: o ritmo já ensina.",'🖼️':"Olhe a imagem por um minuto e descreva três coisas que você vê, em inglês.",'🎨':"Olhe a imagem por um minuto e descreva três coisas que você vê, em inglês.",'🎭':"Procure um trecho encenado e preste atenção no ritmo das falas.",'📜':"Ouça o texto lido em voz alta e acompanhe com os olhos.",'🏛️':"Procure fotos e visitas virtuais e repare nos detalhes."}
STOP=set("the a an and or but of to in on at for with from by is are was were be been this that it its as not no so if then than your my our their his her you i we they he she me him them us do did does have has had will would can could may might must should".split())
def emo(k): return str(k).split(' ')[0]
def sents(t):
    t=re.sub(r'\s+',' ',t.replace('*','')).strip()
    return [x for x in re.split(r'(?<=[.!?])\s+',t) if x]
def words(t,n=45):
    w=t.split()
    if len(w)<=n: return t
    cut=' '.join(w[:n]);m=max(cut.rfind('. '),cut.rfind('! '))
    return cut[:m+1] if m>20 else cut+'…'
def run(cid):
    it=[]
    for f in sorted(glob.glob('/home/user/OXPogg/data/%s_*.json'%cid)): it+=json.load(open(f))
    mains={x['n']:x for x in it if not x.get('xof')}
    works=[]
    for m in mains.values():
        c=(m['fr'][0] if m['fr'] else {}).get('cw')
        if c and re.fullmatch(r'\d{3,4}',str(c.get('year','')).strip()): works.append({'n':c['work'],'k':emo(c.get('kind','')),'y':int(c['year']),'m':m['n']})
    kinds=sorted({m['fr'][0]['cw']['kind'] for m in mains.values() if m['fr'] and m['fr'][0].get('cw') and m['fr'][0]['cw'].get('kind')})
    qwords=sorted({w.strip('.,’\'“”!?').lower() for A in cult_a1.C.values() for w in A['quote'][0].split() if len(w)>=5 and w.lower().strip('.,’\'“”!?') not in STOP})
    cnt=0
    for m in mains.values():
        cov=m['fr'][0] if m['fr'] else {};cw=cov.get('cw')
        if not cw: continue
        m['fr']=[s for s in m['fr'] if s['k'] not in ('cultx','cultq','cultob','cultgame')]
        rnd=random.Random(m['n']*11+5);A=cult_a1.C.get(m['n']);k=emo(cw.get('kind',''))
        y=str(cw.get('year','')).strip();au=str(cw.get('by','')).strip()
        chips=[cw.get('kind','')]+([y] if y else [])+([au.replace(' · ',' · ')] if au else [])
        pan=(A.get('panels') or sents(A['story'])) if A else sents(cw['intro'])[:3]
        ob={'k':'cultob','title':'A obra de hoje','pa':cw.get('pa'),'work':cw['work'],'chips':[c for c in chips if c],'hook':(A or {}).get('hook'),'panels':pan,'say':'Conheça a obra de hoje!'}
        tiles=[]
        if A:
            tiles+=[{'ic':'🗣️','l':'Uma frase da obra','en':A['quote'][0],'pt':A['quote'][1]},{'ic':'💡','l':'Curiosidade','t':A['curio']},{'ic':'🎯','l':'Como entrar','t':A['enter']}]
        else:
            tiles+=[{'ic':'💡','l':'Curiosidade','t':cw['fact'][2]},{'ic':'🎯','l':'Como entrar','t':ENTER.get(k,"Procure um trecho curto e curta os primeiros cinco minutos.")}]
        cx={'k':'cultx','title':'Por dentro da obra','pa':cw.get('pa'),'work':cw['work'],'tag':cw.get('kind'),'tiles':tiles,'say':'Abra cada cartão e descubra mais!'}
        rounds=[]
        if len(pan)>=2: rounds.append({'t':'order','items':pan})
        if A:
            q=A['quote'][0];toks=q.split();cand=[i for i,w in enumerate(toks) if i>0 and len(re.sub(r'\W','',w))>=5 and re.sub(r'\W','',w).lower() not in STOP]
            if cand:
                i=max(cand,key=lambda j:len(toks[j]));core=re.sub(r"[^A-Za-z’']",'',toks[i]);pre=toks[i][:toks[i].index(core[0])] if core else '';post=toks[i][len(pre)+len(core):]
                others=[w for w in qwords if w!=core.lower()];ds=rnd.sample(others,2)
                o=[core]+ds;rnd.shuffle(o)
                toks2=toks[:];toks2[i]=pre+'___'+post
                rounds.append({'t':'gap','en':' '.join(toks2),'pt':A['quote'][1],'a':core,'o':o})
            tq,ta,tw=A['tf'];rounds.append({'t':'tf','s':tq,'a':ta,'why':tw})
        else:
            cands={};
            for x in kinds:
                if emo(x)!=k: cands.setdefault(emo(x),x)
            if len(cands)>=2 and cw.get('kind'):
                d=rnd.sample(sorted(cands.values()),2);oo=[cw['kind']]+d;rnd.shuffle(oo)
                rounds.append({'t':'mc','q':'“%s” é…'%cw['work'],'o':oo,'a':oo.index(cw['kind']),'why':'“%s” é %s.'%(cw['work'],cw['kind'].split(' ',1)[-1].lower())})
        gm={'k':'cultgame','title':'Missão da obra','work':cw['work'],'rounds':rounds,'say':'Missão da obra! Vamos jogar com o que você acabou de conhecer?'}
        m['fr'][1:1]=[ob,cx,gm] if rounds else [ob,cx];cnt+=1
        x=next((z for z in it if z.get('xof')==m['n']),None)
        if x:
            x['fr']=[s for s in x['fr'] if s['k'] not in ('cult','culttl')]
            yy=int(y) if re.fullmatch(r'\d{3,4}',y) else None
            if yy:
                pool=[w for w in works if w['m']!=m['n'] and abs(w['y']-yy)>=12];rnd.shuffle(pool);pick=[]
                for w in pool:
                    if all(abs(w['y']-p['y'])>=12 for p in pick): pick.append(w)
                    if len(pick)==2: break
                if len(pick)==2:
                    cur={'n':cw['work'],'k':k,'y':yy,'m':m['n']};ws=[cur]+pick;rnd.shuffle(ws)
                    fact=(A or {}).get('curio') or words(cw['fact'][2],40)
                    tl={'k':'culttl','title':'%s Você sabia?'%cw['fact'][0],'pa':cw.get('pa'),'fact':fact,'works':[{'n':w['n'],'k':w['k'],'y':w['y']} for w in ws]}
                    pos=1 if x['fr'] and x['fr'][0]['k']=='cover' else 0;x['fr'].insert(pos,tl)
    tmp='/tmp/_cult2_%s.json'%cid;json.dump(it,open(tmp,'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    r.data(cid,tmp);print(cid,'cultura nova em',cnt)
if __name__=='__main__':
    for c in sys.argv[1:]: run(c)
