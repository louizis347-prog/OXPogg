X = dict(
 key=dict(big="Two tickets for the tour, please", label="Comprar ingressos", sub="Diga quantos ingressos, de que passeio, e para quem (adultos ou crianças). Pergunte por desconto e pelo horário."),
 mini=[
  dict(who="Mei", en="Hi! {Two|Three|One} tickets for the tour, please.", pt="Oi! {Dois|Três|Um} ingressos para o passeio, por favor."),
  dict(who="You", en="Adults or {children?|students?|seniors?}", pt="Adultos ou {crianças?|estudantes?|idosos?}"),
  dict(who="Mei", en="{Two adults.|Two students.|One adult.}", pt="{Dois adultos.|Dois estudantes.|Um adulto.}"),
  dict(who="You", en="That's {forty|twenty|thirty} dollars.", pt="São {quarenta|vinte|trinta} dólares."),
 ],
 dlg=[
  dict(who="Mei", en="Hi! {Two|Three} tickets for the tour, please.", pt="Oi! {Dois|Três} ingressos para o passeio, por favor."),
  dict(who="You", en="{Adults or children?|Adults or students?}", pt="{Adultos ou crianças?|Adultos ou estudantes?}"),
  dict(who="Mei", en="{Two adults.|Two students.}", pt="{Dois adultos.|Dois estudantes.}"),
  dict(who="You", en="That's {forty|thirty} dollars.", pt="São {quarenta|trinta} dólares."),
  dict(who="Mei", en="Is there a {student|child} discount?", pt="Tem desconto para {estudante?|criança?}"),
  dict(who="You", en="Yes, with a {student card.|school card.}", pt="Sim, com {carteirinha.|carteirinha da escola.}"),
  dict(who="Mei", en="Here you go. What time is the {tour?|show?}", pt="Aqui está. Que horas é o {passeio?|show?}"),
  dict(who="You", en="At {two|three|four} o'clock.", pt="Às {duas|três|quatro} horas."),
  dict(who="Mei", en="Enjoy the {tour!|show!}", pt="Aproveite o {passeio!|show!}"),
 ],
 vocab=[
  dict(w="tour", pt="passeio", e="🗺️", ex=["The tour is at two o'clock.", "We take a city tour."]),
  dict(w="adult", pt="adulto", e="🧑", ex=["One adult ticket, please.", "An adult ticket is twenty dollars."]),
  dict(w="child", pt="criança", e="🧒", ex=["One child ticket, please.", "The child is eight."]),
  dict(w="discount", pt="desconto", e="🏷️", ex=["Is there a discount?", "A student discount is ten percent."]),
  dict(w="price", pt="preço", e="💲", ex=["What is the price?", "The price is low."]),
  dict(w="entrance", pt="entrada", e="🚪", ex=["The entrance is on the left.", "The tour starts at the entrance."]),
 ],
 molds=[
  dict(title="Pedir os ingressos", frame="{num} tickets for the tour, please.", slots=[dict(key="num", opts=["Two", "Three", "Four"])], model="Two tickets for the tour, please.", note="Número + tickets (com -s) + for the tour. Please deixa o pedido educado."),
  dict(title="Perguntar por desconto", frame="Is there a {kind} discount?", slots=[dict(key="kind", opts=["student", "child", "group"])], model="Is there a student discount?", note="Is there a... discount? = Tem desconto para...? Student discount = desconto de estudante."),
  dict(title="Escrever o pedido", frame="Hi! {num} for the tour, please. Is there a {kind} discount?", slots=[dict(key="num", opts=["Two tickets", "Three tickets", "One ticket"]), dict(key="kind", opts=["student", "child", "group"])], model="Hi! Two tickets for the tour, please. Is there a student discount?", note="Peça os ingressos e pergunte pelo desconto na mesma mensagem."),
 ],
 sounds=[
  dict(say="Adults or children?", tag="ligação: adults or", tip="O s final liga com or: 'a-dultsor'. Acentue A-dults e CHIL-dren."),
  dict(say="Here you go.", tag="ligação: here you", tip="Here you vira 'hiêr-iu'. Una as palavras e acentue GO."),
  dict(say="At two o'clock.", tag="ligação: two o'clock", tip="Two o'clock soa 'tu-uclock'. Una as palavras e acentue TWO."),
 ],
 role=dict(turns=[
  dict(npc="Hi! Two tickets for the tour, please.", opts=[
   dict(en="Adults or children?", pt="Adultos ou crianças?", reply="Two adults."),
   dict(en="Sure. Adults or students?", pt="Claro. Adultos ou estudantes?", reply="Two students."),
   dict(en="Of course. For adults?", pt="Claro. Para adultos?", reply="Yes, two adults.")]),
  dict(npc="Two adults.", opts=[
   dict(en="That's forty dollars.", pt="São quarenta dólares.", reply="Is there a student discount?"),
   dict(en="That's thirty dollars.", pt="São trinta dólares.", reply="Is there a student discount?"),
   dict(en="It's twenty dollars each.", pt="São vinte dólares cada.", reply="Is there a student discount?")]),
  dict(npc="Is there a student discount?", opts=[
   dict(en="Yes, with a student card.", pt="Sim, com carteirinha.", reply="Here you go. What time is the tour?"),
   dict(en="Yes. Can I see your card?", pt="Sim. Posso ver sua carteirinha?", reply="Here you go. What time is the tour?"),
   dict(en="Yes, ten percent.", pt="Sim, dez por cento.", reply="Here you go. What time is the tour?")]),
  dict(npc="What time is the tour?", opts=[
   dict(en="At two o'clock.", pt="Às duas horas.", reply="Great. Thank you!"),
   dict(en="At three o'clock.", pt="Às três horas.", reply="Great. Thank you!"),
   dict(en="It's at four. Enjoy the tour!", pt="É às quatro. Aproveite o passeio!", reply="Thanks! See you at four.")]),
 ], change=["O cliente quer ingressos para uma criança: pergunte a idade.", "O cliente esquece a carteirinha: diga que sem ela o preço é normal.", "O passeio das duas está lotado: ofereça o das quatro."]),
 writing=dict(task="Você quer comprar ingressos para um passeio. Escreva 2 ou 3 frases: peça os ingressos, pergunte por desconto e pelo horário.", model="Hi! Two tickets for the tour, please. Is there a student discount? What time is the tour?", kw=["tickets", "tour", "discount", "time"], checks=["Pediu os ingressos.", "Perguntou por desconto.", "Perguntou o horário."]),
 scenes=dict(pool=["station", "counter", "subway", "street"], npc=dict(g="f", role="customer"), you=dict(g="m")),
 convo=dict(npc=dict(name="Mei"), story="Você vende ingressos de passeio em Seattle e atende a Mei.", turns=[
  dict(npc="Hi! Two tickets for the tour, please.", pt="Oi! Dois ingressos para o passeio, por favor.", opts=[
   dict(en="Enjoy the tour!", pt="Aproveite o passeio!", ok=False, fb="Isso se diz no fim, depois da compra."),
   dict(en="Adults or children?", pt="Adultos ou crianças?", ok=True, fb="Pergunta para quem são os ingressos."),
   dict(en="Is there a student discount?", pt="Tem desconto para estudante?", ok=False, fb="Quem pergunta isso é o cliente.")]),
  dict(npc="Two adults.", pt="Dois adultos.", opts=[
   dict(en="That's forty dollars.", pt="São quarenta dólares.", ok=True, fb="Diz o preço total."),
   dict(en="Hi! Two tickets for the tour, please.", pt="Oi! Dois ingressos para o passeio, por favor.", ok=False, fb="Essa fala é do cliente."),
   dict(en="Here you go.", pt="Aqui está.", ok=False, fb="Quem entrega o dinheiro é o cliente.")]),
  dict(npc="Is there a student discount?", pt="Tem desconto para estudante?", opts=[
   dict(en="At two o'clock.", pt="Às duas horas.", ok=False, fb="Ela pergunta por desconto, não por horário."),
   dict(en="Adults or children?", pt="Adultos ou crianças?", ok=False, fb="Já foi respondido."),
   dict(en="Yes, with a student card.", pt="Sim, com carteirinha.", ok=True, fb="Explica como obter o desconto.")]),
  dict(npc="Here you go. What time is the tour?", pt="Aqui está. Que horas é o passeio?", opts=[
   dict(en="At two o'clock.", pt="Às duas horas.", ok=True, fb="Responde a hora com at."),
   dict(en="That's forty dollars.", pt="São quarenta dólares.", ok=False, fb="Ela pergunta a hora, não o preço."),
   dict(en="Yes, with a student card.", pt="Sim, com carteirinha.", ok=False, fb="Isso já foi dito.")]),
  dict(npc="Enjoy the tour!", pt="Aproveite o passeio!", opts=[
   dict(en="Hi! Two tickets for the tour, please.", pt="Oi! Dois ingressos para o passeio, por favor.", ok=False, fb="Essa fala abre a compra."),
   dict(en="Is there a student discount?", pt="Tem desconto para estudante?", ok=False, fb="Já foi respondido."),
   dict(en="Thanks! Have a nice day!", pt="Obrigado! Tenha um bom dia!", ok=True, fb="Responde com simpatia.")]),
 ]),
)
