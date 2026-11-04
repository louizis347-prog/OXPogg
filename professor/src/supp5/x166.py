X = dict(
 key=dict(big="Could you repeat that?", label="Pedir para repetir", sub="Quando não entender, peça com educação para repetir ou falar mais devagar. É muito comum e ninguém estranha."),
 mini=[
  dict(who="Mei", en="Hi! The total is {eight fifty|nine fifty|six fifty}.", pt="Oi! O total é {oito e cinquenta|nove e cinquenta|seis e cinquenta}."),
  dict(who="You", en="Sorry, could you {repeat that?|say that again?|speak more slowly?}", pt="Desculpe, pode {repetir?|dizer de novo?|falar mais devagar?}"),
  dict(who="Mei", en="Sure. {Eight. Fifty.|Nine. Fifty.|Six. Fifty.}", pt="Claro. {Oito. Cinquenta.|Nove. Cinquenta.|Seis. Cinquenta.}"),
  dict(who="You", en="Okay, I {got it.|understand.|hear you.} Thank you.", pt="Ok, {entendi.|entendo.|estou ouvindo.} Obrigado."),
 ],
 dlg=[
  dict(who="Mei", en="Hi! The total is {eight fifty.|nine fifty.}", pt="Oi! O total é {oito e cinquenta.|nove e cinquenta.}"),
  dict(who="You", en="Sorry, could you {repeat|say} that?", pt="Desculpe, pode {repetir|dizer} isso?"),
  dict(who="Mei", en="{Eight|Nine} dollars and fifty cents.", pt="{Oito|Nove} dólares e cinquenta centavos."),
  dict(who="You", en="Could you speak more {slowly?|clearly?}", pt="Pode falar mais {devagar?|claramente?}"),
  dict(who="Mei", en="Sure. {Eight.|Nine.} Fifty.", pt="Claro. {Oito.|Nove.} Cinquenta."),
  dict(who="You", en="Okay, I {got it.|understand.} Thank you.", pt="Ok, {entendi.|entendo.} Obrigado."),
  dict(who="Mei", en="Do you want a {receipt?|bag?}", pt="Quer o {recibo?|saco?}"),
  dict(who="You", en="Sorry, what does \"{receipt|total}\" mean?", pt="Desculpe, o que significa \"{receipt|total}\"?"),
  dict(who="Mei", en="It's the paper with the {price.|total.}", pt="É o papel com o {preço.|total.}"),
 ],
 vocab=[
  dict(w="understand", pt="entender", e="💡", ex=["I understand the price.", "Do you understand this word?"]),
  dict(w="again", pt="de novo", e="🔄", ex=["Say it again, please.", "I read the menu again."]),
  dict(w="pardon", pt="como? (pedir de novo)", e="🙋", ex=["Pardon? I didn't hear.", "Pardon me, what is the total?"]),
  dict(w="hear", pt="ouvir", e="👂", ex=["I can't hear you.", "Can you hear the music?"]),
  dict(w="sound", pt="som; soar", e="🔊", ex=["I like the sound of the music.", "That sounds good."]),
  dict(w="accent", pt="sotaque", e="🗣️", ex=["I have a Brazilian accent.", "I like your accent."]),
 ],
 molds=[
  dict(title="Pedir para repetir", frame="Sorry, could you {ask} that?", slots=[dict(key="ask", opts=["repeat", "say", "spell"])], model="Sorry, could you repeat that?", note="Could you... é educado. Repeat = repetir; say that again = dizer de novo."),
  dict(title="Pedir ritmo", frame="Could you speak more {how}, please?", slots=[dict(key="how", opts=["slowly", "clearly", "quietly"])], model="Could you speak more slowly, please?", note="Depois de more, use o advérbio: slowly, não slow."),
  dict(title="Escrever uma dúvida", frame="Sorry, I don't {verb} the word \"{word}\". What does it mean?", slots=[dict(key="verb", opts=["understand", "know", "remember"]), dict(key="word", opts=["receipt", "total", "change"])], model="Sorry, I don't understand the word \"receipt\". What does it mean?", note="Don't + verbo. What does it mean? pergunta o significado."),
 ],
 sounds=[
  dict(say="Could you repeat that?", tag="ligação: repeat that", tip="Una repeat e that: 'ripíttat'. Acentue PEAT; 'could you' soa 'cudjú'."),
  dict(say="Could you speak more slowly?", tag="ritmo: SPEAK more SLOWly", tip="Acentue SPEAK e SLOW; 'more' fica curto e fraco."),
  dict(say="Okay, I got it.", tag="ligação: got it", tip="O t entre vogais soa quase como d: 'gárit'. Una got e it."),
 ],
 role=dict(turns=[
  dict(npc="Hi! The total is eight fifty.", opts=[
   dict(en="Sorry, could you repeat that?", pt="Desculpe, pode repetir?", reply="Eight dollars and fifty cents."),
   dict(en="Sorry, I didn't catch that.", pt="Desculpe, não entendi.", reply="Eight dollars and fifty cents."),
   dict(en="Sorry, could you say that again?", pt="Desculpe, pode dizer de novo?", reply="Eight dollars and fifty cents.")]),
  dict(npc="Eight dollars and fifty cents.", opts=[
   dict(en="Could you speak more slowly?", pt="Pode falar mais devagar?", reply="Sure. Eight. Fifty."),
   dict(en="Could you slow down, please?", pt="Pode ir mais devagar, por favor?", reply="Sure. Eight. Fifty."),
   dict(en="Sorry, one more time, slowly?", pt="Desculpe, mais uma vez, devagar?", reply="Sure. Eight. Fifty.")]),
  dict(npc="Sure. Eight. Fifty.", opts=[
   dict(en="Okay, I got it. Thank you.", pt="Ok, entendi. Obrigado.", reply="Do you want a receipt?"),
   dict(en="Eight fifty. Thanks!", pt="Oito e cinquenta. Valeu!", reply="Do you want a receipt?"),
   dict(en="Great, now I understand.", pt="Ótimo, agora entendi.", reply="Do you want a receipt?")]),
  dict(npc="Do you want a receipt?", opts=[
   dict(en="Sorry, what does \"receipt\" mean?", pt="Desculpe, o que significa \"receipt\"?", reply="It's the paper with the price."),
   dict(en="Sorry, what is a receipt?", pt="Desculpe, o que é um receipt?", reply="It's the paper with the price."),
   dict(en="I don't know this word.", pt="Não conheço essa palavra.", reply="It's the paper with the price.")]),
 ], change=["Mei fala muito rápido: peça duas vezes para ela falar mais devagar.", "O café está barulhento e você não ouve: diga isso e peça para repetir.", "Você entendeu o preço errado: confirme dizendo o número que você ouviu."]),
 writing=dict(task="Você não entendeu o caixa do café. Escreva 2 ou 3 frases: peça para repetir, peça para falar devagar e agradeça.", model="Sorry, could you repeat that? Could you speak more slowly, please? Thank you!", kw=["repeat", "slowly", "sorry", "thank"], checks=["Pediu para repetir.", "Pediu para falar devagar.", "Agradeceu com educação."]),
 scenes=dict(pool=["cafe", "cafe2", "cafe3", "counter", "shop"], npc=dict(g="f", role="cashier"), you=dict(g="m")),
 convo=dict(npc=dict(name="Mei"), story="Você está em um café em Seattle. A Mei é a caixa e fala rápido.", turns=[
  dict(npc="Hi! The total is eight fifty.", pt="Oi! O total é oito e cinquenta.", opts=[
   dict(en="Sorry, could you repeat that?", pt="Desculpe, pode repetir?", ok=True, fb="Pedido educado para ouvir de novo."),
   dict(en="Here you go.", pt="Aqui está.", ok=False, fb="Você ainda não entendeu o preço."),
   dict(en="Do you want a receipt?", pt="Quer o recibo?", ok=False, fb="Quem pergunta isso é a caixa.")]),
  dict(npc="Eight dollars and fifty cents.", pt="Oito dólares e cinquenta centavos.", opts=[
   dict(en="It's the paper with the price.", pt="É o papel com o preço.", ok=False, fb="Ainda ninguém falou de recibo."),
   dict(en="Could you speak more slowly?", pt="Pode falar mais devagar?", ok=True, fb="Boa pergunta se ela fala rápido."),
   dict(en="Eight dollars, yes.", pt="Oito dólares, sim.", ok=False, fb="Não pede ajuda; soa estranho.")]),
  dict(npc="Sure. Eight. Fifty.", pt="Claro. Oito. Cinquenta.", opts=[
   dict(en="Sure. Eight. Fifty.", pt="Claro. Oito. Cinquenta.", ok=False, fb="Você repetiria a fala dela."),
   dict(en="Could you speak more slowly?", pt="Pode falar mais devagar?", ok=False, fb="Ela já falou devagar."),
   dict(en="Okay, I got it. Thank you.", pt="Ok, entendi. Obrigado.", ok=True, fb="Mostra que agora você entendeu.")]),
  dict(npc="Do you want a receipt?", pt="Quer o recibo?", opts=[
   dict(en="Sorry, what does \"receipt\" mean?", pt="Desculpe, o que significa \"receipt\"?", ok=True, fb="Pergunta natural sobre uma palavra nova."),
   dict(en="The total is eight fifty.", pt="O total é oito e cinquenta.", ok=False, fb="Ela já disse o total."),
   dict(en="Sorry, could you repeat that?", pt="Desculpe, pode repetir?", ok=False, fb="Possível, mas aqui a dúvida é a palavra.")]),
  dict(npc="It's the paper with the price.", pt="É o papel com o preço.", opts=[
   dict(en="Sorry, what does it mean?", pt="Desculpe, o que significa?", ok=False, fb="Ela acabou de explicar."),
   dict(en="Eight dollars and fifty cents.", pt="Oito dólares e cinquenta centavos.", ok=False, fb="Essa é a fala dela."),
   dict(en="Yes, please. Thank you!", pt="Sim, por favor. Obrigado!", ok=True, fb="Resposta natural e educada.")]),
 ]),
)
