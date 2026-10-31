import json,glob,re
from swap_works import rep
def load(n):
    for fn in glob.glob('data/en-*.json'):
        d=json.load(open(fn))
        for i,e in enumerate(d):
            if e['n']==n:return fn,d,i
def save(fn,d):json.dump(d,open(fn,'w'),ensure_ascii=False,separators=(',',':'))
# 1) 7083135: o título certo é Moby-Dick (a descrição e as cenas já são dele)
fn,d,i=load(7083135);e=d[i]
e=rep(e,lambda s:s.replace('The Diving Bell and the Butterfly','Moby-Dick'))
d[i]=e;save(fn,d)
# 2) 83071: obra certa = Harriet the Spy
fn,d,i=load(83071);e=d[i]
DESC='A referência é a menina que observa as pessoas e descreve o que cada uma está fazendo, descrição por particípio. Em Harriet the Spy, de Louise Fitzhugh, a menina Harriet M. Welsch segue as pessoas do bairro, em Nova York, e anota tudo num caderno. A aula usa esse olhar: descrever quem está fazendo o quê.'
old_d=e['a']['d']
def f(s):
    s=s.replace(old_d,DESC)
    s=s.replace('é o canal com o homem parado ali, descrição por particípio','é a menina que observa as pessoas e descreve o que cada uma está fazendo')
    s=s.replace('Em O Apanhador no Campo de Centeio, o adolescente Holden Caulfield passa dias em Nova York depois de deixar o colégio e observa as pessoas ao redor com olhar crítico.','Em Harriet the Spy, de Louise Fitzhugh, a menina Harriet M. Welsch segue as pessoas do bairro, em Nova York, e anota tudo num caderno.')
    s=s.replace('the narrator keeps watching people pretending to be nice','the girl keeps watching people and writing notes')
    s=s.replace('romance de J. D. Salinger · 1951','romance infantil de Louise Fitzhugh · 1964')
    s=s.replace('The Erie Canal · 1951','Harriet the Spy · 1964')
    s=s.replace('The Erie Canal','Harriet the Spy')
    return s
e=rep(e,f);e['a'].update(w='Harriet the Spy',y='1964',k='romance infantil de Louise Fitzhugh',d=DESC)
d[i]=e;save(fn,d)
# 3) 83105: obra certa = Their Eyes Were Watching God (Hurston); elenco Lockwood/Nelly -> Pheoby/Janie
fn,d,i=load(83105);e=d[i]
old_d=e['a']['d'];tail=old_d[old_d.find('A narrativa é quase toda'):]
DESC2='Em Their Eyes Were Watching God, de Zora Neale Hurston, Janie volta para casa e conta sua vida à amiga Pheoby, na varanda, entre histórias de famílias e de amores. '+tail
def g(s):
    s=s.replace(old_d,DESC2)
    s=s.replace('Em Their Eyes Were Watching God, o inquilino Lockwood ouve de Nelly Dean a história das famílias Earnshaw e Linton nas charnecas inglesas.','Em Their Eyes Were Watching God, de Zora Neale Hurston, Janie volta para casa e conta sua vida à amiga Pheoby, na varanda.')
    s=s.replace('romance de Emily Brontë · 1847','romance de Zora Neale Hurston · 1937').replace('Their Eyes Were Watching God · 1847','Their Eyes Were Watching God · 1937')
    s=s.replace('a história contada por Nelly','a história contada por Janie')
    s=re.sub(r'\bLockwood\b','Pheoby',s);s=re.sub(r'\bNelly\b','Janie',s)
    return s
e=rep(e,g);e['a'].update(y='1937',k='romance de Zora Neale Hurston',d=DESC2)
if isinstance(e['fr'][3].get('cast'),dict):pass
d[i]=e;save(fn,d)
