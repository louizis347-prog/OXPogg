"""Revisão automática do texto do Pocket (arcos B1 36–45 e todo o A1): repetições, espaços, pontuação, números, inglês solto no PT e palavras raras. Não substitui revisão humana."""
import re,glob,collections
def load(pat):
    rows=[]
    for f in sorted(glob.glob(pat)):
        for i,l in enumerate(open(f),1):
            l=l.rstrip('\n')
            if l[:2] in('D:','K:','R:','S:','B:','V:','X:','M:','C:','T:'):rows.append((f,i,l))
    return rows
allrows=load('a1_arco*.txt')+load('a2_arco*.txt')+load('b1_arco*.txt')
def en_pt(l):
    t=l[:2];b=l[2:].lstrip();p=b.split('|')
    if t=='D:':return p[1:3] if len(p)>=3 else None
    if t in('K:','R:','B:'):return p[:2]
    if t=='S:':return [p[1],p[2],p[3],p[4]] if len(p)>=5 else None
W=collections.Counter()
for f,i,l in allrows:
    for m in re.findall(r"[A-Za-z']+",l):W[m.lower()]+=1
issues=[]
for f,i,l in load('b1_arco3[6-9].txt')+load('b1_arco4[0-5].txt')+load('a1_arco*.txt'):
    x=en_pt(l)
    if not x:continue
    pairs=[(x[0],x[1])] if len(x)==2 else [(x[0],x[1]),(x[2],x[3])]
    for en,pt in pairs:
        if re.search(r'\b(?!ha\b|five\b|seven\b|zero\b|one\b|two\b)(\w+) \1\b',en,re.I) and not re.search(r'\b(that that|had had)\b',en,re.I):issues.append((f,i,'repetida EN',en))
        if re.search(r'\b(?!ha\b|cinco\b|sete\b|zero\b|um\b|dois\b)(\w+) \1\b',pt,re.I):issues.append((f,i,'repetida PT',pt))
        if '  ' in en or '  ' in pt:issues.append((f,i,'espaço duplo',en))
        if re.search(r'[,.!?;:][A-Za-zÀ-ú]',en.replace('{0}','')) and not re.search(r'\d[.,]\d|\.com|e\.g|U\.S',en):issues.append((f,i,'falta espaço EN',en))
        if re.search(r'\b(the|and|with|you|your)\b',pt,re.I) and not re.search(r'"|“|\{0\}',pt):issues.append((f,i,'inglês solto no PT?',pt))
        if (en.strip()[-1:]=='?')!=(pt.strip()[-1:]=='?') and en.strip()[-1:] in '?.!' and pt.strip()[-1:] in '?.!':issues.append((f,i,'pontuação difere',en+' || '+pt))
        if en[:1].islower() and not en.startswith('{0}'):issues.append((f,i,'EN começa minúsculo',en))
        for n1 in re.findall(r'\d+',en):
            if n1 not in pt:issues.append((f,i,'número some no PT',en+' || '+pt))
print('achados:',len(issues))
for x in issues[:60]:print(x[0][-10:],x[1],x[2],'|',x[3][:110])
rare=collections.defaultdict(list)
for f,i,l in load('b1_arco3[6-9].txt')+load('b1_arco4[0-5].txt'):
    x=en_pt(l)
    if not x:continue
    for en in (x[::2] if len(x)==4 else x[:1]):
        for m in re.findall(r"[A-Za-z']+",en):
            if W[m.lower()]==1:rare[m.lower()].append(f[-6:-4])
print(len(rare));print(' '.join(sorted(rare)))
