"""Suplemento Quest v5 · aula 182: The power is out + regular A scary night (Frankenstein)."""
SUPP = {
 'reg': 179,
 'badge': {'icon': '🔦', 'name': 'Lights Out Pro', 'desc': 'Stay calm and talk about a power outage in English'},
 'culture': {
  'hook': 'Storms can cut the electricity in many parts of the USA. People keep a flashlight at home, check the street, and call the power company to report the problem.',
  'mythfact': [
   {'s': 'Many American homes keep a flashlight in a drawer.', 'ans': True, 'why': 'It is a simple and common way to prepare for a storm.'},
   {'s': 'After a blackout, people often call the power company.', 'ans': True, 'why': 'Many companies also have a website or app to report it.'},
   {'s': 'You should open the fridge many times in a power outage.', 'ans': False, 'why': 'A closed fridge keeps food cold longer.'},
   {'s': 'Matches and candles are always safe to leave alone.', 'ans': False, 'why': 'Never leave a candle burning when you leave the room.'},
   {'s': '“Frankenstein” is a novel by Mary Shelley.', 'ans': True, 'why': 'It was published in 1818.'}],
  'wild': [
   {'kind': 'Message from the power company', 'lines': ['**Power outage in your area.**', 'We are working to fix it.', 'Estimated time: 3 PM'], 'decode': {'q': 'What is the company doing?', 'opts': ['Fixing the problem', 'Closing the street', 'Moving away'], 'ans': 0, 'why': '“We are working to fix it.”'}},
   {'kind': 'Sticker on a flashlight box', 'lines': ['**Batteries included**', 'Keep in a safe place.', 'Check every six months.'], 'decode': {'q': 'What does “Batteries included” mean?', 'opts': ['Batteries are in the box', 'You need to buy batteries', 'It has no light'], 'ans': 0, 'why': 'Included means they come with it.'}}],
  'compare': {'br': 'In Brazil, many people say “acabou a luz” and often call the energy company or look at its app.', 'us': 'In the USA, people say “The power is out” and check a map on the power company’s website.', 'tip': 'Say: “The power is out. Is it only our building?”', 'ask': 'How do you say “acabou a luz” in English?'},
  'quiz': [
   {'q': 'The lights go off. You say…', 'opts': ['The power is out.', 'The power is exit.', 'The light is dead of me.'], 'ans': 0, 'why': 'Power is out = no electricity.'},
   {'q': 'You want a light. You ask…', 'opts': ['Do we have a flashlight?', 'Have we a flashlight to?', 'We have flashlight?'], 'ans': 0, 'why': 'Do we have…? is a natural question.'},
   {'q': 'You want to say where it is. You say…', 'opts': ['It is in the drawer.', 'It is on the drawer of.', 'It stay drawer.'], 'ans': 0, 'why': 'Use in + place.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Lights out in Houston',
  'text': [
   'It is a stormy night in **Houston**. Rosa and her brother Leo are at home. They are in the living room, and the TV is on. Suddenly, the lights go out. Everything is dark.',
   '“**Oh no! The lights went out**,” Rosa says. “**Is it only our building?**” Leo asks. Rosa goes to the window. “**Let me check outside. No, the whole street.**” The rain is heavy, and the wind is strong.',
   '“**Do we have a flashlight?**” “**Yes, in the kitchen drawer.**” Leo walks slowly in the dark. He opens the drawer and finds it. “**I found it. It works!**” The small light is a big help.',
   '“**Let’s light some candles, too**,” Rosa says. She puts three candles on the table. Leo opens the fridge for a second, then closes it fast. The food stays cold. “**Should we call the power company?**” Leo asks. “**That sounds good**,” Rosa says.',
   'Rosa thinks about the novel “Frankenstein.” Mary Shelley wrote it in 1818. It is a scary story, and it is perfect for a night like this. But the lights come back after an hour. Now everything is **back to normal**. The room is bright, and the two friends laugh.'],
  'glossary': [{'w': 'storm', 'pt': 'tempestade'}, {'w': 'dark', 'pt': 'escuro'}, {'w': 'flashlight', 'pt': 'lanterna'}, {'w': 'drawer', 'pt': 'gaveta'}, {'w': 'candles', 'pt': 'velas'}, {'w': 'fridge', 'pt': 'geladeira'}, {'w': 'power', 'pt': 'energia'}, {'w': 'street', 'pt': 'rua'}, {'w': 'window', 'pt': 'janela'}, {'w': 'scary', 'pt': 'assustador'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Two people stay calm when the power goes out', 'A man buys a new TV', 'A woman goes to the beach'], 'ans': 0, 'why': 'Rosa and Leo find a flashlight and candles.'},
  'scan': [{'q': 'Where is the flashlight?', 'ans': 'in the kitchen drawer', 'alt': ['kitchen drawer', 'in the drawer', 'drawer']}, {'q': 'How many candles does Rosa put on the table?', 'ans': 'three', 'alt': ['3']}, {'q': 'How long are the lights out?', 'ans': 'an hour', 'alt': ['one hour', '1 hour', 'about an hour']}],
  'tf': [{'s': 'Only their building has no power.', 'ans': False, 'why': 'The whole street has no power.'}, {'s': 'The flashlight works.', 'ans': True, 'why': 'Rosa says, “It works!”'}, {'s': 'Leo opens the fridge for a long time.', 'ans': False, 'why': 'He opens it for a second and closes it fast.'}, {'s': 'The lights come back.', 'ans': True, 'why': 'They come back after an hour.'}],
  'order': ['The lights go out.', 'Rosa checks outside.', 'Leo finds the flashlight.', 'Rosa lights candles.', 'The lights come back.'],
  'ctx': [{'sent': 'Everything is dark.', 'w': 'dark', 'opts': ['with no light', 'with a lot of light', 'very hot'], 'ans': 0, 'why': 'Dark = no light.'}, {'sent': 'The wind is strong.', 'w': 'strong', 'opts': ['not weak', 'not warm', 'not near'], 'ans': 0, 'why': 'Strong = not weak.'}, {'sent': 'It is a scary story.', 'w': 'scary', 'opts': ['makes you afraid', 'makes you sleep', 'makes you laugh'], 'ans': 0, 'why': 'Scary = it gives you fear.'}],
  'chunkHunt': ['The lights went out.', 'Is it only our building?', 'Do we have a flashlight?', 'It works!', 'Should we call the power company?'],
  'think': 'What do you have at home for a power outage? Where do you keep it?'},
 'convo': {'npc': {'name': 'Rosa'}, 'story': 'You are at home in Houston with your friend Rosa. A storm comes and the lights go out.', 'turns': [
  {'npc': 'Oh no! The lights went out.', 'pt': 'Ai, não! As luzes apagaram.', 'opts': [
   {'en': 'Is it only our building?', 'pt': 'É só o nosso prédio?', 'ok': True, 'fb': 'A good question.'},
   {'en': 'The lights are out of me.', 'pt': 'As luzes estão fora de mim.', 'ok': False, 'fb': 'It does not make sense in English.'},
   {'en': 'Thank you for the light.', 'pt': 'Obrigado pela luz.', 'ok': False, 'fb': 'There is no light.'}]},
  {'npc': 'Let me check outside. No, the whole street.', 'pt': 'Vou ver lá fora. Não, a rua toda.', 'opts': [
   {'en': 'There is a storm tonight.', 'pt': 'Tem tempestade hoje à noite.', 'ok': True, 'fb': 'Gives a reason.'},
   {'en': 'There have a storm tonight.', 'pt': 'Tem tempestade hoje à noite.', 'ok': False, 'fb': 'Use There is, not There have.'},
   {'en': 'I am a storm.', 'pt': 'Eu sou uma tempestade.', 'ok': False, 'fb': 'It does not fit.'}]},
  {'npc': 'Do we have a flashlight?', 'pt': 'Temos uma lanterna?', 'opts': [
   {'en': 'Yes, in the kitchen drawer.', 'pt': 'Sim, na gaveta da cozinha.', 'ok': True, 'fb': 'Answers with the place.'},
   {'en': 'Yes, I have 30 years.', 'pt': 'Sim, tenho 30 anos.', 'ok': False, 'fb': 'Wrong topic.'},
   {'en': 'Yes, a flashlight is yes.', 'pt': 'Sim, lanterna é sim.', 'ok': False, 'fb': 'It does not say where.'}]},
  {'npc': 'I found it. It works!', 'pt': 'Achei. Funciona!', 'opts': [
   {'en': 'Great! Let’s light some candles, too.', 'pt': 'Ótimo! Vamos acender velas também.', 'ok': True, 'fb': 'Good idea.'},
   {'en': 'Great! I light the candles to you.', 'pt': 'Ótimo! Eu acendo as velas para você.', 'ok': False, 'fb': 'Use Let’s + verb for a suggestion.'},
   {'en': 'Sorry, I do not work.', 'pt': 'Desculpe, eu não funciono.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Should we call the power company?', 'pt': 'Devemos ligar para a companhia de energia?', 'opts': [
   {'en': 'Yes, that sounds good.', 'pt': 'Sim, parece bom.', 'ok': True, 'fb': 'Agrees politely.'},
   {'en': 'No, I am the company.', 'pt': 'Não, eu sou a companhia.', 'ok': False, 'fb': 'It does not fit.'},
   {'en': 'Yes, I call to power.', 'pt': 'Sim, eu ligo para energia.', 'ok': False, 'fb': 'Say power company and use should we.'}]}]},
 'errors': [
  {'wrong': 'The light is out of power.', 'fix': 'The power is out.', 'alt': 'The power is off of.', 'why': 'In English, “the power is out” is the common phrase.'},
  {'wrong': 'We have a flashlight in drawer.', 'fix': 'We have a flashlight in the drawer.', 'alt': 'We have a flashlight on drawer.', 'why': 'Use the before drawer, and in for inside.'},
  {'wrong': 'There have a storm tonight.', 'fix': 'There is a storm tonight.', 'alt': 'It has a storm tonight.', 'why': 'To say something exists, use there is.'},
  {'wrong': 'Let’s to light candles.', 'fix': 'Let’s light some candles.', 'alt': 'Let’s lighting candles.', 'why': 'After let’s, use only the base verb.'}],
 'homework': 'Write a short dialogue: the power goes out at your home and you look for a flashlight.',
 'homework_items': ['Write three things you can use in the dark.', 'Say aloud: The power is out.', 'Listen to the dialogue and shadow Rosa.', 'Review: power / storm / bulb / switch / match / thunder.']}
