import json,glob,os
# n -> descrição da obra (PT) escrita à mão, sem frase de efeito genérica
D={
7083038:"“Without You” é uma canção de 1971 de Harry Nilsson, escrita por Pete Ham e Tom Evans, da banda Badfinger, e uma das baladas mais conhecidas da década. A aula usa o título para praticar como dizer que algo depende de alguém: but for, without e were it not for.",
83039:"“Blue Planet” é uma série documental da BBC, de 2001, narrada por David Attenborough, que filmou o fundo do oceano e criaturas que quase ninguém tinha visto. A aula usa a surpresa dessas cenas para praticar a inversão depois de advérbios negativos: Never have I seen.",
7083039:"“The Dark Knight” (O Cavaleiro das Trevas) é um filme de 2008 dirigido por Christopher Nolan, em que Batman enfrenta o Coringa em Gotham. A aula usa o ritmo do filme, em que um caos segue o outro, para praticar No sooner had… than e Hardly had… when.",
83041:"“San Andreas” é um filme-catástrofe de 2015 com Dwayne Johnson, sobre um terremoto devastador ao longo da falha de San Andreas, na Califórnia. A aula usa as cenas de destruição para praticar a inversão com so e such: So great was the damage that…",
7083041:"“Volcano” é um filme-catástrofe de 1997 dirigido por Mick Jackson, em que a lava surge de repente sob Los Angeles. A aula usa a força da erupção para praticar Such was the force that… e o vocabulário de tempestades e preparação.",
83042:"“Jurassic World” é um filme de 2015 dirigido por Colin Trevorrow, ambientado num parque temático onde dinossauros escapam. A aula usa as cenas de fuga para praticar a inversão depois de expressões de lugar: Out of the fern ran the raptors.",
7083042:"“Those Were the Days” é uma canção de 1968 da cantora galesa Mary Hopkin, produzida por Paul McCartney, que lembra com saudade os dias felizes do passado. A aula usa o clima nostálgico para praticar Gone are the days when… e expressões sobre mudança.",
7940009:"“Texts From Last Night” é um site e livro, criado em 2009, que reúne mensagens de texto anônimas e engraçadas, muitas cheias de abreviações. A aula usa esse estilo para praticar tbh, imo, irl e a escolha do tom certo em cada situação.",
83043:"“It Happened One Night” (Aconteceu Naquela Noite) é uma comédia romântica de 1934 dirigida por Frank Capra, em que uma herdeira fugitiva e um repórter se conhecem num ônibus. A aula usa as discussões do casal para praticar o do enfático e as orações clivadas: It was then that…",
83044:"“Monty Python's Flying Circus” é uma série britânica de esquetes que estreou na BBC em 1969 e transformou o humor da televisão com piadas absurdas. A aula usa o exagero dos personagens para praticar adjetivos extremos: utterly, absolutely, completely.",
7083044:"“Nothing” é um filme canadense de 2003 de Vincenzo Natali sobre dois amigos cuja casa e cujo mundo desaparecem, restando só um vazio branco. A aula usa o título para praticar nothing at all, the very e outras formas de reforçar uma negativa.",
7083048:"“The Wedding Planner” é uma comédia romântica de 2001 dirigida por Adam Shankman, com Jennifer Lopez como uma organizadora de casamentos. A aula usa o mundo dos casamentos para praticar o inglês formal com preposição + which/whom: the reason for which we write.",
83049:"“Yes We Can” é o slogan e o discurso de Barack Obama em New Hampshire, em janeiro de 2008, em que a mesma frase se repete para unir a multidão. A aula usa essa repetição para praticar a anáfora e as estruturas paralelas.",
7940011:"O Acordo da Sexta-Feira Santa (Good Friday Agreement) é o acordo de paz da Irlanda do Norte, assinado em Belfast em 10 de abril de 1998 e aprovado em referendos. A aula usa as negociações para praticar colocações como reach a deal, strike a bargain e settle a dispute.",
83056:"“Urban Legend” (Lenda Urbana) é um filme de terror de 1998 dirigido por Jamie Blanks, em que um assassino imita lendas urbanas num campus. A aula usa as histórias que ninguém sabe provar para praticar a passiva impessoal: It is said that…",
940012:"“Denial” (A Negação) é um filme de 2016 baseado no caso real em que a historiadora Deborah Lipstadt foi processada em Londres por David Irving, que negava o Holocausto. A aula usa o julgamento para praticar deny, admit e insist seguidos de -ing.",
7940012:"“O Diário Secreto de Adrian Mole, Aos 13¾”, de Sue Townsend, é um romance cômico de 1982: um adolescente inglês conta no diário as espinhas, a paixonite por Pandora e os problemas dos pais. A aula usa as perguntas do diário para praticar a fala indireta: She asked whether I knew.",
83059:"“Mind Your Language” é uma comédia britânica que estreou na ITV em 1977, passada numa aula de inglês para adultos em Londres. A aula usa o professor paciente para praticar I won't have you talking like that e a estrutura have someone do something.",
7083063:"“The Mummy” (A Múmia) é um filme de aventura de 1999 dirigido por Stephen Sommers, com Brendan Fraser e Rachel Weisz, sobre uma tumba perdida no Egito. A aula usa a caça ao tesouro para praticar perguntas negativas na passiva: Wasn't it found by soldiers?",
7940014:"“The Lincoln Lawyer” (O Poder e a Lei) é um filme de 2011 com Matthew McConaughey, sobre um advogado que trabalha do banco de trás de um carro. A aula usa os contratos para praticar o inglês jurídico: shall, hereby, null and void e in breach of.",
7083069:"“Spellbound” é um documentário de 2002 dirigido por Jeffrey Blitz, que acompanha oito crianças americanas no concurso nacional de soletrar de 1999. A aula usa a atenção à ortografia para praticar a revisão de e-mails formais: a voz passiva, o tom e fórmulas como further to.",
7083070:"“The Cassandra Crossing” (A Travessia de Cassandra) é um thriller de 1976 sobre um trem com passageiros expostos a um vírus mortal, mandado rumo a uma ponte perigosa. A aula usa o aviso ignorado para praticar orações participiais perfeitas: Having been warned…",
7940015:"“Influence” (As Armas da Persuasão) é um livro de 1984 do psicólogo Robert Cialdini sobre os princípios da persuasão, como reciprocidade e prova social. A aula usa o tema para praticar sugestões educadas: Have you considered…? e suggest + -ing.",
83063:"A Torre Eiffel foi construída pela empresa de Gustave Eiffel para a Exposição Universal de 1889, em Paris, e com cerca de 330 metros foi a estrutura mais alta do mundo por quarenta anos. A aula usa a obra em andamento para praticar a passiva contínua: It was being built.",
}
for f in glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../../data/en-b2_*.json')):
    d=json.load(open(f));ch=False
    for e in d:
        if e['n'] in D and e['a']['d']!=D[e['n']]:
            e['a']['d']=D[e['n']];ch=True
    if ch:json.dump(d,open(f,'w'),ensure_ascii=False,separators=(',',':'))
print('ok')
