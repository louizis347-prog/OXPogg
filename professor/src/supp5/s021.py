"""Suplemento Quest v5 · aula 21: What's the weather? + regular Four Seasons (Vivaldi)."""
SUPP = {
 'reg': 66,
 'badge': {'icon': '🌦️', 'name': 'Weather Talker', 'desc': 'Talk about the weather like a Chicagoan'},
 'sticker': {'cat': 'Everyday culture', 'title': 'Weather Small Talk', 'sub': 'Nice day, huh?'},
 'culture': {
  'hook': 'In the USA, people talk about the weather all the time. It is the easiest way to start a friendly chat with a neighbor, a driver or a stranger in line.',
  'polite': 'Start with **Nice day, isn’t it?** or **Cold enough for you?** Then ask a short question to keep talking.',
  'mythfact': [
   {'s': 'In the USA, the weather is a common small-talk topic.', 'ans': True, 'why': 'Saying “Nice day, huh?” is a normal way to start a conversation.'},
   {'s': 'Americans usually say the temperature in Celsius.', 'ans': False, 'why': 'The USA mostly uses Fahrenheit, not Celsius.'},
   {'s': 'Water freezes at 32 degrees Fahrenheit.', 'ans': True, 'why': '32°F is the same as 0°C.'},
   {'s': 'The weather is the same in every part of the USA.', 'ans': False, 'why': 'The USA is very big: Florida is warm and Alaska is very cold.'},
   {'s': 'Chicago has the nickname “the Windy City”.', 'ans': True, 'why': 'Chicago is famous by this nickname. It is often linked to the wind off Lake Michigan, but some people say it was about talkative politicians.'}],
  'wild': [
   {'kind': 'Weather app', 'lines': ['**Today** · Sunny · High 82°F', '**Tonight** · Clear · Low 64°F', '**Tomorrow** · Rain · High 70°F'], 'decode': {'q': 'What is the weather tomorrow?', 'opts': ['Rain', 'Sunny', 'Snow'], 'ans': 0, 'why': 'The app says “Tomorrow · Rain”.'}},
   {'kind': 'Text message', 'lines': ['Brr! It’s freezing today.', 'Bring a warm coat and a hat.', 'See you at the park at 3!'], 'decode': {'q': 'What should you bring?', 'opts': ['A swimsuit', 'A warm coat and a hat', 'An umbrella'], 'ans': 1, 'why': '“Bring a warm coat and a hat.”'}}],
  'compare': {'br': 'In Brazil, people say “Que calor!” or “Tá chovendo” and use Celsius: 30 degrees is a hot day.', 'us': 'In the USA, people use Fahrenheit: 85 degrees is hot and 30 degrees is very cold. Chicago has hot summers and snowy winters.', 'tip': 'Do not worry about the numbers. Say hot, warm, cool or cold.', 'ask': 'What is the weather like today where you live? Say it in English.'},
  'quiz': [
   {'q': 'A neighbor says, “Nice morning, isn’t it?” You say…', 'opts': ['Yes, it’s sunny today.', 'I am a morning.', 'No, I have sun.'], 'ans': 0, 'why': 'Agree and add a short comment.'},
   {'q': 'Which sentence is correct?', 'opts': ['Is cold today.', 'It cold today.', 'It’s cold today.'], 'ans': 2, 'why': 'In English the weather needs It’s.'},
   {'q': 'Which temperature scale is common in the USA?', 'opts': ['Kelvin', 'Fahrenheit', 'Celsius'], 'ans': 1, 'why': 'Fahrenheit is the everyday scale in the USA.'}]},
 'reading': {
  'genre': 'Postcard', 'title': 'Four seasons, one city',
  'text': [
   'Hello from **Chicago**! I live here, and the weather is always a topic. People say, “**Nice day, huh?**” in the elevator, at the bus stop and in the café.',
   'In **summer**, it is very hot and sunny. We go to the lake and eat ice cream. In **autumn**, it is cool and windy. The trees are red and yellow. Chicago has a nickname: the Windy City.',
   'In **winter**, it is freezing! There is a lot of snow, and I say, “**Brr! Bundle up.**” I wear a warm coat, a hat and gloves. When it is pouring rain, I bring an umbrella. **It’s freezing out there!**',
   'In **spring**, the days are warm again. Flowers come out, and the birds sing. Last week, I listened to “The Four Seasons” by Antonio Vivaldi. It is a famous piece of music from Italy, from about 1725. It has one part for each season. In the spring part, you can hear birds.',
   'Which season do you like? I like spring, but my friend Evan likes snow. He says, “**I need a warm coat**,” and then he laughs. Write soon, and **stay warm**!'],
  'glossary': [{'w': 'weather', 'pt': 'tempo (clima)'}, {'w': 'windy', 'pt': 'ventoso'}, {'w': 'freezing', 'pt': 'congelante'}, {'w': 'snow', 'pt': 'neve'}, {'w': 'bundle up', 'pt': 'agasalhar-se'}, {'w': 'gloves', 'pt': 'luvas'}, {'w': 'umbrella', 'pt': 'guarda-chuva'}, {'w': 'autumn', 'pt': 'outono'}, {'w': 'nickname', 'pt': 'apelido'}, {'w': 'pouring', 'pt': 'chovendo forte'}],
  'fast': {'q': 'What is this postcard about?', 'opts': ['The weather and seasons in Chicago', 'A trip to Italy', 'A pizza recipe'], 'ans': 0, 'why': 'The writer talks about the seasons in Chicago.'},
  'scan': [{'q': 'What is Chicago’s nickname?', 'ans': 'the Windy City', 'alt': ['windy city']}, {'q': 'Who wrote “The Four Seasons”?', 'ans': 'Antonio Vivaldi', 'alt': ['vivaldi']}, {'q': 'What does the writer wear in winter?', 'ans': 'a warm coat, a hat and gloves', 'alt': ['coat', 'a warm coat']}],
  'tf': [{'s': 'Winter in Chicago is warm.', 'ans': False, 'why': '“In winter, it is freezing!”'}, {'s': 'People talk about the weather in Chicago.', 'ans': True, 'why': '“The weather is always a topic.”'}, {'s': 'Vivaldi’s music has a part for each season.', 'ans': True, 'why': '“It has one part for each season.”'}, {'s': 'The writer’s friend Evan likes summer best.', 'ans': False, 'why': 'Evan likes snow.'}],
  'order': ['The writer says hello from Chicago.', 'Summer is hot and sunny.', 'Winter is freezing with snow.', 'Spring brings warm days and flowers.', 'The writer asks about a favorite season.'],
  'ctx': [{'sent': 'It is freezing in winter.', 'w': 'freezing', 'opts': ['very cold', 'very hot', 'very short'], 'ans': 0, 'why': 'Freezing = very cold.'}, {'sent': 'I say, “Bundle up.”', 'w': 'Bundle up', 'opts': ['Take a nap', 'Put on warm clothes', 'Open the window'], 'ans': 1, 'why': 'Bundle up = wear warm clothes.'}, {'sent': 'It is pouring rain today.', 'w': 'pouring', 'opts': ['raining a little', 'raining a lot', 'not raining'], 'ans': 1, 'why': 'Pouring = raining very hard.'}],
  'chunkHunt': ['Nice day, huh?', 'It’s freezing out there!', 'Bundle up.', 'Stay warm!'],
  'think': 'What is the weather like in your city in each season? Which season do you like best?'},
 'convo': {'npc': {'name': 'Evan'}, 'story': 'You meet your neighbor Evan on a cold morning in Chicago. Talk about the weather.',
  'turns': [
   {'npc': 'Nice morning, isn’t it?', 'pt': 'Bela manhã, né?', 'opts': [
    {'en': 'Yes, it’s sunny today.', 'pt': 'Sim, está ensolarado hoje.', 'ok': True, 'fb': 'Agree and add a comment.'},
    {'en': 'Yes, is sunny today.', 'pt': 'Sim, é ensolarado hoje.', 'ok': False, 'fb': 'Use It’s for the weather.'},
    {'en': 'I am sunny.', 'pt': 'Eu sou ensolarado.', 'ok': False, 'fb': 'The weather is it, not I.'}]},
   {'npc': 'But it’s cold!', 'pt': 'Mas está frio!', 'opts': [
    {'en': 'It has cold.', 'pt': 'Tem frio.', 'ok': False, 'fb': 'Use It’s cold.'},
    {'en': 'Chicago is always windy.', 'pt': 'Chicago é sempre ventosa.', 'ok': True, 'fb': 'A natural comment about the city.'},
    {'en': 'I like pizza.', 'pt': 'Eu gosto de pizza.', 'ok': False, 'fb': 'It does not answer.'}]},
   {'npc': 'Is it hot in summer?', 'pt': 'Faz calor no verão?', 'opts': [
    {'en': 'Yes, very hot. And in winter, snow!', 'pt': 'Sim, muito calor. E no inverno, neve!', 'ok': True, 'fb': 'Short answer plus extra information.'},
    {'en': 'Yes, I am hot.', 'pt': 'Sim, eu sou quente.', 'ok': False, 'fb': 'It’s hot, not I am hot, for weather.'},
    {'en': 'In summer is hot yes.', 'pt': 'No verão é quente sim.', 'ok': False, 'fb': 'Use a full sentence: Yes, it is.'}]},
   {'npc': 'Wow. I need a warm coat.', 'pt': 'Nossa. Preciso de um casaco quente.', 'opts': [
    {'en': 'You need a coat warm.', 'pt': 'Você precisa de um casaco quente.', 'ok': False, 'fb': 'Adjective first: a warm coat.'},
    {'en': 'No, thank you.', 'pt': 'Não, obrigado.', 'ok': False, 'fb': 'Evan did not offer anything.'},
    {'en': 'Yes, you do!', 'pt': 'Precisa mesmo!', 'ok': True, 'fb': 'Short answer with do.'}]},
   {'npc': 'Stay warm!', 'pt': 'Fique aquecido!', 'opts': [
    {'en': 'You too! Bye!', 'pt': 'Você também! Tchau!', 'ok': True, 'fb': 'Natural reply.'},
    {'en': 'I am warm yes.', 'pt': 'Estou quente sim.', 'ok': False, 'fb': 'It does not wish him well.'},
    {'en': 'Good afternoon!', 'pt': 'Boa tarde!', 'ok': False, 'fb': 'It is morning.'}]}]},
 'errors': [
  {'wrong': 'Is cold today.', 'fix': 'It’s cold today.', 'alt': 'Has cold today.', 'why': 'English needs the subject It for weather.'},
  {'wrong': 'I am cold in Chicago in winter.', 'fix': 'It is cold in Chicago in winter.', 'alt': 'It has cold in Chicago.', 'why': 'I am cold = my body feels cold. It is cold = the weather.'},
  {'wrong': 'It’s raining a lot of.', 'fix': 'It’s raining a lot.', 'alt': 'It rains a lot of.', 'why': 'A lot ends the sentence by itself.'},
  {'wrong': 'In the summer is very hot.', 'fix': 'It is very hot in summer.', 'alt': 'In summer have hot.', 'why': 'Start with It is, and use in summer without the.'}],
 'homework': 'Write 5 sentences about the weather in your city in each season, and send them to your teacher.',
 'homework_items': ['Write 5 sentences about the weather in your city.', 'Record yourself saying “Nice day, huh?” and 2 answers.', 'Shadow the dialogue with Evan.', 'Review: It’s sunny / cold / windy / hot. Stay warm!']}
