# Conteúdos extras dos 5 primeiros episódios: expressões e gírias, cena com as expressões,
# laboratório de sons e caça-sons. Usado por model_v2.py (mesma ordem de model_v2_data.V2).


def hunt_w(say, opts, a, why):
    return dict(fig='🎧', say=say, ask='Ouça e toque na palavra.', opts=opts, a=a, why=why)


def hunt_p(say, opts, a, pt):
    return dict(fig='🎧', say=say, ask='Ouça e toque na figura.', opts=[[e, ''] for e, _ in opts], a=a,
                why='**%s** = %s.' % (say, pt), pic=1)


def rnd(say, opts, a, why):
    return dict(fig='🎧', say=say, ask='Qual palavra você ouviu?', opts=opts, a=a, why=why)


EXTRA = [
    # ---- 1 · I'm · Paddington ----
    dict(
        exp=[
            dict(ic='🙂', en="How's it going?", tag='Expressão', pt='E aí, tudo bem?', use='Cumprimento **informal**. Os americanos não esperam uma resposta longa.',
                 ex=["How's it going? Not bad!", 'E aí, tudo bem? Nada mal!']),
            dict(ic='👍', en='Not bad.', tag='Expressão', pt='Nada mal.', use='Resposta simpática para "tudo bem?". Quer dizer "estou bem", sem exagerar.',
                 ex=["Not bad, thanks. I'm tired.", 'Nada mal, obrigado. Estou cansado.']),
            dict(ic='🤤', en="I'm starving!", tag='Gíria', pt='Estou morrendo de fome!', use='Exagero divertido para **muita fome**. Não é de verdade "passar fome".',
                 ex=["I'm starving! Let's eat.", 'Estou morrendo de fome! Vamos comer.']),
            dict(ic='🥱', en="I'm beat.", tag='Gíria', pt='Estou exausto.', use='Jeito informal de dizer que você está **muito cansado**.',
                 ex=["I'm beat. It was a long trip.", 'Estou exausto. Foi uma viagem longa.'])],
        exp_scene=dict(rs='kitchen', lines=[
            ['Mrs. Brown', "Good morning! **How's it going**?", 'Bom dia! E aí, tudo bem?'],
            ['Paddington', "**Not bad**, thanks. But I'm **starving**!", 'Nada mal, obrigado. Mas estou morrendo de fome!'],
            ['Mrs. Brown', 'Breakfast is ready. Tea and toast!', 'O café da manhã está pronto. Chá e torradas!'],
            ['Paddington', "Great! I'm so happy.", 'Ótimo! Estou muito feliz.'],
            ['Mrs. Brown', 'Are you tired? You look sleepy.', 'Você está cansado? Parece com sono.'],
            ['Paddington', "Yes, I'm **beat**. It was a long trip.", 'Sim, estou exausto. Foi uma viagem longa.'],
            ['Mrs. Brown', 'Eat first, then rest.', 'Coma primeiro, depois descanse.'],
            ['Paddington', 'Thank you, Mrs. Brown!', 'Obrigado, Sra. Brown!']]),
        lab=dict(
            short='“h” de Hi', title='Laboratório de sons: o “h” de Hi',
            say='Vamos treinar o sopro do “h”? É só fingir que você está embaçando um vidro!',
            intro={'what': 'O **h** no começo de palavras como **hi** e **hat** é um som de verdade em inglês: um sopro de ar. Se você o esquece, **hi** vira **eye** e **hat** vira **at**.',
                   'how': 'Abra a boca na posição da vogal que vem depois e solte o ar da garganta, sem apertar, como se embaçasse um espelho. É um sopro curto e suave, sem vibrar a garganta.',
                   'pt': 'Em português o “h” é mudo (hotel, hora), então o erro mais comum é omitir o som. O mais parecido é o “r” inicial de “rato” em muitos sotaques brasileiros, mas em inglês o sopro é bem mais leve.'},
            ex=[['hungry', 'RÂN-gri', 'com fome', 'o sopro vem antes do “â”'], ['happy', 'RÉ-pi', 'feliz', 'sopre antes do “é”'], ['home', 'RÔUM', 'casa', 'sopro leve e depois “ôum”']],
            pairs=[['hi', 'eye', 'com “h” há um sopro antes; sem ele só se ouve o “ai”'], ['hat', 'at', 'o sopro separa “chapéu” de “em/às”'], ['hear', 'ear', 'sopre no começo para “ouvir”; sem sopro é “orelha”']],
            tip='Coloque a mão na frente da boca e diga “hi”: você deve sentir um sopro quente de ar. Em “eye” não deve sentir nada.',
            phrase=["I'm hungry. I'm happy.", 'Estou com fome. Estou feliz.'],
            rounds=[rnd('hi', ['hi', 'eye'], 0, 'Você ouviu um sopro antes do “ai”: é **hi**. Sem o sopro seria **eye** (olho).'),
                    rnd('hat', ['hat', 'at'], 0, 'O sopro no início mostra que é **hat** (chapéu). **At** começa direto na vogal.'),
                    rnd('hear', ['ear', 'hear'], 1, 'Em **hear** o ar sai antes do “i”. **Ear** (orelha) começa sem sopro.')]),
        hunt=[hunt_w('hold', ['old', 'hold'], 1, '**hold** começa com um sopro de ar, “hhh”; **old** começa direto na vogal.'),
              hunt_w('hit', ['it', 'hit'], 1, '**hit** (bater) começa com sopro; **it** começa direto na vogal.'),
              hunt_p('horse', [('🐴', 'horse'), ('🏠', 'house'), ('❤️', 'heart')], 0, 'cavalo'),
              hunt_w('ill', ['ill', 'hill'], 0, '**ill** (doente) começa direto no “i”; **hill** (morro) começa com sopro.'),
              hunt_p('hand', [('✋', 'hand'), ('🐟', 'fish'), ('🌳', 'tree')], 0, 'mão')]),
    # ---- 2 · Are you…? · Alice ----
    dict(
        exp=[
            dict(ic='🤨', en='Are you kidding?', tag='Informal', pt='Você está brincando?', use='Quando algo parece **bom demais ou absurdo** para ser verdade.',
                 ex=["Are you kidding? That's my hat!", 'Está brincando? Esse é o meu chapéu!']),
            dict(ic='🫶', en='Are you okay?', tag='Expressão', pt='Você está bem?', use='Pergunta com **cuidado**, quando alguém parece mal ou assustado.',
                 ex=["Are you okay? You look lost.", 'Você está bem? Parece perdida.']),
            dict(ic='⏰', en="I'm running late.", tag='Expressão', pt='Estou atrasado.', use='Jeito natural de avisar que você vai **chegar tarde**.',
                 ex=["Sorry, I'm running late!", 'Desculpe, estou atrasado!']),
            dict(ic='🏃', en='Hurry up!', tag='Informal', pt='Anda logo! / Depressa!', use='Para **apressar** alguém. Soa um pouco mandão, use com amigos.',
                 ex=['Hurry up, Alice!', 'Depressa, Alice!'])],
        exp_scene=dict(rs='cafe3', lines=[
            ['Rabbit', "Oh dear! **I'm running late**!", 'Meu Deus! Estou atrasado!'],
            ['Alice', '**Are you okay**?', 'Você está bem?'],
            ['Rabbit', "I'm fine! But **hurry up**, Alice!", 'Estou bem! Mas anda logo, Alice!'],
            ['Alice', '**Are you kidding**? Where are we going?', 'Está brincando? Para onde vamos?'],
            ['Cat', 'To the tea party! Are you ready?', 'Para a festa do chá! Você está pronta?'],
            ['Alice', "No, I'm not ready!", 'Não, não estou pronta!']]),
        lab=dict(
            short='r inicial', title='Laboratório de sons: o “r” de rabbit',
            say='O “r” inglês é bem diferente do nosso! Vamos treinar com o Coelho Branco.',
            intro={'what': 'O **r** inglês, em **rabbit**, **right** e **road**, é um som suave e “redondo”: a língua não encosta em nenhum lugar da boca.',
                   'how': 'Arredonde os lábios como para assobiar, levante a ponta da língua sem encostar no céu da boca e puxe a língua um pouco para trás. Não vibre a língua.',
                   'pt': 'Em português o r inicial é forte (rato, rua) e sai da garganta ou vibra. Em inglês ele é macio. Cuidado para não trocar por **l**: **right** (certo) ≠ **light** (luz).'},
            ex=[['rabbit', 'RÉ-bit', 'coelho', 'lábios arredondados já no começo'], ['right', 'RÁIT', 'certo', 'língua solta, sem encostar'], ['road', 'RÔUD', 'estrada', 'comece com o “r” redondo']],
            pairs=[['right', 'light', 'r: língua solta · l: a ponta da língua toca atrás dos dentes de cima'], ['road', 'load', '“estrada” × “carga”'], ['rock', 'lock', '“pedra” × “trancar”']],
            tip='Diga “ru” assobiando: os lábios redondos ajudam o r certo. No “l” a ponta da língua encosta; no “r”, não.',
            phrase=['Are you in a hurry, rabbit?', 'Você está com pressa, coelho?'],
            rounds=[rnd('right', ['right', 'light'], 0, 'Em **right** a língua não encosta. **Light** (luz) começa tocando atrás dos dentes.'),
                    rnd('lock', ['rock', 'lock'], 1, '**Lock** (trancar) começa com “l”, a língua toca. **Rock** (pedra) começa com “r” redondo.'),
                    rnd('load', ['road', 'load'], 1, '**Load** (carga) começa com “l”. **Road** (estrada) começa com “r”.')]),
        hunt=[hunt_w('light', ['right', 'light'], 1, '**light** (luz) começa com “l”: a língua encosta.'),
              hunt_p('rabbit', [('🐇', 'rabbit'), ('🔒', 'lock'), ('🛣️', 'road')], 0, 'coelho'),
              hunt_w('road', ['road', 'load'], 0, '**road** (estrada) começa com “r” redondo.'),
              hunt_w('rock', ['rock', 'lock'], 0, '**rock** (pedra) começa com “r”, sem encostar a língua.'),
              hunt_p('lock', [('🛣️', 'road'), ('🔒', 'lock'), ('🐇', 'rabbit')], 1, 'trancar / cadeado')]),
    # ---- 3 · He's / She's · Oz ----
    dict(
        exp=[
            dict(ic='😎', en="He's cool.", tag='Gíria', pt='Ele é legal.', use='**Cool** é o jeito mais comum de dizer **legal, bacana**.',
                 ex=["He's cool. He's my friend.", 'Ele é legal. É meu amigo.']),
            dict(ic='🤩', en="She's awesome!", tag='Gíria', pt='Ela é incrível!', use='**Awesome** = incrível, demais. Muito usada para elogiar.',
                 ex=["She's awesome! She's Glinda.", 'Ela é incrível! É a Glinda.']),
            dict(ic='🤪', en="He's nuts.", tag='Gíria', pt='Ele é maluco.', use='Informal e brincalhão: alguém **doido, fora do comum** (nem sempre ofensivo).',
                 ex=["He's nuts, but he's kind.", 'Ele é maluco, mas é gentil.']),
            dict(ic='🏆', en="He's the best!", tag='Expressão', pt='Ele é o melhor!', use='Elogio forte. Troque **he** por **she** para falar de uma mulher.',
                 ex=["She's the best!", 'Ela é a melhor!'])],
        exp_scene=dict(rs='cafe2', lines=[
            ['Scarecrow', "Dorothy, who's that woman?", 'Dorothy, quem é aquela mulher?'],
            ['Dorothy', "She's Glinda. She's **awesome**!", 'Ela é a Glinda. Ela é incrível!'],
            ['Scarecrow', 'And that man?', 'E aquele homem?'],
            ['Dorothy', "He's the Tin Man. He's **cool**!", 'Ele é o Homem de Lata. Ele é legal!'],
            ['Scarecrow', 'And the Lion?', 'E o Leão?'],
            ['Dorothy', "He's **nuts**, but he's kind.", 'Ele é maluco, mas é gentil.'],
            ['Scarecrow', 'And your dog, Toto?', 'E o seu cachorro, o Toto?'],
            ['Dorothy', "He's **the best**!", 'Ele é o melhor!']]),
        lab=dict(
            short='sh de she', title='Laboratório de sons: o “sh” de she',
            say='Shhh! Vamos treinar o chiado do “she”?',
            intro={'what': 'O **sh** de **she** é um chiado suave e contínuo, como quando pedimos silêncio: shhh. Aparece em **she**, **ship** e **shy**.',
                   'how': 'Aproxime os lábios, arredondando um pouco, deixe a língua larga e perto do céu da boca, sem tocar, e solte o ar de forma contínua. Não é “s” e não é “tch”.',
                   'pt': 'Em português o “ch” de chá é parecido, então é um som fácil. O erro comum é dizer **see** (s) no lugar de **she**, ou **chee** (tch).'},
            ex=[['she', 'XI', 'ela', 'chiado prolongado e termina no “i”'], ['ship', 'XIP', 'navio', 'chiado e “i” curto'], ['shy', 'XAI', 'tímido', 'chiado e depois “ai”']],
            pairs=[['she', 'see', 'sh = ela · s = ver'], ['ship', 'sip', '“navio” × “gole”'], ['shy', 'sky', '“tímido” × “céu”']],
            tip='Peça silêncio: “shhh”. Prolongue o chiado e termine no “i”: shhh-i = she.',
            phrase=["She's Glinda. She's awesome!", 'Ela é a Glinda. Ela é incrível!'],
            rounds=[rnd('she', ['she', 'see'], 0, 'Chiado = **she** (ela). **See** (ver) começa com “s”.'),
                    rnd('ship', ['sip', 'ship'], 1, '**Ship** (navio) começa com chiado. **Sip** (gole) começa com “s”.'),
                    rnd('shy', ['sky', 'shy'], 1, '**Shy** (tímido) começa com chiado. **Sky** (céu) começa com “sk”.')]),
        hunt=[hunt_w('she', ['see', 'she'], 1, '**she** começa com chiado “sh”.'),
              hunt_p('ship', [('🚢', 'ship'), ('🌤️', 'sky'), ('🥤', 'sip')], 0, 'navio'),
              hunt_w('shy', ['sky', 'shy'], 1, '**shy** (tímido) tem chiado no começo.'),
              hunt_w('sip', ['ship', 'sip'], 1, '**sip** (gole) começa com “s” simples, sem chiado.'),
              hunt_p('shoe', [('👟', 'shoe'), ('🌤️', 'sky'), ('🥤', 'sip')], 0, 'sapato')]),
    # ---- 4 · Is he/she/it · Peter Pan ----
    dict(
        exp=[
            dict(ic='🤔', en='Is he for real?', tag='Gíria', pt='Ele está falando sério? / Ele é de verdade?', use='**For real** = de verdade, a sério. Mostra surpresa ou dúvida.',
                 ex=['Is he for real? He is a pirate!', 'Ele é de verdade? Ele é um pirata!']),
            dict(ic='🙅', en='No way!', tag='Gíria', pt='De jeito nenhum! / Não acredito!', use='Serve para **recusar** ou mostrar **espanto**, dependendo do tom.',
                 ex=["No way! It isn't true.", 'De jeito nenhum! Não é verdade.']),
            dict(ic='🍰', en="It's a piece of cake.", tag='Expressão', pt='É moleza. / É fácil.', use='Expressão para algo **muito fácil**. Não tem nada a ver com bolo de verdade.',
                 ex=["It's a piece of cake!", 'É moleza!']),
            dict(ic='🤷', en='Is it a big deal?', tag='Informal', pt='É algo grave? / É grande coisa?', use='Pergunta se **algo é importante ou sério**. Resposta comum: **It\'s no big deal.**',
                 ex=["Is it a big deal? No, it isn't.", 'É grande coisa? Não, não é.'])],
        exp_scene=dict(rs='bedroom', lines=[
            ['Wendy', "Peter, is Captain Hook's ship far?", 'Peter, o navio do Capitão Gancho fica longe?'],
            ['Peter', "No, it isn't. It's **a piece of cake**!", 'Não, não fica. É moleza!'],
            ['Wendy', '**Is he for real**? He is a pirate!', 'Ele é de verdade? Ele é um pirata!'],
            ['Peter', "Yes, he is. But **no way** he can catch me!", 'Sim, é. Mas de jeito nenhum ele me pega!'],
            ['Wendy', '**Is it a big deal**? Are you scared?', 'É grande coisa? Você está com medo?'],
            ['Peter', "No way! I'm Peter Pan!", 'Nunca! Eu sou o Peter Pan!']]),
        lab=dict(
            short='i curto × i longo', title='Laboratório de sons: i curto × i longo',
            say='É ship ou sheep? Vamos treinar os dois sons de “i” do inglês!',
            intro={'what': 'O inglês tem dois sons de “i”: o **curto** (**it**, **is**, **ship**) e o **longo** (**eat**, **ease**, **sheep**). Trocar um pelo outro muda a palavra.',
                   'how': 'No curto, a boca fica relaxada e o som é rápido. No longo, estique os lábios num sorriso e segure o som: “iii”.',
                   'pt': 'Em português só temos um “i”, então o curto costuma virar longo: **ship** sai **sheep**. Treine a diferença com os pares abaixo.'},
            ex=[['it', 'IT', 'isso', 'curto e relaxado'], ['is', 'IZ', 'é / está', 'curto, termina em “z”'], ['eat', 'IIT', 'comer', 'sorriso e som longo']],
            pairs=[['ship', 'sheep', 'curto: navio · longo: ovelha'], ['it', 'eat', 'curto: isso · longo: comer'], ['live', 'leave', 'curto: morar · longo: partir']],
            tip='Sorria para o “i” longo e relaxe a boca para o curto.',
            phrase=["Is it a ship? No, it isn't.", 'É um navio? Não, não é.'],
            rounds=[rnd('sheep', ['ship', 'sheep'], 1, 'Som longo: **sheep** (ovelha). **Ship** (navio) é curto.'),
                    rnd('it', ['it', 'eat'], 0, 'Som curto: **it** (isso). **Eat** (comer) é longo.'),
                    rnd('leave', ['live', 'leave'], 1, 'Som longo: **leave** (partir). **Live** (morar) é curto.')]),
        hunt=[hunt_w('ship', ['ship', 'sheep'], 0, '**ship** (navio) tem o “i” curto.'),
              hunt_p('sheep', [('🐑', 'sheep'), ('🚢', 'ship'), ('🐟', 'fish')], 0, 'ovelha'),
              hunt_w('eat', ['it', 'eat'], 1, '**eat** (comer) tem o “i” longo.'),
              hunt_p('ship', [('🚢', 'ship'), ('🐑', 'sheep'), ('🍽️', 'eat')], 0, 'navio'),
              hunt_w('live', ['live', 'leave'], 0, '**live** (morar) tem o “i” curto.')]),
    # ---- 5 · Plural · Toy Story ----
    dict(
        exp=[
            dict(ic='👋', en='Hey, guys!', tag='Gíria', pt='E aí, pessoal!', use='**Guys** é plural informal para chamar um grupo, de homens, mulheres ou misto.',
                 ex=['Hey, guys! Come here!', 'E aí, pessoal! Venham aqui!']),
            dict(ic='🧸', en='Tons of toys!', tag='Gíria', pt='Um monte de brinquedos!', use='**Tons of** = muitos, um monte de. Usa-se com plural.',
                 ex=['I see tons of toys.', 'Vejo um monte de brinquedos.']),
            dict(ic='👍', en='Two thumbs up!', tag='Expressão', pt='Aprovado! / Gostei muito!', use='Elogio forte: **dois polegares para cima**.',
                 ex=['Two thumbs up for this party!', 'Aprovado! Esta festa é ótima!']),
            dict(ic='🚀', en='To infinity and beyond!', tag='Expressão', pt='Ao infinito e além!', use='A frase famosa do **Buzz Lightyear**. Muita gente usa de brincadeira.',
                 ex=['Ready? To infinity and beyond!', 'Pronto? Ao infinito e além!'])],
        exp_scene=dict(rs='yard', lines=[
            ['Woody', "**Hey, guys**! It's Andy's party!", 'E aí, pessoal! É a festa do Andy!'],
            ['Buzz', 'Wow! **Tons of toys** are here, Woody!', 'Uau! Um monte de brinquedos está aqui, Woody!'],
            ['Woody', '**Two thumbs up** for this party!', 'Aprovado! Que festa ótima!'],
            ['Buzz', 'I see balloons and puppies everywhere.', 'Vejo balões e cachorrinhos por todo lado.'],
            ['Woody', 'Great! Are you ready, Buzz?', 'Ótimo! Você está pronto, Buzz?'],
            ['Buzz', '**To infinity and beyond**!', 'Ao infinito e além!']]),
        lab=dict(
            short='-s do plural', title='Laboratório de sons: o -s do plural',
            say='O -s do plural tem três sons diferentes. Vamos descobrir quais!',
            intro={'what': 'O **-s** do plural tem três sons: **/s/** depois de sons duros (**cats**), **/z/** depois de vogais e sons suaves (**toys**, **balloons**, **puppies**) e **/iz/** depois de s, sh, ch, x (**boxes**).',
                   'how': 'Ponha a mão na garganta: no **z** ela vibra (toyz), no **s** não vibra (cats). No **/iz/** aparece uma sílaba a mais: box-iz.',
                   'pt': 'Em português o plural é sempre “s” (gatos, brinquedos). Em inglês a maioria soa como **z**: **toys** = “tóiz”, não “tóis”.'},
            ex=[['cats', 'KÉTS', 'gatos', '/s/: sem vibrar a garganta'], ['toys', 'TÓIZ', 'brinquedos', '/z/: a garganta vibra'], ['boxes', 'BÓK-siz', 'caixas', '/iz/: uma sílaba a mais']],
            pairs=[['cat', 'cats', 'um gato × vários: termina em /s/'], ['toy', 'toys', 'termina em /z/: “tóiz”'], ['box', 'boxes', 'ganha a sílaba extra “-iz”']],
            tip='Com a mão na garganta, diga “toyz”: ela vibra. Em “cats” não vibra.',
            phrase=['I see two toys and three balloons.', 'Vejo dois brinquedos e três balões.'],
            rounds=[rnd('toys', ['toy', 'toys'], 1, 'Termina em /z/: **toys** (brinquedos).'),
                    rnd('boxes', ['box', 'boxes'], 1, 'Tem a sílaba extra “-iz”: **boxes** (caixas).'),
                    rnd('cats', ['cat', 'cats'], 1, 'Termina em /s/: **cats** (gatos).')]),
        hunt=[hunt_w('toys', ['toy', 'toys'], 1, '**toys** termina com o som /z/.'),
              hunt_p('boxes', [('📦', 'boxes'), ('🧸', 'toy'), ('🐱', 'cat')], 0, 'caixas'),
              hunt_w('cats', ['cat', 'cats'], 1, '**cats** termina com o som /s/.'),
              hunt_p('puppies', [('🐶', 'puppies'), ('🐱', 'cats'), ('📦', 'boxes')], 0, 'cachorrinhos'),
              hunt_w('balloons', ['balloon', 'balloons'], 1, '**balloons** termina com o som /z/.')]),
]


def verb(v, ic, pt, eu, eu_pt, he, note_extra=''):
    """he: frase com a terminação em **negrito** (ex.: 'He eat**s** a sandwich.')."""
    import re
    m = re.search(r'(\w+)\*\*(\w+)\*\*', he)
    form = (m.group(1) + m.group(2)) if m else v
    return dict(v=v, ic=ic, pt=pt, f=[['eu', eu], ['ele/ela', he]], ex=[eu, eu_pt],
                note='**%s** = %s. Com he/she: **%s**.%s' % (v, pt, form, note_extra))


VERBS = [
    dict(title='Verbos para viver como o Paddington', tip='Quatro verbos: eat, drink, sleep e love.', items=[
        verb('eat', '🥪', 'comer', 'I eat marmalade sandwiches.', 'Eu como sanduíches de geleia de laranja.', 'He eat**s** a sandwich.'),
        verb('drink', '🫖', 'beber', 'I drink tea every day.', 'Eu bebo chá todo dia.', 'She drink**s** tea.'),
        verb('sleep', '😴', 'dormir', 'I sleep in a small bed.', 'Eu durmo numa cama pequena.', 'He sleep**s** a lot.'),
        verb('love', '❤️', 'amar, adorar', 'I love my new home.', 'Eu adoro minha casa nova.', 'She love**s** Paddington.')]),
    dict(title='Verbos para seguir o Coelho', tip='Quatro verbos: run, ask, follow e fall.', items=[
        verb('run', '🏃', 'correr', 'I run to the tea party.', 'Eu corro para a festa do chá.', 'The Rabbit run**s** fast.'),
        verb('ask', '❓', 'perguntar', 'I ask a question.', 'Eu faço uma pergunta.', 'Alice ask**s** many questions.'),
        verb('follow', '👣', 'seguir', 'I follow the White Rabbit.', 'Eu sigo o Coelho Branco.', 'She follow**s** the rabbit.'),
        verb('fall', '⬇️', 'cair', 'I fall down the hole.', 'Eu caio na toca.', 'Alice fall**s** slowly.')]),
    dict(title='Verbos para a estrada de tijolos amarelos', tip='Quatro verbos: walk, help, sing e need.', items=[
        verb('walk', '🚶', 'andar, caminhar', 'I walk on the yellow road.', 'Eu ando pela estrada amarela.', 'Dorothy walk**s** with her friends.'),
        verb('help', '🤝', 'ajudar', 'I help my friends.', 'Eu ajudo meus amigos.', 'He help**s** Dorothy.'),
        verb('sing', '🎵', 'cantar', 'I sing a song.', 'Eu canto uma música.', 'She sing**s** very well.'),
        verb('need', '🙏', 'precisar', 'I need a friend.', 'Eu preciso de um amigo.', 'The Scarecrow need**s** a brain.')]),
    dict(title='Verbos para a Terra do Nunca', tip='Quatro verbos: fly, play, live e find.', items=[
        verb('fly', '🕊️', 'voar', 'I fly over the sea.', 'Eu voo sobre o mar.', 'Peter fl**ies** every night.'),
        verb('play', '🎮', 'brincar, jogar', 'I play with the fairy.', 'Eu brinco com a fada.', 'He play**s** all day.'),
        verb('live', '🏝️', 'morar', 'I live in Neverland.', 'Eu moro na Terra do Nunca.', 'Peter live**s** in Neverland.'),
        verb('find', '🔍', 'achar, encontrar', 'I find the ship.', 'Eu encontro o navio.', 'She find**s** a star.')]),
    dict(title='Verbos para a festa do Andy', tip='Quatro verbos: play, watch, carry e tell.', items=[
        verb('play', '🎮', 'brincar, jogar', 'I play with my friends.', 'Eu brinco com meus amigos.', 'Woody play**s** with Andy.'),
        verb('watch', '👀', 'assistir, observar', 'I watch the party.', 'Eu assisto à festa.', 'He watch**es** the toys.'),
        verb('carry', '📦', 'carregar', 'I carry a box.', 'Eu carrego uma caixa.', 'She carr**ies** the balloons.'),
        verb('tell', '🗣️', 'contar', 'I tell a story.', 'Eu conto uma história.', 'Buzz tell**s** stories.')]),
]
