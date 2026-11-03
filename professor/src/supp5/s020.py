"""Suplemento Quest v5 · aula 20: Describing a person + regular What Does He Look Like? (Anne of Green Gables)."""
def o(en, pt, ok, fb):
    return {'en': en, 'pt': pt, 'ok': ok, 'fb': fb}

SUPP = {
    'reg': 18,
    'badge': {'icon': '🧑', 'name': 'People Describer', 'desc': 'Describe a person’s looks and personality in English'},
    'sticker': {'cat': 'Everyday culture', 'title': 'Describing People Politely', 'sub': 'What does she look like?'},
    'culture': {
        'hook': 'Describing people is useful when you look for a friend in a crowd or introduce your family. Learn to talk about looks and personality, and to stay polite.',
        'facts': [
            {'vis': 'prop:bag', 'big': 'Look like', 'label': 'Ask about appearance', 'sub': '“What does she look like?” asks about her looks.'},
            {'vis': 'prop:cup', 'big': 'Be like', 'label': 'Ask about personality', 'sub': '“What is she like?” asks about her character.'},
            {'vis': 'prop:coin', 'big': 'Be careful', 'label': 'Weight and age', 'sub': 'Comments about weight or age can sound rude to strangers.'},
            {'vis': 'prop:umbrella', 'big': 'Red hair', 'label': 'A famous character', 'sub': 'Anne of Green Gables has red hair and many freckles.'},
        ],
        'polite': 'Use friendly words like **tall**, **friendly** and **nice**. Do not comment on a stranger’s weight.',
        'mythfact': [
            {'s': '“What does she look like?” asks about personality.', 'ans': False, 'why': 'It asks about appearance. “What is she like?” asks about personality.'},
            {'s': 'It is usually impolite to comment on a stranger’s weight.', 'ans': True, 'why': 'Many people feel it is a private topic.'},
            {'s': '“Anne of Green Gables” was written by a Canadian author.', 'ans': True, 'why': 'L. M. Montgomery published it in 1908.'},
            {'s': 'Anne Shirley has red hair.', 'ans': True, 'why': 'Her red hair is a famous part of the character.'},
            {'s': '“She looks nice” can only be used for clothes.', 'ans': False, 'why': 'It can describe someone’s appearance or how friendly she seems.'},
        ],
        'wild': [
            {'kind': 'Airport pickup text', 'lines': ['I’m at the exit.', 'Look for a tall man with short hair and glasses.', 'I’m wearing a green jacket.'], 'decode': {'q': 'What is the man wearing?', 'opts': ['A green jacket', 'A red hat', 'A blue shirt'], 'ans': 0, 'why': '“I’m wearing a green jacket.”'}},
            {'kind': 'Lost and found sign', 'lines': ['**Looking for my sister, Ana**', 'She is tall, with long dark hair.', 'Last seen near the food court. Call 555-0170.'], 'decode': {'q': 'What color is Ana’s hair?', 'opts': ['Dark', 'Red', 'Blond'], 'ans': 0, 'why': '“Long dark hair.”'}},
        ],
        'compare': {
            'br': 'In Brazil people often make friendly comments about looks, like hair or style, and use affectionate nicknames.',
            'us': 'In the USA people also compliment hair or clothes, but they avoid comments about age, weight or skin with strangers.',
            'tip': 'Compliment what a person chooses, like clothes or style: “I like your jacket!”',
            'ask': 'Describe a person in your family. Say two words for looks and one for personality.',
        },
        'quiz': [
            {'q': 'You want to know how a person looks. You ask…', 'opts': ['What does she look like?', 'How is she?', 'What is she?'], 'ans': 0, 'why': 'Look like asks about appearance.'},
            {'q': 'Your sister has long dark hair. You say…', 'opts': ['She has long, dark hair.', 'She is long hair.', 'She have dark hairs.'], 'ans': 0, 'why': 'Use has for hair, and hair is not plural.'},
            {'q': 'To say she is not shy, you say…', 'opts': ['No, she’s very friendly.', 'No, she is not friendly.', 'No, she friendly.'], 'ans': 0, 'why': 'Use be + adjective.'},
        ],
    },
    'reading': {
        'genre': 'Blog post',
        'title': 'My sister Ana and a girl with red hair',
        'text': [
            'My name is Sofia, and I live in **Tampa**. Yesterday I was at a park with my sister, Ana. A man named Cole saw us. He asked, “Who is that woman?” “That’s my sister,” I said. “**Do you know him**?” Ana asked me. “Not yet,” I said, “but he looks nice.”',
            'Cole said, “She’s tall. Is she shy?” “No, she’s very friendly,” I said. “**What does she look like**?” he asked. “She has long, dark hair,” I said. “She’s tall, and she has brown eyes.” Cole smiled. “**That’s him**!” Ana said, when she saw her friend Tom with a big dog.',
            'I love to describe people. It reminds me of a book, “Anne of Green Gables.” L. M. Montgomery, a Canadian writer, wrote it in 1908. Anne is an orphan girl with red hair and a big imagination. She goes to live on a farm in Canada and talks a lot. Everyone remembers her red hair.',
            'Describing people is fun, but be careful. Say nice things like “She’s friendly” or “He’s tall.” Do not talk about weight or age with strangers. And if you do not know a person well, you can say, “**Not sure**.”',
            'In the end Cole met Ana, and they talked for an hour. “**I’m looking for** a friend with a big dog,” he said, and he laughed. “You’ll like her!” I said. It was a good day at the park.',
        ],
        'glossary': [{'w': 'woman', 'pt': 'mulher'}, {'w': 'tall', 'pt': 'alta'}, {'w': 'shy', 'pt': 'tímida'}, {'w': 'friendly', 'pt': 'simpática'}, {'w': 'hair', 'pt': 'cabelo'}, {'w': 'eyes', 'pt': 'olhos'}, {'w': 'orphan', 'pt': 'órfã'}, {'w': 'farm', 'pt': 'fazenda'}, {'w': 'careful', 'pt': 'cuidadoso'}, {'w': 'strangers', 'pt': 'estranhos'}],
        'fast': {'q': 'What is this text about?', 'opts': ['Describing people and a famous book', 'A cooking contest', 'Buying a phone'], 'ans': 0, 'why': 'Sofia describes Ana and talks about Anne of Green Gables.'},
        'scan': [
            {'q': 'What color are Ana’s eyes?', 'ans': 'brown', 'alt': ['Brown']},
            {'q': 'Where does Sofia live?', 'ans': 'Tampa', 'alt': ['tampa']},
            {'q': 'In which year was “Anne of Green Gables” published?', 'ans': '1908', 'alt': ['in 1908']},
        ],
        'tf': [
            {'s': 'Ana is shy.', 'ans': False, 'why': 'Sofia says, “No, she’s very friendly.”'},
            {'s': 'Ana has long, dark hair.', 'ans': True, 'why': '“She has long, dark hair.”'},
            {'s': 'Anne in the book has black hair.', 'ans': False, 'why': 'Anne has red hair.'},
            {'s': 'Cole meets Ana and they talk.', 'ans': True, 'why': 'They talked for an hour.'},
        ],
        'order': ['Cole sees Ana and asks who she is.', 'Sofia says Ana is her sister.', 'Sofia describes Ana’s hair and eyes.', 'Sofia thinks about Anne of Green Gables.', 'Cole meets Ana.'],
        'ctx': [
            {'sent': 'He is shy and does not talk much.', 'w': 'shy', 'opts': ['nervous with people', 'very loud', 'very funny'], 'ans': 0, 'why': 'Shy = not comfortable with other people.'},
            {'sent': 'Our neighbor is very friendly.', 'w': 'friendly', 'opts': ['nice to people', 'angry', 'sad'], 'ans': 0, 'why': 'Friendly = kind and open.'},
            {'sent': 'Be careful with the hot water.', 'w': 'careful', 'opts': ['pay attention', 'run fast', 'be funny'], 'ans': 0, 'why': 'Careful = paying attention to avoid problems.'},
        ],
        'chunkHunt': ['Do you know him?', 'I’m looking for…', 'That’s him!', 'Not sure.', 'What does she look like?'],
        'think': 'Describe a person you know: looks and personality. What is he or she like?',
    },
    'convo': {
        'npc': {'name': 'Cole'},
        'story': 'You are at a park in Tampa with your sister Ana. Cole asks about her.',
        'turns': [
            {'npc': 'Who is that woman?', 'pt': 'Quem é aquela mulher?', 'opts': [
                o('That’s my sister, Ana.', 'É minha irmã, Ana.', True, 'That’s + who she is.'),
                o('She is my sister, Ana she is.', 'Ela é minha irmã, Ana ela é.', False, 'Do not repeat she is.'),
                o('This woman is a park.', 'Esta mulher é um parque.', False, 'Wrong meaning.')]},
            {'npc': 'She’s tall. Is she shy?', 'pt': 'Ela é alta. Ela é tímida?', 'opts': [
                o('Yes, she is not friendly.', 'Sim, ela não é simpática.', False, 'It does not fit your answer.'),
                o('No, she’s very friendly.', 'Não, ela é muito simpática.', True, 'Be + adjective.'),
                o('No, she have friendly.', 'Não, ela tem simpática.', False, 'Use is, not have.')]},
            {'npc': 'What does she look like?', 'pt': 'Como ela é?', 'opts': [
                o('She is nice and funny.', 'Ela é legal e engraçada.', False, 'That is personality. The question is about looks.'),
                o('She has long, dark hair.', 'Ela tem cabelo longo e escuro.', True, 'Has + hair for looks.'),
                o('She looks like hair.', 'Ela parece cabelo.', False, 'Wrong meaning.')]},
            {'npc': 'She looks nice!', 'pt': 'Ela parece legal!', 'opts': [
                o('Come and meet her.', 'Venha conhecê-la.', True, 'A friendly invitation.'),
                o('Come and meets her.', 'Venha e conhece ela.', False, 'After and meet, use the base verb.'),
                o('Go and see her never.', 'Vá ver ela nunca.', False, 'Not natural.')]},
            {'npc': 'You’ll like her!', 'pt': 'Você vai gostar dela!', 'opts': [
                o('Yes, I like she.', 'Sim, eu gosto ela.', False, 'Use her after like.'),
                o('I am sure. See you later!', 'Tenho certeza. Até mais!', False, 'It sounds like you leave. Say Thanks!'),
                o('I’m sure I will. Thanks!', 'Tenho certeza que sim. Valeu!', True, 'Natural and polite.')]},
        ],
    },
    'errors': [
        {'wrong': 'She is long hair.', 'fix': 'She has long hair.', 'alt': 'She have long hair.', 'why': 'Use has for hair, not is.'},
        {'wrong': 'She has hairs dark.', 'fix': 'She has dark hair.', 'alt': 'She has dark hairs.', 'why': 'Hair is not plural, and the adjective goes first.'},
        {'wrong': 'He have brown eyes.', 'fix': 'He has brown eyes.', 'alt': 'He haves brown eyes.', 'why': 'He / she / it has.'},
        {'wrong': 'How is she?', 'fix': 'What does she look like?', 'alt': 'What is she looking?', 'why': 'How is she? asks about health. Look like asks about looks.'},
        {'wrong': 'My sister is very sympathetic.', 'fix': 'My sister is very friendly.', 'alt': 'My sister is very sympathy.', 'why': 'Simpática in Portuguese is friendly or nice in English.'},
    ],
    'homework': 'Describe a person in your family or a friend in English: looks first, then personality. Record a 45-second audio.',
    'homework_items': ['Describe 3 people: tall / short / hair / eyes.', 'Write 4 sentences: She has… She is…', 'Listen to the dialogue again and shadow Cole.', 'Review: What does she look like? / I’m looking for… / That’s him!'],
}
