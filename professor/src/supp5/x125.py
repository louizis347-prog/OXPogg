X = dict(
 key=dict(big="I have a sore throat", label="Falar do problema", sub="Diga ao médico o que dói, há quanto tempo e se você tem febre."),
 mini=[
  dict(who="Mei", en="Hello. Please sit down. What's the {problem?|matter?|trouble?}", pt="Olá. Sente-se, por favor. Qual é o {problema?|problema?|problema?}"),
  dict(who="You", en="I have a sore {throat|ear|stomach}.", pt="Estou com dor de {garganta|ouvido|barriga}."),
  dict(who="Mei", en="How long do you have {it?|them?|the pain?}", pt="Há quanto tempo você {tem isso?|tem isso?|sente a dor?}"),
  dict(who="You", en="Since {Monday.|yesterday.|last night.}", pt="Desde {segunda.|ontem.|ontem à noite.}"),
 ],
 dlg=[
  dict(who="Mei", en="Hello. Please {sit down.|come in.}", pt="Olá. Por favor, {sente-se.|entre.}"),
  dict(who="You", en="Thank you, {doctor.|Dr. Mei.}", pt="Obrigado, {doutora.|Dra. Mei.}"),
  dict(who="Mei", en="What's the {problem?|matter?}", pt="Qual é o {problema?|problema?}"),
  dict(who="You", en="I have a sore {throat|ear} and a {cough.|fever.}", pt="Estou com dor de {garganta|ouvido} e {tosse.|febre.}"),
  dict(who="Mei", en="How long do you have {them?|it?}", pt="Há quanto tempo {você tem isso?|você tem isso?}"),
  dict(who="You", en="Since {Monday.|Friday.} {Three|Two} days.", pt="Desde {segunda.|sexta.} {Três|Dois} dias."),
  dict(who="Mei", en="Do you have a {fever?|headache?}", pt="Você tem {febre?|dor de cabeça?}"),
  dict(who="You", en="No, I {don't.|do not.}", pt="Não, {não tenho.|não tenho.}"),
  dict(who="Mei", en="Open your {mouth,|ears,} please. Say \"ah.\"", pt="Abra {a boca,|os ouvidos,} por favor. Diga \"ah\"."),
 ],
 vocab=[
  dict(w="patient", pt="paciente", e="🧑‍🦽", ex=["The patient is nervous.", "I am a new patient."]),
  dict(w="chest", pt="peito", e="🫁", ex=["My chest hurts.", "Take a deep breath, chest up."]),
  dict(w="ear", pt="ouvido / orelha", e="👂", ex=["My ear hurts.", "Look in my ear."]),
  dict(w="nose", pt="nariz", e="👃", ex=["My nose is red.", "Blow your nose."]),
  dict(w="waiting room", pt="sala de espera", e="🪑", ex=["Wait in the waiting room.", "The waiting room is quiet."]),
  dict(w="temperature", pt="temperatura", e="🌡️", ex=["Your temperature is normal.", "Check my temperature."]),
 ],
 molds=[
  dict(title="Dizer o problema", frame="I have a {a} and a {b}.", slots=[dict(key="a", opts=["sore throat", "headache", "fever"]), dict(key="b", opts=["cough", "runny nose", "stomachache"])], model="I have a sore throat and a cough.", note="Have a + sintoma. Sore throat = dor de garganta."),
  dict(title="Dizer desde quando", frame="Since {day}. {num} days.", slots=[dict(key="day", opts=["Monday", "Friday", "Sunday"]), dict(key="num", opts=["Three", "Two", "Four"])], model="Since Monday. Three days.", note="Since + dia de início. Depois diga o número de dias."),
  dict(title="Escrever ao consultório", frame="Hello. I have a {symptom}. Since {day}. I don't have a fever.", slots=[dict(key="symptom", opts=["cough", "sore throat", "headache"]), dict(key="day", opts=["Monday", "Friday", "Sunday"])], model="Hello. I have a cough. Since Monday. I don't have a fever.", note="Since + dia diz quando começou. Don't have a fever diz que não há febre."),
 ],
 sounds=[
  dict(say="I have a sore throat.", tag="ligação: have a", tip="Una have e a: 'ha-va'. Acentue SORE e THROAT; th é língua entre os dentes."),
  dict(say="Open your mouth.", tag="ligação: open your", tip="Soa 'openyer'. Acentue O e MOUTH; ou = 'au'."),
  dict(say="Since Monday.", tag="acento: SINCE MONday", tip="Acentue SINCE e MON; 'day' fica fraco e curto: 'dei' rápido."),
 ],
 role=dict(turns=[
  dict(npc="Hello. Please sit down. What's the problem?", opts=[
   dict(en="Thank you, doctor. I have a sore throat and a cough.", pt="Obrigado, doutora. Estou com dor de garganta e tosse.", reply="How long do you have them?"),
   dict(en="Thanks. My throat hurts and I cough.", pt="Obrigado. Minha garganta dói e eu tusso.", reply="How long do you have them?"),
   dict(en="Thank you. I have a sore throat.", pt="Obrigado. Estou com dor de garganta.", reply="How long do you have it?")]),
  dict(npc="How long do you have them?", opts=[
   dict(en="Since Monday. Three days.", pt="Desde segunda. Três dias.", reply="Do you have a fever?"),
   dict(en="Since Sunday. Four days.", pt="Desde domingo. Quatro dias.", reply="Do you have a fever?"),
   dict(en="Two days. Since Wednesday.", pt="Dois dias. Desde quarta.", reply="Do you have a fever?")]),
  dict(npc="Do you have a fever?", opts=[
   dict(en="No, I don't.", pt="Não, não tenho.", reply="Good. Open your mouth, please."),
   dict(en="No, I don't have a fever.", pt="Não, não tenho febre.", reply="Good. Open your mouth, please."),
   dict(en="No, but I feel hot.", pt="Não, mas sinto calor.", reply="OK. Open your mouth, please.")]),
  dict(npc="Open your mouth, please. Say \"ah.\"", opts=[
   dict(en="Ahhh.", pt="Aaah.", reply="Your throat is red."),
   dict(en="OK. Ahhh.", pt="Certo. Aaah.", reply="Your throat is red."),
   dict(en="Like this? Ahhh.", pt="Assim? Aaah.", reply="Yes. Your throat is red.")]),
 ], change=["A médica pergunta se você tem alergia: diga que não tem.", "Você também tem dor de ouvido: acrescente isso.", "Você não entendeu uma pergunta: peça para repetir, por favor."]),
 writing=dict(task="Escreva 2 ou 3 frases para a médica: diga o que dói, desde quando e que você não tem febre.", model="Hello, doctor. I have a sore throat and a cough. Since Monday. I don't have a fever.", kw=["sore", "throat", "since", "fever"], checks=["Disse o que dói.", "Disse desde quando.", "Disse que não tem febre."]),
 scenes=dict(pool=["clinic", "hall", "office", "counter"], npc=dict(g="f", role="doctor"), you=dict(g="m")),
 convo=dict(npc=dict(name="Mei"), story="Você está no consultório em Seattle. A Dra. Mei examina você.", turns=[
  dict(npc="Hello. Please sit down.", pt="Olá. Sente-se, por favor.", opts=[
   dict(en="Thank you, doctor.", pt="Obrigado, doutora.", ok=True, fb="Agradeça com educação."),
   dict(en="Since Monday.", pt="Desde segunda.", ok=False, fb="Ela ainda não perguntou isso."),
   dict(en="Open your mouth.", pt="Abra a boca.", ok=False, fb="É ela quem pede isso.")]),
  dict(npc="What's the problem?", pt="Qual é o problema?", opts=[
   dict(en="No, I don't.", pt="Não, não tenho.", ok=False, fb="Ela não perguntou sobre febre."),
   dict(en="Since Monday.", pt="Desde segunda.", ok=False, fb="Falta dizer o problema."),
   dict(en="I have a sore throat and a cough.", pt="Estou com dor de garganta e tosse.", ok=True, fb="Diga os sintomas.")]),
  dict(npc="How long do you have them?", pt="Há quanto tempo?", opts=[
   dict(en="Since Monday. Three days.", pt="Desde segunda. Três dias.", ok=True, fb="Dia de início e total."),
   dict(en="I have a cough.", pt="Estou com tosse.", ok=False, fb="Ela perguntou há quanto tempo."),
   dict(en="No, I don't.", pt="Não, não tenho.", ok=False, fb="Não responde ao tempo.")]),
  dict(npc="Do you have a fever?", pt="Você tem febre?", opts=[
   dict(en="Since Monday.", pt="Desde segunda.", ok=False, fb="Ela perguntou da febre."),
   dict(en="No, I don't.", pt="Não, não tenho.", ok=True, fb="Resposta curta."),
   dict(en="Thank you, doctor.", pt="Obrigado, doutora.", ok=False, fb="Não responde.")]),
  dict(npc="Open your mouth, please. Say \"ah.\"", pt="Abra a boca, por favor. Diga \"ah\".", opts=[
   dict(en="I have a cough.", pt="Estou com tosse.", ok=False, fb="Já disse. Agora faça o exame."),
   dict(en="OK. Ahhh.", pt="Certo. Aaah.", ok=True, fb="Abra a boca e diga ah."),
   dict(en="Please sit down.", pt="Sente-se, por favor.", ok=False, fb="Já estão sentados.")]),
 ]),
)
