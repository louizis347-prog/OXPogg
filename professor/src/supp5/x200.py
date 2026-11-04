X = dict(
 key=dict(big="What should I wear?", label="Escolher a roupa", sub="Pergunte o que vestir, veja o tempo e escolha. 'What's the weather like?' é a pergunta mais usada antes de sair."),
 mini=[
  dict(who="You", en="What should I wear {today?|tonight?|to school?}", pt="O que devo vestir {hoje?|hoje à noite?|para a escola?}"),
  dict(who="Miles", en="What's the {weather|forecast} like?", pt="Como está {o tempo?|a previsão?}"),
  dict(who="You", en="It's {cool|warm|cold} and {cloudy.|windy.}", pt="Está {fresco|quente|frio} e {nublado.|ventando.}"),
  dict(who="Miles", en="Then wear {long pants|a coat|a sweater}. The {blue|green} shirt looks nice.", pt="Então use {calça comprida|um casaco|um suéter}. A camisa {azul|verde} está bonita."),
 ],
 dlg=[
  dict(who="Miles", en="Mom, what should I {wear|put on} today?", pt="Mãe, o que devo {vestir|vestir} hoje?"),
  dict(who="You", en="What's the {weather|forecast} like?", pt="Como está {o tempo?|a previsão?}"),
  dict(who="Miles", en="It's {cool|warm} and {cloudy.|windy.}", pt="Está {fresco|quente} e {nublado.|ventando.}"),
  dict(who="You", en="Then wear {long pants.|a coat.}", pt="Então use {calça comprida.|um casaco.}"),
  dict(who="Miles", en="Which shirt? The {blue|red} or the {green?|white?}", pt="Qual camisa? A {azul|vermelha} ou a {verde?|branca?}"),
  dict(who="You", en="The {blue|red} one looks {nice.|great.}", pt="A {azul|vermelha} está {bonita.|ótima.}"),
  dict(who="Miles", en="Where are my {socks?|shoes?}", pt="Onde estão {minhas meias?|meus sapatos?}"),
  dict(who="You", en="In the {top|bottom} drawer.", pt="Na gaveta de {cima.|baixo.}"),
  dict(who="Miles", en="Should I wear a {jacket?|raincoat?}", pt="Devo vestir um {casaco?|capa de chuva?}"),
 ],
 vocab=[
  dict(w="shorts", pt="bermuda, short", e="🩳", ex=["I wear shorts in summer.", "Where are my shorts?"]),
  dict(w="coat", pt="casaco grosso", e="🧥", ex=["I wear a coat in winter.", "The coat is warm."]),
  dict(w="outfit", pt="roupa, look", e="👚", ex=["I like your outfit.", "This is a good outfit for school."]),
  dict(w="weather", pt="tempo (clima)", e="🌤️", ex=["The weather is nice.", "What's the weather today?"]),
  dict(w="skirt", pt="saia", e="👗", ex=["She wears a long skirt.", "I like this skirt."]),
  dict(w="raincoat", pt="capa de chuva", e="🌧️", ex=["Take a raincoat.", "My raincoat is yellow."]),
 ],
 molds=[
  dict(title="Perguntar o que vestir", frame="What should I wear {when}?", slots=[dict(key="when", opts=["today", "tonight", "to the party", "to school"])], model="What should I wear today?", note="What + should + I + wear. Serve para pedir conselho."),
  dict(title="Descrever o tempo", frame="It's {temp} and {sky}.", slots=[dict(key="temp", opts=["cool", "warm", "cold"]), dict(key="sky", opts=["cloudy", "windy", "sunny"])], model="It's cool and cloudy.", note="It's + adjetivo descreve o tempo. Sem artigo e sem 'has'."),
  dict(title="Escrever uma sugestão", frame="It's {temp}. Wear {item}, and take {extra}.", slots=[dict(key="temp", opts=["cold", "cool", "rainy"]), dict(key="item", opts=["long pants", "a coat", "a sweater"]), dict(key="extra", opts=["a jacket", "a raincoat", "an umbrella"])], model="It's cold. Wear long pants, and take a jacket.", note="Wear + roupa dá a sugestão. Take + coisa lembra de levar algo."),
 ],
 sounds=[
  dict(say="What should I wear?", tag="redução: should I", tip="Should I soa 'shudai'. O l de should é mudo. Acentue WEAR."),
  dict(say="Where are my socks?", tag="som: w de where", tip="Where começa com w: lábios arredondados, como em 'uau'. Não diga 'ver'."),
  dict(say="It's cool and cloudy.", tag="ligação: cool and", tip="Una cool + and: 'cooland'. O l liga com a vogal seguinte."),
 ],
 role=dict(turns=[
  dict(npc="Are you ready to go?", opts=[
   dict(en="Not yet. What should I wear?", pt="Ainda não. O que devo vestir?", reply="What's the weather like?"),
   dict(en="Almost. What should I wear today?", pt="Quase. O que devo vestir hoje?", reply="What's the weather like?"),
   dict(en="Not yet. Help me choose my clothes.", pt="Ainda não. Ajude-me a escolher a roupa.", reply="Sure. What's the weather like?")]),
  dict(npc="What's the weather like?", opts=[
   dict(en="It's cool and cloudy.", pt="Está fresco e nublado.", reply="Then wear long pants."),
   dict(en="It's warm and sunny.", pt="Está quente e ensolarado.", reply="Then wear shorts."),
   dict(en="It's cold and rainy.", pt="Está frio e chuvoso.", reply="Then wear a coat and take a raincoat.")]),
  dict(npc="Which shirt? The blue or the green?", opts=[
   dict(en="The blue one looks nice.", pt="A azul está bonita.", reply="Great. The blue one is my favorite."),
   dict(en="The green one, please.", pt="A verde, por favor.", reply="Great choice. The green one looks good."),
   dict(en="I like the blue one.", pt="Eu gosto da azul.", reply="Okay, the blue one.")]),
  dict(npc="Anything else?", opts=[
   dict(en="Where are my socks?", pt="Onde estão minhas meias?", reply="In the top drawer."),
   dict(en="Should I wear a jacket?", pt="Devo vestir um casaco?", reply="Yes, it can be cold later."),
   dict(en="Where are my sneakers?", pt="Onde estão meus tênis?", reply="Next to the door.")]),
 ], change=["O tempo muda e começa a chover: peça uma capa de chuva.", "Você tem uma festa à noite: pergunte o que vestir para ela.", "A camisa que você quer está suja: escolha outra."]),
 writing=dict(task="Você vai sair e o dia está fresco e nublado. Escreva 2 ou 3 frases: pergunte o que vestir, diga como está o tempo e escolha uma camisa.", model="What should I wear today? It's cool and cloudy. The blue shirt looks nice.", kw=["wear", "weather", "cool", "shirt"], checks=["Perguntou o que vestir.", "Descreveu o tempo.", "Escolheu uma camisa."]),
 scenes=dict(pool=["living", "bedroom", "home1", "kitchen"], npc=dict(g="m", role="friend"), you=dict(g="f")),
 convo=dict(npc=dict(name="Miles"), story="Você está se arrumando em casa. Seu amigo Miles ajuda a escolher a roupa para um dia fresco e nublado.", turns=[
  dict(npc="Good morning! Are you ready?", pt="Bom dia! Você está pronto?", opts=[
   dict(en="Not yet. What should I wear today?", pt="Ainda não. O que devo vestir hoje?", ok=True, fb="Pergunta natural pedindo conselho."),
   dict(en="Then wear long pants.", pt="Então use calça comprida.", ok=False, fb="Esse conselho vem do Miles, depois."),
   dict(en="In the top drawer.", pt="Na gaveta de cima.", ok=False, fb="Ninguém perguntou onde está algo.")]),
  dict(npc="What's the weather like?", pt="Como está o tempo?", opts=[
   dict(en="The blue one looks nice.", pt="A azul está bonita.", ok=False, fb="Ainda não falaram da camisa."),
   dict(en="Should I wear a jacket?", pt="Devo vestir um casaco?", ok=False, fb="Primeiro descreva o tempo."),
   dict(en="It's cool and cloudy.", pt="Está fresco e nublado.", ok=True, fb="Descreve o tempo com It's.")]),
  dict(npc="Then wear long pants. Which shirt, blue or green?", pt="Então use calça comprida. Qual camisa, azul ou verde?", opts=[
   dict(en="It's cool and cloudy.", pt="Está fresco e nublado.", ok=False, fb="O tempo já foi descrito."),
   dict(en="The blue one looks nice.", pt="A azul está bonita.", ok=True, fb="Escolhe uma camisa e dá o motivo."),
   dict(en="What's the weather like?", pt="Como está o tempo?", ok=False, fb="Você já sabe como está o tempo.")]),
  dict(npc="Good choice. Anything else?", pt="Boa escolha. Mais alguma coisa?", opts=[
   dict(en="Where are my socks?", pt="Onde estão minhas meias?", ok=True, fb="Pergunta o que falta."),
   dict(en="What should I wear today?", pt="O que devo vestir hoje?", ok=False, fb="Você já perguntou isso."),
   dict(en="Then wear long pants.", pt="Então use calça comprida.", ok=False, fb="Esse conselho já foi dado.")]),
  dict(npc="In the top drawer.", pt="Na gaveta de cima.", opts=[
   dict(en="It's cool and cloudy.", pt="Está fresco e nublado.", ok=False, fb="O tempo já foi dito."),
   dict(en="Thanks! Should I wear a jacket?", pt="Valeu! Devo vestir um casaco?", ok=True, fb="Agradece e faz a última pergunta."),
   dict(en="The blue one looks nice.", pt="A azul está bonita.", ok=False, fb="A camisa já foi escolhida.")]),
 ]),
)
