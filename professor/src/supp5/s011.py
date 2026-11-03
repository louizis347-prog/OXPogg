"""Suplemento Quest v5 · aula 11: What time is it? + regular What Time Is It? (Hickory Dickory Dock)."""
def o(en, pt, ok, fb):
    return {'en': en, 'pt': pt, 'ok': ok, 'fb': fb}

SUPP = {
    'reg': 25,
    'badge': {'icon': '⏰', 'name': 'Time Keeper', 'desc': 'Ask the time and talk about schedules in English'},
    'sticker': {'cat': 'Everyday culture', 'title': 'Clocks in the USA', 'sub': 'What time is it?'},
    'culture': {
        'hook': 'Asking the time sounds simple, but in the USA people use a.m. and p.m., half past and quarter after. Learn the small habits so you never miss your bus.',
        'facts': [
            {'vis': 'prop:clock', 'big': 'a.m. / p.m.', 'label': 'The 12-hour clock', 'sub': '7 a.m. = morning · 7 p.m. = evening. Most people say it this way every day.'},
            {'vis': 'prop:clock', 'big': '2:30', 'label': 'Two thirty', 'sub': 'Also “half past two”. 2:15 can be “quarter after two”.'},
            {'vis': 'prop:umbrella', 'big': 'Spring forward', 'label': 'Daylight saving time', 'sub': 'In most of the USA the clocks move one hour in March and again in November.'},
            {'vis': 'prop:bag', 'big': '4 zones', 'label': 'Time zones in the lower 48 states', 'sub': 'Eastern, Central, Mountain and Pacific. Portland is on Pacific time.'},
        ],
        'polite': 'Start with **Excuse me** when you ask a stranger the time. Then say **Thanks!**',
        'mythfact': [
            {'s': 'Most people in the USA say the time with a.m. and p.m.', 'ans': True, 'why': 'The 12-hour clock is normal in daily life. The 24-hour clock is used by the military and in some jobs.'},
            {'s': 'The lower 48 states all share one time zone.', 'ans': False, 'why': 'There are four time zones: Eastern, Central, Mountain and Pacific.'},
            {'s': 'In most of the USA, clocks change twice a year.', 'ans': True, 'why': 'Daylight saving time starts in March and ends in November. Arizona is a well-known exception.'},
            {'s': '“Quarter after three” means 3:45.', 'ans': False, 'why': 'Quarter after three = 3:15. “Quarter to four” = 3:45.'},
            {'s': 'The nursery rhyme “Hickory Dickory Dock” has a mouse in it.', 'ans': True, 'why': 'The mouse runs up the clock, and the clock strikes one.'},
        ],
        'wild': [
            {'kind': 'Bus schedule', 'lines': ['**Route 12 · Downtown**', 'Leaves Pine Street: 2:45 p.m. · 3:00 p.m. · 3:15 p.m.', 'Last bus: 11:30 p.m.'], 'decode': {'q': 'You arrive at 2:50 p.m. When is the next bus?', 'opts': ['3:00 p.m.', '2:45 p.m.', '3:15 a.m.'], 'ans': 0, 'why': 'The 2:45 bus is gone. The next one is at 3:00 p.m.'}},
            {'kind': 'Text message', 'lines': ['Hey! The movie starts at 7:15.', 'Let’s meet at a quarter to seven.', 'Don’t be late!'], 'decode': {'q': 'What time do they meet?', 'opts': ['6:45', '7:45', '7:15'], 'ans': 0, 'why': 'A quarter to seven = 6:45.'}},
        ],
        'compare': {
            'br': 'In Brazil people say “duas e meia” and often write “14h30” on signs and tickets, so the 24-hour style is easy to see.',
            'us': 'In the USA you usually say “two thirty” and write 2:30 p.m. Tickets and schedules often show a.m. and p.m., not 14:30.',
            'tip': 'When you read a schedule, look for a.m. and p.m. first. Then you will not mix up morning and evening.',
            'ask': 'What time do you wake up? Say it in English with a.m. or p.m.',
        },
        'quiz': [
            {'q': 'A stranger can help you. You say…', 'opts': ['Excuse me, what time is it?', 'You, time?', 'What is your time?'], 'ans': 0, 'why': 'Excuse me + What time is it? is polite and natural.'},
            {'q': '“It’s a quarter to six” means…', 'opts': ['5:45', '6:15', '6:45'], 'ans': 0, 'why': 'A quarter to six = 15 minutes before six = 5:45.'},
            {'q': 'The bus leaves at 8 p.m. Is that morning or evening?', 'opts': ['Evening', 'Morning', 'Midnight'], 'ans': 0, 'why': 'p.m. = after noon. 8 p.m. is evening.'},
        ],
    },
    'reading': {
        'genre': 'Blog post',
        'title': 'Just in time at the bus stop',
        'text': [
            'Last Friday I was at a bus stop in **Portland**. I looked at my phone, but the battery was dead. So I asked a woman, “**Excuse me, what time is it?**”',
            'She smiled and looked at her watch. “**It’s two thirty**,” she said. “**Is that the time?**” I said. “My bus is at three o’clock!” I had only thirty minutes, and my friend Carlos was late too.',
            'There was an old clock on the wall of a small cafe, and it made me think of a rhyme. In “Hickory Dickory Dock,” a mouse runs up the clock. The clock strikes one, and the mouse runs down. The rhyme is from 1744, and children still learn it today.',
            'I bought a coffee and sat by the window. **Time flies** when you drink coffee! At ten to three I walked back to the stop. Carlos was there. “Dude, we’re late!” he said. “Chill,” I said. “We have time.”',
            'The bus came at three o’clock, and we got on **just in time**. It was a good day. Now I always check my phone battery in the morning.',
        ],
        'glossary': [{'w': 'bus stop', 'pt': 'ponto de ônibus'}, {'w': 'battery', 'pt': 'bateria'}, {'w': 'watch', 'pt': 'relógio de pulso'}, {'w': 'clock', 'pt': 'relógio de parede'}, {'w': 'mouse', 'pt': 'rato'}, {'w': 'rhyme', 'pt': 'cantiga, rima'}, {'w': 'window', 'pt': 'janela'}, {'w': 'wall', 'pt': 'parede'}, {'w': 'late', 'pt': 'atrasado'}],
        'fast': {'q': 'What is this text about?', 'opts': ['Catching a bus on time', 'Cooking dinner', 'A school test'], 'ans': 0, 'why': 'The writer asks the time and catches the bus just in time.'},
        'scan': [
            {'q': 'What time is the bus?', 'ans': 'three o’clock', 'alt': ['3', '3:00', 'three', 'three o\'clock']},
            {'q': 'What city is the bus stop in?', 'ans': 'Portland', 'alt': ['portland']},
            {'q': 'What year is the rhyme from?', 'ans': '1744', 'alt': ['in 1744']},
        ],
        'tf': [
            {'s': 'The writer’s phone battery is dead.', 'ans': True, 'why': '“The battery was dead.”'},
            {'s': 'The woman says it is three thirty.', 'ans': False, 'why': 'She says, “It’s two thirty.”'},
            {'s': 'The writer drinks a coffee before the bus.', 'ans': True, 'why': '“I bought a coffee and sat by the window.”'},
            {'s': 'They miss the bus.', 'ans': False, 'why': 'They got on just in time.'},
            {'s': 'Carlos is already at the stop at the beginning.', 'ans': False, 'why': 'Carlos was late too.'},
        ],
        'order': ['The writer sees that the phone battery is dead.', 'A woman says it is two thirty.', 'The writer buys a coffee.', 'The writer meets Carlos at the stop.', 'They get on the bus just in time.'],
        'ctx': [
            {'sent': 'My phone battery was dead.', 'w': 'dead', 'opts': ['empty, without power', 'very new', 'loud'], 'ans': 0, 'why': 'A dead battery has no power.'},
            {'sent': 'Time flies when you are happy.', 'w': 'flies', 'opts': ['goes very fast', 'goes very slowly', 'stops'], 'ans': 0, 'why': 'Time flies = time passes quickly.'},
            {'sent': 'We got on the bus just in time.', 'w': 'just in time', 'opts': ['not late', 'very late', 'too early'], 'ans': 0, 'why': 'Just in time = at the last good moment.'},
        ],
        'chunkHunt': ['Excuse me, what time is it?', 'It’s two thirty.', 'Is that the time?', 'Time flies.', 'just in time'],
        'think': 'When are you late and when are you early? What time do you leave home every day?',
    },
    'convo': {
        'npc': {'name': 'Carlos'},
        'story': 'You are at a bus stop in Portland. Carlos is waiting too. Ask and answer about the time.',
        'turns': [
            {'npc': 'Excuse me, what time is it?', 'pt': 'Com licença, que horas são?', 'opts': [
                o('It’s two thirty.', 'São duas e meia.', True, 'Natural: It’s + the time.'),
                o('It is two and half.', 'São duas e meia.', False, 'In English: two thirty or half past two.'),
                o('I am two thirty.', 'Eu sou duas e meia.', False, 'Use It’s for the time, not I am.')]},
            {'npc': 'Thanks! What time is the bus?', 'pt': 'Valeu! Que horas é o ônibus?', 'opts': [
                o('The bus has three o’clock.', 'O ônibus tem três horas.', False, 'Not natural. Say It’s at three o’clock.'),
                o('It’s at three o’clock.', 'É às três horas.', True, 'Use at before a time.'),
                o('Yes, two thirty.', 'Sim, duas e meia.', False, 'It does not answer the question.')]},
            {'npc': 'Oh good. We have thirty minutes.', 'pt': 'Ah, bom. Temos trinta minutos.', 'opts': [
                o('Yes. Do you want coffee?', 'Sim. Você quer café?', True, 'A friendly next step with Do you want…?'),
                o('Yes. You want coffee?', 'Sim. Você quer café?', False, 'Questions need Do: Do you want…?'),
                o('No, I am two coffees.', 'Não, eu sou dois cafés.', False, 'Wrong meaning.')]},
            {'npc': 'Yes, please! There’s a cafe here.', 'pt': 'Quero, por favor! Tem um café aqui.', 'opts': [
                o('Great. Let’s go.', 'Ótimo. Vamos.', True, 'Short and natural.'),
                o('Great. I go to the cafe is.', 'Ótimo. Eu vou ao café é.', False, 'Word order is wrong.'),
                o('Great. We are late.', 'Ótimo. Estamos atrasados.', False, 'You still have time. Do not panic!')]},
            {'npc': 'Perfect. The bus is here!', 'pt': 'Perfeito. O ônibus chegou!', 'opts': [
                o('Phew! Just in time.', 'Ufa! Em cima da hora.', True, 'Just in time = not late.'),
                o('Phew! It is the time.', 'Ufa! É a hora.', False, 'Not natural. Say Just in time.'),
                o('Phew! I am late.', 'Ufa! Eu sou atrasado.', False, 'You are not late. Use just in time.')]},
        ],
    },
    'errors': [
        {'wrong': 'What hour is it?', 'fix': 'What time is it?', 'alt': 'Which time is it?', 'why': 'In English we ask What time is it?, not What hour.'},
        {'wrong': 'The bus is in three o’clock.', 'fix': 'The bus is at three o’clock.', 'alt': 'The bus is on three o’clock.', 'why': 'Use at before a clock time.'},
        {'wrong': 'It’s two and half.', 'fix': 'It’s two thirty.', 'alt': 'It’s two and thirty.', 'why': 'Say two thirty or half past two.'},
        {'wrong': 'Are two thirty.', 'fix': 'It’s two thirty.', 'alt': 'I am two thirty.', 'why': 'For time, use It’s.'},
        {'wrong': 'We have thirty minute.', 'fix': 'We have thirty minutes.', 'alt': 'We has thirty minutes.', 'why': 'More than one = minutes (plural -s).'},
    ],
    'homework': 'Look at the clock three times today and say the time out loud in English, then send a 30-second audio to your teacher.',
    'homework_items': ['Say the time 3 times today in English.', 'Write your daily schedule with 5 times (use at).', 'Listen to the dialogue again and shadow Carlos.', 'Review: What time is it? / It’s at… / Just in time.'],
}
