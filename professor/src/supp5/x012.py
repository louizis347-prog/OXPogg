X = dict(
key=dict(big='When is your birthday?', label='Perguntar a data do aniversário', sub='Responda com in + mês ou on + mês e dia: It\'s in March. On March tenth.'),
mini=[
 dict(who='Evan', en='When is your {birthday|party|class}?', pt='Quando é seu {aniversário|festa|aula}?'),
 dict(who='You', en='It\'s in {March|July|October}. On the {tenth|fourth|twentieth}.', pt='É em {março|julho|outubro}. No dia {dez|quatro|vinte}.'),
 dict(who='Evan', en='Mine is in July. Let\'s have a {party|picnic|dinner}!', pt='O meu é em julho. Vamos fazer {uma festa|um piquenique|um jantar}!'),
 dict(who='You', en='Great idea! I\'ll bring a {cake|pizza|gift}.', pt='Ótima ideia! Eu levo um {bolo|uma pizza|presente}.'),
],
dlg=[
 dict(who='Evan', en='When is your {birthday|party|class}?', pt='Quando é seu {aniversário|festa|aula}?'),
 dict(who='You', en='It\'s in {March|July|October}. On the {tenth|fourth|twentieth}.', pt='É em {março|julho|outubro}. No dia {dez|quatro|vinte}.'),
 dict(who='Evan', en='Mine is in July. July {fourth|4th}!', pt='O meu é em julho. Dia {quatro|4} de julho!'),
 dict(who='You', en='Wow, Independence Day!', pt='Uau, Dia da Independência!'),
 dict(who='Evan', en='Yes. Everyone has fireworks.', pt='Sim. Todo mundo tem fogos.'),
 dict(who='You', en='That\'s cool. Let\'s have a {party|picnic|dinner}.', pt='Que legal. Vamos fazer {uma festa|um piquenique|um jantar}.'),
 dict(who='Evan', en='Great idea! I\'ll bring a {cake|pizza|gift}.', pt='Ótima ideia! Eu levo um {bolo|uma pizza|presente}.'),
 dict(who='You', en='Perfect. See you in {March|July|October}.', pt='Perfeito. Até {março|julho|outubro}.'),
 dict(who='Evan', en='Don\'t forget the {cake|gift|card}!', pt='Não esqueça o {bolo|presente|cartão}!'),
],
vocab=[
 dict(w='January', pt='janeiro', e='❄️', ex=['My birthday is in January.', 'It is cold in January in Chicago.']),
 dict(w='March', pt='março', e='🌷', ex=['My sister\'s birthday is in March.', 'Spring starts in March in the US.']),
 dict(w='July', pt='julho', e='☀️', ex=['Evan\'s birthday is in July.', 'We have a picnic in July.']),
 dict(w='October', pt='outubro', e='🎃', ex=['Halloween is in October.', 'My class starts in October.']),
 dict(w='December', pt='dezembro', e='🎄', ex=['Christmas is in December.', 'The party is in December.']),
 dict(w='April', pt='abril', e='🌷', ex=['My birthday is in April.', 'April is a spring month.']),
],
molds=[
 dict(title='Dizer seu aniversário', frame='My birthday is in {month}.', slots=[dict(key='month', opts=['March', 'July', 'October', 'December'])], model='My birthday is in March.', note='Com só o mês, use in: in March. Com o dia, use on: on March tenth.'),
 dict(title='Perguntar e combinar', frame='When is {who} birthday? Let\'s have a {plan}.', slots=[dict(key='who', opts=['your', 'her', 'his']), dict(key='plan', opts=['party', 'picnic', 'dinner'])], model='When is your birthday? Let\'s have a party.', note='your/her/his vêm antes de birthday. Let\'s + verbo faz uma sugestão.'),
 dict(title='Escrever um convite', frame='The party is {when}. I\'ll bring a {thing}.', slots=[dict(key='when', opts=['in July', 'in October', 'in December']), dict(key='thing', opts=['cake', 'gift', 'card'])], model='The party is in July. I\'ll bring a cake.', note='I\'ll bring… é uma promessa simples de levar algo.'),
],
sounds=[
 dict(say='When is your birthday?', tag='ligação: is your', tip='Junte is e your: "wen-iz-yur". A voz sobe um pouco em birth-DAY.'),
 dict(say='It\'s in March.', tag='ligação: it\'s in', tip='It\'s in soa quase "it-sin": o s liga com o in.'),
 dict(say='Don\'t forget the cake!', tag='acento: for-GET', tip='O acento de forget cai na segunda sílaba: for-GET. The fica fraco: "dhe".'),
],
role=dict(turns=[
 dict(npc='When is your birthday?', opts=[
  dict(en='It\'s in March. On March tenth.', pt='É em março. Dia dez de março.', reply='Nice! Mine is in July.'),
  dict(en='It\'s in October.', pt='É em outubro.', reply='Nice! Mine is in July.'),
  dict(en='My birthday is in December.', pt='Meu aniversário é em dezembro.', reply='Nice! Mine is in July.')]),
 dict(npc='Mine is July fourth! Everyone has fireworks.', opts=[
  dict(en='Wow, Independence Day!', pt='Uau, Dia da Independência!', reply='Yes! It is a big day in the US.'),
  dict(en='That\'s cool!', pt='Que legal!', reply='Yes! I love the fireworks.'),
  dict(en='Fireworks on your birthday? Nice!', pt='Fogos no seu aniversário? Legal!', reply='Yes! Every year.')]),
 dict(npc='Let\'s have a party!', opts=[
  dict(en='Great idea! I\'ll bring a cake.', pt='Ótima ideia! Eu levo um bolo.', reply='Perfect! Then I\'ll bring the drinks.'),
  dict(en='Good idea. I\'ll bring pizza.', pt='Boa ideia. Eu levo pizza.', reply='Perfect! Then I\'ll bring the drinks.'),
  dict(en='Yes! Let\'s have it at my place.', pt='Sim! Vamos fazer na minha casa.', reply='Perfect! I\'ll bring the drinks.')]),
 dict(npc='See you at the party!', opts=[
  dict(en='See you in March!', pt='Até março!', reply='Don\'t forget the cake!'),
  dict(en='Perfect. See you then!', pt='Perfeito. Até lá!', reply='Don\'t forget the cake!'),
  dict(en='Bye! I won\'t forget.', pt='Tchau! Não vou esquecer.', reply='Great. Bye!')],
 ),
], change=['O aniversário do amigo é em outubro, não em julho.', 'Você não pode ir à festa no dia combinado e propõe outro dia.', 'Você esqueceu o que ia levar e pergunta o que falta.']),
writing=dict(task='Escreva 2 ou 3 frases para um amigo: diga quando é seu aniversário, proponha uma festa e diga o que você vai levar.', model='My birthday is in March. On March tenth. Let\'s have a party! I\'ll bring a cake.', kw=['birthday', 'march', 'party', 'bring'], checks=['Disse o mês do aniversário com in.', 'Fez uma sugestão com Let\'s.', 'Disse o que vai levar com I\'ll bring.']),
scenes=dict(pool=['living', 'park', 'kitchen', 'bakery', 'home1'], npc=dict(g='m', role='friend'), you=dict(g='f')),
convo=dict(npc=dict(name='Evan'), story='Você conversa com o vizinho Evan sobre aniversários e combina uma festa.', turns=[
 dict(npc='When is your birthday?', pt='Quando é seu aniversário?', opts=[
  dict(en='My birthday is on a Sunday.', pt='Meu aniversário é num domingo.', ok=False, fb='Evan pergunta o mês e a data, não o dia da semana.'),
  dict(en='It\'s in March. On March tenth.', pt='É em março. Dia dez de março.', ok=True, fb='Resposta completa: mês e dia.'),
  dict(en='I am thirty years old.', pt='Tenho trinta anos.', ok=False, fb='When pergunta a data, não a idade.')]),
 dict(npc='Mine is in July. July fourth!', pt='O meu é em julho. Dia quatro de julho!', opts=[
  dict(en='Wow, Independence Day!', pt='Uau, Dia da Independência!', ok=True, fb='Você reconhece a data famosa.'),
  dict(en='Mine is in March too.', pt='O meu também é em março.', ok=False, fb='Seu aniversário já foi dito e é outra data; reaja ao dele.'),
  dict(en='It\'s in July.', pt='É em julho.', ok=False, fb='Você apenas repete a informação, sem reagir.')]),
 dict(npc='Yes. Everyone has fireworks.', pt='Sim. Todo mundo tem fogos.', opts=[
  dict(en='Yes, it is my birthday.', pt='Sim, é meu aniversário.', ok=False, fb='Quem faz aniversário nesse dia é Evan.'),
  dict(en='That\'s cool. Let\'s have a party.', pt='Que legal. Vamos fazer uma festa.', ok=True, fb='Você reage e sugere um plano.'),
  dict(en='Thank you, you are kind.', pt='Obrigado, você é gentil.', ok=False, fb='Ele não fez um elogio; agradecer não encaixa.')]),
 dict(npc='Great idea! I\'ll bring a cake.', pt='Ótima ideia! Eu levo um bolo.', opts=[
  dict(en='Perfect. See you in March.', pt='Perfeito. Até março.', ok=True, fb='Você aceita e se despede.'),
  dict(en='Happy birthday to you!', pt='Feliz aniversário!', ok=False, fb='O aniversário é em março; hoje não é o dia.'),
  dict(en='Sorry, I can\'t come.', pt='Desculpe, não posso ir.', ok=False, fb='Você mesmo propôs a festa; isso contradiz a conversa.')]),
 dict(npc='Don\'t forget the cake!', pt='Não esqueça o bolo!', opts=[
  dict(en='Happy birthday!', pt='Feliz aniversário!', ok=False, fb='Ainda não é o dia do aniversário.'),
  dict(en='I won\'t. Bye!', pt='Não vou esquecer. Tchau!', ok=True, fb='Resposta natural a um lembrete.'),
  dict(en='When is your birthday?', pt='Quando é seu aniversário?', ok=False, fb='Essa pergunta já foi feita no começo.')]),
]),
)
