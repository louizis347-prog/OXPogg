"""Suplemento Quest v5 · aula 170: Calling a ride + regular I’d like to book a room (Hotel Transylvania)."""
SUPP = {
 'reg': 169,
 'badge': {'icon': '🚗', 'name': 'Ride Ready', 'desc': 'Book a ride and talk to the driver'},
 'culture': {
  'hook': 'In many US cities, people book a ride with an app. The app shows the car and the driver, and a short, friendly talk starts every trip.',
  'mythfact': [
   {'s': 'With a ride app, you can see the driver’s name and the car before the ride.', 'ans': True, 'why': 'Most apps show the name, the car and sometimes a photo.'},
   {'s': 'You can get in any car that stops near you.', 'ans': False, 'why': 'Check the car, the name and the plate in the app first.'},
   {'s': 'It is common to say hello and confirm the destination.', 'ans': True, 'why': 'Many drivers ask, “Going to the airport?” to be sure.'},
   {'s': 'Passengers usually put on the seatbelt.', 'ans': True, 'why': 'A seatbelt is normal and often required by law.'},
   {'s': 'In “Hotel Transylvania”, Dracula runs a hotel for monsters.', 'ans': True, 'why': 'It is an animated film from 2012.'}],
  'wild': [
   {'kind': 'Ride app screen', 'lines': ['**Your driver: Marco**', 'Blue Toyota · 4 min away', 'Pickup: Main Street'], 'decode': {'q': 'How far is the driver?', 'opts': ['4 minutes', '40 minutes', '4 miles'], 'ans': 0, 'why': 'The screen says 4 min away.'}},
   {'kind': 'Airport sign', 'lines': ['**Ride pickup**', 'Level 1, door 3', 'Terminal 2'], 'decode': {'q': 'Where is the ride pickup?', 'opts': ['Level 1, door 3', 'Level 3, door 1', 'Terminal 4'], 'ans': 0, 'why': 'The sign says Level 1, door 3.'}}],
  'compare': {'br': 'In Brazil, people also use apps for rides, and many sit in the back seat.', 'us': 'In the USA, many passengers also sit in the back, but you can ask politely if you can sit in the front. Drivers often confirm your name.', 'tip': 'Say: “Hi! I’m Leo. Going to the airport.”', 'ask': 'Do you use a ride app? Say it in English.'},
  'quiz': [
   {'q': 'The driver asks: “Are you Leo?” You say…', 'opts': ['Yes! You’re my driver, right?', 'Yes, I am a driver.', 'Leo is a car.'], 'ans': 0, 'why': 'Confirm and check the driver.'},
   {'q': 'You want the front seat. You ask…', 'opts': ['Can I sit in the front?', 'Can I sit at the front of the car in?', 'I sit front.'], 'ans': 0, 'why': 'Can I + verb is polite.'},
   {'q': 'What does “buckle up” mean?', 'opts': ['put on the seatbelt', 'open the door', 'start the car'], 'ans': 0, 'why': 'Buckle up = fasten the seatbelt.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Leo takes a ride',
  'text': [
   'Leo is in **Los Angeles**. He needs to go to the airport for a morning flight. He opens an app on his phone and books a ride.',
   'The app shows the car, the driver’s name and the time. A small blue car stops at the door. The driver is Marco. “**Hi! Are you Leo?**” “**Yes! You’re my driver, right?**” “**That’s right. Going to the airport?**” “**Yes, please. Terminal two.**”',
   'Marco says, “**Let me put your bag in the trunk.**” Leo says, “**Thanks. Can I sit in the front?**” “**Sure, buckle up.**” Leo puts on his seatbelt. “**How long will it take?**” “**About twenty minutes.**”',
   'On the road, Leo looks at the map in the app. The route is simple, and the traffic is light. Leo thinks of the film “Hotel Transylvania.” In the film, Dracula runs a big hotel for monsters, and the guests come from far away. Leo smiles. “My trip is easier,” he thinks.',
   'At terminal two, Marco opens the trunk. “Have a good flight!” “Thank you! **Five stars** for you!” Leo says. He gives the driver a good rating in the app and walks into the airport.'],
  'glossary': [{'w': 'books', 'pt': 'reserva, pede (uma corrida)'}, {'w': 'app', 'pt': 'aplicativo'}, {'w': 'driver', 'pt': 'motorista'}, {'w': 'trunk', 'pt': 'porta-malas'}, {'w': 'buckle up', 'pt': 'colocar o cinto'}, {'w': 'route', 'pt': 'rota, trajeto'}, {'w': 'traffic', 'pt': 'trânsito'}, {'w': 'monsters', 'pt': 'monstros'}, {'w': 'guests', 'pt': 'hóspedes'}, {'w': 'rating', 'pt': 'avaliação'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A man takes a ride to the airport', 'A woman buys a jacket', 'A boy plays soccer'], 'ans': 0, 'why': 'Leo books a ride to the airport.'},
  'scan': [{'q': 'What is the driver’s name?', 'ans': 'Marco', 'alt': ['marco']}, {'q': 'Where does Marco put Leo’s bag?', 'ans': 'in the trunk', 'alt': ['trunk', 'the trunk']}, {'q': 'How long is the ride?', 'ans': 'about twenty minutes', 'alt': ['twenty minutes', '20 minutes', 'twenty']}],
  'tf': [{'s': 'Leo uses an app to book the ride.', 'ans': True, 'why': 'He opens an app and books a ride.'}, {'s': 'Leo goes to terminal four.', 'ans': False, 'why': 'He goes to terminal two.'}, {'s': 'Leo sits in the front.', 'ans': True, 'why': 'Marco says sure.'}, {'s': 'The traffic is very heavy.', 'ans': False, 'why': 'The traffic is light.'}],
  'order': ['Leo books a ride in the app.', 'Marco asks if he is Leo.', 'Marco puts the bag in the trunk.', 'Leo puts on his seatbelt.', 'Leo gives the driver five stars.'],
  'ctx': [{'sent': 'Marco is the driver.', 'w': 'driver', 'opts': ['a person who drives a car', 'a person who cooks', 'a kind of phone'], 'ans': 0, 'why': 'A driver drives the car.'}, {'sent': 'The traffic is light.', 'w': 'traffic', 'opts': ['the cars on the road', 'the weather', 'the music'], 'ans': 0, 'why': 'Traffic = cars on the road.'}, {'sent': 'Buckle up, please.', 'w': 'buckle up', 'opts': ['put on your seatbelt', 'open the door', 'wait outside'], 'ans': 0, 'why': 'Buckle up = fasten the seatbelt.'}],
  'chunkHunt': ['Are you Leo?', 'Terminal two.', 'Can I sit in the front?', 'How long will it take?'],
  'think': 'Do you use ride apps? What do you check before you get in the car?'},
 'convo': {'npc': {'name': 'Marco'}, 'story': 'You booked a ride in Los Angeles. Marco is your driver.', 'turns': [
  {'npc': 'Hi! Are you Leo?', 'pt': 'Oi! Você é o Leo?', 'opts': [
   {'en': 'Yes! You’re my driver, right?', 'pt': 'Sim! Você é meu motorista, né?', 'ok': True, 'fb': 'Confirms and checks.'},
   {'en': 'No, I drive you.', 'pt': 'Não, eu dirijo você.', 'ok': False, 'fb': 'You are the passenger.'},
   {'en': 'I am a car.', 'pt': 'Eu sou um carro.', 'ok': False, 'fb': 'Does not make sense.'}]},
  {'npc': 'That’s right. Going to the airport?', 'pt': 'Isso. Vai para o aeroporto?', 'opts': [
   {'en': 'Yes, I go to airport.', 'pt': 'Sim, eu vou para aeroporto.', 'ok': False, 'fb': 'Say: to the airport.'},
   {'en': 'Terminal two, yes.', 'pt': 'Terminal dois, sim.', 'ok': False, 'fb': 'Understandable but short; better: Yes, please. Terminal two.'},
   {'en': 'Yes, please. Terminal two.', 'pt': 'Sim, por favor. Terminal dois.', 'ok': True, 'fb': 'Polite and clear.'}]},
  {'npc': 'Let me put your bag in the trunk.', 'pt': 'Deixe-me pôr sua mala no porta-malas.', 'opts': [
   {'en': 'Thanks. Can I sit in the front?', 'pt': 'Valeu. Posso sentar na frente?', 'ok': True, 'fb': 'Polite request.'},
   {'en': 'The trunk is an elephant.', 'pt': 'O porta-malas é um elefante.', 'ok': False, 'fb': 'Does not fit.'},
   {'en': 'I put my bag, thanks.', 'pt': 'Eu ponho minha mala, valeu.', 'ok': False, 'fb': 'He is helping you.'}]},
  {'npc': 'Sure, buckle up.', 'pt': 'Claro, coloque o cinto.', 'opts': [
   {'en': 'How long will it take?', 'pt': 'Quanto tempo vai demorar?', 'ok': True, 'fb': 'Natural next question.'},
   {'en': 'How much time it takes?', 'pt': 'Quanto tempo leva?', 'ok': False, 'fb': 'Say: How long will it take?'},
   {'en': 'I am buckle.', 'pt': 'Eu sou fivela.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'About twenty minutes.', 'pt': 'Uns vinte minutos.', 'opts': [
   {'en': 'No, I am twenty.', 'pt': 'Não, eu tenho vinte.', 'ok': False, 'fb': 'It does not fit.'},
   {'en': 'Terminal two, please.', 'pt': 'Terminal dois, por favor.', 'ok': False, 'fb': 'You already said it.'},
   {'en': 'Great, thank you!', 'pt': 'Ótimo, obrigado!', 'ok': True, 'fb': 'Short and friendly.'}]}]},
 'errors': [
  {'wrong': 'I go to airport.', 'fix': 'I’m going to the airport.', 'alt': 'I go to the airport now.', 'why': 'Use the airport; for now, I’m going.'},
  {'wrong': 'How much time takes?', 'fix': 'How long will it take?', 'alt': 'How many time will it take?', 'why': 'For duration: How long will it take?'},
  {'wrong': 'Can I sit in front?', 'fix': 'Can I sit in the front?', 'alt': 'Can I sit on the front?', 'why': 'Use in the front.'},
  {'wrong': 'Are you the driver of me?', 'fix': 'Are you my driver?', 'alt': 'You are driver of me?', 'why': 'Use my driver.'}],
 'homework': 'Write a short dialogue: you meet your ride driver and ask about the time to the airport.',
 'homework_items': ['Write the steps to book a ride in an app.', 'Say aloud: How long will it take?', 'Listen to the dialogue and shadow Leo.', 'Review the numbers up to sixty for minutes.']}
