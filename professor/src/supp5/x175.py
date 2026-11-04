X = dict(
 key=dict(big="How does this work?", label="Usar o autoatendimento", sub="Peça ajuda com educação, escaneie cada item, coloque na sacola, pese frutas na tela e pague."),
 mini=[
  dict(who="You", en="Excuse me, how does this {work?|machine work?}", pt="Com licença, como {isso funciona?|essa máquina funciona?}"),
  dict(who="Rosa", en="{Scan|Touch|Put} each item, then pay.", pt="{Escaneie|Toque em|Coloque} cada item, depois pague."),
  dict(who="You", en="Where do I {scan?|pay?|touch?}", pt="Onde eu {escaneio?|pago?|toco?}"),
  dict(who="Rosa", en="Here, on the {red|green|blue} light.", pt="Aqui, na luz {vermelha.|verde.|azul.}"),
 ],
 dlg=[
  dict(who="Rosa", en="Excuse me, how does this {work?|machine work?}", pt="Com licença, como {isso funciona?|essa máquina funciona?}"),
  dict(who="You", en="{Scan|Touch} each item, then {pay.|bag.}", pt="{Escaneie|Toque em} cada item, depois {pague.|ensaque.}"),
  dict(who="Rosa", en="Where do I {scan?|pay?}", pt="Onde {escaneio?|pago?}"),
  dict(who="You", en="Here, on the {red|green} light.", pt="Aqui, na luz {vermelha.|verde.}"),
  dict(who="Rosa", en="It says \"unexpected {item\".|bag\".}", pt="Diz \"{item inesperado\".|sacola inesperada\".}"),
  dict(who="You", en="Put it in the {bag|cart} first.", pt="Ponha na {sacola|carrinho} primeiro."),
  dict(who="Rosa", en="Oh, I see. Now it {works.|scans.}", pt="Ah, entendi. Agora {funciona.|escaneia.}"),
  dict(who="You", en="How do I weigh the {apples?|lemons?}", pt="Como peso as {maçãs?|limões?}"),
  dict(who="Rosa", en="Choose \"produce\" on the {screen.|button.}", pt="Escolha \"hortifrúti\" na {tela.|botão.}"),
 ],
 vocab=[
  dict(w="scan", pt="escanear", e="📟", ex=["Scan the milk here.", "I scan each item."]),
  dict(w="item", pt="item, produto", e="📦", ex=["This item is two dollars.", "Scan every item."]),
  dict(w="list", pt="lista", e="📝", ex=["My list has milk.", "Read the list."]),
  dict(w="frozen", pt="congelado", e="🧊", ex=["I buy frozen pizza.", "The peas are frozen."]),
  dict(w="lemon", pt="limão", e="🍋", ex=["I buy three lemons.", "The lemon is yellow."]),
  dict(w="touch", pt="tocar", e="👆", ex=["Touch the screen.", "Touch here to pay."]),
 ],
 molds=[
  dict(title="Pedir ajuda", frame="Excuse me, how does this {thing} work?", slots=[dict(key="thing", opts=["machine", "screen", "scale"])], model="Excuse me, how does this machine work?", note="How does + this + coisa + work? Com this (singular), use does."),
  dict(title="Perguntar onde", frame="Where do I {action}?", slots=[dict(key="action", opts=["scan", "pay", "put the bag"])], model="Where do I scan?", note="Where do I + verbo? pergunta o lugar da ação."),
  dict(title="Escrever o pedido de ajuda", frame="Hi! How do I {action} the {thing}? It says \"{message}\".", slots=[dict(key="action", opts=["weigh", "scan", "pay for"]), dict(key="thing", opts=["lemons", "apples", "bread"]), dict(key="message", opts=["unexpected item", "wait", "help is coming"])], model="Hi! How do I weigh the lemons? It says \"unexpected item\".", note="How do I + verbo + item? Depois diga o que a tela mostra."),
 ],
 sounds=[
  dict(say="Scan each item.", tag="ligação: scan each", tip="Una scan e each: 'skan-iich'. O n liga na vogal seguinte."),
  dict(say="Put it in the bag first.", tag="ligação: put it in", tip="Soa 'pudidin'. O t entre vogais fica rápido, quase d."),
  dict(say="How do I weigh the apples?", tag="ritmo: HOW do I WEIGH the APples", tip="Acentue HOW, WEIGH e AP; 'do I' e 'the' ficam fracos."),
 ],
 role=dict(turns=[
  dict(npc="Hi! Can I help you?", opts=[
   dict(en="Excuse me, how does this work?", pt="Com licença, como isso funciona?", reply="Scan each item, then pay."),
   dict(en="Hi! How does this machine work?", pt="Oi! Como essa máquina funciona?", reply="Scan each item, then pay."),
   dict(en="Excuse me, I need help.", pt="Com licença, preciso de ajuda.", reply="Sure. Scan each item, then pay.")]),
  dict(npc="Scan each item, then pay.", opts=[
   dict(en="Where do I scan?", pt="Onde escaneio?", reply="Here, on the red light."),
   dict(en="Where is the red light?", pt="Onde fica a luz vermelha?", reply="Here, on the red light."),
   dict(en="Where do I put the item?", pt="Onde coloco o item?", reply="Here, on the red light.")]),
  dict(npc="Here, on the red light.", opts=[
   dict(en="It says \"unexpected item\".", pt="Diz \"item inesperado\".", reply="Put it in the bag first."),
   dict(en="It does not work.", pt="Não funciona.", reply="Put it in the bag first."),
   dict(en="The screen says \"wait\".", pt="A tela diz \"espere\".", reply="Put the item in the bag first.")]),
  dict(npc="Put it in the bag first.", opts=[
   dict(en="Oh, I see. Now it works.", pt="Ah, entendi. Agora funciona.", reply="Great! Anything else?"),
   dict(en="Thanks! How do I weigh the apples?", pt="Obrigado! Como peso as maçãs?", reply="Choose \"produce\" on the screen."),
   dict(en="Okay. How do I weigh the lemons?", pt="Certo. Como peso os limões?", reply="Choose \"produce\" on the screen.")]),
 ], change=["A máquina não aceita seu cartão: peça ajuda.", "Sua sacola ficou pesada demais: peça outra sacola.", "Você não acha o código do item: pergunte como escanear."]),
 writing=dict(task="Escreva 2 ou 3 frases pedindo ajuda no autoatendimento: pergunte como funciona e como pesar uma fruta.", model="Excuse me, how does this work? Where do I scan? How do I weigh the apples?", kw=["how", "scan", "weigh", "apples"], checks=["Perguntou como funciona.", "Perguntou onde escanear.", "Perguntou como pesar."]),
 scenes=dict(pool=["supermarket", "market", "counter", "shop"], npc=dict(g="f", role="clerk"), you=dict(g="m")),
 convo=dict(npc=dict(name="Rosa"), story="Você está em um supermercado em Houston e não sabe usar o autoatendimento. A Rosa trabalha ali.", turns=[
  dict(npc="Hi! Can I help you?", pt="Oi! Posso ajudar?", opts=[
   dict(en="Scan each item, then pay.", pt="Escaneie cada item, depois pague.", ok=False, fb="Essa instrução é dela."),
   dict(en="Excuse me, how does this work?", pt="Com licença, como isso funciona?", ok=True, fb="Pedido educado de ajuda."),
   dict(en="Put it in the bag first.", pt="Ponha na sacola primeiro.", ok=False, fb="Essa instrução é dela.")]),
  dict(npc="Scan each item, then pay.", pt="Escaneie cada item, depois pague.", opts=[
   dict(en="Where do I scan?", pt="Onde escaneio?", ok=True, fb="Pergunta o lugar."),
   dict(en="Here, on the red light.", pt="Aqui, na luz vermelha.", ok=False, fb="Essa resposta é dela."),
   dict(en="Now it works.", pt="Agora funciona.", ok=False, fb="Cedo demais: você ainda não escaneou.")]),
  dict(npc="Here, on the red light.", pt="Aqui, na luz vermelha.", opts=[
   dict(en="Choose \"produce\" on the screen.", pt="Escolha \"hortifrúti\" na tela.", ok=False, fb="Essa instrução vem depois e é dela."),
   dict(en="Where do I scan?", pt="Onde escaneio?", ok=False, fb="Ela acabou de responder."),
   dict(en="It says \"unexpected item\".", pt="Diz \"item inesperado\".", ok=True, fb="Conta o problema.")]),
  dict(npc="Put it in the bag first.", pt="Ponha na sacola primeiro.", opts=[
   dict(en="Scan each item, then pay.", pt="Escaneie cada item, depois pague.", ok=False, fb="Ela já disse isso."),
   dict(en="Oh, I see. Now it works.", pt="Ah, entendi. Agora funciona.", ok=True, fb="Mostra que entendeu."),
   dict(en="Where do I scan?", pt="Onde escaneio?", ok=False, fb="Já foi respondido.")]),
  dict(npc="Great! Anything else?", pt="Ótimo! Mais alguma coisa?", opts=[
   dict(en="Choose \"produce\" on the screen.", pt="Escolha \"hortifrúti\" na tela.", ok=False, fb="Quem explica é ela."),
   dict(en="Put it in the bag first.", pt="Ponha na sacola primeiro.", ok=False, fb="Essa instrução é dela."),
   dict(en="How do I weigh the apples?", pt="Como peso as maçãs?", ok=True, fb="Próxima dúvida natural.")]),
 ]),
)
