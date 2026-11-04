X = dict(
 key=dict(big="I don't feel well", label="Não estou bem", sub="Diga que não se sente bem, o que dói e o que você precisa: água, descanso ou remédio."),
 mini=[
  dict(who="Claire", en="You look tired. Are you {OK?|sick?|cold?}", pt="Você parece cansado. Está {bem?|doente?|com frio?}"),
  dict(who="You", en="No, I don't feel well. I have a {headache|stomachache|fever}.", pt="Não, não me sinto bem. Estou com {dor de cabeça|dor de barriga|febre}."),
  dict(who="Claire", en="Do you want some {water?|tea?|soup?}", pt="Quer um pouco de {água?|chá?|sopa?}"),
  dict(who="You", en="Yes, please. I need to {rest|lie down|sleep}.", pt="Quero, por favor. Preciso {descansar|me deitar|dormir}."),
 ],
 dlg=[
  dict(who="Claire", en="Hi, Nell. You look {tired.|sick.} Are you {OK?|fine?}", pt="Oi, Nell. Você parece {cansada.|doente.} Está {bem?|bem?}"),
  dict(who="You", en="No, I don't feel {well.|good.} I have a {headache.|stomachache.}", pt="Não, não me sinto {bem.|bem.} Estou com {dor de cabeça.|dor de barriga.}"),
  dict(who="Claire", en="Oh no. Do you have a {fever?|cold?}", pt="Ah, não. Você está com {febre?|resfriado?}"),
  dict(who="You", en="No, but I feel {hot.|dizzy.}", pt="Não, mas me sinto {com calor.|tonta.}"),
  dict(who="Claire", en="Do you want some {water?|tea?}", pt="Quer um pouco de {água?|chá?}"),
  dict(who="You", en="Yes, please. And a {rest.|nap.}", pt="Quero, por favor. E um {descanso.|cochilo.}"),
  dict(who="Claire", en="Lie down on the {sofa.|bed.}", pt="Deite no {sofá.|na cama.}"),
  dict(who="You", en="Thanks. I'll take a {nap.|rest.}", pt="Valeu. Vou tirar uma {soneca.|descansada.}"),
  dict(who="Claire", en="Do you need {medicine?|a pill?}", pt="Precisa de {remédio?|um comprimido?}"),
 ],
 vocab=[
  dict(w="sick", pt="doente", e="🤒", ex=["I feel sick today.", "My brother is sick."]),
  dict(w="nap", pt="soneca", e="😴", ex=["I take a nap at two.", "A short nap helps me."]),
  dict(w="sofa", pt="sofá", e="🛋️", ex=["Lie down on the sofa.", "The sofa is soft."]),
  dict(w="rest", pt="descansar / descanso", e="🛌", ex=["I need to rest.", "Rest is good for you."]),
  dict(w="pill", pt="comprimido", e="💊", ex=["Take one pill.", "The pill is small."]),
  dict(w="honey", pt="mel", e="🍯", ex=["Tea with honey is nice.", "I like honey."]),
 ],
 molds=[
  dict(title="Dizer que não está bem", frame="I don't feel {adj}. I have a {pain}.", slots=[dict(key="adj", opts=["well", "good", "great"]), dict(key="pain", opts=["headache", "stomachache", "fever"])], model="I don't feel well. I have a headache.", note="Com dor, use have a + palavra. Não diga I am headache."),
  dict(title="Oferecer ajuda", frame="Do you want some {thing}?", slots=[dict(key="thing", opts=["water", "tea", "soup", "honey"])], model="Do you want some water?", note="Some é usado em ofertas com coisas que não se contam bem: water, tea, soup."),
  dict(title="Escrever o que precisa", frame="I feel {adj}. I'm going to {action} on the {place}.", slots=[dict(key="adj", opts=["tired", "sick", "hot"]), dict(key="action", opts=["rest", "lie down", "take a nap"]), dict(key="place", opts=["sofa", "bed", "couch"])], model="I feel tired. I'm going to rest on the sofa.", note="I'm going to + verbo conta o plano. On the sofa/bed diz onde."),
 ],
 sounds=[
  dict(say="I don't feel well.", tag="ritmo: I DON'T FEEL WELL", tip="Acentue DON'T, FEEL e WELL. O 'I' fica curto. O t de don't é suave."),
  dict(say="Do you have a fever?", tag="ligação: have a", tip="Una have e a: 'ha-va'. Acentue HA e FE; 'a' fica fraco."),
  dict(say="I'll take a nap.", tag="contração: I'll", tip="I'll soa 'ail'. Acentue TAKE e NAP; 'a' fica fraco."),
 ],
 role=dict(turns=[
  dict(npc="You look tired. Are you OK?", opts=[
   dict(en="No, I don't feel well. I have a headache.", pt="Não, não me sinto bem. Estou com dor de cabeça.", reply="Oh no. Do you have a fever?"),
   dict(en="Not really. I have a stomachache.", pt="Na verdade, não. Estou com dor de barriga.", reply="Oh no. Do you have a fever?"),
   dict(en="No, I feel sick.", pt="Não, me sinto mal.", reply="Oh no. Do you have a fever?")]),
  dict(npc="Do you have a fever?", opts=[
   dict(en="No, but I feel hot.", pt="Não, mas me sinto com calor.", reply="Do you want some water?"),
   dict(en="No, I don't.", pt="Não, não tenho.", reply="Do you want some water?"),
   dict(en="I think so. I feel hot.", pt="Acho que sim. Sinto calor.", reply="Do you want some water?")]),
  dict(npc="Do you want some water?", opts=[
   dict(en="Yes, please. And a rest.", pt="Quero, por favor. E um descanso.", reply="Lie down on the sofa."),
   dict(en="Yes, please. Thank you.", pt="Quero, por favor. Obrigado.", reply="Lie down on the sofa."),
   dict(en="Yes, and some tea, please.", pt="Quero, e um chá também, por favor.", reply="Lie down on the sofa.")]),
  dict(npc="Lie down on the sofa.", opts=[
   dict(en="Thanks. I'll take a nap.", pt="Valeu. Vou tirar uma soneca.", reply="Do you need medicine?"),
   dict(en="Thank you. I need to rest.", pt="Obrigado. Preciso descansar.", reply="Do you need medicine?"),
   dict(en="OK. I'll sleep a little.", pt="Certo. Vou dormir um pouco.", reply="Do you need medicine?")]),
 ], change=["Claire pergunta se você quer comer algo: diga que só quer água.", "Você está com dor de barriga, não de cabeça: diga isso.", "Claire quer ligar para o médico: diga que primeiro vai descansar."]),
 writing=dict(task="Escreva 2 ou 3 frases para uma amiga: diga que você não se sente bem, o que dói e que vai descansar.", model="Hi Claire. I don't feel well. I have a headache. I'm going to rest.", kw=["feel", "headache", "rest", "well"], checks=["Disse que não se sente bem.", "Disse o que dói.", "Disse que vai descansar."]),
 scenes=dict(pool=["living", "home1", "bedroom", "kitchen"], npc=dict(g="f", role="friend"), you=dict(g="f")),
 convo=dict(npc=dict(name="Claire"), story="Você está na casa da sua amiga Claire e não se sente bem.", turns=[
  dict(npc="You look tired. Are you OK?", pt="Você parece cansada. Está bem?", opts=[
   dict(en="No, I don't feel well. I have a headache.", pt="Não, não me sinto bem. Estou com dor de cabeça.", ok=True, fb="Diga como se sente e o que dói."),
   dict(en="Thanks. I'll take a nap.", pt="Valeu. Vou tirar uma soneca.", ok=False, fb="Ainda é cedo para isso."),
   dict(en="Do you need medicine?", pt="Você precisa de remédio?", ok=False, fb="Quem está mal é você.")]),
  dict(npc="Oh no. Do you have a fever?", pt="Ah, não. Você está com febre?", opts=[
   dict(en="Yes, please. And a rest.", pt="Quero, por favor. E um descanso.", ok=False, fb="Não responde sobre febre."),
   dict(en="No, but I feel hot.", pt="Não, mas sinto calor.", ok=True, fb="Responda e acrescente."),
   dict(en="Lie down on the sofa.", pt="Deite no sofá.", ok=False, fb="É a fala dela.")]),
  dict(npc="Do you want some water?", pt="Quer um pouco de água?", opts=[
   dict(en="Yes, please. And a rest.", pt="Quero, por favor. E um descanso.", ok=True, fb="Aceite com please."),
   dict(en="No, but I feel hot.", pt="Não, mas sinto calor.", ok=False, fb="Ela perguntou da água."),
   dict(en="Do you have a fever?", pt="Você tem febre?", ok=False, fb="Ela é quem pergunta isso.")]),
  dict(npc="Lie down on the sofa.", pt="Deite no sofá.", opts=[
   dict(en="Do you want some water?", pt="Quer um pouco de água?", ok=False, fb="Já ofereceram água."),
   dict(en="Thanks. I'll take a nap.", pt="Valeu. Vou tirar uma soneca.", ok=True, fb="Agradeça e diga o que vai fazer."),
   dict(en="I have a headache.", pt="Estou com dor de cabeça.", ok=False, fb="Você já disse isso.")]),
  dict(npc="Do you need medicine?", pt="Precisa de remédio?", opts=[
   dict(en="Yes, a pill, please. Thank you, Claire.", pt="Sim, um comprimido, por favor. Obrigada, Claire.", ok=True, fb="Responda e agradeça."),
   dict(en="Lie down on the sofa.", pt="Deite no sofá.", ok=False, fb="Ela já mandou você deitar."),
   dict(en="You look tired.", pt="Você parece cansada.", ok=False, fb="Não responde ao pedido.")]),
 ]),
)
