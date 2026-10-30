#!/usr/bin/env python3
"""Pocket: gera data/pk-<nivel>_NN.json a partir de tools/pocket/<nivel>_arcoNN.py e atualiza manifest/counts."""
import json,glob,importlib.util,os,sys,re
R=os.path.dirname(os.path.abspath(__file__));D=os.path.join(R,'..','..','data')
GR=[('#FF8A5B','#FFC857'),('#2EC4B6','#3A86FF'),('#B388FF','#FF6FB5'),('#43D17A','#2EC4B6'),('#FF7A7A','#FFB84D')]
BASE={'a1':950000,'a2':951000,'b1':952000,'b2':953000,'c1':954000,'c2':955000}
def parse_txt(fn):
    eps=[];cur=None
    def sp(x):return [t.strip() for t in x.split('|')]
    for ln in open(fn,encoding='utf-8'):
        ln=ln.rstrip('\n')
        if not ln.strip() or ln.startswith('#'):continue
        k,_,v=ln.partition(':');k=k.strip();v=v.strip()
        if k=='T':
            a=sp(v);w=[t.strip() for t in a[4].split(',')]
            cur=dict(t=a[0],s=a[1],sc=a[2],city=a[3],who=(w[0],w[1],w[2],w[3]),dlg=[],vocab=[],build=[],speak=[],recap=[]);eps.append(cur)
        elif k=='K':a=sp(v);cur['key']=(a[0],a[1])
        elif k=='M':cur['mission']=v
        elif k=='D':a=sp(v);cur['dlg'].append((a[0],a[1],a[2]))
        elif k=='V':cur['vocab']+=[tuple(sp(x)) for x in v.split(';')]
        elif k=='B':a=sp(v);cur['build'].append(dict(en=a[0],pt=a[1],opts=[tuple(o.split('=')) for o in a[2].split(';')]))
        elif k=='S':a=sp(v);cur['speak'].append(dict(who=a[0],line=(a[1],a[2]),target=a[3],pt=a[4]))
        elif k=='R':a=sp(v);cur['recap'].append((a[0],a[1]))
        elif k=='X':a=sp(v);cur['expr']=(a[0],a[1])
        elif k=='C':cur['culture']=v
        elif k=='N':cur['teaser']=v
        elif k=='BOSS':cur['boss']=True
    return eps
def load(fn):
    if fn.endswith('.txt'):
        class M:pass
        m=M();m.EPS=parse_txt(fn);m.ARC=('','');return m
    sp=importlib.util.spec_from_file_location('m',fn);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m

EMO={}
_ef=os.path.join(R,'emoji_a1.txt')
if os.path.exists(_ef):
    for _p in open(_ef,encoding='utf-8').read().replace('\n','|').split('|'):
        if ':' in _p:_a,_,_b=_p.strip().partition(':');EMO.setdefault(_a.strip().lower(),_b.strip())
def vocab_cards(x):
    out=[]
    for v in x['vocab']:
        w=v[0];key=w.lower().split(' ')[0];ex=['','']
        for (_who,en,pt) in x['dlg']:
            if re.search(r'\b'+re.escape(w.lower())+r'\b',en.lower()):ex=[en,pt];break
        if not ex[0]:
            for (_who,en,pt) in x['dlg']:
                if re.search(r'\b'+re.escape(key)+r'\b',en.lower()):ex=[en,pt];break
        if not ex[0]:ex=[x['key'][0],x['key'][1]]
        out.append([w,v[1],EMO.get(w.lower(),EMO.get(key,'')),ex[0],ex[1]])
    return out
NOTAS=[
 (r"\bhow (are you|is [a-z ]{2,14}|are they|are we) doing\b","💡 Tradução não literal: “doing” significa “fazendo”, mas “How are you doing?” é uma expressão fixa que quer dizer “Como vai?”. Não dá para traduzir palavra por palavra."),
 (r"\bwhat (are|is) (you|we|they|he|she)\b[^.?!]*\bdoing\b[^.?!]*\b(weekend|saturday|sunday|tonight|tomorrow|next|friday)\b","💡 Aqui “are doing” (presente contínuo) fala de planos próximos. “doing” é “fazendo”, mas em português dizemos “vai fazer”."),
 (r"\bwhat'?s up\b|\bwhat is up\b","💡 Expressão informal: “What’s up?” é “E aí?”. Literalmente seria “o que está em cima?”, mas ninguém diz isso."),
 (r"\bhow'?s it going\b|\bhow is it going\b","💡 Expressão fixa: “How’s it going?” é “Como vai?” / “E aí, tudo bem?”. Não é “como está indo” palavra por palavra."),
 (r"\bnice to meet you\b","💡 Expressão fixa: “Nice to meet you” é “Prazer em conhecer você”. Literalmente seria “bom conhecer você”."),
 (r"\byou'?re welcome\b|\byou are welcome\b","💡 Expressão fixa: “You’re welcome” é “De nada”. Literalmente seria “você é bem-vindo”."),
 (r"\bno problem\b","💡 Expressão fixa: “No problem” é “Sem problema / De nada”."),
 (r"\bsee you\b","💡 Expressão fixa: “See you” é “Até mais”. Literalmente seria “vejo você”."),
 (r"\bhow much\b[^?]*\b(is|are|does|do)\b","💡 “How much” pergunta o preço ou a quantidade: “Quanto custa / Quanto é?”."),
]
def nota_de(text):
    t=text.lower().replace('’',"'")
    for rx_,msg in NOTAS:
        if re.search(rx_,t):return msg
    return ''
def notas_ep(x):
    out=[];seen=set()
    cand=[(x['key'][0],x['key'][1])]+[(d[1],d[2]) for d in x['dlg']]
    for en,pt in cand:
        m=nota_de(en)
        if m and m not in seen:seen.add(m);out.append(dict(en=en,pt=pt,txt=m))
    return out
def build_note(b):
    for o in b['opts']:
        m=nota_de(b['en'].replace('{0}',o[0]))
        if m:return m
    return ''
STOP={'back','right','left','up','down','over','under','top','bottom','point','change','time','number','word','words','face','room','plan','test','class','level','work','free','open','new','old','ready','middle','front','behind','around','across','between','near','far','inside','outside','post','follow','share','miss','fix','answer','question','name','address','code','call','send','help','win','play','meet','visit','think','love','look','talk','speak','read','write'}
def pick_icon(text,vocab,fallback):
    ws=re.findall(r"[a-z]+(?: [a-z]+)?",text.lower().replace('’',"'"))
    toks=re.findall(r"[a-z']+",text.lower())
    for v in vocab:
        e=EMO.get(v[0].lower()) or EMO.get(v[0].lower().split(' ')[0])
        if e and re.search(r'\b'+re.escape(v[0].lower().split(' ')[0])+r'\b',text.lower()):return e
    for i,t in enumerate(toks):
        if i+1<len(toks) and (t+' '+toks[i+1]) in EMO:return EMO[t+' '+toks[i+1]]
    for t in toks:
        if t in EMO and t not in STOP:return EMO[t]
    return fallback
def narrate(x,name,city):
    """Leitura em forma de narração (3ª pessoa) montada a partir do diálogo: 'Dee asks: "..."'. Só presente simples (A1)."""
    L=x['dlg'];pars=[]
    pars.append(dict(lead=['In %s, you meet %s.'%(city,name),'Em %s, você encontra %s.'%(city,name)],q=['',''],who=None,ic='🏙️'))
    prevq=False;prevwho=None
    conn=[('',''),('Then,','Então,'),('',''),('Next,','Depois,'),('',''),('After that,','Em seguida,'),('',''),('Then,','Então,')]
    for i,(who,en,pt) in enumerate(L):
        you=(who=='You');first=re.split(r'(?<=[.!?])\s+',en.strip())[0];isq=first.endswith('?');endq=en.strip().endswith('?')
        if isq:ve,vp='ask' if you else 'asks','pergunta'
        elif prevq and prevwho!=who:ve,vp='answer' if you else 'answers','responde'
        else:ve,vp='say' if you else 'says','diz'
        ce,cp=conn[i%len(conn)] if i<len(L)-1 else ('Finally,','Por fim,')
        if i==0:ce=cp=''
        se=('you' if you else who) if ce else ('You' if you else who)
        sp=('você' if you else who) if cp else ('Você' if you else who)
        lead_en=((ce+' ') if ce else '')+se+' '+ve+':'
        lead_pt=((cp+' ') if cp else '')+sp+' '+vp+':'
        pars.append(dict(lead=[lead_en,lead_pt],q=[en,pt],who=who,ic=pick_icon(en,x['vocab'],'❓' if isq else '💬')))
        prevq=endq;prevwho=who
    pars.append(dict(lead=['Now you know:','Agora você sabe:'],q=[x['key'][0],x['key'][1]],who=None,ic='💡'))
    return pars
def episode(lv,arc_i,k,x,base,order):
    n=base+order;g=GR[arc_i%len(GR)];who=x['who']
    name,gender,face,role=who
    face=face.replace('🧑','👨' if gender=='m' else '👩')
    fr=[
     dict(k='pkhero',g=list(g),num=order,lvl=lv.upper(),face=face,name=name,city=x['city'],sub=x['s'],mission=x['mission'],hook=list(x['key']),boss=bool(x.get('boss'))),
     dict(k='pkdlg',g=list(g),title='Diálogo',lines=[list(l) for l in x['dlg']],vocab=[list(v) for v in x['vocab']],cast={name:[face,g[0]],'You':['🙂','#e85d75']}),
     dict(k='pkvoc',g=list(g),title='Vocabulário',cards=vocab_cards(x),notes=notas_ep(x)),
     dict(k='pkread',g=list(g),title='Leitura',pars=narrate(x,name,x['city']),vocab=[list(v) for v in x['vocab']]),
     dict(k='pkbuild',g=list(g),title='Monte a frase',items=[dict(en=b['en'],pt=b['pt'],opts=[list(o) for o in b['opts']],note=build_note(b)) for b in x['build']]),
     dict(k='pkspeak',g=list(g),title='Fale',items=[dict(who=s['who'],line=list(s['line']),target=s['target'],pt=s['pt']) for s in x['speak']]),
     dict(k='wrap',title='Mochila do episódio',recap=[list(r) for r in x['recap']],expr=list(x['expr']),culture=x['culture'],teaser=dict(t=x['teaser'],d=''),
          sticker=dict(name=name,face=face,role=role,city=x['city'],boss=bool(x.get('boss'))),stickers=vocab_cards(x)),
    ]
    return dict(n=n,o=n,t=x['t'],s=x['s'],sc=x['sc'],lv=lv.upper(),a=dict(k='Situação',w=x['t'],y='',d=x['culture']),
      h=dict(l=x['dlg'][0][1],src='Pocket',tr=x['dlg'][0][2]),p=x['mission'],g=dict(t=x['key'][0]),v2=True,
      v=[[v[0],v[1],''] for v in x['vocab']],presentation='pocket-v1',pocket=1,
      character=dict(id='pk_'+name.lower(),name=name,gender=gender,role=role,city=x['city'],recurring=True),
      arc=dict(i=arc_i+1,pos=k+1,of=10),fr=fr)
def main():
    out={}
    for lv in BASE:
        files=sorted(glob.glob(os.path.join(R,lv+'_arco*.py'))+glob.glob(os.path.join(R,lv+'_arco*.txt')))
        if not files:continue
        flat=[]
        for ai,fn in enumerate(files):
            m=load(fn)
            for k,x in enumerate(m.EPS):flat.append(x)
        # ordem pedagógica (tools/pocket/ordem_<nivel>.json): por complexidade, intercalando dia a dia e tema
        of=os.path.join(R,'ordem_%s.json'%lv)
        if os.path.exists(of):
            pos={t:i for i,t in enumerate(json.load(open(of)))}
            flat=sorted(flat,key=lambda x:pos.get(x['t'],10**6))
        eps=[]
        for order,x in enumerate(flat,1):
            nx=flat[order]['t'] if order<len(flat) else None
            x['teaser']=('Próximo: '+nx) if nx else 'Fim por enquanto. Novos episódios chegando.'
            ai=(order-1)//10;k=(order-1)%10
            x['boss']=(k==9);x['s']=re.sub(r'^Desafio do arco: ?','',x['s'])
            eps.append(episode(lv,ai,k,x,BASE[lv],order))
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
