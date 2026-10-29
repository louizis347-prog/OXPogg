import json,glob,re
GENERIC={'🧩','🎚️','💡','🧭','🎙️','🪶','✍️','🎧'}
def sents(e):
    out=[]
    for x in e['fr']:
        if x['k']=='pgscene':out+=[(l[1],l[2] if len(l)>2 else '') for l in x['lines']]
        if x['k'] in('pgexp','verbs'):out+=[(i['ex'][0],i['ex'][1]) for i in x.get('items',[]) if len(i.get('ex',[]))>=2]
    return out
def build(e,old):
    S=sents(e);its=[];ptw={w[0].lower():w[1] for w in e['v']}
    for it in old['items']:
        w=it.get('say','');fig=it.get('fig','')
        if not w or not fig or fig in GENERIC:return None
        pat=re.compile(r'\b'+re.escape(w)+r'(s|es)?\b',re.I)
        cand=[(a,b) for a,b in S if pat.search(a) and len(a.split())>=4]
        if not cand:continue
        a,b=min(cand,key=lambda t:len(t[0]))
        m=pat.search(a)
        its.append({'w':m.group(0),'e':fig,'s':a[:m.start()]+'___'+a[m.end():],'pt':ptw.get(w.lower(),'')})
    if len(its)<4:return None
    board=[it['fig'] for it in old['items']]
    f={'k':'pgfind','title':'Ache no cenário','items':its,'board':board[:7]}
    for k in('rs','chars','bubble','avatar'):
        if k in old:f[k]=old[k]
    f['bubble']=[(old.get('bubble') or ['Poggie'])[0],'Read the clue and find it in the scene.','Leia a pista e ache no cenário.']
    f['say']='Descubra pela frase qual objeto está faltando.'
    return f
n=0
for fn in sorted(glob.glob('data/en-*.json')):
    d=json.load(open(fn));ch=False
    for e in d:
        fr=e['fr']
        ps=[i for i,x in enumerate(fr) if x['k']=='pgsheet']
        if len(ps)<2:continue
        i=ps[1];x=fr[i]
        if x['k']=='pgsheet' and x.get('items') and 'fig' in x['items'][0] and 'say' in x['items'][0] and all(isinstance(o,str) for o in x['items'][0].get('opts',[])) and 'Ouça' not in (x.get('title') or ''):
            f=build(e,x)
            if f:fr[i]=f;ch=True;n+=1
    if ch:json.dump(d,open(fn,'w'),ensure_ascii=False,separators=(',',':'))
print(n)
