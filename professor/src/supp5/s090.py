"""Suplemento Quest v5 · aula 90: At the museum + regular At the Art Gallery (The Starry Night)."""
SUPP = {
 'reg': 95,
 'badge': {'icon': '🎨', 'name': 'Museum Visitor', 'desc': 'Buy tickets, ask the time and ask about photos'},
 'culture': {
  'hook': 'At a museum in the USA, the first stop is the ticket desk. You say how many tickets you want, show a student card if you have one, and ask about the rules.',
  'mythfact': [
   {'s': 'Many US museums give a lower price to students who show a student card.', 'ans': True, 'why': 'Student, child and senior prices are common, but the rules change from museum to museum.'},
   {'s': 'You can touch every painting in a museum.', 'ans': False, 'why': 'Most museums ask you not to touch the art, because skin can damage it.'},
   {'s': 'Many museums let you take photos without flash.', 'ans': True, 'why': 'Flash can hurt old paintings, so it is often not allowed. Some rooms do not allow photos at all.'},
   {'s': 'Every museum in the USA is free.', 'ans': False, 'why': 'Some are free or have free days, but many have a ticket price.'},
   {'s': '“The Starry Night” is a painting by Vincent van Gogh.', 'ans': True, 'why': 'He painted it in 1889, and it is now in a museum in New York.'}],
  'wild': [
   {'kind': 'Museum ticket board', 'lines': ['**Adult** $20', '**Student** $12 (with card)', '**Child under 6** free'], 'decode': {'q': 'How much is a student ticket?', 'opts': ['$12', '$20', 'It is free'], 'ans': 0, 'why': 'A student ticket is $12 with a card.'}},
   {'kind': 'Museum rule sign', 'lines': ['**No flash photos.**', 'Please do not touch the art.', 'Open 10 a.m. – 5 p.m.'], 'decode': {'q': 'What is not allowed?', 'opts': ['Flash photos', 'Walking', 'Looking at art'], 'ans': 0, 'why': '“No flash photos.”'}}],
  'compare': {'br': 'In Brazil, many museums give half price to students with a student card, and some have free days.', 'us': 'In the USA, many museums have special prices for students, children and seniors. Ask at the desk and show your card.', 'tip': 'Ask: “Is there a student discount?”', 'ask': 'Do you like art? Which museum do you want to visit? Say it in English.'},
  'quiz': [
   {'q': 'You want to ask about photos. You say…', 'opts': ['Can I take photos?', 'I can take photos?', 'Can I to take photos?'], 'ans': 0, 'why': 'Can I + base verb.'},
   {'q': 'You ask the closing time. You say…', 'opts': ['What time does the museum close?', 'What time the museum closes?', 'What time does the museum closes?'], 'ans': 0, 'why': 'After does, the verb has no -s: close.'},
   {'q': 'What does “no flash” mean?', 'opts': ['Do not use the camera light', 'Do not walk fast', 'Do not buy a ticket'], 'ans': 0, 'why': 'Flash is the strong light of a camera.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'A day with art',
  'text': [
   'It is a rainy Saturday in Los Angeles. Marco and his sister Gina go to a big art museum. At the ticket desk, a woman smiles. “**Hi! Two tickets, please**,” Marco says. “**That’s thirty dollars. Students get a discount**,” she says.',
   '“**I have a student card**,” Marco says, and he shows it. “**Then it’s twenty-four dollars**,” the woman says. Marco pays, and she gives him a map. “**What time does the museum close?**” he asks. “**At five o’clock.**”',
   '“**Can I take photos?**” Gina asks. “**Yes, but no flash**,” the woman says. “Flash can hurt old paintings.” Gina puts her phone in photo mode. The woman smiles. “**Enjoy the museum!**”',
   'The paintings are on the second floor. Gina likes a blue and yellow one. It makes her think of “The Starry Night” by Vincent van Gogh. He painted the sky with big stars, a bright moon and a quiet village. “It’s beautiful,” Gina says. “It’s my favorite.”',
   'They walk slowly and look closely at each painting. Marco learns the names of two painters. Gina takes five photos with no flash. At four-thirty, a guard says, “The museum closes soon.” The brother and sister smile and walk to the gift shop.'],
  'glossary': [{'w': 'desk', 'pt': 'balcão, mesa'}, {'w': 'discount', 'pt': 'desconto'}, {'w': 'student card', 'pt': 'carteirinha de estudante'}, {'w': 'map', 'pt': 'mapa'}, {'w': 'flash', 'pt': 'flash da câmera'}, {'w': 'hurt', 'pt': 'machucar, danificar'}, {'w': 'floor', 'pt': 'andar'}, {'w': 'painted', 'pt': 'pintou'}, {'w': 'village', 'pt': 'vilarejo'}, {'w': 'gift shop', 'pt': 'lojinha de lembranças'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Two people visit an art museum', 'A man goes camping', 'A woman rents a car'], 'ans': 0, 'why': 'Marco and Gina buy tickets and see paintings.'},
  'scan': [{'q': 'How much are the two tickets with the student card?', 'ans': 'twenty-four dollars', 'alt': ['$24', '24 dollars', 'twenty-four']}, {'q': 'What time does the museum close?', 'ans': 'at five o’clock', 'alt': ['five o’clock', 'five', '5']}, {'q': 'On which floor are the paintings?', 'ans': 'the second floor', 'alt': ['second floor', 'second']}],
  'tf': [{'s': 'Marco has a student card.', 'ans': True, 'why': '“I have a student card.”'}, {'s': 'Photos with flash are okay.', 'ans': False, 'why': 'The woman says, “No flash.”'}, {'s': 'The museum closes at five.', 'ans': True, 'why': 'She says, “At five o’clock.”'}, {'s': 'Gina does not like the painting.', 'ans': False, 'why': 'She says, “It’s my favorite.”'}],
  'order': ['Marco asks for two tickets.', 'He shows his student card.', 'Gina asks about photos.', 'They look at the paintings.', 'They go to the gift shop.'],
  'ctx': [{'sent': 'Students get a discount.', 'w': 'discount', 'opts': ['a lower price', 'a free map', 'a long line'], 'ans': 0, 'why': 'Discount = desconto.'}, {'sent': 'Flash can hurt old paintings.', 'w': 'hurt', 'opts': ['damage', 'clean', 'sell'], 'ans': 0, 'why': 'Hurt = machucar, danificar.'}, {'sent': 'The paintings are on the second floor.', 'w': 'floor', 'opts': ['level of a building', 'part of a painting', 'kind of ticket'], 'ans': 0, 'why': 'Floor = andar.'}],
  'chunkHunt': ['Two tickets, please.', 'I have a student card.', 'What time does the museum close?', 'Can I take photos?'],
  'think': 'What is your favorite painting or kind of art? Why?'},
 'convo': {'npc': {'name': 'Marco'}, 'story': 'You are at a museum ticket desk. Marco works there. Talk to him.', 'turns': [
  {'npc': 'Hello! Welcome to the museum. How can I help you?', 'pt': 'Olá! Bem-vindo ao museu. Como posso ajudar?', 'opts': [
   {'en': 'Hi! Two tickets, please.', 'pt': 'Oi! Dois ingressos, por favor.', 'ok': True, 'fb': 'Clear and polite.'},
   {'en': 'I am two tickets.', 'pt': 'Eu sou dois ingressos.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'Enjoy the museum!', 'pt': 'Aproveite o museu!', 'ok': False, 'fb': 'That is for the clerk to say.'}]},
  {'npc': 'That’s thirty dollars. Students get a discount.', 'pt': 'São trinta dólares. Estudantes têm desconto.', 'opts': [
   {'en': 'I am student card.', 'pt': 'Eu sou carteirinha.', 'ok': False, 'fb': 'Say: I have a student card.'},
   {'en': 'I have a student card.', 'pt': 'Tenho carteirinha de estudante.', 'ok': True, 'fb': 'Shows you can get the discount.'},
   {'en': 'At five o’clock.', 'pt': 'Às cinco.', 'ok': False, 'fb': 'Does not answer.'}]},
  {'npc': 'Then it’s twenty-four dollars.', 'pt': 'Então são vinte e quatro dólares.', 'opts': [
   {'en': 'What time does the museum close?', 'pt': 'Que horas o museu fecha?', 'ok': True, 'fb': 'Useful question after paying.'},
   {'en': 'What time the museum closes?', 'pt': 'Que horas o museu fecha?', 'ok': False, 'fb': 'Use does + close.'},
   {'en': 'I have thirty dollars.', 'pt': 'Eu tenho trinta dólares.', 'ok': False, 'fb': 'Does not follow the new price.'}]},
  {'npc': 'At five o’clock.', 'pt': 'Às cinco.', 'opts': [
   {'en': 'Can I take photos?', 'pt': 'Posso tirar fotos?', 'ok': True, 'fb': 'Polite question.'},
   {'en': 'I can take photos?', 'pt': 'Eu posso tirar fotos?', 'ok': False, 'fb': 'For a question, put Can first.'},
   {'en': 'Two tickets, please.', 'pt': 'Dois ingressos, por favor.', 'ok': False, 'fb': 'You already did that.'}]},
  {'npc': 'Yes, but no flash. Enjoy the museum!', 'pt': 'Sim, mas sem flash. Aproveite o museu!', 'opts': [
   {'en': 'Welcome to the museum!', 'pt': 'Bem-vindo ao museu!', 'ok': False, 'fb': 'Wrong person and moment.'},
   {'en': 'Yes, but no flash.', 'pt': 'Sim, mas sem flash.', 'ok': False, 'fb': 'That is the clerk’s line, not yours.'},
   {'en': 'Thanks! Have a nice day!', 'pt': 'Obrigado! Tenha um bom dia!', 'ok': True, 'fb': 'Natural and polite.'}]}]},
 'errors': [
  {'wrong': 'Two ticket, please.', 'fix': 'Two tickets, please.', 'alt': 'Tickets two, please.', 'why': 'After two, use the plural: tickets.'},
  {'wrong': 'What time the museum close?', 'fix': 'What time does the museum close?', 'alt': 'What time does the museum closes?', 'why': 'Use does + the base verb close.'},
  {'wrong': 'I can to take photos?', 'fix': 'Can I take photos?', 'alt': 'I can take photos?', 'why': 'In a question, Can comes first, and take has no to.'},
  {'wrong': 'I am a student card.', 'fix': 'I have a student card.', 'alt': 'I have student card.', 'why': 'Use have for things, and add a before card.'}],
 'homework': 'Write a short dialogue: you buy two tickets at a museum and ask about the closing time and photos.',
 'homework_items': ['Write 5 prices in English (for example, twenty-four dollars).', 'Say aloud: What time does the museum close?', 'Listen to the dialogue and shadow Marco.', 'Review: like + verb-ing (I like painting).']}
