X = dict(
 key=dict(big="Four players, please", label="Entrar na pista de boliche", sub="No balcão, diga quantos jogam, o tamanho dos sapatos e pergunte qual bola usar."),
 mini=[
  dict(who="Evan", en="Welcome! How many {players?|people?|friends?}", pt="Bem-vindos! Quantos {jogadores?|pessoas?|amigos?}"),
  dict(who="You", en="{Four|Three|Five} players, please. We need {shoes.|shoes, please.}", pt="{Quatro|Três|Cinco} jogadores, por favor. Precisamos de {sapatos.|sapatos, por favor.}"),
  dict(who="Evan", en="Here you go. Lane number {six.|four.|eight.}", pt="Aqui estão. Pista número {seis.|quatro.|oito.}"),
  dict(who="You", en="Thanks. Which {ball|shoes|lane} should I use?", pt="Valeu. Qual {bola|sapato|pista} devo usar?"),
 ],
 dlg=[
  dict(who="Evan", en="Welcome! How many {players?|people?}", pt="Bem-vindos! Quantos {jogadores?|pessoas?}"),
  dict(who="You", en="{Four|Three} players, please.", pt="{Quatro|Três} jogadores, por favor."),
  dict(who="Evan", en="Do you need {shoes?|socks?}", pt="Precisam de {sapatos?|meias?}"),
  dict(who="You", en="Yes, size {nine|eight} and size seven.", pt="Sim, tamanho {quarenta e três|quarenta e dois} e quarenta."),
  dict(who="Evan", en="Here you go. Lane number {six.|five.}", pt="Aqui estão. Pista número {seis.|cinco.}"),
  dict(who="You", en="Thanks. Which {ball|lane} should I use?", pt="Valeu. Qual {bola|pista} devo usar?"),
  dict(who="Evan", en="Try the {blue|green} one. It's lighter.", pt="Tente a {azul.|verde.} É mais leve."),
  dict(who="You", en="Okay. Who goes {first?|next?}", pt="Ok. Quem {começa?|é o próximo?}"),
  dict(who="Evan", en="{Ladies|Kids} first!", pt="{As damas|As crianças} primeiro!"),
 ],
 vocab=[
  dict(w="bowling", pt="boliche", e="🎳", ex=["We play bowling on Friday.", "I love bowling."]),
  dict(w="strike", pt="strike (todos os pinos)", e="💥", ex=["Maya gets a strike!", "A strike is ten pins."]),
  dict(w="pins", pt="pinos", e="🎳", ex=["Knock down the pins.", "There are ten pins."]),
  dict(w="points", pt="pontos", e="🔢", ex=["A strike gives ten points.", "We count the points."]),
  dict(w="round", pt="rodada", e="🔁", ex=["This is round two.", "We play one more round."]),
  dict(w="alley", pt="pista de boliche, beco", e="🏟️", ex=["The bowling alley is busy.", "We go to the alley on Friday."]),
 ],
 molds=[
  dict(title="Dizer quantas pessoas", frame="{number} players, please.", slots=[dict(key="number", opts=["Two", "Three", "Four", "Five"])], model="Two players, please.", note="Número + players, please. Fale devagar nos números."),
  dict(title="Pedir sapatos", frame="Yes, size {a} and size {b}.", slots=[dict(key="a", opts=["six", "seven", "eight", "nine"]), dict(key="b", opts=["six", "seven", "eight"])], model="Yes, size six and size six.", note="Size + número. Os números dos EUA são diferentes dos do Brasil."),
  dict(title="Escrever um pedido", frame="Hi! {number} players, please. We need shoes. Which {thing} should I use?", slots=[dict(key="number", opts=["Two", "Three", "Four"]), dict(key="thing", opts=["ball", "lane", "shoes"])], model="Hi! Two players, please. We need shoes. Which ball should I use?", note="Peça como no balcão: jogadores, sapatos e uma pergunta."),
 ],
 sounds=[
  dict(say="Lane number six, please.", tag="vogal curta: six, it", tip="O i é curto e relaxado. Six não soa como 'seeks'."),
  dict(say="Who goes first?", tag="acento: WHO GOES FIRST", tip="Acentue WHO, GOES e FIRST. O who fica claro, com h leve."),
  dict(say="Which ball should I use?", tag="ligação: should I", tip="Una should e I: 'shu-dai'. O l não é pronunciado."),
 ],
 role=dict(turns=[
  dict(npc="Welcome! How many players?", opts=[
   dict(en="Four players, please.", pt="Quatro jogadores, por favor.", reply="Great. Do you need shoes?"),
   dict(en="Two players, please.", pt="Dois jogadores, por favor.", reply="Great. Do you need shoes?"),
   dict(en="Three players, please.", pt="Três jogadores, por favor.", reply="Okay. Do you need shoes?")]),
  dict(npc="Do you need shoes?", opts=[
   dict(en="Yes, size nine and size seven.", pt="Sim, tamanho quarenta e três e quarenta.", reply="Here you go. Lane number six."),
   dict(en="Yes, size eight, please.", pt="Sim, tamanho quarenta e dois, por favor.", reply="Here you go. Lane number four."),
   dict(en="No, thanks. We have shoes.", pt="Não, obrigado. Temos sapatos.", reply="Okay. Lane number five.")]),
  dict(npc="Here you go. Lane number six.", opts=[
   dict(en="Thanks. Which ball should I use?", pt="Valeu. Qual bola devo usar?", reply="Try the blue one. It's lighter."),
   dict(en="Thanks. Is it a heavy ball?", pt="Valeu. É uma bola pesada?", reply="Not really. Try the blue one."),
   dict(en="Thanks! Where is lane six?", pt="Valeu! Onde fica a pista seis?", reply="It's on the left. Try the blue ball.")]),
  dict(npc="Try the blue one. It's lighter.", opts=[
   dict(en="Okay. Who goes first?", pt="Ok. Quem começa?", reply="Ladies first!"),
   dict(en="Thanks. Can I start?", pt="Valeu. Posso começar?", reply="Sure! Ladies first, though."),
   dict(en="Great. I'll go first!", pt="Ótimo. Eu começo!", reply="Ladies first!")]),
 ], change=["A bola azul é pesada demais: peça uma mais leve.", "Seu sapato é pequeno demais: peça um tamanho maior.", "A pista seis está ocupada: pergunte por outra pista."]),
 writing=dict(task="Escreva 2 ou 3 frases no balcão do boliche: diga quantos jogam, peça sapatos e pergunte qual bola usar.", model="Hi! Four players, please. We need shoes, size nine and size seven. Which ball should I use?", kw=["players", "shoes", "size", "ball"], checks=["Disse quantos jogam.", "Pediu sapatos com o tamanho.", "Perguntou sobre a bola."]),
 scenes=dict(pool=["nightcity", "counter", "stadium", "hall"], npc=dict(g="m", role="clerk"), you=dict(g="f")),
 convo=dict(npc=dict(name="Evan"), story="Você vai a uma pista de boliche com três amigos. O Evan trabalha no balcão e ajuda você.", turns=[
  dict(npc="Welcome! How many players?", pt="Bem-vindos! Quantos jogadores?", opts=[
   dict(en="Four players, please.", pt="Quatro jogadores, por favor.", ok=True, fb="Responde com o número."),
   dict(en="Do you need shoes?", pt="Precisam de sapatos?", ok=False, fb="Quem pergunta isso é o Evan."),
   dict(en="Lane number six.", pt="Pista número seis.", ok=False, fb="Quem diz isso é o Evan, depois.")]),
  dict(npc="Do you need shoes?", pt="Precisam de sapatos?", opts=[
   dict(en="Four players, please.", pt="Quatro jogadores, por favor.", ok=False, fb="Você já disse isso."),
   dict(en="Try the blue one.", pt="Tente a azul.", ok=False, fb="Quem diz isso é o Evan."),
   dict(en="Yes, size nine and size seven.", pt="Sim, tamanho quarenta e três e quarenta.", ok=True, fb="Responde sim e dá os tamanhos.")]),
  dict(npc="Here you go. Lane number six.", pt="Aqui estão. Pista número seis.", opts=[
   dict(en="Thanks. Which ball should I use?", pt="Valeu. Qual bola devo usar?", ok=True, fb="Agradece e pergunta."),
   dict(en="Yes, size nine and size seven.", pt="Sim, tamanho quarenta e três e quarenta.", ok=False, fb="Você já deu os tamanhos."),
   dict(en="Ladies first!", pt="As damas primeiro!", ok=False, fb="Ainda não é hora disso.")]),
  dict(npc="Try the blue one. It's lighter.", pt="Tente a azul. É mais leve.", opts=[
   dict(en="Ladies first!", pt="As damas primeiro!", ok=False, fb="Essa fala é do Evan."),
   dict(en="Which ball should I use?", pt="Qual bola devo usar?", ok=False, fb="Ele já respondeu."),
   dict(en="Okay. Who goes first?", pt="Ok. Quem começa?", ok=True, fb="Aceita e pergunta quem começa.")]),
  dict(npc="Ladies first!", pt="As damas primeiro!", opts=[
   dict(en="Four players, please.", pt="Quatro jogadores, por favor.", ok=False, fb="Já passou dessa parte."),
   dict(en="Go, Maya! You can do it!", pt="Vai, Maya! Você consegue!", ok=True, fb="Torce por uma amiga."),
   dict(en="Try the blue one.", pt="Tente a azul.", ok=False, fb="Essa fala é do Evan.")]),
 ]),
)
