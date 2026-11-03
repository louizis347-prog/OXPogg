X = dict(
key=dict(big='What do you do in your free time?', label='Falar do tempo livre', sub='Use play com esporte, jogo e instrumento; read com livros: I play soccer. I read books.'),
mini=[
 dict(who='Grace', en='What do you do in your {free time|weekend|spare time}?', pt='O que você faz {no tempo livre|no fim de semana|nas horas vagas}?'),
 dict(who='You', en='I play {soccer|tennis|video games} and read {books|comics|magazines}.', pt='Jogo {futebol|tênis|videogame} e leio {livros|quadrinhos|revistas}.'),
 dict(who='Grace', en='Cool! I play {guitar|piano|drums}.', pt='Legal! Eu toco {violão|piano|bateria}.'),
 dict(who='You', en='Do you want to play {soccer|tennis|cards} on {Saturday|Sunday|Friday}?', pt='Quer jogar {futebol|tênis|cartas} {no sábado|no domingo|na sexta}?'),
],
dlg=[
 dict(who='Grace', en='What do you do in your {free time|weekend|spare time}?', pt='O que você faz {no tempo livre|no fim de semana|nas horas vagas}?'),
 dict(who='You', en='I play {soccer|tennis|video games} and read books.', pt='Jogo {futebol|tênis|videogame} e leio livros.'),
 dict(who='Grace', en='Cool! I play {guitar|piano|drums}.', pt='Legal! Eu toco {violão|piano|bateria}.'),
 dict(who='You', en='Do you play in a band?', pt='Você toca em banda?'),
 dict(who='Grace', en='No, I play at home. Just for fun.', pt='Não, toco em casa. Só por diversão.'),
 dict(who='You', en='Do you want to play {soccer|tennis|cards} on {Saturday|Sunday|Friday}?', pt='Quer jogar {futebol|tênis|cartas} {no sábado|no domingo|na sexta}?'),
 dict(who='Grace', en='Sure! What time?', pt='Claro! Que horas?'),
 dict(who='You', en='At {ten|nine|eleven}, in the park.', pt='Às {dez|nove|onze}, no parque.'),
 dict(who='Grace', en='See you on {Saturday|Sunday|Friday}!', pt='Até {sábado|domingo|sexta}!'),
],
vocab=[
 dict(w='play', pt='jogar; tocar', e='⚽', ex=['I play soccer on Saturday.', 'Grace plays the guitar.']),
 dict(w='read', pt='ler', e='📚', ex=['I read books at night.', 'She likes to read.']),
 dict(w='guitar', pt='violão, guitarra', e='🎸', ex=['Grace plays the guitar.', 'My guitar is old.']),
 dict(w='movie', pt='filme', e='🎬', ex=['We watch a movie on Friday.', 'This movie is long.']),
 dict(w='game', pt='jogo', e='🎮', ex=['I play a game after dinner.', 'The soccer game is at ten.']),
 dict(w='hobby', pt='passatempo', e='🎨', ex=['Reading is my hobby.', 'What is your hobby?']),
],
molds=[
 dict(title='Dizer seu passatempo', frame='I play {game} and I read {thing}.', slots=[dict(key='game', opts=['soccer', 'tennis', 'video games']), dict(key='thing', opts=['books', 'comics', 'magazines'])], model='I play soccer and I read books.', note='Play vai com esporte e jogos; read, com livros. Para instrumento: play the guitar.'),
 dict(title='Convidar', frame='Do you want to play {game} on {day}? At {time}.', slots=[dict(key='game', opts=['soccer', 'tennis', 'cards']), dict(key='day', opts=['Saturday', 'Sunday', 'Friday']), dict(key='time', opts=['ten', 'nine', 'eleven'])], model='Do you want to play soccer on Saturday? At ten.', note='Do you want to + verbo é um convite simples. Dia com on, hora com at.'),
 dict(title='Escrever sobre você', frame='In my free time, I {thing}. It\'s fun!', slots=[dict(key='thing', opts=['play soccer', 'watch movies', 'read books'])], model='In my free time, I play soccer. It\'s fun!', note='Cada atividade tem seu verbo: play soccer, watch movies, read books.'),
],
sounds=[
 dict(say='What do you do?', tag='ligação: what do you', tip='What do you soa "wa-dyu-du". O acento forte vai no segundo DO.'),
 dict(say='I play soccer.', tag='acento: SOC-cer', tip='Em soccer a força está na primeira sílaba: SOC-er, com o r final fraco.'),
 dict(say='Just for fun.', tag='ritmo: palavras fortes', tip='Bata JUST, FUN. For é fraco: "jus-fer-FUN".'),
],
role=dict(turns=[
 dict(npc='What do you do in your free time?', opts=[
  dict(en='I play soccer and read books.', pt='Jogo futebol e leio livros.', reply='Cool! I play guitar.'),
  dict(en='I like to read and play tennis.', pt='Gosto de ler e jogar tênis.', reply='Cool! I play guitar.'),
  dict(en='I play video games and watch movies.', pt='Jogo videogame e assisto a filmes.', reply='Cool! I play guitar.')]),
 dict(npc='I play guitar.', opts=[
  dict(en='Do you play in a band?', pt='Você toca em banda?', reply='No, I play at home. Just for fun.'),
  dict(en='Nice! Do you play every day?', pt='Legal! Você toca todo dia?', reply='Almost every day. Just for fun.'),
  dict(en='Cool! Is it hard?', pt='Legal! É difícil?', reply='A little. But it\'s fun.')]),
 dict(npc='No, I play at home. Just for fun.', opts=[
  dict(en='Do you want to play soccer on Saturday?', pt='Quer jogar futebol no sábado?', reply='Sure! What time?'),
  dict(en='That\'s nice. Do you want to play tennis?', pt='Que legal. Quer jogar tênis?', reply='Sure! What time?'),
  dict(en='Cool! Let\'s play a game on Sunday.', pt='Legal! Vamos jogar algo no domingo.', reply='Sure! What time?')]),
 dict(npc='Sure! What time?', opts=[
  dict(en='At ten, in the park.', pt='Às dez, no parque.', reply='See you on Saturday!'),
  dict(en='At nine, at the soccer field.', pt='Às nove, no campo de futebol.', reply='See you on Saturday!'),
  dict(en='At eleven. Is that OK?', pt='Às onze. Pode ser?', reply='Yes, that\'s OK. See you!')]),
], change=['Grace diz que não gosta de futebol; sugira outra atividade.', 'Chove no sábado; proponha outro dia.', 'Grace pergunta se pode levar uma amiga.']),
writing=dict(task='Escreva 2 ou 3 frases sobre o que você faz no tempo livre e convide alguém para uma atividade.', model='In my free time, I play soccer and read books. Do you want to play on Saturday?', kw=['play', 'free', 'read', 'saturday'], checks=['Disse o que faz no tempo livre.', 'Usou play ou read corretamente.', 'Fez um convite com Do you want to…?']),
scenes=dict(pool=['park', 'soccerfield', 'musicroom', 'playground', 'living'], npc=dict(g='f', role='friend'), you=dict(g='m')),
convo=dict(npc=dict(name='Grace'), story='No parque, você e Grace falam do que gostam de fazer no tempo livre.', turns=[
 dict(npc='What do you do in your free time?', pt='O que você faz no tempo livre?', opts=[
  dict(en='I play soccer and read books.', pt='Jogo futebol e leio livros.', ok=True, fb='Lista duas atividades.'),
  dict(en='I am free on Saturday.', pt='Estou livre no sábado.', ok=False, fb='A pergunta é sobre o que você faz, não quando está livre.'),
  dict(en='I do soccer and book.', pt='Eu faço futebol e livro.', ok=False, fb='Use play soccer e read books, não do.')]),
 dict(npc='Cool! I play guitar.', pt='Legal! Eu toco violão.', opts=[
  dict(en='Do you play in a band?', pt='Você toca em banda?', ok=True, fb='Pergunta natural sobre o que ela contou.'),
  dict(en='I read books too.', pt='Eu também leio livros.', ok=False, fb='Soa estranho: ela falou de violão, não de leitura.'),
  dict(en='Yes, I do.', pt='Sim, eu toco.', ok=False, fb='Ela não fez uma pergunta de sim ou não.')]),
 dict(npc='No, I play at home. Just for fun.', pt='Não, toco em casa. Só por diversão.', opts=[
  dict(en='What is your name?', pt='Qual é seu nome?', ok=False, fb='Vocês já se conhecem.'),
  dict(en='Do you want to play soccer on Saturday?', pt='Quer jogar futebol no sábado?', ok=True, fb='Convite com Do you want to…?'),
  dict(en='I play in a band.', pt='Eu toco em banda.', ok=False, fb='Isso contradiz o que você disse sobre seu tempo livre.')]),
 dict(npc='Sure! What time?', pt='Claro! Que horas?', opts=[
  dict(en='At ten, in the park.', pt='Às dez, no parque.', ok=True, fb='Hora com at e lugar com in.'),
  dict(en='On Saturday.', pt='No sábado.', ok=False, fb='O dia já foi dito; ela pergunta a hora.'),
  dict(en='It is ten dollars.', pt='São dez dólares.', ok=False, fb='What time? pergunta hora, não preço.')]),
 dict(npc='See you on Saturday!', pt='Até sábado!', opts=[
  dict(en='See you! Bye!', pt='Até! Tchau!', ok=True, fb='Despedida natural.'),
  dict(en='What time?', pt='Que horas?', ok=False, fb='Isso já foi resolvido.'),
  dict(en='Sorry, I can\'t.', pt='Desculpe, não posso.', ok=False, fb='Você mesmo propôs o jogo.')]),
]),
)
