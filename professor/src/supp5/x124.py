X = dict(
 key=dict(big="I'd like to make an appointment", label="Marcar uma consulta", sub="Ao telefone, diga que quer marcar, dê seu nome, soletre o sobrenome e escolha dia e hora."),
 mini=[
  dict(who="Darius", en="Good morning, Dr. Rivera's {office.|clinic.|desk.}", pt="Bom dia, {consultório|clínica|recepção} do Dr. Rivera."),
  dict(who="You", en="Hi. I'd like to make an {appointment.|visit.|check-up.}", pt="Oi. Gostaria de marcar {uma consulta.|uma visita.|um check-up.}"),
  dict(who="Darius", en="What's your {name?|last name?|phone number?}", pt="Qual é {seu nome?|seu sobrenome?|seu telefone?}"),
  dict(who="You", en="Do you have time on {Tuesday?|Monday?|Friday?}", pt="Vocês têm horário {na terça?|na segunda?|na sexta?}"),
 ],
 dlg=[
  dict(who="Darius", en="Good morning, Dr. Rivera's {office.|clinic.}", pt="Bom dia, {consultório|clínica} do Dr. Rivera."),
  dict(who="You", en="Hi. I'd like to make an {appointment.|visit.}", pt="Oi. Gostaria de marcar {uma consulta.|uma visita.}"),
  dict(who="Darius", en="Sure. What's your {name?|last name?}", pt="Claro. Qual é {seu nome?|seu sobrenome?}"),
  dict(who="You", en="It's {Alex Silva.|Ana Souza.}", pt="É {Alex Silva.|Ana Souza.}"),
  dict(who="Darius", en="How do you {spell|write} your last name?", pt="Como se {escreve|escreve} seu sobrenome?"),
  dict(who="You", en="{S-I-L-V-A.|S-O-U-Z-A.}", pt="{S-I-L-V-A.|S-O-U-Z-A.}"),
  dict(who="Darius", en="When can you {come?|visit?}", pt="Quando você pode {vir?|vir?}"),
  dict(who="You", en="Do you have time on {Tuesday?|Monday?}", pt="Vocês têm horário {na terça?|na segunda?}"),
  dict(who="Darius", en="We have {ten|nine} o'clock or {two|three} o'clock.", pt="Temos às {dez|nove} ou às {duas.|três.}"),
 ],
 vocab=[
  dict(w="last name", pt="sobrenome", e="🏷️", ex=["My last name is Silva.", "What is your last name?"]),
  dict(w="Tuesday", pt="terça-feira", e="📆", ex=["See you on Tuesday.", "Tuesday is a good day."]),
  dict(w="clinic", pt="clínica", e="🏥", ex=["The clinic opens at nine.", "I go to the clinic."]),
  dict(w="date", pt="data", e="🗓️", ex=["What is the date?", "The date is Tuesday, May ten."]),
  dict(w="answer", pt="atender / resposta", e="📞", ex=["Please answer the phone.", "I know the answer."]),
  dict(w="reminder", pt="lembrete", e="🔔", ex=["I got a reminder.", "The reminder says two o'clock."]),
 ],
 molds=[
  dict(title="Pedir a consulta", frame="Hi. I'd like to make an appointment {when}.", slots=[dict(key="when", opts=["for Tuesday", "for Monday", "for next week", "for tomorrow"])], model="Hi. I'd like to make an appointment for Tuesday.", note="I'd like to... é educado. Use for + dia."),
  dict(title="Perguntar horário", frame="Do you have time on {day} at {time}?", slots=[dict(key="day", opts=["Tuesday", "Monday", "Friday"]), dict(key="time", opts=["ten", "two", "four"])], model="Do you have time on Tuesday at ten?", note="Use on com dias e at com horas. Na fala, ten o'clock é comum."),
  dict(title="Escrever o pedido", frame="Hello. My name is {name}. I'd like an appointment on {day} at {time} o'clock.", slots=[dict(key="name", opts=["Alex Silva", "Ana Souza", "Leo Costa"]), dict(key="day", opts=["Tuesday", "Monday", "Friday"]), dict(key="time", opts=["ten", "two", "three"])], model="Hello. My name is Alex Silva. I'd like an appointment on Tuesday at ten o'clock.", note="Diga seu nome, o dia (on) e a hora (at)."),
 ],
 sounds=[
  dict(say="S-I-L-V-A.", tag="ritmo: letras em inglês", tip="Diga cada letra com pausa. Atenção: I soa 'ai' e A soa 'êi'."),
  dict(say="I'd like to make an appointment.", tag="redução: I'd like to", tip="Soa 'aid-laik-ta'. Acentue LIKE, MAKE e POINT."),
  dict(say="Do you have time on Tuesday?", tag="ligação: time on", tip="Una time e on: 'tai-mon'. Acentue TIME e TUES."),
 ],
 role=dict(turns=[
  dict(npc="Good morning, Dr. Rivera's office.", opts=[
   dict(en="Hi. I'd like to make an appointment.", pt="Oi. Gostaria de marcar uma consulta.", reply="Sure. What's your name?"),
   dict(en="Good morning. I need an appointment.", pt="Bom dia. Preciso de uma consulta.", reply="Sure. What's your name?"),
   dict(en="Hello. Can I make an appointment?", pt="Olá. Posso marcar uma consulta?", reply="Sure. What's your name?")]),
  dict(npc="Sure. What's your name?", opts=[
   dict(en="It's Alex Silva.", pt="É Alex Silva.", reply="How do you spell your last name?"),
   dict(en="My name is Ana Souza.", pt="Meu nome é Ana Souza.", reply="How do you spell your last name?"),
   dict(en="Alex Silva, please.", pt="Alex Silva, por favor.", reply="How do you spell your last name?")]),
  dict(npc="How do you spell your last name?", opts=[
   dict(en="S-I-L-V-A.", pt="S-I-L-V-A.", reply="Thanks. When can you come?"),
   dict(en="It's S-I-L-V-A.", pt="É S-I-L-V-A.", reply="Thanks. When can you come?"),
   dict(en="S, I, L, V, A.", pt="S, I, L, V, A.", reply="Thanks. When can you come?")]),
  dict(npc="When can you come?", opts=[
   dict(en="Do you have time on Tuesday?", pt="Vocês têm horário na terça?", reply="We have ten o'clock or two o'clock."),
   dict(en="Is Monday OK?", pt="Segunda está bom?", reply="We have ten o'clock or two o'clock."),
   dict(en="I can come on Friday.", pt="Posso ir na sexta.", reply="We have ten o'clock or two o'clock.")]),
 ], change=["O horário que você quer está cheio: pergunte por outro dia.", "A recepcionista não entendeu seu sobrenome: soletre de novo.", "Você prefere de manhã: peça o horário das dez."]),
 writing=dict(task="Escreva 2 ou 3 frases para um consultório: diga seu nome, que quer marcar uma consulta e pergunte se há horário na terça.", model="Hello. My name is Alex Silva. I'd like to make an appointment. Do you have time on Tuesday?", kw=["appointment", "name", "tuesday", "time"], checks=["Disse seu nome.", "Disse que quer marcar uma consulta.", "Perguntou por um dia."]),
 scenes=dict(pool=["clinic", "office", "counter", "hall"], npc=dict(g="m", role="receptionist"), you=dict(g="m")),
 convo=dict(npc=dict(name="Darius"), story="Você liga para o consultório do Dr. Rivera. Darius atende.", turns=[
  dict(npc="Good morning, Dr. Rivera's office.", pt="Bom dia, consultório do Dr. Rivera.", opts=[
   dict(en="S-I-L-V-A.", pt="S-I-L-V-A.", ok=False, fb="Ainda ninguém pediu o sobrenome."),
   dict(en="Hi. I'd like to make an appointment.", pt="Oi. Gostaria de marcar uma consulta.", ok=True, fb="Diga por que liga."),
   dict(en="We have ten o'clock.", pt="Temos às dez.", ok=False, fb="É a fala da recepção.")]),
  dict(npc="Sure. What's your name?", pt="Claro. Qual é seu nome?", opts=[
   dict(en="It's Alex Silva.", pt="É Alex Silva.", ok=True, fb="Diga o nome."),
   dict(en="Do you have time on Tuesday?", pt="Vocês têm horário na terça?", ok=False, fb="Primeiro o nome."),
   dict(en="Good morning.", pt="Bom dia.", ok=False, fb="Já se cumprimentaram.")]),
  dict(npc="How do you spell your last name?", pt="Como se escreve seu sobrenome?", opts=[
   dict(en="It's Alex.", pt="É Alex.", ok=False, fb="Alex não é o sobrenome."),
   dict(en="Tuesday, please.", pt="Terça, por favor.", ok=False, fb="Ele pediu letras."),
   dict(en="S-I-L-V-A.", pt="S-I-L-V-A.", ok=True, fb="Soletre devagar.")]),
  dict(npc="When can you come?", pt="Quando você pode vir?", opts=[
   dict(en="Do you have time on Tuesday?", pt="Vocês têm horário na terça?", ok=True, fb="Pergunte por um dia."),
   dict(en="It's Alex Silva.", pt="É Alex Silva.", ok=False, fb="Ele já tem seu nome."),
   dict(en="I'd like to make an appointment.", pt="Gostaria de marcar uma consulta.", ok=False, fb="Você já disse isso.")]),
  dict(npc="We have ten o'clock or two o'clock.", pt="Temos às dez ou às duas.", opts=[
   dict(en="S-I-L-V-A.", pt="S-I-L-V-A.", ok=False, fb="Não responde ao horário."),
   dict(en="Ten o'clock works for me. Thanks!", pt="Às dez serve pra mim. Obrigado!", ok=True, fb="Escolha um horário e agradeça."),
   dict(en="I'd like to make an appointment.", pt="Gostaria de marcar uma consulta.", ok=False, fb="Já foi feito.")]),
 ]),
)
