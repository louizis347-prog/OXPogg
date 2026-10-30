"""Ordem pedagógica do Pocket A1.
1) Trilha inicial CURADA à mão (apresentar-se, números e tempo, pedir, minha vida, lugares e casa).
2) O resto entra por estágio (tema + dificuldade), com variedade: nunca dois episódios seguidos do mesmo arco.
Gera ordem_a1.json e mapa_a1.csv."""
import glob,json,re,csv,os
src=open('build.py').read().replace('\nmain()','\n')
ns={'__file__':os.path.abspath('build.py')};exec(compile(src,'build.py','exec'),ns);load=ns['load']
eps=[]
for fn in sorted(glob.glob('a1_arco*.txt')+glob.glob('a1_arco*.py')):
    a=int(re.search(r'arco(\d+)',fn).group(1))
    cur=a;marks=[]
    if fn.endswith('.txt'):
        for l in open(fn):
            if l.startswith('# Arco'):cur=int(re.search(r'Arco (\d+)',l).group(1))
            if l.startswith('T:'):marks.append(cur)
    for k,x in enumerate(load(fn).EPS):
        x['_f']=marks[k] if k<len(marks) else a;x['_k']=k;eps.append(x)
by={x['t']:x for x in eps}
# ---------- trilha curada (títulos) ----------
TRILHA=[
# 1. Primeiros contatos
('1 Primeiros contatos',['Nice to meet you','How are you?','Say hello in many languages','Where are you from?','Nationalities','What languages do you speak?',
 'Count with me','What time is it?','Telling the time','Days of the week','Months of the year',"Today's date",'Happy birthday!','Happy New Year!']),
# 2. Pedir e perguntar o básico
('2 Pedir o básico',['A coffee, please','How much is it?','Price check','Give change','Weight and size','My phone number','A dozen eggs','Where is the restroom?','A table for two',
 'Is this seat free?','One ticket, please','To the airport, please','Two tickets, please','Where is gate 12?','Which way to the station?',
 'I am so sorry','Thanks a lot','Can you help me?','Could you repeat that?','I do not understand']),
# 3. Eu, família e gente
('3 Eu e as pessoas',['This is my family','How old are you?','I have two brothers','Do you have pets?','My dog and my cat','I like pizza','What do you do?',
 'Jobs around us','Where do you work?','Meet my family!','Meet my friends','What does he look like?','What is she like?',"My favorite color",'What color?',
 'What are you wearing?','My birthday is in May','What is your favorite season?','A sunny day','How are you feeling?','I think it is great','Who is that?',
 'I miss you','A little about me','My first week in English']),
# 4. Lugares, casa e cidade
('4 Lugares e casa',['Where is the milk?','Is there a bakery nearby?','Is there a bank near here?','My bedroom','In the kitchen','Living room','The bathroom',
 'Which room is this?','In the garden','Where is the sofa?','I am looking for an apartment','How much is the rent?','Is it furnished?','My address is…',
 'Meet the neighbor','Nice to meet the neighbors','Housewarming party','Welcome home','Does this bus go downtown?','What is the next stop?','Getting around town',
 'Central Park','My neighborhood','The corner store','At the post office','At the bank','At the library','Where is it?','Find it in the store','At the supermarket',
 'Where is the classroom?','A campus tour','Is this the right office?']),
]

FIM=['Everything you know','Look how much you know','A full day']
DIA=lambda n:n<=21 or (n>=42 and n%2==0)
usados=set();ordem=[]
for nome,lst in TRILHA:
    for t in lst:
        if t in by and t not in usados:ordem.append((nome,t));usados.add(t)
        elif t not in by:print('FALTA',t)
def dif(x):
    t=' '.join(l[1] for l in x['dlg']).lower()
    s=len(t.split())/18
    for p,w in [(r"\b(am|is|are) \w+ing\b",3),(r"\b(he|she|it) \w+s\b",2),(r"\bcan\b",1),(r"\b(would like|may i|could you)\b",2),(r"\bbecause\b",2),(r"\b(bigger|cheaper|best|most|more)\b",2)]:
        s+=min(len(re.findall(p,t)),3)*w
    return s
resto=[x for x in eps if x['t'] not in usados and x['t'] not in FIM]
unid={}
for x in resto:unid.setdefault(x['_f'],[]).append(x)
for u in unid.values():u.sort(key=lambda x:x['_k'])
ORD_DIA=[1,2,3,4,46,5,6,7,42,8,50,9,44,10,52,11,12,48,13,58,14,54,15,16,19,20,21,56]
ORD_TEMA=[22,23,57,29,31,30,32,25,27,33,28,24,38,39,40,26,34,45,47,49,59,41,43,51,35,36,37,53,55]
def fluxo(dia):
    ordem_u=ORD_DIA if dia else ORD_TEMA
    resto_u=[n for n in unid if DIA(n)==dia and n not in ordem_u]
    if resto_u:print('unidades fora da lista',dia,resto_u)
    return [x for n in ordem_u+sorted(resto_u) if n in unid for x in unid[n]]
D=fluxo(True);T=fluxo(False)
# intercala em proporção: ímpar = dia a dia, par = tema
seq=[];i=j=0
while i<len(D) or j<len(T):
    ri=(i+.5)/len(D) if i<len(D) else 9
    rj=(j+.5)/len(T) if j<len(T) else 9
    if ri<=rj:seq.append(D[i]);i+=1
    else:seq.append(T[j]);j+=1
bl=lambda n:'5 Dia a dia + temas (módulo %d)'%((n//40)+1)
for n,x in enumerate(seq):ordem.append((bl(n),x['t']))
for t in FIM:
    if t in by and t not in usados:ordem.append(('Integração',t))
tit=[t for _,t in ordem]
assert len(tit)==len(set(tit))
faltam=[x['t'] for x in eps if x['t'] not in set(tit)]
print('episódios',len(eps),'ordenados',len(tit),'fora',faltam)
tit+=faltam
json.dump(tit,open('ordem_a1.json','w'),ensure_ascii=False,indent=0)
with open('mapa_a1.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(['ordem','bloco','titulo','padrao_chave','arco_origem','tipo','vocabulario'])
    nomes=dict((t,n) for n,t in ordem)
    for n,t in enumerate(tit,1):
        x=by[t];w.writerow([n,nomes.get(t,'?'),t,x['key'][0],x['_f'],'dia a dia' if DIA(x['_f']) else 'tema',';'.join(v[0] for v in x['vocab'])])
