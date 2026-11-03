X = dict(
key=dict(big='Mine is blue. Yours?', label='Dizer de quem é e a cor', sub='Use this/that para perto e longe, e mine/yours para dono: This one is mine.'),
mini=[
 dict(who='Kai', en='Excuse me, is this your {bag|phone|jacket}?', pt='Com licença, {esta é sua bolsa|este é seu celular|esta é sua jaqueta}?'),
 dict(who='You', en='No, mine is {blue|black|green}. This one is {red|white|yellow}.', pt='Não, {a minha é azul|a minha é preta|a minha é verde}. {Esta é vermelha|Esta é branca|Esta é amarela}.'),
 dict(who='Kai', en='Is that your bag {over there|by the door|on the chair}?', pt='Aquela é sua bolsa {ali|perto da porta|na cadeira}?'),
 dict(who='You', en='Yes! That\'s {mine|my bag|my red bag}. Thank you!', pt='Sim! {É minha|É minha bolsa|É minha bolsa vermelha}. Valeu!'),
],
dlg=[
 dict(who='Kai', en='Excuse me, is this your {bag|phone|jacket}?', pt='Com licença, {esta é sua bolsa|este é seu celular|esta é sua jaqueta}?'),
 dict(who='You', en='No, mine is {blue|black|green}. This one is red.', pt='Não, {a minha é azul|a minha é preta|a minha é verde}. Esta é vermelha.'),
 dict(who='Kai', en='Is that your bag {over there|by the door|on the chair}?', pt='Aquela ali é sua bolsa {ali|perto da porta|na cadeira}?'),
 dict(who='You', en='Yes! That\'s mine. Thank you!', pt='Sim! É minha. Valeu!'),
 dict(who='Kai', en='What color is your {phone|bag|jacket}?', pt='Que cor é {seu celular|sua bolsa|sua jaqueta}?'),
 dict(who='You', en='It\'s {black|blue|gray}. And yours?', pt='É {preto|azul|cinza}. E o seu?'),
 dict(who='Kai', en='Mine is {white|green|red}.', pt='O meu é {branco|verde|vermelho}.'),
 dict(who='You', en='Nice colors!', pt='Que cores legais!'),
 dict(who='Kai', en='Take care of your things!', pt='Cuide das suas coisas!'),
],
vocab=[
 dict(w='red', pt='vermelho', e='🔴', ex=['My bag is red.', 'The red jacket is Kai\'s.']),
 dict(w='blue', pt='azul', e='🔵', ex=['My phone is blue.', 'I like the blue bag.']),
 dict(w='green', pt='verde', e='🟢', ex=['The green hat is on the chair.', 'Her bag is green.']),
 dict(w='black', pt='preto', e='⚫', ex=['My phone is black.', 'He has a black jacket.']),
 dict(w='white', pt='branco', e='⚪', ex=['Kai\'s phone is white.', 'I have a white bag.']),
 dict(w='bag', pt='bolsa, mochila', e='👜', ex=['Is this your bag?', 'My bag is on the chair.']),
],
molds=[
 dict(title='Perguntar de quem é', frame='Is {obj} {owner}?', slots=[dict(key='obj', opts=['this bag', 'that bag', 'this phone']), dict(key='owner', opts=['yours', 'hers', 'his'])], model='Is this bag yours?', note='This é para algo perto; that, para algo mais longe. Yours/hers/his dizem de quem é.'),
 dict(title='Dizer a cor', frame='{whose} is {color}.', slots=[dict(key='whose', opts=['Mine', 'Yours', 'Hers']), dict(key='color', opts=['blue', 'black', 'white'])], model='Mine is blue.', note='Mine, yours e hers substituem "meu/seu/dela" sem repetir o objeto.'),
 dict(title='Descrever por escrito', frame='My {thing} is {color}. It\'s {place}.', slots=[dict(key='thing', opts=['bag', 'phone', 'jacket']), dict(key='color', opts=['red', 'black', 'green']), dict(key='place', opts=['on the chair', 'by the door', 'over there'])], model='My bag is red. It\'s on the chair.', note='Cor depois de is; lugar no fim: on the chair, by the door.'),
],
sounds=[
 dict(say='Is this your bag?', tag='ligação: is this', tip='Junte as palavras: "iz-dhis-yor-bag". O acento forte cai em BAG.'),
 dict(say='What color is your phone?', tag='ligação: what color', tip='What color soa "wot-KUH-ler". A sílaba forte de color é a primeira.'),
 dict(say='Thank you!', tag='som: th', tip='Em thank, ponha a língua entre os dentes e solte o ar, sem virar "t" nem "f".'),
],
role=dict(turns=[
 dict(npc='Excuse me, is this your bag?', opts=[
  dict(en='No, mine is blue. This one is red.', pt='Não, a minha é azul. Esta é vermelha.', reply='Oh, sorry! Is that your bag over there?'),
  dict(en='No, mine is black.', pt='Não, a minha é preta.', reply='Oh, sorry! Is that your bag over there?'),
  dict(en='No, that\'s not mine. Mine is green.', pt='Não, essa não é minha. A minha é verde.', reply='Oh, sorry! Is that your bag over there?')]),
 dict(npc='Is that your bag over there?', opts=[
  dict(en='Yes! That\'s mine. Thank you!', pt='Sim! É minha. Valeu!', reply='You\'re welcome. What color is your phone?'),
  dict(en='Yes, it\'s mine. Thanks a lot!', pt='Sim, é minha. Muito obrigado!', reply='No problem. What color is your phone?'),
  dict(en='Yes, the blue one. Thank you!', pt='Sim, a azul. Valeu!', reply='Great! What color is your phone?')]),
 dict(npc='What color is your phone?', opts=[
  dict(en='It\'s black. And yours?', pt='É preto. E o seu?', reply='Mine is white.'),
  dict(en='It\'s gray. And yours?', pt='É cinza. E o seu?', reply='Mine is white.'),
  dict(en='My phone is blue. What about yours?', pt='Meu celular é azul. E o seu?', reply='Mine is white.')]),
 dict(npc='Mine is white. Take care of your things!', opts=[
  dict(en='Nice colors! You too.', pt='Que cores legais! Você também.', reply='Thanks! Bye!'),
  dict(en='Thanks! I will. Bye!', pt='Valeu! Vou cuidar. Tchau!', reply='Bye!'),
  dict(en='Good advice. See you!', pt='Bom conselho. Até!', reply='See you!')]),
], change=['Você não sabe qual bolsa é a sua porque há duas azuis; descreva a sua com outro detalhe.', 'Kai acha que o celular branco é seu; corrija com educação.', 'Você perdeu o celular e descreve cor e lugar onde o deixou.']),
writing=dict(task='Escreva 2 ou 3 frases para um aviso de objeto perdido: o que é, a cor e onde está.', model='My bag is red. It\'s on the chair. Is this your bag? Mine is blue.', kw=['bag', 'red', 'chair', 'mine'], checks=['Disse o objeto e a cor.', 'Disse onde o objeto está.', 'Usou mine ou your.']),
scenes=dict(pool=['shop', 'street', 'cafe', 'station', 'park'], npc=dict(g='m', role='stranger'), you=dict(g='f')),
convo=dict(npc=dict(name='Kai'), story='Você está numa loja e um desconhecido, Kai, pergunta de quem é uma bolsa.', turns=[
 dict(npc='Excuse me, is this your bag?', pt='Com licença, esta é sua bolsa?', opts=[
  dict(en='No, mine is blue. This one is red.', pt='Não, a minha é azul. Esta é vermelha.', ok=True, fb='Nega e diz qual é a sua.'),
  dict(en='Yes, I am.', pt='Sim, eu sou.', ok=False, fb='Is this your…? pede "yes, it is" ou "no, it isn\'t", não "I am".'),
  dict(en='Excuse me, where is the door?', pt='Com licença, onde fica a porta?', ok=False, fb='Kai fez uma pergunta sobre a bolsa; responda a ela primeiro.')]),
 dict(npc='Is that your bag over there?', pt='Aquela ali é sua bolsa?', opts=[
  dict(en='My bag is red.', pt='Minha bolsa é vermelha.', ok=False, fb='Kai quer saber se aquela bolsa é sua; comece com yes ou no.'),
  dict(en='Yes, you are welcome.', pt='Sim, de nada.', ok=False, fb='You\'re welcome só vem depois de um agradecimento.'),
  dict(en='Yes! That\'s mine. Thank you!', pt='Sim! É minha. Valeu!', ok=True, fb='Confirma e agradece.')]),
 dict(npc='What color is your phone?', pt='Que cor é seu celular?', opts=[
  dict(en='It\'s black. And yours?', pt='É preto. E o seu?', ok=True, fb='Responde e devolve a pergunta.'),
  dict(en='My phone is on the chair.', pt='Meu celular está na cadeira.', ok=False, fb='What color pede a cor, não o lugar.'),
  dict(en='It costs ten dollars.', pt='Custa dez dólares.', ok=False, fb='A pergunta é sobre cor, não sobre preço.')]),
 dict(npc='Mine is white.', pt='O meu é branco.', opts=[
  dict(en='What color is your phone?', pt='Que cor é seu celular?', ok=False, fb='Ele acabou de dizer a cor; a pergunta fica repetida.'),
  dict(en='Nice colors!', pt='Que cores legais!', ok=True, fb='Um comentário simpático.'),
  dict(en='No, thanks.', pt='Não, obrigado.', ok=False, fb='Kai não ofereceu nada; "No, thanks" não encaixa.')]),
 dict(npc='Take care of your things!', pt='Cuide das suas coisas!', opts=[
  dict(en='Thanks! You too. Bye!', pt='Valeu! Você também. Tchau!', ok=True, fb='Despedida natural.'),
  dict(en='Is this your bag?', pt='Esta é sua bolsa?', ok=False, fb='Essa pergunta já foi resolvida.'),
  dict(en='Excuse me, please.', pt='Com licença, por favor.', ok=False, fb='É uma despedida; use Thanks ou Bye.')]),
]),
)
