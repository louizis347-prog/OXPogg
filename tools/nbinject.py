# -*- coding: utf-8 -*-
# Integra arcos novos dos cursos Neighbors e injeta os passos extras (ditado, acentos, der/die/das, escrita à mão).
import json,glob,sys,re,random,unicodedata,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import reg3 as r
R='/home/user/OXPogg/'
G=['#2D98DA','#20BF6B']
def strip(s): return ''.join(c for c in unicodedata.normalize('NFD',s) if unicodedata.category(c)!='Mn')
ALT={'é':'èê','è':'éê','ê':'éè','à':'â','â':'à','ô':'o','î':'i','û':'ù','ù':'û','ë':'e','ï':'i','ç':'c'}
TIPS=[(r'ç','O “ç” (cedilha) soa /s/ antes de a, o, u: français, garçon.'),(r'è','O acento grave (è) soa aberto /ɛ/: très, mère.'),(r'ê','O circunflexo (ê) também soa aberto /ɛ/ e costuma indicar um “s” antigo: fête, forêt.'),(r'é','O acento agudo (é) soa fechado /e/: café, été.'),(r'.','Em francês os acentos mudam o som da vogal: é (fechado), è/ê (aberto), à/â, ô, û.')]
HAS=re.compile(r'[áéíóúñüàèìòùâêîôûçãõëïœ]',re.I)
def variants(w,rnd):
    vs=[];st=strip(w)
    if st!=w: vs.append(st)
    for i,c in enumerate(w):
        for a in ALT.get(c,''): vs.append(w[:i]+a+w[i+1:])
    out=[]
    for v in vs:
        if v!=w and v not in out: out.append(v)
    return out
def tip(w):
    for p,t in TIPS:
        if re.search(p,w): return t
def add_dict(x):
    if any(s['k']=='nbdict' for s in x['fr']): return
    lines=[l for s in x['fr'] if s['k']=='nbchat' for l in s['lines']]
    c=[l for l in lines if 3<=len(l[1].split())<=9 and len(l[1])<=70]
    if len(c)<3: c=lines
    if len(c)<3: return
    pick=[c[0],c[len(c)//2],c[-1]] if len(c)>=3 else c
    seen=[];out=[]
    for l in pick+c:
        if l[1] in seen: continue
        seen.append(l[1]);out.append({'t':l[1],'pt':l[2]})
        if len(out)==3: break
    j=max(k for k,s in enumerate(x['fr']) if s['k'] in ('nbvocab','nbacc','nbart','nbkanji','nbwrite'))
    x['fr'].insert(j+1,{'k':'nbdict','g':G,'title':'Ditado','items':out})
def add_acc(x):
    if any(s['k']=='nbacc' for s in x['fr']): return
    rnd=random.Random(x['n']);items=[];seen=set()
    for w in x.get('v',[]):
        word=w[0].strip()
        if not HAS.search(word) or word in seen or len(word)>26: continue
        vs=variants(word,rnd)
        if not vs: continue
        seen.add(word)
        alts=[vs[0]]+[v for v in rnd.sample(vs[1:],min(1,len(vs)-1))] if len(vs)>1 else vs[:1]
        items.append({'w':word,'s':strip(word),'pt':w[1],'alts':alts[:2],'tip':tip(word)})
    if len(items)<3:
        for sec in x['fr']:
            if sec['k']!='nbchat': continue
            for l in sec['lines']:
                for tok in re.findall(r"[\w'’]+",l[1]):
                    if not HAS.search(tok) or len(tok)<4 or tok in seen or len(items)>=5: continue
                    vs=variants(tok,rnd)
                    if not vs: continue
                    seen.add(tok);alts=[vs[0]]+[v for v in rnd.sample(vs[1:],min(1,len(vs)-1))] if len(vs)>1 else vs[:1]
                    items.append({'w':tok,'s':strip(tok),'pt':'na frase: «'+(l[2] if len(l)>2 else '')+'»','alts':alts[:2],'tip':tip(tok)})
    if len(items)<3: return
    j=next(k for k,s in enumerate(x['fr']) if s['k']=='nbvocab')
    x['fr'].insert(j+1,{'k':'nbacc','g':x['fr'][0].get('g'),'title':'Acentos e ortografia','items':items[:5]})
def add_art(x):
    if any(s['k']=='nbart' for s in x['fr']): return
    it=[]
    for w in x.get('v',[]):
        m=re.match(r'^(der|die|das)\s+(\S+)$',w[0].strip())
        if m: it.append([m.group(1),m.group(2),w[1]])
    if len(it)<2: return
    j=next(k for k,s in enumerate(x['fr']) if s['k']=='nbvocab')
    x['fr'].insert(j+1,{'k':'nbart','g':['#00B894','#0984E3'],'title':'Der · Die · Das','items':it[:4]})
KS=None
def ks():
    global KS
    if KS is None:
        KS=set(json.load(open(R+'data/kana-strokes.json')).keys())|set(json.load(open(R+'data/kanji-strokes.json')).keys())
    return KS
def add_write(x):
    if any(s['k']=='nbwrite' for s in x['fr']): return
    it=[]
    for w in x.get('v',[]):
        word=w[0].strip();m=re.search(r'«(.+?)»',w[2] if len(w)>2 else '')
        if word and all(c in ks() for c in word) and m:
            it.append({'w':word,'m':w[1],'r':m.group(1),'s':word})
        if len(it)==3: break
    if len(it)<2: return
    j=next(k for k,s in enumerate(x['fr']) if s['k'] in ('nbkanji','nbvocab') and not any(t['k']=='nbkanji' for t in x['fr'][k+1:k+2]))
    j=max(k for k,s in enumerate(x['fr']) if s['k'] in ('nbvocab','nbkanji'))
    x['fr'].insert(j+1,{'k':'nbwrite','g':G,'title':'Escreva à mão','items':it})
def integrate(cid,newjson,lang,drop):
    it=[]
    for f in sorted(glob.glob(R+'data/%s_*.json'%cid)): it+=json.load(open(f))
    new=json.load(open(newjson));ids={x['n'] for x in new}
    it=[x for x in it if x['n'] not in ids and not drop(x)]
    for x in new:
        if x.get('rev'): continue
        if lang=='fr': add_acc(x);add_dict(x)
        if lang=='de': add_art(x);add_dict(x)
        if lang=='ja': add_write(x)
    it+=new
    tmp='/tmp/_int_%s.json'%cid;json.dump(it,open(tmp,'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    n=r.data(cid,tmp);print(cid,'itens',n,'novos',len(new))
    return n
def add_arcs(cid,lst):
    s=open(R+'index.html',encoding='utf-8').read()
    m=re.search(r" '%s':\[(\[.*?\])\],\n"%re.escape(cid),s)
    assert m,cid
    have=set(re.findall(r"\[(\d+),'",m.group(1)))
    add=",".join("[%d,'%s']"%(n,t.replace("'","\\'")) for n,t in lst if str(n) not in have)
    if not add: return
    new=m.group(0).replace("]],\n","],"+add+"],\n") if m.group(0).endswith("]],\n") else None
    assert new
    open(R+'index.html','w',encoding='utf-8').write(s.replace(m.group(0),new,1))
