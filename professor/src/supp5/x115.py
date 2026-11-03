X = dict(
 key=dict(big="I need school supplies", label="Comprar material escolar", sub="Diga o que precisa, pergunte onde fica, o preço e a cor, e decida com I'll take."),
 mini=[
  dict(who="You", en="Hi! I need {school supplies|a notebook|a backpack}.", pt="Oi! Preciso de {material escolar|um caderno|uma mochila}."),
  dict(who="Rosa", en="What do you need? We have {pencils,|rulers,|erasers,} too.", pt="Do que você precisa? Também temos {lápis,|réguas,|borrachas,}"),
  dict(who="You", en="{Pencils|Notebooks|Markers} and a ruler.", pt="{Lápis|Cadernos|Canetas} e uma régua."),
  dict(who="Rosa", en="They're in aisle {four.|two.|six.}", pt="Estão no corredor {quatro.|dois.|seis.}"),
 ],
 dlg=[
  dict(who="Rosa", en="Hi! I need {school|art} supplies.", pt="Oi! Preciso de material {escolar.|de arte.}"),
  dict(who="You", en="What do you {need?|want?}", pt="Do que você {precisa?|quer?}"),
  dict(who="Rosa", en="{Pencils,|Markers,} notebooks and a {ruler.|calculator.}", pt="{Lápis,|Canetas,} cadernos e uma {régua.|calculadora.}"),
  dict(who="You", en="They're in aisle {four.|two.}", pt="Estão no corredor {quatro.|dois.}"),
  dict(who="Rosa", en="How {much|many} are the pencils?", pt="{Quanto custam|Quantos são} os lápis?"),
  dict(who="You", en="A pack of ten is {three|five} dollars.", pt="Um pacote com dez custa {três|cinco} dólares."),
  dict(who="Rosa", en="I'll {take|buy} two packs.", pt="Vou {levar|comprar} dois pacotes."),
  dict(who="You", en="What about a {backpack?|calculator?}", pt="E uma {mochila?|calculadora?}"),
  dict(who="Rosa", en="We have {red,|green,} blue and {black.|white.}", pt="Temos {vermelha,|verde,} azul e {preta.|branca.}"),
 ],
 vocab=[
  dict(w="pencil", pt="lápis", e="✏️", ex=["I need a pencil.", "This pencil is sharp."]),
  dict(w="ruler", pt="régua", e="📏", ex=["The ruler is long.", "I draw a line with a ruler."]),
  dict(w="eraser", pt="borracha", e="🧽", ex=["I need an eraser.", "The eraser is pink."]),
  dict(w="calculator", pt="calculadora", e="🧮", ex=["I use a calculator.", "The calculator is cheap."]),
  dict(w="notebook", pt="caderno", e="📓", ex=["Open your notebook.", "My notebook is blue."]),
  dict(w="glue", pt="cola", e="🧴", ex=["I need glue for the paper.", "The glue is in aisle four."]),
 ],
 molds=[
  dict(title="Dizer o que precisa", frame="I need {thing}.", slots=[dict(key="thing", opts=["school supplies", "a ruler", "two notebooks", "a calculator"])], model="I need school supplies.", note="I need + coisa. Need é verbo de estado: não use -ing."),
  dict(title="Perguntar onde fica", frame="Where {thing}?", slots=[dict(key="thing", opts=["are the pencils", "are the notebooks", "is the ruler"])], model="Where are the pencils?", note="Where are + plural. Para um item: Where is the ruler?"),
  dict(title="Escrever o pedido", frame="Hi! I'll take {n} packs of {thing}. How much is it?", slots=[dict(key="n", opts=["two", "three", "four"]), dict(key="thing", opts=["pencils", "erasers", "markers"])], model="Hi! I'll take two packs of pencils. How much is it?", note="I'll take… decide a compra. A pack of = um pacote de."),
 ],
 sounds=[
  dict(say="I need school supplies.", tag="som: s + consoante em school", tip="Comece com 'sk', sem vogal antes: 'skool', não 'iskool'. Acentue SCHOOL e SUP."),
  dict(say="How much are the pencils?", tag="ligação: much are", tip="Una much e are: 'mucha'. Acentue HOW e PEN; the fica fraco."),
  dict(say="I'll take two packs.", tag="som final: packs", tip="Termine em 'ks' sem vogal: 'paks', não 'paki-s'. A língua vai direto ao s."),
 ],
 role=dict(turns=[
  dict(npc="Hi! Can I help you?", opts=[
   dict(en="Yes. I need school supplies.", pt="Sim. Preciso de material escolar.", reply="What do you need?"),
   dict(en="Hi! Where are the notebooks?", pt="Oi! Onde ficam os cadernos?", reply="They're in aisle four."),
   dict(en="Hello. I'm looking for a backpack.", pt="Olá. Estou procurando uma mochila.", reply="We have red, blue and black.")]),
  dict(npc="What do you need?", opts=[
   dict(en="Pencils, notebooks and a ruler.", pt="Lápis, cadernos e uma régua.", reply="They're in aisle four."),
   dict(en="Two notebooks and an eraser.", pt="Dois cadernos e uma borracha.", reply="They're in aisle four."),
   dict(en="A calculator and a pack of pencils.", pt="Uma calculadora e um pacote de lápis.", reply="Calculators are in aisle five.")]),
  dict(npc="A pack of ten pencils is three dollars.", opts=[
   dict(en="I'll take two packs.", pt="Vou levar dois pacotes.", reply="Great. That's six dollars."),
   dict(en="Do you have a bigger pack?", pt="Vocês têm um pacote maior?", reply="Yes. A pack of twenty is five dollars."),
   dict(en="That's a good price. I'll take one.", pt="É um bom preço. Levo um.", reply="Okay, three dollars.")]),
  dict(npc="What about a backpack? We have red, blue and black.", opts=[
   dict(en="The blue one, please.", pt="A azul, por favor.", reply="Great choice!"),
   dict(en="Can I see the black one?", pt="Posso ver a preta?", reply="Sure, here it is."),
   dict(en="No, thanks. I have one.", pt="Não, obrigado. Eu já tenho uma.", reply="No problem.")]),
 ], change=["O lápis que você quer acabou: pergunte se há outro tipo.", "O preço está alto: pergunte se há promoção.", "Você não acha o corredor: peça para a Rosa mostrar o caminho."]),
 writing=dict(task="Escreva 2 ou 3 frases para uma lista de compras: diga o que precisa, quantos e uma cor.", model="I need two notebooks, a ruler and a pack of pencils. I want a blue backpack too.", kw=["need", "notebooks", "ruler", "backpack"], checks=["Disse o que precisa.", "Disse quantos ou qual cor.", "Usou I need ou I want."]),
 scenes=dict(pool=["shop", "supermarket", "bookshop", "counter"], npc=dict(g="f", role="clerk"), you=dict(g="m")),
 convo=dict(npc=dict(name="Rosa"), story="Você está em uma loja e precisa de material escolar. A Rosa trabalha lá e ajuda você.", turns=[
  dict(npc="Hi! Can I help you?", pt="Oi! Posso ajudar?", opts=[
   dict(en="What do you need?", pt="Do que você precisa?", ok=False, fb="Quem pergunta isso é ela."),
   dict(en="Yes. I need school supplies.", pt="Sim. Preciso de material escolar.", ok=True, fb="Diz o que você quer."),
   dict(en="They're in aisle four.", pt="Estão no corredor quatro.", ok=False, fb="Quem diz isso é ela.")]),
  dict(npc="What do you need?", pt="Do que você precisa?", opts=[
   dict(en="Pencils, notebooks and a ruler.", pt="Lápis, cadernos e uma régua.", ok=True, fb="Lista os itens."),
   dict(en="A pack of ten is three dollars.", pt="Um pacote com dez custa três dólares.", ok=False, fb="Quem diz o preço é ela."),
   dict(en="I'll take two packs.", pt="Vou levar dois pacotes.", ok=False, fb="Ainda não viu o preço.")]),
  dict(npc="They're in aisle four.", pt="Estão no corredor quatro.", opts=[
   dict(en="We have red, blue and black.", pt="Temos vermelha, azul e preta.", ok=False, fb="Quem fala das cores é ela."),
   dict(en="What do you need?", pt="Do que você precisa?", ok=False, fb="Ela já perguntou e você respondeu."),
   dict(en="Thanks! How much are the pencils?", pt="Obrigado! Quanto custam os lápis?", ok=True, fb="Pergunta o preço.")]),
  dict(npc="A pack of ten is three dollars.", pt="Um pacote com dez custa três dólares.", opts=[
   dict(en="I'll take two packs.", pt="Vou levar dois pacotes.", ok=True, fb="Decide a compra."),
   dict(en="How much are the pencils?", pt="Quanto custam os lápis?", ok=False, fb="Ela acabou de dizer o preço."),
   dict(en="They're in aisle four.", pt="Estão no corredor quatro.", ok=False, fb="Essa informação é dela.")]),
  dict(npc="What about a backpack? We have red, blue and black.", pt="E uma mochila? Temos vermelha, azul e preta.", opts=[
   dict(en="Pencils, notebooks and a ruler.", pt="Lápis, cadernos e uma régua.", ok=False, fb="Você já listou isso."),
   dict(en="What about a backpack?", pt="E uma mochila?", ok=False, fb="Ela acabou de perguntar."),
   dict(en="The blue one, please.", pt="A azul, por favor.", ok=True, fb="Escolhe a cor.")]),
 ]),
)
