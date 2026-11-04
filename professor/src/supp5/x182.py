X = dict(
 key=dict(big="The power is out", label="Acabou a luz", sub="Diga o que aconteceu, veja se é só o seu prédio e procure a lanterna. Frases curtas ajudam a manter a calma."),
 mini=[
  dict(who="Rosa", en="Oh no! {The lights went out.|The power went out.|The TV went off.}", pt="Ai, não! {As luzes apagaram.|A energia acabou.|A TV desligou.}"),
  dict(who="You", en="Is it only our {building?|street?|house?}", pt="É só {o nosso prédio?|a nossa rua?|a nossa casa?}"),
  dict(who="Rosa", en="Do we have a {flashlight?|candle?|match?}", pt="Temos {uma lanterna?|uma vela?|um fósforo?}"),
  dict(who="You", en="Yes, in the {kitchen drawer.|bedroom closet.}", pt="Sim, {na gaveta da cozinha.|no armário do quarto.}"),
 ],
 dlg=[
  dict(who="Rosa", en="Oh no! {The lights went out.|The power went out.}", pt="Ai, não! {As luzes apagaram.|A energia acabou.}"),
  dict(who="You", en="Is it only our {building?|house?}", pt="É só {o nosso prédio?|a nossa casa?}"),
  dict(who="Rosa", en="Let me check {outside.|upstairs.} No, the whole {street.|city.}", pt="Vou ver {lá fora.|lá em cima.} Não, {a rua toda.|a cidade toda.}"),
  dict(who="You", en="There's a {storm|big storm} tonight.", pt="Tem {tempestade|uma grande tempestade} hoje à noite."),
  dict(who="Rosa", en="Do we have a {flashlight?|candle?}", pt="Temos {uma lanterna?|uma vela?}"),
  dict(who="You", en="Yes, in the kitchen {drawer.|closet.}", pt="Sim, {na gaveta da cozinha.|no armário da cozinha.}"),
  dict(who="Rosa", en="I found it. It {works!|is bright!}", pt="Achei. {Funciona!|Está forte!}"),
  dict(who="You", en="Let's light some {candles,|matches,} too.", pt="Vamos acender {velas,|fósforos,} também."),
  dict(who="Rosa", en="Should we call the {power|electric} company?", pt="Devemos ligar para a companhia de {energia?|eletricidade?}"),
 ],
 vocab=[
  dict(w="power", pt="energia, eletricidade", e="⚡", ex=["The power is out.", "The power is back."]),
  dict(w="storm", pt="tempestade", e="⛈️", ex=["There is a big storm.", "The storm is loud."]),
  dict(w="wire", pt="fio", e="🔌", ex=["The wire is red.", "Do not touch the wire."]),
  dict(w="switch", pt="interruptor", e="🔘", ex=["Press the switch.", "The switch is on the wall."]),
  dict(w="match", pt="fósforo", e="🔥", ex=["I have a match.", "Use a match for the candle."]),
  dict(w="thunder", pt="trovão", e="🌩️", ex=["I hear thunder.", "The thunder is loud."]),
 ],
 molds=[
  dict(title="Dizer o que aconteceu", frame="The {thing} went out. Is it only our {place}?", slots=[dict(key="thing", opts=["lights", "power", "TV"]), dict(key="place", opts=["building", "house", "street"])], model="The lights went out. Is it only our building?", note="Went out = apagou. A segunda frase é uma pergunta sim/não."),
  dict(title="Perguntar e dizer onde está", frame="Do we have a {item}? Yes, in the {place}.", slots=[dict(key="item", opts=["flashlight", "candle", "match"]), dict(key="place", opts=["kitchen", "drawer", "closet"])], model="Do we have a flashlight? Yes, in the kitchen.", note="Do we have…? pergunta se existe. In + lugar diz onde está."),
  dict(title="Escrever uma mensagem", frame="Hi! The power is out. I {action} the {thing}, and it {result}.", slots=[dict(key="action", opts=["found", "checked", "closed"]), dict(key="thing", opts=["flashlight", "fridge", "window"]), dict(key="result", opts=["works", "is okay", "is safe"])], model="Hi! The power is out. I found the flashlight, and it works.", note="Found, checked e closed estão no passado. Mantenha frases curtas."),
 ],
 sounds=[
  dict(say="The lights went out.", tag="ligação: went out", tip="Went out soa “wentout”: ligue o t final ao o seguinte, sem pausa."),
  dict(say="Do we have a flashlight?", tag="ritmo: FLASHlight", tip="Flashlight tem acento na primeira parte: FLASH-light. Do we have fica leve e rápido."),
  dict(say="I found it. It works!", tag="ligação: found it", tip="Found it soa “foundit”: o d passa para o it, sem parar."),
 ],
 role=dict(turns=[
  dict(npc="Oh no! The lights went out.", opts=[
   dict(en="Is it only our building?", pt="É só o nosso prédio?", reply="Let me check outside. No, the whole street."),
   dict(en="Is it only our floor?", pt="É só o nosso andar?", reply="Let me check. No, the whole building."),
   dict(en="Is it the whole street?", pt="É a rua toda?", reply="Let me check outside. Yes, it is.")]),
  dict(npc="The whole street.", opts=[
   dict(en="There's a storm tonight.", pt="Tem tempestade hoje à noite.", reply="Yes, I hear the thunder."),
   dict(en="Do we have a flashlight?", pt="Temos uma lanterna?", reply="I think so. Where is it?"),
   dict(en="Stay calm. Let's look for a light.", pt="Calma. Vamos procurar uma luz.", reply="Okay. Do we have a flashlight?")]),
  dict(npc="Do we have a flashlight?", opts=[
   dict(en="Yes, in the kitchen drawer.", pt="Sim, na gaveta da cozinha.", reply="I found it. It works!"),
   dict(en="Yes, in the bedroom closet.", pt="Sim, no armário do quarto.", reply="I found it. It works!"),
   dict(en="I think it's in the drawer.", pt="Acho que está na gaveta.", reply="I found it. It works!")]),
  dict(npc="I found it. It works!", opts=[
   dict(en="Let's light some candles, too.", pt="Vamos acender velas também.", reply="Good idea. Should we call the power company?"),
   dict(en="Great! Keep the fridge closed.", pt="Ótimo! Mantenha a geladeira fechada.", reply="Good idea. Should we call the power company?"),
   dict(en="Great! Let's call the power company.", pt="Ótimo! Vamos ligar para a companhia de energia.", reply="That sounds good.")]),
 ], change=["A lanterna não funciona: veja se a pilha está certa ou procure outra luz.", "Você não acha fósforos: peça para o amigo procurar na cozinha.", "A luz volta depois de uma hora: diga que está tudo de volta ao normal."]),
 writing=dict(task="A luz acabou na sua casa. Escreva 2 ou 3 frases para um amigo: diga o que aconteceu, que há tempestade e que você achou a lanterna.", model="The power is out. There is a storm tonight. I found the flashlight, and it works.", kw=["power", "storm", "flashlight", "works"], checks=["Disse que a luz acabou.", "Mencionou a tempestade.", "Falou da lanterna."]),
 scenes=dict(pool=["living", "kitchen", "home1", "nightcity"], npc=dict(g="f", role="friend"), you=dict(g="m")),
 convo=dict(npc=dict(name="Rosa"), story="Você está em casa, em Houston, com a Rosa. Há uma tempestade e a luz acaba.", turns=[
  dict(npc="Oh no! The lights went out.", pt="Ai, não! As luzes apagaram.", opts=[
   dict(en="Is it only our building?", pt="É só o nosso prédio?", ok=True, fb="Pergunta natural depois do apagão."),
   dict(en="It works!", pt="Funciona!", ok=False, fb="Isso se diz quando a lanterna funciona."),
   dict(en="Yes, in the kitchen drawer.", pt="Sim, na gaveta da cozinha.", ok=False, fb="Ninguém perguntou onde está algo.")]),
  dict(npc="Let me check outside. No, the whole street.", pt="Vou ver lá fora. Não, a rua toda.", opts=[
   dict(en="Is it only our building?", pt="É só o nosso prédio?", ok=False, fb="Ela já respondeu isso."),
   dict(en="There's a storm tonight.", pt="Tem tempestade hoje à noite.", ok=True, fb="Dá o motivo provável."),
   dict(en="Let's light some candles.", pt="Vamos acender velas.", ok=False, fb="Ainda é cedo; primeiro falem da causa.")]),
  dict(npc="Do we have a flashlight?", pt="Temos uma lanterna?", opts=[
   dict(en="Yes, in the kitchen drawer.", pt="Sim, na gaveta da cozinha.", ok=True, fb="Responde com o lugar."),
   dict(en="I found it.", pt="Achei.", ok=False, fb="Quem acha é a Rosa, depois."),
   dict(en="Should we call the company?", pt="Devemos ligar para a companhia?", ok=False, fb="Primeiro responda à pergunta.")]),
  dict(npc="I found it. It works!", pt="Achei. Funciona!", opts=[
   dict(en="Do we have a flashlight?", pt="Temos uma lanterna?", ok=False, fb="Ela já achou."),
   dict(en="Let's light some candles, too.", pt="Vamos acender velas também.", ok=True, fb="Sugestão com Let's."),
   dict(en="The whole street.", pt="A rua toda.", ok=False, fb="Isso já foi dito.")]),
  dict(npc="Should we call the power company?", pt="Devemos ligar para a companhia de energia?", opts=[
   dict(en="Yes, in the drawer.", pt="Sim, na gaveta.", ok=False, fb="A resposta não encaixa na pergunta."),
   dict(en="Let's light some candles.", pt="Vamos acender velas.", ok=False, fb="Já falamos disso."),
   dict(en="That sounds good.", pt="Parece bom.", ok=True, fb="Concordar de forma simples.")]),
 ]),
)
