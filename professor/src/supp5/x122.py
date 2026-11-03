X = dict(
 key=dict(big="What are your plans?", label="Planos de sexta", sub="Fale da sua semana, diga seus planos e combine um jantar com um colega."),
 mini=[
  dict(who="Leo", en="It's Friday! How was your {week|day|morning}?", pt="É sexta! Como foi {sua semana|seu dia|sua manhã}?"),
  dict(who="You", en="It was {busy|long|great}, but good. And yours?", pt="Foi {corrida|longa|ótima}, mas boa. E a sua?"),
  dict(who="Leo", en="Same here. What are your {plans|ideas|thoughts}?", pt="Igual. Quais são {seus planos|suas ideias|seus pensamentos}?"),
  dict(who="You", en="I'm going to {relax|sleep|read} at home.", pt="Vou {relaxar|dormir|ler} em casa."),
 ],
 dlg=[
  dict(who="Leo", en="It's {Friday!|Friday night!} How was your {week?|day?}", pt="É {sexta!|sexta à noite!} Como foi {sua semana?|seu dia?}"),
  dict(who="You", en="It was {busy|long}, but good. And yours?", pt="Foi {corrida|longa}, mas boa. E a sua?"),
  dict(who="Leo", en="Same here. What are your {plans?|ideas?}", pt="Igual. Quais são {seus planos?|suas ideias?}"),
  dict(who="You", en="I'm going to {relax|rest} at home.", pt="Vou {relaxar|descansar} em casa."),
  dict(who="Leo", en="Do you want to get {dinner|lunch} tonight?", pt="Quer {jantar|almoçar} hoje à noite?"),
  dict(who="You", en="Sure! {Where?|When?}", pt="Claro! {Onde?|Quando?}"),
  dict(who="Leo", en="How about the {Italian|Mexican} place?", pt="Que tal o lugar {italiano?|mexicano?}"),
  dict(who="You", en="Great. What {time?|day?}", pt="Ótimo. Que {horas?|dia?}"),
  dict(who="Leo", en="At {seven thirty.|eight o'clock.}", pt="Às {sete e meia.|oito horas.}"),
 ],
 vocab=[
  dict(w="plans", pt="planos", e="🗓️", ex=["What are your plans?", "I have no plans tonight."]),
  dict(w="weekday", pt="dia de semana", e="📅", ex=["Monday is a weekday.", "I work on weekdays."]),
  dict(w="Italian", pt="italiano", e="🇮🇹", ex=["I like Italian food.", "The Italian place is near."]),
  dict(w="table", pt="mesa", e="🪑", ex=["A table for two, please.", "The table is by the window."]),
  dict(w="deadline", pt="prazo", e="⏳", ex=["The deadline is Friday.", "I have a deadline today."]),
  dict(w="happy hour", pt="happy hour", e="🍻", ex=["Happy hour starts at five.", "Let's go to happy hour."]),
 ],
 molds=[
  dict(title="Contar da semana", frame="My {noun} was {adj}, but good.", slots=[dict(key="noun", opts=["week", "day", "Monday"]), dict(key="adj", opts=["busy", "long", "hard"])], model="My week was busy, but good.", note="Was é o passado de is. Use para uma semana ou dia que acabou."),
  dict(title="Dizer um plano", frame="I'm going to {verb} {place}.", slots=[dict(key="verb", opts=["relax", "sleep", "cook"]), dict(key="place", opts=["at home", "tonight", "this weekend"])], model="I'm going to relax at home.", note="I'm going to + verbo na forma base fala de planos."),
  dict(title="Convidar por escrito", frame="Hi! Do you want to get {meal} {when}? How about the {food} place at {time}?", slots=[dict(key="meal", opts=["dinner", "lunch", "coffee"]), dict(key="when", opts=["tonight", "tomorrow", "on Saturday"]), dict(key="food", opts=["Italian", "Mexican", "Chinese"]), dict(key="time", opts=["seven thirty", "seven", "eight"])], model="Hi! Do you want to get dinner tonight? How about the Italian place at seven thirty?", note="Do you want to...? convida com simpatia. Use at com horas."),
 ],
 sounds=[
  dict(say="What are your plans?", tag="ligação: what are", tip="Una what e are: 'wha-tar'. O t fica leve, quase um d rápido."),
  dict(say="I'm going to relax.", tag="redução: going to → gonna", tip="Na fala rápida, going to soa 'gonna'. Acentue GO e reLAX."),
  dict(say="Do you want to get dinner?", tag="redução: want to → wanna", tip="Want to vira 'wanna'. Diga 'Dyou wanna get DINner?' com o acento em DIN."),
 ],
 role=dict(turns=[
  dict(npc="It's Friday! How was your week?", opts=[
   dict(en="It was busy, but good. And yours?", pt="Foi corrida, mas boa. E a sua?", reply="Same here. I need a break."),
   dict(en="It was long, but fine. And yours?", pt="Foi longa, mas boa. E a sua?", reply="Mine was busy, too."),
   dict(en="Great! And yours?", pt="Ótima! E a sua?", reply="Pretty good, thanks.")]),
  dict(npc="What are your plans?", opts=[
   dict(en="I'm going to relax at home.", pt="Vou relaxar em casa.", reply="That sounds nice."),
   dict(en="I'm going to sleep a lot.", pt="Vou dormir bastante.", reply="Good idea!"),
   dict(en="I don't have plans yet.", pt="Ainda não tenho planos.", reply="Then, how about dinner?")]),
  dict(npc="Do you want to get dinner tonight?", opts=[
   dict(en="Sure! Where?", pt="Claro! Onde?", reply="How about the Italian place?"),
   dict(en="Yes, I'd love to. Where?", pt="Sim, adoraria. Onde?", reply="How about the Italian place?"),
   dict(en="Sounds good. Where?", pt="Parece bom. Onde?", reply="How about the Italian place?")]),
  dict(npc="How about the Italian place?", opts=[
   dict(en="Great. What time?", pt="Ótimo. Que horas?", reply="At seven thirty."),
   dict(en="Perfect. When?", pt="Perfeito. Quando?", reply="At seven thirty."),
   dict(en="I love pasta. What time?", pt="Adoro massa. Que horas?", reply="At seven thirty.")]),
 ], change=["Você não pode às sete e meia: sugira outra hora.", "Você prefere comida mexicana: diga isso com educação.", "Leo pergunta se pode chamar mais um colega: diga que sim."]),
 writing=dict(task="Escreva 2 ou 3 frases para um colega: conte como foi sua semana e convide-o para jantar hoje à noite.", model="Hi! My week was busy, but good. Do you want to get dinner tonight?", kw=["week", "busy", "dinner", "tonight"], checks=["Falou da semana.", "Usou busy ou outro adjetivo.", "Convidou para jantar."]),
 scenes=dict(pool=["office", "hall", "street", "restaurant"], npc=dict(g="m", role="friend"), you=dict(g="f")),
 convo=dict(npc=dict(name="Leo"), story="É sexta à tarde no trabalho. Seu colega Leo quer combinar a noite.", turns=[
  dict(npc="It's Friday! How was your week?", pt="É sexta! Como foi sua semana?", opts=[
   dict(en="It was busy, but good. And yours?", pt="Foi corrida, mas boa. E a sua?", ok=True, fb="Responda e devolva a pergunta."),
   dict(en="At seven thirty.", pt="Às sete e meia.", ok=False, fb="Essa é a fala sobre o horário."),
   dict(en="Sure! Where?", pt="Claro! Onde?", ok=False, fb="Ele ainda não convidou.")]),
  dict(npc="Same here. What are your plans?", pt="Igual. Quais são seus planos?", opts=[
   dict(en="It was busy.", pt="Foi corrida.", ok=False, fb="Ele já ouviu isso."),
   dict(en="I'm going to relax at home.", pt="Vou relaxar em casa.", ok=True, fb="Plano com going to."),
   dict(en="Great. What time?", pt="Ótimo. Que horas?", ok=False, fb="Ainda não há horário.")]),
  dict(npc="Do you want to get dinner tonight?", pt="Quer jantar hoje à noite?", opts=[
   dict(en="I'm going to relax at home.", pt="Vou relaxar em casa.", ok=False, fb="Já disse isso e ele convidou."),
   dict(en="Sure! Where?", pt="Claro! Onde?", ok=True, fb="Aceite e pergunte o lugar."),
   dict(en="How about the Italian place?", pt="Que tal o italiano?", ok=False, fb="É a sugestão dele.")]),
  dict(npc="How about the Italian place?", pt="Que tal o italiano?", opts=[
   dict(en="It's Friday!", pt="É sexta!", ok=False, fb="Não responde à sugestão."),
   dict(en="Great. What time?", pt="Ótimo. Que horas?", ok=True, fb="Aceite e pergunte a hora."),
   dict(en="At seven thirty.", pt="Às sete e meia.", ok=False, fb="Quem diz a hora é ele.")]),
  dict(npc="At seven thirty. See you there!", pt="Às sete e meia. Até lá!", opts=[
   dict(en="Sounds good. See you there!", pt="Combinado. Até lá!", ok=True, fb="Confirme e despeça-se."),
   dict(en="Same here.", pt="Igual.", ok=False, fb="Não combina com a fala."),
   dict(en="What are your plans?", pt="Quais são seus planos?", ok=False, fb="Já falaram dos planos.")]),
 ]),
)
