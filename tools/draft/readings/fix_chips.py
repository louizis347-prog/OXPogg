import json,glob,re,os
D=os.path.dirname(os.path.abspath(__file__))
# (ep,linha,chip): (EN errada, PT errada)  -- EN/PT certas ficam como estão
M={
(82106,5,0):('too','demais'),(930034,3,0):('start','início'),(930057,2,0):('start','largada'),
(7082252,2,0):('bandage','curativo'),(82252,5,0):('basket','cesto'),(7082323,5,0):('basket','cesto'),
(7082252,5,0):('wet','molhado'),(7082286,3,0):('July','julho'),(7930065,4,0):('shoes','sapatos'),
(82305,3,0):('never','nunca'),(7082312,2,0):('flattering','lisonjeando'),(7930067,3,0):('upload','enviá-lo'),
(7930067,4,0):('download','baixe'),(930072,5,0):('width','largura'),(7930073,2,0):('leaf','folha'),
(81278,2,0):('improbable','improvável'),(7081278,3,0):('quietness','quietness'),(82271,0,0):('has rose','subiram'),
(82350,5,0):('challenge','desafio'),(82271,4,0):('fossil fuels','combustíveis fósseis'),
(7082236,3,0):('vouchers','vales'),(82296,5,0):('playlists','playlists'),(7082325,2,0):('necklines','decotes'),
(930073,5,0):('burdens','fardos'),(82252,2,0):('bruises','hematomas'),(930010,5,0):('orientations','orientações'),
(930011,4,0):('no hard feeling','sem ressentimento'),(82078,4,0):('meet far','encontrar longe'),
(7930016,3,0):('stick apart','ficar separados'),(7930017,3,0):('discharge','descarregar'),
(930025,3,0):('shy','tímido'),(7930027,3,0):('presents','presentes'),(7082127,4,0):('deliveries','entregas'),
(930029,3,0):('milestone','marco'),(7082134,5,0):('dragonfly','libélula'),(7082210,1,0):('dragonfly','libélula'),
(930030,3,0):('speaking','falando'),(7930030,5,0):('speaking','falando'),(930035,1,0):('Just kidded','Brincou'),
(7930035,3,0):('serious','sério'),(82170,4,0):('skylines','horizontes'),(7082175,4,0):('timetables','horários'),
(82197,3,0):('seem','parecem'),(81046,4,0):('fear','medos'),(7082209,4,0):('pizza','pizza'),
(7082193,3,0):('spare times','tempos livres'),(82225,4,0):('gratitude','gratidão'),(7930075,2,0):('gratitude','gratidão'),
(7082225,4,0):('chances','chances'),(7082228,3,0):('deposits','sinais'),(930052,0,0):('busting','pegando'),
(82241,1,0):('more spectacular','espetacular demais'),(82241,3,0):('breathless','sem fôlego'),
(7082298,4,0):('imaginary','imaginário'),(7082301,2,0):('overcooked','cozido demais'),
(82288,2,0):('attention','atenção'),(82229,5,0):('bags','malas'),(82246,4,0):('tomorrow','amanhã'),
(7930049,2,0):('today','hoje'),(82239,2,0):('Easter','Páscoa'),(7930047,4,0):('striker','atacante'),
(930047,3,0):('player','jogador'),(82218,0,0):('everything','tudo'),(7930048,4,0):('disaster','desastre'),
(7930071,2,0):('disaster','desastre'),(7082228,4,0):('disaster','desastre'),(82221,2,0):('Receipt','Recibo'),
(7082221,3,0):('urgency','urgência'),(82318,3,0):('balloon','balão'),(82231,2,0):('sweet','doce'),
(7082250,5,0):('dinner','jantar'),(7082260,3,0):('screen','tela'),(7082267,3,0):('console','console'),
(82269,3,0):('plugged out','desconectado'),(82274,4,0):('telescopes','telescópios'),
(7082275,1,0):('most peaceful','a mais pacífica'),(7082275,4,0):('frog','sapo'),(82279,2,0):('musical','musical'),
(82286,3,0):('dollars','dólares'),(82286,1,0):('terminal','terminal'),(7082289,4,0):('vocal','vocal'),
(7930062,3,0):('Pleased','Satisfeito'),(7082299,1,0):('performer','artista'),(7082299,4,0):('interview','entrevista'),
(82301,2,0):('cold','frio'),(82302,4,0):('ginger','gengibre'),(930065,5,0):('occupation','ocupação'),
(82324,3,0):('library','biblioteca'),(7082324,5,0):('spoon','colher'),(7082325,1,0):('silk','seda'),
(82341,4,0):('importance','importância'),(7082224,2,0):('imbalance','desequilíbrio'),(82266,2,0):('replays','reproduz'),
}
PTFIX={(7082224,2):('Quero um melhor equilíbrio entre vida e {trabalho|lastro}.','Quero um melhor {equilíbrio|desequilíbrio} entre vida e trabalho.'),
(82266,2):('Eu {reouço|reouve}','Eu {ouço de novo|ouve de novo}')}
CH=re.compile(r"\{([^{}|]+)\|([^{}|]+)\}")
def sub(s,j,new):
    k=[-1]
    def r(m):
        k[0]+=1
        return '{%s|%s}'%(m.group(1),new) if k[0]==j else m.group(0)
    return CH.sub(r,s)
n=0
for fn in sorted(glob.glob(D+'/../../../data/en-b1_*.json')):
    d=json.load(open(fn));ch=False
    for e in d:
        for fr in e['fr']:
            if fr['k']!='pgdlg':continue
            for i,l in enumerate(fr['lines']):
                for j in range(4):
                    key=(e['n'],i,j)
                    if key in M:
                        en,pt=M[key]
                        if (e['n'],i) in PTFIX:
                            a,b=PTFIX[(e['n'],i)]
                            if a in l[2]:l[2]=l[2].replace(a,b)
                            l[1]=sub(l[1],j,en);n+=1;continue
                        l[1]=sub(l[1],j,en);l[2]=sub(l[2],j,pt);n+=1
            ch=True
    if ch:json.dump(d,open(fn,'w'),ensure_ascii=False,separators=(',',':'))
print('chips trocados',n)
