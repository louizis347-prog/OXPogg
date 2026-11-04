X = dict(
 key=dict(big="Is this your first time?", label="Primeira aula de yoga", sub="Você diz que é sua primeira vez, pega um tapete, pergunta onde colocar e se precisa de sapatos, e começa pela respiração."),
 mini=[
  dict(who="Victor", en="Welcome! Is this your {first|second|third} time?", pt="Bem-vinda! É sua {primeira|segunda|terceira} vez?"),
  dict(who="You", en="Yes, I'm a little {nervous|tired|shy}.", pt="Sim, estou um pouco {nervosa|cansada|tímida}."),
  dict(who="Victor", en="Take a mat. Put it {anywhere you like|here|by the window}.", pt="Pegue um tapete. Coloque {onde quiser|aqui|perto da janela}."),
  dict(who="You", en="Do I need {shoes|socks|a towel}?", pt="Preciso de {sapatos|meias|uma toalha}?"),
 ],
 dlg=[
  dict(who="Victor", en="Welcome to class! Is this your {first|second} time?", pt="Bem-vinda à aula! É sua {primeira|segunda} vez?"),
  dict(who="You", en="Yes, I'm a little {nervous.|tired.}", pt="Sim, estou um pouco {nervosa.|cansada.}"),
  dict(who="Victor", en="Don't worry. Take a {mat.|towel.}", pt="Não se preocupe. Pegue {um tapete.|uma toalha.}"),
  dict(who="You", en="Where should I {put|place} it?", pt="Onde devo {colocar|pôr} isso?"),
  dict(who="Victor", en="{Anywhere|Somewhere} you like.", pt="{Onde quiser.|Em algum lugar que quiser.}"),
  dict(who="You", en="Do I need {shoes?|socks?}", pt="Preciso de {sapatos?|meias?}"),
  dict(who="Victor", en="No, we practice {barefoot.|slowly.}", pt="Não, praticamos {descalços.|devagar.}"),
  dict(who="You", en="Okay. What do we do {first?|next?}", pt="Ok. O que fazemos {primeiro?|depois?}"),
  dict(who="Victor", en="We start by {breathing|stretching} slowly.", pt="Começamos {respirando|alongando} devagar."),
 ],
 vocab=[
  dict(w="mat", pt="tapete (de yoga)", e="🧘", ex=["Take a mat, please.", "My mat is blue."]),
  dict(w="leg", pt="perna", e="🦵", ex=["Bend your leg.", "My leg is tired."]),
  dict(w="back", pt="costas", e="🔙", ex=["My back hurts a little.", "Keep your back straight."]),
  dict(w="head", pt="cabeça", e="🙂", ex=["Move your head slowly.", "My head is calm."]),
  dict(w="pose", pt="posição / postura", e="🤸", ex=["This pose is easy.", "Hold the pose for five breaths."]),
  dict(w="calm", pt="calmo / tranquilo", e="😌", ex=["I feel calm.", "The room is calm."]),
 ],
 molds=[
  dict(title="Perguntar o que precisa", frame="Do I need {thing}?", slots=[dict(key="thing", opts=["shoes", "a mat", "a towel", "a bottle"])], model="Do I need shoes?", note="Do I need...? pergunta se algo é necessário. 'a' antes de mat, towel, bottle."),
  dict(title="Perguntar onde colocar", frame="Where should I put my {thing}?", slots=[dict(key="thing", opts=["mat", "bag", "bottle", "shoes"])], model="Where should I put my mat?", note="Should I (nessa ordem) em perguntas: Where should I...?"),
  dict(title="Escrever sobre a aula", frame="In yoga, I {verb} my {part}. It feels {adj}.", slots=[dict(key="verb", opts=["stretch", "lift", "relax"]), dict(key="part", opts=["arms", "legs", "shoulders"]), dict(key="adj", opts=["calm", "good", "nice"])], model="In yoga, I stretch my arms. It feels calm.", note="Feels + adjetivo descreve a sensação."),
 ],
 sounds=[
  dict(say="We start by breathing slowly.", tag="ritmo: START, BREATH, SLOW", tip="Acentue START, BREATH e SLOW; 'we', 'by' e '-ing' ficam fracas."),
  dict(say="Anywhere you like.", tag="ritmo: ANY-where you LIKE", tip="Acentue a 1ª sílaba de ANYwhere e a palavra LIKE; 'you' é fraco."),
  dict(say="Don't worry. Take a mat.", tag="ritmo: DON'T WOR-ry, TAKE a MAT", tip="Bata o ritmo nas sílabas fortes; 'a' fica quase 'uh'."),
 ],
 role=dict(turns=[
  dict(npc="Welcome to class! Is this your first time?", opts=[
   dict(en="Yes, I'm a little nervous.", pt="Sim, estou um pouco nervosa.", reply="Don't worry. Take a mat."),
   dict(en="Yes, it is. I'm excited!", pt="Sim. Estou animada!", reply="Great! Take a mat."),
   dict(en="No, it's my second time.", pt="Não, é minha segunda vez.", reply="Welcome back! Take a mat.")]),
  dict(npc="Take a mat.", opts=[
   dict(en="Where should I put it?", pt="Onde devo colocar?", reply="Anywhere you like."),
   dict(en="Thanks. Can I sit by the window?", pt="Obrigada. Posso ficar perto da janela?", reply="Sure. Anywhere you like."),
   dict(en="Thanks. Is this mat clean?", pt="Obrigada. Este tapete está limpo?", reply="Yes, it is. Put it anywhere you like.")]),
  dict(npc="Anywhere you like.", opts=[
   dict(en="Do I need shoes?", pt="Preciso de sapatos?", reply="No, we practice barefoot."),
   dict(en="Do I need a towel?", pt="Preciso de toalha?", reply="No, but a towel can help. We practice barefoot."),
   dict(en="Do I need water?", pt="Preciso de água?", reply="A bottle is good. And we practice barefoot.")]),
  dict(npc="We practice barefoot.", opts=[
   dict(en="Okay. What do we do first?", pt="Ok. O que fazemos primeiro?", reply="We start by breathing slowly."),
   dict(en="Okay. Is it hard?", pt="Ok. É difícil?", reply="No. We go slowly. First, we breathe."),
   dict(en="Okay. Can I rest?", pt="Ok. Posso descansar?", reply="Of course. You should rest when you need it.")]),
 ], change=["Sua costa dói um pouco: diga isso e pergunte o que fazer.", "Você esqueceu a garrafa de água: pergunte se pode pegar água.", "Outro aluno está no seu lugar: pergunte onde pode colocar o tapete."]),
 writing=dict(task="Você chega a uma aula de yoga. Escreva 2 ou 3 frases: diga que é sua primeira vez, pergunte onde colocar o tapete e se precisa de sapatos.", model="Hi! This is my first time. Where should I put my mat? Do I need shoes?", kw=["first", "mat", "shoes", "where"], checks=["Disse que é a primeira vez.", "Perguntou onde colocar o tapete.", "Perguntou sobre sapatos."]),
 scenes=dict(pool=["gym", "hall", "garden", "beach"], npc=dict(g="m", role="teacher"), you=dict(g="f")),
 convo=dict(npc=dict(name="Victor"), story="Você está na sua primeira aula de yoga. O Victor, o professor, recebe você.", turns=[
  dict(npc="Welcome to class! Is this your first time?", pt="Bem-vinda à aula! É sua primeira vez?", opts=[
   dict(en="Yes, I'm a little nervous.", pt="Sim, estou um pouco nervosa.", ok=True, fb="Responde e conta como se sente."),
   dict(en="Yes, I need shoes.", pt="Sim, preciso de sapatos.", ok=False, fb="Não responde sobre a primeira vez."),
   dict(en="Take a mat.", pt="Pegue um tapete.", ok=False, fb="Essa fala é do professor.")]),
  dict(npc="Don't worry. Take a mat.", pt="Não se preocupe. Pegue um tapete.", opts=[
   dict(en="Yes, I'm nervous.", pt="Sim, estou nervosa.", ok=False, fb="Você já disse isso."),
   dict(en="No, we practice barefoot.", pt="Não, praticamos descalços.", ok=False, fb="Essa resposta é dele."),
   dict(en="Thanks. Where should I put it?", pt="Obrigada. Onde devo colocar?", ok=True, fb="Agradece e pergunta onde pôr o tapete.")]),
  dict(npc="Anywhere you like.", pt="Onde quiser.", opts=[
   dict(en="Take a mat.", pt="Pegue um tapete.", ok=False, fb="Você já tem o tapete."),
   dict(en="Do I need shoes?", pt="Preciso de sapatos?", ok=True, fb="Pergunta natural na primeira aula."),
   dict(en="We start by breathing slowly.", pt="Começamos respirando devagar.", ok=False, fb="Quem diz isso é o professor.")]),
  dict(npc="No, we practice barefoot.", pt="Não, praticamos descalços.", opts=[
   dict(en="Anywhere you like.", pt="Onde quiser.", ok=False, fb="Resposta do professor, não sua."),
   dict(en="Okay. What do we do first?", pt="Ok. O que fazemos primeiro?", ok=True, fb="Aceita e pergunta o próximo passo."),
   dict(en="Yes, I'm a little nervous.", pt="Sim, estou um pouco nervosa.", ok=False, fb="Não responde ao que ele disse.")]),
  dict(npc="We start by breathing slowly.", pt="Começamos respirando devagar.", opts=[
   dict(en="Where should I put it?", pt="Onde devo colocar?", ok=False, fb="Você já colocou o tapete."),
   dict(en="Do I need shoes?", pt="Preciso de sapatos?", ok=False, fb="Ele já respondeu isso."),
   dict(en="That sounds good. I'm ready.", pt="Parece bom. Estou pronta.", ok=True, fb="Resposta positiva para começar.")]),
 ]),
)
