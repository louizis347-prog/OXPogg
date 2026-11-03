X = dict(
 key=dict(big="How long to the beach?", label="Perguntar o tempo da viagem", sub="Pergunte quanto tempo leva, compare com e sem trânsito e proponha outro caminho."),
 mini=[
  dict(who="Marco", en="Are you ready to {go|leave|start}?", pt="Você está pronto para {ir|sair|começar}?"),
  dict(who="You", en="Yes. How long to the {beach|airport|hotel}?", pt="Sim. Quanto tempo até {a praia|o aeroporto|o hotel}?"),
  dict(who="Marco", en="Without traffic, {thirty|twenty|forty} minutes.", pt="Sem trânsito, {trinta|vinte|quarenta} minutos."),
  dict(who="You", en="And {with traffic?|at rush hour?|on Friday?}", pt="E {com trânsito?|na hora do rush?|na sexta?}"),
 ],
 dlg=[
  dict(who="Marco", en="Are you {ready|set} to go?", pt="Você está {pronto|preparado} para ir?"),
  dict(who="You", en="Yes. How long to the {beach?|pier?}", pt="Sim. Quanto tempo até {a praia?|o píer?}"),
  dict(who="Marco", en="Without traffic, {thirty|twenty} minutes.", pt="Sem trânsito, {trinta|vinte} minutos."),
  dict(who="You", en="And with {traffic?|rush hour?}", pt="E com {trânsito?|hora do rush?}"),
  dict(who="Marco", en="Maybe {two|three} hours!", pt="Talvez {duas|três} horas!"),
  dict(who="You", en="Wow. Is it {always|often} like this?", pt="Uau. É {sempre|muitas vezes} assim?"),
  dict(who="Marco", en="Almost always, on the {freeway.|highway.}", pt="Quase sempre, na {rodovia.|estrada.}"),
  dict(who="You", en="Should we take the side {streets?|roads?}", pt="Devemos pegar as {ruas laterais?|estradas pequenas?}"),
  dict(who="Marco", en="Good {idea.|call.} Let me check the app.", pt="{Boa ideia.|Boa escolha.} Vou ver o aplicativo."),
 ],
 vocab=[
  dict(w="freeway", pt="rodovia urbana", e="🛣️", ex=["The freeway is full.", "We take the freeway to the beach."]),
  dict(w="detour", pt="desvio", e="🔀", ex=["There is a detour on Main Street.", "Take the detour, please."]),
  dict(w="commute", pt="trajeto diário (casa-trabalho)", e="🚗", ex=["My commute is one hour.", "Her commute is short."]),
  dict(w="ramp", pt="rampa de acesso", e="🚧", ex=["Take the ramp on the right.", "The ramp is near the bridge."]),
  dict(w="jam", pt="engarrafamento", e="🚙", ex=["There is a big jam today.", "We are in a traffic jam."]),
  dict(w="shortcut", pt="atalho", e="↪️", ex=["Marco knows a shortcut.", "This shortcut saves time."]),
 ],
 molds=[
  dict(title="Perguntar o tempo", frame="How long to the {place}?", slots=[dict(key="place", opts=["beach", "airport", "hotel", "station"])], model="How long to the beach?", note="How long to + lugar pergunta quanto tempo leva ir até lá."),
  dict(title="Comparar o trânsito", frame="Without traffic, {time} minutes. With traffic, maybe {hours} hours.", slots=[dict(key="time", opts=["twenty", "thirty", "forty"]), dict(key="hours", opts=["two", "three", "four"])], model="Without traffic, twenty minutes. With traffic, maybe two hours.", note="Without traffic = sem trânsito; with traffic = com trânsito. Sem artigo."),
  dict(title="Escrever a sugestão", frame="Wow. Is it always like this on the {road}? Should we take the {other}?", slots=[dict(key="road", opts=["freeway", "highway", "bridge"]), dict(key="other", opts=["side streets", "bus", "train"])], model="Wow. Is it always like this on the freeway? Should we take the side streets?", note="Should we + verbo base faz uma sugestão."),
 ],
 sounds=[
  dict(say="How long to the beach?", tag="ritmo: HOW LONG to the BEACH", tip="Acentue HOW, LONG e BEACH. 'To the' fica fraco e rápido: 'tuh-thuh'."),
  dict(say="Maybe two hours!", tag="ritmo: MAY-be TWO HOURS", tip="Acentue MAY, TWO e HOURS; 'be' é curto e fraco."),
  dict(say="Almost always, on the freeway.", tag="ritmo: AL-most AL-ways, FREE-way", tip="Acentue AL, AL e FREE. Faça uma pequena pausa na vírgula."),
 ],
 role=dict(turns=[
  dict(npc="Are you ready to go?", opts=[
   dict(en="Yes. How long to the beach?", pt="Sim. Quanto tempo até a praia?", reply="Without traffic, thirty minutes."),
   dict(en="Yes. How long is the drive?", pt="Sim. Quanto tempo de carro?", reply="Without traffic, thirty minutes."),
   dict(en="Almost. How far is the beach?", pt="Quase. A que distância fica a praia?", reply="About twenty miles. Without traffic, thirty minutes.")]),
  dict(npc="Without traffic, thirty minutes.", opts=[
   dict(en="And with traffic?", pt="E com trânsito?", reply="Maybe two hours!"),
   dict(en="What about with traffic?", pt="E se tiver trânsito?", reply="Maybe two hours!"),
   dict(en="And at rush hour?", pt="E na hora do rush?", reply="Maybe two hours!")]),
  dict(npc="Maybe two hours!", opts=[
   dict(en="Wow. Is it always like this?", pt="Uau. Sempre é assim?", reply="Almost always, on the freeway."),
   dict(en="Really? Is it like this every day?", pt="Sério? É assim todo dia?", reply="Almost every day, on the freeway."),
   dict(en="Oh no. Is there an accident?", pt="Ah, não. Tem um acidente?", reply="Maybe. It's always busy on the freeway.")]),
  dict(npc="It's always busy on the freeway.", opts=[
   dict(en="Should we take the side streets?", pt="Devemos pegar as ruas laterais?", reply="Good idea. Let me check the app."),
   dict(en="Can we take another road?", pt="Podemos pegar outro caminho?", reply="Good idea. Let me check the app."),
   dict(en="Is there a shortcut?", pt="Existe um atalho?", reply="Good question. Let me check the app.")]),
 ], change=["O aplicativo mostra um acidente: sugira esperar um pouco.", "Marco quer ir de ônibus: pergunte quanto tempo leva.", "O trânsito acabou: comente que hoje é um dia bom."]),
 writing=dict(task="Você quer ir à praia em Los Angeles. Escreva 2 ou 3 frases: pergunte quanto tempo leva e sugira outro caminho.", model="How long to the beach? Is it always like this? Should we take the side streets?", kw=["how", "long", "beach", "traffic"], checks=["Perguntou quanto tempo leva.", "Falou do trânsito.", "Sugeriu outro caminho."]),
 scenes=dict(pool=["street", "busstop", "station", "pier", "beach"], npc=dict(g="m", role="friend"), you=dict(g="f")),
 convo=dict(npc=dict(name="Marco"), story="Você está em Los Angeles com seu amigo Marco. Vocês querem ir à praia.", turns=[
  dict(npc="Are you ready to go?", pt="Você está pronto para ir?", opts=[
   dict(en="Almost always, on the freeway.", pt="Quase sempre, na rodovia.", ok=False, fb="Isso é resposta do Marco."),
   dict(en="Yes. How long to the beach?", pt="Sim. Quanto tempo até a praia?", ok=True, fb="Responde e pergunta o tempo."),
   dict(en="Let me check the app.", pt="Vou ver o aplicativo.", ok=False, fb="Ainda não é hora disso.")]),
  dict(npc="Without traffic, thirty minutes.", pt="Sem trânsito, trinta minutos.", opts=[
   dict(en="Maybe two hours!", pt="Talvez duas horas!", ok=False, fb="Quem diz isso é o Marco."),
   dict(en="Yes. How long to the beach?", pt="Sim. Quanto tempo até a praia?", ok=False, fb="Você já perguntou isso."),
   dict(en="And with traffic?", pt="E com trânsito?", ok=True, fb="Compara com o caso do trânsito.")]),
  dict(npc="Maybe two hours!", pt="Talvez duas horas!", opts=[
   dict(en="Wow. Is it always like this?", pt="Uau. Sempre é assim?", ok=True, fb="Reação e pergunta naturais."),
   dict(en="Good idea. Let me check the app.", pt="Boa ideia. Vou ver o aplicativo.", ok=False, fb="Ninguém sugeriu nada ainda."),
   dict(en="Without traffic, thirty minutes.", pt="Sem trânsito, trinta minutos.", ok=False, fb="Marco já disse isso.")]),
  dict(npc="Almost always, on the freeway.", pt="Quase sempre, na rodovia.", opts=[
   dict(en="Are you ready to go?", pt="Você está pronto para ir?", ok=False, fb="Vocês já estão a caminho."),
   dict(en="Should we take the side streets?", pt="Devemos pegar as ruas laterais?", ok=True, fb="Sugere um caminho melhor."),
   dict(en="Maybe two hours!", pt="Talvez duas horas!", ok=False, fb="Não responde à situação.")]),
  dict(npc="Good idea. Let me check the app.", pt="Boa ideia. Vou ver o aplicativo.", opts=[
   dict(en="How long to the beach?", pt="Quanto tempo até a praia?", ok=False, fb="Você já perguntou."),
   dict(en="Thanks, Marco. Good call!", pt="Obrigado, Marco. Boa escolha!", ok=True, fb="Agradece de forma natural."),
   dict(en="Almost always, on the freeway.", pt="Quase sempre, na rodovia.", ok=False, fb="Não combina com a fala.")]),
 ]),
)
