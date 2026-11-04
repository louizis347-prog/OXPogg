X = dict(
 key=dict(big="A little loud", label="Pedir silêncio", sub="Bata na porta, comece com “Sorry to bother you” e diga o problema de forma suave. Frases curtas e calmas costumam resolver."),
 mini=[
  dict(who="You", en="Hi. Sorry to {bother you.|interrupt.|knock so late.}", pt="Oi. Desculpe {incomodar.|interromper.|bater tão tarde.}"),
  dict(who="Grace", en="No problem. What's {up?|wrong?}", pt="Sem problema. O que {houve?|aconteceu?}"),
  dict(who="You", en="The {TV|music|noise} is a little {loud.|high.}", pt="{A TV|A música|O barulho} está um pouco {alto.|alto.}"),
  dict(who="Grace", en="Oh, I'm sorry! I'll turn it {down.|off.|low.}", pt="Ah, desculpe! Vou {abaixar.|desligar.|baixar.}"),
 ],
 dlg=[
  dict(who="Grace", en="Hi. Sorry to {bother|disturb} you.", pt="Oi. Desculpe {incomodar.|incomodar.}"),
  dict(who="You", en="No problem. What's {up?|wrong?}", pt="Sem problema. O que {houve?|aconteceu?}"),
  dict(who="Grace", en="The {music|TV} is a little {loud.|high.}", pt="{A música|A TV} está um pouco {alta.|alta.}"),
  dict(who="You", en="Oh, I'm so {sorry!|sorry,} really!", pt="Ah, sinto {muito!|muito,} de verdade!"),
  dict(who="Grace", en="It's {late,|night,} and I have to {sleep.|rest.}", pt="É {tarde,|noite,} e preciso {dormir.|descansar.}"),
  dict(who="You", en="I understand. I'll turn it {down.|off.}", pt="Entendo. Vou {abaixar.|desligar.}"),
  dict(who="Grace", en="Thank you {very much.|so much.}", pt="Muito {obrigada.|obrigada.}"),
  dict(who="You", en="I didn't know it was so {loud.|high.}", pt="Eu não sabia que estava tão {alto.|alto.}"),
  dict(who="Grace", en="It's okay. It {happens.|is fine.}", pt="Tudo bem. {Acontece.|Está tudo bem.}"),
 ],
 vocab=[
  dict(w="sleep", pt="dormir", e="😴", ex=["I need to sleep.", "Sleep well tonight."]),
  dict(w="volume", pt="volume", e="🔊", ex=["Turn the volume down.", "The volume is high."]),
  dict(w="knock", pt="bater (na porta)", e="🚪", ex=["Please knock on the door.", "I hear a knock."]),
  dict(w="TV", pt="televisão", e="📺", ex=["The TV is on.", "Turn off the TV."]),
  dict(w="bother", pt="incomodar", e="🙇", ex=["Sorry to bother you.", "Does it bother you?"]),
  dict(w="shout", pt="gritar", e="📢", ex=["Please do not shout.", "Kids shout in the hall."]),
 ],
 molds=[
  dict(title="Dizer o problema", frame="The {thing} is a little {problem}.", slots=[dict(key="thing", opts=["music", "TV", "noise"]), dict(key="problem", opts=["loud", "high", "late"])], model="The music is a little loud.", note="A little deixa a frase mais suave. Depois de is, use o adjetivo: loud."),
  dict(title="Dar o motivo", frame="It's late, and I have to {action}.", slots=[dict(key="action", opts=["sleep", "work", "study"])], model="It's late, and I have to sleep.", note="Have to + verbo mostra obrigação: preciso dormir."),
  dict(title="Escrever um bilhete", frame="Hi! Sorry to bother you. Could you turn the {thing} {direction}, please?", slots=[dict(key="thing", opts=["music", "TV", "volume"]), dict(key="direction", opts=["down", "off", "low"])], model="Hi! Sorry to bother you. Could you turn the music down, please?", note="Could you + verbo é um pedido educado. Turn down = abaixar."),
 ],
 sounds=[
  dict(say="Sorry to bother you.", tag="acento: SOrry, BOther", tip="As duas palavras fortes têm acento na primeira sílaba: SOR-ry, BO-ther. O th de bother é vozeado, com a língua entre os dentes."),
  dict(say="It's late, and I have to sleep.", tag="ritmo: late / have to / sleep", tip="Acentue LATE e SLEEP. Have to soa quase “hafta”: une as palavras."),
  dict(say="It's a little loud.", tag="ligação: it's a", tip="It's a vira “itsa”: ligue o s ao a, sem pausa."),
 ],
 role=dict(turns=[
  dict(npc="Hi. Who is it?", opts=[
   dict(en="Hi. Sorry to bother you.", pt="Oi. Desculpe incomodar.", reply="No problem. What's up?"),
   dict(en="Hi. I'm your neighbor in 3B.", pt="Oi. Sou seu vizinho do 3B.", reply="Oh, hi! What's up?"),
   dict(en="Hello. Sorry to knock so late.", pt="Olá. Desculpe bater tão tarde.", reply="No problem. What's up?")]),
  dict(npc="What's up?", opts=[
   dict(en="The music is a little loud.", pt="A música está um pouco alta.", reply="Oh, I'm so sorry!"),
   dict(en="The TV is a little loud.", pt="A TV está um pouco alta.", reply="Oh, I'm so sorry!"),
   dict(en="I can hear the music in my room.", pt="Escuto a música no meu quarto.", reply="Oh no, I'm sorry!")]),
  dict(npc="Oh, I'm so sorry!", opts=[
   dict(en="It's late, and I have to sleep.", pt="É tarde e preciso dormir.", reply="I understand. I'll turn it down."),
   dict(en="It's late, and I work early.", pt="É tarde e trabalho cedo.", reply="I understand. I'll turn it down."),
   dict(en="Could you turn it down, please?", pt="Pode abaixar, por favor?", reply="Of course. I'll turn it down.")]),
  dict(npc="I'll turn it down.", opts=[
   dict(en="Thank you very much.", pt="Muito obrigado.", reply="I didn't know it was so loud."),
   dict(en="Thanks. I appreciate it.", pt="Valeu. Agradeço.", reply="Sure. It happens."),
   dict(en="Thank you. Sleep tight!", pt="Obrigado. Durma bem!", reply="You too!")]),
 ], change=["O vizinho não abre a porta: deixe um bilhete curto.", "A música continua alta depois de dez minutos: bata de novo, com educação.", "O vizinho diz que está em uma festa de aniversário: peça só para abaixar um pouco."]),
 writing=dict(task="Escreva um bilhete de 2 ou 3 frases para o vizinho: peça desculpa por incomodar, diga que a música está alta e peça para abaixar.", model="Hi! Sorry to bother you. The music is a little loud, and I have to sleep. Could you turn it down, please?", kw=["sorry", "music", "loud", "sleep"], checks=["Começou com educação.", "Disse qual é o problema.", "Pediu para abaixar."]),
 scenes=dict(pool=["lobby", "lobby1", "hall", "living"], npc=dict(g="f", role="neighbor"), you=dict(g="m")),
 convo=dict(npc=dict(name="Grace"), story="Você mora em um prédio em Boston. É tarde e a música da Grace, sua vizinha, está alta. Você bate na porta dela.", turns=[
  dict(npc="Hi. Who is it?", pt="Oi. Quem é?", opts=[
   dict(en="Hi. Sorry to bother you.", pt="Oi. Desculpe incomodar.", ok=True, fb="Início educado."),
   dict(en="It happens. It's okay.", pt="Acontece. Tudo bem.", ok=False, fb="Essa resposta vem depois de um pedido de desculpa."),
   dict(en="I'll turn it down.", pt="Vou abaixar.", ok=False, fb="Quem abaixa o som é ela, não você.")]),
  dict(npc="No problem. What's up?", pt="Sem problema. O que houve?", opts=[
   dict(en="Thank you very much.", pt="Muito obrigado.", ok=False, fb="Ainda não há o que agradecer."),
   dict(en="The music is a little loud.", pt="A música está um pouco alta.", ok=True, fb="Diz o problema com suavidade."),
   dict(en="Oh, I'm so sorry!", pt="Ah, sinto muito!", ok=False, fb="Quem pede desculpa é a Grace.")]),
  dict(npc="Oh, I'm so sorry!", pt="Ah, sinto muito!", opts=[
   dict(en="No problem. What's up?", pt="Sem problema. O que houve?", ok=False, fb="Você já disse o problema."),
   dict(en="I understand. I'll turn it down.", pt="Entendo. Vou abaixar.", ok=False, fb="Quem diz isso é a Grace."),
   dict(en="It's late, and I have to sleep.", pt="É tarde e preciso dormir.", ok=True, fb="Dá o motivo.")]),
  dict(npc="I understand. I'll turn it down.", pt="Entendo. Vou abaixar.", opts=[
   dict(en="Thank you very much.", pt="Muito obrigado.", ok=True, fb="Agradecimento simples."),
   dict(en="Sorry to bother you.", pt="Desculpe incomodar.", ok=False, fb="Você já falou isso."),
   dict(en="It's a little loud.", pt="Está um pouco alto.", ok=False, fb="Ela já concordou.")]),
  dict(npc="I didn't know it was so loud.", pt="Eu não sabia que estava tão alto.", opts=[
   dict(en="I'll turn it down.", pt="Vou abaixar.", ok=False, fb="Esse é o papel dela."),
   dict(en="Oh, I'm so sorry!", pt="Ah, sinto muito!", ok=False, fb="Ela é quem pede desculpas."),
   dict(en="It's okay. It happens.", pt="Tudo bem. Acontece.", ok=True, fb="Resposta gentil.")]),
 ]),
)
