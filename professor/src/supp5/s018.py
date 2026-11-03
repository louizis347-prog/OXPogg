"""Suplemento Quest v5 · aula 18: My hobbies + regular What do you do for fun? (The Swing)."""
def o(en, pt, ok, fb):
    return {'en': en, 'pt': pt, 'ok': ok, 'fb': fb}

SUPP = {
    'reg': 118,
    'badge': {'icon': '⚽', 'name': 'Hobby Hero', 'desc': 'Talk about your free time and invite friends in English'},
    'sticker': {'cat': 'Everyday culture', 'title': 'Hobbies and Weekends in the USA', 'sub': 'What do you do for fun?'},
    'culture': {
        'hook': 'In the USA people love to talk about free time. Learn the words for hobbies, and remember: in the USA, football is not the same sport as in Brazil.',
        'facts': [
            {'vis': 'prop:coin', 'big': 'Soccer', 'label': 'What the USA calls futebol', 'sub': 'In the USA, “football” usually means American football.'},
            {'vis': 'prop:clock', 'big': 'Saturday', 'label': 'Weekend sports', 'sub': 'Many children play soccer in a local league on Saturday morning.'},
            {'vis': 'prop:umbrella', 'big': 'April', 'label': 'The Boston Marathon', 'sub': 'It is held every April in Boston, Massachusetts.'},
            {'vis': 'prop:bag', 'big': 'I’m in!', 'label': 'Accept an invitation', 'sub': 'Also: “Count me in.”'},
        ],
        'polite': 'To invite someone, say **Do you want to…?** To accept, say **Sure!** or **I’m in!**',
        'mythfact': [
            {'s': 'In the USA, “football” usually means American football.', 'ans': True, 'why': 'The sport with a round ball is called soccer.'},
            {'s': 'The Boston Marathon is held in April.', 'ans': True, 'why': 'It is held every year in April, on Patriots’ Day.'},
            {'s': 'People in the USA call soccer “football”.', 'ans': False, 'why': 'They call it soccer.'},
            {'s': 'You can say “I enjoy reading” to talk about a hobby.', 'ans': True, 'why': 'Enjoy + verb-ing is correct.'},
            {'s': 'The poem “The Swing” was written by Robert Louis Stevenson.', 'ans': True, 'why': 'It was published in 1885 in “A Child’s Garden of Verses”.'},
        ],
        'wild': [
            {'kind': 'Park flyer', 'lines': ['**Pickup soccer · Saturdays**', '10 a.m. at Riverside Park', 'All ages welcome · Bring water'], 'decode': {'q': 'What time does the game start?', 'opts': ['10 a.m.', '10 p.m.', '9 a.m.'], 'ans': 0, 'why': '“10 a.m. at Riverside Park.”'}},
            {'kind': 'Text message', 'lines': ['Wanna hang out this weekend?', 'I’m in! What’s the plan?', 'Soccer at ten, then lunch.'], 'decode': {'q': 'What is the plan?', 'opts': ['Soccer and lunch', 'A movie', 'A concert'], 'ans': 0, 'why': '“Soccer at ten, then lunch.”'}},
        ],
        'compare': {
            'br': 'In Brazil, futebol is the most popular sport, and people say “jogar bola”.',
            'us': 'In the USA, baseball, basketball and American football are very popular, and soccer is also played by many children.',
            'tip': 'Use play with sports and games (play soccer), but with instruments you say play the guitar.',
            'ask': 'What do you do in your free time? Say two hobbies in English.',
        },
        'quiz': [
            {'q': 'A friend asks about your free time. You say…', 'opts': ['I play soccer and read books.', 'I am playing at free time.', 'I do soccer.'], 'ans': 0, 'why': 'Use simple present for habits.'},
            {'q': 'You want to invite a friend to play. You say…', 'opts': ['Do you want to play soccer on Saturday?', 'You want soccer Saturday?', 'Play soccer with you Saturday?'], 'ans': 0, 'why': 'Do you want to… is polite.'},
            {'q': 'A friend invites you. You say yes. You say…', 'opts': ['I’m in!', 'I am out!', 'I do not in.'], 'ans': 0, 'why': 'I’m in! = I want to join.'},
        ],
    },
    'reading': {
        'genre': 'Blog post',
        'title': 'My free time in Boston',
        'text': [
            'My name is Jack, and I live in **Boston**. In my free time I play soccer and read books. I **enjoy reading** on the train, and I **enjoy swimming** in the summer.',
            'Last week my friend Grace asked, “What do you do in your free time?” “I play soccer,” I said. “And you?” “I play guitar,” she said. “I’m **into music**.” I asked, “Do you play in a band?” “No, I play at home. Just for fun.”',
            '“Do you want to play soccer on Saturday?” I asked. “Sure! What time?” “At ten, in the park.” “I’m in! **Don’t be late**,” she said, and we both laughed.',
            'My favorite poem is “The Swing,” by Robert Louis Stevenson. He wrote it in 1885. In the poem, a child goes up and down on a swing and sees the garden and the river. The child is **having a blast**. I think hobbies are like a swing: they make you happy.',
            'On Saturday we played soccer, and then we had lunch. It was a very good morning. What do you do for fun?',
        ],
        'glossary': [{'w': 'free time', 'pt': 'tempo livre'}, {'w': 'train', 'pt': 'trem'}, {'w': 'swimming', 'pt': 'natação'}, {'w': 'band', 'pt': 'banda'}, {'w': 'laughed', 'pt': 'riu'}, {'w': 'poem', 'pt': 'poema'}, {'w': 'swing', 'pt': 'balanço'}, {'w': 'garden', 'pt': 'jardim'}, {'w': 'lunch', 'pt': 'almoço'}],
        'fast': {'q': 'What is this text about?', 'opts': ['Hobbies and a weekend plan', 'A trip abroad', 'A job at a bank'], 'ans': 0, 'why': 'Jack and Grace talk about free time and plan soccer.'},
        'scan': [
            {'q': 'What instrument does Grace play?', 'ans': 'guitar', 'alt': ['the guitar', 'Guitar']},
            {'q': 'What time is the soccer game?', 'ans': 'ten', 'alt': ['10', 'at ten', '10:00']},
            {'q': 'Who wrote “The Swing”?', 'ans': 'Robert Louis Stevenson', 'alt': ['stevenson', 'robert louis stevenson']},
        ],
        'tf': [
            {'s': 'Jack lives in Boston.', 'ans': True, 'why': '“I live in Boston.”'},
            {'s': 'Grace plays in a band.', 'ans': False, 'why': 'She says, “No, I play at home.”'},
            {'s': 'They play soccer on Sunday.', 'ans': False, 'why': 'They play on Saturday.'},
            {'s': 'They have lunch after the game.', 'ans': True, 'why': '“We played soccer, and then we had lunch.”'},
        ],
        'order': ['Grace asks Jack about his free time.', 'Jack asks Grace if she plays in a band.', 'Jack invites Grace to play soccer.', 'They play soccer on Saturday.', 'They have lunch.'],
        'ctx': [
            {'sent': 'I read books in my free time.', 'w': 'free time', 'opts': ['time without work or school', 'a free gift', 'a bad day'], 'ans': 0, 'why': 'Free time = time to do what you like.'},
            {'sent': 'The children laughed at the joke.', 'w': 'laughed', 'opts': ['made a happy sound', 'cried', 'slept'], 'ans': 0, 'why': 'Laughed = showed that something is funny.'},
            {'sent': 'He is having a blast at the party.', 'w': 'having a blast', 'opts': ['having a great time', 'feeling tired', 'being late'], 'ans': 0, 'why': 'Having a blast = having a lot of fun.'},
        ],
        'chunkHunt': ['I enjoy reading', 'I enjoy swimming', 'I’m into music.', 'Having a blast.', 'Do you want to…?', 'I’m in!'],
        'think': 'What do you enjoy doing on Saturday? Write two sentences with enjoy + -ing.',
    },
    'convo': {
        'npc': {'name': 'Grace'},
        'story': 'You meet Grace in Boston. Talk about hobbies and make a plan for Saturday.',
        'turns': [
            {'npc': 'What do you do in your free time?', 'pt': 'O que você faz no tempo livre?', 'opts': [
                o('I play soccer and read books.', 'Jogo futebol e leio livros.', True, 'Simple present for hobbies.'),
                o('I am playing football and reading.', 'Estou jogando futebol e lendo.', False, 'Use simple present for habits.'),
                o('I do free time.', 'Eu faço tempo livre.', False, 'Wrong meaning.')]},
            {'npc': 'Cool! I play guitar.', 'pt': 'Legal! Eu toco violão.', 'opts': [
                o('Do you play in a band?', 'Você toca em banda?', True, 'A good follow-up question.'),
                o('You play violão?', 'Você toca violão?', False, 'In English: guitar.'),
                o('Cool! I am guitar.', 'Legal! Eu sou violão.', False, 'Wrong meaning.')]},
            {'npc': 'No, I play at home. Just for fun.', 'pt': 'Não, toco em casa. Só por diversão.', 'opts': [
                o('That’s nice. I enjoy playing soccer.', 'Que legal. Gosto de jogar futebol.', False, 'Fine, but the plan is the next step.'),
                o('Do you want to play soccer on Saturday?', 'Quer jogar futebol no sábado?', True, 'An invitation.'),
                o('You play for fun, I play for money.', 'Você toca por diversão, eu toco por dinheiro.', False, 'Not true for this story.')]},
            {'npc': 'Sure! What time?', 'pt': 'Claro! Que horas?', 'opts': [
                o('In ten o’clock, in park.', 'Em dez horas, em parque.', False, 'Use At ten, in the park.'),
                o('Ten in the morning is.', 'Dez da manhã é.', False, 'Word order is wrong.'),
                o('At ten, in the park.', 'Às dez, no parque.', True, 'At + time, in + place.')]},
            {'npc': 'See you on Saturday!', 'pt': 'Até sábado!', 'opts': [
                o('See you! Don’t be late!', 'Até lá! Não se atrase!', True, 'Natural and friendly.'),
                o('Until Saturday!', 'Até sábado!', False, 'Say See you on Saturday!'),
                o('Good morning!', 'Bom dia!', False, 'This is goodbye.')]},
        ],
    },
    'errors': [
        {'wrong': 'I play guitar in my free time every days.', 'fix': 'I play the guitar in my free time every day.', 'alt': 'I play guitar in my free time every days.', 'why': 'Say play the guitar, and every day is singular.'},
        {'wrong': 'I enjoy to read.', 'fix': 'I enjoy reading.', 'alt': 'I enjoy read.', 'why': 'After enjoy use verb-ing.'},
        {'wrong': 'I play futebol on Saturday.', 'fix': 'I play soccer on Saturday.', 'alt': 'I play football on Saturday.', 'why': 'In the USA, the sport is called soccer.'},
        {'wrong': 'We play in the Saturday.', 'fix': 'We play on Saturday.', 'alt': 'We play at Saturday.', 'why': 'Use on before days.'},
        {'wrong': 'Do you want play soccer?', 'fix': 'Do you want to play soccer?', 'alt': 'Do you wants to play soccer?', 'why': 'Want + to + verb.'},
    ],
    'homework': 'Say what you do in your free time and invite a friend to join you. Record a 45-second audio in English.',
    'homework_items': ['Write 4 hobbies: I enjoy…', 'Invite a friend: Do you want to…?', 'Listen to the dialogue again and shadow Grace.', 'Review: I’m into… / Having a blast. / I’m in!'],
}
