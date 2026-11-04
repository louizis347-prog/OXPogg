"""Suplemento Quest v5 · aula 167: I like your jacket + regular Wrap a present (Clueless)."""
SUPP = {
 'reg': 171,
 'badge': {'icon': '🧥', 'name': 'Nice Compliment', 'desc': 'Give and receive compliments'},
 'culture': {
  'hook': 'In the USA, many people give small compliments to friends, coworkers and even new people. A compliment is a nice way to start a short, friendly talk.',
  'mythfact': [
   {'s': 'In the USA, a compliment from a new person is always strange.', 'ans': False, 'why': 'In many places it is common and friendly, for example about a bag or a jacket.'},
   {'s': 'The normal answer to a compliment is “Thank you.”', 'ans': True, 'why': 'It is short and polite. You can add “It’s new!” or “I like yours, too.”'},
   {'s': 'It is polite to say “No, it is ugly” when someone likes your jacket.', 'ans': False, 'why': 'Most people say thank you and accept the compliment.'},
   {'s': 'People often compliment hair, shoes, bags and clothes.', 'ans': True, 'why': 'These are easy, friendly things to talk about.'},
   {'s': '“Clueless” is a movie about a teenage girl who loves clothes and fashion.', 'ans': True, 'why': 'It is a 1995 movie with a girl named Cher.'}],
  'wild': [
   {'kind': 'Store sign', 'lines': ['**New jackets**', 'Blue, black and green', 'Half price this week'], 'decode': {'q': 'What colors are the jackets?', 'opts': ['Blue, black and green', 'Red and white', 'Only black'], 'ans': 0, 'why': 'The sign says blue, black and green.'}},
   {'kind': 'Text message', 'lines': ['**Love your new hair!**', 'The color looks great on you.', 'Coffee later?'], 'decode': {'q': 'What does the friend like?', 'opts': ['The new hair', 'A new bag', 'A coffee shop'], 'ans': 0, 'why': '“Love your new hair!”'}}],
  'compare': {'br': 'In Brazil, people also compliment each other, and many say “Que lindo!” or “Ficou ótimo em você!”.', 'us': 'In the USA, people often answer with a simple “Thank you!” and then give a compliment back. They usually do not say “it is nothing”.', 'tip': 'Say: “Thank you! I like your bag, too.”', 'ask': 'What compliment do you like to hear? Say it in English.'},
  'quiz': [
   {'q': 'Someone says, “I like your jacket.” You say…', 'opts': ['Thank you! It’s new.', 'Thank you for the jacket.', 'I am a jacket.'], 'ans': 0, 'why': 'Thank you + a short comment is natural.'},
   {'q': 'You like your friend’s bag. You say…', 'opts': ['I like your bag.', 'I like of your bag.', 'I am liking you bag.'], 'ans': 0, 'why': 'Like is followed directly by the thing: your bag.'},
   {'q': 'Which word is a place to buy clothes?', 'opts': ['mall', 'hair', 'gift'], 'ans': 0, 'why': 'A mall has many stores.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'A jacket and a nice day',
  'text': [
   'Cleo lives in **Austin**. Today she has a new jacket. It is blue, and the color is bright. She likes it very much. She goes to a café near her office.',
   'At the café, a man named Omar says, “**Hey! I like your jacket.**” Cleo smiles. “**Thank you! It’s new.**” “**Where did you get it?**” “**At the mall, downtown.**” Omar says, “**The color looks great on you.**”',
   '“**You’re so kind. I like your bag,**” Cleo says. “**Thanks! It was a gift.**” “**It’s really beautiful.**” “**Your hair looks nice, too,**” Omar says. Cleo laughs. “**That’s so sweet.**” Omar laughs, too. The compliments make her day.',
   'Cleo thinks of the movie “Clueless.” In the film, a girl named Cher loves clothes and always says nice things to her friends. She also helps people choose a style. Cleo likes that idea. A small, kind word can make someone happy.',
   'Before Cleo leaves, she says, “Thanks, Omar. Have a good day!” Omar smiles. “You, too!” The sun is warm, and the street is quiet. Cleo walks home in her blue jacket. She feels good.'],
  'glossary': [{'w': 'bright', 'pt': 'vivo, forte (cor)'}, {'w': 'office', 'pt': 'escritório'}, {'w': 'color', 'pt': 'cor'}, {'w': 'kind', 'pt': 'gentil'}, {'w': 'gift', 'pt': 'presente'}, {'w': 'beautiful', 'pt': 'lindo(a)'}, {'w': 'laughs', 'pt': 'ri'}, {'w': 'compliments', 'pt': 'elogios'}, {'w': 'style', 'pt': 'estilo'}, {'w': 'clothes', 'pt': 'roupas'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A man and a woman say nice things', 'A woman loses her bag', 'A man buys a car'], 'ans': 0, 'why': 'Omar and Cleo give compliments.'},
  'scan': [{'q': 'What color is Cleo’s jacket?', 'ans': 'blue', 'alt': ['it is blue']}, {'q': 'Where did Cleo get the jacket?', 'ans': 'at the mall', 'alt': ['the mall', 'mall', 'at the mall, downtown']}, {'q': 'What was Omar’s bag?', 'ans': 'a gift', 'alt': ['gift', 'it was a gift']}],
  'tf': [{'s': 'Cleo has an old jacket.', 'ans': False, 'why': 'Her jacket is new.'}, {'s': 'Omar likes Cleo’s jacket.', 'ans': True, 'why': '“I like your jacket.”'}, {'s': 'Cleo gets her jacket at a café.', 'ans': False, 'why': 'She gets it at the mall.'}, {'s': 'Cleo feels good at the end.', 'ans': True, 'why': 'The last line says she feels good.'}],
  'order': ['Cleo puts on her new jacket.', 'She goes to a café.', 'Omar likes her jacket.', 'Cleo likes Omar’s bag.', 'Cleo walks home.'],
  'ctx': [{'sent': 'The color is bright.', 'w': 'bright', 'opts': ['strong and easy to see', 'very old', 'very small'], 'ans': 0, 'why': 'A bright color is strong.'}, {'sent': 'You’re so kind.', 'w': 'kind', 'opts': ['nice to other people', 'very tall', 'very late'], 'ans': 0, 'why': 'Kind = nice and good to others.'}, {'sent': 'Cleo laughs.', 'w': 'laughs', 'opts': ['makes a happy sound', 'goes home', 'drinks coffee'], 'ans': 0, 'why': 'You laugh when something is funny or happy.'}],
  'chunkHunt': ['I like your jacket.', 'Where did you get it?', 'The color looks great on you.', 'Thank you! It’s new.'],
  'think': 'Who do you want to compliment today? What do you say?'},
 'convo': {'npc': {'name': 'Omar'}, 'story': 'You are at a café in Austin. Omar likes your new jacket.', 'turns': [
  {'npc': 'Hey! I like your jacket.', 'pt': 'Oi! Gosto da sua jaqueta.', 'opts': [
   {'en': 'I like of your jacket.', 'pt': 'Eu gosto de da sua jaqueta.', 'ok': False, 'fb': 'Do not add “of” after like.'},
   {'en': 'No, it is not nice.', 'pt': 'Não, ela não é bonita.', 'ok': False, 'fb': 'Too negative for a compliment.'},
   {'en': 'Thank you! It’s new.', 'pt': 'Obrigada! É nova.', 'ok': True, 'fb': 'Thank + a short comment.'}]},
  {'npc': 'Where did you get it?', 'pt': 'Onde você comprou?', 'opts': [
   {'en': 'At the mall, downtown.', 'pt': 'No shopping do centro.', 'ok': True, 'fb': 'Answers the place.'},
   {'en': 'It is blue.', 'pt': 'É azul.', 'ok': False, 'fb': 'He asks where, not what color.'},
   {'en': 'In the mall, I buy it.', 'pt': 'No shopping, eu compro.', 'ok': False, 'fb': 'Past: I got it at the mall.'}]},
  {'npc': 'The color looks great on you.', 'pt': 'A cor fica ótima em você.', 'opts': [
   {'en': 'The color is you.', 'pt': 'A cor é você.', 'ok': False, 'fb': 'Does not make sense.'},
   {'en': 'You’re so kind. I like your bag.', 'pt': 'Você é muito gentil. Gosto da sua bolsa.', 'ok': True, 'fb': 'Thanks him and gives a compliment back.'},
   {'en': 'Where did you get it?', 'pt': 'Onde você comprou?', 'ok': False, 'fb': 'He did not say what “it” is.'}]},
  {'npc': 'Thanks! It was a gift.', 'pt': 'Valeu! Foi presente.', 'opts': [
   {'en': 'It’s really beautiful.', 'pt': 'É muito bonita.', 'ok': True, 'fb': 'Natural reaction.'},
   {'en': 'I gift you the bag.', 'pt': 'Eu dou a bolsa a você.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'It is new.', 'pt': 'É nova.', 'ok': False, 'fb': 'Your jacket is new, not his bag.'}]},
  {'npc': 'Your hair looks nice, too.', 'pt': 'Seu cabelo está bonito também.', 'opts': [
   {'en': 'My hair is a gift.', 'pt': 'Meu cabelo é um presente.', 'ok': False, 'fb': 'Does not fit.'},
   {'en': 'I like the mall.', 'pt': 'Gosto do shopping.', 'ok': False, 'fb': 'Not related.'},
   {'en': 'Thank you! That’s so sweet.', 'pt': 'Obrigada! Que gentil.', 'ok': True, 'fb': 'Polite and warm.'}]}]},
 'errors': [
  {'wrong': 'I like of your jacket.', 'fix': 'I like your jacket.', 'alt': 'I am liking your jacket.', 'why': 'Like goes straight to the thing. Like is not used with -ing here.'},
  {'wrong': 'Your jacket is very nice in you.', 'fix': 'Your jacket looks great on you.', 'alt': 'Your jacket looks good in you.', 'why': 'Use on you for clothes.'},
  {'wrong': 'Where you buy it?', 'fix': 'Where did you get it?', 'alt': 'Where you got it?', 'why': 'Question in the past: Where did + you + get.'},
  {'wrong': 'It is a present of my mother.', 'fix': 'It was a gift from my mom.', 'alt': 'It was a gift of my mom.', 'why': 'Use gift from + person.'}],
 'homework': 'Write a short dialogue: you give a compliment to a friend and he or she answers.',
 'homework_items': ['Write 3 compliments for clothes or hair.', 'Say aloud: The color looks great on you.', 'Listen to the dialogue and shadow Cleo.', 'Review the colors: blue, black, green, red, white.']}
