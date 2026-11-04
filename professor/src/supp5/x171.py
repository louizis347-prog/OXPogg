X = dict(
 key=dict(big="I'd like to make a reservation", label="Reservar uma mesa", sub="Diga que quer reservar, informe quantas pessoas, o dia e o horário, e peça o lugar que prefere."),
 mini=[
  dict(who="You", en="Hi. I'd like to {make a reservation|book a table|reserve a table}.", pt="Oi. Gostaria de {fazer uma reserva|reservar uma mesa|reservar uma mesa}."),
  dict(who="Cole", en="Sure. For how many {people|guests|friends}?", pt="Claro. Para quantas {pessoas|convidados|amigos}?"),
  dict(who="You", en="{Four|Two|Six} people, {Saturday|Friday|Sunday} at seven thirty.", pt="{Quatro|Duas|Seis} pessoas, {sábado|sexta|domingo} às sete e meia."),
  dict(who="Cole", en="Yes, we have a table {outside|inside|by the window}.", pt="Sim, temos uma mesa {do lado de fora|lá dentro|perto da janela}."),
 ],
 dlg=[
  dict(who="Cole", en="Good {evening,|afternoon,} Bella's Kitchen.", pt="{Boa noite,|Boa tarde,} Bella's Kitchen."),
  dict(who="You", en="Hi. I'd like to make a {reservation.|booking.}", pt="Oi. Gostaria de fazer uma {reserva.|reserva.}"),
  dict(who="Cole", en="Sure. For how many {people?|guests?}", pt="Claro. Para quantas {pessoas?|pessoas?}"),
  dict(who="You", en="{Four|Two|Six} people.", pt="{Quatro|Duas|Seis} pessoas."),
  dict(who="Cole", en="What {day|date} and time?", pt="Que {dia|data} e horário?"),
  dict(who="You", en="{Saturday|Friday} at seven {thirty.|fifteen.}", pt="{Sábado|Sexta} às sete e {meia.|quinze.}"),
  dict(who="Cole", en="Let me check. Yes, we have a {table.|spot.}", pt="Vou ver. Sim, temos uma {mesa.|vaga.}"),
  dict(who="You", en="Great. Can we sit {outside?|inside?}", pt="Ótimo. Podemos ficar {do lado de fora?|lá dentro?}"),
  dict(who="Cole", en="Yes, on the {patio.|porch.}", pt="Sim, no {pátio.|alpendre.}"),
 ],
 vocab=[
  dict(w="patio", pt="pátio, área externa", e="🌿", ex=["We sit on the patio.", "The patio is quiet."]),
  dict(w="menu", pt="cardápio", e="📋", ex=["Can I see the menu?", "The menu is on the table."]),
  dict(w="outside", pt="do lado de fora", e="🌳", ex=["We sit outside.", "It is nice outside."]),
  dict(w="quiet", pt="tranquilo, silencioso", e="🤫", ex=["This place is quiet.", "I want a quiet table."]),
  dict(w="candle", pt="vela", e="🕯️", ex=["There is a candle on the table.", "The candle is red."]),
  dict(w="full", pt="lotado, cheio", e="🈵", ex=["The restaurant is full.", "Saturday is full."]),
 ],
 molds=[
  dict(title="Pedir uma reserva", frame="I'd like to {do} for {number} people.", slots=[dict(key="do", opts=["book a table", "reserve a table", "make a reservation"]), dict(key="number", opts=["two", "four", "six"])], model="I'd like to book a table for two people.", note="I'd like to... é educado. Book/reserve a table = reservar uma mesa."),
  dict(title="Dizer dia e hora", frame="{day} at {time}, please.", slots=[dict(key="day", opts=["Friday", "Saturday", "Sunday"]), dict(key="time", opts=["six", "seven thirty", "eight"])], model="Friday at six, please.", note="Com horário, use at: at six, at seven thirty."),
  dict(title="Escrever o pedido", frame="Hi! A table for {number}, {day} at {time}. Can we sit {place}?", slots=[dict(key="number", opts=["three", "four", "five"]), dict(key="day", opts=["Friday", "Saturday", "Sunday"]), dict(key="time", opts=["seven", "eight", "nine"]), dict(key="place", opts=["outside", "inside", "by the window"])], model="Hi! A table for three, Friday at seven. Can we sit outside?", note="Table for + número diz quantas pessoas. Can we sit...? pede o lugar."),
 ],
 sounds=[
  dict(say="Can we sit outside?", tag="ligação: sit outside", tip="Una sit e outside: 'sitoutside'. O t liga na vogal seguinte."),
  dict(say="What day and time?", tag="redução: and", tip="And fica fraco, quase 'n': 'day-n-time'. Acentue DAY e TIME."),
  dict(say="Saturday at seven thirty.", tag="ritmo: SAturday at SEven THIRty", tip="Acentue SA, SE e THIR; 'at' fica rápido e fraco."),
 ],
 role=dict(turns=[
  dict(npc="Good evening, Bella's Kitchen.", opts=[
   dict(en="Hi. I'd like to make a reservation.", pt="Oi. Gostaria de fazer uma reserva.", reply="Sure. For how many people?"),
   dict(en="Hello. Can I book a table?", pt="Olá. Posso reservar uma mesa?", reply="Sure. For how many people?"),
   dict(en="Hi. I'd like to reserve a table.", pt="Oi. Gostaria de reservar uma mesa.", reply="Of course. For how many people?")]),
  dict(npc="For how many people?", opts=[
   dict(en="Four people.", pt="Quatro pessoas.", reply="What day and time?"),
   dict(en="A table for four, please.", pt="Uma mesa para quatro, por favor.", reply="What day and time?"),
   dict(en="Six people, please.", pt="Seis pessoas, por favor.", reply="Okay. What day and time?")]),
  dict(npc="What day and time?", opts=[
   dict(en="Saturday at seven thirty.", pt="Sábado às sete e meia.", reply="Let me check. Yes, we have a table."),
   dict(en="Friday at eight.", pt="Sexta às oito.", reply="Let me check. Yes, we have a table."),
   dict(en="Sunday at six.", pt="Domingo às seis.", reply="Let me check. Yes, we have a table.")]),
  dict(npc="Yes, we have a table.", opts=[
   dict(en="Great. Can we sit outside?", pt="Ótimo. Podemos ficar do lado de fora?", reply="Yes, on the patio."),
   dict(en="Thanks. Can we sit inside?", pt="Obrigado. Podemos ficar lá dentro?", reply="Yes, inside is fine."),
   dict(en="Perfect. Is it a quiet table?", pt="Perfeito. É uma mesa tranquila?", reply="Yes, it is quiet.")]),
 ], change=["O restaurante está lotado no horário: peça outro horário.", "Você precisa de uma mesa para mais duas pessoas: avise o número novo.", "Você vai chegar atrasado: ligue e avise."]),
 writing=dict(task="Escreva 2 ou 3 frases para reservar uma mesa: diga quantas pessoas, o dia, o horário e o lugar que você quer.", model="Hi! I'd like a table for four on Saturday at seven thirty. Can we sit outside?", kw=["table", "four", "saturday", "outside"], checks=["Disse quantas pessoas.", "Disse o dia e o horário.", "Pediu o lugar."]),
 scenes=dict(pool=["diner", "restaurant", "counter", "street"], npc=dict(g="m", role="host"), you=dict(g="f")),
 convo=dict(npc=dict(name="Cole"), story="Você liga para o restaurante Bella's Kitchen para reservar uma mesa. O Cole atende.", turns=[
  dict(npc="Good evening, Bella's Kitchen.", pt="Boa noite, Bella's Kitchen.", opts=[
   dict(en="Hi. I'd like to make a reservation.", pt="Oi. Gostaria de fazer uma reserva.", ok=True, fb="Abre a ligação e diz o objetivo."),
   dict(en="Yes, we have a table.", pt="Sim, temos uma mesa.", ok=False, fb="Quem diz isso é o restaurante."),
   dict(en="Four people.", pt="Quatro pessoas.", ok=False, fb="Cedo demais: primeiro diga que quer reservar.")]),
  dict(npc="Sure. For how many people?", pt="Claro. Para quantas pessoas?", opts=[
   dict(en="Saturday at seven thirty.", pt="Sábado às sete e meia.", ok=False, fb="Ele ainda não perguntou o dia."),
   dict(en="Four people.", pt="Quatro pessoas.", ok=True, fb="Responde a pergunta."),
   dict(en="Yes, on the patio.", pt="Sim, no pátio.", ok=False, fb="Essa fala é dele e não responde.")]),
  dict(npc="What day and time?", pt="Que dia e horário?", opts=[
   dict(en="Four people.", pt="Quatro pessoas.", ok=False, fb="Você já disse isso."),
   dict(en="Let me check.", pt="Vou ver.", ok=False, fb="Quem confere a agenda é ele."),
   dict(en="Saturday at seven thirty.", pt="Sábado às sete e meia.", ok=True, fb="Dia e hora, com at.")]),
  dict(npc="Let me check. Yes, we have a table.", pt="Vou ver. Sim, temos uma mesa.", opts=[
   dict(en="Great. Can we sit outside?", pt="Ótimo. Podemos ficar do lado de fora?", ok=True, fb="Pedido educado do lugar."),
   dict(en="I'd like to make a reservation.", pt="Gostaria de fazer uma reserva.", ok=False, fb="Você já fez o pedido."),
   dict(en="What day and time?", pt="Que dia e horário?", ok=False, fb="Você já disse o dia e a hora.")]),
  dict(npc="Yes, on the patio.", pt="Sim, no pátio.", opts=[
   dict(en="Sorry, we are full.", pt="Desculpe, estamos lotados.", ok=False, fb="Quem diz isso é o restaurante."),
   dict(en="That sounds good. Thank you!", pt="Parece bom. Obrigado!", ok=True, fb="Fecha a ligação com simpatia."),
   dict(en="For how many people?", pt="Para quantas pessoas?", ok=False, fb="Já foi respondido.")]),
 ]),
)
