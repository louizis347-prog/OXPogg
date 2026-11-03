"""Suplemento Quest v5 · aula 12: Months and birthdays + regular What's the date? (Statue of Liberty)."""
def o(en, pt, ok, fb):
    return {'en': en, 'pt': pt, 'ok': ok, 'fb': fb}

SUPP = {
    'reg': 97,
    'badge': {'icon': '🎂', 'name': 'Date Master', 'desc': 'Say months, dates and birthdays in English'},
    'sticker': {'cat': 'Everyday culture', 'title': 'Birthdays and the Fourth of July', 'sub': 'What’s the date?'},
    'culture': {
        'hook': 'Birthdays and holidays are big moments in the USA. Learn how to say the date, because in the USA the month comes first.',
        'facts': [
            {'vis': 'prop:clock', 'big': '7/4', 'label': 'Month first', 'sub': 'In the USA, 7/4 means July 4. In Brazil, 7/4 means April 7.'},
            {'vis': 'prop:umbrella', 'big': 'July 4', 'label': 'Independence Day', 'sub': 'The Declaration of Independence was adopted on July 4, 1776. People have fireworks and picnics.'},
            {'vis': 'prop:cup', 'big': 'Make a wish', 'label': 'Birthday cake', 'sub': 'People sing “Happy Birthday to You”, then blow out the candles.'},
            {'vis': 'prop:bag', 'big': 'Oct 28, 1886', 'label': 'The Statue of Liberty', 'sub': 'A gift from France, dedicated in New York.'},
        ],
        'polite': 'Say **Happy birthday!** and add the person’s name. Say dates with ordinal numbers: “March tenth.”',
        'mythfact': [
            {'s': 'In the USA, 10/3 usually means October 3.', 'ans': True, 'why': 'The USA writes month/day. Many other countries write day/month.'},
            {'s': 'Independence Day in the USA is in December.', 'ans': False, 'why': 'It is on July 4.'},
            {'s': 'The Statue of Liberty was a gift from France.', 'ans': True, 'why': 'France gave it to the USA. It was dedicated in 1886.'},
            {'s': 'People often blow out candles on a birthday cake.', 'ans': True, 'why': 'They also make a wish before they blow.'},
            {'s': 'July fourth is called “Thanksgiving”.', 'ans': False, 'why': 'July 4 is Independence Day. Thanksgiving is in November.'},
        ],
        'wild': [
            {'kind': 'Party invitation', 'lines': ['**You’re invited!**', 'Marcus’s birthday party', 'Saturday, March 10 · 6 p.m.', 'Bring a friend. We’ll have cake!'], 'decode': {'q': 'What day and month is the party?', 'opts': ['March 10', 'October 3', 'July 4'], 'ans': 0, 'why': '“Saturday, March 10.”'}},
            {'kind': 'Calendar note', 'lines': ['**July 4** · Independence Day', 'No mail today. Parade at 10 a.m.', 'Fireworks at 9 p.m.'], 'decode': {'q': 'What happens at 9 p.m.?', 'opts': ['Fireworks', 'A parade', 'Mail delivery'], 'ans': 0, 'why': '“Fireworks at 9 p.m.”'}},
        ],
        'compare': {
            'br': 'In Brazil, Independence Day is September 7, and you write dates as day/month, like 10/03 for March 10.',
            'us': 'In the USA, Independence Day is July 4, and you write month/day, like 3/10 for March 10.',
            'tip': 'To avoid confusion, write the month in letters: March 10, not 3/10.',
            'ask': 'When is your birthday? Say the month and the day in English.',
        },
        'quiz': [
            {'q': 'How do you answer “When is your birthday?”', 'opts': ['It’s on March tenth.', 'It has March ten.', 'I am March.'], 'ans': 0, 'why': 'Use It’s on + month + date.'},
            {'q': 'What do you say to someone on a birthday?', 'opts': ['Happy birthday!', 'Good birthday!', 'Nice year!'], 'ans': 0, 'why': 'Happy birthday! is the set phrase.'},
            {'q': 'In the USA, 12/25 means…', 'opts': ['December 25', 'The 12th of May', 'August 25'], 'ans': 0, 'why': 'Month first: December 25.'},
        ],
    },
    'reading': {
        'genre': 'Diary entry',
        'title': 'A birthday on the Fourth of July',
        'text': [
            'Dear diary, today is a special day. My friend Evan lives in **Detroit**, and his birthday is on July fourth. It is also Independence Day!',
            'This morning I asked him, “**What’s the date today?**” He laughed. “**I forgot**!” he said. “Today is my birthday!” I said, “**Happy birthday**! **Make a wish**!”',
            'We went to a park. Many people had picnics, and children had flags. I thought about the Statue of Liberty in New York. France gave it to the United States, and people dedicated it on October 28, 1886. It is a famous symbol of freedom, and many visitors take photos of it every day.',
            'My birthday is in March, on March tenth. Evan said, “Let’s have a party **on a holiday** next year!” “It’s a date,” I said. We both laughed. In the USA, the month comes first, so I write 3/10 for my birthday. My friends say that is easy to remember, and I smile.',
            'At night we saw fireworks over the river. Evan blew out the candles on his cake. It was the **best day ever**.',
        ],
        'glossary': [{'w': 'diary', 'pt': 'diário'}, {'w': 'birthday', 'pt': 'aniversário'}, {'w': 'park', 'pt': 'parque'}, {'w': 'picnics', 'pt': 'piqueniques'}, {'w': 'flags', 'pt': 'bandeiras'}, {'w': 'gave', 'pt': 'deu'}, {'w': 'freedom', 'pt': 'liberdade'}, {'w': 'fireworks', 'pt': 'fogos de artifício'}, {'w': 'candles', 'pt': 'velas'}, {'w': 'holiday', 'pt': 'feriado'}],
        'fast': {'q': 'What is this text about?', 'opts': ['A birthday on Independence Day', 'A trip to Brazil', 'A school exam'], 'ans': 0, 'why': 'Evan’s birthday is on July 4, Independence Day.'},
        'scan': [
            {'q': 'What is Evan’s birthday?', 'ans': 'July fourth', 'alt': ['july 4', 'july fourth', 'july 4th', 'the fourth of july']},
            {'q': 'What month is the writer’s birthday?', 'ans': 'March', 'alt': ['march', 'march tenth', 'march 10']},
            {'q': 'Which country gave the Statue of Liberty to the USA?', 'ans': 'France', 'alt': ['france']},
        ],
        'tf': [
            {'s': 'Evan lives in Detroit.', 'ans': True, 'why': '“My friend Evan lives in Detroit.”'},
            {'s': 'Evan remembers the date.', 'ans': False, 'why': 'He says, “I forgot!”'},
            {'s': 'The writer’s birthday is in July.', 'ans': False, 'why': 'It is in March, on March tenth.'},
            {'s': 'They see fireworks at night.', 'ans': True, 'why': '“At night we saw fireworks over the river.”'},
        ],
        'order': ['The writer asks Evan the date.', 'Evan says he forgot his own birthday.', 'They go to a park.', 'They talk about a party next year.', 'They watch fireworks and Evan blows out the candles.'],
        'ctx': [
            {'sent': 'I forgot my keys at home.', 'w': 'forgot', 'opts': ['did not remember', 'found', 'lost forever'], 'ans': 0, 'why': 'Forgot = did not remember.'},
            {'sent': 'It is a holiday, so no school today.', 'w': 'holiday', 'opts': ['a special day off', 'a test', 'a bad day'], 'ans': 0, 'why': 'A holiday is a special day, often with no work.'},
            {'sent': 'She is making a wish before she blows out the candles.', 'w': 'wish', 'opts': ['something you hope for', 'a loud song', 'a gift box'], 'ans': 0, 'why': 'A wish is something you hope will happen.'},
        ],
        'chunkHunt': ['What’s the date today?', 'I forgot.', 'on a holiday', 'It’s a date.', 'Happy birthday'],
        'think': 'Which holiday do you like best? What is the date, and what do you do that day?',
    },
    'convo': {
        'npc': {'name': 'Evan'},
        'story': 'You are talking with Evan in Detroit. His birthday is on the Fourth of July.',
        'turns': [
            {'npc': 'When is your birthday?', 'pt': 'Quando é seu aniversário?', 'opts': [
                o('I have birthday in March.', 'Eu tenho aniversário em março.', False, 'Say My birthday is in March.'),
                o('It’s in March. On March tenth.', 'É em março. Dia dez de março.', True, 'Month + date with an ordinal number.'),
                o('It is March the ten years.', 'É março os dez anos.', False, 'Not a date. Say March tenth.')]},
            {'npc': 'Mine is in July. July fourth!', 'pt': 'O meu é em julho. Dia quatro de julho!', 'opts': [
                o('Wow, Independence Day!', 'Uau, Dia da Independência!', True, 'July 4 is Independence Day in the USA.'),
                o('Wow, you are July!', 'Uau, você é julho!', False, 'Wrong meaning.'),
                o('Wow, Thanksgiving!', 'Uau, Dia de Ação de Graças!', False, 'Thanksgiving is in November.')]},
            {'npc': 'Yes. Everyone has fireworks.', 'pt': 'Sim. Todo mundo tem fogos.', 'opts': [
                o('That’s cool. Let’s have a party.', 'Que legal. Vamos fazer uma festa.', True, 'Natural reaction and invitation.'),
                o('That is cool. We make a party.', 'Isso é legal. Nós fazemos uma festa.', False, 'Use Let’s have a party.'),
                o('No, I do not have a firework.', 'Não, eu não tenho um fogo.', False, 'Out of context.')]},
            {'npc': 'Great idea! I’ll bring a cake.', 'pt': 'Ótima ideia! Eu levo um bolo.', 'opts': [
                o('Happy birthday for you!', 'Feliz aniversário para você!', False, 'Say Happy birthday! (and it is not today).'),
                o('Perfect. See you in March.', 'Perfeito. Até março.', True, 'A natural way to close the plan.'),
                o('I will to bring a cake.', 'Eu vou levar um bolo.', False, 'It is Evan who brings the cake.')]},
            {'npc': 'Don’t forget the cake!', 'pt': 'Não esqueça o bolo!', 'opts': [
                o('Best day ever!', 'Melhor dia de todos!', False, 'Fun, but it does not answer the joke.'),
                o('I forget not.', 'Eu esqueço não.', False, 'Say I won’t forget!'),
                o('I won’t forget. Happy birthday!', 'Não vou esquecer. Feliz aniversário!', True, 'Natural and friendly.')]},
        ],
    },
    'errors': [
        {'wrong': 'My birthday is on March.', 'fix': 'My birthday is in March.', 'alt': 'My birthday is at March.', 'why': 'Use in before a month, on before a date.'},
        {'wrong': 'My birthday is in March ten.', 'fix': 'My birthday is on March tenth.', 'alt': 'My birthday is at March tenth.', 'why': 'Use on + the date.'},
        {'wrong': 'I have 20 years.', 'fix': 'I am 20 years old.', 'alt': 'I am 20 years.', 'why': 'English uses be for age.'},
        {'wrong': 'When is the your birthday?', 'fix': 'When is your birthday?', 'alt': 'When is you birthday?', 'why': 'No the before your. Use your, not you.'},
        {'wrong': 'Today is 4 of July.', 'fix': 'Today is July fourth.', 'alt': 'Today is the 4 July.', 'why': 'In the USA say July fourth, month first.'},
    ],
    'homework': 'Write the month and day of five birthdays in your family in English and record yourself saying them.',
    'homework_items': ['Say the 12 months out loud.', 'Write 5 birthdays: “Mom’s birthday is on ...”.', 'Listen to the dialogue again and shadow Evan.', 'Review: What’s the date? / on a holiday / It’s a date.'],
}
