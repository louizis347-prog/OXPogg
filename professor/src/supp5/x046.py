"""Bloco extra · aula 46: The bus stop."""
X = dict(
 key=dict(big='Does this bus go downtown?', label='Pegar o ônibus', sub='Antes de subir, pergunte se o ônibus vai ao seu destino, quanto custa e como pagar.'),
 mini=[
  dict(who='Ethan', en='Excuse me, does this bus go {downtown|to the park|to the airport}?', pt='Com licença, este ônibus vai {ao centro|ao parque|ao aeroporto}?'),
  dict(who='You', en='Yes, it goes {downtown|to the park|to the airport}.', pt='Sim, vai {ao centro|ao parque|ao aeroporto}.'),
  dict(who='Ethan', en='How much is the {fare|ticket|ride}?', pt='Quanto custa {a passagem|o bilhete|a viagem}?'),
  dict(who='You', en='It’s {two dollars and fifty cents|three dollars|two dollars}.', pt='Custa {dois dólares e cinquenta centavos|três dólares|dois dólares}.')],
 dlg=[
  dict(who='Ethan', en='Excuse me, does this bus go {downtown|to the park|to the airport}?', pt='Com licença, este ônibus vai {ao centro|ao parque|ao aeroporto}?'),
  dict(who='You', en='Yes, it goes {downtown|to the park|to the airport}.', pt='Sim, vai {ao centro|ao parque|ao aeroporto}.'),
  dict(who='Ethan', en='How much is the {fare|ticket|ride}?', pt='Quanto custa {a passagem|o bilhete|a viagem}?'),
  dict(who='You', en='{Two dollars and fifty cents|Three dollars|Two dollars}.', pt='{Dois dólares e cinquenta centavos|Três dólares|Dois dólares}.'),
  dict(who='Ethan', en='Do I pay the {driver|machine|cashier}?', pt='Pago {ao motorista|na máquina|ao caixa}?'),
  dict(who='You', en='Yes, or use a {card|phone|ticket}.', pt='Sim, ou use {um cartão|o celular|um bilhete}.'),
  dict(who='Ethan', en='How long does it take?', pt='Quanto tempo demora?'),
  dict(who='You', en='About {twenty|thirty|fifteen} minutes.', pt='Uns {vinte|trinta|quinze} minutos.'),
  dict(who='Ethan', en='Enjoy your {trip|day}!', pt='Aproveite a {viagem|o dia}!')],
 vocab=[
  dict(w='driver', pt='motorista', e='🧑‍✈️', ex=['The driver is friendly.', 'Pay the driver at the front.']),
  dict(w='fare', pt='passagem (preço)', e='💵', ex=['The fare is two dollars.', 'What is the fare to downtown?']),
  dict(w='downtown', pt='centro', e='🌆', ex=['This bus goes downtown.', 'My office is downtown.']),
  dict(w='wait', pt='esperar', e='⏳', ex=['I wait for the bus here.', 'Please wait five minutes.']),
  dict(w='seat', pt='assento', e='💺', ex=['Is this seat free?', 'There is a seat in the back.']),
  dict(w='bus stop', pt='ponto de ônibus', e='🚏', ex=['The bus stop is on the corner.', 'I wait at the bus stop.'])],
 molds=[
  dict(title='Perguntar o destino', frame='Excuse me, does this bus go {place}?', slots=[dict(key='place', opts=['downtown', 'to the airport', 'to the park', 'to the station'])], model='Excuse me, does this bus go downtown?', note='“Does this bus go…?” confirma o destino antes de embarcar.'),
  dict(title='Perguntar preço e tempo', frame='How much is the {thing}? How long does it take to {place}?', slots=[dict(key='thing', opts=['fare', 'ticket', 'ride']), dict(key='place', opts=['get downtown', 'get there', 'get home'])], model='How much is the fare? How long does it take to get downtown?', note='“How long does it take?” pergunta a duração da viagem.'),
  dict(title='Escrever a resposta', frame='The fare is {price}. You can pay the driver or use a {pay}. It takes about {n} minutes.', slots=[dict(key='price', opts=['two dollars', 'three dollars', 'two fifty']), dict(key='pay', opts=['card', 'phone', 'ticket']), dict(key='n', opts=['twenty', 'thirty', 'fifteen'])], model='The fare is two dollars. You can pay the driver or use a card. It takes about twenty minutes.', note='Resposta completa: preço, forma de pagar e duração.')],
 sounds=[
  dict(say='Does this bus go downtown?', tag='redução: does this', tip='“Does this” sai rápido, quase “duz-this”. A voz sobe no fim da pergunta.'),
  dict(say='How long does it take?', tag='ligação: take it', tip='Na pergunta, “does it” soa como “duzit”. O foco forte é em “long”.'),
  dict(say='Two dollars and fifty cents.', tag='ritmo: preço', tip='“And” é fraco: “two dollars-n-fifty cents”. Marque “dol-”, “fif-” e “cents”.')],
 role=dict(turns=[
  dict(npc='Excuse me, does this bus go downtown?', opts=[
   dict(en='Yes, it goes downtown.', pt='Sim, vai ao centro.', reply='Great. How much is the fare?'),
   dict(en='Yes, this is the right bus.', pt='Sim, este é o ônibus certo.', reply='Great. How much is the fare?'),
   dict(en='Yes, and it stops at the museum.', pt='Sim, e para no museu.', reply='Perfect! How much is the fare?')]),
  dict(npc=None, opts=[
   dict(en='Two dollars and fifty cents.', pt='Dois dólares e cinquenta centavos.', reply='OK. Do I pay the driver?'),
   dict(en='It’s about three dollars.', pt='Custa uns três dólares.', reply='OK. Do I pay the driver?'),
   dict(en='I think it’s two dollars.', pt='Acho que são dois dólares.', reply='OK. Do I pay the driver?')]),
  dict(npc=None, opts=[
   dict(en='Yes, or use a card.', pt='Sim, ou use um cartão.', reply='Good. How long does it take?'),
   dict(en='Yes, you pay when you get on.', pt='Sim, você paga quando entra.', reply='Good. How long does it take?'),
   dict(en='Yes. Cash or phone, both work.', pt='Sim. Dinheiro ou celular, ambos servem.', reply='Nice. How long does it take?')]),
  dict(npc=None, opts=[
   dict(en='About twenty minutes.', pt='Uns vinte minutos.', reply='Thanks! Enjoy your trip!'),
   dict(en='About thirty minutes in traffic.', pt='Uns trinta minutos no trânsito.', reply='OK, thanks! Enjoy your trip!'),
   dict(en='Fifteen minutes, I think.', pt='Quinze minutos, acho.', reply='Great, thanks! Enjoy your trip!')])],
  change=['A pessoa tem só notas grandes e pergunta se o motorista dá troco.', 'O ônibus não vai ao centro; indique outra linha.', 'A pessoa quer saber o horário do próximo ônibus.']),
 writing=dict(task='Escreva uma mensagem para um amigo explicando como ir de ônibus ao centro: preço, como pagar e quanto tempo demora.', model='Take the bus to downtown. The fare is two dollars. You can pay the driver or use a card. It takes about twenty minutes.', kw=['bus', 'fare', 'driver', 'minutes'], checks=['Disse o preço da passagem.', 'Expliquei como pagar.', 'Disse quanto tempo demora.']),
 scenes=dict(pool=['busstop', 'street', 'park2', 'station'], npc=dict(g='m', role='friend'), you=dict(g='f')),
 convo=dict(npc=dict(name='Ethan'), turns=[
  dict(npc='Excuse me, does this bus go downtown?', pt='Com licença, este ônibus vai ao centro?', opts=[
   dict(en='Yes, it goes downtown.', pt='Sim, vai ao centro.', ok=True, fb='Confirma o destino com o verbo certo.'),
   dict(en='Yes, I go downtown.', pt='Sim, eu vou ao centro.', ok=False, fb='A pergunta é sobre o ônibus, não sobre você.'),
   dict(en='This bus is very big.', pt='Este ônibus é muito grande.', ok=False, fb='Não responde sobre o destino.')]),
  dict(npc='How much is the fare?', pt='Quanto custa a passagem?', opts=[
   dict(en='It takes twenty minutes.', pt='Demora vinte minutos.', ok=False, fb='Isso responde a “how long”, não a “how much”.'),
   dict(en='Two dollars and fifty cents.', pt='Dois dólares e cinquenta centavos.', ok=True, fb='Dá o preço.'),
   dict(en='The driver is Tom.', pt='O motorista é o Tom.', ok=False, fb='Informação que ninguém pediu.')]),
  dict(npc='Do I pay the driver?', pt='Pago ao motorista?', opts=[
   dict(en='No, the driver pays you.', pt='Não, o motorista paga você.', ok=False, fb='Inverte quem paga.'),
   dict(en='Yes, or use a card.', pt='Sim, ou use um cartão.', ok=True, fb='Confirma e dá outra opção.'),
   dict(en='I pay the driver too.', pt='Eu também pago ao motorista.', ok=False, fb='Fala de você, mas a pergunta é o que ele deve fazer.')]),
  dict(npc='How long does it take?', pt='Quanto tempo demora?', opts=[
   dict(en='About twenty minutes.', pt='Uns vinte minutos.', ok=True, fb='Dá uma estimativa com “about”.'),
   dict(en='It takes two dollars.', pt='Demora dois dólares.', ok=False, fb='Mistura tempo com dinheiro.'),
   dict(en='I take a long bus.', pt='Eu pego um ônibus longo.', ok=False, fb='Frase estranha; responda com minutos.')]),
  dict(npc='Enjoy your trip!', pt='Aproveite a viagem!', opts=[
   dict(en='Bye! Take care.', pt='Tchau! Se cuide.', ok=True, fb='Despedida simpática de quem ajudou.'),
   dict(en='Excuse me, does this bus go downtown?', pt='Com licença, este ônibus vai ao centro?', ok=False, fb='Ele já perguntou isso.'),
   dict(en='You’re welcome. Bye!', pt='De nada. Tchau!', ok=False, fb='Ele ainda não agradeceu; “you’re welcome” fica cedo demais.')])]),
)
