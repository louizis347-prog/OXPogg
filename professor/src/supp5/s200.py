"""Suplemento Quest v5 · aula 200: What should I wear? + regular Flip-flops at the beach (The Water-Babies)."""
SUPP = {
 'reg': 202,
 'badge': {'icon': '👕', 'name': 'Dressed Right', 'desc': 'Check the weather and choose clothes for the day'},
 'culture': {
  'hook': 'In the USA, the weather can change a lot in one day, so many people check the forecast before they choose clothes. A simple question to a friend or family member also helps.',
  'mythfact': [
   {'s': 'Many people in the USA check the weather before they dress.', 'ans': True, 'why': 'The weather can change quickly in many places.'},
   {'s': 'You always wear shorts in the USA.', 'ans': False, 'why': 'It depends on the weather and the place. Winters can be very cold.'},
   {'s': '“Dressing in layers” means wearing a few light clothes, one over another.', 'ans': True, 'why': 'It helps when the temperature changes in the day.'},
   {'s': '“Cool” can mean a little cold.', 'ans': True, 'why': 'Cool weather is between warm and cold.'},
   {'s': '“The Water-Babies” is a fairy tale from 1863.', 'ans': True, 'why': 'Charles Kingsley wrote it.'}],
  'wild': [
   {'kind': 'Weather app', 'lines': ['**Today: Cloudy**', 'High 61°F · Low 50°F', 'Chance of rain: 20%'], 'decode': {'q': 'What is the weather like?', 'opts': ['Cloudy and cool', 'Hot and sunny', 'Very snowy'], 'ans': 0, 'why': 'It says cloudy, and 61°F is cool.'}},
   {'kind': 'Tag in a jacket', 'lines': ['**Machine wash cold**', 'Do not iron', 'Size M'], 'decode': {'q': 'How do you wash it?', 'opts': ['With cold water', 'With hot water', 'You cannot wash it'], 'ans': 0, 'why': '“Machine wash cold” means to wash in a machine with cold water.'}}],
  'compare': {'br': 'In Brazil, many people ask “Que roupa eu uso hoje?” and often look at the sky or the phone for the weather.', 'us': 'In the USA, many people use a phone app and talk about “the high” and “the low” of the day, in Fahrenheit.', 'tip': 'Say: “What’s the weather like today?”', 'ask': 'How do you ask about the weather in English? Say it.'},
  'quiz': [
   {'q': 'You want advice on clothes. You ask…', 'opts': ['What should I wear today?', 'What I should wear today?', 'What do I should wear?'], 'ans': 0, 'why': 'What + should + I + verb.'},
   {'q': 'You ask about the weather. You say…', 'opts': ['What’s the weather like?', 'How is the weather like?', 'What the weather is?'], 'ans': 0, 'why': 'What’s the weather like? is the usual phrase.'},
   {'q': 'You ask where your socks are. You say…', 'opts': ['Where are my socks?', 'Where is my socks?', 'Where my socks are?'], 'ans': 0, 'why': 'Socks is plural, so use are.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Blue shirt, long pants',
  'text': [
   'Miles looks at his closet. He has shorts, a raincoat, sneakers and many shirts. Next Saturday, his class goes to the beach, so he thinks about flip-flops. But today is a school day, and he needs a good outfit.',
   '“**Mom, what should I wear today?**” “**What’s the weather like?**” “**It’s cool and cloudy.**” “**Then wear long pants.**” Miles takes his pants from the bed and puts them on.',
   '“**Which shirt? The blue or the green?**” “**The blue one looks nice.**” Miles puts on the blue shirt. Then he looks around. “**Where are my socks?**” “**In the top drawer.**” He finds them next to his shorts.',
   '“**Should I wear a jacket?**” Mom looks out the window. “Yes, take a jacket. It can be cold at lunch.” Miles also thinks about “The Water-Babies,” a fairy tale from 1863 about a boy in the sea. On Saturday, he will wear shorts and flip-flops, but today the jacket is right. Mom smiles. “You look great, Miles.” He grabs his bag and goes to school.'],
  'glossary': [{'w': 'closet', 'pt': 'armário de roupas'}, {'w': 'shorts', 'pt': 'bermuda'}, {'w': 'raincoat', 'pt': 'capa de chuva'}, {'w': 'outfit', 'pt': 'roupa, look'}, {'w': 'weather', 'pt': 'tempo (clima)'}, {'w': 'cloudy', 'pt': 'nublado'}, {'w': 'cool', 'pt': 'fresco'}, {'w': 'long pants', 'pt': 'calça comprida'}, {'w': 'drawer', 'pt': 'gaveta'}, {'w': 'fairy tale', 'pt': 'conto de fadas'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A boy chooses clothes for a cool, cloudy day', 'A boy cooks lunch', 'A boy goes swimming'], 'ans': 0, 'why': 'Miles asks his mom what to wear.'},
  'scan': [{'q': 'What is the weather like?', 'ans': 'cool and cloudy', 'alt': ['cloudy', 'cool']}, {'q': 'What color shirt does Miles wear?', 'ans': 'blue', 'alt': ['the blue one', 'a blue shirt']}, {'q': 'Where are the socks?', 'ans': 'in the top drawer', 'alt': ['top drawer', 'in the drawer']}],
  'tf': [{'s': 'Miles wears shorts to school today.', 'ans': False, 'why': 'He wears long pants.'}, {'s': 'Mom says the blue shirt looks nice.', 'ans': True, 'why': '“The blue one looks nice.”'}, {'s': 'The socks are in the top drawer.', 'ans': True, 'why': 'Mom says it.'}, {'s': 'Mom says no jacket.', 'ans': False, 'why': 'She says, “Yes, take a jacket.”'}],
  'order': ['Miles asks what to wear.', 'Mom asks about the weather.', 'Miles picks the blue shirt.', 'Miles asks for his socks.', 'Mom says to take a jacket.'],
  'ctx': [{'sent': 'It is cool and cloudy.', 'w': 'cloudy', 'opts': ['with many clouds', 'very hot', 'with a lot of snow'], 'ans': 0, 'why': 'Cloudy means many clouds.'}, {'sent': 'He needs a good outfit.', 'w': 'outfit', 'opts': ['clothes to wear together', 'a kind of food', 'a small bag'], 'ans': 0, 'why': 'An outfit is clothes that go together.'}, {'sent': 'Miles has a raincoat.', 'w': 'raincoat', 'opts': ['a coat for rain', 'a hat for sun', 'shoes for snow'], 'ans': 0, 'why': 'A raincoat protects you from rain.'}],
  'chunkHunt': ['What should I wear today?', 'What’s the weather like?', 'The blue one looks nice.', 'Should I wear a jacket?'],
  'think': 'What do you wear on a cool, cloudy day? Do you check the weather first?'},
 'convo': {'npc': {'name': 'Miles'}, 'story': 'You are getting dressed at home. Your friend Miles helps you choose clothes for a cool, cloudy day.', 'turns': [
  {'npc': 'Good morning! Are you ready?', 'pt': 'Bom dia! Você está pronto?', 'opts': [
   {'en': 'Not yet. What should I wear today?', 'pt': 'Ainda não. O que devo vestir hoje?', 'ok': True, 'fb': 'Natural question with should.'},
   {'en': 'Not yet. What I should wear?', 'pt': 'Ainda não. O que eu devo vestir?', 'ok': False, 'fb': 'Word order: What should I wear?'},
   {'en': 'Yes, I wear it.', 'pt': 'Sim, eu visto isso.', 'ok': False, 'fb': 'Does not answer.'}]},
  {'npc': 'Look outside! What’s the weather like?', 'pt': 'Olhe lá fora! Como está o tempo?', 'opts': [
   {'en': 'The weather is a jacket.', 'pt': 'O tempo é um casaco.', 'ok': False, 'fb': 'Describe the weather: cool, cloudy.'},
   {'en': 'It’s cool and cloudy.', 'pt': 'Está fresco e nublado.', 'ok': True, 'fb': 'Clear and short.'},
   {'en': 'It has cool and cloudy.', 'pt': 'Tem fresco e nublado.', 'ok': False, 'fb': 'Use It’s + adjective.'}]},
  {'npc': 'Then wear long pants. Which shirt? The blue or the green?', 'pt': 'Então use calça comprida. Qual camisa? A azul ou a verde?', 'opts': [
   {'en': 'The blue one looks nice.', 'pt': 'A azul está bonita.', 'ok': True, 'fb': 'Picks one with a reason.'},
   {'en': 'The weather looks nice.', 'pt': 'O tempo está bonito.', 'ok': False, 'fb': 'The question is about the shirt.'},
   {'en': 'Yes, the blue.', 'pt': 'Sim, a azul.', 'ok': False, 'fb': 'It is not a yes/no question.'}]},
  {'npc': 'Anything else?', 'pt': 'Mais alguma coisa?', 'opts': [
   {'en': 'Where is my socks?', 'pt': 'Onde está minhas meias?', 'ok': False, 'fb': 'Socks is plural: Where are my socks?'},
   {'en': 'Where are my socks?', 'pt': 'Onde estão minhas meias?', 'ok': True, 'fb': 'Correct plural form.'},
   {'en': 'My socks are cool.', 'pt': 'Minhas meias são legais.', 'ok': False, 'fb': 'Does not ask where they are.'}]},
  {'npc': 'In the top drawer.', 'pt': 'Na gaveta de cima.', 'opts': [
   {'en': 'Thanks! Should I wear a jacket?', 'pt': 'Valeu! Devo vestir um casaco?', 'ok': True, 'fb': 'Thanks and a new question.'},
   {'en': 'Thanks! Should I to wear a jacket?', 'pt': 'Valeu! Devo vestir um casaco?', 'ok': False, 'fb': 'After should, use the base verb: wear.'},
   {'en': 'In the top drawer, too.', 'pt': 'Na gaveta de cima também.', 'ok': False, 'fb': 'Does not fit.'}]}]},
 'errors': [
  {'wrong': 'What I should wear today?', 'fix': 'What should I wear today?', 'alt': 'What do I should wear today?', 'why': 'In questions, put should before I.'},
  {'wrong': 'How is the weather?', 'fix': 'What’s the weather like?', 'alt': 'How is the weather like?', 'why': 'The usual phrase is What’s the weather like? Do not add like after how.'},
  {'wrong': 'Where is my socks?', 'fix': 'Where are my socks?', 'alt': 'Where are my sock?', 'why': 'Socks is plural, so use are.'},
  {'wrong': 'It makes cool today.', 'fix': 'It’s cool today.', 'alt': 'Is cool today.', 'why': 'For weather, use It’s + adjective.'}],
 'homework': 'Write a short dialogue: you ask a friend what to wear, check the weather and pick a shirt.',
 'homework_items': ['Write an outfit for a cool, cloudy day.', 'Say aloud: What should I wear today?', 'Listen to the dialogue and shadow Miles.', 'Review: shorts / coat / outfit / weather.']}
