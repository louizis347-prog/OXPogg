"""Suplemento Quest v5 · aula 13: Colors and things + regular What Color Is It? (The Purple Cow)."""
def o(en, pt, ok, fb):
    return {'en': en, 'pt': pt, 'ok': ok, 'fb': fb}

SUPP = {
    'reg': 22,
    'badge': {'icon': '🎨', 'name': 'Color Pro', 'desc': 'Name colors and say what is yours in English'},
    'sticker': {'cat': 'Everyday culture', 'title': 'Colors in the USA', 'sub': 'What color is it?'},
    'culture': {
        'hook': 'Some colors in the USA are famous all over the world. Yellow taxis, yellow school buses and green dollars all tell a small story about daily life.',
        'facts': [
            {'vis': 'prop:coin', 'big': 'Green', 'label': 'The dollar bill', 'sub': 'People call US paper money “greenbacks”.'},
            {'vis': 'prop:bag', 'big': 'Yellow', 'label': 'School buses', 'sub': 'Yellow school buses are easy to see, so cars know to stop.'},
            {'vis': 'prop:umbrella', 'big': 'Red, white, blue', 'label': 'The US flag', 'sub': 'The flag has 13 stripes and 50 stars.'},
            {'vis': 'prop:cup', 'big': 'Yellow cabs', 'label': 'New York City taxis', 'sub': 'Yellow taxis are a symbol of the city.'},
        ],
        'polite': 'To ask whose it is, say **Excuse me, is this your bag?** Then say **Thanks!**',
        'mythfact': [
            {'s': 'School buses in the USA are usually yellow.', 'ans': True, 'why': 'Yellow school buses are the standard in the USA.'},
            {'s': 'New York City taxis are famous for being purple.', 'ans': False, 'why': 'They are famous for being yellow.'},
            {'s': 'The US flag has red, white and blue.', 'ans': True, 'why': 'Red, white and blue are the colors of the US flag.'},
            {'s': 'A “greenback” is a US dollar.', 'ans': True, 'why': 'The back of the bill is green, so the name stuck.'},
            {'s': 'The poem “The Purple Cow” says the writer saw many purple cows.', 'ans': False, 'why': 'The poet says he never saw one and never hopes to see one.'},
        ],
        'wild': [
            {'kind': 'Lost and found sign', 'lines': ['**Lost: one backpack**', 'Color: blue with a red zipper', 'Lost at the bus station on Monday', 'Call 555-0134'], 'decode': {'q': 'What color is the zipper?', 'opts': ['Red', 'Blue', 'Black'], 'ans': 0, 'why': '“Blue with a red zipper.”'}},
            {'kind': 'Shopping website', 'lines': ['**Phone case**', 'Colors: black · white · green', 'Free shipping on orders over $25'], 'decode': {'q': 'Which color is NOT in this list?', 'opts': ['Red', 'Black', 'White'], 'ans': 0, 'why': 'The colors are black, white and green. Red is not there.'}},
        ],
        'compare': {
            'br': 'The Brazilian flag is green, yellow, blue and white. Many Brazilians say “a minha é azul” without repeating the noun.',
            'us': 'The US flag is red, white and blue. In English you say “mine is blue”: mine, yours, his, hers replace “my bag”, “your bag”.',
            'tip': 'Say “Is this yours?” and “It’s mine.” You do not need to repeat the noun.',
            'ask': 'What color is your phone? Say it in English.',
        },
        'quiz': [
            {'q': 'Someone asks “Is this your bag?” It is yours. You say…', 'opts': ['Yes, it’s mine.', 'Yes, it’s me.', 'Yes, it’s my.'], 'ans': 0, 'why': 'Mine replaces “my bag”.'},
            {'q': 'What color is a typical US school bus?', 'opts': ['Yellow', 'Green', 'Purple'], 'ans': 0, 'why': 'School buses are yellow.'},
            {'q': 'A nice way to say you like a color is…', 'opts': ['Nice color!', 'Color is nice me.', 'I am color.'], 'ans': 0, 'why': 'Nice color! is short and friendly.'},
        ],
    },
    'reading': {
        'genre': 'Short story',
        'title': 'The red bag at the airport',
        'text': [
            'Lena is at the airport in **Phoenix**. She waits for her bag. Many bags come out on the belt. There are black bags, green bags and blue bags.',
            'A young man points at a red bag. “**Excuse me, is this your bag?**” he asks. “No,” says Lena. “**Mine is blue**. This one is red.” Then she sees her bag. “Oh, **that’s mine**! Thank you!”',
            'The man smiles. “**What color is your phone?**” he asks. It is a strange question, but Lena answers: “It’s black. And yours?” “Mine is white,” he says. “**Nice colors!**”',
            'Lena thinks of a funny poem called “The Purple Cow.” An American writer, Gelett Burgess, wrote it in 1895. He says he **never saw** a purple cow, and he never hopes to see one. “**That’s funny!**” Lena thinks. Her bag is not purple. It is a normal blue, but it is easy to find.',
            'The man takes the red bag. “**Not my color**,” he laughs, “but it is my bag!” Lena says goodbye. “**Take care of your things!**” she says. He smiles and waves.',
        ],
        'glossary': [{'w': 'airport', 'pt': 'aeroporto'}, {'w': 'belt', 'pt': 'esteira'}, {'w': 'points', 'pt': 'aponta'}, {'w': 'strange', 'pt': 'estranho'}, {'w': 'poem', 'pt': 'poema'}, {'w': 'writer', 'pt': 'escritor'}, {'w': 'purple', 'pt': 'roxo'}, {'w': 'waves', 'pt': 'acena'}, {'w': 'easy', 'pt': 'fácil'}],
        'fast': {'q': 'What is this text about?', 'opts': ['Finding the right bag at an airport', 'Buying a new phone', 'Painting a house'], 'ans': 0, 'why': 'Lena finds her blue bag at the airport.'},
        'scan': [
            {'q': 'What color is Lena’s bag?', 'ans': 'blue', 'alt': ['Blue', 'it is blue']},
            {'q': 'What color is Lena’s phone?', 'ans': 'black', 'alt': ['Black', 'it is black']},
            {'q': 'In what year did Gelett Burgess write the poem?', 'ans': '1895', 'alt': ['in 1895']},
        ],
        'tf': [
            {'s': 'Lena is at the airport in Phoenix.', 'ans': True, 'why': '“Lena is at the airport in Phoenix.”'},
            {'s': 'The red bag is Lena’s.', 'ans': False, 'why': 'Lena says, “Mine is blue. This one is red.”'},
            {'s': 'The young man’s phone is white.', 'ans': True, 'why': '“Mine is white,” he says.'},
            {'s': 'Lena’s bag is purple.', 'ans': False, 'why': 'It is a normal blue bag.'},
        ],
        'order': ['Lena waits at the airport.', 'A man asks about the red bag.', 'Lena finds her blue bag.', 'They talk about their phones.', 'The man takes the red bag and they say goodbye.'],
        'ctx': [
            {'sent': 'She points at the door.', 'w': 'points', 'opts': ['shows with her finger', 'closes', 'paints'], 'ans': 0, 'why': 'Points at = shows with a finger.'},
            {'sent': 'It is a strange question.', 'w': 'strange', 'opts': ['not normal', 'very easy', 'very long'], 'ans': 0, 'why': 'Strange = unusual.'},
            {'sent': 'He never saw a purple cow.', 'w': 'never', 'opts': ['not one time', 'every day', 'sometimes'], 'ans': 0, 'why': 'Never = not at any time.'},
        ],
        'chunkHunt': ['Excuse me, is this your bag?', 'Mine is blue.', 'What color is your phone?', 'Nice colors!', 'I never saw…', 'Not my color.'],
        'think': 'What is your favorite color? What things do you have in that color?',
    },
    'convo': {
        'npc': {'name': 'Kai'},
        'story': 'You are at a station in Phoenix. Kai asks about bags and phones. Answer with mine and yours.',
        'turns': [
            {'npc': 'Excuse me, is this your bag?', 'pt': 'Com licença, esta é sua bolsa?', 'opts': [
                o('No, mine is blue. This one is red.', 'Não, a minha é azul. Esta é vermelha.', True, 'Mine replaces my bag.'),
                o('No, my is blue.', 'Não, meu é azul.', False, 'Use mine alone, or my + noun.'),
                o('No, I am blue.', 'Não, eu sou azul.', False, 'Wrong meaning.')]},
            {'npc': 'Is that your bag over there?', 'pt': 'Aquela ali é sua bolsa?', 'opts': [
                o('Yes, that is me.', 'Sim, aquela sou eu.', False, 'Say It’s mine, not that is me.'),
                o('Yes. They are blue.', 'Sim. Elas são azuis.', False, 'One bag = it is.'),
                o('Yes! That’s mine. Thank you!', 'Sim! É minha. Valeu!', True, 'That’s mine = natural.')]},
            {'npc': 'What color is your phone?', 'pt': 'Que cor é seu celular?', 'opts': [
                o('It’s black. And yours?', 'É preto. E o seu?', True, 'Answer and ask back.'),
                o('It has black.', 'Tem preto.', False, 'Use It’s black.'),
                o('My phone is color black me.', 'Meu celular é cor preto eu.', False, 'Not a correct sentence.')]},
            {'npc': 'Mine is white.', 'pt': 'O meu é branco.', 'opts': [
                o('Nice colors!', 'Que cores legais!', True, 'A friendly comment.'),
                o('Is good white.', 'É bom branco.', False, 'Say Nice! or I like it.'),
                o('No, mine.', 'Não, meu.', False, 'Out of context.')]},
            {'npc': 'Take care of your things!', 'pt': 'Cuide das suas coisas!', 'opts': [
                o('Thanks! You too!', 'Valeu! Você também!', True, 'Natural reply.'),
                o('Thanks! Your things too!', 'Valeu! Suas coisas também!', False, 'It sounds strange. Say You too!'),
                o('Yes, I am things.', 'Sim, eu sou coisas.', False, 'Wrong meaning.')]},
        ],
    },
    'errors': [
        {'wrong': 'The bag blue is mine.', 'fix': 'The blue bag is mine.', 'alt': 'The bag is blue mine.', 'why': 'In English the color goes before the noun.'},
        {'wrong': 'I have two bags blues.', 'fix': 'I have two blue bags.', 'alt': 'I have two blues bags.', 'why': 'Color words do not take -s and go before the noun.'},
        {'wrong': 'This bag is mine one.', 'fix': 'This bag is mine.', 'alt': 'This bag is my.', 'why': 'Mine stands alone.'},
        {'wrong': 'Is this your?', 'fix': 'Is this yours?', 'alt': 'Is this you?', 'why': 'Use yours when you do not say the noun.'},
        {'wrong': 'What color has your phone?', 'fix': 'What color is your phone?', 'alt': 'What color are your phone?', 'why': 'Use is for colors, not has.'},
    ],
    'homework': 'Look around your room and say the color of 10 things in English in a short audio for your teacher.',
    'homework_items': ['Name 10 things and their colors.', 'Write 3 sentences with mine and yours.', 'Listen to the dialogue again and shadow Kai.', 'Review: What color is it? / Mine is… / Nice colors!'],
}
