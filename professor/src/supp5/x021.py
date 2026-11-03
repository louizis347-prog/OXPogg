X = dict(
key=dict(big='It\'s sunny, but it\'s cold.', label='Falar do tempo', sub='Use It\'s + adjetivo para o tempo: sunny, cold, hot, windy. Use but para um contraste.'),
mini=[
 dict(who='Evan', en='Nice {morning|afternoon|day}, isn\'t it?', pt='{Bela manhã|Bela tarde|Belo dia}, né?'),
 dict(who='You', en='Yes, it\'s {sunny|warm|clear} today.', pt='Sim, está {ensolarado|quente|limpo} hoje.'),
 dict(who='Evan', en='But it\'s {cold|windy|cool}!', pt='Mas está {frio|ventando|fresco}!'),
 dict(who='You', en='Chicago is always {windy|cold|busy}.', pt='Chicago é sempre {ventosa|fria|movimentada}.'),
],
dlg=[
 dict(who='Evan', en='Nice {morning|afternoon|day}, isn\'t it?', pt='{Bela manhã|Bela tarde|Belo dia}, né?'),
 dict(who='You', en='Yes, it\'s {sunny|warm|clear} today.', pt='Sim, está {ensolarado|quente|limpo} hoje.'),
 dict(who='Evan', en='But it\'s {cold|windy|cool}!', pt='Mas está {frio|ventando|fresco}!'),
 dict(who='You', en='Chicago is always windy.', pt='Chicago é sempre ventosa.'),
 dict(who='Evan', en='Is it {hot|warm|sunny} in summer?', pt='{Faz calor|Está quente|Faz sol} no verão?'),
 dict(who='You', en='Yes, very hot. And in winter, {snow|ice|wind}!', pt='Sim, muito calor. E no inverno, {neve|gelo|vento}!'),
 dict(who='Evan', en='Wow. I need a {warm|winter|thick} coat.', pt='Nossa. Preciso de um casaco {quente|de inverno|grosso}.'),
 dict(who='You', en='Yes, you do!', pt='Precisa mesmo!'),
 dict(who='Evan', en='Stay {warm|safe|dry}!', pt='Fique {aquecido|em segurança|seco}!'),
],
vocab=[
 dict(w='sunny', pt='ensolarado', e='☀️', ex=['It\'s sunny today.', 'Sunny days are nice.']),
 dict(w='rain', pt='chuva', e='🌧️', ex=['I need an umbrella in the rain.', 'The rain is cold.']),
 dict(w='snow', pt='neve', e='❄️', ex=['We have snow in winter.', 'The snow is white.']),
 dict(w='cold', pt='frio', e='🥶', ex=['It\'s cold in Chicago in winter.', 'My hands are cold.']),
 dict(w='hot', pt='quente; calor', e='🥵', ex=['It\'s hot in summer.', 'The coffee is hot.']),
 dict(w='windy', pt='ventoso', e='💨', ex=['Chicago is windy.', 'It\'s a windy day.']),
],
molds=[
 dict(title='Descrever o tempo', frame='It\'s {weather} today, but it\'s {weather2}.', slots=[dict(key='weather', opts=['sunny', 'clear', 'dry']), dict(key='weather2', opts=['cold', 'windy', 'cool'])], model='It\'s sunny today, but it\'s cold.', note='But liga dois fatos que parecem contrários: sol, mas frio.'),
 dict(title='Falar das estações', frame='In winter, it\'s {cold}. In summer, it\'s {hot}.', slots=[dict(key='cold', opts=['cold', 'snowy', 'windy']), dict(key='hot', opts=['hot', 'sunny', 'warm'])], model='In winter, it\'s cold. In summer, it\'s hot.', note='Estação com in: in winter. Para o tempo, it\'s + adjetivo.'),
 dict(title='Escrever uma dica', frame='It\'s {tip}!', slots=[dict(key='tip', opts=['cold. Take a coat', 'rainy. Take an umbrella', 'sunny. Take a hat'])], model='It\'s cold. Take a coat!', note='Take + objeto é uma sugestão. O item combina com o tempo.'),
],
sounds=[
 dict(say='Nice morning, isn\'t it?', tag='entonação: isn\'t it?', tip='Em "isn\'t it?" a voz sobe um pouco, pedindo concordância. Nice e MOR são fortes.'),
 dict(say='It\'s very hot.', tag='ligação: it\'s very', tip='It\'s very soa "it-sve-ri". A sílaba forte de very é a primeira.'),
 dict(say='I need a warm coat.', tag='ritmo: palavras fortes', tip='Bata NEED, WARM, COAT. I e a ficam fracos: "ai-NEED-a-WARM-COAT".'),
],
role=dict(turns=[
 dict(npc='Nice morning, isn\'t it?', opts=[
  dict(en='Yes, it\'s sunny today.', pt='Sim, está ensolarado hoje.', reply='But it\'s cold!'),
  dict(en='Yes, it is. It\'s a nice day.', pt='É mesmo. Está um bom dia.', reply='But it\'s cold!'),
  dict(en='Yes! The sun is out.', pt='Sim! O sol saiu.', reply='But it\'s cold!')]),
 dict(npc='But it\'s cold!', opts=[
  dict(en='Chicago is always windy.', pt='Chicago é sempre ventosa.', reply='Is it hot in summer?'),
  dict(en='Yes, it is. It\'s windy too.', pt='É verdade. E está ventando.', reply='Is it hot in summer?'),
  dict(en='A little. Take a coat!', pt='Um pouco. Leve um casaco!', reply='Is it hot in summer?')]),
 dict(npc='Is it hot in summer?', opts=[
  dict(en='Yes, very hot. And in winter, snow!', pt='Sim, muito calor. E no inverno, neve!', reply='Wow. I need a warm coat.'),
  dict(en='Yes, it is hot in July.', pt='Sim, faz calor em julho.', reply='Wow. I need a warm coat for winter!'),
  dict(en='Yes, and it\'s sometimes rainy.', pt='Sim, e às vezes chove.', reply='Wow. I need a warm coat and an umbrella.')]),
 dict(npc='Wow. I need a warm coat.', opts=[
  dict(en='Yes, you do!', pt='Precisa mesmo!', reply='Thanks! Stay warm!'),
  dict(en='Yes. There are good stores near here.', pt='Sim. Tem boas lojas perto daqui.', reply='Great, thanks! Stay warm!'),
  dict(en='I need one too!', pt='Eu também preciso de um!', reply='Let\'s go together! Stay warm!')]),
], change=['Evan pergunta se chove muito em Chicago; responda e peça a previsão de amanhã.', 'Você mora no Brasil e descreve o tempo na sua cidade em julho.', 'De repente começa a chover e você sugere entrar numa cafeteria.']),
writing=dict(task='Escreva 2 ou 3 frases sobre o tempo na sua cidade hoje e em cada estação, com um conselho.', model='It\'s sunny today, but it\'s cold. In winter, it\'s very cold. Take a warm coat!', kw=['sunny', 'cold', 'winter', 'coat'], checks=['Descreveu o tempo de hoje.', 'Falou de uma estação com in.', 'Deu um conselho com Take ou Stay.']),
scenes=dict(pool=['street', 'park', 'snow', 'nyc', 'beach'], npc=dict(g='m', role='neighbor'), you=dict(g='f')),
convo=dict(npc=dict(name='Evan'), story='Numa praça de Chicago, você e Evan falam do tempo.', turns=[
 dict(npc='Nice morning, isn\'t it?', pt='Bela manhã, né?', opts=[
  dict(en='Yes, it\'s sunny today.', pt='Sim, está ensolarado hoje.', ok=True, fb='Concorda e descreve.'),
  dict(en='No, I am a morning.', pt='Não, eu sou uma manhã.', ok=False, fb='Frase sem sentido: use it\'s para o tempo.'),
  dict(en='Good night!', pt='Boa noite!', ok=False, fb='É manhã; good night é despedida à noite.')]),
 dict(npc='But it\'s cold!', pt='Mas está frio!', opts=[
  dict(en='Chicago is always windy.', pt='Chicago é sempre ventosa.', ok=True, fb='Explica com um fato sobre a cidade.'),
  dict(en='I have cold.', pt='Eu tenho frio (traduzido ao pé da letra).', ok=False, fb='Em inglês: I am cold ou It is cold.'),
  dict(en='Yes, I am.', pt='Sim, eu sou.', ok=False, fb='Para o tempo use it\'s, não I am.')]),
 dict(npc='Is it hot in summer?', pt='Faz calor no verão?', opts=[
  dict(en='Yes, very hot. And in winter, snow!', pt='Sim, muito calor. E no inverno, neve!', ok=True, fb='Responde e acrescenta o inverno.'),
  dict(en='It is winter now.', pt='Agora é inverno.', ok=False, fb='Ele perguntou do verão, não da estação atual.'),
  dict(en='I like summer.', pt='Gosto de verão.', ok=False, fb='Não responde se faz calor.')]),
 dict(npc='Wow. I need a warm coat.', pt='Nossa. Preciso de um casaco quente.', opts=[
  dict(en='It\'s very hot.', pt='Está muito quente.', ok=False, fb='Contradiz o que você disse sobre o inverno.'),
  dict(en='Yes, you do!', pt='Precisa mesmo!', ok=True, fb='Concorda de forma natural.'),
  dict(en='I need a warm coat too, please.', pt='Eu também preciso de um casaco quente, por favor.', ok=False, fb='Please não encaixa: ele não ofereceu nada.')]),
 dict(npc='Stay warm!', pt='Fique aquecido!', opts=[
  dict(en='Thanks! You too. Bye!', pt='Valeu! Você também. Tchau!', ok=True, fb='Despedida natural.'),
  dict(en='Is it cold?', pt='Está frio?', ok=False, fb='A conversa está acabando.'),
  dict(en='Nice morning, isn\'t it?', pt='Bela manhã, né?', ok=False, fb='Isso foi dito no início.')]),
]),
)
