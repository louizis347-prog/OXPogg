X = dict(
 key=dict(big="Passport control", label="Controle de passaportes", sub="Entregue o passaporte e responda com frases curtas: motivo da visita, quanto tempo e onde vai ficar."),
 mini=[
  dict(who="Bethany", en="What's the purpose of your {visit?|trip?}", pt="Qual o motivo da sua {visita?|viagem?}"),
  dict(who="You", en="{Tourism.|Work.|Study.} I'm here on {vacation.|business.|a trip.}", pt="{Turismo.|Trabalho.|Estudo.} Estou aqui {de férias.|a negócios.|em viagem.}"),
  dict(who="Bethany", en="How long will you stay?", pt="Quanto tempo vai ficar?"),
  dict(who="You", en="{Two weeks.|Ten days.|One week.} At a {hotel|friend's house|hostel} in Midtown.", pt="{Duas semanas.|Dez dias.|Uma semana.} Em um {hotel|casa de amigo|hostel} em Midtown."),
 ],
 dlg=[
  dict(who="Bethany", en="Next, please. {Passport?|Visa?}", pt="Próximo, por favor. {Passaporte?|Visto?}"),
  dict(who="You", en="Here you {go.|are.}", pt="Aqui {está.|está.}"),
  dict(who="Bethany", en="What's the {purpose|reason} of your visit?", pt="Qual o {motivo|motivo} da sua visita?"),
  dict(who="You", en="{Tourism.|Study.} I'm here on {vacation.|a trip.}", pt="{Turismo.|Estudo.} Estou aqui {de férias.|em viagem.}"),
  dict(who="Bethany", en="How long will you {stay?|be here?}", pt="Quanto tempo vai {ficar?|ficar aqui?}"),
  dict(who="You", en="{Two weeks.|One week.}", pt="{Duas semanas.|Uma semana.}"),
  dict(who="Bethany", en="Where will you {stay?|sleep?}", pt="Onde vai {ficar?|dormir?}"),
  dict(who="You", en="At a {hotel|hostel} in Midtown.", pt="Em um {hotel|hostel} em Midtown."),
  dict(who="Bethany", en="Do you have a return {ticket?|flight?}", pt="Tem {passagem|voo} de volta?"),
 ],
 vocab=[
  dict(w="officer", pt="oficial, agente", e="👮", ex=["The officer is kind.", "The officer looks at my passport."]),
  dict(w="visa", pt="visto", e="📄", ex=["Do I need a visa?", "My visa is in my passport."]),
  dict(w="week", pt="semana", e="📅", ex=["I stay for one week.", "Two weeks is a long time."]),
  dict(w="stay", pt="ficar, hospedar-se", e="🛏️", ex=["I stay at a hotel.", "How long will you stay?"]),
  dict(w="welcome", pt="bem-vindo; de nada", e="👋", ex=["Welcome to the USA!", "Thank you. — You're welcome."]),
  dict(w="customs", pt="alfândega", e="🧾", ex=["I go through customs.", "Customs is after passport control."]),
 ],
 molds=[
  dict(title="Dizer o motivo", frame="{reason}. I'm here on {kind}.", slots=[dict(key="reason", opts=["Tourism", "Business", "Study"]), dict(key="kind", opts=["vacation", "a trip", "business"])], model="Tourism. I'm here on vacation.", note="I'm here on vacation = estou aqui de férias. Use on, não in."),
  dict(title="Dizer o tempo", frame="I'll stay for {time}.", slots=[dict(key="time", opts=["one week", "two weeks", "ten days", "a month"])], model="I'll stay for one week.", note="For + tempo diz a duração. I'll = I will."),
  dict(title="Escrever as respostas", frame="I'm here for {reason}. I'll stay {where} for {time}.", slots=[dict(key="reason", opts=["tourism", "work", "study"]), dict(key="where", opts=["at a hotel", "at a hostel", "with a friend"]), dict(key="time", opts=["a week", "two weeks", "ten days"])], model="I'm here for tourism. I'll stay at a hotel for a week.", note="Três respostas curtas: motivo, lugar e tempo."),
 ],
 sounds=[
  dict(say="Here you go.", tag="ligação: here you go", tip="Soa 'hiyugou'. Una as três palavras e acentue GO."),
  dict(say="How long will you stay?", tag="ritmo: HOW LONG will you STAY", tip="Acentue HOW, LONG e STAY; 'will you' fica rápido: 'wilyu'."),
  dict(say="Two weeks.", tag="o som do w", tip="Arredonde os lábios em 'w' de weeks: 'uíks', sem encostar os dentes no lábio."),
 ],
 role=dict(turns=[
  dict(npc="Next, please. Passport?", opts=[
   dict(en="Here you go.", pt="Aqui está.", reply="What's the purpose of your visit?"),
   dict(en="Good morning. Here is my passport.", pt="Bom dia. Aqui está meu passaporte.", reply="What's the purpose of your visit?"),
   dict(en="Hello! Here it is.", pt="Olá! Aqui está.", reply="What's the purpose of your visit?")]),
  dict(npc="What's the purpose of your visit?", opts=[
   dict(en="Tourism. I'm here on vacation.", pt="Turismo. Estou de férias.", reply="How long will you stay?"),
   dict(en="Business. I have a meeting.", pt="Negócios. Tenho uma reunião.", reply="How long will you stay?"),
   dict(en="I'm here to visit a friend.", pt="Vim visitar um amigo.", reply="How long will you stay?")]),
  dict(npc="How long will you stay?", opts=[
   dict(en="Two weeks.", pt="Duas semanas.", reply="Where will you stay?"),
   dict(en="Ten days.", pt="Dez dias.", reply="Where will you stay?"),
   dict(en="One week.", pt="Uma semana.", reply="Where will you stay?")]),
  dict(npc="Where will you stay?", opts=[
   dict(en="At a hotel in Midtown.", pt="Em um hotel em Midtown.", reply="Do you have a return ticket?"),
   dict(en="With a friend in Atlanta.", pt="Com um amigo em Atlanta.", reply="Do you have a return ticket?"),
   dict(en="At a hostel downtown.", pt="Em um hostel no centro.", reply="Do you have a return ticket?")]),
 ], change=["O oficial não ouviu bem: peça para repetir a pergunta com educação.", "Você esqueceu o nome do hotel: diga que está no celular e mostre.", "O oficial diz bem-vindo: agradeça e se despeça."]),
 writing=dict(task="Escreva 2 ou 3 frases para o oficial: diga o motivo da visita, quanto tempo vai ficar e onde.", model="Tourism. I'm here on vacation. I'll stay for two weeks at a hotel in Midtown.", kw=["tourism", "vacation", "weeks", "hotel"], checks=["Disse o motivo da visita.", "Disse quanto tempo vai ficar.", "Disse onde vai ficar."]),
 scenes=dict(pool=["airport", "airport2", "counter", "hall"], npc=dict(g="f", role="officer"), you=dict(g="m")),
 convo=dict(npc=dict(name="Bethany"), story="Você chegou a Atlanta. A Bethany é a oficial do controle de passaportes.", turns=[
  dict(npc="Next, please. Passport?", pt="Próximo, por favor. Passaporte?", opts=[
   dict(en="Here you go.", pt="Aqui está.", ok=True, fb="Entrega o passaporte."),
   dict(en="Two weeks.", pt="Duas semanas.", ok=False, fb="Ainda não perguntaram o tempo."),
   dict(en="I'm here on vacation.", pt="Estou de férias.", ok=False, fb="Primeiro entregue o passaporte.")]),
  dict(npc="What's the purpose of your visit?", pt="Qual o motivo da sua visita?", opts=[
   dict(en="At a hotel in Midtown.", pt="Em um hotel em Midtown.", ok=False, fb="Isso responde 'onde'."),
   dict(en="Tourism. I'm here on vacation.", pt="Turismo. Estou de férias.", ok=True, fb="Responde o motivo."),
   dict(en="Here you go.", pt="Aqui está.", ok=False, fb="Já entregou o passaporte.")]),
  dict(npc="How long will you stay?", pt="Quanto tempo vai ficar?", opts=[
   dict(en="Two weeks.", pt="Duas semanas.", ok=True, fb="Responde o tempo."),
   dict(en="I'm here for tourism.", pt="Estou aqui por turismo.", ok=False, fb="Já disse o motivo."),
   dict(en="Yes, I do.", pt="Sim, tenho.", ok=False, fb="Não é pergunta de sim ou não.")]),
  dict(npc="Where will you stay?", pt="Onde vai ficar?", opts=[
   dict(en="Two weeks.", pt="Duas semanas.", ok=False, fb="Já disse o tempo."),
   dict(en="At a hotel in Midtown.", pt="Em um hotel em Midtown.", ok=True, fb="Responde o lugar."),
   dict(en="Next, please.", pt="Próximo, por favor.", ok=False, fb="Essa fala é da oficial.")]),
  dict(npc="Do you have a return ticket?", pt="Tem passagem de volta?", opts=[
   dict(en="Where will you stay?", pt="Onde vai ficar?", ok=False, fb="É ela quem faz as perguntas."),
   dict(en="Yes, I do. Here it is.", pt="Sim, tenho. Aqui está.", ok=True, fb="Responde e mostra a passagem."),
   dict(en="I'm here on vacation.", pt="Estou de férias.", ok=False, fb="Não responde sobre a passagem.")]),
 ]),
)
