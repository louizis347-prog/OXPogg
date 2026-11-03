X = dict(
 key=dict(big="What can I do?", label="Dia do voluntário", sub="Pergunte como pode ajudar, receba o material, peça por onde começar e pergunte se o amigo pode ajudar."),
 mini=[
  dict(who="Victor", en="Welcome to {Volunteer Day!|Cleanup Day!|Park Day!} Are you ready?", pt="Boas-vindas ao {Dia do Voluntário!|Dia da Limpeza!|Dia do Parque!} Está pronto?"),
  dict(who="You", en="Yes! What can I {do?|bring?|carry?}", pt="Sim! O que posso {fazer?|trazer?|carregar?}"),
  dict(who="Victor", en="Please {pick up trash|plant flowers|rake leaves} in the park.", pt="Por favor, {recolha o lixo|plante flores|junte as folhas} no parque."),
  dict(who="You", en="OK. Where do I {start?|put the bags?|get gloves?}", pt="Ok. {Por onde começo?|Onde coloco as sacolas?|Onde pego as luvas?}"),
 ],
 dlg=[
  dict(who="Victor", en="Welcome to Volunteer Day! Are you {ready?|here?}", pt="Boas-vindas ao Dia do Voluntário! Está {pronto?|aqui?}"),
  dict(who="You", en="Yes! What can I {do?|bring?}", pt="Sim! O que posso {fazer?|trazer?}"),
  dict(who="Victor", en="Please {pick up trash|rake leaves|plant flowers} in the park.", pt="Por favor, {recolha o lixo|junte as folhas|plante flores} no parque."),
  dict(who="You", en="Here are {gloves|vests} and a {bag.|rake.}", pt="Aqui estão {luvas|coletes} e uma {sacola.|rastelo.}"),
  dict(who="Victor", en="Thank you. Where do I {start?|go?}", pt="Valeu. {Por onde começo?|Para onde vou?}"),
  dict(who="You", en="Start near the {lake.|bench.}", pt="Comece perto do {lago.|banco.}"),
  dict(who="Victor", en="OK. Can my {friend|team} help too?", pt="Ok. Meu {amigo|time} pode ajudar também?"),
  dict(who="You", en="Of course! More {hands,|people,} less work.", pt="Claro! Mais {mãos,|pessoas,} menos trabalho."),
  dict(who="Victor", en="We have lots of {trash!|leaves!}", pt="Temos muito {lixo!|folha!}"),
 ],
 vocab=[
  dict(w="volunteer", pt="voluntário", e="🙋", ex=["I am a volunteer.", "Volunteers help the park."]),
  dict(w="community", pt="comunidade", e="🏘️", ex=["I help my community.", "The community loves the park."]),
  dict(w="rake", pt="rastelo", e="🍂", ex=["I have a rake.", "Use a rake for the leaves."]),
  dict(w="vest", pt="colete", e="🦺", ex=["The vest is orange.", "Put on your vest."]),
  dict(w="shovel", pt="pá", e="⛏️", ex=["I need a shovel.", "The shovel is old."]),
  dict(w="team", pt="equipe, time", e="🤝", ex=["We are a team.", "Our team is ready."]),
 ],
 molds=[
  dict(title="Oferecer ajuda", frame="What can I {verb}?", slots=[dict(key="verb", opts=["do", "bring", "carry", "start"])], model="What can I do?", note="What can I + verbo. Não diga 'What I can do'."),
  dict(title="Pedir por onde começar", frame="Where do I {verb}?", slots=[dict(key="verb", opts=["start", "go", "put the bags", "get gloves"])], model="Where do I start?", note="Where do I...? é a pergunta para pedir instrução de lugar."),
  dict(title="Escrever o convite", frame="Join us for {event} on {day}! Bring a {thing}.", slots=[dict(key="event", opts=["Park Day", "Cleanup Day", "Volunteer Day"]), dict(key="day", opts=["Saturday", "Sunday", "Friday"]), dict(key="thing", opts=["friend", "hat", "water bottle"])], model="Join us for Park Day on Saturday! Bring a friend.", note="Join us for... é o convite. Bring a... pede para trazer algo."),
 ],
 sounds=[
  dict(say="Please pick up trash.", tag="ligação: pick up", tip="Una pick e up: 'pi-kup'. O k liga na vogal de up."),
  dict(say="Start near the lake.", tag="ritmo: START NEAR the LAKE", tip="Acentue START, NEAR e LAKE; the fica fraco, quase 'thuh'."),
  dict(say="Of course!", tag="ligação: of course", tip="Of course soa 'uv-kors'. O of fica fraco, e course é forte."),
 ],
 role=dict(turns=[
  dict(npc="Welcome to Volunteer Day! Are you ready?", opts=[
   dict(en="Yes! What can I do?", pt="Sim! O que posso fazer?", reply="Please pick up trash in the park."),
   dict(en="Yes, I'm ready. How can I help?", pt="Sim, estou pronto. Como posso ajudar?", reply="Please pick up trash in the park."),
   dict(en="Hi! I'm here to help. What can I do?", pt="Oi! Vim ajudar. O que posso fazer?", reply="Please pick up trash in the park.")]),
  dict(npc="Please pick up trash in the park. Here are gloves and a bag.", opts=[
   dict(en="Thank you. Where do I start?", pt="Obrigado. Por onde começo?", reply="Start near the lake."),
   dict(en="Thanks. Where should I go?", pt="Valeu. Para onde devo ir?", reply="Start near the lake."),
   dict(en="Great. Where do I put the full bags?", pt="Ótimo. Onde coloco as sacolas cheias?", reply="Start near the lake, and put full bags by the gate.")]),
  dict(npc="Start near the lake.", opts=[
   dict(en="OK. Can my friend help too?", pt="Ok. Meu amigo pode ajudar também?", reply="Of course! More hands, less work."),
   dict(en="OK. My sister is here. Can she help?", pt="Ok. Minha irmã está aqui. Ela pode ajudar?", reply="Of course! More hands, less work."),
   dict(en="Sure. Can my team join?", pt="Claro. Meu time pode participar?", reply="Of course! More hands, less work.")]),
  dict(npc="Of course! More hands, less work.", opts=[
   dict(en="Great! We have lots of trash!", pt="Ótimo! Temos muito lixo!", reply="Thank you for helping today!"),
   dict(en="Right! Many hands make light work.", pt="Isso! Muitas mãos tornam o trabalho leve.", reply="Thank you for helping today!"),
   dict(en="Teamwork!", pt="Trabalho em equipe!", reply="Thank you for helping today!")]),
 ], change=["Acabaram as luvas: peça outro par.", "Você não encontra o lago: pergunte onde fica.", "Você quer descansar: peça um minuto e água."]),
 writing=dict(task="Escreva um convite curto para um amigo: fale do dia do voluntário, onde é e o que fazer.", model="Join us for Park Day on Saturday! We pick up trash near the lake. Bring a friend!", kw=["join", "park", "trash", "friend"], checks=["Convidou o amigo.", "Disse o dia e o lugar.", "Disse o que vão fazer."]),
 scenes=dict(pool=["park", "park2", "lake", "playground", "garden"], npc=dict(g="m", role="leader"), you=dict(g="f")),
 convo=dict(npc=dict(name="Victor"), story="Você chega ao Dia do Voluntário no parque. O líder dá as instruções.", turns=[
  dict(npc="Welcome to Volunteer Day! Are you ready?", pt="Boas-vindas ao Dia do Voluntário! Está pronto?", opts=[
   dict(en="Please pick up trash in the park.", pt="Por favor, recolha o lixo no parque.", ok=False, fb="Essa instrução é do líder."),
   dict(en="Yes! What can I do?", pt="Sim! O que posso fazer?", ok=True, fb="Mostra vontade de ajudar."),
   dict(en="Start near the lake.", pt="Comece perto do lago.", ok=False, fb="Você ainda não sabe o que fazer.")]),
  dict(npc="Please pick up trash in the park. Here are gloves and a bag.", pt="Por favor, recolha o lixo no parque. Aqui estão luvas e uma sacola.", opts=[
   dict(en="Thank you. Where do I start?", pt="Obrigado. Por onde começo?", ok=True, fb="Pergunta o lugar de partida."),
   dict(en="What can I do?", pt="O que posso fazer?", ok=False, fb="Ele já disse o que fazer."),
   dict(en="Welcome to Volunteer Day!", pt="Boas-vindas ao Dia do Voluntário!", ok=False, fb="Quem dá as boas-vindas é o líder.")]),
  dict(npc="Start near the lake.", pt="Comece perto do lago.", opts=[
   dict(en="Where do I start?", pt="Por onde começo?", ok=False, fb="Ele já respondeu."),
   dict(en="Here are gloves and a bag.", pt="Aqui estão luvas e uma sacola.", ok=False, fb="Ele já deu o material a você."),
   dict(en="OK. Can my friend help too?", pt="Ok. Meu amigo pode ajudar também?", ok=True, fb="Pergunta com educação.")]),
  dict(npc="Of course! More hands, less work.", pt="Claro! Mais mãos, menos trabalho.", opts=[
   dict(en="Great! We have lots of trash!", pt="Ótimo! Temos muito lixo!", ok=True, fb="Comenta a tarefa com bom humor."),
   dict(en="No, my friend cannot help.", pt="Não, meu amigo não pode ajudar.", ok=False, fb="Contradiz o que você pediu."),
   dict(en="Please pick up trash.", pt="Por favor, recolha o lixo.", ok=False, fb="Quem dá instruções é o líder.")]),
  dict(npc="Thank you for helping today!", pt="Obrigado por ajudar hoje!", opts=[
   dict(en="Are you ready?", pt="Está pronto?", ok=False, fb="O dia já está acabando."),
   dict(en="Start near the lake.", pt="Comece perto do lago.", ok=False, fb="Você já terminou."),
   dict(en="It feels great to give back.", pt="É ótimo retribuir.", ok=True, fb="Resposta simpática e natural.")]),
 ]),
)
