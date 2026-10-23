# Mais repertório para os 5 primeiros episódios do A1 (além das frases da cena da obra):
# molde de frases, quiz de expressões, mais perguntas, mais falas e missões do "Sua vez".
# Mesma ordem de model_v2_data.V2.

def sl(cat, *opts):
    return dict(cat=cat, opts=[list(o) for o in opts])


def page(label, slots, end='.', endpt=None):
    return dict(label=label, slots=slots, end=[end, endpt if endpt is not None else end])


def qz(ask, opts, a, why, say=None):
    d = dict(ask=ask, opts=opts, a=a, why=why)
    if say:
        d['say'] = say
    return d


def ms(ic, name, desc, prompt, chip, model, check, kw, tips, ok, reply):
    """Missão do 'Sua vez': só 1 peça, sem resposta escrita no campo."""
    return dict(ic=ic, name=name, desc=desc, data=dict(
        prompt=prompt, ph='Escreva a sua resposta aqui…', chips=[chip], model=model, check=check, kw=kw, tips=tips, ok=ok, reply=reply))


MORE = [
    # ---- 1 · I'm ----
    dict(
        mold=[
            page('Dizer quem você é', [
                sl('saudação', ('Hi,', 'oi,'), ('Hello,', 'olá,'), ('Hey,', 'e aí,'), ('Good morning,', 'bom dia,')),
                sl('eu sou', ("I'm", 'eu sou')),
                sl('nome', ('Ana', 'a Ana'), ('Leo', 'o Leo'), ('Maria', 'a Maria'), ('Sam', 'o Sam'), ('Paddington', 'o Paddington'))]),
            page('Dizer de onde você é', [
                sl('eu sou de', ("I'm from", 'eu sou de')),
                sl('lugar', ('Brazil', 'Brasil'), ('Portugal', 'Portugal'), ('Peru', 'Peru'), ('London', 'Londres'), ('São Paulo', 'São Paulo'), ('Japan', 'Japão'))]),
            page('Dizer como você está', [
                sl('eu estou', ("I'm", 'eu estou')),
                sl('sentimento', ('hungry', 'com fome'), ('tired', 'cansado(a)'), ('happy', 'feliz'), ('nervous', 'nervoso(a)'), ('excited', 'animado(a)'), ('ready', 'pronto(a)')),
                sl('quando', ('today', 'hoje'), ('now', 'agora'), ('tonight', 'hoje à noite'))])],
        speak=[["Hi! I'm Ana. I'm from Brazil.", 'Oi! Eu sou a Ana. Sou do Brasil.'], ["I'm beat, but I'm happy.", 'Estou exausto, mas estou feliz.']],
        trap=[qz('O que “I’m starving!” quer dizer?', ['Estou com muita fome.', 'Estou com frio.', 'Estou com medo.'], 0, '**starving** é gíria para muita fome.', "I'm starving!"),
              qz('Qual frase está certa?', ['She sleep a lot.', 'She sleeps a lot.', 'She sleeping a lot.'], 1, 'Com she, o verbo ganha o final: **sleeps**.')],
        gap=[dict(text='___ starving! I need food.', pt='Estou morrendo de fome! Preciso comer.', opts=["I'm", 'I', 'Me'], a=0, why="Eu estou = **I'm**.", say="I'm starving! I need food."),
             dict(text="How's it ___?", pt='E aí, tudo bem?', opts=['going', 'go', 'goes'], a=0, why="A expressão inteira é **How's it going?**", say="How's it going?")],
        expq=[qz('Seu amigo está morrendo de fome. O que ele diz?', ["I'm starving!", "I'm beat.", 'Not bad.'], 0, '**I\'m starving!** = estou morrendo de fome.'),
              qz('Alguém pergunta “How’s it going?”. Qual resposta combina?', ['Not bad, thanks.', "I'm from Peru.", 'Yes, I am.'], 0, '**Not bad.** é a resposta típica.'),
              qz('Você está exausto depois de um dia longo. O que diz?', ["I'm beat.", "I'm starving!", "How's it going?"], 0, '**I\'m beat.** = estou exausto.')],
        missions=[
            ms('🎒', 'Primeiro dia de aula', 'Apresente-se a um colega novo.',
               "No primeiro dia de aula, você conhece um colega. **Diga seu nome com I'm, de onde você é e como você está.**", "I'm",
               "Hi! I'm Leo. I'm from Portugal. I'm a little nervous today.",
               ["Disse meu nome com I'm?", 'Disse de onde eu sou?', 'Disse como eu estou?'],
               [r"\bI(?:['’]m| am)\s+(?!(?:from|a|an|the|not|very|so|really|fine|good|great|tired|hungry|happy|ok|okay|sleepy|excited|nervous|ready|cold|hot|well|sad|busy)\b)[a-zà-ú]+|\bmy name is\s+\w+", r"\bfrom\s+\w+",
                r"\bI(?:['’]m| am)\s+(?:very |so |really |a little |a bit )?(?:fine|good|great|tired|hungry|happy|ok|okay|sleepy|excited|nervous|ready|cold|hot|well|sad|busy)\b"],
               [[["Hi! I'm Ana.", 'Oi! Eu sou a Ana.']], [["I'm from São Paulo.", 'Sou de São Paulo.']], [["I'm a little nervous.", 'Estou um pouco nervoso.']]],
               ['Nome com I\'m! 🙋', 'De onde você é! 🌎', 'Como você está! 😄'],
               ["Nice to meet you! Welcome to our class!", 'Prazer! Bem-vindo à nossa turma!']),
            ms('🗣️', 'Papo de gente de verdade', 'Cumprimente e responda com gírias.',
               "Seu amigo pergunta **How's it going?** **Responda de um jeito natural e diga que está com muita fome ou muito cansado, usando a gíria.**", "Not bad.",
               "Not bad, thanks! But I'm starving. Let's eat!",
               ['Respondi de forma natural?', 'Usei uma gíria (starving ou beat)?', 'Disse como estou com I\'m?'],
               [r"\bnot bad\b|\bI['’]?m (?:good|fine|great|okay|ok)\b|\bpretty good\b", r"\bstarving\b|\bbeat\b", r"\bI['’]?m\b|\bI am\b"],
               [[['Not bad, thanks.', 'Nada mal, obrigado.']], [["I'm starving!", 'Estou morrendo de fome!']], [["I'm beat.", 'Estou exausto.']]],
               ['Resposta natural! 👍', 'Gíria usada! 🤤', 'Com I\'m! 🙋'],
               ["Ha ha! Me too. Let's get a sandwich!", 'Ha ha! Eu também. Vamos comer um sanduíche!'])]),
    # ---- 2 · Are you…? ----
    dict(
        mold=[
            page('Perguntar com Are you…?', [
                sl('pergunta', ('Are you', 'você está/é')),
                sl('palavra', ('tired', 'cansado(a)'), ('lost', 'perdido(a)'), ('hungry', 'com fome'), ('ready', 'pronto(a)'), ('late', 'atrasado(a)'), ('new here', 'novo(a) aqui'), ('a teacher', 'professor(a)'), ('from Brazil', 'do Brasil'))], '?'),
            page('Responder', [
                sl('sim ou não', ('Yes,', 'sim,'), ('No,', 'não,')),
                sl('resposta curta', ('I am.', 'eu sou/estou.'), ("I'm not.", 'eu não sou/estou.'))]),
            page('Onde você está?', [
                sl('pergunta', ('Are you', 'você está')),
                sl('lugar', ('at home', 'em casa'), ('at work', 'no trabalho'), ('at school', 'na escola'), ('at the station', 'na estação'), ('in a hurry', 'com pressa'))], '?')],
        speak=[["Are you tired? No, I'm not.", 'Você está cansado? Não, não estou.'], ['Are you kidding? Hurry up!', 'Está brincando? Anda logo!']],
        trap=[qz('“Are you kidding?” quer dizer…', ['Você está brincando?', 'Você está com frio?', 'Você está perdido?'], 0, '**Are you kidding?** = está brincando? (surpresa).', 'Are you kidding?'),
              qz('Qual frase está certa?', ['I am late running.', "I'm running late.", 'I running late.'], 1, 'Estou atrasado = **I\'m running late.**')],
        gap=[dict(text='___ you okay?', pt='Você está bem?', opts=['Are', 'Is', 'Do'], a=0, why='Com you: **Are** you…?', say='Are you okay?'),
             dict(text="Hurry ___, we're late!", pt='Anda logo, estamos atrasados!', opts=['up', 'on', 'in'], a=0, why='**Hurry up!** = anda logo!', say="Hurry up, we're late!")],
        expq=[qz('Seu amigo parece muito triste. O que você pergunta?', ['Are you okay?', 'Are you kidding?', 'Hurry up!'], 0, '**Are you okay?** = você está bem?'),
              qz('Você vai chegar tarde e quer avisar.', ["I'm running late.", 'Hurry up!', 'Are you okay?'], 0, '**I\'m running late.** = estou atrasado.'),
              qz('Alguém diz algo absurdo e você não acredita.', ['Are you kidding?', "I'm running late.", 'Are you okay?'], 0, '**Are you kidding?** mostra surpresa.')],
        missions=[
            ms('👋', 'Colega novo', 'Faça perguntas e responda com respostas curtas.',
               "Você encontra uma pessoa nova na escola. **Faça duas perguntas com Are you…? e responda uma delas com Yes, I am ou No, I'm not.**", 'Are you',
               "Are you new here? Yes, I am. Are you from Brazil?",
               ['Fiz uma pergunta com Are you…?', 'Fiz duas perguntas?', 'Usei a resposta curta?'],
               [r"\bare you\b[^.!?]*\?", r"(?:\bare you\b[^.!?]*\?[\s\S]*){2}", r"\b(?:yes,?\s*i am|no,?\s*i(?:['’]m| am) not)\b"],
               [[['Are you new here?', 'Você é novo aqui?']], [['Are you from Brazil?', 'Você é do Brasil?']], [['Yes, I am.', 'Sim, sou.'], ["No, I'm not.", 'Não, não sou.']]],
               ['Pergunta com Are you! ❓', 'Duas perguntas! ✌️', 'Resposta curta certa! ✅'],
               ["Yes, I am! Nice to meet you!", 'Sim, sou! Prazer em conhecer você!']),
            ms('🏃', 'Atrasado de novo!', 'Use as expressões do episódio.',
               "Seu amigo está atrasado e parece nervoso. **Pergunte se ele está bem, avise que você também está atrasado e peça para ele andar logo.**", 'Are you okay?',
               "Are you okay? I'm running late too. Hurry up!",
               ['Perguntei se ele está bem?', 'Avisei que estou atrasado?', 'Pedi para andar logo?'],
               [r"\bare you (?:okay|ok)\b", r"\brunning late\b", r"\bhurry up\b"],
               [[['Are you okay?', 'Você está bem?']], [["I'm running late.", 'Estou atrasado.']], [['Hurry up!', 'Anda logo!']]],
               ['Cuidado com o amigo! 🫶', 'Aviso dado! ⏰', 'Anda logo! 🏃'],
               ["I'm fine! Let's run!", 'Estou bem! Vamos correr!'])]),
    # ---- 3 · He's / She's ----
    dict(
        mold=[
            page('Dizer quem é', [
                sl('quem', ("He's", 'ele é'), ("She's", 'ela é')),
                sl('o quê', ('a teacher', 'professor(a)'), ('a doctor', 'médico(a)'), ('a singer', 'cantor(a)'), ('a student', 'estudante'), ('my friend', 'meu amigo/minha amiga'), ('from Brazil', 'do Brasil'))]),
            page('Dizer como é', [
                sl('quem', ("He's", 'ele é'), ("She's", 'ela é')),
                sl('como', ('kind', 'gentil'), ('funny', 'engraçado(a)'), ('smart', 'inteligente'), ('brave', 'corajoso(a)'), ('tired', 'cansado(a)'), ('cool', 'legal'), ('awesome', 'incrível'))]),
            page('Dizer onde está', [
                sl('quem', ("He's", 'ele está'), ("She's", 'ela está')),
                sl('onde', ('at home', 'em casa'), ('at work', 'no trabalho'), ('at school', 'na escola'), ('in the kitchen', 'na cozinha'), ('in London', 'em Londres'))])],
        speak=[["He's my friend. He's cool.", 'Ele é meu amigo. Ele é legal.'], ["She's a doctor. She's awesome!", 'Ela é médica. Ela é incrível!']],
        trap=[qz('“He’s nuts” quer dizer…', ['Ele é maluco (informal).', 'Ele está com fome.', 'Ele é novo.'], 0, '**nuts** é gíria para maluco, doido.', "He's nuts."),
              qz('Qual frase está certa?', ['He walk to school.', 'He walks to school.', 'He walking to school.'], 1, 'Com he, o verbo ganha o final: **walks**.')],
        gap=[dict(text="___ my friend. He's cool.", pt='Ele é meu amigo. Ele é legal.', opts=["He's", "She's", "I'm"], a=0, why='Falando de um homem: **He\'s**.', say="He's my friend. He's cool."),
             dict(text="She's ___! Everybody loves her.", pt='Ela é incrível! Todo mundo gosta dela.', opts=['awesome', 'nuts', 'a Wizard'], a=0, why='**awesome** = incrível.', say="She's awesome! Everybody loves her.")],
        expq=[qz('Você quer elogiar muito uma amiga.', ["She's awesome!", "He's nuts.", "He's from Kansas."], 0, '**awesome** = incrível.'),
              qz('Seu amigo faz coisas doidas.', ["He's nuts.", "She's awesome!", "He's the best!"], 0, '**nuts** = maluco, doido.'),
              qz('Seu cachorro é o melhor do mundo para você.', ["He's the best!", "He's from Kansas.", "She's a Wizard."], 0, '**the best** = o melhor.')],
        missions=[
            ms('📷', 'Foto de colegas', 'Diga quem são e o que fazem.',
               "Você mostra uma foto de dois colegas de trabalho. **Diga quem são e o que fazem, com He's e She's.**", "He's",
               "He's Leo. He's a doctor. She's Ana. She's a teacher.",
               ["Falei de um homem com He's?", "Falei de uma mulher com She's?", 'Disse o que fazem ou quem são?'],
               [r"\bhe(?:['’]s| is)\b", r"\bshe(?:['’]s| is)\b", r"\b(?:he|she)(?:['’]s| is)\s+(?:a|an|my|the)\s+\w+"],
               [[["He's Leo.", 'Ele é o Leo.']], [["She's Ana.", 'Ela é a Ana.']], [["He's a doctor.", 'Ele é médico.'], ["She's a teacher.", 'Ela é professora.']]],
               ['Falou dele! 👨', 'Falou dela! 👩', 'Quem são! 🌟'],
               ['Great team! They sound awesome.', 'Ótima equipe! Parecem incríveis.']),
            ms('🌟', 'Elogie com gírias', 'Use cool, awesome, nuts ou the best.',
               "Fale de um amigo e de uma amiga e **use gírias de elogio: cool, awesome, nuts ou the best.**", "She's",
               "He's cool. She's awesome! He's nuts, but he's the best!",
               ["Falei de um amigo com He's?", "Falei de uma amiga com She's?", 'Usei uma gíria?'],
               [r"\bhe(?:['’]s| is)\b", r"\bshe(?:['’]s| is)\b", r"\b(?:cool|awesome|nuts|the best)\b"],
               [[["He's cool.", 'Ele é legal.']], [["She's awesome!", 'Ela é incrível!']], [["He's the best!", 'Ele é o melhor!']]],
               ['Amigo! 👨', 'Amiga! 👩', 'Gíria usada! 😎'],
               ['Wow! Your friends are lucky to have you!', 'Uau! Seus amigos têm sorte de ter você!'])]),
    # ---- 4 · Is he / she / it ----
    dict(
        mold=[
            page('Perguntar', [
                sl('pergunta', ('Is he', 'ele é/está'), ('Is she', 'ela é/está'), ('Is it', 'isso é/está')),
                sl('palavra', ('a fairy', 'uma fada'), ('angry', 'bravo(a)'), ('a big ship', 'um navio grande'), ('far', 'longe'), ('your friend', 'seu amigo'), ('a bird', 'um pássaro'), ('ready', 'pronto(a)'))], '?'),
            page('Responder', [
                sl('sim ou não', ('Yes,', 'sim,'), ('No,', 'não,')),
                sl('resposta curta', ('he is.', 'ele é.'), ('she is.', 'ela é.'), ('it is.', 'é.'), ("he isn't.", 'ele não é.'), ("it isn't.", 'não é.'))]),
            page('Perguntas do dia a dia', [
                sl('pergunta', ('Is it', 'isso é/está')),
                sl('palavra', ('a big deal', 'grande coisa'), ('far from here', 'longe daqui'), ('expensive', 'caro'), ('easy', 'fácil'), ('for real', 'de verdade'))], '?')],
        speak=[['Is he for real? No way!', 'Ele é de verdade? Nem pensar!'], ["Is it far? No, it's a piece of cake.", 'É longe? Não, é moleza.']],
        trap=[qz('“It’s a piece of cake” quer dizer…', ['É moleza.', 'É um bolo.', 'É perigoso.'], 0, '**piece of cake** = muito fácil.', "It's a piece of cake."),
              qz('Qual frase está certa?', ['She fly every night.', 'She flies every night.', 'She flys every night.'], 1, 'fly → **flies** (y vira -ies).')],
        gap=[dict(text='___ he for real?', pt='Ele é de verdade?', opts=['Is', 'Are', 'Does'], a=0, why='Com he: **Is** he…?', say='Is he for real?'),
             dict(text='No ___! I do not believe it.', pt='Nem pensar! Eu não acredito.', opts=['way', 'day', 'one'], a=0, why='**No way!** = nem pensar!', say='No way! I do not believe it.')],
        expq=[qz('Algo é muito fácil. O que você diz?', ["It's a piece of cake.", 'No way!', 'Is it a big deal?'], 0, '**piece of cake** = moleza.'),
              qz('Você não acredita no que ouviu.', ['No way!', "It's a piece of cake.", 'Is it a big deal?'], 0, '**No way!** = não acredito!'),
              qz('Você quer saber se algo é grave.', ['Is it a big deal?', 'No way!', "It's a piece of cake."], 0, '**big deal** = grande coisa, algo sério.')],
        missions=[
            ms('🔍', 'Foto misteriosa', 'Pergunte sobre ele, ela e a coisa.',
               "Você vê uma foto do seu amigo e do cachorro dele. **Faça uma pergunta com Is he…? e uma com Is it…?, e responda uma com Yes ou No.**", 'Is he',
               "Is he your friend? Is it a big dog? Yes, it is!",
               ['Fiz uma pergunta com Is he…?', 'Fiz uma pergunta com Is it…?', 'Usei uma resposta curta?'],
               [r"\bis he\b[^.!?]*\?", r"\bis it\b[^.!?]*\?", r"\b(?:yes,?\s*(?:he|she|it) is|no,?\s*(?:he|she|it) isn['’]?t)\b"],
               [[['Is he your friend?', 'Ele é seu amigo?']], [['Is it a big dog?', 'É um cachorro grande?']], [['Yes, it is.', 'Sim, é.'], ["No, he isn't.", 'Não, não é.']]],
               ['Pergunta sobre ele! 🧒', 'Pergunta sobre a coisa! 🐶', 'Resposta curta! ✅'],
               ['Good questions! Yes, he is my friend.', 'Boas perguntas! Sim, ele é meu amigo.']),
            ms('😮', 'Dúvida e moleza', 'Use as expressões do episódio.',
               "Alguém promete algo difícil. **Mostre dúvida com Is he for real? ou No way!, e diga que algo é moleza com It's a piece of cake.**", 'No way!',
               "Is he for real? No way! It's a piece of cake!",
               ['Mostrei dúvida (for real ou no way)?', 'Disse que é moleza?', 'Fiz uma pergunta ou usei It\'s?'],
               [r"\bis (?:he|she|it) for real\b|\bno way\b", r"\bpiece of cake\b", r"\bis (?:he|she|it)\b[^.!?]*\?|\bit['’]?s\b"],
               [[['Is he for real?', 'Ele está falando sério?']], [["It's a piece of cake!", 'É moleza!']], [['No way!', 'Nem pensar!']]],
               ['Dúvida! 🤔', 'Moleza! 🍰', 'Frase completa! ✅'],
               ["Really? It's easy for me too!", 'Sério? Para mim também é fácil!'])]),
    # ---- 5 · Plural ----
    dict(
        mold=[
            page('Contar coisas', [
                sl('verbo', ('I see', 'eu vejo'), ('I have', 'eu tenho'), ('I love', 'eu adoro')),
                sl('número', ('two', 'dois'), ('three', 'três'), ('four', 'quatro'), ('five', 'cinco')),
                sl('coisas', ('toys', 'brinquedos'), ('balloons', 'balões'), ('books', 'livros'), ('puppies', 'cachorrinhos'), ('stories', 'histórias'), ('parties', 'festas'), ('boxes', 'caixas'), ('cats', 'gatos'))]),
            page('Gostar de', [
                sl('verbo', ('I love', 'eu adoro'), ('I like', 'eu gosto de')),
                sl('coisas', ('puppies', 'cachorrinhos'), ('stories', 'histórias'), ('parties', 'festas'), ('toys', 'brinquedos'), ('movies', 'filmes'), ('cookies', 'biscoitos'))]),
            page('Perguntar quantos', [
                sl('pergunta', ('How many', 'quantos')),
                sl('coisas', ('toys', 'brinquedos'), ('balloons', 'balões'), ('puppies', 'cachorrinhos'), ('boxes', 'caixas')),
                sl('fim', ('are there', 'há'))], '?')],
        speak=[['Hey, guys! I have tons of toys.', 'E aí, pessoal! Tenho um monte de brinquedos.'], ['Two thumbs up! I love parties.', 'Aprovado! Eu adoro festas.']],
        trap=[qz('“Two thumbs up!” quer dizer…', ['Aprovado! Gostei muito!', 'Estou com medo!', 'Preciso de ajuda!'], 0, '**Two thumbs up!** = aprovado, gostei muito.', 'Two thumbs up!'),
              qz('Qual frase está certa?', ['He watchs the toys.', 'He watches the toys.', 'He watching the toys.'], 1, 'watch → **watches** (final -ch ganha -es).')],
        gap=[dict(text='I have tons of ___.', pt='Tenho um monte de brinquedos.', opts=['toys', 'toy', 'toies'], a=0, why='**tons of** + plural: toys.', say='I have tons of toys.'),
             dict(text='Hey, ___! Come to the party!', pt='E aí, pessoal! Venham para a festa!', opts=['guys', 'guy', 'guyes'], a=0, why='**guys** = pessoal (plural).', say='Hey, guys! Come to the party!')],
        expq=[qz('Você quer chamar um grupo de amigos.', ['Hey, guys!', 'Two thumbs up!', 'Tons of toys!'], 0, '**Hey, guys!** = e aí, pessoal!'),
              qz('Você adorou a festa e quer aprovar.', ['Two thumbs up!', 'Hey, guys!', 'Tons of toys!'], 0, '**Two thumbs up!** = aprovado!'),
              qz('Tem brinquedo demais no quarto.', ['Tons of toys!', 'Two thumbs up!', 'Hey, guys!'], 0, '**Tons of** = um monte de.')],
        missions=[
            ms('🏠', 'Meu quarto', 'Conte o que há no seu quarto.',
               "Você descreve o seu quarto. **Use três plurais: pelo menos dois com -s e um com -ies.**", 'I have',
               "I have three books and two cats. I love puppies and stories.",
               ['Usei número + plural com -s?', 'Usei um plural com -ies?', 'Disse o que tenho ou adoro?'],
               [r"\b(?:two|three|four|five|six|seven|eight|nine|ten|many|some)\s+\w+s\b", r"\b\w+ies\b", r"\bI\s+(?:have|see|love|like)\b"],
               [[['I have three books.', 'Tenho três livros.']], [['I love puppies.', 'Eu adoro cachorrinhos.']], [['I see two cats.', 'Vejo dois gatos.']]],
               ['Número com plural! 🔢', 'Plural com -ies! 🐶', 'Frase completa! 🏠'],
               ['Wow! Your room is full of fun things.', 'Uau! Seu quarto está cheio de coisas legais.']),
            ms('🎉', 'Convite para a festa', 'Use as expressões do episódio.',
               "Você chama os amigos para uma festa. **Use Hey, guys! e Tons of…, e aprove a festa com Two thumbs up!**", 'Hey, guys!',
               "Hey, guys! Come to my party! Tons of toys and balloons. Two thumbs up!",
               ['Chamei o grupo (Hey, guys)?', 'Usei Tons of…?', 'Aprovei com Two thumbs up?'],
               [r"\bhey,?\s*guys\b", r"\btons of\b", r"\btwo thumbs up\b"],
               [[['Hey, guys!', 'E aí, pessoal!']], [['Tons of toys!', 'Um monte de brinquedos!']], [['Two thumbs up!', 'Aprovado!']]],
               ['Grupo chamado! 👋', 'Um monte! 🧸', 'Aprovado! 👍'],
               ["Awesome! We'll be there!", 'Demais! A gente vai!'])]),
]


def ctx(text, pt, opts, a=0):
    return dict(text=text, pt=pt, opts=opts, a=a)


# Palavras em contexto: 6 frases, uma para cada palavra do episódio (a resposta é sempre a primeira opção; o gerador embaralha)
CONTEXT = [
    [ctx('He is brown, he wears a red hat and he loves marmalade. He is a ___.', 'Ele é marrom, usa chapéu vermelho e adora geleia. Ele é um urso.', ['bear', 'station', 'tired']),
     ctx('The train stops at the ___. We wait on the platform.', 'O trem para na estação. Esperamos na plataforma.', ['station', 'hungry', 'Peru']),
     ctx("It's lunch time and I want a sandwich. I'm ___.", 'É hora do almoço e quero um sanduíche. Estou com fome.', ['hungry', 'happy', 'bear']),
     ctx("It was a long trip. Now I want to sleep. I'm ___.", 'Foi uma viagem longa. Agora quero dormir. Estou cansado.', ['tired', 'station', 'happy']),
     ctx("I have a new home and new friends. I'm so ___!", 'Tenho uma casa nova e amigos novos. Estou tão feliz!', ['happy', 'tired', 'hungry']),
     ctx('Machu Picchu is in ___. It is a country in South America.', 'Machu Picchu fica no Peru. É um país da América do Sul.', ['Peru', 'bear', 'station'])],
    [ctx('It has long ears and it jumps. In the story, the White ___ has a clock.', 'Tem orelhas compridas e pula. Na história, o Coelho Branco tem um relógio.', ['rabbit', 'cat', 'hurry']),
     ctx("The class starts at eight. It's eight thirty. I'm ___.", 'A aula começa às oito. São oito e meia. Estou atrasado.', ['late', 'new', 'lost']),
     ctx("I don't know the way and I have no map. I'm ___.", 'Não sei o caminho e não tenho mapa. Estou perdida.', ['lost', 'new', 'late']),
     ctx("It's my first day at school. I'm ___ here.", 'É meu primeiro dia na escola. Sou nova aqui.', ['new', 'lost', 'cat']),
     ctx('It says meow, it has whiskers and it sleeps a lot. It is a ___.', 'Faz miau, tem bigodes e dorme muito. É um gato.', ['cat', 'rabbit', 'hurry']),
     ctx('The train leaves in two minutes! We are in a ___.', 'O trem sai em dois minutos! Estamos com pressa.', ['hurry', 'late', 'lost'])],
    [ctx('She has a black hat and a broom. In the story there is a good ___.', 'Ela tem chapéu preto e vassoura. Na história há uma bruxa boa.', ['witch', 'wizard', 'lion']),
     ctx('He does magic in the Emerald City. He is the ___ of Oz.', 'Ele faz mágica na Cidade das Esmeraldas. Ele é o Mágico de Oz.', ['wizard', 'witch', 'home']),
     ctx('He is a big cat with a mane. He is a ___.', 'Ele é um gato grande com juba. Ele é um leão.', ['lion', 'wizard', 'kind']),
     ctx("She helps everybody. She's very ___.", 'Ela ajuda todo mundo. Ela é muito gentil.', ['kind', 'scared', 'home']),
     ctx("It's dark and he hears a noise. He's ___.", 'Está escuro e ele ouve um barulho. Ele está com medo.', ['scared', 'kind', 'lion']),
     ctx("There's no place like ___.", 'Não há lugar como o nosso lar.', ['home', 'witch', 'wizard'])],
    [ctx('She is very small, she has wings and she shines. She is a ___.', 'Ela é bem pequena, tem asas e brilha. Ela é uma fada.', ['fairy', 'bird', 'ship']),
     ctx('It sails on the sea. Pirates travel on a ___.', 'Ele navega no mar. Piratas viajam em um navio.', ['ship', 'light', 'captain']),
     ctx('It flies, it sings and it lives in a tree. It is a ___.', 'Voa, canta e vive numa árvore. É um pássaro.', ['bird', 'fairy', 'angry']),
     ctx('His face is red and he shouts. He is very ___.', 'O rosto dele está vermelho e ele grita. Ele está muito bravo.', ['angry', 'captain', 'light']),
     ctx('He leads the ship and the pirates. He is the ___.', 'Ele comanda o navio e os piratas. Ele é o capitão.', ['captain', 'bird', 'ship']),
     ctx("It's dark. Turn on the ___, please.", 'Está escuro. Acenda a luz, por favor.', ['light', 'fairy', 'angry'])],
    [ctx('Andy has a doll, a car and a robot. They are his ___.', 'O Andy tem uma boneca, um carro e um robô. São os brinquedos dele.', ['toys', 'planets', 'parties']),
     ctx('At the party there are red, blue and yellow ___.', 'Na festa há balões vermelhos, azuis e amarelos.', ['balloons', 'stories', 'puppies']),
     ctx('Two baby dogs are under the table. They are ___.', 'Dois filhotes de cachorro estão debaixo da mesa. São cachorrinhos.', ['puppies', 'planets', 'toys']),
     ctx('Grandma reads before bed. I love her ___.', 'A vovó lê antes de dormir. Eu adoro as histórias dela.', ['stories', 'parties', 'balloons']),
     ctx('We have cake, music and friends at birthday ___.', 'Temos bolo, música e amigos nas festas de aniversário.', ['parties', 'puppies', 'stories']),
     ctx('Mars, Venus and Earth are ___.', 'Marte, Vênus e a Terra são planetas.', ['planets', 'toys', 'balloons'])],
]
