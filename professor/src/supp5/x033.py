X = dict(
 key=dict(big="How much is the bread?", label="Perguntar o preço", sub="Preços de pão e doces costumam ser por unidade: four dollars a loaf = quatro dólares cada pão."),
 mini=[
  dict(who="Ava", en="Hi! Can I {help you|help you today|help you with something}?", pt="Oi! Posso {ajudar|ajudar hoje|ajudar em algo}?"),
  dict(who="You", en="Yes. How much is the {bread|croissant|cake}?", pt="Sim. Quanto custa {o pão|o croissant|o bolo}?"),
  dict(who="Ava", en="{Four dollars a loaf.|Three dollars each.|Twenty dollars for the whole cake.}", pt="{Quatro dólares o pão.|Três dólares cada.|Vinte dólares o bolo inteiro.}"),
  dict(who="You", en="I'll take {one|two|three}, please.", pt="Vou levar {um|dois|três}, por favor."),
 ],
 dlg=[
  dict(who="Ava", en="Hi! Can I {help you|help you today}?", pt="Oi! Posso {ajudar|ajudar hoje}?"),
  dict(who="You", en="Yes. How much is the {bread|croissant|cake}?", pt="Sim. Quanto custa {o pão|o croissant|o bolo}?"),
  dict(who="Ava", en="{Four dollars a loaf.|Four dollars each.}", pt="{Quatro dólares o pão.|Quatro dólares cada.}"),
  dict(who="You", en="I'll take {one|two}, please.", pt="Vou levar {um|dois}, por favor."),
  dict(who="Ava", en="Anything else? The {cookies|croissants} are fresh.", pt="Mais alguma coisa? Os {biscoitos|croissants} são frescos."),
  dict(who="You", en="{Two cookies|Three cookies|One cookie}, please.", pt="{Dois biscoitos|Três biscoitos|Um biscoito}, por favor."),
  dict(who="Ava", en="That's six dollars.", pt="São seis dólares."),
  dict(who="You", en="Here you go. {Thanks!|Thank you!}", pt="Aqui está. {Valeu!|Obrigado!}"),
  dict(who="Ava", en="Have a {sweet|nice|great} day!", pt="Tenha um dia {doce|bom|ótimo}!"),
 ],
 vocab=[
  dict(w="bakery", pt="padaria", e="🥖", ex=["The bakery is open.", "I buy bread at the bakery."]),
  dict(w="croissant", pt="croissant", e="🥐", ex=["One croissant, please.", "The croissant is warm."]),
  dict(w="cookie", pt="biscoito", e="🍪", ex=["I'll take two cookies.", "This cookie has chocolate."]),
  dict(w="cake", pt="bolo", e="🎂", ex=["How much is the cake?", "The chocolate cake looks good."]),
  dict(w="fresh", pt="fresco, do dia", e="✨", ex=["The bread is fresh.", "Are the cookies fresh?"]),
  dict(w="loaf", pt="pão (inteiro)", e="🍞", ex=["A loaf of bread is four dollars.", "I'll take one loaf, please."]),
 ],
 molds=[
  dict(title="Perguntar o preço", frame="How much is the {item}?", slots=[dict(key="item", opts=["bread", "croissant", "cake", "cookie"])], model="How much is the bread?", note="How much is...? serve para qualquer produto. Use the e o nome no singular."),
  dict(title="Fazer o pedido", frame="I'll take {order}, please.", slots=[dict(key="order", opts=["one loaf", "two croissants", "three cookies"])], model="I'll take one loaf, please.", note="I'll take... = vou levar... Com one use o singular; com dois ou mais, o plural."),
  dict(title="Escrever o pedido", frame="Hi! Two {item}, please. How much is that?", slots=[dict(key="item", opts=["cookies", "croissants", "cakes"])], model="Hi! Two cookies, please. How much is that?", note="That = o total. É uma forma simples de perguntar quanto deu tudo."),
 ],
 sounds=[
  dict(say="How much is the bread?", tag="acento: much e bread", tip="As palavras fortes são much e bread. Is the fica curto e rápido."),
  dict(say="I'll take one, please.", tag="acento: take e one", tip="Dê força a take e one; I'll fica leve, quase 'ail'."),
  dict(say="That's six dollars.", tag="acento: six e dollars", tip="Six e dollars recebem o acento. 'That's' é bem curto."),
 ],
 role=dict(turns=[
  dict(npc="Hi! Can I help you?", opts=[
   dict(en="Yes. How much is the bread?", pt="Sim. Quanto custa o pão?", reply="Four dollars a loaf."),
   dict(en="Yes. How much is the cake?", pt="Sim. Quanto custa o bolo?", reply="Twenty dollars for the whole cake."),
   dict(en="Yes. How much are the cookies?", pt="Sim. Quanto custam os biscoitos?", reply="Two dollars each.")]),
  dict(npc="Four dollars a loaf.", opts=[
   dict(en="I'll take one, please.", pt="Vou levar um, por favor.", reply="One loaf. Great choice!"),
   dict(en="I'll take two, please.", pt="Vou levar dois, por favor.", reply="Two loaves. That's eight dollars."),
   dict(en="Okay. One loaf, please.", pt="Ok. Um pão, por favor.", reply="Sure! Here it is.")]),
  dict(npc="Anything else? The cookies are fresh.", opts=[
   dict(en="Two cookies, please.", pt="Dois biscoitos, por favor.", reply="Two cookies. Anything else?"),
   dict(en="One croissant, please.", pt="Um croissant, por favor.", reply="One croissant. It's still warm!"),
   dict(en="No, that's all, thanks.", pt="Não, é só isso, obrigado.", reply="Okay! That's all.")]),
  dict(npc="That's six dollars.", opts=[
   dict(en="Here you go. Thanks!", pt="Aqui está. Valeu!", reply="Thank you! Have a sweet day!"),
   dict(en="Here's ten dollars.", pt="Aqui estão dez dólares.", reply="Thanks! Here's your change."),
   dict(en="Can I pay by card?", pt="Posso pagar com cartão?", reply="Yes, of course.")]),
 ], change=["A padaria está sem croissants: escolha outro item.", "Você só tem uma nota de vinte dólares: pergunte se há troco.", "Você quer um bolo inteiro: pergunte o preço e peça uma caixa."]),
 writing=dict(task="Você quer comprar pães e doces. Escreva 2 ou 3 frases: pergunte um preço, diga o que vai levar e agradeça.", model="Hi! How much is the bread? I'll take one loaf and two cookies, please. Thank you!", kw=["much", "bread", "take", "cookies"], checks=["Perguntou o preço com How much.", "Disse o que vai levar com I'll take.", "Usou please ou thank you."]),
 scenes=dict(pool=["bakery", "market", "shop", "counter"], npc=dict(g="f", role="baker"), you=dict(g="m")),
 convo=dict(npc=dict(name="Ava"), story="Você está numa padaria. Pergunte o preço, peça e pague.", turns=[
  dict(npc="Hi! Can I help you?", pt="Oi! Posso ajudar?", opts=[
   dict(en="Yes, you can. I'm fine.", pt="Sim, pode. Estou bem.", ok=False, fb="Ela oferece ajuda com a compra, não pergunta como você está."),
   dict(en="Yes. How much is the bread?", pt="Sim. Quanto custa o pão?", ok=True, fb="Pergunta o preço de forma natural."),
   dict(en="Four dollars a loaf.", pt="Quatro dólares o pão.", ok=False, fb="Quem diz o preço é a padeira.")]),
  dict(npc="Four dollars a loaf.", pt="Quatro dólares o pão.", opts=[
   dict(en="I'll take one, please.", pt="Vou levar um, por favor.", ok=True, fb="Você decide comprar e é educado."),
   dict(en="It's four dollars, too.", pt="É quatro dólares também.", ok=False, fb="O preço já foi dito; agora é hora de escolher."),
   dict(en="Yes, I'm hungry.", pt="Sim, estou com fome.", ok=False, fb="Não responde ao preço; diga que vai levar o pão.")]),
  dict(npc="Anything else? The cookies are fresh.", pt="Mais alguma coisa? Os biscoitos são frescos.", opts=[
   dict(en="Have a sweet day!", pt="Tenha um dia doce!", ok=False, fb="Isso é uma despedida, e a conversa ainda não terminou."),
   dict(en="No, I'm a baker.", pt="Não, eu sou padeiro.", ok=False, fb="Não faz sentido: você é o cliente."),
   dict(en="Two cookies, please.", pt="Dois biscoitos, por favor.", ok=True, fb="Aceita a sugestão e pede a quantidade.")]),
  dict(npc="That's six dollars.", pt="São seis dólares.", opts=[
   dict(en="Here you go. Thanks!", pt="Aqui está. Valeu!", ok=True, fb="Você paga e agradece."),
   dict(en="How much is the bread?", pt="Quanto custa o pão?", ok=False, fb="O preço já foi falado; agora é hora de pagar."),
   dict(en="I'll take six, please.", pt="Vou levar seis, por favor.", ok=False, fb="Seis é o preço total, não a quantidade de itens.")]),
  dict(npc="Have a sweet day!", pt="Tenha um dia doce!", opts=[
   dict(en="Anything else?", pt="Mais alguma coisa?", ok=False, fb="Essa pergunta é de quem vende, não do cliente."),
   dict(en="Thanks! You too.", pt="Obrigado! Você também.", ok=True, fb="Resposta simpática à despedida."),
   dict(en="Two cookies, please.", pt="Dois biscoitos, por favor.", ok=False, fb="A compra já terminou.")]),
 ]),
)
