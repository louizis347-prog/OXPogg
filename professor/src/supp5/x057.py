X = dict(
 key=dict(big="Excuse me, I'm lost", label="Pedir ajuda quando está perdido", sub="Comece com Excuse me, diga que está perdido e responda para onde quer ir. Quem ajuda dá o ônibus e o lugar do ponto."),
 mini=[
  dict(who="Grace", en="Excuse me, I'm {lost|new here|late}.", pt="Com licença, estou {perdida|nova aqui|atrasada}."),
  dict(who="You", en="Where do you want to {go?|be?|walk?}", pt="Aonde você quer {ir?|estar?|andar?}"),
  dict(who="Grace", en="To the {Science Museum|train station|bus stop}.", pt="Ao {Museu de Ciências|estação de trem|ponto de ônibus}."),
  dict(who="You", en="It's {far|not far|very far} from here.", pt="Fica {longe|perto|muito longe} daqui."),
 ],
 dlg=[
  dict(who="Grace", en="Excuse me, I'm {lost.|lost, sorry.}", pt="Com licença, estou {perdida.|perdida, desculpe.}"),
  dict(who="You", en="Where do you want to {go?|go today?}", pt="Aonde você quer {ir?|ir hoje?}"),
  dict(who="Grace", en="To the {Science Museum.|train station.}", pt="Ao {Museu de Ciências.|estação de trem.}"),
  dict(who="You", en="It's {far|very far} from here. Take the {bus.|subway.}", pt="Fica {longe|muito longe} daqui. Pegue o {ônibus.|metrô.}"),
  dict(who="Grace", en="Which {bus?|one?}", pt="Qual {ônibus?|deles?}"),
  dict(who="You", en="Number {eighty-six.|sixty-six.} The stop is {there.|here.}", pt="O {oitenta e seis.|sessenta e seis.} O ponto é {ali.|aqui.}"),
  dict(who="Grace", en="Thank you {very much.|so much.}", pt="Muito {obrigada.|obrigada mesmo.}"),
  dict(who="You", en="Good {luck!|trip!}", pt="Boa {sorte!|viagem!}"),
  dict(who="Grace", en="Good luck, and safe {travels!|trip!}", pt="Boa sorte e boa {viagem!|viagem!}"),
 ],
 vocab=[
  dict(w="map", pt="mapa", e="🗺️", ex=["I have a map in my bag.", "Look at the map."]),
  dict(w="lost", pt="perdido", e="❓", ex=["I'm lost.", "The tourist is lost."]),
  dict(w="museum", pt="museu", e="🏛️", ex=["The museum is far.", "I want to go to the museum."]),
  dict(w="tourist", pt="turista", e="🧳", ex=["She is a tourist.", "The tourist has a map."]),
  dict(w="directions", pt="direções / instruções de caminho", e="🧭", ex=["Can you give me directions?", "I need directions to the museum."]),
  dict(w="luck", pt="sorte", e="🍀", ex=["Good luck!", "Luck is important."]),
 ],
 molds=[
  dict(title="Dizer aonde quer ir", frame="I want to go to the {place}.", slots=[dict(key="place", opts=["Science Museum", "train station", "park", "bus stop"])], model="I want to go to the Science Museum.", note="Want to go to = querer ir a. Depois de to the vem o lugar."),
  dict(title="Dar a direção", frame="It's {dist} from here. Take the {ride}.", slots=[dict(key="dist", opts=["far", "not far", "very far"]), dict(key="ride", opts=["bus", "train", "subway"])], model="It's far from here. Take the bus.", note="Far = longe. Take the... = pegue o... (ônibus, trem, metrô)."),
  dict(title="Escrever o pedido", frame="Excuse me, I'm lost. I want to go to the {place}. Is it {how}?", slots=[dict(key="place", opts=["museum", "park", "station"]), dict(key="how", opts=["far", "near", "close"])], model="Excuse me, I'm lost. I want to go to the museum. Is it far?", note="Comece com Excuse me, diga o lugar e pergunte se é longe."),
 ],
 sounds=[
  dict(say="Excuse me, I'm lost.", tag="acento: ex-CUSE me", tip="A força está em CUSE: ex-CUSE me. Diga i'm LOST com o L bem claro no final."),
  dict(say="Number eighty-six.", tag="acento: EIGH-ty", tip="Em números com -ty, a força vai na primeira sílaba: EIGH-ty. Em -teen é na última: eigh-TEEN."),
  dict(say="Good luck!", tag="ritmo: Good LUCK", tip="Diga as duas palavras juntas, com força em LUCK. O d de good fica leve."),
 ],
 role=dict(turns=[
  dict(npc="Excuse me, I'm lost.", opts=[
   dict(en="Where do you want to go?", pt="Aonde você quer ir?", reply="To the Science Museum."),
   dict(en="Sure. Where is your hotel?", pt="Claro. Onde fica seu hotel?", reply="It is near the park."),
   dict(en="I can help. Where are you going?", pt="Posso ajudar. Aonde você vai?", reply="To the Science Museum.")]),
  dict(npc="To the Science Museum.", opts=[
   dict(en="It's far from here. Take the bus.", pt="Fica longe daqui. Pegue o ônibus.", reply="Which bus?"),
   dict(en="It's not far. Take the train.", pt="Não fica longe. Pegue o trem.", reply="Which train?"),
   dict(en="It's far. Take the subway.", pt="Fica longe. Pegue o metrô.", reply="Which line?")]),
  dict(npc="Which bus?", opts=[
   dict(en="Number eighty-six. The stop is there.", pt="O número oitenta e seis. O ponto é ali.", reply="Thank you very much."),
   dict(en="Number twenty. The stop is here.", pt="O número vinte. O ponto é aqui.", reply="Thank you very much."),
   dict(en="Number sixty. The stop is over there.", pt="O número sessenta. O ponto fica logo ali.", reply="Thank you very much.")]),
  dict(npc="Thank you very much.", opts=[
   dict(en="Good luck!", pt="Boa sorte!", reply="Good luck, and safe travels!"),
   dict(en="You're welcome. Good luck!", pt="De nada. Boa sorte!", reply="Good luck, and safe travels!"),
   dict(en="No problem. Have a good day!", pt="Sem problema. Tenha um bom dia!", reply="You too, and safe travels!")]),
 ], change=["A pessoa não entende a palavra bus: diga de outro jeito ou aponte.", "O lugar é perto: diga que fica a dez minutos a pé.", "Você também não sabe o caminho: diga com educação e sugira o mapa."]),
 writing=dict(task="Você encontra uma pessoa perdida. Escreva 2 ou 3 frases: pergunte aonde ela quer ir e diga como chegar.", model="Hello! Where do you want to go? The museum is far from here. Take bus number eighty-six, please.", kw=["museum", "far", "bus", "take"], checks=["Perguntou aonde a pessoa quer ir.", "Disse se é longe ou perto.", "Disse qual transporte pegar."]),
 scenes=dict(pool=["park", "street", "nyc", "busstop"], npc=dict(g="f", role="tourist"), you=dict(g="m")),
 convo=dict(npc=dict(name="Grace"), story="Você está numa praça em Boston e uma pessoa perdida pede ajuda.", turns=[
  dict(npc="Excuse me, I'm lost.", pt="Com licença, estou perdida.", opts=[
   dict(en="Good luck, and safe travels!", pt="Boa sorte e boa viagem!", ok=False, fb="Isso se diz no fim, quando a pessoa vai embora."),
   dict(en="Number eighty-six.", pt="O oitenta e seis.", ok=False, fb="Ainda não sabemos aonde ela quer ir."),
   dict(en="Where do you want to go?", pt="Aonde você quer ir?", ok=True, fb="Pergunta o destino para poder ajudar.")]),
  dict(npc="To the Science Museum.", pt="Ao Museu de Ciências.", opts=[
   dict(en="It's far from here. Take the bus.", pt="Fica longe daqui. Pegue o ônibus.", ok=True, fb="Dá a distância e como chegar."),
   dict(en="Excuse me, I'm lost.", pt="Com licença, estou perdido.", ok=False, fb="Quem está perdida é ela, não você."),
   dict(en="Thank you very much.", pt="Muito obrigado.", ok=False, fb="Você ainda não ajudou.")]),
  dict(npc="Which bus?", pt="Qual ônibus?", opts=[
   dict(en="To the Science Museum.", pt="Ao Museu de Ciências.", ok=False, fb="Essa resposta é dela, e já foi dita."),
   dict(en="Number eighty-six. The stop is there.", pt="O oitenta e seis. O ponto é ali.", ok=True, fb="Diz o número e onde fica o ponto."),
   dict(en="Good luck!", pt="Boa sorte!", ok=False, fb="Ainda não respondeu a pergunta.")]),
  dict(npc="Thank you very much.", pt="Muito obrigada.", opts=[
   dict(en="Which bus?", pt="Qual ônibus?", ok=False, fb="Essa pergunta já foi respondida."),
   dict(en="Good luck!", pt="Boa sorte!", ok=True, fb="Responde com simpatia."),
   dict(en="It's far from here.", pt="Fica longe daqui.", ok=False, fb="Isso já foi dito e não responde ao agradecimento.")]),
  dict(npc="Good luck, and safe travels!", pt="Boa sorte e boa viagem!", opts=[
   dict(en="Excuse me, I'm lost.", pt="Com licença, estou perdido.", ok=False, fb="Essa fala é de quem pede ajuda, no começo."),
   dict(en="Thanks! Bye!", pt="Valeu! Tchau!", ok=True, fb="Fecha a conversa com educação."),
   dict(en="Take the bus.", pt="Pegue o ônibus.", ok=False, fb="Você já disse isso.")]),
 ]),
)
