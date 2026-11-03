X = dict(
 key=dict(big="How much is it?", label="Quanto custa?", sub="A pergunta do preço no shopping. Depois dá para perguntar Is it on sale? para saber se tem desconto."),
 mini=[
  dict(who="Rosa", en="Look at this {bag|jacket|dress}! It's so cute.", pt="Olha {esta bolsa|esta jaqueta|este vestido}! É tão fofo."),
  dict(who="You", en="How much is it?", pt="Quanto custa?"),
  dict(who="Rosa", en="It's {fifty|thirty|sixty} dollars.", pt="São {cinquenta|trinta|sessenta} dólares."),
  dict(who="You", en="Is it on sale? That's {cheap|expensive|a good price}.", pt="Está em promoção? Isso é {barato|caro|um bom preço}."),
 ],
 dlg=[
  dict(who="Rosa", en="Look at this {bag!|dress!|jacket!} It's so cute.", pt="Olha {esta bolsa!|este vestido!|esta jaqueta!} É tão fofa."),
  dict(who="You", en="How {much|much money} is it?", pt="Quanto {custa?|custa?}"),
  dict(who="Rosa", en="It's {fifty|forty|sixty} dollars.", pt="São {cinquenta|quarenta|sessenta} dólares."),
  dict(who="You", en="Is it on {sale?|sale today?}", pt="Está em {promoção?|promoção hoje?}"),
  dict(who="Rosa", en="Yes, {thirty|twenty|fifty} percent off.", pt="Sim, {trinta|vinte|cinquenta} por cento de desconto."),
  dict(who="You", en="That's a good {price.|deal.}", pt="É um bom {preço.|negócio.}"),
  dict(who="Rosa", en="I'll {take it.|buy it.}", pt="Vou {levar.|comprar.}"),
  dict(who="You", en="{Cash|Card} or {card?|cash?}", pt="{Dinheiro|Cartão} ou {cartão?|dinheiro?}"),
  dict(who="Rosa", en="Thanks for {coming in!|shopping!}", pt="Obrigado por {vir!|comprar!}"),
 ],
 vocab=[
  dict(w="mall", pt="shopping center", e="🏬", ex=["The mall opens at ten.", "We meet at the mall."]),
  dict(w="cashier", pt="caixa (pessoa)", e="🧑‍💼", ex=["The cashier says hello.", "Ask the cashier, please."]),
  dict(w="receipt", pt="recibo / nota", e="🧾", ex=["Keep the receipt.", "Here's your receipt."]),
  dict(w="coupon", pt="cupom", e="🎟️", ex=["I have a coupon.", "The coupon is for ten percent off."]),
  dict(w="cheap", pt="barato", e="🪙", ex=["This shirt is cheap.", "The shoes are not cheap."]),
  dict(w="expensive", pt="caro", e="💎", ex=["That jacket is expensive.", "It's too expensive for me."]),
 ],
 molds=[
  dict(title="Perguntar o preço", frame="How much {verb}?", slots=[dict(key="verb", opts=["is it", "are they", "is this", "are these"])], model="How much is it?", note="Use is it para uma coisa e are they para várias (shoes, jeans)."),
  dict(title="Comentar o preço", frame="It's {adj}. That's {comment}.", slots=[dict(key="adj", opts=["cheap", "expensive", "on sale"]), dict(key="comment", opts=["a good price", "too much", "a good deal"])], model="It's cheap. That's a good price.", note="Cheap = barato, expensive = caro. A good price / a good deal = um bom preço."),
  dict(title="Escrever uma compra", frame="I bought a {item} for {price} dollars. It was {adj}!", slots=[dict(key="item", opts=["bag", "jacket", "dress"]), dict(key="price", opts=["thirty", "forty", "fifty"]), dict(key="adj", opts=["on sale", "cheap", "a good price"])], model="I bought a bag for thirty dollars. It was on sale!", note="Bought é o passado de buy. Dollars fica no plural."),
 ],
 sounds=[
  dict(say="Thirty, forty, fifty.", tag="acento: thirty × thirteen", tip="THIR-ty tem força no começo; thir-TEEN, no fim. Em preços isso importa."),
  dict(say="How much is it?", tag="ligação: much is", tip="Much is soa 'muchiz'. Una as palavras e suba a voz no final."),
  dict(say="Cash or card?", tag="entonação: lista de opções", tip="Na primeira opção a voz sobe (cash↗), na última desce (card↘)."),
 ],
 role=dict(turns=[
  dict(npc="Look at this bag! It's so cute.", opts=[
   dict(en="How much is it?", pt="Quanto custa?", reply="It's fifty dollars."),
   dict(en="Wow! How much is it?", pt="Uau! Quanto custa?", reply="It's fifty dollars."),
   dict(en="Nice! What's the price?", pt="Legal! Qual é o preço?", reply="It's fifty dollars.")]),
  dict(npc="It's fifty dollars.", opts=[
   dict(en="Is it on sale?", pt="Está em promoção?", reply="Yes, thirty percent off."),
   dict(en="Is there a discount?", pt="Tem desconto?", reply="Yes, thirty percent off."),
   dict(en="Is that the final price?", pt="É o preço final?", reply="No, it's thirty percent off.")]),
  dict(npc="Yes, thirty percent off.", opts=[
   dict(en="That's a good price.", pt="É um bom preço.", reply="I'll take it."),
   dict(en="That's a good deal.", pt="É um bom negócio.", reply="I'll take it."),
   dict(en="Nice! It's not expensive now.", pt="Legal! Não está caro agora.", reply="Right? I'll take it.")]),
  dict(npc="I'll take it.", opts=[
   dict(en="Cash or card?", pt="Dinheiro ou cartão?", reply="Card, please. Thanks for coming in!"),
   dict(en="Do you pay by card?", pt="Você paga no cartão?", reply="Yes, by card. Thanks for coming in!"),
   dict(en="Do you want a receipt?", pt="Quer o recibo?", reply="Yes, please. Thanks for coming in!")]),
 ], change=["A bolsa não está em promoção: pergunte se há outra mais barata.", "O cartão não passa: pergunte se pode pagar em dinheiro.", "Você perdeu o recibo: pergunte se ainda pode devolver."]),
 writing=dict(task="Você vê uma bolsa no shopping. Escreva 2 ou 3 frases: pergunte o preço, pergunte se está em promoção e diga como vai pagar.", model="Hi! How much is this bag? Is it on sale? I'll pay by card, please.", kw=["how much", "sale", "card", "bag"], checks=["Perguntou o preço.", "Perguntou da promoção.", "Disse como vai pagar."]),
 scenes=dict(pool=["market", "shop", "counter", "street"], npc=dict(g="f", role="friend"), you=dict(g="f")),
 convo=dict(npc=dict(name="Rosa"), story="Você está no shopping em Houston com a sua amiga Rosa. Ela vê uma bolsa.", turns=[
  dict(npc="Look at this bag! It's so cute.", pt="Olha esta bolsa! É tão fofa.", opts=[
   dict(en="Cash or card?", pt="Dinheiro ou cartão?", ok=False, fb="É cedo para falar de pagamento."),
   dict(en="How much is it?", pt="Quanto custa?", ok=True, fb="Pergunta o preço."),
   dict(en="Thanks for coming in!", pt="Obrigado por vir!", ok=False, fb="Essa frase é para o final, na saída.")]),
  dict(npc="It's fifty dollars.", pt="São cinquenta dólares.", opts=[
   dict(en="Is it on sale?", pt="Está em promoção?", ok=True, fb="Pergunta por desconto."),
   dict(en="I'll take it.", pt="Vou levar.", ok=False, fb="Você ainda não sabe do desconto."),
   dict(en="How much is it?", pt="Quanto custa?", ok=False, fb="Ela acabou de dizer o preço.")]),
  dict(npc="Yes, thirty percent off.", pt="Sim, trinta por cento de desconto.", opts=[
   dict(en="Is it on sale?", pt="Está em promoção?", ok=False, fb="Ela já respondeu que sim."),
   dict(en="That's a good price.", pt="É um bom preço.", ok=True, fb="Comenta que o preço ficou bom."),
   dict(en="It's fifty dollars.", pt="São cinquenta dólares.", ok=False, fb="Esse era o preço sem desconto, dito por ela.")]),
  dict(npc="I'll take it.", pt="Vou levar.", opts=[
   dict(en="Cash or card?", pt="Dinheiro ou cartão?", ok=True, fb="Pergunta como ela vai pagar."),
   dict(en="Look at this bag!", pt="Olha esta bolsa!", ok=False, fb="Essa fala foi dela, no começo."),
   dict(en="Is it on sale?", pt="Está em promoção?", ok=False, fb="Isso já foi respondido.")]),
  dict(npc="Thanks for coming in!", pt="Obrigada por vir!", opts=[
   dict(en="How much is it?", pt="Quanto custa?", ok=False, fb="Já terminou a compra."),
   dict(en="You're welcome. See you!", pt="De nada. Até mais!", ok=True, fb="Despedida simpática."),
   dict(en="I'll take it.", pt="Vou levar.", ok=False, fb="Essa fala já passou.")]),
 ]),
)
