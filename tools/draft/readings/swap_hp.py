import json,glob,re
from swap_works import rep
NEW='Harry Potter and the Chamber of Secrets'
D='Harry Potter and the Chamber of Secrets é o segundo livro da série de J. K. Rowling, de 1998. Colin Creevey chega novo à escola de magia de Hogwarts, apresenta-se a todo mundo e tenta fazer amigos. A referência abre com alguém novo se apresentando: o modelo de I am e you are.'
M=[('Call me Ishmael','Call me Colin'),('Pode me chamar de Ishmael','Pode me chamar de Colin'),('Moby-Dick de novo','Hogwarts de novo'),
('Capitão Ahab','Hagrid'),('Captain Ahab','Hagrid'),('What\'s up, Captain?','What\'s up, Hagrid?'),('E aí, Capitão?','E aí, Hagrid?'),
('A school of whales','A school of wizards'),('a school of whales','a school of wizards'),('This is a school of whales','This is a school of wizards'),('Isto é um cardume de baleias','Isto é uma escola de bruxos'),
('Say the word: whale','Say the word: wizard'),('Diga a palavra: baleia','Diga a palavra: bruxo'),('Whale!','Wizard!'),('Baleia!','Bruxo!'),
('first class at sea','first class at school'),('primeira aula no mar','primeira aula na escola'),('I am new on the ship','I am new at the castle'),
('Welcome to the ship','Welcome to Hogwarts'),('Bem-vindo ao navio','Bem-vindo a Hogwarts'),('como o Ishmael ao chegar ao navio','como o Colin ao chegar ao castelo'),('navio-escola','escola de bruxos'),
('Pequod','Hogwarts'),('Starbuck','Hermione'),('Ishmael','Colin'),('Ahab','Hagrid')]
def fn(s,old_d):
    s=s.replace(old_d,D)
    s=s.replace('A referência abre com o narrador se apresentando, “Call me Ishmael”, o modelo de I am e you are. Romance do escritor americano Herman Melville, de 1851.','Harry Potter and the Chamber of Secrets é o segundo livro de J. K. Rowling, de 1998.')
    s=re.sub(r'Romance do escritor americano Herman Melville, de 1851\. O narrador, Ishmael, embarca no navio baleeiro Pequod, comandado pelo capitão Ahab, que persegue a grande baleia branca, Moby Dick\. O livro começa com a frase “Call me Ishmael\.”\.?','Colin Creevey chega novo à escola de magia de Hogwarts, apresenta-se a todo mundo e tenta fazer amigos.',s)
    s=s.replace('Moby-Dick · 1851',NEW+' · 1998').replace('“Moby-Dick” is a novel by Herman Melville, from 1851.','“Harry Potter and the Chamber of Secrets” is the second book in J. K. Rowling\'s series, from 1998.').replace('“Moby Dick” é um romance de Herman Melville, de 1851.','“Harry Potter and the Chamber of Secrets” é o segundo livro da série de J. K. Rowling, de 1998.')
    s=s.replace('Moby-Dick abre com o narrador se apresentando, “Call me Ishmael”, o modelo de I am e you are.','Hogwarts recebe um aluno novo que se apresenta: o modelo de I am e you are.')
    s=s.replace('Moby-Dick',NEW)
    for a,b in M:s=s.replace(a,b)
    return s
for f in sorted(glob.glob('data/en-a1_*.json')):
    d=json.load(open(f));ch=False
    for i,e in enumerate(d):
        if e['n']==10151:
            old_d=e['a']['d'];e2=rep(e,lambda s:fn(s,old_d))
            e2['a'].update(w=NEW,y='1998',k='📖 Romance',d=D)
            e2['fr']=[x for x in e2['fr'] if not(x['k']=='rdg' and x.get('obra')) and x['k']!='pgdlg']
            d[i]=e2;ch=True
    if ch:json.dump(d,open(f,'w'),ensure_ascii=False,separators=(',',':'))
