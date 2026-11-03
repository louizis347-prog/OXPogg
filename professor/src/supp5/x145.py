X = dict(
 key=dict(big="When does it start?", label="Entrar em um passeio guiado", sub="Confirme que veio para o passeio, pergunte a hora, o caminho, a duração e se é difícil."),
 mini=[
  dict(who="Grace", en="Hello! Are you here for the {tour?|walk?|trip?}", pt="Olá! Vocês vieram para {o passeio?|a caminhada?|a viagem?}"),
  dict(who="You", en="Yes. When does it {start?|begin?|leave?}", pt="Sim. Quando {começa?|começa?|sai?}"),
  dict(who="Grace", en="In {five|ten|fifteen} minutes. Follow the red line.", pt="Em {cinco|dez|quinze} minutos. Sigam a linha vermelha."),
  dict(who="You", en="How long is the {walk?|tour?|trail?}", pt="Quanto tempo dura {a caminhada?|o passeio?|a trilha?}"),
 ],
 dlg=[
  dict(who="Grace", en="Hello! Are you here for the {tour?|walk?}", pt="Olá! Vocês vieram para {o passeio?|a caminhada?}"),
  dict(who="You", en="Yes. When does it {start?|begin?}", pt="Sim. Quando {começa?|começa?}"),
  dict(who="Grace", en="In {five|ten} minutes. Follow the red {line.|path.}", pt="Em {cinco|dez} minutos. Sigam a {linha|trilha} vermelha."),
  dict(who="You", en="Why is there a red {line?|path?}", pt="Por que tem uma {linha|trilha} vermelha?"),
  dict(who="Grace", en="It shows the {Freedom Trail.|way.}", pt="Ela mostra {a Trilha da Liberdade.|o caminho.}"),
  dict(who="You", en="How long is the {walk?|tour?}", pt="Quanto tempo dura {a caminhada?|o passeio?}"),
  dict(who="Grace", en="About two and a half {miles.|hours.}", pt="Cerca de duas e meia {milhas.|horas.}"),
  dict(who="You", en="Is it {hard?|long?}", pt="É {difícil?|longo?}"),
  dict(who="Grace", en="No, it's {easy|simple} and flat.", pt="Não, é {fácil|simples} e plano."),
 ],
 vocab=[
  dict(w="history", pt="história", e="📜", ex=["I like history.", "Boston has a long history."]),
  dict(w="trail", pt="trilha", e="🥾", ex=["The trail is easy.", "We walk the Freedom Trail."]),
  dict(w="brick", pt="tijolo", e="🧱", ex=["The red line is made of brick.", "This building is brick."]),
  dict(w="harbor", pt="porto", e="⚓", ex=["The harbor is near.", "Boats stay in the harbor."]),
  dict(w="church", pt="igreja", e="⛪", ex=["The church is very old.", "We see an old church."]),
  dict(w="freedom", pt="liberdade", e="🗽", ex=["Freedom is important.", "This trail shows freedom stories."]),
 ],
 molds=[
  dict(title="Perguntar a hora de início", frame="When does the {thing} start? In {time} minutes.", slots=[dict(key="thing", opts=["tour", "walk", "show"]), dict(key="time", opts=["five", "ten", "fifteen"])], model="When does the tour start? In five minutes.", note="When does + sujeito + verbo base. Sem -s em start."),
  dict(title="Perguntar a duração", frame="How long is the {thing}? About {n} hours.", slots=[dict(key="thing", opts=["walk", "tour", "trail"]), dict(key="n", opts=["two", "three", "four"])], model="How long is the walk? About two hours.", note="How long is... pergunta a duração. Hours fica no plural depois de two, three, four."),
  dict(title="Escrever a pergunta", frame="Hi. Is the {thing} easy? It is {adj} and flat.", slots=[dict(key="thing", opts=["walk", "tour", "trail"]), dict(key="adj", opts=["easy", "short", "nice"])], model="Hi. Is the walk easy? It is easy and flat.", note="Is the... easy? pergunta se algo é fácil."),
 ],
 sounds=[
  dict(say="About two and a half miles.", tag="redução: and → 'n'", tip="'And' vira 'n' fraco: 'two n a half'. Acentue TWO, HALF e MILES."),
  dict(say="Follow the red line.", tag="redução: the → 'thuh'", tip="'The' fica curto e fraco: 'FOL-low thuh RED LINE'."),
  dict(say="It's easy and flat.", tag="redução: and → 'n'", tip="Diga 'EA-sy n FLAT'. O 'and' quase desaparece."),
 ],
 role=dict(turns=[
  dict(npc="Hello! Are you here for the tour?", opts=[
   dict(en="Yes. When does it start?", pt="Sim. Quando começa?", reply="In five minutes."),
   dict(en="Yes. What time does it start?", pt="Sim. A que horas começa?", reply="At ten o'clock. In five minutes."),
   dict(en="Yes, we are. Are we on time?", pt="Sim, somos nós. Estamos no horário?", reply="Yes. It starts in five minutes.")]),
  dict(npc="In five minutes. Follow the red line.", opts=[
   dict(en="Why is there a red line?", pt="Por que tem uma linha vermelha?", reply="It shows the Freedom Trail."),
   dict(en="What is the red line?", pt="O que é a linha vermelha?", reply="It shows the Freedom Trail."),
   dict(en="Where does it go?", pt="Para onde ela vai?", reply="It goes to sixteen historic places.")]),
  dict(npc="It shows the Freedom Trail.", opts=[
   dict(en="How long is the walk?", pt="Quanto tempo dura a caminhada?", reply="About two and a half miles."),
   dict(en="How far is it?", pt="Qual é a distância?", reply="About two and a half miles."),
   dict(en="How long is the tour?", pt="Quanto tempo dura o passeio?", reply="About ninety minutes.")]),
  dict(npc="It's a long walk, but fun.", opts=[
   dict(en="Is it hard?", pt="É difícil?", reply="No, it's easy and flat."),
   dict(en="Are there many hills?", pt="Tem muitas ladeiras?", reply="No, it's easy and flat."),
   dict(en="Can children walk it?", pt="Crianças podem fazer?", reply="Yes. It's easy and flat.")]),
 ], change=["A guia diz que o passeio já começou: pergunte se dá para entrar agora.", "Você está cansado: pergunte se tem um lugar para sentar.", "Um amigo quer saber o preço: pergunte à guia."]),
 writing=dict(task="Você chega a um passeio histórico em Boston. Escreva 2 ou 3 frases: pergunte quando começa, quanto tempo dura e se é difícil.", model="Hello! When does the tour start? How long is the walk? Is it hard?", kw=["when", "start", "long", "hard"], checks=["Perguntou quando começa.", "Perguntou quanto dura.", "Perguntou se é difícil."]),
 scenes=dict(pool=["park", "park2", "street", "harbor", "pier"], npc=dict(g="f", role="guide"), you=dict(g="m")),
 convo=dict(npc=dict(name="Grace"), story="Você chega a um passeio a pé em Boston. Grace é a guia.", turns=[
  dict(npc="Hello! Are you here for the tour?", pt="Olá! Vocês vieram para o passeio?", opts=[
   dict(en="No, it's easy and flat.", pt="Não, é fácil e plano.", ok=False, fb="Essa frase responde outra pergunta."),
   dict(en="Yes. When does it start?", pt="Sim. Quando começa?", ok=True, fb="Confirma e pergunta a hora."),
   dict(en="About two and a half miles.", pt="Cerca de quatro quilômetros.", ok=False, fb="Ela não perguntou a distância.")]),
  dict(npc="In five minutes. Follow the red line.", pt="Em cinco minutos. Sigam a linha vermelha.", opts=[
   dict(en="Why is there a red line?", pt="Por que tem uma linha vermelha?", ok=True, fb="Pergunta natural."),
   dict(en="Yes. When does it start?", pt="Sim. Quando começa?", ok=False, fb="Ela acabou de dizer."),
   dict(en="It shows the Freedom Trail.", pt="Ela mostra a Trilha da Liberdade.", ok=False, fb="Essa resposta é da guia.")]),
  dict(npc="It shows the Freedom Trail.", pt="Ela mostra a Trilha da Liberdade.", opts=[
   dict(en="Hello! Are you here for the tour?", pt="Olá! Vocês vieram para o passeio?", ok=False, fb="Essa pergunta é dela."),
   dict(en="Is it hard?", pt="É difícil?", ok=False, fb="Ainda falta saber a duração."),
   dict(en="How long is the walk?", pt="Quanto tempo dura a caminhada?", ok=True, fb="Pergunta a duração.")]),
  dict(npc="About two and a half miles.", pt="Cerca de quatro quilômetros.", opts=[
   dict(en="Is it hard?", pt="É difícil?", ok=True, fb="Pergunta lógica depois da distância."),
   dict(en="In five minutes.", pt="Em cinco minutos.", ok=False, fb="Não responde à fala dela."),
   dict(en="Follow the red line.", pt="Sigam a linha vermelha.", ok=False, fb="Quem diz isso é a guia.")]),
  dict(npc="No, it's easy and flat.", pt="Não, é fácil e plano.", opts=[
   dict(en="Great. Let's go!", pt="Ótimo. Vamos!", ok=True, fb="Encerramento natural."),
   dict(en="How long is the walk?", pt="Quanto tempo dura a caminhada?", ok=False, fb="Você já perguntou."),
   dict(en="Why is there a red line?", pt="Por que tem uma linha vermelha?", ok=False, fb="Você já perguntou isso.")]),
 ]),
)
