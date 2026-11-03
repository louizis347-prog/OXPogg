X = dict(
key=dict(big='What does she look like?', label='Descrever uma pessoa', sub='Use She\'s + adjetivo (tall, shy) e She has + cabelo/olhos: She has long, dark hair.'),
mini=[
 dict(who='Cole', en='Who is that {woman|man|girl}?', pt='Quem é {aquela mulher|aquele homem|aquela menina}?'),
 dict(who='You', en='That\'s my {sister|brother|cousin}, Ana.', pt='É {minha irmã|meu irmão|minha prima}, Ana.'),
 dict(who='Cole', en='She\'s {tall|short|young}. What does she look like?', pt='Ela é {alta|baixa|jovem}. Como ela é?'),
 dict(who='You', en='She has {long|short|curly} hair. She\'s very {friendly|funny|kind}.', pt='Ela tem cabelo {longo|curto|cacheado}. Ela é muito {simpática|engraçada|gentil}.'),
],
dlg=[
 dict(who='Cole', en='Who is that {woman|girl|lady}?', pt='Quem é {aquela mulher|aquela menina|aquela senhora}?'),
 dict(who='You', en='That\'s my sister, Ana.', pt='É minha irmã, Ana.'),
 dict(who='Cole', en='She\'s {tall|short|young}. Is she {shy|quiet|friendly}?', pt='Ela é {alta|baixa|jovem}. Ela é {tímida|quieta|simpática}?'),
 dict(who='You', en='No, she\'s very {friendly|funny|kind}.', pt='Não, ela é muito {simpática|engraçada|gentil}.'),
 dict(who='Cole', en='What does she look like?', pt='Como ela é?'),
 dict(who='You', en='She has {long|short|curly} hair.', pt='Ela tem cabelo {longo|curto|cacheado}.'),
 dict(who='Cole', en='She looks {nice|happy|kind}!', pt='Ela parece {legal|feliz|gentil}!'),
 dict(who='You', en='Come and meet her.', pt='Venha conhecê-la.'),
 dict(who='Cole', en='You\'ll like her!', pt='Você vai gostar dela!'),
],
vocab=[
 dict(w='tall', pt='alto', e='📏', ex=['My sister is tall.', 'He is tall and thin.']),
 dict(w='short', pt='baixo; curto', e='🤏', ex=['My brother is short.', 'She has short hair.']),
 dict(w='hair', pt='cabelo', e='💇', ex=['She has long hair.', 'His hair is dark.']),
 dict(w='eyes', pt='olhos', e='👀', ex=['She has brown eyes.', 'His eyes are green.']),
 dict(w='friendly', pt='simpático', e='😊', ex=['Ana is very friendly.', 'My neighbors are friendly.']),
 dict(w='shy', pt='tímido', e='🙈', ex=['Is she shy?', 'He is shy with new people.']),
],
molds=[
 dict(title='Dizer como a pessoa é', frame='She is {height} and {trait}.', slots=[dict(key='height', opts=['tall', 'short', 'young']), dict(key='trait', opts=['friendly', 'funny', 'kind'])], model='She is tall and friendly.', note='Be + adjetivo descreve: She is tall. Use and para ligar dois adjetivos.'),
 dict(title='Cabelo e olhos', frame='She has {length} {color} hair and {eyes} eyes.', slots=[dict(key='length', opts=['long', 'short', 'curly']), dict(key='color', opts=['dark', 'blond', 'brown']), dict(key='eyes', opts=['brown', 'green', 'blue'])], model='She has long dark hair and brown eyes.', note='Have/has para partes do corpo: has hair, has eyes. O adjetivo vem antes do nome.'),
 dict(title='Apresentar por escrito', frame='This is my {person}. She looks {adj}.', slots=[dict(key='person', opts=['sister', 'friend', 'cousin']), dict(key='adj', opts=['nice', 'happy', 'kind'])], model='This is my sister. She looks nice.', note='Looks + adjetivo diz a impressão: She looks nice. (parece legal)'),
],
sounds=[
 dict(say='What does she look like?', tag='ligação e ritmo: does she', tip='Does she soa "duh-shee". A força cai em LOOK. Like fica no fim, com a voz descendo.'),
 dict(say='She has long, dark hair.', tag='pausa: vírgula', tip='Faça uma pausa curta na vírgula; long e dark são fortes, hair também.'),
 dict(say='You\'ll like her!', tag='redução: you\'ll', tip='You\'ll soa "yool". Her perde o h: "lai-ker".'),
],
role=dict(turns=[
 dict(npc='Who is that woman?', opts=[
  dict(en='That\'s my sister, Ana.', pt='É minha irmã, Ana.', reply='She\'s tall. Is she shy?'),
  dict(en='That\'s Ana. She\'s my sister.', pt='É a Ana. Ela é minha irmã.', reply='She\'s tall. Is she shy?'),
  dict(en='She\'s my sister. Her name is Ana.', pt='Ela é minha irmã. O nome dela é Ana.', reply='She\'s tall. Is she shy?')]),
 dict(npc='Is she shy?', opts=[
  dict(en='No, she\'s very friendly.', pt='Não, ela é muito simpática.', reply='Nice! What does she look like?'),
  dict(en='A little, but she\'s kind.', pt='Um pouco, mas é gentil.', reply='Nice! What does she look like?'),
  dict(en='No, she\'s funny and talkative.', pt='Não, ela é engraçada e falante.', reply='Nice! What does she look like?')]),
 dict(npc='What does she look like?', opts=[
  dict(en='She has long, dark hair.', pt='Ela tem cabelo longo e escuro.', reply='She looks nice!'),
  dict(en='She is tall, with brown eyes.', pt='Ela é alta, de olhos castanhos.', reply='She looks nice!'),
  dict(en='She has short curly hair.', pt='Ela tem cabelo curto e cacheado.', reply='She looks nice!')]),
 dict(npc='She looks nice!', opts=[
  dict(en='Come and meet her.', pt='Venha conhecê-la.', reply='You\'ll like her! Let\'s go.'),
  dict(en='Thanks! Let\'s say hello.', pt='Valeu! Vamos cumprimentá-la.', reply='Great! Let\'s go.'),
  dict(en='She is! Do you want to meet her?', pt='É mesmo! Quer conhecê-la?', reply='Yes, please!')]),
], change=['Cole confunde Ana com outra mulher; corrija descrevendo a roupa dela.', 'Cole pergunta como é seu irmão, que é baixo e usa óculos.', 'Ana está longe e Cole não a vê; descreva onde ela está.']),
writing=dict(task='Escreva 2 ou 3 frases descrevendo uma pessoa que você conhece: altura, cabelo e personalidade.', model='This is my sister, Ana. She is tall and friendly. She has long, dark hair.', kw=['sister', 'tall', 'friendly', 'hair'], checks=['Disse quem é a pessoa.', 'Usou is/has corretamente.', 'Descreveu cabelo ou aparência e personalidade.']),
scenes=dict(pool=['park', 'park2', 'street', 'cafe', 'hall'], npc=dict(g='m', role='friend'), you=dict(g='f')),
convo=dict(npc=dict(name='Cole'), story='No parque, Cole vê a sua irmã e pergunta como ela é.', turns=[
 dict(npc='Who is that woman?', pt='Quem é aquela mulher?', opts=[
  dict(en='That\'s my sister, Ana.', pt='É minha irmã, Ana.', ok=True, fb='Apresenta quem ela é.'),
  dict(en='She is tall.', pt='Ela é alta.', ok=False, fb='Who pergunta quem é, não como é.'),
  dict(en='Yes, she is.', pt='Sim, ela é.', ok=False, fb='Who is…? não é pergunta de sim ou não.')]),
 dict(npc='She\'s tall. Is she shy?', pt='Ela é alta. Ela é tímida?', opts=[
  dict(en='No, she\'s very friendly.', pt='Não, ela é muito simpática.', ok=True, fb='Responde e dá o contraste.'),
  dict(en='No, she has hair.', pt='Não, ela tem cabelo.', ok=False, fb='Hair não é uma característica de personalidade.'),
  dict(en='Yes, I do.', pt='Sim, eu sou.', ok=False, fb='Is she…? pede "Yes, she is." / "No, she isn\'t."')]),
 dict(npc='What does she look like?', pt='Como ela é?', opts=[
  dict(en='She likes music.', pt='Ela gosta de música.', ok=False, fb='Look like pergunta a aparência, não o gosto.'),
  dict(en='She has long, dark hair.', pt='Ela tem cabelo longo e escuro.', ok=True, fb='Descreve a aparência com has.'),
  dict(en='She is my sister.', pt='Ela é minha irmã.', ok=False, fb='Isso já foi dito.')]),
 dict(npc='She looks nice!', pt='Ela parece legal!', opts=[
  dict(en='Come and meet her.', pt='Venha conhecê-la.', ok=True, fb='Convida de forma natural.'),
  dict(en='She is looking at me.', pt='Ela está olhando para mim.', ok=False, fb='Fora do contexto: ele elogiou a aparência dela.'),
  dict(en='No, she does not.', pt='Não, ela não.', ok=False, fb='Ele não fez uma pergunta.')]),
 dict(npc='You\'ll like her!', pt='Você vai gostar dela!', opts=[
  dict(en='I think so. Come on!', pt='Acho que sim. Vamos!', ok=True, fb='Reage e segue com o plano.'),
  dict(en='Who is that woman?', pt='Quem é aquela mulher?', ok=False, fb='Essa pergunta já foi feita no início.'),
  dict(en='She has long hair.', pt='Ela tem cabelo longo.', ok=False, fb='Isso já foi descrito; agora é hora de ir.')]),
]),
)
