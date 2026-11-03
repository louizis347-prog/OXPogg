"""Bloco extra · aula 50: At the gas station."""
X = dict(
 key=dict(big='Regular or premium?', label='Abastecer o carro', sub='Nos postos dos EUA, “regular” e “premium” são tipos de gasolina; o aviso de preço e a forma de pagar variam.'),
 mini=[
  dict(who='Jonah', en='Hi! Pump number {three|two|five}, please.', pt='Oi! Bomba número {três|dois|cinco}, por favor.'),
  dict(who='You', en='How much gas do you want?', pt='Quanto de gasolina você quer?'),
  dict(who='Jonah', en='{Twenty|Thirty|Ten} dollars, please.', pt='{Vinte|Trinta|Dez} dólares, por favor.'),
  dict(who='You', en='Do you want {regular|premium} or {premium|regular}?', pt='Quer {comum|premium} ou {premium|comum}?')],
 dlg=[
  dict(who='Jonah', en='Hi! Pump number {three|two|five}, please.', pt='Oi! Bomba número {três|dois|cinco}, por favor.'),
  dict(who='You', en='How much gas do you want?', pt='Quanto de gasolina você quer?'),
  dict(who='Jonah', en='{Twenty|Thirty|Ten} dollars, please.', pt='{Vinte|Trinta|Dez} dólares, por favor.'),
  dict(who='You', en='Do you want regular or premium?', pt='Quer comum ou premium?'),
  dict(who='Jonah', en='{Regular|Premium}, please.', pt='{Comum|Premium}, por favor.'),
  dict(who='You', en='Do you need anything else?', pt='Precisa de mais alguma coisa?'),
  dict(who='Jonah', en='A bottle of {water|juice|soda}.', pt='Uma garrafa de {água|suco|refrigerante}.'),
  dict(who='You', en='That’s {twenty-two|thirty-two|twelve} dollars.', pt='São {vinte e dois|trinta e dois|doze} dólares.'),
  dict(who='Jonah', en='Drive {safe|carefully|well}!', pt='Dirija {com segurança|com cuidado|bem}!')],
 vocab=[
  dict(w='gas', pt='gasolina', e='⛽', ex=['I need gas for the trip.', 'Gas is cheap here.']),
  dict(w='pump', pt='bomba', e='🛢️', ex=['Which pump is free?', 'Use pump number three.']),
  dict(w='regular', pt='comum', e='🅰️', ex=['I want regular gas.', 'Regular is cheaper than premium.']),
  dict(w='premium', pt='premium', e='⭐', ex=['Premium costs more.', 'This car uses premium gas.']),
  dict(w='bathroom', pt='banheiro', e='🚻', ex=['The bathroom is behind the store.', 'Where is the bathroom?']),
  dict(w='key', pt='chave', e='🔑', ex=['Ask for the key at the counter.', 'I lost my car key.'])],
 molds=[
  dict(title='Pedir a bomba', frame='Hi! Pump number {n}, please. {amount} dollars, {kind}.', slots=[dict(key='n', opts=['three', 'two', 'five']), dict(key='amount', opts=['Twenty', 'Thirty', 'Ten']), dict(key='kind', opts=['regular', 'premium', 'regular, please'])], model='Hi! Pump number three, please. Twenty dollars, regular.', note='Diga a bomba, o valor e o tipo de gasolina em frases curtas.'),
  dict(title='Atender no posto', frame='How much gas do you want? Do you want {a} or {b}?', slots=[dict(key='a', opts=['regular', 'premium', 'diesel']), dict(key='b', opts=['premium', 'regular', 'premium'])], model='How much gas do you want? Do you want regular or premium?', note='Duas perguntas curtas: quanto e qual tipo.'),
  dict(title='Escrever o total', frame='Pump {n}: {amount} dollars of gas and a bottle of {drink}. That’s {total} dollars.', slots=[dict(key='n', opts=['three', 'two', 'five']), dict(key='amount', opts=['twenty', 'thirty', 'ten']), dict(key='drink', opts=['water', 'juice', 'soda']), dict(key='total', opts=['twenty-two', 'thirty-two', 'twelve'])], model='Pump three: twenty dollars of gas and a bottle of water. That’s twenty-two dollars.', note='Resuma a compra numa frase com bomba, gasolina, item extra e total.')],
 sounds=[
  dict(say='Pump number three, please.', tag='ritmo: palavras fortes', tip='Marque “pump”, “num-” e “three”. “Please” fecha a frase com a voz descendo.'),
  dict(say='Regular or premium?', tag='acento: premium', tip='“Premium” tem acento em “pre-”: PRE-mi-um. A voz sobe em “regular” e desce em “premium”.'),
  dict(say='That’s twenty-two dollars.', tag='ritmo: números', tip='“Twenty-two” tem acento em “twen-” e em “two”. Diga junto, sem pausa.')],
 role=dict(turns=[
  dict(npc='Hi! Pump number three, please.', opts=[
   dict(en='How much gas do you want?', pt='Quanto de gasolina você quer?', reply='Twenty dollars, please.'),
   dict(en='Sure. How much gas?', pt='Claro. Quanto de gasolina?', reply='Twenty dollars, please.'),
   dict(en='OK, pump three. How much do you want?', pt='Ok, bomba três. Quanto quer?', reply='Thirty dollars, please.')]),
  dict(npc=None, opts=[
   dict(en='Do you want regular or premium?', pt='Quer comum ou premium?', reply='Regular, please.'),
   dict(en='Regular or premium?', pt='Comum ou premium?', reply='Premium, please.'),
   dict(en='OK. Which gas: regular or premium?', pt='Ok. Qual gasolina: comum ou premium?', reply='Regular, please.')]),
  dict(npc=None, opts=[
   dict(en='Do you need anything else?', pt='Precisa de mais alguma coisa?', reply='A bottle of water.'),
   dict(en='Anything else for you?', pt='Mais alguma coisa para você?', reply='Yes, a bottle of juice.'),
   dict(en='Do you want a drink or a snack?', pt='Quer uma bebida ou um lanche?', reply='A bottle of water, please.')]),
  dict(npc=None, opts=[
   dict(en='That’s twenty-two dollars.', pt='São vinte e dois dólares.', reply='Here you go. Thanks! Drive safe!'),
   dict(en='OK. The total is twenty-two dollars.', pt='Ok. O total é vinte e dois dólares.', reply='Here you go. Drive safe!'),
   dict(en='That’s twenty-two dollars. Cash or card?', pt='São vinte e dois dólares. Dinheiro ou cartão?', reply='Card, please. Drive safe!')])],
  change=['O cliente pergunta onde fica o banheiro.', 'A bomba três está quebrada; indique a bomba quatro.', 'O cliente quer pagar com cartão antes de abastecer.']),
 writing=dict(task='Escreva o que um cliente e o atendente dizem no posto: bomba, valor, tipo de gasolina e total.', model='Pump three, please. Twenty dollars of regular. Do you need anything else? That is twenty-two dollars.', kw=['pump', 'dollars', 'regular', 'else'], checks=['Citei a bomba e o valor.', 'Disse o tipo de gasolina.', 'Incluí o total ou a pergunta “anything else?”.']),
 scenes=dict(pool=['street', 'shop', 'counter', 'busstop'], npc=dict(g='m', role='customer'), you=dict(g='f')),
 convo=dict(npc=dict(name='Jonah'), turns=[
  dict(npc='Hi! Pump number three, please.', pt='Oi! Bomba número três, por favor.', opts=[
   dict(en='Sure. How much gas do you want?', pt='Claro. Quanto de gasolina você quer?', ok=True, fb='Aceita o pedido e pergunta a quantidade.'),
   dict(en='Yes, I am number three.', pt='Sim, eu sou o número três.', ok=False, fb='Confunde o número da bomba com a pessoa.'),
   dict(en='Where is the bathroom?', pt='Onde fica o banheiro?', ok=False, fb='É pergunta de cliente, não de quem atende.')]),
  dict(npc='Twenty dollars, please.', pt='Vinte dólares, por favor.', opts=[
   dict(en='Do you want regular or premium?', pt='Quer comum ou premium?', ok=True, fb='Falta saber o tipo de gasolina.'),
   dict(en='Thank you, goodbye.', pt='Obrigado, tchau.', ok=False, fb='O abastecimento ainda nem começou.'),
   dict(en='Twenty dollars is gas.', pt='Vinte dólares é gasolina.', ok=False, fb='Frase sem sentido útil.')]),
  dict(npc='Regular, please.', pt='Comum, por favor.', opts=[
   dict(en='You are regular.', pt='Você é comum.', ok=False, fb='Mudou o sentido de “regular”.'),
   dict(en='Premium is better.', pt='Premium é melhor.', ok=False, fb='Contraria o cliente sem necessidade.'),
   dict(en='Do you need anything else?', pt='Precisa de mais alguma coisa?', ok=True, fb='Pergunta típica de atendimento.')]),
  dict(npc='A bottle of water.', pt='Uma garrafa de água.', opts=[
   dict(en='That’s twenty-two dollars.', pt='São vinte e dois dólares.', ok=True, fb='Diz o total.'),
   dict(en='The key is in the car.', pt='A chave está no carro.', ok=False, fb='Não tem relação com o pedido.'),
   dict(en='Water is gas.', pt='Água é gasolina.', ok=False, fb='Confunde os produtos.')]),
  dict(npc='Drive safe!', pt='Dirija com segurança!', opts=[
   dict(en='Thanks! Have a nice day!', pt='Valeu! Tenha um bom dia!', ok=True, fb='Agradece e se despede.'),
   dict(en='Which pump, please?', pt='Qual bomba, por favor?', ok=False, fb='A compra acabou; não cabe perguntar isso.'),
   dict(en='Pump number three, please.', pt='Bomba número três, por favor.', ok=False, fb='Isso foi dito no começo.')])]),
)
