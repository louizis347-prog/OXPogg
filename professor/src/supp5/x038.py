X = dict(
 key=dict(big="The check, please", label="Pedir a conta", sub="Nos EUA, check é a conta do restaurante (bill também se usa). Em geral se pede à mesa e se paga ao garçom ou no caixa."),
 mini=[
  dict(who="Leila", en="Excuse me. The {check|bill}, please.", pt="Com licença. A {conta|nota}, por favor."),
  dict(who="You", en="Sure. {Together or separate?|One check or separate checks?|Do you want it together or separate?}", pt="Claro. {Junto ou separado?|Uma conta ou contas separadas?|Quer junto ou separado?}"),
  dict(who="Leila", en="{Together|Separate|All together}, please.", pt="{Junto|Separado|Tudo junto}, por favor."),
  dict(who="You", en="Here you go. It's {forty|thirty|fifty} dollars.", pt="Aqui está. São {quarenta|trinta|cinquenta} dólares."),
 ],
 dlg=[
  dict(who="Leila", en="Excuse me. The {check|bill}, please.", pt="Com licença. A {conta|nota}, por favor."),
  dict(who="You", en="Sure. {Together or separate?|One check or separate?}", pt="Claro. {Junto ou separado?|Uma conta ou separadas?}"),
  dict(who="Leila", en="{Together|All together}, please.", pt="{Junto|Tudo junto}, por favor."),
  dict(who="You", en="Here you go. It's {forty|fifty} dollars.", pt="Aqui está. São {quarenta|cinquenta} dólares."),
  dict(who="Leila", en="Can I pay by {card|cash}?", pt="Posso pagar com {cartão|dinheiro}?"),
  dict(who="You", en="Yes, {of course.|sure.}", pt="Sim, {claro.|com certeza.}"),
  dict(who="Leila", en="Here's my {card|cash}.", pt="Aqui está meu {cartão|dinheiro}."),
  dict(who="You", en="Thank you. Have a {nice|great} day!", pt="Obrigado. Tenha um {bom|ótimo} dia!"),
  dict(who="Leila", en="Thank you, come again!", pt="Obrigada, volte sempre!"),
 ],
 vocab=[
  dict(w="check", pt="conta (restaurante)", e="🧾", ex=["The check, please.", "Here is your check."]),
  dict(w="card", pt="cartão", e="💳", ex=["Can I pay by card?", "Here's my card."]),
  dict(w="cash", pt="dinheiro (em espécie)", e="💵", ex=["Do you take cash?", "I'll pay in cash."]),
  dict(w="pay", pt="pagar", e="💰", ex=["Can I pay here?", "We pay at the end of the meal."]),
  dict(w="together", pt="junto", e="🤝", ex=["Together, please.", "We want to pay together."]),
  dict(w="separate", pt="separado", e="✂️", ex=["Separate checks, please.", "Can we pay separate?"]),
 ],
 molds=[
  dict(title="Pedir a conta", frame="Excuse me. {request}, please.", slots=[dict(key="request", opts=["The check", "The bill", "Separate checks"])], model="Excuse me. The check, please.", note="Excuse me chama o garçom com educação. Separate checks = contas separadas."),
  dict(title="Perguntar como pagar", frame="Can I pay {how}?", slots=[dict(key="how", opts=["by card", "in cash", "here", "with my phone"])], model="Can I pay by card?", note="Pay by card = pagar com cartão; in cash = em dinheiro."),
  dict(title="Escrever o fechamento", frame="Hi! {split}, please. I'll pay {how}.", slots=[dict(key="split", opts=["Together", "Separate checks", "One check"]), dict(key="how", opts=["by card", "in cash", "with my phone"])], model="Hi! Together, please. I'll pay by card.", note="Diga como quer dividir a conta e como vai pagar."),
 ],
 sounds=[
  dict(say="The check, please.", tag="acento: check e please", tip="Acentue check e please. The fica curto: 'the-CHECK-PLEEZ'."),
  dict(say="Can I pay by card?", tag="ligação: can I", tip="Can I soa 'kenai'. Una Can I e pay: 'kenai-PAY'."),
  dict(say="Together or separate?", tag="ritmo: or", tip="Or fica fraco: 'togetherer separate'. Acentue to-GE-ther e SE-pa-rate."),
 ],
 role=dict(turns=[
  dict(npc="Excuse me. The check, please.", opts=[
   dict(en="Sure. Together or separate?", pt="Claro. Junto ou separado?", reply="Together, please."),
   dict(en="Of course. One check or separate?", pt="Claro. Uma conta ou separadas?", reply="One check, please."),
   dict(en="Sure thing. Together or separate?", pt="Pode deixar. Junto ou separado?", reply="Together is fine.")]),
  dict(npc="Together, please.", opts=[
   dict(en="Here you go. It's forty dollars.", pt="Aqui está. São quarenta dólares.", reply="Thanks. Can I pay by card?"),
   dict(en="Here's the check. It's forty dollars.", pt="Aqui está a conta. São quarenta dólares.", reply="Okay. Do you take cards?"),
   dict(en="Sure. That's forty dollars.", pt="Claro. São quarenta dólares.", reply="Great. Can I pay by card?")]),
  dict(npc="Can I pay by card?", opts=[
   dict(en="Yes, of course.", pt="Sim, claro.", reply="Here's my card."),
   dict(en="Yes, sure. Card is fine.", pt="Sim, com certeza. Cartão pode.", reply="Perfect. Here's my card."),
   dict(en="Of course. Cash or card.", pt="Claro. Dinheiro ou cartão.", reply="Card, please. Here it is.")]),
  dict(npc="Here's my card.", opts=[
   dict(en="Thank you. Have a nice day!", pt="Obrigado. Tenha um bom dia!", reply="Thank you, come again!"),
   dict(en="Thanks! Have a great day!", pt="Valeu! Tenha um ótimo dia!", reply="You too. Come again!"),
   dict(en="Thank you. Come again soon!", pt="Obrigado. Volte logo!", reply="Thanks. See you!")]),
 ], change=["O cartão não passa: peça outra forma de pagamento.", "São quatro amigos e cada um quer pagar o seu: use separate.", "A conta veio errada: avise com educação."]),
 writing=dict(task="Você terminou o jantar. Escreva 2 ou 3 frases: peça a conta, diga se é junto ou separado e pergunte se pode pagar com cartão.", model="Excuse me. The check, please. Together, please. Can I pay by card?", kw=["check", "together", "pay", "card"], checks=["Pediu a conta (check).", "Disse junto ou separado.", "Perguntou como pagar."]),
 scenes=dict(pool=["diner", "restaurant", "counter", "cafe"], npc=dict(g="f", role="customer"), you=dict(g="m")),
 convo=dict(npc=dict(name="Leila"), story="Você é garçom num restaurante. Uma cliente pede a conta e quer pagar.", turns=[
  dict(npc="Excuse me. The check, please.", pt="Com licença. A conta, por favor.", opts=[
   dict(en="Sure. Together or separate?", pt="Claro. Junto ou separado?", ok=True, fb="Aceita e pergunta como dividir."),
   dict(en="Yes, I'm the check.", pt="Sim, eu sou a conta.", ok=False, fb="Frase sem sentido."),
   dict(en="Enjoy your meal!", pt="Bom apetite!", ok=False, fb="A refeição já acabou.")]),
  dict(npc="Together, please.", pt="Junto, por favor.", opts=[
   dict(en="Here you go. It's forty dollars.", pt="Aqui está. São quarenta dólares.", ok=True, fb="Entrega a conta e diz o total."),
   dict(en="Together or separate?", pt="Junto ou separado?", ok=False, fb="Ela acabou de responder."),
   dict(en="Can I pay by card?", pt="Posso pagar com cartão?", ok=False, fb="Esta pergunta é da cliente.")]),
  dict(npc="Can I pay by card?", pt="Posso pagar com cartão?", opts=[
   dict(en="Yes, you can. Thank you.", pt="Sim, pode. Obrigado.", ok=False, fb="Soa estranho: quem agradece é a cliente, e falta uma resposta clara como Yes, of course."),
   dict(en="Yes, of course.", pt="Sim, claro.", ok=True, fb="Confirma de forma amigável."),
   dict(en="Here's my card.", pt="Aqui está meu cartão.", ok=False, fb="Isso é a cliente quem diz.")]),
  dict(npc="Here's my card.", pt="Aqui está meu cartão.", opts=[
   dict(en="Excuse me. The check, please.", pt="Com licença. A conta, por favor.", ok=False, fb="A conta já foi entregue."),
   dict(en="Thank you. Have a nice day!", pt="Obrigado. Tenha um bom dia!", ok=True, fb="Agradece e se despede."),
   dict(en="Together, please.", pt="Junto, por favor.", ok=False, fb="Isso já foi decidido.")]),
  dict(npc="Thank you, come again!", pt="Obrigada, volte sempre!", opts=[
   dict(en="Sure. Together or separate?", pt="Claro. Junto ou separado?", ok=False, fb="A conta já foi paga."),
   dict(en="Thanks! See you soon.", pt="Valeu! Até logo.", ok=True, fb="Despedida simpática."),
   dict(en="It's forty dollars.", pt="São quarenta dólares.", ok=False, fb="O pagamento já foi feito.")]),
 ]),
)
