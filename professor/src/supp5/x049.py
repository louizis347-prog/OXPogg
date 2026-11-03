"""Bloco extra · aula 49: Parking."""
X = dict(
 key=dict(big='No parking zone', label='Onde estacionar', sub='Placas dizem onde você pode ou não estacionar; leia a placa e, na dúvida, pergunte.'),
 mini=[
  dict(who='Rosa', en='Excuse me, can I park {here|there|in front of the shop}?', pt='Com licença, posso estacionar {aqui|ali|em frente à loja}?'),
  dict(who='You', en='No, this is a no parking {zone|area|spot}.', pt='Não, aqui é {zona|área|vaga} de estacionamento proibido.'),
  dict(who='Rosa', en='Where can I park?', pt='Onde posso estacionar?'),
  dict(who='You', en='There’s a parking lot on {Oak Street|Main Street|Park Street}.', pt='Tem um estacionamento na {Rua Oak|Rua Principal|Rua do Parque}.')],
 dlg=[
  dict(who='Rosa', en='Excuse me, can I park {here|there|in front of the shop}?', pt='Com licença, posso estacionar {aqui|ali|em frente à loja}?'),
  dict(who='You', en='No, this is a no parking {zone|area|spot}.', pt='Não, aqui é {zona|área|vaga} de estacionamento proibido.'),
  dict(who='Rosa', en='Where can I park?', pt='Onde posso estacionar?'),
  dict(who='You', en='There’s a parking lot on {Oak Street|Main Street|Park Street}.', pt='Tem um estacionamento na {Rua Oak|Rua Principal|Rua do Parque}.'),
  dict(who='Rosa', en='How much is it?', pt='Quanto custa?'),
  dict(who='You', en='{Five|Four|Six} dollars an hour.', pt='{Cinco|Quatro|Seis} dólares por hora.'),
  dict(who='Rosa', en='OK. Thanks for the {help|information|tip}.', pt='Ok. Valeu pela {ajuda|informação|dica}.'),
  dict(who='You', en='{No problem|You’re welcome|Anytime}!', pt='{Sem problema|De nada|Quando precisar}!'),
  dict(who='Rosa', en='Drive safe!', pt='Dirija com segurança!')],
 vocab=[
  dict(w='park', pt='estacionar', e='🅿️', ex=['Can I park here?', 'I park my car near the shop.']),
  dict(w='parking lot', pt='estacionamento', e='🏢', ex=['The parking lot is full.', 'There is a parking lot behind the bank.']),
  dict(w='hour', pt='hora', e='⏰', ex=['It is five dollars an hour.', 'I wait for one hour.']),
  dict(w='machine', pt='máquina', e='🏧', ex=['Pay at the machine.', 'The machine takes cards.']),
  dict(w='sign', pt='placa', e='🪧', ex=['Read the sign first.', 'The sign says no parking.']),
  dict(w='ticket', pt='bilhete / multa', e='🎟️', ex=['Take a ticket at the gate.', 'A parking ticket is expensive.'])],
 molds=[
  dict(title='Perguntar se pode', frame='Excuse me, can I park {where}?', slots=[dict(key='where', opts=['here', 'there', 'in front of the shop'])], model='Excuse me, can I park here?', note='“Can I…?” pede permissão de forma simples e educada.'),
  dict(title='Dizer onde estacionar', frame='There’s a parking lot on {street}. It’s {price} dollars an hour.', slots=[dict(key='street', opts=['Oak Street', 'Main Street', 'Park Street']), dict(key='price', opts=['five', 'four', 'six'])], model='There’s a parking lot on Oak Street. It’s five dollars an hour.', note='“There’s…” apresenta uma coisa que existe no lugar.'),
  dict(title='Escrever um aviso', frame='No parking {time}. You can park in the {place}.', slots=[dict(key='time', opts=['here', 'on weekdays', 'after six']), dict(key='place', opts=['parking lot', 'back', 'next street'])], model='No parking here. You can park in the parking lot.', note='Avisos são curtos: diga o que não pode e o que pode.')],
 sounds=[
  dict(say='Can I park here?', tag='redução: can I', tip='“Can I” vira “kenai”, fraco e junto. O foco é em “park”.'),
  dict(say='There’s a parking lot on Oak Street.', tag='ligação: there’s a', tip='“There’s a” liga como “theresuh”. Marque “park-”, “lot” e “Oak”.'),
  dict(say='Five dollars an hour.', tag='ligação: dollars an hour', tip='Junte: “dollar-san-hour”. O “h” de “hour” é mudo.')],
 role=dict(turns=[
  dict(npc='Excuse me, can I park here?', opts=[
   dict(en='No, this is a no parking zone.', pt='Não, aqui é proibido estacionar.', reply='Oh, thanks. Where can I park?'),
   dict(en='Sorry, no. Look at the sign.', pt='Desculpe, não. Olhe a placa.', reply='Oh, I see it. Where can I park?'),
   dict(en='Not here. It’s only for deliveries.', pt='Aqui não. É só para entregas.', reply='I see. Where can I park?')]),
  dict(npc=None, opts=[
   dict(en='There’s a parking lot on Oak Street.', pt='Tem um estacionamento na Rua Oak.', reply='Great. How much is it?'),
   dict(en='Try the parking lot behind the bank.', pt='Tente o estacionamento atrás do banco.', reply='Good idea. How much is it?'),
   dict(en='There’s a lot next to the park.', pt='Tem um estacionamento ao lado do parque.', reply='Perfect. How much is it?')]),
  dict(npc=None, opts=[
   dict(en='Five dollars an hour.', pt='Cinco dólares por hora.', reply='OK. Thanks for the help.'),
   dict(en='It’s five dollars an hour. Pay at the machine.', pt='São cinco dólares por hora. Pague na máquina.', reply='OK, the machine. Thanks for the help.'),
   dict(en='Four dollars an hour, I think.', pt='Quatro dólares por hora, acho.', reply='OK. Thanks for the help.')]),
  dict(npc=None, opts=[
   dict(en='No problem!', pt='Sem problema!', reply='Bye! Drive safe!'),
   dict(en='You’re welcome. Good luck!', pt='De nada. Boa sorte!', reply='Thanks! Drive safe!'),
   dict(en='Anytime! Have a nice day.', pt='Quando precisar! Tenha um bom dia.', reply='You too! Drive safe!')])],
  change=['O estacionamento está cheio; indique outro.', 'A pessoa quer saber se pode pagar com cartão na máquina.', 'A vaga é só por duas horas; explique o limite.']),
 writing=dict(task='Escreva um aviso curto para um estacionamento ou rua: o que é proibido e onde estacionar.', model='No parking here. There is a parking lot on Oak Street. It is five dollars an hour. Pay at the machine.', kw=['parking', 'lot', 'hour', 'machine'], checks=['Disse onde não pode estacionar.', 'Indiquei onde pode.', 'Informei o preço ou como pagar.']),
 scenes=dict(pool=['street', 'busstop', 'shop', 'supermarket'], npc=dict(g='f', role='friend'), you=dict(g='m')),
 convo=dict(npc=dict(name='Rosa'), turns=[
  dict(npc='Excuse me, can I park here?', pt='Com licença, posso estacionar aqui?', opts=[
   dict(en='No, this is a no parking zone.', pt='Não, aqui é proibido estacionar.', ok=True, fb='Responde que não e explica por quê.'),
   dict(en='Yes, I park here every day.', pt='Sim, eu estaciono aqui todo dia.', ok=False, fb='Responde sobre você, não sobre ela.'),
   dict(en='The car is very nice.', pt='O carro é muito bonito.', ok=False, fb='Não responde à pergunta.')]),
  dict(npc='Where can I park?', pt='Onde posso estacionar?', opts=[
   dict(en='Five dollars an hour.', pt='Cinco dólares por hora.', ok=False, fb='Isso é preço; ela perguntou onde.'),
   dict(en='There’s a parking lot on Oak Street.', pt='Tem um estacionamento na Rua Oak.', ok=True, fb='Indica um lugar concreto.'),
   dict(en='Yes, you can.', pt='Sim, pode.', ok=False, fb='Contradiz o que você disse antes.')]),
  dict(npc='How much is it?', pt='Quanto custa?', opts=[
   dict(en='Five dollars an hour.', pt='Cinco dólares por hora.', ok=True, fb='Preço claro com “an hour”.'),
   dict(en='It’s on Oak Street.', pt='Fica na Rua Oak.', ok=False, fb='Isso você já disse; ela pergunta o preço.'),
   dict(en='It takes one hour.', pt='Leva uma hora.', ok=False, fb='Mistura tempo com preço.')]),
  dict(npc='OK. Thanks for the help.', pt='Ok. Valeu pela ajuda.', opts=[
   dict(en='Thanks for the help too.', pt='Valeu pela ajuda também.', ok=False, fb='Você é quem ajudou.'),
   dict(en='Excuse me, can I park here?', pt='Com licença, posso estacionar aqui?', ok=False, fb='Essa pergunta já foi feita e respondida.'),
   dict(en='No problem!', pt='Sem problema!', ok=True, fb='Resposta natural a um agradecimento.')]),
  dict(npc='Drive safe!', pt='Dirija com segurança!', opts=[
   dict(en='Thanks! You too.', pt='Valeu! Você também.', ok=True, fb='Retribui o desejo.'),
   dict(en='I drive a car.', pt='Eu dirijo um carro.', ok=False, fb='Não responde ao desejo.'),
   dict(en='Park here, please.', pt='Estacione aqui, por favor.', ok=False, fb='Contradiz que aqui é proibido.')])]),
)
