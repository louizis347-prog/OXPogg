X = dict(
 key=dict(big="How much is the rent?", label="Alugar um quarto", sub="Ao falar sobre um quarto, pergunte o aluguel, se as contas estão incluídas e marque um horário."),
 mini=[
  dict(who="Ava", en="Hi! I'm calling about the {room|apartment|house} for rent.", pt="Oi! Estou ligando sobre {o quarto|o apartamento|a casa} para alugar."),
  dict(who="You", en="Yes, it's still {available|open|free}.", pt="Sim, ainda está {disponível|aberto|livre}."),
  dict(who="Ava", en="How much is the {rent|deposit|room}?", pt="Quanto é {o aluguel|o depósito|o quarto}?"),
  dict(who="You", en="It's eight hundred dollars a {month|week|day}.", pt="São oitocentos dólares por {mês|semana|dia}."),
 ],
 dlg=[
  dict(who="Ava", en="Hi! I'm calling about the {room|flat} for rent.", pt="Oi! Estou ligando sobre {o quarto|o apartamento} para alugar."),
  dict(who="You", en="Yes, it's still {available.|free.}", pt="Sim, ainda está {disponível.|livre.}"),
  dict(who="Ava", en="How much is the {rent?|deposit?}", pt="Quanto é {o aluguel?|o depósito?}"),
  dict(who="You", en="It's {eight hundred|nine hundred|seven hundred} dollars a month.", pt="São {oitocentos|novecentos|setecentos} dólares por mês."),
  dict(who="Ava", en="Are {bills|utilities} included?", pt="{As contas|As taxas} estão incluídas?"),
  dict(who="You", en="Yes, water and {Wi-Fi,|internet,} but not {electricity.|gas.}", pt="Sim, água e {Wi-Fi,|internet,} mas não {a luz.|o gás.}"),
  dict(who="Ava", en="When can I {see it?|visit?}", pt="Quando posso {ver?|visitar?}"),
  dict(who="You", en="Tomorrow at {five?|six?|four?}", pt="Amanhã às {cinco?|seis?|quatro?}"),
  dict(who="Ava", en="Great. See you tomorrow at {five!|six!}", pt="Ótimo. Até amanhã às {cinco!|seis!}"),
 ],
 vocab=[
  dict(w="lease", pt="contrato de aluguel", e="📝", ex=["I sign the lease today.", "The lease is for one year."]),
  dict(w="bills", pt="contas", e="🧾", ex=["Are bills included?", "The bills are high."]),
  dict(w="electricity", pt="eletricidade (luz)", e="💡", ex=["Electricity is not included.", "I pay for electricity."]),
  dict(w="roommate", pt="colega de quarto", e="🧑‍🤝‍🧑", ex=["My roommate is friendly.", "I want a quiet roommate."]),
  dict(w="deposit", pt="caução, depósito", e="🏦", ex=["The deposit is one month.", "I pay a deposit."]),
  dict(w="available", pt="disponível", e="✅", ex=["Is the room available?", "It is available now."]),
 ],
 molds=[
  dict(title="Dizer o preço", frame="It's {price} dollars a month.", slots=[dict(key="price", opts=["eight hundred", "nine hundred", "seven hundred"])], model="It's eight hundred dollars a month.", note="Hundred não leva -s: eight hundred. A month = por mês."),
  dict(title="Perguntar o que está incluído", frame="Are {thing} included?", slots=[dict(key="thing", opts=["bills", "utilities", "the bills and Wi-Fi"])], model="Are bills included?", note="Are... included? pergunta o que já está no preço."),
  dict(title="Marcar a visita", frame="Can I see it {when} at {time}?", slots=[dict(key="when", opts=["tomorrow", "today", "on Friday"]), dict(key="time", opts=["five", "six", "four"])], model="Can I see it tomorrow at five?", note="Tomorrow e today não levam 'on'. Com dia da semana, use on."),
 ],
 sounds=[
  dict(say="Eight hundred dollars.", tag="números: eight HUNdred", tip="Acentue EIGHT e HUN. Em hundred, o d final é bem leve."),
  dict(say="Are bills included?", tag="ligação: are bills", tip="Are bills soa 'arbilz'. Una e acentue INCLUDED na segunda sílaba."),
  dict(say="See you tomorrow at five!", tag="ritmo: SEE you toMORrow at FIVE", tip="Acentue SEE, MOR e FIVE; you e at ficam fracos."),
 ],
 role=dict(turns=[
  dict(npc="Hi! I'm calling about the room for rent.", opts=[
   dict(en="Yes, it's still available.", pt="Sim, ainda está disponível.", reply="Great! How much is the rent?"),
   dict(en="Hi! Yes, the room is available.", pt="Oi! Sim, o quarto está disponível.", reply="Great! How much is the rent?"),
   dict(en="Yes, it is. Do you want to see it?", pt="Sim. Você quer ver?", reply="Yes, please. How much is the rent?")]),
  dict(npc="How much is the rent?", opts=[
   dict(en="It's eight hundred dollars a month.", pt="São oitocentos dólares por mês.", reply="Okay. Are bills included?"),
   dict(en="It's nine hundred dollars a month.", pt="São novecentos dólares por mês.", reply="Hmm, a little high. Are bills included?"),
   dict(en="It's seven hundred a month.", pt="São setecentos por mês.", reply="Nice! Are bills included?")]),
  dict(npc="Are bills included?", opts=[
   dict(en="Yes, water and Wi-Fi, but not electricity.", pt="Sim, água e Wi-Fi, mas não a luz.", reply="Okay. When can I see it?"),
   dict(en="Yes, all the bills are included.", pt="Sim, todas as contas estão incluídas.", reply="Great! When can I see it?"),
   dict(en="No, bills are not included.", pt="Não, as contas não estão incluídas.", reply="Okay. When can I see it?")]),
  dict(npc="When can I see it?", opts=[
   dict(en="Tomorrow at five?", pt="Amanhã às cinco?", reply="Great. See you tomorrow at five!"),
   dict(en="Today at six?", pt="Hoje às seis?", reply="Perfect. See you at six!"),
   dict(en="On Friday at four?", pt="Na sexta às quatro?", reply="Good. See you Friday at four!")]),
 ], change=["O quarto já foi alugado: peça desculpas e ofereça outro.", "Ava pergunta se pode trazer um amigo à visita: responda.", "Ava quer ver o quarto hoje: diga se pode e a que horas."]),
 writing=dict(task="Você tem um quarto para alugar. Escreva 2 ou 3 frases de anúncio: preço, o que está incluído e como ligar.", model="Room for rent. It's eight hundred dollars a month. Water and Wi-Fi are included. Call me at 555-0142.", kw=["room", "rent", "month", "included"], checks=["Disse o preço por mês.", "Disse o que está incluído.", "Deu um jeito de contato."]),
 scenes=dict(pool=["lobby", "living", "bedroom", "street", "hall"], npc=dict(g="f", role="customer"), you=dict(g="m")),
 convo=dict(npc=dict(name="Ava"), story="Você tem um quarto para alugar e a Ava liga.", turns=[
  dict(npc="Hi! I'm calling about the room for rent.", pt="Oi! Estou ligando sobre o quarto para alugar.", opts=[
   dict(en="See you tomorrow at five!", pt="Até amanhã às cinco!", ok=False, fb="É a despedida; a ligação acabou de começar."),
   dict(en="Yes, it's still available.", pt="Sim, ainda está disponível.", ok=True, fb="Confirma que o quarto está livre."),
   dict(en="How much is the rent?", pt="Quanto é o aluguel?", ok=False, fb="Quem pergunta isso é a Ava.")]),
  dict(npc="How much is the rent?", pt="Quanto é o aluguel?", opts=[
   dict(en="It's eight hundred dollars a month.", pt="São oitocentos dólares por mês.", ok=True, fb="Diz o preço por mês."),
   dict(en="Yes, it's still available.", pt="Sim, ainda está disponível.", ok=False, fb="Você já disse isso."),
   dict(en="Are bills included?", pt="As contas estão incluídas?", ok=False, fb="Essa pergunta é da Ava.")]),
  dict(npc="Are bills included?", pt="As contas estão incluídas?", opts=[
   dict(en="It's eight hundred dollars.", pt="São oitocentos dólares.", ok=False, fb="Você já disse o preço; ela pergunta das contas."),
   dict(en="When can I see it?", pt="Quando posso ver?", ok=False, fb="Essa pergunta é dela."),
   dict(en="Yes, water and Wi-Fi, but not electricity.", pt="Sim, água e Wi-Fi, mas não a luz.", ok=True, fb="Diz o que está e o que não está incluído.")]),
  dict(npc="When can I see it?", pt="Quando posso ver?", opts=[
   dict(en="Tomorrow at five?", pt="Amanhã às cinco?", ok=True, fb="Sugere um horário claro."),
   dict(en="Are bills included?", pt="As contas estão incluídas?", ok=False, fb="Ela já perguntou e você respondeu."),
   dict(en="I'm calling about the room.", pt="Estou ligando sobre o quarto.", ok=False, fb="É a fala dela.")]),
  dict(npc="Great. See you tomorrow at five!", pt="Ótimo. Até amanhã às cinco!", opts=[
   dict(en="See you! Bye!", pt="Até lá! Tchau!", ok=True, fb="Despedida curta."),
   dict(en="It's eight hundred dollars.", pt="São oitocentos dólares.", ok=False, fb="O preço já foi dito."),
   dict(en="Yes, it's still available.", pt="Sim, ainda está disponível.", ok=False, fb="Já respondeu isso no início.")]),
 ]),
)
