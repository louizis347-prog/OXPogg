import json,glob,re,zlib
def windows(e):
    W=[]
    for x in e['fr']:
        if x['k']=='pgscene':
            L=x['lines']
            for i in range(len(L)-1):
                a,b=L[i],L[i+1]
                nw=len(a[1].split())+len(b[1].split())
                if 8<=nw<=30:W.append((a,b,nw,len(W)))
    return W
def build(e,old):
    W=windows(e)
    if len(W)<6:return None
    exps=[(x.get('en') or x.get('x') or '').lower() for fr in e['fr'] if fr['k']=='pgexp' for x in fr['items']]
    sc=lambda w:sum(1 for q in exps if q and q.split()[0][:4] in (w[0][1]+' '+w[1][1]).lower())
    order=sorted(range(len(W)),key=lambda i:(-sc(W[i]),i))
    chosen=[];used=set()
    for i in order:
        a,b=W[i][0],W[i][1]
        if a[1] in used or b[1] in used:continue
        chosen.append(i);used.add(a[1]);used.add(b[1])
        if len(chosen)==4:break
    if len(chosen)<3:return None
    items=[]
    for n,i in enumerate(sorted(chosen)):
        w=W[i];txt=lambda t:t[0][1]+' '+t[1][1]
        others=[j for j in range(len(W)) if j!=i and W[j][0][1]!=w[0][1] and W[j][1][1]!=w[1][1] and W[j][0][1]!=w[1][1]]
        others.sort(key=lambda j:(abs(W[j][2]-w[2]),j))
        d=[txt(W[j]) for j in others[:2]]
        if len(d)<2:return None
        pos=zlib.crc32((str(e['n'])+str(n)).encode())%3
        opts=d[:];opts.insert(pos,txt(w))
        items.append({'fig':'🎧','say':txt(w),'ask':'Ouça o trecho e marque o que você escutou.','opts':opts,'a':pos,
          'why':'%s e %s: “%s” — %s %s'%(w[0][0],w[1][0],txt(w),w[0][2],w[1][2])})
    f=dict(old);f['items']=items;f['title']='Ouça o trecho da cena'
    f['bubble']=[(old.get('bubble') or ['Poggie'])[0],'Listen, then pick what you heard.','Ouça e escolha o que escutou.']
    return f
B={ 'lac':('Fill in the missing piece.','Complete a peça que falta.'),
    'comp':('What do you remember from the scene?','O que você lembra da cena?'),
    'voc':('Listen and pick the word.','Ouça e escolha a palavra.'),
    'snd':('Listen and tap the one you hear.','Ouça e toque no que você escuta.'),
    'wr':('Write it from memory.','Escreva de memória.'),
    'fit':('Which one fits best?','Qual combina melhor?')}
def kind(x):
    it=x.get('items') or []
    if not it:return None
    t=x.get('title') or ''
    if any('___' in (i.get('text') or '') for i in it):return 'lac'
    if 'ouça o trecho' in t.lower():return None
    if any(i.get('pic') for i in it) or all(len(i.get('opts',[]))==2 and all(isinstance(o,str) for o in i['opts']) and 'pronún' in (i.get('ask') or '').lower()+'' for i in it):return 'snd'
    if any('escreva' in (i.get('ask') or '').lower() or 'trace' in (i.get('ask') or '').lower() for i in it):return 'wr'
    if 'speak' in it[0] and 'pt' in it[0]:return 'comp'
    if 'fig' in it[0] and 'say' in it[0]:
        a=(it[0].get('ask') or '').lower()
        if 'som' in t.lower() or 'sons' in t.lower() or 'pistas' in t.lower() and 'som' in a:return 'snd'
        return 'voc'
    if not (it[0].get('text')):return 'fit'
    return None
n1=n2=0
for fn in sorted(glob.glob('data/en-*.json')):
    d=json.load(open(fn));ch=False
    for e in d:
        for i,x in enumerate(e['fr']):
            if x['k']!='pgsheet':continue
            if x.get('title')=='Ouça e escolha a fala':
                f=build(e,x)
                if f:e['fr'][i]=x=f;n1+=1;ch=True
            k=kind(x)
            if k and x.get('bubble'):
                nb=[x['bubble'][0],*B[k]]
                if x['bubble']!=nb:x['bubble']=nb;n2+=1;ch=True
    if ch:json.dump(d,open(fn,'w'),ensure_ascii=False,separators=(',',':'))
print(n1,n2)
