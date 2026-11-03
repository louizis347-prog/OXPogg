"""Suplemento Quest v5 · aula 19: My favorite music + regular Play the Guitar! (Guitar Hero)."""
def o(en, pt, ok, fb):
    return {'en': en, 'pt': pt, 'ok': ok, 'fb': fb}

SUPP = {
    'reg': 67,
    'badge': {'icon': '🎸', 'name': 'Music Fan', 'desc': 'Talk about music and buy concert tickets in English'},
    'sticker': {'cat': 'Everyday culture', 'title': 'Music and Concerts in the USA', 'sub': 'What music do you like?'},
    'culture': {
        'hook': 'Music is a favorite topic in the USA, from country in Nashville to pop on the radio. Learn how to say what you like and how to talk about concert tickets.',
        'facts': [
            {'vis': 'prop:coin', 'big': 'Country', 'label': 'A famous US style', 'sub': 'Nashville, Tennessee, is closely linked to country music.'},
            {'vis': 'prop:clock', 'big': 'Online', 'label': 'Buying tickets', 'sub': 'Many concert tickets are sold online, and popular shows can sell out fast.'},
            {'vis': 'prop:cup', 'big': 'Taylor Swift', 'label': 'A US singer-songwriter', 'sub': 'She started in country music and also makes pop.'},
            {'vis': 'prop:umbrella', 'big': 'Guitar Hero', 'label': 'A video game from 2005', 'sub': 'Players press buttons on a toy guitar to play rock songs.'},
        ],
        'polite': 'To share a taste, say **I like…** or **I love…**. To invite, say **Let’s…**',
        'mythfact': [
            {'s': 'Nashville is famous for country music.', 'ans': True, 'why': 'Many country music artists record and perform there.'},
            {'s': 'Concert tickets are always cheap.', 'ans': False, 'why': 'Prices can be high, especially for very popular shows.'},
            {'s': 'Guitar Hero is a video game with a toy guitar.', 'ans': True, 'why': 'It was first released in 2005.'},
            {'s': 'Taylor Swift is a singer from Brazil.', 'ans': False, 'why': 'She is an American singer-songwriter.'},
            {'s': '“Turn it up!” means “make the music louder”.', 'ans': True, 'why': 'Up = more volume.'},
        ],
        'wild': [
            {'kind': 'Concert ticket', 'lines': ['**Live in Concert**', 'Saturday, May 18 · Doors 6 p.m. · Show 8 p.m.', 'Section B · Row 12 · Seat 5', 'No refunds'], 'decode': {'q': 'What time does the show start?', 'opts': ['8 p.m.', '6 p.m.', '5 p.m.'], 'ans': 0, 'why': '“Doors 6 p.m. · Show 8 p.m.”'}},
            {'kind': 'Text message', 'lines': ['Tickets go on sale at 10 a.m. today!', 'Let’s buy them together.', 'I’m obsessed with this band!'], 'decode': {'q': 'When do the tickets go on sale?', 'opts': ['10 a.m. today', '10 p.m. tomorrow', 'Next week'], 'ans': 0, 'why': '“10 a.m. today.”'}},
        ],
        'compare': {
            'br': 'Brazil has many styles, such as samba, forró and sertanejo, and concerts are a big part of life.',
            'us': 'In the USA people also love pop, rock, hip hop and country, and big shows often have tickets sold online.',
            'tip': 'To talk about taste, use I like + style or I love + singer.',
            'ask': 'What music do you like? Who is your favorite singer? Say it in English.',
        },
        'quiz': [
            {'q': 'You want to say your music taste. You say…', 'opts': ['I like pop and rock.', 'I am liking pop.', 'I like of pop.'], 'ans': 0, 'why': 'Like + noun, no preposition.'},
            {'q': 'Tickets are expensive. You say…', 'opts': ['They are expensive.', 'It is expensive.', 'They is expensive.'], 'ans': 0, 'why': 'Tickets = plural, so They are.'},
            {'q': 'A song is great. You say…', 'opts': ['This song is a banger!', 'This song is a bang.', 'This song are great.'], 'ans': 0, 'why': 'A banger is a very good song.'},
        ],
    },
    'reading': {
        'genre': 'Blog post',
        'title': 'My first concert',
        'text': [
            'My name is Emily, and I live in **Charlotte**. I love music. I like pop and country, and my friend Simone likes rock. We always say, “**Turn it up**!” when a good song starts. “**Nice tune**!” is our favorite phrase.',
            'Last week Simone asked me, “Who is your favorite singer?” “I love Taylor Swift,” I said. “Me too!” she said. “Do you have tickets?” “Not yet. They are expensive,” I said. “Let’s buy them together.”',
            'Next day we got the tickets online. I felt very happy. I took my old guitar and played the same song again and again. **Practice makes perfect**, my teacher says. “**Play it again**!” Simone said, and I played the song three more times.',
            'Do you know the game “Guitar Hero”? It came out in 2005. You hold a toy guitar with colored buttons, and you press the right button at the right time. It has songs from famous rock bands. Many people learned to love music with that game.',
            'Now I wait for the big night. I know I will sing and dance. Music makes me happy, and it also helps me learn English. What music do you like?',
        ],
        'glossary': [{'w': 'favorite', 'pt': 'favorito'}, {'w': 'singer', 'pt': 'cantor'}, {'w': 'tickets', 'pt': 'ingressos'}, {'w': 'expensive', 'pt': 'caro'}, {'w': 'online', 'pt': 'pela internet'}, {'w': 'guitar', 'pt': 'violão, guitarra'}, {'w': 'practice', 'pt': 'treino, prática'}, {'w': 'buttons', 'pt': 'botões'}, {'w': 'dance', 'pt': 'dançar'}],
        'fast': {'q': 'What is this text about?', 'opts': ['Music and buying concert tickets', 'A cooking class', 'A walk in the park'], 'ans': 0, 'why': 'Emily and Simone talk about music and buy tickets.'},
        'scan': [
            {'q': 'What music does Simone like?', 'ans': 'rock', 'alt': ['Rock']},
            {'q': 'Who is Emily’s favorite singer?', 'ans': 'Taylor Swift', 'alt': ['taylor swift']},
            {'q': 'In which year did Guitar Hero come out?', 'ans': '2005', 'alt': ['in 2005']},
        ],
        'tf': [
            {'s': 'Emily lives in Charlotte.', 'ans': True, 'why': '“I live in Charlotte.”'},
            {'s': 'Simone likes country music best.', 'ans': False, 'why': 'Simone likes rock.'},
            {'s': 'The tickets are expensive.', 'ans': True, 'why': '“They are expensive.”'},
            {'s': 'They buy the tickets at the box office.', 'ans': False, 'why': 'They got the tickets online.'},
        ],
        'order': ['Simone asks about a favorite singer.', 'Emily says she loves Taylor Swift.', 'They say the tickets are expensive.', 'They buy tickets online.', 'Emily plays the guitar at home.'],
        'ctx': [
            {'sent': 'Who is your favorite singer?', 'w': 'favorite', 'opts': ['the one you like best', 'the oldest', 'the loudest'], 'ans': 0, 'why': 'Favorite = best liked.'},
            {'sent': 'These shoes are expensive.', 'w': 'expensive', 'opts': ['costs a lot', 'costs little', 'is free'], 'ans': 0, 'why': 'Expensive = high price.'},
            {'sent': 'I practice the guitar every day.', 'w': 'practice', 'opts': ['do again to get better', 'sell', 'break'], 'ans': 0, 'why': 'Practice = repeat to improve.'},
        ],
        'chunkHunt': ['Play it again!', 'Practice makes perfect.', 'Turn it up!', 'Nice tune!'],
        'think': 'Which song do you listen to the most? Say why you like it.',
    },
    'convo': {
        'npc': {'name': 'Simone'},
        'story': 'You talk with Simone in Charlotte about music and plan to buy concert tickets.',
        'turns': [
            {'npc': 'What music do you like?', 'pt': 'Que música você gosta?', 'opts': [
                o('I like pop and country. And you?', 'Gosto de pop e country. E você?', True, 'Answer and ask back.'),
                o('I like of pop and country.', 'Gosto de de pop e country.', False, 'Do not add of after like.'),
                o('I am pop.', 'Eu sou pop.', False, 'Wrong meaning.')]},
            {'npc': 'I like rock. Who is your favorite singer?', 'pt': 'Gosto de rock. Quem é seu cantor favorito?', 'opts': [
                o('My favorite singer is rock.', 'Meu cantor favorito é rock.', False, 'Rock is a style, not a singer.'),
                o('The singer favorite is Taylor.', 'O cantor favorito é Taylor.', False, 'Word order: my favorite singer.'),
                o('I love Taylor Swift.', 'Adoro a Taylor Swift.', True, 'I love + singer.')]},
            {'npc': 'Me too! Do you have tickets?', 'pt': 'Eu também! Você tem ingressos?', 'opts': [
                o('Not yet. They are expensive.', 'Ainda não. São caros.', True, 'Natural answer with a reason.'),
                o('No, I have not yet money.', 'Não, eu não tenho ainda dinheiro.', False, 'Say Not yet.'),
                o('Yes, I am tickets.', 'Sim, eu sou ingressos.', False, 'Wrong meaning.')]},
            {'npc': 'Let’s buy them together.', 'pt': 'Vamos comprar juntos.', 'opts': [
                o('No, let’s not.', 'Não, vamos não.', False, 'It does not fit the story.'),
                o('Yes, we buy together.', 'Sim, nós compramos juntos.', False, 'Say Great idea! or Yes, let’s.'),
                o('Great idea!', 'Ótima ideia!', True, 'A natural answer.')]},
            {'npc': 'Let’s get the tickets today!', 'pt': 'Vamos comprar os ingressos hoje!', 'opts': [
                o('Okay! Turn it up!', 'Ok! Aumenta o som!', False, 'Turn it up! is for music.'),
                o('Okay! Let’s go to a concert!', 'Ok! Vamos a um show!', True, 'Matching the excitement.'),
                o('I get the ticket yesterday.', 'Eu compro o ingresso ontem.', False, 'Wrong time.')]},
        ],
    },
    'errors': [
        {'wrong': 'I like very much pop.', 'fix': 'I like pop very much.', 'alt': 'I very like pop.', 'why': 'Very much goes after the noun.'},
        {'wrong': 'She play the guitar.', 'fix': 'She plays the guitar.', 'alt': 'She playing the guitar.', 'why': 'He / she / it takes -s.'},
        {'wrong': 'The tickets is expensive.', 'fix': 'The tickets are expensive.', 'alt': 'The ticket are expensive.', 'why': 'Tickets is plural, so use are.'},
        {'wrong': 'I play guitar.', 'fix': 'I play the guitar.', 'alt': 'I play a guitar.', 'why': 'With instruments, use play the + instrument.'},
        {'wrong': 'My favorite singer are Taylor.', 'fix': 'My favorite singer is Taylor Swift.', 'alt': 'My favorite singers is Taylor.', 'why': 'One singer = is.'},
    ],
    'homework': 'Tell your teacher about your favorite singer and song in an audio of 45 seconds in English.',
    'homework_items': ['Say your favorite singer and song.', 'Write 3 sentences: I like… / I love…', 'Listen to the dialogue again and shadow Simone.', 'Review: Turn it up! / Play it again! / Nice tune!'],
}
