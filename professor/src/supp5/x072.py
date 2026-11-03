X = dict(
 key=dict(big="Where does the trash go?", label="Onde vai o lixo?", sub="A pergunta que todo vizinho novo faz. Em cada prédio ou cidade as lixeiras, as cores e os dias de coleta mudam."),
 mini=[
  dict(who="Mei", en="Excuse me, where does the {trash|recycling|glass} go?", pt="Com licença, onde {vai o lixo|vai a reciclagem|vai o vidro}?"),
  dict(who="You", en="In the {big|blue|green} bin.", pt="Na lixeira {grande|azul|verde}."),
  dict(who="Mei", en="When do they {collect it|come|pick it up}?", pt="Quando eles {recolhem|vêm|recolhem}?"),
  dict(who="You", en="Trash is {Tuesday|Monday|Thursday}.", pt="O lixo é {terça|segunda|quinta}."),
 ],
 dlg=[
  dict(who="Mei", en="Excuse me, where does the {trash|garbage} go?", pt="Com licença, onde vai o {lixo|lixo}?"),
  dict(who="You", en="In the big bin {behind the building.|next to the door.}", pt="Na lixeira grande {atrás do prédio.|ao lado da porta.}"),
  dict(who="Mei", en="And {recycling?|compost?}", pt="E {reciclagem?|compostagem?}"),
  dict(who="You", en="{Blue|Green} bin for paper and plastic.", pt="Lixeira {azul|verde} para papel e plástico."),
  dict(who="Mei", en="When do they {collect it?|come?}", pt="Quando eles {recolhem?|vêm?}"),
  dict(who="You", en="Trash is {Tuesday.|Monday.} Recycling is {Friday.|Thursday.}", pt="O lixo é {terça.|segunda.} A reciclagem é {sexta.|quinta.}"),
  dict(who="Mei", en="Thanks! What about {glass?|cardboard?}", pt="Valeu! E {o vidro?|o papelão?}"),
  dict(who="You", en="{Glass|Cardboard} goes in the {green|blue} bin.", pt="{Vidro vai|Papelão vai} na lixeira {verde.|azul.}"),
  dict(who="Mei", en="Perfect. Thanks for {helping!|the help!}", pt="Perfeito. Valeu {pela ajuda!|pela ajuda!}"),
 ],
 vocab=[
  dict(w="garbage", pt="lixo", e="🗑️", ex=["Take out the garbage, please.", "The garbage is full."]),
  dict(w="bin", pt="lixeira", e="🪣", ex=["The blue bin is for recycling.", "Close the lid of the bin."]),
  dict(w="recycling", pt="reciclagem", e="♻️", ex=["Recycling is on Friday.", "Where is the recycling bin?"]),
  dict(w="cardboard", pt="papelão", e="📦", ex=["Flatten the cardboard box.", "Cardboard goes in the blue bin."]),
  dict(w="truck", pt="caminhão", e="🚛", ex=["The truck comes at seven.", "I hear the trash truck."]),
  dict(w="compost", pt="compostagem", e="🥬", ex=["Food scraps go in the compost.", "The compost bin is brown."]),
 ],
 molds=[
  dict(title="Perguntar onde vai", frame="Where does the {thing} go?", slots=[dict(key="thing", opts=["trash", "glass", "cardboard", "compost"])], model="Where does the trash go?", note="Com the + coisa no singular, use does...go. Where do the bottles go? usa do no plural."),
  dict(title="Dizer o dia", frame="{thing} is {day}.", slots=[dict(key="thing", opts=["Trash", "Recycling", "Compost"]), dict(key="day", opts=["Tuesday", "Wednesday", "Friday"])], model="Trash is Tuesday.", note="Para dias fixos da semana, basta dizer: Trash is Tuesday. Também dá para dizer on Tuesday."),
  dict(title="Escrever um recado", frame="Hi! {thing} goes in the {color} bin. The truck comes on {day}.", slots=[dict(key="thing", opts=["Paper", "Glass", "Cardboard"]), dict(key="color", opts=["blue", "green", "brown"]), dict(key="day", opts=["Tuesday", "Wednesday", "Friday"])], model="Hi! Paper goes in the blue bin. The truck comes on Tuesday.", note="goes in = vai em. O dia vem depois de on."),
 ],
 sounds=[
  dict(say="Where does the trash go?", tag="redução: does the", tip="Does the soa 'dazthe', bem fraco. Acentue TRASH e GO."),
  dict(say="Blue bin for paper and plastic.", tag="acento: palavras de conteúdo", tip="Bata BLUE, BIN, PA-per, PLAS-tic. 'For' e 'and' são fracos: 'fer', 'n'."),
  dict(say="When do they collect it?", tag="ligação: collect it", tip="Collect it soa 'colec-tit'. O t de collect gruda no it."),
 ],
 role=dict(turns=[
  dict(npc="Excuse me, where does the trash go?", opts=[
   dict(en="In the big bin behind the building.", pt="Na lixeira grande atrás do prédio.", reply="Behind the building? Okay, thanks."),
   dict(en="In the big bin next to the door.", pt="Na lixeira grande ao lado da porta.", reply="Next to the door? Okay, thanks."),
   dict(en="In the bin in the hallway.", pt="Na lixeira do corredor.", reply="In the hallway? Okay, thanks.")]),
  dict(npc="And recycling?", opts=[
   dict(en="Blue bin for paper and plastic.", pt="Lixeira azul para papel e plástico.", reply="Blue bin. Got it."),
   dict(en="The blue bin is for paper and cardboard.", pt="A lixeira azul é para papel e papelão.", reply="Blue bin for paper and cardboard. Got it."),
   dict(en="Recycling goes in the blue bin.", pt="A reciclagem vai na lixeira azul.", reply="In the blue bin. Got it.")]),
  dict(npc="When do they collect it?", opts=[
   dict(en="Trash is Tuesday. Recycling is Friday.", pt="O lixo é terça. A reciclagem é sexta.", reply="Tuesday and Friday. I'll write it down."),
   dict(en="The truck comes on Tuesday and Friday.", pt="O caminhão vem na terça e na sexta.", reply="Tuesday and Friday. I'll write it down."),
   dict(en="Trash is Tuesday. Recycling is Thursday.", pt="O lixo é terça. A reciclagem é quinta.", reply="Tuesday and Thursday. I'll write it down.")]),
  dict(npc="Thanks! What about glass?", opts=[
   dict(en="Glass goes in the green bin.", pt="Vidro vai na lixeira verde.", reply="Perfect. Thanks for helping!"),
   dict(en="Glass has its own green bin.", pt="O vidro tem a própria lixeira verde.", reply="Perfect. Thanks for helping!"),
   dict(en="Put glass in the green bin.", pt="Ponha o vidro na lixeira verde.", reply="Perfect. Thanks for helping!")]),
 ], change=["Mei pergunta onde jogar uma caixa de pizza gordurosa: diga que é melhor no lixo comum e confira a regra.", "O caminhão já passou hoje: diga que ela deve esperar até a próxima coleta.", "Mei não vê a lixeira azul: diga onde ela está e ofereça ir junto."]),
 writing=dict(task="Escreva um bilhete para um vizinho novo: diga onde vai o lixo, a cor da lixeira da reciclagem e os dias da coleta.", model="Hi! The trash goes in the big bin behind the building. Recycling goes in the blue bin. Trash is Tuesday and recycling is Friday.", kw=["trash", "bin", "recycling", "friday"], checks=["Disse onde vai o lixo.", "Falou da lixeira da reciclagem.", "Disse os dias da coleta."]),
 scenes=dict(pool=["street", "hall", "yard", "lobby"], npc=dict(g="f", role="neighbor"), you=dict(g="m")),
 convo=dict(npc=dict(name="Mei"), story="Mei é uma vizinha nova no seu prédio em Seattle e pergunta sobre o lixo.", turns=[
  dict(npc="Excuse me, where does the trash go?", pt="Com licença, onde vai o lixo?", opts=[
   dict(en="Trash is Tuesday.", pt="O lixo é terça.", ok=False, fb="Ela perguntou onde, não quando."),
   dict(en="Perfect. Thanks for helping!", pt="Perfeito. Valeu pela ajuda!", ok=False, fb="Essa frase é da Mei, no final."),
   dict(en="In the big bin behind the building.", pt="Na lixeira grande atrás do prédio.", ok=True, fb="Responde o lugar com clareza.")]),
  dict(npc="And recycling?", pt="E reciclagem?", opts=[
   dict(en="Blue bin for paper and plastic.", pt="Lixeira azul para papel e plástico.", ok=True, fb="Diz a cor e o que vai nela."),
   dict(en="Excuse me, where does the trash go?", pt="Com licença, onde vai o lixo?", ok=False, fb="Essa pergunta já foi feita e respondida."),
   dict(en="Trash is Tuesday.", pt="O lixo é terça.", ok=False, fb="Isso fala do lixo e do dia, não da reciclagem.")]),
  dict(npc="When do they collect it?", pt="Quando eles recolhem?", opts=[
   dict(en="Glass goes in the green bin.", pt="Vidro vai na lixeira verde.", ok=False, fb="Ela pergunta quando, e o vidro vem depois."),
   dict(en="Trash is Tuesday. Recycling is Friday.", pt="O lixo é terça. A reciclagem é sexta.", ok=True, fb="Dá os dois dias."),
   dict(en="In the big bin.", pt="Na lixeira grande.", ok=False, fb="Isso é um lugar, e ela pergunta o dia.")]),
  dict(npc="Thanks! What about glass?", pt="Valeu! E o vidro?", opts=[
   dict(en="Glass goes in the green bin.", pt="Vidro vai na lixeira verde.", ok=True, fb="Responde onde o vidro vai."),
   dict(en="You're welcome. And recycling?", pt="De nada. E reciclagem?", ok=False, fb="Você já falou de reciclagem; ela pergunta do vidro."),
   dict(en="Trash is Tuesday.", pt="O lixo é terça.", ok=False, fb="Não responde sobre o vidro.")]),
  dict(npc="Perfect. Thanks for helping!", pt="Perfeito. Valeu pela ajuda!", opts=[
   dict(en="Where does the trash go?", pt="Onde vai o lixo?", ok=False, fb="A pergunta já foi respondida."),
   dict(en="No problem. Welcome to the building!", pt="Sem problema. Bem-vinda ao prédio!", ok=True, fb="Fecha de forma simpática."),
   dict(en="Blue bin for paper.", pt="Lixeira azul para papel.", ok=False, fb="Ela já agradeceu; não precisa repetir.")]),
 ]),
)
