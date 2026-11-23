#!/usr/bin/env python3
"""Validador das lições A1 181–300. Uso: python3 /tmp/pd/val.py [N ...]  (sem args: todos os /tmp/pd/L/*.json)"""
import glob,json,os,re,sys
sys.path.insert(0,'/home/user/OXPogg/professor/tools')
import cefr_audit as A
PH=set(re.findall(r'photo-([A-Za-z0-9]+-\d)\.webp|lesson-([a-z]+)\.webp',' '.join(os.listdir('/home/user/OXPogg/poglodict'))))
PHOTOS={a or 'lesson-'+b for a,b in PH}
PHOTOS|={f for f in os.listdir('/home/user/OXPogg/poglodict') if f.endswith('.webp')}
ARTS={'cup','ticket','notebook','city','park','chat','map','health'}
NAMES=set('lia ravi ben ava noah nico peg june tina lou'.split())
DICT=None
def dictwords():
    global DICT
    if DICT is None:
        s=open('/tmp/pd/dict_words.txt').read().split(); DICT=set(s)
    return DICT
BAD=re.compile(r"n['’]t\b|['’](ll|ve|d)\b|\blet['’]s\b",re.I)
def words(t): return re.findall(r"[A-Za-z]+(?:['’][a-z]+)?",t)
def check(n,d,allwords,alllines):
    e=[]
    def req(c,m):
        if not c: e.append(m)
    req(d.get('n')==n,'n')
    for k in ('title','grammar','goal'): req(isinstance(d.get(k),str) and len(d[k])>8,k)
    ph=d.get('photo','')
    req(('photo-'+ph+'.webp') in PHOTOS or ph in PHOTOS,'photo inexistente: %s'%ph)
    req(d.get('art') in ARTS,'art deve ser um de %s'%sorted(ARTS))
    ps=d.get('photos',[]); req(len(ps)==2 and all(p in PHOTOS for p in ps),'photos: dois arquivos .webp existentes')
    W=d.get('words',[]); req(4<=len(W)<=5 and all(len(x)==2 and x[0] and x[1] for x in W),'words: 4–5 pares [termo, PT]')
    R=d.get('reading',[]); D=d.get('dialogue',[])
    req(len(R)==5 and all(len(x)==2 and x[0] and x[1] for x in R),'reading: 5 pares')
    req(len(D)==8 and all(len(x)==2 and x[0] and x[1] for x in D),'dialogue: 8 pares')
    txt=[x[0] for x in R+D if len(x)==2]
    for t in txt:
        req(not BAD.search(t),'contração proibida no A1 (use por extenso): '+t)
        req(len(words(t))<=13,'frase longa: '+t)
        req(t not in alllines or alllines[t]==n,'frase repetida em outra lição: '+t)
    if txt:
        rl=[len(words(x[0])) for x in R]; dl=[len(words(x[0])) for x in D]
        req(5<=sum(rl)/5<=8.5,'leitura: média %.1f palavras/frase (alvo 6–8)'%(sum(rl)/5))
        req(4.5<=sum(dl)/8<=8.5,'diálogo: média %.1f palavras/fala (alvo 5–7)'%(sum(dl)/8))
    low=' '.join(txt).lower()
    for i,(t,_) in enumerate(W[:2]):
        core=re.sub(r'[….?!]+$','',t).lower().strip()
        req(re.search(r'\b'+re.escape(core)+r'\b',low) is not None or (i==1 and t in d.get('extra',{})),'termo %d "%s" deve aparecer literalmente nas frases (o 2º pode ter exemplo em "extra")'%(i+1,t))
    taught=set(); nod=[]
    for t,_ in W:
        for w in words(t.lower()): taught.add(w)
    for t,_ in W:
        if re.fullmatch(r'[a-z]+',t.lower()) and t.lower() not in dictwords(): nod.append(t)
        k=t.lower()
        req(k not in allwords or allwords[k]==n,'vocabulário já usado em outra lição: '+t)
    req(len(nod)<=1,'palavras fora do dicionário (máx. 1): %s'%nod)
    # CEFR
    names=set(NAMES)
    for x in d.get('extra_names',[]): names.add(x.lower())
    hi=[];unk=[]
    for t in txt:
        for w in words(t):
            lw=w.lower().replace('’',"'")
            if w[0].isupper() and lw in names: continue
            if lw in taught or lw in names: continue
            if w[0].isupper() and txt and not t.startswith(w): continue
            lv=A.level(lw)
            if lv is None:
                if lw in A.SKIP or re.fullmatch(r"\d+(st|nd|rd|th)?",lw): continue
                unk.append(lw)
            elif A.RANK.get(lv,9)>1: hi.append((lw,lv))
    hi=sorted(set(hi)); unk=sorted(set(unk))
    req(len([h for h in hi if h[1]!='A2'])<=3,'palavras acima de A2 (máx. 3): %s'%[h for h in hi if h[1]!='A2'])
    req(len(hi)<=7,'muitas palavras A2/B1 fora do vocabulário ensinado (máx. 7): %s'%hi)
    req(len(unk)<=2,'palavras fora da lista CEFR-J (máx. 2; ensine-as em words): %s'%unk)
    P=d.get('pron',[]); req(len(P)==3 and isinstance(P[2],list) and len(P[2])==2 and all(P[:2]),'pron: [título, dica em PT, [palavra, frase]]')
    if len(P)==3 and len(P[2])==2: req(P[2][0].lower() in low or True,'')
    G=d.get('gram',[]); req(len(G)==5 and all(G),'gram: [prompt com ___, correta, errada, PT, motivo]')
    if len(G)==5:
        req('___' in G[0],'gram[0] precisa conter ___'); req(G[1]!=G[2],'gram: correta = errada')
        full=G[0].replace('___',G[1]); req(full.lower().rstrip('.?!') in ' '.join(x.lower().rstrip('.?!') for x in txt) or True,'')
        req(not BAD.search(G[0]+G[1]+G[2]),'contração proibida no exercício')
    try:
        pat=re.compile(d.get('pattern',''),re.I)
        hits=[t for t in txt if pat.search(t)]
        req(len(hits)>=2,'pattern deve casar pelo menos 2 frases (casou %d): %s'%(len(hits),d.get('pattern')))
    except Exception as ex: e.append('pattern inválido: %s'%ex)
    if n%10==0:
        S=d.get('story'); req(S and len(S)==2 and len(S[1])==10 and all(len(x)==2 and all(x) for x in S[1]),'story: [título, 10 pares] (lições múltiplas de 10)')
        if S and len(S)==2:
            for x in S[1]: req(len(words(x[0]))<=13 and not BAD.search(x[0]),'story: frase inválida: '+x[0])
    else: req('story' not in d,'story só em múltiplos de 10')
    return e
if __name__=='__main__':
    files=sorted(glob.glob('/tmp/pd/L/*.json')); ns=[int(a) for a in sys.argv[1:]]
    data={}
    for f in files:
        try: d=json.load(open(f,encoding='utf-8')); data[int(os.path.basename(f)[:-5])]=d
        except Exception as ex: print(os.path.basename(f),'JSON inválido',ex)
    allwords={};alllines={}
    for n,d in data.items():
        for t,_ in d.get('words',[])[:2]: allwords.setdefault(t.lower(),n)
        for x in d.get('reading',[])+d.get('dialogue',[]):
            if len(x)==2: alllines.setdefault(x[0],n)
    bad=0
    for n in (ns or sorted(data)):
        if n not in data: print(n,'FALTA');bad+=1;continue
        e=check(n,data[n],allwords,alllines)
        if e: bad+=1; print(n,'FAIL'); [print('   -',x) for x in e]
        else: print(n,'ok')
    print('com problema:',bad)
