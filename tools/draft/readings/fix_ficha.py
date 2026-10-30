import json,glob,sys,os
D=os.path.dirname(os.path.abspath(__file__))
# n: (obra_antiga, obra_nova, ano, tipo, descricao, autor, intro, fato)
F={
82033:("The Gift of the Magi","An Occurrence at Owl Creek Bridge","1890","📖 Conto","“An Occurrence at Owl Creek Bridge” é um conto de Ambrose Bierce, de 1890, sobre um homem numa ponte durante a Guerra Civil Americana e um final famoso.","Ambrose Bierce","Em **An Occurrence at Owl Creek Bridge**, tudo muda na última linha. Hoje falamos de **contrastes e finais irônicos**: *However, he never arrived.*","O conto de Bierce é famoso pelo final inesperado e é estudado em aulas de literatura."),
82034:("Songs in the Key of Life","Songs in the Key of Life","1976","💿 Álbum","“Songs in the Key of Life” é um álbum duplo de Stevie Wonder, lançado em 1976, com músicas como “I Wish” e “Sir Duke”.","Stevie Wonder","Em **Songs in the Key of Life**, Stevie Wonder reúne canções sobre vida, amor e tempo. Hoje falamos de **o que você tem feito ultimamente**: *What have you been doing?*","Stevie Wonder levou cerca de dois anos para concluir o álbum duplo."),
82041:("Casablanca","Coming to America","1988","🎬 Filme","“Coming to America” (Um Príncipe em Nova York) é uma comédia de 1988 com Eddie Murphy, sobre um príncipe africano que chega ao Queens.","John Landis","Em **Coming to America**, o príncipe Akeem acaba de chegar a Nova York. Hoje falamos de **chegadas recentes**: *We just got here.*","O filme foi dirigido por John Landis e estreou em 1988."),
82042:("The Hound of the Baskervilles","Gone Girl","2012","🔎 Livro","“Gone Girl” (Garota Exemplar) é um romance de 2012 de Gillian Flynn, adaptado ao cinema em 2014, sobre o desaparecimento de uma esposa.","Gillian Flynn","Em **Gone Girl**, uma mulher desaparece no dia do aniversário de casamento. Hoje falamos de **relatar o que sumiu**: *My wife has gone missing.*","O filme de 2014 foi dirigido por David Fincher."),
82063:("Doctor Strangelove","Doctor Strangelove","1964","🎬 Filme","“Doctor Strangelove” (Dr. Fantástico) é uma comédia de humor negro de 1964 dirigida por Stanley Kubrick sobre o medo da guerra nuclear.","Stanley Kubrick","Em **Doctor Strangelove**, tudo está quase pronto, mas ainda não. Hoje falamos de **quase, mas ainda não**: *Not quite yet.*","O filme de Kubrick foi lançado em 1964, durante a Guerra Fria."),
82065:("Long Day's Journey into Night","Long Day's Journey into Night","1956","🎭 Peça","“Long Day's Journey into Night” é uma peça de Eugene O'Neill, encenada pela primeira vez em 1956, sobre uma família durante um único dia em 1912.","Eugene O'Neill","Em **Long Day's Journey into Night**, uma família fala dos seus planos durante um dia inteiro. Hoje falamos de **planos futuros**: *I'm going to study business.*","Eugene O'Neill ganhou o Prêmio Pulitzer por essa peça, em 1957."),
82068:("Rosencrantz and Guildenstern Are Dead","Rosencrantz and Guildenstern Are Dead","1966","🎭 Peça","“Rosencrantz and Guildenstern Are Dead” é uma peça de 1966 de Tom Stoppard que reconta Hamlet pelos olhos de dois personagens secundários.","Tom Stoppard","Em **Rosencrantz and Guildenstern Are Dead**, dois homens esperam compromissos que não entendem. Hoje falamos de **compromissos combinados**: *I'm meeting him at five.*","A peça de Tom Stoppard estreou em 1966 e o tornou famoso."),
82076:("The Glass Palace","The Time Machine","1895","📖 Livro","“A Máquina do Tempo” (The Time Machine) é um romance de ficção científica de H. G. Wells, de 1895, sobre um cientista que viaja ao futuro distante.","H. G. Wells","Em **The Time Machine**, um viajante promete contar tudo quando voltar. Hoje falamos de **orações de tempo**: *When I come back, I will tell you.*","H. G. Wells publicou o romance em 1895 e popularizou a ideia de máquina do tempo."),
82080:("The Go-Between","The Go-Between","1953","📖 Livro","“The Go-Between” é um romance de 1953 de L. P. Hartley, sobre um menino que entrega cartas secretas num verão inglês.","L. P. Hartley","Em **The Go-Between**, um menino leva mensagens entre dois adultos e logo descobre o peso delas. Hoje revisamos o **futuro**: *I'm going to deliver it. I will tell you.*","O romance de Hartley abre com a frase famosa: “O passado é um país estrangeiro.”"),
930018:("Fill in the Blank","Fill in the Blank","exercício","📝 Exercício","“Fill in the Blank” é o clássico exercício de completar lacunas, usado em aulas e em formulários, e serve de ponte para os verbos fill in e fill out.","","Hoje partimos do exercício **Fill in the Blank**, em que completamos lacunas. Falamos de **fill in, fill out e fill up**: *Please fill in this form.*","Em inglês britânico se diz fill in a form; em americano, fill out a form."),
82106:("The Firebird","The Firebird","1910","🎭 Balé","“O Pássaro de Fogo” (The Firebird) é um balé de Igor Stravinsky, de 1910, baseado num conto popular russo sobre um príncipe e uma ave mágica.","Igor Stravinsky","Em **The Firebird**, o príncipe Ivan recebe uma pena mágica e não precisa se apressar. Hoje falamos do que **não é necessário**: *You needn't hurry.*","Stravinsky tinha 28 anos quando o balé estreou em Paris."),
82120:("Nighthawks","Nighthawks","1942","🖼️ Pintura","“Nighthawks” é uma pintura de 1942 do artista americano Edward Hopper, que mostra pessoas numa lanchonete à noite.","Edward Hopper","Em **Nighthawks**, a luz de uma lanchonete ilumina a noite vazia. Hoje falamos de **como as coisas são feitas**: *Cars are made in factories.*","A pintura de Hopper está no Art Institute of Chicago."),
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
