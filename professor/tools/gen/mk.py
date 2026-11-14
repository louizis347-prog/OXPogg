import sys;sys.path.insert(0,'/tmp/gen');sys.path.insert(0,'/tmp/a2')
from compact import *
from plan import P as PLAN

import re as _g
BAN=[(r"\bcould(n't)?\b","could"),(r"\bwould(n't)?\b(?! (you |i |we |he |she |they )?like)","would (só 'would like')"),(r"\bmight\b","might"),(r"\bmay\b","may"),(r"\bmust(n't)?\b","must"),
 (r"\bused to\b","used to"),(r"\b(haven't|hasn't|hadn't)\b","present/past perfect negativo"),(r"\b(have|has) (you |he |she |they |we |I )?(ever|never|already|just|yet|been|seen|done|eaten|gone|tried|finished)\b","present perfect"),
 (r"\b(i|you|we|they|he|she|it|that|there)'ve\b|\b(he|she|it|that)'s (been|gone|seen|done|eaten|just|already)\b","present perfect (contração)"),(r"\bshouldn't\b","shouldn't"),(r"\bShould (I|we|you|he|she|it|they)\b|\bshould (I|we|you|he|she|it|they) \w+\?","Should + sujeito (pergunta)"),
 (r"\bwon't\b|\bwill not\b","will negativo"),(r"(^|[.!?]\s*)Will (you|it|we|they|he|she|there|the)\b","pergunta com will"),(r"\b(don't|doesn't|didn't) have to\b|\bhad to\b|\b(Do|Does|Did) (you|I|we|they|he|she) have to\b","have to fora do afirmativo no presente"),
 (r"\b(was|were) (made|built|written|painted|sold|born|found|invented|designed|used|cooked|baked|taken|called)\b","passivo no passado"),
 (r"\b\w+ (who|which|whom|whose|that) (is|are|was|were|has|have|had|lives|works|makes|sells|helps|likes|wants|knows|comes|goes|speaks|did|does|do)\b|, which\b","oração relativa"),
 (r"\b(myself|yourself|himself|herself|itself|ourselves|themselves)\b","pronome reflexivo"),(r"\bas \w+ as\b","as…as"),(r"\benough\b","enough"),
 (r"\b(do you know|can you tell me|could you tell me|i wonder|do you remember|i don't know|i'm not sure|do you think) (where|what|when|how|why|if|who|which)\b","pergunta indireta"),
 (r"\btold (me|you|him|her|us|them)\b|\basked (me|you|him|her|us) (if|to)\b|\bsaid (that )?(i|he|she|we|they|you|it) \b","discurso indireto"),
 (r"(^|[.!?]\s*)(Please )?Don't (?!worry)\w+","imperativo negativo (só 'Don't worry')"),(r"\bhad (been|gone|seen|done|eaten|finished|already)\b","past perfect"),(r"\bif I (were|was|had|could|didn't|knew)\b","segundo condicional")]
def grammar_check(k,texts):
    bad=[]
    for t in texts:
        s=t.replace('’',"'")
        for pat,name in BAN:
            if _g.search(pat,s,_g.I if name!="may" else 0): bad.append((name,t[:60]))
    return bad

_PV={}
def _prev_vocab(k):
    import glob,os
    out=set()
    for f in glob.glob('/home/user/OXPogg/professor/data/v4/20*.json'):
        n=int(os.path.basename(f)[:-5])
        if n>=2000 and n<2000+k and n not in _PV:
            try:
                d=json.load(open(f)); _PV[n]={x[0].lower() for p in d['pages'] if p.get('kind')=='vocab' for x in p.get('words',[])}
            except Exception: _PV[n]=set()
    for n,s in _PV.items():
        if n<2000+k: out|=s
    return out
def A2(k,d):
    row=PLAN[k-1];title,city,npc,you,struct,sc=row
    nxt=PLAN[k][0] if k<len(PLAN) else 'Próxima etapa'
    L=[(('You' if w=='Y' else npc),e,p) for w,e,p in d['L']]
    gl=d['gl']; gloss=[(g[0],g[1]) for g in gl]; vocab=[(g[0],g[1],g[2],g[3],g[4]) for g in gl[:6]]
    ctx=[]
    for i in range(3):
        w,pt=gl[i][0],gl[i][1]; oth=[g[1] for g in gl[3:] if g[1]!=pt][:2]
        ctx.append((w.capitalize()+'.',w,[pt]+oth,w+' = '+pt+'.'))
    ex=d['ex']; exprs=[(e[0],e[1],L[e[2]][1],e[3]) for e in ex]
    chunks=[e[0] for e in ex[:5]]
    role=[]
    for i in (0,2,4,6):
        n_=L[i]; y=L[i+1]
        role.append([(n_[1],n_[2],y[1]),('Really?','Mesmo?','Yes, really.'),('I see.','Entendi.','Okay.')])
    m=dict(reg=(k if k<=233 else k-233),title=title,city=city,npc=npc,you=you,face=d['face'],g=d['g'],yg=d['yg'],crole=d['crole'],sc=sc,pool=d.get('pool') or [sc,'street','cafe2','park'],
     story=d['story'],p=d['p'],mission=d['mission'],emo=d['emo'],teaser=nxt,teaser_d=d.get('td','Próxima situação'),badge=d['badge'],
     lines=L,open=d['O'],close=d['C'],rtitle=d['rt'],gloss=gloss,fast=d['fast'],scan=d['scan'],tf=d['tf'],order=d['order'],ctx=ctx,chunks=chunks,think=d['think'],
     cu=d['cu'],errors=d['err'],homework=d['hw'],hw=d['hwf'],lab=d['lab'],cards=d['cards'],key=d['key'],vocab=vocab,molds=d['mo'],sounds=d['so'],role=role,change=d['chg'],
     wtask=d['wt'][0],wmodel=d['wt'][1],kw=d['wt'][2],verbs=[tuple(x) if not isinstance(x,str) else vb_(x) for x in d['vb']],exprs=exprs,real=d['real'],swaps=d['sw'],mini=list(d['sw'])[:4])
    for i,s in d['sw'].items():
        if s[0] not in L[i][1] or s[2] not in L[i][2]: print('SWAP?',k,i,s[0] in L[i][1],s[2] in L[i][2])
    for g in gl:
        if g[0].lower() not in (' '.join(e for e,_ in sum([list(x) for x in [d['O'],d['C']]],[]))+' '.join(l[1] for l in L)).lower(): print('GLOSS?',k,g[0])
    for g in gl[:6]:
        if g[0].lower() not in g[4].lower(): print('VOCABEX?',k,g[0])
    sys.path.insert(0,'/home/user/OXPogg/professor/tools')
    import cefr_audit as CA, re as _re
    taught=set(w for g in gl for w in _re.findall(r"[a-z']+",g[0].lower()))|set(w for e in d['ex'] for w in _re.findall(r"[a-z']+",e[0].lower().replace('’',"'")))|set(v.split('|')[0] for v in d['vb'] if isinstance(v,str))|set(v.split('|')[3] for v in d['vb'] if isinstance(v,str))
    nm={npc.lower(),you.lower(),city.lower()}
    cef=[]
    for _,en,_ in L:
        txt=en.replace('’',"'")
        for mt in _re.finditer(r"[A-Za-z]+(?:'[a-z]+)?",txt):
            w=mt.group(0);w2=w.lower();bf=txt[:mt.start()].rstrip()
            if w[0].isupper() and bf and bf[-1] not in '.?!“"': continue
            if w2 in nm or w2 in CA.SKIP: continue
            lv=CA.level(w2)
            if lv is None or CA.RANK[lv]<=2: 
                if lv is None and len(w2)>2 and not any(b in taught for b in CA.base_forms(w2)) and w2 not in taught: cef.append(w2+':??')
                continue
            if w2 in taught or any(b in taught for b in CA.base_forms(w2)): continue
            cef.append(w2+':'+lv)
    pv=_prev_vocab(k); rep=[g[0] for g in gl[:6] if g[0].lower() in pv]
    if len(rep)>=3: print('REPEAT?',k,'palavras já ensinadas em aulas A2 anteriores:',rep)
    if cef: print('CEFR?',k,sorted(set(cef)))
    gb=grammar_check(k,[e for _,e,_ in L]+[e[0] for e in d['ex']]+[e[0] for e in d['ex']][:0])
    if gb: print('GRAMMAR?',k,gb)
    for mo in d['mo']:
        f=mo[1]
        for key,opts in mo[2]: f=f.replace('{'+key+'}',opts[0])
        if f!=mo[3]: print('MOLD?',k,f,'|',mo[3])
    compact(2000+k,m)
def vb_(s):
    v,ic,pt,past,p1,p3,pp,pg=s.split('|')
    third=v+'es' if v.endswith(('s','sh','ch','x','o')) else (v[:-1]+'ies' if v.endswith('y') and v[-2] not in 'aeiou' else v+'s')
    ing=(v[:-1] if v.endswith('e') and not v.endswith('ee') else v)+'ing'
    if v in('run','stop','get','swim','sit','plan','shop'): ing=v+v[-1]+'ing'
    return (v,ic,pt,'%s = %s. Passado: %s.'%(v.capitalize(),pt,past),third,past,ing,p1,p3,pp,pg)
