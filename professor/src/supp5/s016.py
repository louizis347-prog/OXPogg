"""Suplemento Quest v5 · aula 16: My pet + regular Puppies and Kittens (Three Little Kittens)."""
def o(en, pt, ok, fb):
    return {'en': en, 'pt': pt, 'ok': ok, 'fb': fb}

SUPP = {
    'reg': 36,
    'badge': {'icon': '🐶', 'name': 'Pet Friend', 'desc': 'Talk about your pet and its age in English'},
    'sticker': {'cat': 'Everyday culture', 'title': 'Pets in the USA', 'sub': 'How old is he?'},
    'culture': {
        'hook': 'Many people in the USA treat their pets like family. Learn how to talk about a dog or a cat, and how to be polite when you meet someone’s pet.',
        'facts': [
            {'vis': 'prop:cup', 'big': 'Ask first', 'label': 'Before you pet a dog', 'sub': 'Say “Can I pet him?” and wait for the owner to say yes.'},
            {'vis': 'prop:coin', 'big': 'He / She', 'label': 'Pets have a gender word', 'sub': 'People say he or she for a pet with a name, not it.'},
            {'vis': 'prop:bag', 'big': 'Dog park', 'label': 'A place for dogs', 'sub': 'Many cities have parks where dogs can run and play.'},
            {'vis': 'prop:clock', 'big': 'Cat nap', 'label': 'A short sleep', 'sub': 'People use this phrase for a quick sleep, even for people.'},
        ],
        'polite': 'Say **Can I pet him?** before you touch a dog. Say **He’s adorable!** to give a compliment.',
        'mythfact': [
            {'s': 'It is polite to ask the owner before you pet a dog.', 'ans': True, 'why': 'Some dogs are nervous. Always ask first.'},
            {'s': 'In English you say “It has three years” for a pet’s age.', 'ans': False, 'why': 'Say “He is three years old.” English uses be for age.'},
            {'s': '“Cat nap” means a short sleep.', 'ans': True, 'why': 'It is a common phrase for a quick rest.'},
            {'s': '“Curiosity killed the cat” means cats are dangerous.', 'ans': False, 'why': 'It warns people that too much curiosity can bring trouble.'},
            {'s': '“Three Little Kittens” is a children’s poem about kittens that lose their mittens.', 'ans': True, 'why': 'Eliza Lee Follen wrote it, and it was published in 1843.'},
        ],
        'wild': [
            {'kind': 'Lost dog flyer', 'lines': ['**LOST DOG**', 'Name: Max · 3 years old', 'Brown, friendly, wears a red collar', 'Last seen near Main Park. Call 555-0198.'], 'decode': {'q': 'What color is Max’s collar?', 'opts': ['Red', 'Brown', 'Blue'], 'ans': 0, 'why': '“Wears a red collar.”'}},
            {'kind': 'Vet reminder text', 'lines': ['Hi! Luna has a checkup on Friday at 4 p.m.', 'Please bring her in a carrier.', 'Reply C to confirm.'], 'decode': {'q': 'When is the checkup?', 'opts': ['Friday at 4 p.m.', 'Monday at 4 a.m.', 'Friday at 9 a.m.'], 'ans': 0, 'why': '“On Friday at 4 p.m.”'}},
        ],
        'compare': {
            'br': 'In Brazil people say “Ele tem três anos”, and “vira-lata” is a popular word for a mixed-breed dog.',
            'us': 'In the USA you say “He is three years old.” People also say “mixed breed” or “mutt” for a mixed dog.',
            'tip': 'For age, always use am / is / are + number + years old.',
            'ask': 'Do you have a pet? Say its name and age in English.',
        },
        'quiz': [
            {'q': 'Your friend has a dog. You want to touch it. You say…', 'opts': ['Can I pet him?', 'I touch him?', 'Give me the dog.'], 'ans': 0, 'why': 'Can I pet him? is polite.'},
            {'q': 'How do you say the age of your cat?', 'opts': ['She is two years old.', 'She has two years.', 'She is two year.'], 'ans': 0, 'why': 'Use is + number + years old.'},
            {'q': '“Cat nap” means…', 'opts': ['A short sleep', 'A cat’s dinner', 'A night walk'], 'ans': 0, 'why': 'A cat nap is a short sleep.'},
        ],
    },
    'reading': {
        'genre': 'Blog post',
        'title': 'My dog Max and a kitten called Luna',
        'text': [
            'My name is Diego, and I live in **San Antonio**. I have a dog. His name is Max. He is three years old, and he is brown and white. “**So adorable**!” people say when they see him.',
            'Last Saturday we went to the park. A woman said, “Look! What a cute dog!” “Thanks,” I said. “His name is Max.” She asked, “**How old is he?**” “He’s three years old,” I answered. “Does he like people?” she asked. “Yes, he loves people,” I said.',
            'The woman has a cat called Luna. “**Aww**!” I said when I saw her photo. Luna is small and gray, and she sleeps all day. A **cat nap** is perfect for her! My grandmother says, “**Curiosity killed the cat**,” because Luna opens every box.',
            'In school, I learned a poem called “Three Little Kittens.” An American writer, Eliza Lee Follen, wrote it in 1843. Three kittens lose their mittens, and their mother is not happy. The kittens find the mittens in the end, and everybody is happy again.',
            'Now Max and Luna are friends. They run in the park, and then they sleep. I love my little pet family.',
        ],
        'glossary': [{'w': 'cute', 'pt': 'fofo'}, {'w': 'adorable', 'pt': 'adorável'}, {'w': 'photo', 'pt': 'foto'}, {'w': 'gray', 'pt': 'cinza'}, {'w': 'sleeps', 'pt': 'dorme'}, {'w': 'box', 'pt': 'caixa'}, {'w': 'poem', 'pt': 'poema'}, {'w': 'mittens', 'pt': 'luvas'}, {'w': 'curiosity', 'pt': 'curiosidade'}],
        'fast': {'q': 'What is this text about?', 'opts': ['A dog, a cat and two friends', 'A school test', 'A trip to the beach'], 'ans': 0, 'why': 'Diego talks about Max, Luna and the park.'},
        'scan': [
            {'q': 'How old is Max?', 'ans': 'three', 'alt': ['3', 'three years old', '3 years old']},
            {'q': 'What is the cat’s name?', 'ans': 'Luna', 'alt': ['luna']},
            {'q': 'In which year did Eliza Lee Follen write the poem?', 'ans': '1843', 'alt': ['in 1843']},
        ],
        'tf': [
            {'s': 'Diego lives in San Antonio.', 'ans': True, 'why': '“I live in San Antonio.”'},
            {'s': 'Max is five years old.', 'ans': False, 'why': 'Max is three years old.'},
            {'s': 'Max loves people.', 'ans': True, 'why': '“Yes, he loves people.”'},
            {'s': 'Luna is a big black cat.', 'ans': False, 'why': 'Luna is small and gray.'},
        ],
        'order': ['Diego goes to the park with Max.', 'A woman says Max is cute.', 'Diego says Max is three years old.', 'He sees a photo of Luna.', 'Max and Luna become friends.'],
        'ctx': [
            {'sent': 'What a cute puppy!', 'w': 'cute', 'opts': ['nice and sweet to look at', 'very loud', 'very old'], 'ans': 0, 'why': 'Cute = sweet and attractive.'},
            {'sent': 'My cat sleeps all day.', 'w': 'sleeps', 'opts': ['rests with eyes closed', 'runs fast', 'eats a lot'], 'ans': 0, 'why': 'Sleeps = is in bed or resting.'},
            {'sent': 'She opens every box because of her curiosity.', 'w': 'curiosity', 'opts': ['wish to know things', 'fear of boxes', 'hunger'], 'ans': 0, 'why': 'Curiosity = wanting to know more.'},
        ],
        'chunkHunt': ['So adorable!', 'How old is he?', 'Aww!', 'Cat nap', 'Curiosity killed the cat.'],
        'think': 'Which pet would you like to have? Why?',
    },
    'convo': {
        'npc': {'name': 'Claire'},
        'story': 'You are at a park in San Antonio with your dog Max. Claire wants to talk about pets.',
        'turns': [
            {'npc': 'Look! What a cute dog!', 'pt': 'Olha! Que cachorro fofo!', 'opts': [
                o('Thanks! His name is Max.', 'Valeu! O nome dele é Max.', True, 'Thank her and give the name.'),
                o('Thanks! It name is Max.', 'Valeu! Seu nome é Max.', False, 'For a pet use his or her, not it.'),
                o('Yes, I am a dog.', 'Sim, eu sou um cachorro.', False, 'Wrong meaning.')]},
            {'npc': 'How old is he?', 'pt': 'Quantos anos ele tem?', 'opts': [
                o('He has three years.', 'Ele tem três anos.', False, 'English uses is: He is three years old.'),
                o('Three old.', 'Três velho.', False, 'Say He’s three years old.'),
                o('He’s three years old.', 'Ele tem três anos.', True, 'Be + number + years old.')]},
            {'npc': 'Does he like people?', 'pt': 'Ele gosta de gente?', 'opts': [
                o('Yes, he loves people. Do you have a pet?', 'Sim, ele adora gente. Você tem um bichinho?', True, 'Answer and ask back.'),
                o('Yes, he like people.', 'Sim, ele gosta gente.', False, 'He loves / likes: add -s.'),
                o('No, he is people.', 'Não, ele é gente.', False, 'Wrong meaning.')]},
            {'npc': 'I have a cat. Her name is Luna.', 'pt': 'Tenho uma gata. O nome dela é Luna.', 'opts': [
                o('Aww! Can I pet her?', 'Aww! Posso fazer carinho nela?', False, 'Luna is not here. Say Nice!'),
                o('Nice! Max loves cats too.', 'Legal! O Max também adora gatos.', True, 'Natural reaction.'),
                o('Nice! It is Luna cat.', 'Legal! É Luna gata.', False, 'Word order is wrong.')]},
            {'npc': 'Bring Luna to the park!', 'pt': 'Traga a Luna ao parque!', 'opts': [
                o('Okay! She loves the park.', 'Ok! Ela adora o parque.', False, 'You do not know yet. Say Good idea!'),
                o('I bring her yesterday.', 'Eu trago ela ontem.', False, 'Wrong tense.'),
                o('Good idea! Let’s do it on Saturday.', 'Boa ideia! Vamos fazer isso no sábado.', True, 'Accepts the plan.')]},
        ],
    },
    'errors': [
        {'wrong': 'He has three years.', 'fix': 'He is three years old.', 'alt': 'He is three years.', 'why': 'English uses be for age.'},
        {'wrong': 'It name is Max.', 'fix': 'His name is Max.', 'alt': 'He name is Max.', 'why': 'Use his or her for a pet’s name.'},
        {'wrong': 'My dog like people.', 'fix': 'My dog likes people.', 'alt': 'My dog liking people.', 'why': 'He / she / it takes -s: likes.'},
        {'wrong': 'I have a cat black.', 'fix': 'I have a black cat.', 'alt': 'I have a cat blacks.', 'why': 'The color goes before the noun.'},
        {'wrong': 'Can I to pet him?', 'fix': 'Can I pet him?', 'alt': 'Can I petting him?', 'why': 'After Can I use the base verb.'},
    ],
    'homework': 'Describe a pet (yours or a friend’s) in English: name, age and color. Record a 45-second audio.',
    'homework_items': ['Say the name and age of 3 pets you know.', 'Write 4 sentences about a pet.', 'Listen to the dialogue again and shadow Claire.', 'Review: How old is he? / So adorable! / Aww!'],
}
