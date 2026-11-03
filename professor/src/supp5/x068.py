X = dict(
 key=dict(big="How does this machine work?", label="Usar a lavanderia do prédio", sub="Peça ajuda com Excuse me, pergunte o preço e o tempo, e confirme com Press start."),
 mini=[
  dict(who="Claire", en="Excuse me, how does this {machine|washer|dryer} work?", pt="Com licença, como funciona {esta máquina|esta lavadora|esta secadora}?"),
  dict(who="You", en="Put your {clothes|towels|socks} in and add soap.", pt="Coloque {as roupas|as toalhas|as meias} e adicione sabão."),
  dict(who="Claire", en="How much is it? I have {four|eight|six} quarters.", pt="Quanto custa? Tenho {quatro|oito|seis} moedas de vinte e cinco."),
  dict(who="You", en="It takes {forty|thirty|fifty} minutes.", pt="Demora {quarenta|trinta|cinquenta} minutos."),
 ],
 dlg=[
  dict(who="Claire", en="Excuse me, how does this {machine|washer} work?", pt="Com licença, como funciona {esta máquina|esta lavadora}?"),
  dict(who="You", en="Put your {clothes|towels} in and add soap.", pt="Coloque {as roupas|as toalhas} e adicione sabão."),
  dict(who="Claire", en="How much is it?", pt="Quanto custa?"),
  dict(who="You", en="{Two|Three} dollars. Do you have coins?", pt="{Dois|Três} dólares. Você tem moedas?"),
  dict(who="Claire", en="Yes, I have {four|eight} quarters.", pt="Tenho, {quatro|oito} moedas de vinte e cinco."),
  dict(who="You", en="Great. Press {start|the green button}.", pt="Ótimo. Aperte {iniciar|o botão verde}."),
  dict(who="Claire", en="How long does it take?", pt="Quanto tempo demora?"),
  dict(who="You", en="{Forty|Thirty|Fifty} minutes.", pt="{Quarenta|Trinta|Cinquenta} minutos."),
  dict(who="Claire", en="Thanks for the help. Bye!", pt="Valeu pela ajuda. Tchau!"),
 ],
 vocab=[
  dict(w="laundry", pt="roupa suja / lavanderia", e="🧺", ex=["I do laundry on Sunday.", "The laundry room is downstairs."]),
  dict(w="basket", pt="cesto", e="🧺", ex=["My basket is full.", "Put the socks in the basket."]),
  dict(w="towel", pt="toalha", e="🧖", ex=["I need a clean towel.", "The towel is wet."]),
  dict(w="sock", pt="meia", e="🧦", ex=["I lost a sock.", "This sock is blue."]),
  dict(w="quarter", pt="moeda de 25 centavos", e="🪙", ex=["A quarter is twenty-five cents.", "I have one quarter."]),
  dict(w="hanger", pt="cabide", e="🪝", ex=["Put the shirt on a hanger.", "I need a hanger."]),
 ],
 molds=[
  dict(title="Colocar na máquina", frame="Put your {things} in the {machine}.", slots=[dict(key="things", opts=["clothes", "towels", "socks", "shirts"]), dict(key="machine", opts=["washer", "dryer", "machine"])], model="Put your clothes in the washer.", note="Put... in = colocar dentro. Washer lava; dryer seca."),
  dict(title="Dizer o tempo", frame="It takes {n} minutes.", slots=[dict(key="n", opts=["forty", "thirty", "fifty", "twenty"])], model="It takes forty minutes.", note="It takes + tempo diz quanto demora."),
  dict(title="Escrever o pedido de ajuda", frame="Excuse me, how does this {machine} work? Do you have {thing}? I have {n} quarters.", slots=[dict(key="machine", opts=["machine", "washer", "dryer"]), dict(key="thing", opts=["coins", "soap", "quarters"]), dict(key="n", opts=["four", "six", "eight"])], model="Excuse me, how does this machine work? Do you have coins? I have four quarters.", note="Peça ajuda, pergunte o que precisa e diga o que você tem."),
 ],
 sounds=[
  dict(say="Put your clothes in.", tag="ligação: clothes in", tip="Clothes in soa 'clozin'. Una a última consoante com a vogal seguinte."),
  dict(say="How long does it take?", tag="ligação: does it", tip="Does it vira 'duzit'. Acentue LONG e TAKE."),
  dict(say="Press start.", tag="ligação: press start", tip="Press start soa 'pres-start' sem pausa entre as palavras."),
 ],
 role=dict(turns=[
  dict(npc="Hi! Is this your first time here?", opts=[
   dict(en="Yes. How does this machine work?", pt="Sim. Como funciona esta máquina?", reply="Put your clothes in and add soap."),
   dict(en="Yes. Excuse me, how does it work?", pt="Sim. Com licença, como funciona?", reply="Put your clothes in and add soap."),
   dict(en="Yes. Can you help me, please?", pt="Sim. Pode me ajudar, por favor?", reply="Sure! Put your clothes in and add soap.")]),
  dict(npc="Put your clothes in and add soap.", opts=[
   dict(en="Okay. How much is it?", pt="Certo. Quanto custa?", reply="Two dollars. Do you have coins?"),
   dict(en="Done. How much is the washer?", pt="Pronto. Quanto custa a lavadora?", reply="Two dollars. Do you have coins?"),
   dict(en="Thanks. Do I pay now?", pt="Valeu. Pago agora?", reply="Yes. It's two dollars. Do you have coins?")]),
  dict(npc="Do you have coins?", opts=[
   dict(en="Yes, I have four quarters.", pt="Tenho, quatro moedas de vinte e cinco.", reply="Great. Press start."),
   dict(en="Yes, I have eight quarters.", pt="Tenho, oito moedas de vinte e cinco.", reply="Perfect. Press start."),
   dict(en="No, I don't. Is there a change machine?", pt="Não tenho. Tem máquina de trocar dinheiro?", reply="Yes, it's by the door. Then press start.")]),
  dict(npc="Great. Press start.", opts=[
   dict(en="Done. How long does it take?", pt="Pronto. Quanto tempo demora?", reply="Forty minutes."),
   dict(en="Okay. How long does it take?", pt="Certo. Quanto tempo demora?", reply="Forty minutes."),
   dict(en="Done. Is forty minutes normal?", pt="Pronto. Quarenta minutos é normal?", reply="Yes, forty minutes is normal.")]),
 ], change=["A máquina não aceita as moedas: peça ajuda ao vizinho.", "Você não tem sabão: pergunte se pode pegar um pouco.", "A lavadora para antes do fim: pergunte o que fazer."]),
 writing=dict(task="Você está na lavanderia do prédio. Escreva 2 ou 3 frases: peça ajuda com a máquina, pergunte o preço e o tempo.", model="Excuse me, how does this machine work? How much is it? And how long does it take?", kw=["excuse", "machine", "much", "long"], checks=["Pediu ajuda com a máquina.", "Perguntou o preço.", "Perguntou o tempo."]),
 scenes=dict(pool=["lobby", "lobby1", "lobby2", "hall"], npc=dict(g="m", role="neighbor"), you=dict(g="f")),
 convo=dict(npc=dict(name="Dan"), story="Você está na lavanderia do prédio e um vizinho está lá.", turns=[
  dict(npc="Hi! Is this your first time here?", pt="Oi! É a sua primeira vez aqui?", opts=[
   dict(en="Yes. Excuse me, how does this machine work?", pt="Sim. Com licença, como funciona esta máquina?", ok=True, fb="Responde e pede ajuda."),
   dict(en="Forty minutes.", pt="Quarenta minutos.", ok=False, fb="Ninguém perguntou o tempo ainda."),
   dict(en="Press start.", pt="Aperte iniciar.", ok=False, fb="Quem explica é o vizinho.")]),
  dict(npc="Put your clothes in and add soap.", pt="Coloque as roupas e adicione sabão.", opts=[
   dict(en="Two dollars.", pt="Dois dólares.", ok=False, fb="Você não é quem vende; pergunte o preço."),
   dict(en="Okay. How much is it?", pt="Certo. Quanto custa?", ok=True, fb="Pergunta o preço."),
   dict(en="Do you have coins?", pt="Você tem moedas?", ok=False, fb="Quem pergunta isso é o vizinho.")]),
  dict(npc="Two dollars. Do you have coins?", pt="Dois dólares. Você tem moedas?", opts=[
   dict(en="Yes, I have four quarters.", pt="Tenho, quatro moedas de vinte e cinco.", ok=True, fb="Diz quais moedas você tem."),
   dict(en="Put your clothes in.", pt="Coloque suas roupas.", ok=False, fb="Essa instrução é dele."),
   dict(en="How much is it?", pt="Quanto custa?", ok=False, fb="O preço acabou de ser dito.")]),
  dict(npc="Great. Press start.", pt="Ótimo. Aperte iniciar.", opts=[
   dict(en="Forty minutes.", pt="Quarenta minutos.", ok=False, fb="Essa é a resposta, não a pergunta."),
   dict(en="Done. How long does it take?", pt="Pronto. Quanto tempo demora?", ok=True, fb="Pergunta o tempo."),
   dict(en="Add soap.", pt="Adicione sabão.", ok=False, fb="O vizinho já disse isso.")]),
  dict(npc="Forty minutes.", pt="Quarenta minutos.", opts=[
   dict(en="Thanks for the help. Bye!", pt="Valeu pela ajuda. Tchau!", ok=True, fb="Agradece e se despede."),
   dict(en="Excuse me, how does this work?", pt="Com licença, como funciona?", ok=False, fb="Você já perguntou isso."),
   dict(en="Do you have coins?", pt="Você tem moedas?", ok=False, fb="Você já respondeu isso.")]),
 ]),
)
