X = dict(
key=dict(big='Let\'s get pizza at seven.', label='Combinar um encontro por mensagem', sub='Sugira com Let\'s, diga a hora com at e o lugar com at/near: at seven, near the park.'),
mini=[
 dict(who='Cole', en='Hey! Are you free {tonight|tomorrow|on Friday}?', pt='Ei! Você está livre {hoje à noite|amanhã|na sexta}?'),
 dict(who='You', en='Yes! What\'s {up|new|the plan}?', pt='Estou! {O que foi|O que há de novo|Qual é o plano}?'),
 dict(who='Cole', en='Let\'s get {pizza|burgers|tacos} at {six|seven|eight}.', pt='Vamos comer {pizza|hambúrguer|tacos} às {seis|sete|oito}.'),
 dict(who='You', en='Sounds {great|good|perfect}! Where?', pt='{Ótimo|Boa|Perfeito}! Onde?'),
],
dlg=[
 dict(who='Cole', en='Hey! Are you free {tonight|tomorrow|on Friday}?', pt='Ei! Você está livre {hoje à noite|amanhã|na sexta}?'),
 dict(who='You', en='Yes! What\'s up?', pt='Estou! O que foi?'),
 dict(who='Cole', en='Let\'s get {pizza|burgers|tacos} at seven.', pt='Vamos comer {pizza|hambúrguer|tacos} às sete.'),
 dict(who='You', en='Sounds {great|good|perfect}! Where?', pt='{Ótimo|Boa|Perfeito}! Onde?'),
 dict(who='Cole', en='At Joe\'s Pizza, {near the park|near the station|next to the bank}.', pt='Na Joe\'s Pizza, {perto do parque|perto da estação|ao lado do banco}.'),
 dict(who='You', en='OK. I\'ll be there.', pt='Ok. Eu chego lá.'),
 dict(who='Cole', en='Can you {text|call|message} Mia too?', pt='Pode {mandar mensagem|ligar|escrever} pra Mia também?'),
 dict(who='You', en='Sure. See you at {seven|six|eight}!', pt='Claro. Até as {sete|seis|oito}!'),
 dict(who='Cole', en='Can\'t wait! See you!', pt='Mal posso esperar! Até lá!'),
],
vocab=[
 dict(w='text', pt='mandar mensagem', e='💬', ex=['I\'ll text you later.', 'Can you text Mia?']),
 dict(w='tonight', pt='hoje à noite', e='🌙', ex=['Are you free tonight?', 'We have dinner tonight.']),
 dict(w='pizza', pt='pizza', e='🍕', ex=['Let\'s get pizza.', 'The pizza is hot.']),
 dict(w='meet', pt='encontrar', e='🤝', ex=['Let\'s meet at seven.', 'I\'ll meet you at the park.']),
 dict(w='park', pt='parque', e='🌳', ex=['The pizza place is near the park.', 'We walk in the park.']),
 dict(w='free', pt='livre, disponível', e='🆓', ex=['Are you free on Friday?', 'I\'m free after six.']),
],
molds=[
 dict(title='Convidar', frame='Are you free {when}? Let\'s get {food}.', slots=[dict(key='when', opts=['tonight', 'tomorrow', 'on Friday']), dict(key='food', opts=['pizza', 'burgers', 'tacos'])], model='Are you free tonight? Let\'s get pizza.', note='Are you free…? é um convite aberto. Let\'s get… sugere o plano.'),
 dict(title='Marcar hora e lugar', frame='Let\'s meet at {time}, {place}.', slots=[dict(key='time', opts=['six', 'seven', 'eight']), dict(key='place', opts=['near the park', 'near the station', 'at the café'])], model='Let\'s meet at six, near the park.', note='Hora com at: at six. Lugar com near/at.'),
 dict(title='Escrever uma mensagem', frame='Sounds {adj}! I\'ll be {place}. See you at {time}!', slots=[dict(key='adj', opts=['great', 'good', 'perfect']), dict(key='place', opts=['there', 'at the park', 'at Joe\'s']), dict(key='time', opts=['seven', 'six', 'eight'])], model='Sounds great! I\'ll be there. See you at seven!', note='Sounds great! aceita um plano. I\'ll be there. promete chegar.'),
],
sounds=[
 dict(say='Are you free tonight?', tag='ligação: are you', tip='Are you soa "ar-yu". O acento forte cai em to-NIGHT.'),
 dict(say='Let\'s get pizza at seven.', tag='ritmo: palavras fortes', tip='Bata o ritmo nas fortes: LET\'s get PIZ-za at SE-ven. At fica fraco.'),
 dict(say='Can\'t wait!', tag='acento: can\'t', tip='Can\'t tem vogal longa e forte; can (afirmativo) é curto e fraco. Aqui: "kant WAIT".'),
],
role=dict(turns=[
 dict(npc='Hey! Are you free tonight?', opts=[
  dict(en='Yes! What\'s up?', pt='Estou! O que foi?', reply='Let\'s get pizza at seven.'),
  dict(en='Yes, I am. What\'s the plan?', pt='Estou, sim. Qual é o plano?', reply='Let\'s get pizza at seven.'),
  dict(en='I think so. Why?', pt='Acho que sim. Por quê?', reply='Let\'s get pizza at seven.')]),
 dict(npc='Let\'s get pizza at seven.', opts=[
  dict(en='Sounds great! Where?', pt='Ótimo! Onde?', reply='At Joe\'s Pizza, near the park.'),
  dict(en='Good idea! Where do we meet?', pt='Boa ideia! Onde nos encontramos?', reply='At Joe\'s Pizza, near the park.'),
  dict(en='Perfect. Which place?', pt='Perfeito. Qual lugar?', reply='Joe\'s Pizza, near the park.')]),
 dict(npc='At Joe\'s Pizza, near the park.', opts=[
  dict(en='OK. I\'ll be there.', pt='Ok. Eu chego lá.', reply='Great! Can you text Mia too?'),
  dict(en='I know it. See you there!', pt='Conheço. Até lá!', reply='Great! Can you text Mia too?'),
  dict(en='Perfect. I\'ll be there at seven.', pt='Perfeito. Chego lá às sete.', reply='Great! Can you text Mia too?')]),
 dict(npc='Can you text Mia too?', opts=[
  dict(en='Sure. See you at seven!', pt='Claro. Até as sete!', reply='Can\'t wait! See you!'),
  dict(en='Yes, I\'ll text her now.', pt='Sim, mando mensagem agora.', reply='Thanks! See you at seven!'),
  dict(en='OK. I\'ll call her too.', pt='Ok. Eu também ligo pra ela.', reply='Thanks! See you at seven!')]),
], change=['Você não pode às sete e propõe oito horas.', 'Você não conhece a pizzaria e pergunta como chegar.', 'A Mia responde que não pode ir; avise o Cole.']),
writing=dict(task='Escreva uma mensagem curta convidando um amigo para comer algo: diga quando, onde e peça uma resposta.', model='Hey! Are you free tonight? Let\'s get pizza at seven near the park. Can you text me?', kw=['free', 'tonight', 'pizza', 'seven'], checks=['Fez o convite com Are you free…?', 'Disse a hora com at.', 'Disse o lugar.']),
scenes=dict(pool=['cafe', 'park', 'street', 'diner', 'restaurant'], npc=dict(g='m', role='friend'), you=dict(g='f')),
convo=dict(npc=dict(name='Cole'), story='Seu amigo Cole manda mensagens para combinar uma pizza hoje à noite.', turns=[
 dict(npc='Hey! Are you free tonight?', pt='Ei! Você está livre hoje à noite?', opts=[
  dict(en='Yes! What\'s up?', pt='Estou! O que foi?', ok=True, fb='Aceita e pergunta o plano.'),
  dict(en='I\'m fine, thanks.', pt='Estou bem, obrigada.', ok=False, fb='Free aqui é "disponível", não "bem".'),
  dict(en='I\'m free at the park.', pt='Estou livre no parque.', ok=False, fb='A pergunta é se você pode hoje à noite; o lugar vem depois.')]),
 dict(npc='Let\'s get pizza at seven.', pt='Vamos comer pizza às sete.', opts=[
  dict(en='Yes, I get it.', pt='Sim, eu entendo.', ok=False, fb='Get it quer dizer "entender", e Cole fez um convite.'),
  dict(en='Sounds great! Where?', pt='Ótimo! Onde?', ok=True, fb='Aceita e pergunta o lugar.'),
  dict(en='I\'m eating pizza now.', pt='Estou comendo pizza agora.', ok=False, fb='Ele sugere um plano futuro; responda ao convite.')]),
 dict(npc='At Joe\'s Pizza, near the park.', pt='Na Joe\'s Pizza, perto do parque.', opts=[
  dict(en='OK. I\'ll be there.', pt='Ok. Eu chego lá.', ok=True, fb='Confirma que vai.'),
  dict(en='Where is Joe\'s Pizza?', pt='Onde fica a Joe\'s Pizza?', ok=False, fb='Ele acabou de dizer: perto do parque.'),
  dict(en='Let\'s get pizza at seven.', pt='Vamos comer pizza às sete.', ok=False, fb='Foi ele quem sugeriu isso; repetir não avança.')]),
 dict(npc='Can you text Mia too?', pt='Pode mandar mensagem pra Mia também?', opts=[
  dict(en='Sure. See you at seven!', pt='Claro. Até as sete!', ok=True, fb='Aceita o pedido e confirma a hora.'),
  dict(en='Yes, Mia is my friend.', pt='Sim, a Mia é minha amiga.', ok=False, fb='Cole pediu uma ação, não uma informação sobre a Mia.'),
  dict(en='No, I\'m free tonight.', pt='Não, estou livre hoje à noite.', ok=False, fb='A resposta não responde ao pedido.')]),
 dict(npc='Can\'t wait! See you!', pt='Mal posso esperar! Até lá!', opts=[
  dict(en='See you! Bye!', pt='Até! Tchau!', ok=True, fb='Despedida natural.'),
  dict(en='Are you free tonight?', pt='Você está livre hoje à noite?', ok=False, fb='O plano já está feito.'),
  dict(en='Sorry, I can\'t come.', pt='Desculpe, não posso ir.', ok=False, fb='Contradiz tudo o que você combinou.')]),
]),
)
