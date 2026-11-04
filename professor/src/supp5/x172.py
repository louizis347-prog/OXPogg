X = dict(
 key=dict(big="I think there's a mistake", label="Pedido errado", sub="Chame o garçom com educação, diga o que pediu e peça para trocar. Frases curtas e calmas funcionam bem."),
 mini=[
  dict(who="You", en="Excuse me, I think there's a {mistake|problem|mix-up}.", pt="Com licença, acho que há um {erro|problema|engano}."),
  dict(who="Jonah", en="I'm sorry. What's the {problem?|matter?}", pt="Sinto muito. Qual é o {problema?|problema?}"),
  dict(who="You", en="I ordered {chicken|pasta|a salad}, not {fish.|soup.|pizza.}", pt="Pedi {frango|massa|uma salada}, não {peixe.|sopa.|pizza.}"),
  dict(who="Jonah", en="My {mistake.|bad.} I'll change it {now.|right away.|in ten minutes.}", pt="{Foi erro meu.|Foi culpa minha.} Vou trocar {agora.|já.|em dez minutos.}"),
 ],
 dlg=[
  dict(who="Jonah", en="Excuse me, I think there's a {mistake.|problem.}", pt="Com licença, acho que há um {erro.|problema.}"),
  dict(who="You", en="I'm {sorry.|sorry,} What's the {problem?|matter?}", pt="Sinto {muito.|muito.} Qual é o {problema?|problema?}"),
  dict(who="Jonah", en="I ordered {chicken,|pasta,} not {fish.|soup.}", pt="Pedi {frango,|massa,} não {peixe.|sopa.}"),
  dict(who="You", en="Oh no, I'm so {sorry.|sorry!}", pt="Ai, não, sinto {muito.|muito!}"),
  dict(who="Jonah", en="Can you {change|fix} it, please?", pt="Pode {trocar|resolver} isso, por favor?"),
  dict(who="You", en="Of course. It'll take {ten|five} minutes.", pt="Claro. Vai levar {dez|cinco} minutos."),
  dict(who="Jonah", en="That's okay. {Thank you.|Thanks.}", pt="Tudo bem. {Obrigado.|Valeu.}"),
  dict(who="You", en="Also, my {soup|food} is {cold.|warm.}", pt="Também, {minha sopa|minha comida} está {fria.|morna.}"),
  dict(who="Jonah", en="Let me {heat|warm} it up for you.", pt="Deixe-me {esquentar|esquentar} para você."),
 ],
 vocab=[
  dict(w="mistake", pt="erro", e="❌", ex=["There is a mistake.", "It is my mistake."]),
  dict(w="wrong", pt="errado", e="🙅", ex=["This is the wrong plate.", "My order is wrong."]),
  dict(w="warm", pt="morno, quente", e="♨️", ex=["The soup is warm.", "I want warm bread."]),
  dict(w="tasty", pt="gostoso", e="😋", ex=["The soup is tasty.", "This is a tasty dish."]),
  dict(w="sauce", pt="molho", e="🥫", ex=["I want more sauce.", "The sauce is red."]),
  dict(w="sorry", pt="sinto muito, desculpe", e="🙏", ex=["I'm sorry.", "Sorry, one more thing."]),
 ],
 molds=[
  dict(title="Dizer que há um problema", frame="Excuse me, my {thing} is {problem}.", slots=[dict(key="thing", opts=["soup", "food", "order"]), dict(key="problem", opts=["cold", "wrong", "missing"])], model="Excuse me, my soup is cold.", note="Is + problema descreve o que está errado. Cold = frio, wrong = errado."),
  dict(title="Dizer o que pediu", frame="I ordered {food}, not {other}.", slots=[dict(key="food", opts=["chicken", "soup", "pasta"]), dict(key="other", opts=["fish", "pizza", "rice"])], model="I ordered chicken, not fish.", note="Ordered é o passado de order. A estrutura 'X, not Y' mostra a diferença."),
  dict(title="Escrever o pedido de troca", frame="Hi! I think there's a mistake. Can you {action} my {thing}, please?", slots=[dict(key="action", opts=["change", "fix", "check"]), dict(key="thing", opts=["order", "plate", "soup"])], model="Hi! I think there's a mistake. Can you change my order, please?", note="Can you + verbo base pede um favor. Mantenha o tom calmo e educado."),
 ],
 sounds=[
  dict(say="I ordered chicken, not fish.", tag="ritmo: I ORdered CHIcken NOT FISH", tip="Acentue as palavras de conteúdo: ORdered, CHIcken, NOT, FISH. As outras ficam leves."),
  dict(say="Can you change it?", tag="redução: can you", tip="Can you soa 'kenya'. Una as duas palavras sem pausa."),
  dict(say="I'm so sorry.", tag="acento: SOrry", tip="Sorry tem acento no começo: SOR-ry. O o é aberto, como 'sór'."),
 ],
 role=dict(turns=[
  dict(npc="Here is your plate. Enjoy!", opts=[
   dict(en="Excuse me, I think there's a mistake.", pt="Com licença, acho que há um erro.", reply="I'm sorry. What's the problem?"),
   dict(en="Excuse me, this is not my order.", pt="Com licença, este não é o meu pedido.", reply="Oh, I'm sorry. What did you order?"),
   dict(en="Sorry, this is the wrong plate.", pt="Desculpe, este é o prato errado.", reply="Oh no. What's the problem?")]),
  dict(npc="What's the problem?", opts=[
   dict(en="I ordered chicken, not fish.", pt="Pedi frango, não peixe.", reply="Oh no, I'm so sorry."),
   dict(en="I ordered pasta, not pizza.", pt="Pedi massa, não pizza.", reply="Oh no, I'm so sorry."),
   dict(en="I ordered soup, not salad.", pt="Pedi sopa, não salada.", reply="My mistake. I'm sorry.")]),
  dict(npc="I'm so sorry.", opts=[
   dict(en="Can you change it, please?", pt="Pode trocar, por favor?", reply="Of course. It'll take ten minutes."),
   dict(en="Can you fix it, please?", pt="Pode resolver, por favor?", reply="Of course. It'll take ten minutes."),
   dict(en="Can I get the right plate?", pt="Posso receber o prato certo?", reply="Of course. It'll take ten minutes.")]),
  dict(npc="It'll take ten minutes.", opts=[
   dict(en="That's okay. Thank you.", pt="Tudo bem. Obrigado.", reply="Anything else?"),
   dict(en="Okay. Also, my soup is cold.", pt="Certo. Também, minha sopa está fria.", reply="Let me heat it up for you."),
   dict(en="No problem. Thanks.", pt="Sem problema. Obrigado.", reply="Anything else?")]),
 ], change=["O garçom traz o prato certo, mas falta o molho: peça o molho.", "A comida chegou muito fria: peça para esquentar.", "O garçom diz que o prato está acabando: escolha outro prato."]),
 writing=dict(task="Seu prato veio errado. Escreva 2 ou 3 frases: diga que há um erro, o que você pediu e peça para trocar.", model="Excuse me, I think there's a mistake. I ordered chicken, not fish. Can you change it, please?", kw=["mistake", "ordered", "not", "change"], checks=["Disse que há um erro.", "Disse o que pediu.", "Pediu a troca com educação."]),
 scenes=dict(pool=["diner", "restaurant", "counter", "cafe"], npc=dict(g="m", role="waiter"), you=dict(g="f")),
 convo=dict(npc=dict(name="Jonah"), story="Você é cliente em um restaurante em Denver. O Jonah é o garçom e seu pedido veio errado.", turns=[
  dict(npc="Here is your plate. Enjoy!", pt="Aqui está o seu prato. Bom apetite!", opts=[
   dict(en="Excuse me, I think there's a mistake.", pt="Com licença, acho que há um erro.", ok=True, fb="Abre o problema com educação."),
   dict(en="Of course. It'll take ten minutes.", pt="Claro. Vai levar dez minutos.", ok=False, fb="Quem diz isso é o garçom."),
   dict(en="Let me heat it up for you.", pt="Deixe-me esquentar para você.", ok=False, fb="Essa fala é do garçom.")]),
  dict(npc="I'm sorry. What's the problem?", pt="Sinto muito. Qual é o problema?", opts=[
   dict(en="Can you change it, please?", pt="Pode trocar, por favor?", ok=False, fb="Primeiro diga qual é o problema."),
   dict(en="I ordered chicken, not fish.", pt="Pedi frango, não peixe.", ok=True, fb="Explica o que está errado."),
   dict(en="Oh no, I'm so sorry.", pt="Ai, não, sinto muito.", ok=False, fb="O garçom é quem pede desculpas.")]),
  dict(npc="Oh no, I'm so sorry.", pt="Ai, não, sinto muito.", opts=[
   dict(en="Excuse me, I think there's a mistake.", pt="Com licença, acho que há um erro.", ok=False, fb="Você já disse isso."),
   dict(en="Of course. It'll take ten minutes.", pt="Claro. Vai levar dez minutos.", ok=False, fb="Quem diz isso é o garçom."),
   dict(en="Can you change it, please?", pt="Pode trocar, por favor?", ok=True, fb="Pedido educado de troca.")]),
  dict(npc="Of course. It'll take ten minutes.", pt="Claro. Vai levar dez minutos.", opts=[
   dict(en="That's okay. Thank you.", pt="Tudo bem. Obrigado.", ok=True, fb="Resposta calma e educada."),
   dict(en="I ordered chicken, not fish.", pt="Pedi frango, não peixe.", ok=False, fb="Você já explicou isso."),
   dict(en="What's the problem?", pt="Qual é o problema?", ok=False, fb="Quem pergunta isso é o garçom.")]),
  dict(npc="Anything else?", pt="Mais alguma coisa?", opts=[
   dict(en="No, it'll take ten minutes.", pt="Não, vai levar dez minutos.", ok=False, fb="Essa informação veio do garçom."),
   dict(en="Also, my soup is cold.", pt="Também, minha sopa está fria.", ok=True, fb="Adiciona o segundo problema."),
   dict(en="I think there's a mistake.", pt="Acho que há um erro.", ok=False, fb="Esse problema já foi resolvido.")]),
 ]),
)
