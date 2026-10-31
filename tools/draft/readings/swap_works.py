"""Troca 8 obras repetidas por obras novas (nome, ano, tipo, descrição) em todo o JSON do episódio."""
import json,glob,re
OLD_NEW={
70052:dict(old=['Cafe Terrace at Night'],new='Cafe Society',y='2016',k='🎬 Filme',
  d='Cafe Society é um filme de 2016, escrito e dirigido por Woody Allen, que passa pelos anos 1930, de Hollywood a um clube noturno de Nova York, com mesas, garçons e música. A referência é o filme do café e do clube noturno, com mesas e lugares.',
  frag=[('Cafe Terrace at Night é uma pintura de Vincent van Gogh de um café ao ar livre à noite.','Cafe Society é um filme de 2016, escrito e dirigido por Woody Allen, que passa por Hollywood e por um clube noturno de Nova York.'),
        ('o quadro do café à noite','o filme do café e do clube noturno'),('___ Terrace at Night','___ Society')]),
81158:dict(old=['Three Billy Goats Gruff'],new='Goldilocks and the Three Bears',y='1837',k='📜 Conto de fadas',
  d='Goldilocks and the Three Bears é um conto de fadas inglês, registrado por escrito pelo poeta Robert Southey em 1837. Uma visitante entra sozinha na casa de três ursos e prova cadeiras, mingaus e camas. A referência mostra coisas grandes demais e pequenas demais, ótimo para dizer too big e too small.',
  frag=[('Three Billy Goats Gruff é o conto de três bodes que atravessam a ponte e enfrentam o troll.','Goldilocks and the Three Bears é o conto da menina que entra na casa dos três ursos e prova cadeiras grandes demais e pequenas demais.')]),
81288:dict(old=['Anthony Bourdain: Lugares Desconhecidos: Comida de Rua','Anthony Bourdain: Parts Unknown: Street food','Anthony Bourdain: Parts Unknown'],new='Street Food',y='2019',k='🌮 Série',
  d='Street Food é uma série documental da Netflix, de 2019, que visita cozinheiros de rua em cidades da Ásia e da América Latina. A obra conversa com o foco da aula: “pedir na rua: Can I have two tacos? How much is it? Would you like it spicy?”.',
  frag=[('Anthony Bourdain: Parts Unknown é uma série documental da CNN apresentada pelo chef e escritor Anthony Bourdain.','Street Food é uma série documental da Netflix, de 2019, que visita cozinheiros de rua em cidades da Ásia e da América Latina.')]),
7960121:dict(old=['Help!'],new='Gossip Girl',y='2007',k='📺 Série',
  d='Gossip Girl é uma série americana, de 2007, sobre adolescentes ricos de Manhattan cujos segredos viram boato num blog anônimo. A referência é a série do boato que se espalha: spread like wildfire.',
  frag=[('Help! é uma canção dos Beatles que pede ajuda.','Gossip Girl é uma série americana sobre adolescentes ricos de Manhattan e um blog de boatos.'),
        ('Help! is a Beatles song and a film.','Gossip Girl is a TV series about rich teenagers in Manhattan.'),
        ('Help! é uma canção e um filme dos Beatles.','Gossip Girl é uma série sobre adolescentes ricos de Manhattan.'),
        ('John Lennon later said it was a real cry for help.','A secret blog turns every rumor into news.'),
        ('John Lennon disse depois que era um pedido de socorro de verdade.','Um blog secreto transforma cada boato em notícia.'),
        ('é a canção do pedido de ajuda','é a série do boato que se espalha'),('é a canção do pedido de ajuda.','é a série do boato que se espalha.'),
        ('\\bHelp\\b','\\bGossip\\b')]),
930059:dict(old=['Wall Street'],new='Casino Royale',y='2006',k='🎬 Filme',
  d='Casino Royale é um filme de 2006, dirigido por Martin Campbell, em que o agente James Bond joga uma partida de pôquer de alto risco contra um vilão. Combina com falar de recuar de uma aposta e dar apoio ao aliado. A cena é autoral; não adapta o filme.',
  frag=[('Wall Street é um filme de 1987, dirigido por Oliver Stone, sobre um jovem corretor e um investidor poderoso no mercado financeiro de Nova York.','Casino Royale é um filme de 2006, dirigido por Martin Campbell, em que o agente James Bond joga uma partida de pôquer de alto risco contra um vilão.')]),
84237:dict(old=['Scream'],new='Scary Movie',y='2000',k='🎬 Filme',
  d='Scary Movie é uma comédia de 2000 que faz paródia dos filmes de terror e de suas regras. A referência é a paródia que brinca com as convenções do gênero. A cena desta aula é original; não reproduz a obra.',
  frag=[('é um filme de terror que brinca com as regras do gênero','é uma comédia que faz paródia dos filmes de terror e de suas regras'),
        ('É um filme de terror que brinca com as regras do gênero','É uma comédia que faz paródia dos filmes de terror e de suas regras'),('**1996**','**2000**'),('· 1996','· 2000'),('\\bScream\\b','\\bScary\\b')]),
960099:dict(old=['The Arrival'],new='Close Encounters of the Third Kind',y='1977',k='🎬 Filme',
  d='Close Encounters of the Third Kind é um filme de ficção científica de 1977, dirigido por Steven Spielberg, sobre pessoas que seguem sinais de uma chegada extraterrestre até um encontro. A referência é o filme da chegada em que se chega a uma resposta e se recua: arrive at, back away. A cena desta aula é original; não reproduz a obra.',
  frag=[('The aliens write in circular symbols.','The visitors answer with five musical notes.'),('Os alienígenas escrevem em símbolos circulares.','Os visitantes respondem com cinco notas musicais.'),
        ('Amy Adams plays the linguist.','Richard Dreyfuss plays an ordinary electrician.'),('Amy Adams faz a linguista.','Richard Dreyfuss faz um eletricista comum.'),
        ('shows how language shapes thought','shows how music can be a common language'),('mostra como a linguagem molda o pensamento','mostra como a música pode ser uma língua comum'),('**1996**','**1977**'),('· 1996','· 1977'),('\\bThe\\s+Arrival\\b','\\bEncounters\\b')]),
84282:dict(old=['Cambridge English: Advanced','Cambridge English'],new='PTE Academic',y='2009',k='📝 Exame',
  d='PTE Academic é um exame internacional de proficiência em inglês, feito em computador, usado para estudar e trabalhar no exterior. A referência é o exame em que se completam lacunas e se reescrevem frases. A cena desta aula é original; não reproduz a obra.',
  frag=[('é o exame Cambridge de inglês avançado','é um exame internacional de inglês feito em computador'),('É o exame Cambridge de inglês avançado','É um exame internacional de inglês feito em computador'),('**1913**','**2009**'),('· 1913','· 2009'),('\\bCambridge\\b','\\bPTE\\b')]),
}
def rep(o,fn):
    if isinstance(o,dict):return {k:rep(v,fn) for k,v in o.items()}
    if isinstance(o,list):return [rep(v,fn) for v in o]
    if isinstance(o,str):return fn(o)
    return o
if __name__=='__main__':
    for f in sorted(glob.glob('data/en-*.json')):
        d=json.load(open(f));ch=False
        for i,e in enumerate(d):
            c=OLD_NEW.get(e['n'])
            if not c:continue
            old_d=e['a']['d'];old_w=e['a']['w']
            def fn(s):
                for fr_old,fr_new in c['frag']:s=s.replace(fr_old,fr_new)
                s=s.replace(old_d,c['d'])
                for o in c['old']:
                    s=re.sub(re.escape(o)+r' · \d{4}',c['new']+' · '+c['y'],s)
                    s=s.replace(o,c['new'])
                return s
            e2=rep(e,fn)
            e2['a']['w']=c['new'];e2['a']['y']=c['y'];e2['a']['k']=c['k'];e2['a']['d']=c['d']
            d[i]=e2;ch=True
        if ch:json.dump(d,open(f,'w'),ensure_ascii=False,separators=(',',':'))
