X = dict(
 key=dict(big="Can I borrow some sugar?", label="Pedir algo emprestado ao vizinho", sub="Comece com Can I ask you a favor?, peça com Can I borrow...? e agradeça no fim."),
 mini=[
  dict(who="Miles", en="Hi, {Pearl|Ana|Sam}! Can I ask you a favor?", pt="Oi, {Pearl|Ana|Sam}! Posso pedir um favor?"),
  dict(who="You", en="Of course, honey. What is it?", pt="Claro, querido. O que é?"),
  dict(who="Miles", en="Can I borrow {some sugar|some flour|some butter}? Just {one cup|two cups|a little}, please.", pt="Posso pegar {um pouco de açúcar|um pouco de farinha|um pouco de manteiga} emprestado? {Uma xícara|Duas xícaras|Só um pouco}, por favor."),
  dict(who="You", en="Sure. Here you go. Are you baking?", pt="Claro. Aqui está. Você vai assar algo?"),
 ],
 dlg=[
  dict(who="Miles", en="Hi, {Pearl|Ana}! Can I ask you a favor?", pt="Oi, {Pearl|Ana}! Posso pedir um favor?"),
  dict(who="You", en="Of course, honey. What is it?", pt="Claro, querido. O que é?"),
  dict(who="Miles", en="Can I borrow some {sugar|flour|butter}?", pt="Posso pegar um pouco de {açúcar|farinha|manteiga} emprestado?"),
  dict(who="You", en="Sure. How much do you need?", pt="Claro. Quanto você precisa?"),
  dict(who="Miles", en="Just {one|two} {cup|cups}, please.", pt="Só {uma|duas} {xícara|xícaras}, por favor."),
  dict(who="You", en="Here you go. Are you {baking|cooking}?", pt="Aqui está. Você vai {assar algo|cozinhar}?"),
  dict(who="Miles", en="Yes, a {cake|pie|cookie} for tonight.", pt="Sim, {um bolo|uma torta|um biscoito} para hoje à noite."),
  dict(who="You", en="Nice! Save me a slice.", pt="Que bom! Guarde-me uma fatia."),
  dict(who="Miles", en="Thanks again. You're a lifesaver!", pt="Valeu de novo. Você me salvou!"),
 ],
 vocab=[
  dict(w="recipe", pt="receita", e="📖", ex=["This recipe is easy.", "I have a recipe for cake."]),
  dict(w="butter", pt="manteiga", e="🧈", ex=["I need some butter.", "The butter is on the table."]),
  dict(w="lend", pt="emprestar", e="🤲", ex=["Can you lend me a cup?", "I can lend you my ladder."]),
  dict(w="apron", pt="avental", e="👩‍🍳", ex=["She wears a blue apron.", "My apron is on the hook."]),
  dict(w="doorbell", pt="campainha", e="🔔", ex=["I ring the doorbell.", "The doorbell is loud."]),
  dict(w="frosting", pt="cobertura", e="🧁", ex=["The cake has pink frosting.", "I love chocolate frosting."]),
 ],
 molds=[
  dict(title="Pedir emprestado", frame="Can I borrow {thing}?", slots=[dict(key="thing", opts=["some sugar", "some flour", "some butter", "a ladder"])], model="Can I borrow some sugar?", note="Borrow = pegar emprestado. Com coisas que não se contam, use some."),
  dict(title="Dizer a quantidade", frame="Just {amount}, please.", slots=[dict(key="amount", opts=["one cup", "two cups", "a little", "one spoon"])], model="Just one cup, please.", note="Just = só. Boa forma curta de dizer a quantidade."),
  dict(title="Escrever o bilhete", frame="Hi, {name}! Can I ask you a favor? Can I borrow {thing}? Just {amount}, please. Thanks, you're a lifesaver!", slots=[dict(key="name", opts=["Pearl", "Ana", "Sam"]), dict(key="thing", opts=["some sugar", "some flour", "some butter"]), dict(key="amount", opts=["one cup", "two cups", "a little"])], model="Hi, Pearl! Can I ask you a favor? Can I borrow some sugar? Just one cup, please. Thanks, you're a lifesaver!", note="Cumprimente, peça o favor, diga o quê e quanto, e agradeça."),
 ],
 sounds=[
  dict(say="Can I ask you a favor?", tag="redução: ask you", tip="Ask you soa 'as-kyu' ou 'ask-ya'. Acentue ASK e FA-vor."),
  dict(say="How much do you need?", tag="redução: do you", tip="Do you vira 'dya': how-much-dya-NEED."),
  dict(say="Here you go.", tag="redução: here you", tip="Here you soa 'heer-ya'. Diga rápido e leve: HERE-ya-GO."),
 ],
 role=dict(turns=[
  dict(npc="Hi, Miles! What's up?", opts=[
   dict(en="Hi, Pearl! Can I ask you a favor?", pt="Oi, Pearl! Posso pedir um favor?", reply="Of course, honey. What is it?"),
   dict(en="Hi! I need a small favor.", pt="Oi! Preciso de um favorzinho.", reply="Of course. What is it?"),
   dict(en="Hello, Pearl. Do you have a minute?", pt="Olá, Pearl. Você tem um minuto?", reply="Sure. What is it?")]),
  dict(npc="What is it?", opts=[
   dict(en="Can I borrow some sugar?", pt="Posso pegar um pouco de açúcar emprestado?", reply="Sure. How much do you need?"),
   dict(en="Can I borrow some flour?", pt="Posso pegar um pouco de farinha emprestada?", reply="Sure. How much do you need?"),
   dict(en="Can I borrow your ladder?", pt="Posso pegar sua escada emprestada?", reply="Of course. How long do you need it?")]),
  dict(npc="How much do you need?", opts=[
   dict(en="Just one cup, please.", pt="Só uma xícara, por favor.", reply="Here you go. Are you baking?"),
   dict(en="Just two cups, please.", pt="Só duas xícaras, por favor.", reply="Here you go. Are you baking?"),
   dict(en="Just a little, please.", pt="Só um pouquinho, por favor.", reply="Here you go. Are you baking?")]),
  dict(npc="Here you go. Are you baking?", opts=[
   dict(en="Yes, a cake for tonight.", pt="Sim, um bolo para hoje à noite.", reply="Nice! Save me a slice."),
   dict(en="Yes, cookies for my sister.", pt="Sim, biscoitos para minha irmã.", reply="Nice! Save me a cookie."),
   dict(en="Yes, a pie for dinner.", pt="Sim, uma torta para o jantar.", reply="Nice! Save me a slice.")]),
 ], change=["Pearl não tem açúcar: agradeça e pergunte se ela tem outra coisa.", "Você quer devolver amanhã: diga quando vai trazer de volta.", "Pearl quer ajudar a assar: aceite ou recuse com educação."]),
 writing=dict(task="Escreva um bilhete curto a um vizinho: peça um favor, peça algo emprestado e agradeça.", model="Hi, Pearl! Can I ask you a favor? Can I borrow some sugar? Just one cup, please. Thanks, you're a lifesaver!", kw=["favor", "borrow", "sugar", "thanks"], checks=["Pediu um favor.", "Usou borrow certo.", "Agradeceu."]),
 scenes=dict(pool=["lobby", "lobby1", "lobby2", "hall"], npc=dict(g="f", role="neighbor"), you=dict(g="m")),
 convo=dict(npc=dict(name="Pearl"), story="Você é o Miles e precisa de açúcar. Bate na porta da vizinha Pearl.", turns=[
  dict(npc="Hi, Miles! Come in.", pt="Oi, Miles! Entre.", opts=[
   dict(en="Hi, Pearl! Can I ask you a favor?", pt="Oi, Pearl! Posso pedir um favor?", ok=True, fb="Começa o pedido com educação."),
   dict(en="Here you go.", pt="Aqui está.", ok=False, fb="Essa frase é de quem entrega algo."),
   dict(en="Just one cup, please.", pt="Só uma xícara, por favor.", ok=False, fb="Você ainda não disse o que precisa.")]),
  dict(npc="Of course, honey. What is it?", pt="Claro, querido. O que é?", opts=[
   dict(en="Can I borrow some sugar?", pt="Posso pegar um pouco de açúcar emprestado?", ok=True, fb="Faz o pedido."),
   dict(en="How much do you need?", pt="Quanto você precisa?", ok=False, fb="Quem pergunta isso é a vizinha."),
   dict(en="Nice! Save me a slice.", pt="Que bom! Guarde-me uma fatia.", ok=False, fb="Ainda não falaram de bolo.")]),
  dict(npc="Sure. How much do you need?", pt="Claro. Quanto você precisa?", opts=[
   dict(en="Just one cup, please.", pt="Só uma xícara, por favor.", ok=True, fb="Diz a quantidade."),
   dict(en="Yes, a cake for tonight.", pt="Sim, um bolo para hoje à noite.", ok=False, fb="Responde outra pergunta, a seguinte."),
   dict(en="Can I ask you a favor?", pt="Posso pedir um favor?", ok=False, fb="Você já pediu.")]),
  dict(npc="Here you go. Are you baking?", pt="Aqui está. Você vai assar algo?", opts=[
   dict(en="Yes, a cake for tonight.", pt="Sim, um bolo para hoje à noite.", ok=True, fb="Responde e diz o que vai fazer."),
   dict(en="Of course, honey.", pt="Claro, querido.", ok=False, fb="Essa frase é da vizinha."),
   dict(en="Can I borrow some sugar?", pt="Posso pegar um pouco de açúcar emprestado?", ok=False, fb="Você já recebeu o açúcar.")]),
  dict(npc="Nice! Save me a slice.", pt="Que bom! Guarde-me uma fatia.", opts=[
   dict(en="Sure! Thanks again. You're a lifesaver!", pt="Claro! Valeu de novo. Você me salvou!", ok=True, fb="Aceita e agradece."),
   dict(en="Here you go.", pt="Aqui está.", ok=False, fb="Ela não está pedindo algo agora."),
   dict(en="How much do you need?", pt="Quanto você precisa?", ok=False, fb="Essa pergunta é dela e já passou.")]),
 ]),
)
