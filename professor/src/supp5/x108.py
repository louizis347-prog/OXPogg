X = dict(
 key=dict(big="When is the meeting?", label="Horário, sala e duração", sub="Pergunte quando e onde é a reunião, quanto tempo dura e o que levar."),
 mini=[
  dict(who="You", en="Excuse me, when is the {team meeting|class|lunch}?", pt="Com licença, quando é {a reunião da equipe|a aula|o almoço}?"),
  dict(who="Evan", en="It's at {ten|nine|two} o'clock.", pt="É às {dez|nove|duas} horas."),
  dict(who="You", en="Is it in room {two|three|five}?", pt="É na sala {dois|três|cinco}?"),
  dict(who="Evan", en="Yes, on the {second|third|first} floor.", pt="Sim, no {segundo|terceiro|primeiro} andar."),
 ],
 dlg=[
  dict(who="Evan", en="Excuse me, when is the team {meeting?|lunch?}", pt="Com licença, quando é {a reunião da equipe?|o almoço da equipe?}"),
  dict(who="You", en="It's at {ten|nine|two} o'clock.", pt="É às {dez|nove|duas} horas."),
  dict(who="Evan", en="Where is it?", pt="Onde é?"),
  dict(who="You", en="In room {two,|three,} on the {second|third} floor.", pt="Na sala {dois,|três,} no {segundo|terceiro} andar."),
  dict(who="Evan", en="How long is it?", pt="Quanto tempo dura?"),
  dict(who="You", en="About {thirty|twenty|forty} minutes.", pt="Uns {trinta|vinte|quarenta} minutos."),
  dict(who="Evan", en="Do I need to bring {anything?|a laptop?}", pt="Preciso levar {algo?|um laptop?}"),
  dict(who="You", en="Just a {pen|marker} and your {notebook.|laptop.}", pt="Só {uma caneta|um marcador} e seu {caderno.|laptop.}"),
  dict(who="Evan", en="What time is it now?", pt="Que horas são agora?"),
 ],
 vocab=[
  dict(w="slide", pt="slide", e="🖼️", ex=["This slide is long.", "Show the next slide."]),
  dict(w="agenda", pt="pauta", e="📋", ex=["The agenda has three items.", "Read the agenda, please."]),
  dict(w="marker", pt="marcador", e="🖍️", ex=["I need a marker.", "The marker is red."]),
  dict(w="pen", pt="caneta", e="🖊️", ex=["I need a pen.", "This pen is black."]),
  dict(w="topic", pt="assunto / tema", e="💬", ex=["What is the topic today?", "This topic is easy."]),
  dict(w="calendar", pt="calendário", e="🗓️", ex=["Check your calendar.", "The meeting is in my calendar."]),
 ],
 molds=[
  dict(title="Perguntar quando", frame="When is the {event}?", slots=[dict(key="event", opts=["team meeting", "class", "lunch"])], model="When is the team meeting?", note="When is...? pergunta o dia ou a hora. Não use 'What time is when'."),
  dict(title="Dizer hora e lugar", frame="It's at {time} o'clock, in room {room}, on the {floor} floor.", slots=[dict(key="time", opts=["nine", "ten", "two"]), dict(key="room", opts=["two", "three", "five"]), dict(key="floor", opts=["first", "second", "third"])], model="It's at nine o'clock, in room two, on the first floor.", note="At + hora, in + sala, on + andar."),
  dict(title="Escrever aviso", frame="Hi team! The meeting is at {time} in room {room}. Please bring a {thing}.", slots=[dict(key="time", opts=["nine o'clock", "ten o'clock", "two o'clock"]), dict(key="room", opts=["two", "three", "five"]), dict(key="thing", opts=["pen", "notebook", "laptop"])], model="Hi team! The meeting is at nine o'clock in room two. Please bring a pen.", note="Please bring... é um pedido educado em avisos."),
 ],
 sounds=[
  dict(say="About thirty minutes.", tag="acento: THIR-ty", tip="Em thirty a força vai no começo: THIR-ty. Em thirteen, no fim: thir-TEEN."),
  dict(say="Room two, second floor.", tag="acento: SEC-ond FLOOR", tip="Acentue SEC em 'second' e deixe 'ond' fraco. Bata também em FLOOR."),
  dict(say="What time is it now?", tag="acento: WHAT TIME … NOW", tip="Bata em WHAT, TIME e NOW. 'is it' fica fraco e rápido."),
 ],
 role=dict(turns=[
  dict(npc="Hi! Are you new here?", opts=[
   dict(en="Yes. When is the team meeting?", pt="Sou. Quando é a reunião da equipe?", reply="It's at ten o'clock."),
   dict(en="Yes. What time is the meeting?", pt="Sou. Que horas é a reunião?", reply="At ten o'clock."),
   dict(en="Yes, I am. Is there a meeting today?", pt="Sou. Tem reunião hoje?", reply="Yes, at ten o'clock.")]),
  dict(npc="Do you have any questions?", opts=[
   dict(en="Where is it?", pt="Onde é?", reply="In room two, on the second floor."),
   dict(en="Which room is it?", pt="Qual sala é?", reply="Room two, on the second floor."),
   dict(en="Is it in room one?", pt="É na sala um?", reply="No, in room two, on the second floor.")]),
  dict(npc="Anything else?", opts=[
   dict(en="How long is it?", pt="Quanto tempo dura?", reply="About thirty minutes."),
   dict(en="How long is the meeting?", pt="Quanto tempo dura a reunião?", reply="About thirty minutes."),
   dict(en="Is it long?", pt="É longa?", reply="No, only about thirty minutes.")]),
  dict(npc="Just ask if you need something.", opts=[
   dict(en="Do I need to bring anything?", pt="Preciso levar algo?", reply="Just a pen and your notebook."),
   dict(en="Do I need my laptop?", pt="Preciso do meu laptop?", reply="No, just a pen and your notebook."),
   dict(en="Should I bring paper?", pt="Devo levar papel?", reply="Your notebook is enough, and a pen.")]),
 ], change=["A reunião mudou para as onze: pergunte o novo horário.", "A sala está fechada: pergunte onde fica a outra sala.", "Você chega atrasado: diga que sente muito e pergunte se ainda pode entrar."]),
 writing=dict(task="Escreva um aviso curto para a equipe: diga a hora, a sala e o que levar.", model="Hi team! The meeting is at ten o'clock in room two. Please bring a pen and a notebook.", kw=["meeting", "room", "pen", "notebook"], checks=["Disse a hora da reunião.", "Disse a sala.", "Disse o que levar."]),
 scenes=dict(pool=["office", "lobby", "meetingroom", "hall"], npc=dict(g="m", role="coworker"), you=dict(g="f")),
 convo=dict(npc=dict(name="Evan"), story="Você é novo no escritório. Evan é um colega que conhece a agenda da equipe.", turns=[
  dict(npc="Hi! I'm Evan. Are you new here?", pt="Oi! Sou o Evan. Você é novo aqui?", opts=[
   dict(en="It's at ten o'clock.", pt="É às dez horas.", ok=False, fb="Você ainda não sabe o horário."),
   dict(en="Yes. Excuse me, when is the team meeting?", pt="Sou. Com licença, quando é a reunião da equipe?", ok=True, fb="Responda e pergunte o horário."),
   dict(en="About thirty minutes.", pt="Uns trinta minutos.", ok=False, fb="Ninguém perguntou a duração.")]),
  dict(npc="It's at ten o'clock.", pt="É às dez horas.", opts=[
   dict(en="Where is it?", pt="Onde é?", ok=True, fb="Próximo passo: o lugar."),
   dict(en="Fine, thank you.", pt="Bem, obrigado.", ok=False, fb="Ele disse o horário; pergunte o local."),
   dict(en="Just a pen.", pt="Só uma caneta.", ok=False, fb="Ainda não perguntou o que levar.")]),
  dict(npc="In room two, on the second floor.", pt="Na sala dois, no segundo andar.", opts=[
   dict(en="Where is it?", pt="Onde é?", ok=False, fb="Ele já disse onde."),
   dict(en="Just a pen and your notebook.", pt="Só uma caneta e seu caderno.", ok=False, fb="Essa é a resposta dele, não a sua."),
   dict(en="How long is it?", pt="Quanto tempo dura?", ok=True, fb="Pergunta a duração.")]),
  dict(npc="About thirty minutes.", pt="Uns trinta minutos.", opts=[
   dict(en="Do I need to bring anything?", pt="Preciso levar algo?", ok=True, fb="Pergunta o que levar."),
   dict(en="It's at ten o'clock.", pt="É às dez horas.", ok=False, fb="Ele já respondeu o horário."),
   dict(en="Room two, please.", pt="Sala dois, por favor.", ok=False, fb="Não é um pedido.")]),
  dict(npc="Just a pen and your notebook.", pt="Só uma caneta e seu caderno.", opts=[
   dict(en="What time is the meeting?", pt="Que horas é a reunião?", ok=False, fb="Você já sabe."),
   dict(en="Great, thanks! See you there.", pt="Ótimo, valeu! Até lá.", ok=True, fb="Agradeça e se despeça."),
   dict(en="About thirty minutes.", pt="Uns trinta minutos.", ok=False, fb="É resposta de outra pergunta.")]),
 ]),
)
