import json,glob,re
from swap_works import rep
NEW='The Adventures of Pinocchio'
D='The Adventures of Pinocchio é um romance infantil do italiano Carlo Collodi, publicado em 1883, sobre um boneco de madeira que ganha vida e quer virar um menino de verdade. A referência é o boneco que precisa aprender bons hábitos: lavar as mãos, escovar os dentes.'
def fn(s,old_d):
    s=s.replace(old_d,D)
    s=s.replace('Goldilocks and the Three Bears · 1837',NEW+' · 1883')
    s=s.replace('“Goldilocks and the Three Bears” is an English fairy tale; Robert Southey published an early version in 1837.','“The Adventures of Pinocchio” is a children\'s novel by the Italian Carlo Collodi, published in 1883.')
    s=s.replace('traz uma menina entrando numa casa de ursos','traz um boneco de madeira que aprende bons hábitos')
    s=s.replace('Goldilocks and the Three Bears é um conto de fadas inglês, registrado por escrito pelo poeta Robert Southey em 1837. Uma visitante entra sozinha na ca','Goldilocks')
    s=s.replace('Goldilocks and the Three Bears',NEW)
    s=s.replace('Mama Bear combs her fur','Geppetto combs his hair').replace('Mama Bear ___ her fur','Geppetto ___ his hair')
    s=s.replace('washes her face','washes his face').replace('dries her face','dries his face')
    s=s.replace('A Mamãe Ursa penteia o pelo','Geppetto penteia o cabelo').replace('Mamãe Ursa penteia o pelo','Geppetto penteia o cabelo')
    s=s.replace('Mama Bear','Geppetto').replace('Goldilocks','Pinocchio')
    s=s.replace('Cachinhos Dourados','Pinóquio').replace('Cachinhos','Pinóquio').replace('Mamãe Ursa','Geppetto').replace('Mama Urso','Geppetto')
    return s
for f in sorted(glob.glob('data/en-a1_*.json')):
    d=json.load(open(f));ch=False
    for i,e in enumerate(d):
        if e['n']==80185:
            old_d=e['a']['d'];e2=rep(e,lambda s:fn(s,old_d))
            e2['a']['w']=NEW;e2['a']['y']='1883';e2['a']['k']='📖 Livro';e2['a']['d']=D
            e2['fr']=[x for x in e2['fr'] if not(x['k']=='rdg' and x.get('obra')) and x['k']!='pgdlg']
            d[i]=e2;ch=True
    if ch:json.dump(d,open(f,'w'),ensure_ascii=False,separators=(',',':'))
