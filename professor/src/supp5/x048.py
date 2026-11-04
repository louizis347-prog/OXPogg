"""Bloco extra · aula 48: Taking a taxi."""
X = dict(
 key=dict(big='To the airport, please', label='Pedir um táxi', sub='Diga o destino com “To… please”. Perguntar o preço e o tempo antes ou durante a corrida é comum.'),
 mini=[
  dict(who='Marco', en='Hi! Where to?', pt='Oi! Para onde?'),
  dict(who='You', en='To the {airport|train station|hotel}, please.', pt='Para {o aeroporto|a estação de trem|o hotel}, por favor.'),
  dict(who='Marco', en='Sure. Which {terminal|entrance|street}?', pt='Claro. Qual {terminal|entrada|rua}?'),
  dict(who='You', en='{Terminal two|The main entrance|Oak Street}.', pt='{Terminal dois|A entrada principal|Rua Oak}.')],
 dlg=[
  dict(who='Marco', en='{Hi|Hello|Good morning}! Where to?', pt='{Oi|Olá|Bom dia}! Para onde?'),
  dict(who='You', en='To the {airport|train station|hotel}, please.', pt='Para {o aeroporto|a estação de trem|o hotel}, por favor.'),
  dict(who='Marco', en='Sure. Which {terminal|entrance|street}?', pt='Claro. Qual {terminal|entrada|rua}?'),
  dict(who='You', en='{Terminal two|The main entrance|Oak Street}.', pt='{Terminal dois|A entrada principal|Rua Oak}.'),
  dict(who='Marco', en='How long does it take?', pt='Quanto tempo demora?'),
  dict(who='You', en='About {thirty|twenty|forty} minutes.', pt='Uns {trinta|vinte|quarenta} minutos.'),
  dict(who='Marco', en='How much is it?', pt='Quanto custa?'),
  dict(who='You', en='About {forty|thirty|fifty} dollars.', pt='Uns {quarenta|trinta|cinquenta} dólares.'),
  dict(who='Marco', en='Safe travels!', pt='Boa viagem!')],
 vocab=[
  dict(w='taxi', pt='táxi', e='🚕', ex=['I take a taxi to the airport.', 'The taxi is outside.']),
  dict(w='airport', pt='aeroporto', e='✈️', ex=['The airport is far from here.', 'Which airport is it?']),
  dict(w='cab', pt='táxi', e='🚕', ex=['I take a cab to work.', 'The cab is here.']),
  dict(w='trip', pt='viagem / corrida', e='🧳', ex=['The trip is thirty minutes.', 'Have a good trip!']),
  dict(w='app', pt='aplicativo', e='📱', ex=['I call a car with the app.', 'The app shows the price.']),
  dict(w='terminal', pt='terminal', e='🛫', ex=['I am at terminal two.', 'Which terminal is your flight?'])],
 molds=[
  dict(title='Dizer o destino', frame='To the {place}, please. {terminal}.', slots=[dict(key='place', opts=['airport', 'train station', 'hotel']), dict(key='terminal', opts=['Terminal two', 'The main entrance', 'The front door'])], model='To the airport, please. Terminal two.', note='“To… please” é o jeito curto e educado de dar o destino.'),
  dict(title='Perguntar tempo e preço', frame='How long does it take? How much is it to the {place}?', slots=[dict(key='place', opts=['airport', 'hotel', 'station'])], model='How long does it take? How much is it to the airport?', note='Pergunte antes de aceitar se o preço importa.'),
  dict(title='Escrever sobre a corrida', frame='The trip to the {place} takes about {n} minutes. It costs about {price} dollars.', slots=[dict(key='place', opts=['airport', 'hotel', 'station']), dict(key='n', opts=['thirty', 'twenty', 'forty']), dict(key='price', opts=['forty', 'thirty', 'fifty'])], model='The trip to the airport takes about thirty minutes. It costs about forty dollars.', note='Escreva duas frases com tempo e preço aproximados.')],
 sounds=[
  dict(say='To the airport, please.', tag='ritmo: to the', tip='“To the” é fraco e rápido: “tuh-thuh”. Forte em “air-” e “please”.'),
  dict(say='How long does it take?', tag='ligação: does it', tip='“Does it” vira “duzit”. A voz sobe no fim da pergunta.'),
  dict(say='About thirty minutes.', tag='acento: thirty', tip='“Thirty” tem acento na primeira sílaba. Compare com “thirteen”, que acentua o fim.')],
 role=dict(turns=[
  dict(npc='Hi! Where to?', opts=[
   dict(en='To the airport, please.', pt='Para o aeroporto, por favor.', reply='Sure. Which terminal?'),
   dict(en='To the main train station, please.', pt='Para a estação central, por favor.', reply='Sure. Which entrance?'),
   dict(en='Can you take me to the Grand Hotel?', pt='Pode me levar ao Grand Hotel?', reply='Sure. Which street is it on?')]),
  dict(npc=None, opts=[
   dict(en='Terminal two.', pt='Terminal dois.', reply='OK. How long does it take?'),
   dict(en='The main entrance, please.', pt='A entrada principal, por favor.', reply='OK. How long does it take?'),
   dict(en='It’s on Oak Street.', pt='Fica na Rua Oak.', reply='OK. How long does it take?')]),
  dict(npc=None, opts=[
   dict(en='About thirty minutes.', pt='Uns trinta minutos.', reply='And how much is it?'),
   dict(en='About twenty minutes with no traffic.', pt='Uns vinte minutos sem trânsito.', reply='Good. How much is it?'),
   dict(en='Maybe forty minutes. There’s traffic.', pt='Talvez quarenta minutos. Tem trânsito.', reply='OK. And how much is it?')]),
  dict(npc=None, opts=[
   dict(en='About forty dollars.', pt='Uns quarenta dólares.', reply='Thanks. Safe travels!'),
   dict(en='Around thirty dollars, I think.', pt='Uns trinta dólares, acho.', reply='OK, thanks. Safe travels!'),
   dict(en='The app shows fifty dollars.', pt='O aplicativo mostra cinquenta dólares.', reply='Fine, thanks. Safe travels!')])],
  change=['Há trânsito e a corrida vai demorar mais; ajuste o tempo.', 'Você esqueceu o terminal e precisa conferir o bilhete.', 'A pessoa quer pagar com cartão, mas só dinheiro é aceito.']),
 writing=dict(task='Escreva o que você diria ao entrar em um táxi para ir a um lugar da sua cidade: destino, tempo e preço.', model='To the airport, please. How long does it take? How much is it? About thirty minutes and forty dollars is OK.', kw=['airport', 'please', 'long', 'much'], checks=['Disse o destino com “please”.', 'Perguntei quanto tempo demora.', 'Perguntei o preço.']),
 scenes=dict(pool=['street', 'airport', 'airport2', 'busstop'], npc=dict(g='m', role='driver'), you=dict(g='f')),
 convo=dict(npc=dict(name='Marco'), turns=[
  dict(npc='Hi! Where to?', pt='Oi! Para onde?', opts=[
   dict(en='I am in a taxi.', pt='Eu estou num táxi.', ok=False, fb='Óbvio, mas não diz o destino.'),
   dict(en='To the airport, please.', pt='Para o aeroporto, por favor.', ok=True, fb='Destino claro e educado.'),
   dict(en='Yes, hello.', pt='Sim, olá.', ok=False, fb='“Where to?” pede um lugar, não sim ou não.')]),
  dict(npc='Sure. Which terminal?', pt='Claro. Qual terminal?', opts=[
   dict(en='Terminal two.', pt='Terminal dois.', ok=True, fb='Responde com o terminal.'),
   dict(en='Two airports.', pt='Dois aeroportos.', ok=False, fb='Ele pergunta qual terminal, não quantos aeroportos.'),
   dict(en='The airport is big.', pt='O aeroporto é grande.', ok=False, fb='Não responde.')]),
  dict(npc='How long does it take?', pt='Quanto tempo demora?', opts=[
   dict(en='About forty dollars.', pt='Uns quarenta dólares.', ok=False, fb='Isso é preço, não tempo.'),
   dict(en='I take a taxi every day.', pt='Eu pego táxi todo dia.', ok=False, fb='Fala de hábito, não da duração.'),
   dict(en='About thirty minutes.', pt='Uns trinta minutos.', ok=True, fb='Estimativa de tempo com “about”.')]),
  dict(npc='How much is it?', pt='Quanto custa?', opts=[
   dict(en='About forty dollars.', pt='Uns quarenta dólares.', ok=True, fb='Estimativa de preço.'),
   dict(en='About thirty minutes.', pt='Uns trinta minutos.', ok=False, fb='Isso é tempo, não preço.'),
   dict(en='Terminal two, please.', pt='Terminal dois, por favor.', ok=False, fb='Isso já foi dito.')]),
  dict(npc='Safe travels!', pt='Boa viagem!', opts=[
   dict(en='Thanks! Bye!', pt='Valeu! Tchau!', ok=True, fb='Agradece e se despede.'),
   dict(en='Where to?', pt='Para onde?', ok=False, fb='É pergunta do motorista, no começo.'),
   dict(en='Welcome to the airport.', pt='Bem-vindo ao aeroporto.', ok=False, fb='Frase de quem recebe alguém, não de quem sai.')])]),
)
