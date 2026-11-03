X = dict(
 key=dict(big="Where is the milk?", label="Perguntar onde fica", sub="No supermercado, os corredores (aisles) têm número. A resposta típica é It's in aisle three."),
 mini=[
  dict(who="Serena", en="Excuse me, where is the {milk|bread|rice}?", pt="Com licença, onde fica {o leite|o pão|o arroz}?"),
  dict(who="You", en="It's in aisle {three|five|seven}.", pt="Fica no corredor {três|cinco|sete}."),
  dict(who="Serena", en="And where is the {bread|cheese|juice}?", pt="E onde fica {o pão|o queijo|o suco}?"),
  dict(who="You", en="It's {next to the milk|on the left|on the right}.", pt="Fica {do lado do leite|à esquerda|à direita}."),
 ],
 dlg=[
  dict(who="Serena", en="Excuse me, where is the {milk|rice|cheese}?", pt="Com licença, onde fica {o leite|o arroz|o queijo}?"),
  dict(who="You", en="It's in aisle {three|four|six}.", pt="Fica no corredor {três|quatro|seis}."),
  dict(who="Serena", en="And where is the {bread|juice}?", pt="E onde fica {o pão|o suco}?"),
  dict(who="You", en="It's {next to the milk|on the left}.", pt="Fica {do lado do leite|à esquerda}."),
  dict(who="Serena", en="Thanks! Do you have {rice|pasta}?", pt="Valeu! Vocês têm {arroz|massa}?"),
  dict(who="You", en="Yes, in aisle five, on the {left|right}.", pt="Sim, no corredor cinco, à {esquerda|direita}."),
  dict(who="Serena", en="Great. {Thank you!|Thanks a lot!}", pt="Ótimo. {Obrigado!|Muito obrigado!}"),
  dict(who="You", en="{You're welcome.|No problem.}", pt="{De nada.|Sem problema.}"),
  dict(who="Serena", en="Happy shopping!", pt="Boas compras!"),
 ],
 vocab=[
  dict(w="aisle", pt="corredor", e="🛒", ex=["The milk is in aisle three.", "Which aisle has the rice?"]),
  dict(w="shelf", pt="prateleira", e="🗄️", ex=["The rice is on the top shelf.", "Is the bread on this shelf?"]),
  dict(w="left", pt="esquerda", e="⬅️", ex=["Turn left at the end of the aisle.", "The juice is on the left."]),
  dict(w="right", pt="direita", e="➡️", ex=["The cheese is on the right.", "Turn right, please."]),
  dict(w="milk", pt="leite", e="🥛", ex=["Where is the milk?", "The milk is next to the cheese."]),
  dict(w="rice", pt="arroz", e="🍚", ex=["Do you have rice?", "The rice is in aisle five."]),
 ],
 molds=[
  dict(title="Perguntar onde fica", frame="Excuse me, where is the {item}?", slots=[dict(key="item", opts=["milk", "bread", "rice", "juice"])], model="Excuse me, where is the milk?", note="Excuse me chama a atenção com educação. Where is the...? pergunta a localização."),
  dict(title="Dar a localização", frame="It's in aisle {num}, {side}.", slots=[dict(key="num", opts=["three", "five", "seven"]), dict(key="side", opts=["on the left", "on the right", "at the end"])], model="It's in aisle three, on the left.", note="Aisle + número e depois left ou right: a resposta que o cliente quer ouvir."),
  dict(title="Escrever uma indicação", frame="The {item} is {place}.", slots=[dict(key="item", opts=["bread", "rice", "juice"]), dict(key="place", opts=["next to the milk", "on the left", "in aisle four"])], model="The bread is next to the milk.", note="Next to = ao lado de. Escreva a frase inteira com The ... is ..."),
 ],
 sounds=[
  dict(say="Excuse me, where is the milk?", tag="ligação: excuse me", tip="Excuse e me se juntam: 'ik-skiuz-mi'. Sem pausa entre as duas."),
  dict(say="It's in aisle three.", tag="ligação: it's in", tip="It's in vira quase 'itsin'. O acento está em aisle e three."),
  dict(say="Yes, in aisle five, on the left.", tag="ligação: in aisle", tip="In aisle soa como 'inail'. Una as palavras e mantenha o ritmo."),
 ],
 role=dict(turns=[
  dict(npc="Excuse me, where is the milk?", opts=[
   dict(en="It's in aisle three.", pt="Fica no corredor três.", reply="Aisle three. Thanks!"),
   dict(en="It's in aisle five, on the left.", pt="Fica no corredor cinco, à esquerda.", reply="Aisle five, on the left. Got it."),
   dict(en="It's next to the cheese.", pt="Fica ao lado do queijo.", reply="Next to the cheese. Great, thanks!")]),
  dict(npc="And where is the bread?", opts=[
   dict(en="It's next to the milk.", pt="Fica do lado do leite.", reply="Perfect. Easy to find."),
   dict(en="It's in aisle four.", pt="Fica no corredor quatro.", reply="Aisle four. Thank you!"),
   dict(en="It's on the right.", pt="Fica à direita.", reply="On the right. Thanks!")]),
  dict(npc="Thanks! Do you have rice?", opts=[
   dict(en="Yes, in aisle five, on the left.", pt="Sim, no corredor cinco, à esquerda.", reply="Great. I'll go there now."),
   dict(en="Yes, it's on the top shelf.", pt="Sim, está na prateleira de cima.", reply="Okay. I can see it."),
   dict(en="Yes, it's next to the pasta.", pt="Sim, fica ao lado da massa.", reply="Next to the pasta. Perfect.")]),
  dict(npc="Great. Thank you!", opts=[
   dict(en="You're welcome.", pt="De nada.", reply="Thanks again!"),
   dict(en="No problem. Happy shopping!", pt="Sem problema. Boas compras!", reply="Thanks! You too."),
   dict(en="My pleasure.", pt="Com prazer.", reply="That's so kind. Bye!")]),
 ], change=["O cliente não encontra o item: ofereça-se para levá-lo até lá.", "O produto acabou: diga que não tem e sugira outro.", "O cliente pergunta onde ficam os caixas: dê a direção."]),
 writing=dict(task="Você ajuda um cliente no mercado. Escreva 2 ou 3 frases: diga em que corredor está o leite e onde está o pão.", model="The milk is in aisle three. The bread is next to the milk. It is on the left.", kw=["aisle", "milk", "bread", "left"], checks=["Disse o número do corredor.", "Usou next to, left ou right.", "As frases têm The ... is ..."]),
 scenes=dict(pool=["supermarket", "market", "shop", "counter"], npc=dict(g="f", role="customer"), you=dict(g="m")),
 convo=dict(npc=dict(name="Serena"), story="Você trabalha num supermercado. Uma cliente pergunta onde ficam os produtos.", turns=[
  dict(npc="Excuse me, where is the milk?", pt="Com licença, onde fica o leite?", opts=[
   dict(en="Yes, I have milk.", pt="Sim, eu tenho leite.", ok=False, fb="Ela pergunta a localização, não se você tem leite."),
   dict(en="It's in aisle three.", pt="Fica no corredor três.", ok=True, fb="Dá a localização com o número do corredor."),
   dict(en="I'm sorry, thank you.", pt="Desculpe, obrigado.", ok=False, fb="Não responde à pergunta.")]),
  dict(npc="And where is the bread?", pt="E onde fica o pão?", opts=[
   dict(en="It's next to the milk.", pt="Fica do lado do leite.", ok=True, fb="Referência simples e clara."),
   dict(en="Happy shopping!", pt="Boas compras!", ok=False, fb="É uma despedida; a cliente ainda precisa da informação."),
   dict(en="The bread is good.", pt="O pão é bom.", ok=False, fb="Ela perguntou onde está, não como é.")]),
  dict(npc="Thanks! Do you have rice?", pt="Valeu! Vocês têm arroz?", opts=[
   dict(en="You're welcome.", pt="De nada.", ok=False, fb="Ela fez uma nova pergunta, então responda sobre o arroz."),
   dict(en="Excuse me, where is the rice?", pt="Com licença, onde fica o arroz?", ok=False, fb="Quem pergunta onde fica é a cliente, não você."),
   dict(en="Yes, in aisle five, on the left.", pt="Sim, no corredor cinco, à esquerda.", ok=True, fb="Responde sim e diz onde está.")]),
  dict(npc="Great. Thank you!", pt="Ótimo. Obrigada!", opts=[
   dict(en="You're welcome.", pt="De nada.", ok=True, fb="Resposta padrão a um agradecimento."),
   dict(en="Thank you, too!", pt="Obrigado você também!", ok=False, fb="Você ajudou a cliente; a resposta natural é 'de nada'."),
   dict(en="Where is the milk?", pt="Onde fica o leite?", ok=False, fb="O leite já foi explicado.")]),
  dict(npc="Happy shopping!", pt="Boas compras!", opts=[
   dict(en="Excuse me, where is the bread?", pt="Com licença, onde fica o pão?", ok=False, fb="Ela está se despedindo; já tem as informações."),
   dict(en="Thanks! Have a good day.", pt="Valeu! Tenha um bom dia.", ok=True, fb="Despedida simpática."),
   dict(en="It's in aisle five.", pt="Fica no corredor cinco.", ok=False, fb="Ela já se despediu; não é hora de nova indicação.")]),
 ]),
)
