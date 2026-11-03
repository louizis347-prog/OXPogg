X = dict(
 key=dict(big="How much is the tip?", label="Gorjeta (tip)", sub="Em restaurantes com serviço à mesa nos EUA, a gorjeta costuma ficar entre 15% e 20% da conta; não costuma vir incluída."),
 mini=[
  dict(who="Cole", en="How was {everything|the food|your meal}?", pt="Como {estava tudo|estava a comida|foi a refeição}?"),
  dict(who="You", en="{Great|Delicious|Really good}, thank you!", pt="{Ótimo|Delicioso|Muito bom}, obrigado!"),
  dict(who="Cole", en="Here's your {check|bill|receipt}.", pt="Aqui está {a conta|a conta|o recibo}."),
  dict(who="You", en="Thanks. How much is the {tip|tip here|service}?", pt="Valeu. Quanto é {a gorjeta|a gorjeta aqui|o serviço}?"),
 ],
 dlg=[
  dict(who="Cole", en="How was {everything|the food}?", pt="Como {estava tudo|estava a comida}?"),
  dict(who="You", en="{Great|Delicious}, thank you!", pt="{Ótimo|Delicioso}, obrigado!"),
  dict(who="Cole", en="Here's your {check|bill}.", pt="Aqui está {a conta|a conta}."),
  dict(who="You", en="Thanks. How much is the {tip|tip here}?", pt="Valeu. Quanto é {a gorjeta|a gorjeta aqui}?"),
  dict(who="Cole", en="{Fifteen to twenty|Fifteen to eighteen} percent.", pt="De {quinze a vinte|quinze a dezoito} por cento."),
  dict(who="You", en="Okay. {Twenty|Eighteen|Fifteen} percent, then.", pt="Ok. {Vinte|Dezoito|Quinze} por cento, então."),
  dict(who="Cole", en="You're so {kind|nice}. Thank you!", pt="Você é muito {gentil|legal}. Obrigada!"),
  dict(who="You", en="Have a {great|good} night!", pt="Tenha uma {ótima|boa} noite!"),
  dict(who="Cole", en="Have a lovely night!", pt="Tenha uma linda noite!"),
 ],
 vocab=[
  dict(w="tip", pt="gorjeta", e="💵", ex=["How much is the tip?", "I leave a tip for good service."]),
  dict(w="percent", pt="por cento", e="💯", ex=["Twenty percent is a good tip.", "Ten percent of ten dollars is one dollar."]),
  dict(w="change", pt="troco", e="🪙", ex=["Keep the change.", "Here's your change."]),
  dict(w="waiter", pt="garçom", e="🧑‍🍳", ex=["The waiter is very kind.", "Thank the waiter, please."]),
  dict(w="service", pt="serviço, atendimento", e="🙏", ex=["The service was great.", "Is service included?"]),
  dict(w="kind", pt="gentil", e="😊", ex=["You are so kind.", "The waiter is kind."]),
 ],
 molds=[
  dict(title="Perguntar da gorjeta", frame="How much is the {thing}?", slots=[dict(key="thing", opts=["tip", "check", "total"])], model="How much is the tip?", note="How much is...? serve para tip, check ou total."),
  dict(title="Escolher a porcentagem", frame="Okay. {num} percent, then.", slots=[dict(key="num", opts=["Twenty", "Eighteen", "Fifteen"])], model="Okay. Twenty percent, then.", note="Percent vem depois do número. 'Then' fecha a decisão."),
  dict(title="Escrever um agradecimento", frame="Thank you! The {what} was {adj}.", slots=[dict(key="what", opts=["food", "service", "meal"]), dict(key="adj", opts=["great", "excellent", "really good"])], model="Thank you! The food was great.", note="Elogie com The + coisa + was + adjetivo."),
 ],
 sounds=[
  dict(say="How was everything?", tag="ligação: how was", tip="How was soa 'haowaz'. Una as palavras e acentue EV-ry-thing."),
  dict(say="Fifteen to twenty percent.", tag="ritmo: fifteen / twenty", tip="Em fifteen o acento está em -TEEN; em twenty, em TWEN. To fica fraco: 'fifTEEN-ta-TWEN-ty'."),
  dict(say="Have a lovely night!", tag="ligação: have a", tip="Have a vira 'hava'. Acentue LOVE-ly e NIGHT."),
 ],
 role=dict(turns=[
  dict(npc="How was everything?", opts=[
   dict(en="Great, thank you!", pt="Ótimo, obrigado!", reply="I'm glad you liked it."),
   dict(en="Delicious, thanks!", pt="Delicioso, valeu!", reply="Wonderful! I'll tell the cook."),
   dict(en="Really good. Thank you!", pt="Muito bom. Obrigado!", reply="That's great to hear.")]),
  dict(npc="Here's your check.", opts=[
   dict(en="Thanks. How much is the tip?", pt="Valeu. Quanto é a gorjeta?", reply="Fifteen to twenty percent."),
   dict(en="Thank you. What is the usual tip?", pt="Obrigado. Qual é a gorjeta comum?", reply="Usually fifteen to twenty percent."),
   dict(en="Thanks. Is service included?", pt="Valeu. O serviço está incluído?", reply="No, it's not. Fifteen to twenty percent is usual.")]),
  dict(npc="Fifteen to twenty percent.", opts=[
   dict(en="Okay. Twenty percent, then.", pt="Ok. Vinte por cento, então.", reply="That's very kind of you."),
   dict(en="Okay. Eighteen percent, then.", pt="Ok. Dezoito por cento, então.", reply="Thank you so much."),
   dict(en="Okay. Fifteen percent, then.", pt="Ok. Quinze por cento, então.", reply="Thank you. Have a nice night.")]),
  dict(npc="You're so kind. Thank you!", opts=[
   dict(en="Have a great night!", pt="Tenha uma ótima noite!", reply="Have a lovely night!"),
   dict(en="You're welcome. Good night!", pt="De nada. Boa noite!", reply="Good night! Come again."),
   dict(en="No problem. Have a good night!", pt="Sem problema. Tenha uma boa noite!", reply="You too!")]),
 ], change=["O serviço foi ruim: decida a gorjeta e explique com educação.", "Você está num café com balcão: pergunte se há pote de gorjeta.", "Você viaja e não sabe os costumes: pergunte se o serviço está incluído."]),
 writing=dict(task="Você jantou num restaurante nos EUA. Escreva 2 ou 3 frases: elogie o serviço, pergunte da gorjeta e diga quanto vai deixar.", model="Thank you! The service was great. How much is the tip? I'll leave twenty percent.", kw=["service", "tip", "percent", "thank"], checks=["Elogiou o serviço ou a comida.", "Perguntou ou falou da tip.", "Disse uma porcentagem."]),
 scenes=dict(pool=["diner", "restaurant", "counter", "lobby"], npc=dict(g="m", role="waiter"), you=dict(g="f")),
 convo=dict(npc=dict(name="Cole"), story="Você acabou de jantar. O garçom traz a conta e você decide a gorjeta.", turns=[
  dict(npc="How was everything?", pt="Como estava tudo?", opts=[
   dict(en="Great, thank you!", pt="Ótimo, obrigado!", ok=True, fb="Elogia e agradece."),
   dict(en="Yes, it was Tuesday.", pt="Sim, era terça-feira.", ok=False, fb="Ele pergunta sobre a refeição, não o dia."),
   dict(en="Here's your check.", pt="Aqui está a conta.", ok=False, fb="Quem traz a conta é o garçom.")]),
  dict(npc="Here's your check.", pt="Aqui está a conta.", opts=[
   dict(en="Great, thank you!", pt="Ótimo, obrigado!", ok=False, fb="Você já elogiou; agora há uma dúvida prática."),
   dict(en="Thanks. How much is the tip?", pt="Valeu. Quanto é a gorjeta?", ok=True, fb="Boa pergunta quando se está em outro país."),
   dict(en="How was everything?", pt="Como estava tudo?", ok=False, fb="Essa pergunta é do garçom.")]),
  dict(npc="Fifteen to twenty percent.", pt="De quinze a vinte por cento.", opts=[
   dict(en="Okay. Twenty percent, then.", pt="Ok. Vinte por cento, então.", ok=True, fb="Escolhe um valor dentro da faixa."),
   dict(en="Fifteen to twenty dollars.", pt="De quinze a vinte dólares.", ok=False, fb="Ele falou em porcentagem, não em dólares."),
   dict(en="Have a lovely night!", pt="Tenha uma linda noite!", ok=False, fb="É cedo para se despedir; falta decidir a gorjeta.")]),
  dict(npc="You're so kind. Thank you!", pt="Você é muito gentil. Obrigada!", opts=[
   dict(en="How much is the tip?", pt="Quanto é a gorjeta?", ok=False, fb="Isso já foi resolvido."),
   dict(en="Have a great night!", pt="Tenha uma ótima noite!", ok=True, fb="Resposta simpática."),
   dict(en="You're so kind, too.", pt="Você também é muito gentil.", ok=False, fb="Soa estranho aqui; é melhor desejar uma boa noite.")]),
  dict(npc="Have a lovely night!", pt="Tenha uma linda noite!", opts=[
   dict(en="Thank you, you too!", pt="Obrigado, você também!", ok=True, fb="Retribui o desejo."),
   dict(en="Here's your check.", pt="Aqui está a conta.", ok=False, fb="A conta já foi paga."),
   dict(en="Fifteen percent, please.", pt="Quinze por cento, por favor.", ok=False, fb="A gorjeta já foi decidida.")]),
 ]),
)
