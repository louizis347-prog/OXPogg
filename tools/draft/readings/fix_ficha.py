import json,glob,sys,os
D=os.path.dirname(os.path.abspath(__file__))
# n: (obra_antiga, obra_nova, ano, tipo, descricao, autor, intro, fato)
F={
82033:("The Gift of the Magi","An Occurrence at Owl Creek Bridge","1890","📖 Conto","“An Occurrence at Owl Creek Bridge” é um conto de Ambrose Bierce, de 1890, sobre um homem numa ponte durante a Guerra Civil Americana e um final famoso.","Ambrose Bierce","Em **An Occurrence at Owl Creek Bridge**, tudo muda na última linha. Hoje falamos de **contrastes e finais irônicos**: *However, he never arrived.*","O conto de Bierce é famoso pelo final inesperado e é estudado em aulas de literatura."),
82034:("Songs in the Key of Life","Songs in the Key of Life","1976","💿 Álbum","“Songs in the Key of Life” é um álbum duplo de Stevie Wonder, lançado em 1976, com músicas como “I Wish” e “Sir Duke”.","Stevie Wonder","Em **Songs in the Key of Life**, Stevie Wonder reúne canções sobre vida, amor e tempo. Hoje falamos de **o que você tem feito ultimamente**: *What have you been doing?*","Stevie Wonder levou cerca de dois anos para concluir o álbum duplo."),
82041:("Casablanca","Coming to America","1988","🎬 Filme","“Coming to America” (Um Príncipe em Nova York) é uma comédia de 1988 com Eddie Murphy, sobre um príncipe africano que chega ao Queens.","John Landis","Em **Coming to America**, o príncipe Akeem acaba de chegar a Nova York. Hoje falamos de **chegadas recentes**: *We just got here.*","O filme foi dirigido por John Landis e estreou em 1988."),
82042:("The Hound of the Baskervilles","Gone Girl","2012","🔎 Livro","“Gone Girl” (Garota Exemplar) é um romance de 2012 de Gillian Flynn, adaptado ao cinema em 2014, sobre o desaparecimento de uma esposa.","Gillian Flynn","Em **Gone Girl**, uma mulher desaparece no dia do aniversário de casamento. Hoje falamos de **relatar o que sumiu**: *My wife has gone missing.*","O filme de 2014 foi dirigido por David Fincher."),
82048:("Groundhog Day","Russian Doll","2019","📺 Série","“Russian Doll” é uma série da Netflix de 2019 sobre uma mulher que revive a mesma noite de aniversário em Nova York.","Natasha Lyonne","Em **Russian Doll**, Nadia acorda sempre no mesmo banheiro. Hoje falamos de **quantas vezes algo aconteceu**: *How many times have you tried?*","A série foi criada por Natasha Lyonne, Leslye Headland e Amy Poehler."),
7082035:("Long Time No See","Long Time No See","expressão","💬 Expressão","“Long time no see” é uma saudação informal do inglês, usada quando duas pessoas se reencontram depois de muito tempo.","","Hoje partimos da expressão **Long time no see**, usada quando nos reencontramos. Falamos de **há quanto tempo**: *How long have you…?*","A frase é tão comum que aparece em conversas do dia a dia no mundo todo."),
}
def fix(e,v):
    old,new,y,k,d,by,intro,fact=v
    s=json.dumps(e,ensure_ascii=False)
    if old!=new:s=s.replace(old,new)
    e2=json.loads(s)
    e2['a'].update({'w':new,'y':y,'k':k,'d':d})
    for fr in e2['fr']:
        cw=fr.get('cw')
        if cw:
            cw.update({'work':new,'year':y,'kind':k,'intro':intro})
            if by:cw['by']=by
            if isinstance(cw.get('fact'),list):cw['fact'][-1]=fact
    return e2
for fn in sorted(glob.glob(D+'/../../../data/en-b1_*.json')):
    d=json.load(open(fn));ch=False
    for i,e in enumerate(d):
        if e['n'] in F:
            d[i]=fix(e,F[e['n']]);ch=True
    if ch:json.dump(d,open(fn,'w'),ensure_ascii=False,separators=(',',':'))
print('ok')
