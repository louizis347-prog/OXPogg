X = dict(
 key=dict(big="What should I wear?", label="Convite de casamento", sub="Você confirma que recebeu o convite, diz que vai, pergunta quando e onde é e o que vestir."),
 mini=[
  dict(who="Cole", en="Did you get the {invitation|card|message}?", pt="Você recebeu o {convite|cartão|recado}?"),
  dict(who="You", en="Yes! I'm so {happy|glad|excited} for you.", pt="Sim! Estou tão {feliz|contente|empolgado} por você."),
  dict(who="Cole", en="The wedding is June tenth, at {four|three|five} o'clock.", pt="O casamento é dez de junho, às {quatro|três|cinco} horas."),
  dict(who="You", en="Where is it? In a {garden|church|hotel}?", pt="Onde é? Em {um jardim|uma igreja|um hotel}?"),
 ],
 dlg=[
  dict(who="Cole", en="Did you get the {invitation?|card?}", pt="Você recebeu o {convite?|cartão?}"),
  dict(who="You", en="Yes! I'm so {happy|glad} for you.", pt="Sim! Estou tão {feliz|contente} por você."),
  dict(who="Cole", en="Can you come to the {wedding?|party?}", pt="Você pode ir {ao casamento?|à festa?}"),
  dict(who="You", en="Of course. {When|What time} is it?", pt="Claro. {Quando|A que horas} é?"),
  dict(who="Cole", en="{June tenth|June fifth}, at {four|five} o'clock.", pt="{Dez|Cinco} de junho, às {quatro|cinco} horas."),
  dict(who="You", en="{Where is it?|Is it far?}", pt="{Onde é?|É longe?}"),
  dict(who="Cole", en="In a {garden|park} near the lake.", pt="Em {um jardim|um parque} perto do lago."),
  dict(who="You", en="What should I {wear?|bring?}", pt="O que devo {vestir?|levar?}"),
  dict(who="Cole", en="A dress or a suit. {Nothing white.|No jeans.}", pt="Vestido ou terno. {Nada branco.|Sem jeans.}"),
 ],
 vocab=[
  dict(w="wedding", pt="casamento", e="💒", ex=["The wedding is in June.", "I go to a wedding."]),
  dict(w="ring", pt="aliança / anel", e="💍", ex=["The ring is gold.", "He has the ring."]),
  dict(w="flower", pt="flor", e="🌸", ex=["This flower is pink.", "She has a flower in her hair."]),
  dict(w="garden", pt="jardim", e="🌳", ex=["The garden is big.", "We sit in the garden."]),
  dict(w="bride", pt="noiva", e="👰", ex=["The bride is happy.", "The bride wears white."]),
  dict(w="groom", pt="noivo", e="🤵", ex=["The groom is nervous.", "The groom wears a suit."]),
 ],
 molds=[
  dict(title="Dizer data e hora", frame="The wedding is {date}, at {time} o'clock.", slots=[dict(key="date", opts=["June tenth", "July fifth", "May second"]), dict(key="time", opts=["four", "three", "five"])], model="The wedding is June tenth, at four o'clock.", note="Datas em inglês: June tenth (ordinal). At + hora + o'clock."),
  dict(title="Perguntar o que fazer", frame="What should I {verb}?", slots=[dict(key="verb", opts=["wear", "bring", "say", "do"])], model="What should I wear?", note="What should I...? pede um conselho. Should vem antes de I."),
  dict(title="Responder ao convite", frame="Thank you for the invitation! I can come to the wedding on {date}. I want to bring {thing}.", slots=[dict(key="date", opts=["June tenth", "July fifth", "May second"]), dict(key="thing", opts=["flowers", "a card", "a gift"])], model="Thank you for the invitation! I can come to the wedding on June tenth. I want to bring flowers.", note="On + data. I want to bring... diz o que você quer levar."),
 ],
 sounds=[
  dict(say="Can you come to the wedding?", tag="redução: can you", tip="Can fica fraco: 'kn-ya'. Acentue COME e WED."),
  dict(say="Yes, I can come.", tag="redução: can", tip="Can fraco soa 'kən'. Acentue COME, não can."),
  dict(say="Sorry, I can't come.", tag="contraste: can't", tip="Can't é forte e longo: 'kænt'. Acentue CAN'T e COME."),
 ],
 role=dict(turns=[
  dict(npc="Did you get the invitation?", opts=[
   dict(en="Yes! I'm so happy for you.", pt="Sim! Estou tão feliz por você.", reply="Thanks! Can you come to the wedding?"),
   dict(en="Yes, it's beautiful!", pt="Sim, é lindo!", reply="Thank you! Can you come to the wedding?"),
   dict(en="Yes! Congratulations, Cole!", pt="Sim! Parabéns, Cole!", reply="Thanks! Can you come to the wedding?")]),
  dict(npc="Can you come to the wedding?", opts=[
   dict(en="Of course. When is it?", pt="Claro. Quando é?", reply="June tenth, at four o'clock."),
   dict(en="Yes! What day is it?", pt="Sim! Que dia é?", reply="June tenth. At four o'clock."),
   dict(en="I'd love to. What time is it?", pt="Adoraria. A que horas é?", reply="At four o'clock, on June tenth.")]),
  dict(npc="June tenth, at four o'clock.", opts=[
   dict(en="Where is it?", pt="Onde é?", reply="In a garden near the lake."),
   dict(en="Is it far from here?", pt="É longe daqui?", reply="Not far. It's in a garden near the lake."),
   dict(en="Is it inside or outside?", pt="É dentro ou fora?", reply="Outside, in a garden near the lake.")]),
  dict(npc="In a garden near the lake.", opts=[
   dict(en="What should I wear?", pt="O que devo vestir?", reply="A dress or a suit. Nothing white."),
   dict(en="Is it formal?", pt="É formal?", reply="A little. A dress or a suit is good. Nothing white."),
   dict(en="Should I bring a gift?", pt="Devo levar um presente?", reply="Just come! And wear a dress or a suit. Nothing white.")]),
 ], change=["Você não pode ir ao casamento: diga isso com educação e deseje felicidades.", "Você quer levar um amigo: pergunte se pode.", "Chove no dia: pergunte se o casamento continua no jardim."]),
 writing=dict(task="Cole convidou você para o casamento. Responda em 2 ou 3 frases: agradeça, diga que pode ir e pergunte o que vestir.", model="Thanks for the invitation! I can come to the wedding. What should I wear?", kw=["invitation", "wedding", "come", "wear"], checks=["Agradeceu o convite.", "Disse que pode ir.", "Perguntou o que vestir."]),
 scenes=dict(pool=["garden", "lake", "park", "hall"], npc=dict(g="m", role="friend"), you=dict(g="f")),
 convo=dict(npc=dict(name="Cole"), story="Seu primo Cole vai se casar. Ele liga para falar do convite.", turns=[
  dict(npc="Did you get the invitation?", pt="Você recebeu o convite?", opts=[
   dict(en="A dress or a suit.", pt="Vestido ou terno.", ok=False, fb="Essa fala é do Cole, e vem mais tarde."),
   dict(en="Yes! I'm so happy for you.", pt="Sim! Estou tão feliz por você.", ok=True, fb="Responde sim e demonstra carinho."),
   dict(en="Of course. When is it?", pt="Claro. Quando é?", ok=False, fb="Ele ainda não convidou você.")]),
  dict(npc="Can you come to the wedding?", pt="Você pode ir ao casamento?", opts=[
   dict(en="Yes! I'm so happy for you.", pt="Sim! Estou tão feliz por você.", ok=False, fb="Você já disse isso."),
   dict(en="June tenth, at four o'clock.", pt="Dez de junho, às quatro.", ok=False, fb="Essa informação é do Cole."),
   dict(en="Of course. When is it?", pt="Claro. Quando é?", ok=True, fb="Aceita e pergunta a data.")]),
  dict(npc="June tenth, at four o'clock.", pt="Dez de junho, às quatro horas.", opts=[
   dict(en="Of course. When is it?", pt="Claro. Quando é?", ok=False, fb="Ele acabou de dizer quando."),
   dict(en="Where is it?", pt="Onde é?", ok=True, fb="Próxima pergunta: o lugar."),
   dict(en="Did you get the invitation?", pt="Você recebeu o convite?", ok=False, fb="Essa pergunta era dele, no início.")]),
  dict(npc="In a garden near the lake.", pt="Em um jardim perto do lago.", opts=[
   dict(en="When is it?", pt="Quando é?", ok=False, fb="Ele já disse a data."),
   dict(en="Can you come to the wedding?", pt="Você pode ir ao casamento?", ok=False, fb="Quem convida é o Cole."),
   dict(en="What should I wear?", pt="O que devo vestir?", ok=True, fb="Pergunta natural sobre a roupa.")]),
  dict(npc="A dress or a suit. Nothing white.", pt="Vestido ou terno. Nada branco.", opts=[
   dict(en="Where is it?", pt="Onde é?", ok=False, fb="Ele já respondeu."),
   dict(en="That sounds good. See you there!", pt="Parece bom. Te vejo lá!", ok=True, fb="Fecha a conversa com simpatia."),
   dict(en="Yes, I got it.", pt="Sim, eu recebi.", ok=False, fb="Não responde à fala dele.")]),
 ]),
)
