import json,glob,re,os
D=os.path.dirname(os.path.abspath(__file__))
STOP=set('he she it we they now let time there the and of is are take crown eat prices friday suppose imagine have what while one this that when how who with for you your i a an to in on at by from tell look bring dream hello reino unido irmãos país maravilhas centeio novo mundial nova tira férias compra svovlstikkerne canada posthumous club'.split())
SPARE=['Alex','Jordan','Sam','Max','Ben','Mia']
def sus(name,by):
    ws=re.findall(r"\w+",name.lower())
    if all(w in STOP for w in ws):return True
    bw=set(re.findall(r"\w+",by.lower()))
    return bool(ws) and bool(bw) and all(w in bw for w in ws) and len(ws)==1 and name not in('Pi',)
tot=0
for fn in sorted(glob.glob(D+'/../../../data/en-*.json')):
    d=json.load(open(fn));ch=False
    for e in d:
        by=''
        for fr in e['fr']:
            if fr['k']=='cover' and fr.get('cw'):by=fr['cw'].get('by','')
        for m_ in re.findall(r"(?:por|pelo|pela|de|do|da) ((?:[A-Z][\w'.-]+ ?){2,3})",e['a'].get('d','')):by+=' '+m_
        names=[]
        for fr in e['fr']:
            if fr['k']=='pgscene':
                for n in fr['cast']:
                    if n not in names:names.append(n)
        bad=[n for n in names if sus(n,by)]
        if not bad:continue
        free=[s for s in SPARE if s not in names]
        m={n:free[i] for i,n in enumerate(bad)}
        for fr in e['fr']:
            if fr['k']=='pgscene':
                fr['cast']={m.get(n,n):v for n,v in fr['cast'].items()}
                for l in fr['lines']:
                    l[0]=m.get(l[0],l[0])
        ch=True;tot+=1
    if ch:json.dump(d,open(fn,'w'),ensure_ascii=False,separators=(',',':'))
print('episódios com elenco corrigido',tot)
