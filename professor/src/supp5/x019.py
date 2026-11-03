X = dict(
key=dict(big='Who is your favorite singer?', label='Falar de música e artistas', sub='Use What music do you like? e Who is your favorite…? para conhecer gostos.'),
mini=[
 dict(who='Simone', en='What music do you like?', pt='Que música você gosta?'),
 dict(who='You', en='I like {pop|rock|country}. And you?', pt='Gosto de {pop|rock|country}. E você?'),
 dict(who='Simone', en='I like {rock|jazz|pop}. Who is your favorite {singer|band|artist}?', pt='Gosto de {rock|jazz|pop}. Quem é seu {cantor|banda|artista} favorito?'),
 dict(who='You', en='I love {Taylor Swift|Beyoncé|Bruno Mars}.', pt='Adoro {a Taylor Swift|a Beyoncé|o Bruno Mars}.'),
],
dlg=[
 dict(who='Simone', en='What {music|songs|bands} do you like?', pt='Que {música|canções|bandas} você gosta?'),
 dict(who='You', en='I like {pop|rock|jazz} and country. And you?', pt='Gosto de {pop|rock|jazz} e country. E você?'),
 dict(who='Simone', en='I like {rock|jazz|pop}. Who is your favorite {singer|band|artist}?', pt='Gosto de {rock|jazz|pop}. Quem é seu {cantor|banda|artista} favorito?'),
 dict(who='You', en='I love {Taylor Swift|Beyoncé|Bruno Mars}.', pt='Adoro {a Taylor Swift|a Beyoncé|o Bruno Mars}.'),
 dict(who='Simone', en='Me too! Do you have {tickets|plans|time}?', pt='Eu também! Você tem {ingressos|planos|tempo}?'),
 dict(who='You', en='Not yet. They are {expensive|cheap|sold out}.', pt='Ainda não. São {caros|baratos|esgotados}.'),
 dict(who='Simone', en='Let\'s buy them together.', pt='Vamos comprar juntos.'),
 dict(who='You', en='Great idea!', pt='Ótima ideia!'),
 dict(who='Simone', en='Let\'s get the tickets {today|tonight|tomorrow}!', pt='Vamos comprar os ingressos {hoje|hoje à noite|amanhã}!'),
],
vocab=[
 dict(w='music', pt='música', e='🎵', ex=['What music do you like?', 'I listen to music every day.']),
 dict(w='singer', pt='cantor, cantora', e='🎤', ex=['Who is your favorite singer?', 'The singer is very good.']),
 dict(w='song', pt='canção', e='🎶', ex=['I love this song.', 'This song is fun.']),
 dict(w='concert', pt='show', e='🎟️', ex=['The concert is on Saturday.', 'Let\'s go to the concert.']),
 dict(w='ticket', pt='ingresso', e='🎫', ex=['I have two tickets.', 'The ticket is expensive.']),
 dict(w='favorite', pt='favorito', e='⭐', ex=['This is my favorite song.', 'Who is your favorite singer?']),
],
molds=[
 dict(title='Falar do seu gosto', frame='I like {music}. My favorite singer is {name}.', slots=[dict(key='music', opts=['pop', 'rock', 'jazz']), dict(key='name', opts=['Beyoncé', 'Bruno Mars', 'Adele'])], model='I like pop. My favorite singer is Beyoncé.', note='My favorite + coisa + is + nome. O gênero vem depois de like.'),
 dict(title='Perguntar e propor', frame='Do you have tickets? Let\'s {plan}.', slots=[dict(key='plan', opts=['buy them today', 'buy them together', 'get them now'])], model='Do you have tickets? Let\'s buy them today.', note='Do you have…? e Let\'s + verbo são duas frases úteis para combinar um show.'),
 dict(title='Escrever sobre um show', frame='The concert is {when}. The tickets are {price}.', slots=[dict(key='when', opts=['on Saturday', 'on Friday', 'next month']), dict(key='price', opts=['expensive', 'cheap', 'sold out'])], model='The concert is on Saturday. The tickets are expensive.', note='Tickets é plural, então use are. Dia da semana com on.'),
],
sounds=[
 dict(say='Who is your favorite singer?', tag='acento: FAV-rit', tip='Favorite soa "FEIV-rit", com duas sílabas fortes na fala: FAV-rit SING-er.'),
 dict(say='I love Taylor Swift.', tag='acento: TAY-lor', tip='Dê força em love e em TAY-lor. Swift começa com "sw", sem vogal antes.'),
 dict(say='Let\'s buy them together.', tag='redução: them', tip='Them vira "dhem" fraco, quase "em": "buy-em".'),
],
role=dict(turns=[
 dict(npc='What music do you like?', opts=[
  dict(en='I like pop and country. And you?', pt='Gosto de pop e country. E você?', reply='I like rock. Who is your favorite singer?'),
  dict(en='I like pop. What about you?', pt='Gosto de pop. E você?', reply='I like rock. Who is your favorite singer?'),
  dict(en='I like jazz and pop. And you?', pt='Gosto de jazz e pop. E você?', reply='I like rock. Who is your favorite singer?')]),
 dict(npc='Who is your favorite singer?', opts=[
  dict(en='I love Taylor Swift.', pt='Adoro a Taylor Swift.', reply='Me too! Do you have tickets?'),
  dict(en='My favorite is Bruno Mars.', pt='O meu favorito é o Bruno Mars.', reply='Cool! Do you have tickets for his concert?'),
  dict(en='I like Beyoncé a lot.', pt='Gosto muito da Beyoncé.', reply='Me too! Do you have tickets?')]),
 dict(npc='Do you have tickets?', opts=[
  dict(en='Not yet. They are expensive.', pt='Ainda não. São caros.', reply='Let\'s buy them together.'),
  dict(en='No, I don\'t. Do you?', pt='Não. E você?', reply='Not yet. Let\'s buy them together.'),
  dict(en='Not yet. When is the concert?', pt='Ainda não. Quando é o show?', reply='On Saturday. Let\'s buy them together.')]),
 dict(npc='Let\'s get the tickets today!', opts=[
  dict(en='Great idea!', pt='Ótima ideia!', reply='Perfect! See you at the box office.'),
  dict(en='OK. Let\'s do it after class.', pt='Ok. Vamos depois da aula.', reply='Perfect! See you then.'),
  dict(en='Yes! I can go at six.', pt='Sim! Posso ir às seis.', reply='Perfect! See you at six.')]),
], change=['Os ingressos custam mais do que você pode pagar; diga isso e proponha outro show.', 'Simone prefere rock e discorda do seu gosto; reaja com respeito.', 'Os ingressos esgotaram; sugira uma alternativa.']),
writing=dict(task='Escreva 2 ou 3 frases sobre música: do que você gosta, quem é seu cantor favorito e um convite para um show.', model='I like pop and rock. My favorite singer is Beyoncé. Let\'s go to a concert!', kw=['music', 'favorite', 'singer', 'concert'], checks=['Disse o gênero de que gosta.', 'Disse o cantor favorito.', 'Fez um convite com Let\'s.']),
scenes=dict(pool=['musicroom', 'stage', 'street', 'stadium', 'living'], npc=dict(g='f', role='friend'), you=dict(g='m')),
convo=dict(npc=dict(name='Simone'), story='Você e Simone conversam sobre música e pensam em ir a um show.', turns=[
 dict(npc='What music do you like?', pt='Que música você gosta?', opts=[
  dict(en='I like pop and country. And you?', pt='Gosto de pop e country. E você?', ok=True, fb='Responde e devolve a pergunta.'),
  dict(en='I am a singer.', pt='Eu sou cantor.', ok=False, fb='A pergunta é sobre gosto, não profissão.'),
  dict(en='Yes, I like it.', pt='Sim, eu gosto.', ok=False, fb='What pede um tipo de música, não sim ou não.')]),
 dict(npc='I like rock. Who is your favorite singer?', pt='Gosto de rock. Quem é seu cantor favorito?', opts=[
  dict(en='I like rock too.', pt='Eu também gosto de rock.', ok=False, fb='Não é o que você disse antes e não responde à pergunta.'),
  dict(en='I love Taylor Swift.', pt='Adoro a Taylor Swift.', ok=True, fb='Diz o nome do cantor.'),
  dict(en='It is a song.', pt='É uma canção.', ok=False, fb='Who pede uma pessoa.')]),
 dict(npc='Me too! Do you have tickets?', pt='Eu também! Você tem ingressos?', opts=[
  dict(en='Yes, I love tickets.', pt='Sim, eu adoro ingressos.', ok=False, fb='Respondemos se temos ingressos, não do que gostamos.'),
  dict(en='Not yet. They are expensive.', pt='Ainda não. São caros.', ok=True, fb='Responde e dá o motivo.'),
  dict(en='My favorite singer is Taylor Swift.', pt='Minha cantora favorita é a Taylor Swift.', ok=False, fb='Isso você já disse; ela quer saber dos ingressos.')]),
 dict(npc='Let\'s buy them together.', pt='Vamos comprar juntos.', opts=[
  dict(en='Great idea!', pt='Ótima ideia!', ok=True, fb='Aceita a sugestão.'),
  dict(en='I buy them together.', pt='Eu compro juntos.', ok=False, fb='Ela fez uma sugestão com Let\'s; aceite ou recuse.'),
  dict(en='What music do you like?', pt='Que música você gosta?', ok=False, fb='Essa pergunta já foi feita.')]),
 dict(npc='Let\'s get the tickets today!', pt='Vamos comprar os ingressos hoje!', opts=[
  dict(en='OK! See you today.', pt='Ok! Até hoje.', ok=True, fb='Fecha o plano.'),
  dict(en='I love concert.', pt='Eu adoro show.', ok=False, fb='Soa solto: falta sentido para o plano e concert precisa de a.'),
  dict(en='They are expensive.', pt='São caros.', ok=False, fb='Isso já foi dito e não fecha o plano.')]),
]),
)
