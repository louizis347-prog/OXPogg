"""Suplemento Quest v5 · aula 39: Tip and thank you + regular Please, Thanks, Sorry (The Golden Goose)."""
SUPP = {
 'reg': 14,
 'badge': {'icon': '🙏', 'name': 'Kind Customer', 'desc': 'Talk about tips and say thank you like a local'},
 'culture': {
  'hook': 'In the USA, a tip is part of eating out. Learn how much to leave, how to ask, and how to say thank you in a warm, natural way.',
  'mythfact': [
   {'s': 'In the USA, a normal restaurant tip is about 15 to 20 percent.', 'ans': True, 'why': 'Many people leave 18 or 20 percent when the service is good.'},
   {'s': 'The tip is always already included in the check.', 'ans': False, 'why': 'Usually it is not, so you add it. Some places add it for big groups.'},
   {'s': 'Many servers earn a low base wage, so tips matter a lot.', 'ans': True, 'why': 'In many states, tips are a large part of a server’s pay.'},
   {'s': 'Nashville is known as “Music City”.', 'ans': True, 'why': 'It is famous for country music and live music in many bars.'},
   {'s': 'You should tip at a self-service supermarket.', 'ans': False, 'why': 'Tips are for services like restaurants, taxis and hair salons.'}],
  'wild': [
   {'kind': 'Check footer', 'lines': ['Subtotal $50.00', 'Suggested tip: 18% = $9.00 · 20% = $10.00', 'Thank you!'], 'decode': {'q': 'How much is a 20% tip?', 'opts': ['$10', '$9', '$20'], 'ans': 0, 'why': 'The footer says 20% = $10.00.'}},
   {'kind': 'Tip jar sign', 'lines': ['Tips are appreciated!', 'Thank you for supporting our team.', 'Have a great day!'], 'decode': {'q': 'What does “appreciated” mean here?', 'opts': ['welcome and valued', 'forbidden', 'required'], 'ans': 0, 'why': 'Appreciated = people are grateful for it.'}}],
  'compare': {'br': 'In Brazil, many restaurants add a 10% service charge, so people often do not need to tip extra.', 'us': 'In the USA, the tip is usually not included, so you decide the amount, often 15–20%.', 'tip': 'Say “Keep the change” or “Twenty percent, please” if you want to be clear.', 'ask': 'How do you thank a server where you live? Say it in English.'},
  'quiz': [
   {'q': 'You want to know how much to tip. You ask…', 'opts': ['How much is the tip?', 'What tip you pay?', 'How many tips?'], 'ans': 0, 'why': 'How much is the tip? is natural.'},
   {'q': 'What is 20 percent of $10?', 'opts': ['$2', '$20', '$0.20'], 'ans': 0, 'why': '10% of $10 is $1, so 20% is $2.'},
   {'q': 'The server says “You’re so kind. Thank you!” You answer…', 'opts': ['My pleasure.', 'Yes, I am.', 'No money.'], 'ans': 0, 'why': 'My pleasure is a warm answer.'}]},
 'reading': {
  'genre': 'Blog post',
  'title': 'Dinner and a thank-you',
  'text': [
   'I am in **Nashville**, the city of music. Tonight my friend Nora and I have dinner in a restaurant with live guitar. The food is great, and the server, Cole, is friendly.',
   'After dinner, Cole asks, “**How was everything?**” I say, “**Great, thank you!**” He brings the check. “**Here’s your check.**” I look at it and ask, “**How much is the tip?**” He says, “**Fifteen to twenty percent.**”',
   'I think for a moment. The service was very good, and Cole worked hard. “**Okay. Twenty percent, then**,” I say. Cole smiles. “**You’re so kind. Thank you!**” “**Have a great night!**” I say. “**Have a lovely night!**” he answers.',
   'Nora tells me about a fairy tale called The Golden Goose. In the story, a kind boy shares his cake with a little man, and he gets a golden prize. The story says kindness is a treasure. A tip is a small way to be kind, too.',
   'I leave the restaurant happy. Good food, good music and good manners: that is a perfect night. I know the important words: tip, change, percent and service. Don’t forget the tip!'],
  'glossary': [{'w': 'live', 'pt': 'ao vivo'}, {'w': 'server', 'pt': 'garçom'}, {'w': 'check', 'pt': 'conta'}, {'w': 'tip', 'pt': 'gorjeta'}, {'w': 'percent', 'pt': 'por cento'}, {'w': 'service', 'pt': 'atendimento'}, {'w': 'kind', 'pt': 'gentil'}, {'w': 'treasure', 'pt': 'tesouro'}, {'w': 'manners', 'pt': 'boas maneiras'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Giving a tip after dinner', 'Buying a guitar', 'Going to the airport'], 'ans': 0, 'why': 'The writer asks about and leaves a tip.'},
  'scan': [{'q': 'What city are they in?', 'ans': 'Nashville', 'alt': ['nashville']}, {'q': 'What percent does the writer tip?', 'ans': '20 percent', 'alt': ['twenty percent', '20%', '20']}, {'q': 'Who is the server?', 'ans': 'Cole', 'alt': ['cole']}],
  'tf': [{'s': 'Cole is the server.', 'ans': True, 'why': 'Cole brings the check.'}, {'s': 'The writer leaves a 10 percent tip.', 'ans': False, 'why': 'The writer leaves twenty percent.'}, {'s': 'The service was bad.', 'ans': False, 'why': 'The service was very good.'}, {'s': 'The Golden Goose is a fairy tale.', 'ans': True, 'why': 'Nora tells the writer about the fairy tale.'}],
  'order': ['Cole asks how everything was.', 'He brings the check.', 'The writer asks about the tip.', 'The writer chooses twenty percent.', 'The writer leaves happy.'],
  'ctx': [{'sent': 'Cole worked hard all night.', 'w': 'worked hard', 'opts': ['did a lot of work', 'slept a lot', 'was late'], 'ans': 0, 'why': 'Worked hard = did a lot of work.'}, {'sent': 'You are so kind.', 'w': 'kind', 'opts': ['nice to others', 'very tall', 'very old'], 'ans': 0, 'why': 'Kind = nice and caring.'}, {'sent': 'Good manners are important.', 'w': 'manners', 'opts': ['polite behavior', 'musical notes', 'food'], 'ans': 0, 'why': 'Manners = polite behavior.'}],
  'chunkHunt': ['How was everything?', 'How much is the tip?', 'Fifteen to twenty percent.', 'Have a lovely night!'],
  'think': 'Is it normal to leave a tip where you live? How much?'},
 'convo': {'npc': {'name': 'Cole'}, 'story': 'You finish dinner in a restaurant in Nashville. Cole is your server. Ask about the tip and say thank you.', 'turns': [
  {'npc': 'How was everything?', 'pt': 'Como estava tudo?', 'opts': [
   {'en': 'Great, thank you!', 'pt': 'Ótimo, obrigado!', 'ok': True, 'fb': 'Short and polite.'},
   {'en': 'Yes, was everything.', 'pt': 'Sim, estava tudo.', 'ok': False, 'fb': 'Answer with an opinion.'},
   {'en': 'I am a customer.', 'pt': 'Eu sou cliente.', 'ok': False, 'fb': 'It does not answer.'}]},
  {'npc': 'Here’s your check.', 'pt': 'Aqui está a conta.', 'opts': [
   {'en': 'Thanks. How many is the tip?', 'pt': 'Valeu. Quantos é a gorjeta?', 'ok': False, 'fb': 'Use How much.'},
   {'en': 'The tip is here you.', 'pt': 'A gorjeta é aqui você.', 'ok': False, 'fb': 'Wrong structure.'},
   {'en': 'Thanks. How much is the tip?', 'pt': 'Valeu. Quanto é a gorjeta?', 'ok': True, 'fb': 'A direct question for the amount.'}]},
  {'npc': 'Fifteen to twenty percent.', 'pt': 'Quinze a vinte por cento.', 'opts': [
   {'en': 'Okay. Twenty percent, then.', 'pt': 'Ok. Vinte por cento, então.', 'ok': True, 'fb': 'Make your decision.'},
   {'en': 'Percent is twenty me.', 'pt': 'Por cento é vinte eu.', 'ok': False, 'fb': 'Wrong structure.'},
   {'en': 'I have zero percent.', 'pt': 'Eu tenho zero por cento.', 'ok': False, 'fb': 'Not polite here.'}]},
  {'npc': 'You’re so kind. Thank you!', 'pt': 'Você é muito gentil. Obrigada!', 'opts': [
   {'en': 'You welcome.', 'pt': 'Você bem-vindo.', 'ok': False, 'fb': 'Say You’re welcome.'},
   {'en': 'My pleasure. You were great.', 'pt': 'Foi um prazer. Você foi ótimo.', 'ok': True, 'fb': 'Warm and natural.'},
   {'en': 'I am kind yes.', 'pt': 'Eu sou gentil sim.', 'ok': False, 'fb': 'Sounds odd.'}]},
  {'npc': 'Have a lovely night!', 'pt': 'Tenha uma linda noite!', 'opts': [
   {'en': 'Good appetite!', 'pt': 'Bom apetite!', 'ok': False, 'fb': 'The meal is over.'},
   {'en': 'Thanks! You too!', 'pt': 'Valeu! Você também!', 'ok': True, 'fb': 'The natural answer.'},
   {'en': 'Good morning!', 'pt': 'Bom dia!', 'ok': False, 'fb': 'It is night.'}]}]},
 'errors': [
  {'wrong': 'How many is the tip?', 'fix': 'How much is the tip?', 'alt': 'How much cost the tip?', 'why': 'Use How much for an amount of money.'},
  {'wrong': 'I give the gorjeta to him.', 'fix': 'I leave a tip for him.', 'alt': 'I give a tip him.', 'why': 'In English, you leave a tip. Do not use gorjeta.'},
  {'wrong': 'Twenty per cent of tip.', 'fix': 'A twenty percent tip.', 'alt': 'Twenty percent from tip.', 'why': 'The percent word goes before the noun: a twenty percent tip.'},
  {'wrong': 'Thank you very much for all!', 'fix': 'Thank you for everything!', 'alt': 'Thanks for all.', 'why': 'English says for everything.'}],
 'homework': 'Write a thank-you note to a server and practice saying three tip amounts aloud.',
 'homework_items': ['Calculate 15%, 18% and 20% of $40.', 'Write a 3-line thank-you note.', 'Listen to the dialogue again and shadow Cole.', 'Review: tip / change / percent / service.']}
