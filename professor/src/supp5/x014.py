X = dict(
key=dict(big='Hello? Who is this?', label='Atender e se identificar ao telefone', sub='Ao telefone, diga This is… para se identificar e Is … there? para pedir alguém.'),
mini=[
 dict(who='Victor', en='{Hello?|Hi?|Yes?}', pt='{Alô?|Oi?|Pois não?}'),
 dict(who='You', en='Hi, is {Raj|Mia|Sam} there?', pt='Oi, {o Raj|a Mia|o Sam} está?'),
 dict(who='Victor', en='This is Raj. Who is {this|calling|speaking}?', pt='É o Raj. Quem {fala|está ligando|fala}?'),
 dict(who='You', en='It\'s your {neighbor|friend|classmate}.', pt='É seu {vizinho|amigo|colega de turma}.'),
],
dlg=[
 dict(who='Victor', en='{Hello?|Hi?|Yes?}', pt='{Alô?|Oi?|Pois não?}'),
 dict(who='You', en='Hi, is {Raj|Mia|Sam} there?', pt='Oi, {o Raj|a Mia|o Sam} está?'),
 dict(who='Victor', en='This is Raj. Who is this?', pt='É o Raj. Quem fala?'),
 dict(who='You', en='It\'s your {neighbor|friend|classmate} from 4B.', pt='É seu {vizinho|amigo|colega de turma} do 4B.'),
 dict(who='Victor', en='Oh, {hi|hello|hey}! How can I help you?', pt='Ah, {oi|olá|ei}! Como posso ajudar?'),
 dict(who='You', en='Can you open the {door|window|gate}? I forgot my {key|phone|bag}.', pt='Pode abrir a {porta|janela|portão}? Esqueci {minha chave|meu celular|minha bolsa}.'),
 dict(who='Victor', en='Sure. I\'m coming {now|soon|later}.', pt='Claro. Estou indo {agora|logo|depois}.'),
 dict(who='You', en='Thanks, you\'re the best!', pt='Valeu, você é demais!'),
 dict(who='Victor', en='Anytime. Bye!', pt='Quando quiser. Tchau!'),
],
vocab=[
 dict(w='call', pt='ligar; ligação', e='📞', ex=['I\'ll call you later.', 'Thanks for the call.']),
 dict(w='phone', pt='telefone', e='📱', ex=['My phone is in my bag.', 'He answers the phone.']),
 dict(w='message', pt='recado', e='💬', ex=['Can I leave a message?', 'I have a message for Raj.']),
 dict(w='later', pt='depois', e='🕒', ex=['Call me later, please.', 'See you later!']),
 dict(w='speak', pt='falar', e='🗣️', ex=['Can I speak to Mia?', 'Please speak slowly.']),
 dict(w='neighbor', pt='vizinho', e='🏠', ex=['I am your neighbor.', 'My neighbor is friendly.']),
],
molds=[
 dict(title='Pedir alguém ao telefone', frame='Hi, is {name} there? Can I speak to {name}?', slots=[dict(key='name', opts=['Raj', 'Mia', 'Sam'])], model='Hi, is Raj there? Can I speak to Raj?', note='Duas formas de pedir alguém: Is … there? e Can I speak to …? Ambas são naturais.'),
 dict(title='Se identificar', frame='This is {name}. I\'m your {who} from {place}.', slots=[dict(key='name', opts=['Ana', 'Leo', 'Bia']), dict(key='who', opts=['neighbor', 'friend', 'classmate']), dict(key='place', opts=['4B', 'work', 'class'])], model='This is Ana. I\'m your neighbor from 4B.', note='Ao telefone diga This is…, não "I am…" logo no começo.'),
 dict(title='Deixar um recado', frame='Can you tell {name} to call me {when}?', slots=[dict(key='name', opts=['Raj', 'Mia', 'Sam']), dict(key='when', opts=['later', 'tonight', 'tomorrow'])], model='Can you tell Raj to call me later?', note='tell + pessoa + to + verbo: um recado simples.'),
],
sounds=[
 dict(say='Hello? Who is this?', tag='entonação: sobe no Hello?', tip='Em Hello? a voz sobe no fim. Em Who is this? a voz desce.'),
 dict(say='Can I speak to Raj?', tag='redução: can I', tip='Can I soa "kn-ai": can é fraco e liga com I.'),
 dict(say='I forgot my key.', tag='ligação: forgot my', tip='Forgot my: o t quase some e liga com my: "for-GOT-mai". Acento em GOT.'),
],
role=dict(turns=[
 dict(npc='Hello?', opts=[
  dict(en='Hi, is Raj there?', pt='Oi, o Raj está?', reply='This is Raj. Who is this?'),
  dict(en='Hello! Can I speak to Raj?', pt='Olá! Posso falar com o Raj?', reply='This is Raj. Who is this?'),
  dict(en='Hi! Is this Raj?', pt='Oi! É o Raj?', reply='Yes, this is Raj. Who is this?')]),
 dict(npc='Who is this?', opts=[
  dict(en='It\'s your neighbor from 4B.', pt='É seu vizinho do 4B.', reply='Oh, hi! How can I help you?'),
  dict(en='This is Ana, from 4B.', pt='É a Ana, do 4B.', reply='Oh, hi, Ana! How can I help you?'),
  dict(en='It\'s Leo. I\'m your neighbor.', pt='É o Leo. Sou seu vizinho.', reply='Oh, hi, Leo! How can I help you?')]),
 dict(npc='How can I help you?', opts=[
  dict(en='Can you open the door? I forgot my key.', pt='Pode abrir a porta? Esqueci minha chave.', reply='Sure. I\'m coming now.'),
  dict(en='I forgot my key. Can you open the gate?', pt='Esqueci minha chave. Pode abrir o portão?', reply='Sure. I\'m coming now.'),
  dict(en='Can you help me, please? The door is locked.', pt='Pode me ajudar, por favor? A porta está trancada.', reply='Sure. I\'m coming now.')]),
 dict(npc='Sure. I\'m coming now.', opts=[
  dict(en='Thanks, you\'re the best!', pt='Valeu, você é demais!', reply='Anytime. Bye!'),
  dict(en='Thank you so much!', pt='Muito obrigado!', reply='No problem. Bye!'),
  dict(en='Great, thanks! Bye!', pt='Ótimo, valeu! Tchau!', reply='Anytime. Bye!')]),
], change=['Outra pessoa atende e diz que o Raj não está; peça para deixar um recado.', 'A ligação está ruim; peça para repetir devagar.', 'Você ligou para o número errado; peça desculpas.']),
writing=dict(task='Escreva 2 ou 3 frases de um recado de telefone: quem você é, para quem é e o que a pessoa deve fazer.', model='Hi Raj, this is Ana from 4B. I forgot my key. Please call me later.', kw=['this', 'forgot', 'key', 'call'], checks=['Se identificou com This is.', 'Disse o problema ou motivo.', 'Pediu uma ação com please ou can you.']),
scenes=dict(pool=['lobby', 'street', 'living', 'hall', 'home1'], npc=dict(g='m', role='neighbor'), you=dict(g='f')),
convo=dict(npc=dict(name='Victor'), story='Você liga para o vizinho Raj, mas é Victor quem atende o telefone.', turns=[
 dict(npc='Hello?', pt='Alô?', opts=[
  dict(en='Hi, is Raj there?', pt='Oi, o Raj está?', ok=True, fb='Pede a pessoa de forma natural.'),
  dict(en='Bye, then!', pt='Tchau!', ok=False, fb='Goodbye é despedida; você acabou de ligar.'),
  dict(en='I am fine, and you?', pt='Estou bem, e você?', ok=False, fb='Ao atender, a pessoa não pergunta como você está; diga quem procura.')]),
 dict(npc='This is Raj. Who is this?', pt='É o Raj. Quem fala?', opts=[
  dict(en='Yes, this is Raj.', pt='Sim, aqui é o Raj.', ok=False, fb='Raj é quem atende; você deve dizer quem é você.'),
  dict(en='It\'s your neighbor from 4B.', pt='É seu vizinho do 4B.', ok=True, fb='Se identifica com clareza.'),
  dict(en='I am ready.', pt='Estou pronto.', ok=False, fb='Who is this? pede seu nome ou quem você é.')]),
 dict(npc='Oh, hi! How can I help you?', pt='Ah, oi! Como posso ajudar?', opts=[
  dict(en='Can you open the door? I forgot my key.', pt='Pode abrir a porta? Esqueci minha chave.', ok=True, fb='Pede ajuda e explica o motivo.'),
  dict(en='No, thank you. I am OK.', pt='Não, obrigado. Estou bem.', ok=False, fb='Você ligou porque precisa de algo; aceite a ajuda.'),
  dict(en='You are welcome.', pt='De nada.', ok=False, fb='Ainda não houve agradecimento.')]),
 dict(npc='Sure. I\'m coming now.', pt='Claro. Estou indo agora.', opts=[
  dict(en='Sorry, wrong number.', pt='Desculpe, número errado.', ok=False, fb='Você ligou para a pessoa certa; essa fala não combina.'),
  dict(en='Who is this?', pt='Quem fala?', ok=False, fb='Você já sabe: é o Raj.'),
  dict(en='Thanks, you\'re the best!', pt='Valeu, você é demais!', ok=True, fb='Agradece com calor.')]),
 dict(npc='Anytime. Bye!', pt='Quando quiser. Tchau!', opts=[
  dict(en='Bye! See you soon.', pt='Tchau! Até logo.', ok=True, fb='Despedida natural.'),
  dict(en='Hello? Is Raj there?', pt='Alô? O Raj está?', ok=False, fb='A conversa está terminando.'),
  dict(en='Please call me later.', pt='Por favor, ligue mais tarde.', ok=False, fb='Ele já está vindo; não precisa de nova ligação.')]),
]),
)
