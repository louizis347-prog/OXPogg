"""Suplemento Quest v5 · aula 184: A flat tire + regular Stopped and planned (Thomas and Friends)."""
SUPP = {
 'reg': 200,
 'badge': {'icon': '🛞', 'name': 'Road Ready', 'desc': 'Call roadside help and explain a flat tire'},
 'culture': {
  'hook': 'In the USA, many drivers have a roadside assistance plan. If a tire goes flat, you stop in a safe place, call, and say where you are and what car you have.',
  'mythfact': [
   {'s': 'On a highway, you should stop in a safe place and stay away from the traffic.', 'ans': True, 'why': 'Safety comes first, and many people also turn on their hazard lights.'},
   {'s': 'Roadside assistance asks where you are.', 'ans': True, 'why': 'They need your location to send help.'},
   {'s': 'Many cars come with a full spare tire.', 'ans': False, 'why': 'Many new cars have a small spare tire or only a repair kit, so check your car.'},
   {'s': 'It is a good idea to know your exit number or a nearby sign.', 'ans': True, 'why': 'Exit numbers and mile signs help helpers find you fast.'},
   {'s': '“Thomas & Friends” is a children’s TV show about trains.', 'ans': True, 'why': 'It is based on stories by Rev. W. Awdry.'}],
  'wild': [
   {'kind': 'Roadside sign', 'lines': ['**Exit 5**', 'Main Street – 1 mile', 'Gas – Food'], 'decode': {'q': 'What exit is it?', 'opts': ['Exit 5', 'Exit 1', 'Exit 10'], 'ans': 0, 'why': 'The sign says Exit 5.'}},
   {'kind': 'Text from roadside assistance', 'lines': ['Hi Sam, help is on the way.', '**Arrival time: 25 minutes**', 'Please stay in a safe place.'], 'decode': {'q': 'How long until help arrives?', 'opts': ['25 minutes', '5 minutes', '2 hours'], 'ans': 0, 'why': 'Arrival time: 25 minutes.'}}],
  'compare': {'br': 'In Brazil, drivers often call a “guincho” or an insurance helpline and say the road name and the kilometer.', 'us': 'In the USA, drivers say the highway number, the exit, or the nearest sign and the car color and brand.', 'tip': 'Say: “I have a flat tire. I’m on Highway 10, near exit 5.”', 'ask': 'How do you say your location in English?'},
  'quiz': [
   {'q': 'You call for help. You say…', 'opts': ['I have a flat tire.', 'I am a flat tire.', 'My tire has flat.'], 'ans': 0, 'why': 'Use I have a flat tire.'},
   {'q': 'The operator asks, “What kind of car do you have?” You say…', 'opts': ['A white Honda.', 'I have white of Honda.', 'It is Honda a white.'], 'ans': 0, 'why': 'Use a + color + brand.'},
   {'q': 'The operator asks if you are safe. You say…', 'opts': ['Yes, I’m on the side of the road.', 'Yes, I am side road.', 'Yes, I am safe road.'], 'ans': 0, 'why': 'Use on the side of the road.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Stop on the side',
  'text': [
   'Sam is driving on a highway near **Tulsa**. The road is quiet and sunny. Suddenly, the car shakes and goes slow. He hears a loud sound. He stops on the side of the road and turns on his lights.',
   'Sam gets out and looks at the wheel. The tire is flat. He calls roadside assistance. “**Hello, roadside assistance. How can I help?**” “**Hi. I have a flat tire.**” “**Are you safe right now?**” “**Yes, I’m on the side of the road.**”',
   '“**What’s your location?**” “**Highway ten, near exit five.**” “**What kind of car do you have?**” “**A white Honda.**” “**Do you have a spare tire?**” Sam opens the trunk. He sees a small spare tire and a tool bag.',
   '“**Yes, I have a spare**,” he says. “**Stay put. Help is on the way**,” the operator says. “**It will take about twenty minutes.**” Sam waits near the car, away from the cars. He keeps his phone in his hand.',
   'While he waits, Sam thinks about “Thomas & Friends,” a children’s TV show about little trains. Thomas is a blue engine. Sometimes he stops, and sometimes he makes a plan. Today Sam makes a plan, too: call, wait, and stay safe. Soon a truck comes, and a kind man says hello.'],
  'glossary': [{'w': 'highway', 'pt': 'rodovia'}, {'w': 'tire', 'pt': 'pneu'}, {'w': 'flat', 'pt': 'furado, vazio'}, {'w': 'wheel', 'pt': 'roda'}, {'w': 'location', 'pt': 'localização'}, {'w': 'exit', 'pt': 'saída'}, {'w': 'spare', 'pt': 'estepe, reserva'}, {'w': 'trunk', 'pt': 'porta-malas'}, {'w': 'tool', 'pt': 'ferramenta'}, {'w': 'operator', 'pt': 'atendente'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A driver calls for help with a flat tire', 'A man buys a new car', 'A boy rides a train'], 'ans': 0, 'why': 'Sam has a flat tire and calls roadside assistance.'},
  'scan': [{'q': 'What kind of car does Sam have?', 'ans': 'a white Honda', 'alt': ['white Honda', 'Honda']}, {'q': 'Near which exit is Sam?', 'ans': 'exit five', 'alt': ['five', 'exit 5', '5']}, {'q': 'How long will help take?', 'ans': 'about twenty minutes', 'alt': ['twenty minutes', '20 minutes']}],
  'tf': [{'s': 'Sam stops on the side of the road.', 'ans': True, 'why': 'He stops and turns on his lights.'}, {'s': 'The tire is fine.', 'ans': False, 'why': 'The tire is flat.'}, {'s': 'Sam has a spare tire.', 'ans': True, 'why': 'He sees a small spare in the trunk.'}, {'s': 'Sam stands in the middle of the road.', 'ans': False, 'why': 'He waits near the car, away from the cars.'}],
  'order': ['The car shakes and goes slow.', 'Sam stops on the side.', 'Sam calls roadside assistance.', 'Sam says his location.', 'A truck comes.'],
  'ctx': [{'sent': 'The tire is flat.', 'w': 'flat', 'opts': ['it has no air', 'it is new', 'it is red'], 'ans': 0, 'why': 'A flat tire has no air.'}, {'sent': 'What’s your location?', 'w': 'location', 'opts': ['the place where you are', 'your car color', 'your name'], 'ans': 0, 'why': 'Location = where you are.'}, {'sent': 'Stay put.', 'w': 'put', 'opts': ['stay in the same place', 'go away', 'drive fast'], 'ans': 0, 'why': 'Stay put = do not move.'}],
  'chunkHunt': ['I have a flat tire.', 'Are you safe right now?', 'What’s your location?', 'A white Honda.', 'Do you have a spare tire?'],
  'think': 'What do you need to say when you call for help on the road?'},
 'convo': {'npc': {'name': 'Luis'}, 'story': 'You are in your car near Tulsa. Your tire is flat. You call roadside assistance and Luis answers.', 'turns': [
  {'npc': 'Hello, roadside assistance. How can I help?', 'pt': 'Olá, assistência na estrada. Como posso ajudar?', 'opts': [
   {'en': 'Hi. I have a flat tire.', 'pt': 'Oi. Estou com um pneu furado.', 'ok': True, 'fb': 'Clear problem.'},
   {'en': 'Hi. I am a flat tire.', 'pt': 'Oi. Eu sou um pneu furado.', 'ok': False, 'fb': 'Use I have, not I am.'},
   {'en': 'Hi. Thank you very much.', 'pt': 'Oi. Muito obrigado.', 'ok': False, 'fb': 'Too early to say thanks.'}]},
  {'npc': 'Are you safe right now?', 'pt': 'Você está seguro agora?', 'opts': [
   {'en': 'Yes, I am in the road middle.', 'pt': 'Sim, estou no meio da estrada.', 'ok': False, 'fb': 'It is not safe, and the phrase is wrong.'},
   {'en': 'Yes, I’m on the side of the road.', 'pt': 'Sim, estou no acostamento.', 'ok': True, 'fb': 'Safe place.'},
   {'en': 'Yes, I have a flat tire.', 'pt': 'Sim, estou com pneu furado.', 'ok': False, 'fb': 'It does not answer the question.'}]},
  {'npc': 'What’s your location?', 'pt': 'Qual é sua localização?', 'opts': [
   {'en': 'Highway ten, near exit five.', 'pt': 'Rodovia dez, perto da saída cinco.', 'ok': True, 'fb': 'Gives a clear place.'},
   {'en': 'I am a white Honda.', 'pt': 'Eu sou um Honda branco.', 'ok': False, 'fb': 'That is the car, not the place.'},
   {'en': 'My location is yes.', 'pt': 'Minha localização é sim.', 'ok': False, 'fb': 'It does not make sense.'}]},
  {'npc': 'What kind of car do you have?', 'pt': 'Que carro você tem?', 'opts': [
   {'en': 'I have a car of white Honda.', 'pt': 'Eu tenho um carro de Honda branco.', 'ok': False, 'fb': 'Say a white Honda.'},
   {'en': 'A white Honda.', 'pt': 'Um Honda branco.', 'ok': True, 'fb': 'Short and clear.'},
   {'en': 'Near exit five.', 'pt': 'Perto da saída cinco.', 'ok': False, 'fb': 'You already said the place.'}]},
  {'npc': 'Do you have a spare tire?', 'pt': 'Você tem estepe?', 'opts': [
   {'en': 'Yes, I do. It’s in the trunk.', 'pt': 'Sim, tenho. Está no porta-malas.', 'ok': True, 'fb': 'Answers and gives the place.'},
   {'en': 'Yes, I spare it.', 'pt': 'Sim, eu o poupo.', 'ok': False, 'fb': 'Spare is a noun here: a spare tire.'},
   {'en': 'No, I am safe.', 'pt': 'Não, estou seguro.', 'ok': False, 'fb': 'It does not answer the question.'}]}]},
 'errors': [
  {'wrong': 'My tire is empty.', 'fix': 'I have a flat tire.', 'alt': 'I have a tire flat.', 'why': 'The usual phrase is a flat tire, with flat before the noun.'},
  {'wrong': 'I am in the lateral of the road.', 'fix': 'I’m on the side of the road.', 'alt': 'I’m at the side of road.', 'why': 'Say on the side of the road.'},
  {'wrong': 'I have a Honda white.', 'fix': 'I have a white Honda.', 'alt': 'I have a Honda of white.', 'why': 'The color comes before the noun.'},
  {'wrong': 'I am near of exit five.', 'fix': 'I’m near exit five.', 'alt': 'I’m near to of exit five.', 'why': 'Near does not need of.'}],
 'homework': 'Write a short dialogue: you call roadside assistance for a flat tire and say where you are.',
 'homework_items': ['Write your car: color + brand.', 'Say aloud: I have a flat tire.', 'Listen to the dialogue and shadow Luis.', 'Review: road / wheel / slow / tool / flat / spare.']}
