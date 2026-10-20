"""Reescreve as continuações do inglês regular no modelo aprovado (gancho + história com os mesmos
personagens + menos exercícios + "Sua vez" com resposta do personagem).
Uso (da raiz do repositório):  python3 tools/cont_a1.py [arquivo]      padrão: data/en-a1_01.json
Parte sempre do arquivo original (git, ORIGINAL_REV), então pode rodar de novo sem acumular mudanças.
Cada SPEC é escrito à mão; o script só monta os quadros e testa as palavras-chave."""
import json
import re
import subprocess
import sys

ORIGINAL_REV = 'f170c43'
F = sys.argv[1] if len(sys.argv) > 1 else 'data/en-a1_01.json'

PA = {'t': 'ship', 'p': ['#a8dcf5', '#fde7c8', '#2a6f97'], 'e': ['🗣️', '💬', '✨'], 'v': 0}
CAST = {'Rosa': ['👩‍🦰', '#FF6F59'], 'Mia': ['👩', '#7C4DFF'], 'Sam': ['🧑', '#12B3A8'], 'Ana': ['👩‍🦰', '#FF6F59'],
        'Leo': ['🧑‍🦱', '#7C4DFF'], 'Ben': ['🧑‍🦱', '#7C4DFF'], 'Clerk': ['🧑‍💼', '#12B3A8'], 'Agent': ['🧑‍💼', '#12B3A8'],
        'Mom': ['👩', '#12B3A8'], 'Rita': ['👩‍🦰', '#FF6F59'], 'Dan': ['🧑‍💼', '#7C4DFF'], 'Kenji': ['🧑', '#7C4DFF'], 'Mei': ['👩', '#FF6F59']}


def sc(a, b, *lines):
    return {'a': a, 'b': b, 'lines': [list(x) for x in lines]}


I_AM = r"\bI(?:['’]m| am)"

SPECS = {
 7009801: dict(
    t="Quem é você? · I'm", sub='Quem é você? Em 10 minutos você se apresenta em inglês',
    say='A Mia acabou de chegar ao hotel. O recepcionista pergunta quem ela é. E agora?',
    hook=['Good evening! Welcome to the hotel. And you are…?', 'Boa noite! Bem-vinda ao hotel. E você é…?'],
    rs='lobby1', cast=('Dan', 'Mia'),
    lines=[('Dan', 'Good evening! Welcome to the hotel. And you are…?', 'Boa noite! Bem-vinda ao hotel. E você é…?'),
           ('Mia', "Hi! I'm Mia. I'm from Brazil.", 'Oi! Eu sou a Mia. Sou do Brasil.'),
           ('Dan', "Nice to meet you, Mia! I'm Dan.", 'Prazer, Mia! Eu sou o Dan.'),
           ('Mia', "Nice to meet you, Dan. I'm a little tired. It's a long flight!", 'Prazer, Dan. Estou um pouco cansada. É um voo longo!'),
           ('Dan', 'No problem! Your room is ready.', 'Sem problema! Seu quarto está pronto.'),
           ('Mia', "Great! I'm not hungry, just sleepy.", 'Ótimo! Não estou com fome, só com sono.')],
    fact='Na fala de todo dia, quase ninguém diz **I am** inteiro: o normal é **I\'m**. O “I am” completo soa enfático, como em **“I AM tired!”** (eu estou MESMO cansada).',
    prompt="No hotel, o recepcionista pergunta quem você é. **Diga seu nome com I'm, diga de onde você é e diga como você está.**",
    ph="Ex.: Hi! I'm Ana. I'm from Brazil. I'm a little tired.", chips=["Hi! I'm", "I'm from", "I'm a little"],
    model="Hi! I'm Ana. I'm from Brazil. I'm a little tired, but happy to be here.",
    check=["Disse meu nome com I'm?", 'Disse de onde eu sou?', 'Disse como eu estou?'],
    kw=[I_AM + r"\s+(?!(?:from|a|an|the|not|very|so|really|fine|good|great|tired|hungry|happy|ok|okay|sleepy|excited|nervous|cold|hot|well|sad|busy)\b)[a-zà-ú]+|\bmy name is\s+\w+",
        r"\bfrom\s+\w+",
        I_AM + r"\s+(?:very |so |really |a little |a bit )?(?:fine|good|great|tired|hungry|happy|ok|okay|sleepy|excited|nervous|cold|hot|well|sad|busy)\b|\bnot bad\b"],
    tips=[[["Hi! I'm Ana.", 'Oi! Eu sou a Ana.'], ["Hello, I'm Leo.", 'Olá, eu sou o Leo.'], ["Hey! I'm Mia.", 'E aí! Eu sou a Mia.']],
          [["I'm from Brazil.", 'Eu sou do Brasil.'], ["I'm from São Paulo.", 'Eu sou de São Paulo.'], ["I'm from Portugal.", 'Eu sou de Portugal.']],
          [["I'm a little tired.", 'Estou um pouco cansada.'], ["I'm fine, thanks.", 'Estou bem, obrigada.'], ["I'm so happy to be here!", 'Estou muito feliz de estar aqui!']]],
    ok=["Nome com I'm! 🙋", 'Você disse de onde é! 🌎', 'E como você está! 😄'],
    reply=["Welcome, and nice to meet you! I'm Dan, at the front desk. Your room is ready. Rest well!",
           'Bem-vindo(a) e prazer! Eu sou o Dan, da recepção. Seu quarto está pronto. Descanse bem!', 'Dan', '🧑‍💼'],
    recap=[["I'm Mia.", 'Eu sou a Mia.'], ["I'm from Brazil.", 'Eu sou do Brasil.'], ["I'm a little tired.", 'Estou um pouco cansada.'], ['Nice to meet you!', 'Prazer em conhecer você!']]),

 7070001: dict(
    t='Perdida no metrô · Are you…?', sub='Perdida no metrô: aprenda a perguntar com Are you…?',
    say='A Mia está perdida no metrô de Nova York. Quem pode ajudar?',
    hook=['Excuse me! Are you from New York?', 'Com licença! Você é de Nova York?'],
    rs='subway', cast=('Rosa', 'Mia'),
    lines=[('Mia', 'Excuse me! Are you from New York?', 'Com licença! Você é de Nova York?'),
           ('Rosa', 'Yes, I am. Are you lost?', 'Sim, sou. Você está perdida?'),
           ('Mia', "Yes, I'm lost! I'm not from here.", 'Sim, estou perdida! Não sou daqui.'),
           ('Rosa', "No problem! I'm a student. I know the subway.", 'Sem problema! Sou estudante. Eu conheço o metrô.'),
           ('Mia', 'Great! Are you busy now?', 'Ótimo! Você está ocupada agora?'),
           ('Rosa', "No, I'm not. Come with me!", 'Não, não estou. Venha comigo!')],
    fact='Em inglês, a pergunta com **be** inverte a ordem: “You are lost” vira **“Are you lost?”**. O verbo sobe para o começo da frase.',
    prompt="No metrô, uma pessoa simpática ouve você pedir ajuda. **Pergunte se ela é de Nova York, diga que você está perdido(a) e diga que não é daqui.**",
    ph="Ex.: Excuse me! Are you from New York? I'm lost. I'm not from here.", chips=['Excuse me!', 'Are you', "I'm lost"],
    model="Excuse me! Are you from New York? I'm lost. I'm not from here.",
    check=['Perguntei se é de Nova York?', 'Disse que estou perdido(a)?', 'Disse que não sou daqui?'],
    kw=[r"\bAre you\b", I_AM + r"\s+(?:so |very |really )?lost\b", I_AM + r"\s+not\s+from\b"],
    tips=[[['Are you from New York?', 'Você é de Nova York?'], ['Are you a New Yorker?', 'Você é nova-iorquino(a)?'], ['Excuse me, are you from here?', 'Com licença, você é daqui?']],
          [["I'm lost.", 'Estou perdido(a).'], ["I'm so lost!", 'Estou muito perdido(a)!'], ['I am lost.', 'Estou perdido(a).']],
          [["I'm not from here.", 'Não sou daqui.'], ["I'm not from New York.", 'Não sou de Nova York.'], ["I'm not from this city.", 'Não sou desta cidade.']]],
    ok=['Pergunta com Are you! ❓', 'Perdido(a), mas educado(a)! 🧭', 'Você disse que não é daqui! 🌎'],
    reply=["No problem! I'm Rosa, and I know the subway. Come with me!", 'Sem problema! Eu sou a Rosa e conheço o metrô. Venha comigo!', 'Rosa', '👩‍🦰'],
    recap=[['Are you from New York?', 'Você é de Nova York?'], ["I'm lost.", 'Estou perdido(a).'], ["I'm not from here.", 'Não sou daqui.'], ['No problem!', 'Sem problema!']]),

 7030001: dict(
    t='Foto de família · He\'s / She\'s', sub='Uma foto de família: apresente cada pessoa com He\'s, She\'s e It\'s',
    say='A Mia mostra uma foto da família para o Sam. Quem é quem?',
    hook=['Nice photo! Who is she?', 'Que foto legal! Quem é ela?'],
    rs='home1', cast=('Sam', 'Mia'),
    lines=[('Sam', 'Nice photo! Who is she?', 'Que foto legal! Quem é ela?'),
           ('Mia', "She's my sister, Ana. She's a teacher.", 'Ela é minha irmã, a Ana. Ela é professora.'),
           ('Sam', 'And who is he?', 'E quem é ele?'),
           ('Mia', "He's my brother, Leo. He's a student.", 'Ele é meu irmão, o Leo. Ele é estudante.'),
           ('Sam', "Look at the dog! It's big.", 'Olhe o cachorro! Ele é grande.'),
           ('Mia', "Yes! It's Max. They're my family.", 'Sim! É o Max. Eles são a minha família.')],
    fact='Em inglês, o gênero está no **pronome**, não no adjetivo: **he\'s tall** (ele é alto), **she\'s tall** (ela é alta). A palavra “tall” não muda.',
    prompt="Você mostra uma foto da sua família. **Apresente uma mulher com She's, um homem com He's e o pet com It's.**",
    ph="Ex.: She's my sister. He's my brother. It's my dog.", chips=["She's my", "He's my", "It's my"],
    model="She's my sister. He's my brother. It's my dog, Max.",
    check=["Apresentei uma mulher com She's?", "Apresentei um homem com He's?", "Falei do pet com It's?"],
    kw=[r"\bShe(?:['’]s| is)\b", r"\bHe(?:['’]s| is)\b", r"\bIt(?:['’]s| is)\b"],
    tips=[[["She's my sister.", 'Ela é minha irmã.'], ["She's my mom.", 'Ela é minha mãe.'], ["She's a teacher.", 'Ela é professora.']],
          [["He's my brother.", 'Ele é meu irmão.'], ["He's my dad.", 'Ele é meu pai.'], ["He's a student.", 'Ele é estudante.']],
          [["It's my dog.", 'É o meu cachorro.'], ["It's my cat.", 'É o meu gato.'], ["It's a big dog.", 'É um cachorro grande.']]],
    ok=["She's! 👩", "He's! 👨", "It's! 🐶"],
    reply=['What a nice family! They are so happy!', 'Que família bonita! Eles estão tão felizes!', 'Sam', '🧑'],
    recap=[["She's my sister.", 'Ela é minha irmã.'], ["He's my brother.", 'Ele é meu irmão.'], ["It's my dog.", 'É o meu cachorro.'], ["They're my family.", 'Eles são a minha família.']]),

 7070002: dict(
    t='Conheça os meus pais · They\'re', sub='Apresentar amigos e pais: He\'s, She\'s e They\'re',
    say='A Rita leva o Lee para casa. É hora de conhecer a mãe e o pai!',
    hook=['Mom, this is Lee. He\'s my friend.', 'Mãe, este é o Lee. Ele é meu amigo.'],
    rs='home1', cast=('Rita', 'Mom'),
    lines=[('Rita', "Mom, this is Lee. He's my friend.", 'Mãe, este é o Lee. Ele é meu amigo.'),
           ('Mom', "Hi, Lee! Nice to meet you. I'm Rita's mom.", 'Oi, Lee! Prazer. Sou a mãe da Rita.'),
           ('Rita', "And Dad? He's in the kitchen.", 'E o papai? Ele está na cozinha.'),
           ('Mom', "Yes! They're in the kitchen: Dad and the cat.", 'Sim! Eles estão na cozinha: o papai e o gato.'),
           ('Rita', "Look, it's our cat, Luna! She's so cute.", 'Olhe, é a nossa gata, a Luna! Ela é tão fofa.'),
           ('Mom', 'Come in, Lee! Please, sit down.', 'Entre, Lee! Sente-se, por favor.')],
    fact='**They\'re** serve para pessoas, bichos e coisas no plural: **They\'re my parents. They\'re my cats.** Em inglês, não existe “eles” e “elas” separados: é sempre **they**.',
    prompt="Você leva um amigo para conhecer sua mãe. **Apresente seu amigo com He's, apresente sua amiga com She's e fale dos seus pais com They're.**",
    ph="Ex.: He's my friend. She's my friend. They're my parents.", chips=["He's my", "She's my", "They're my"],
    model="He's my friend, Lee. She's my friend, Rita. They're my parents.",
    check=["Apresentei um amigo com He's?", "Apresentei uma amiga com She's?", "Falei dos meus pais com They're?"],
    kw=[r"\bHe(?:['’]s| is)\b", r"\bShe(?:['’]s| is)\b", r"\bThey(?:['’]re| are)\b"],
    tips=[[["He's my friend.", 'Ele é meu amigo.'], ["He's my classmate.", 'Ele é meu colega.'], ["He's from Brazil.", 'Ele é do Brasil.']],
          [["She's my friend.", 'Ela é minha amiga.'], ["She's my classmate.", 'Ela é minha colega.'], ["She's from Spain.", 'Ela é da Espanha.']],
          [["They're my parents.", 'Eles são meus pais.'], ["They're my mom and dad.", 'Eles são minha mãe e meu pai.'], ["They're nice.", 'Eles são legais.']]],
    ok=["He's! 👦", "She's! 👧", "They're! 👨‍👩‍👧"],
    reply=['Welcome to our home! Please, sit down. Tea?', 'Bem-vindo(a) à nossa casa! Sente-se, por favor. Chá?', 'Mom', '👩'],
    recap=[["He's my friend.", 'Ele é meu amigo.'], ["She's my friend.", 'Ela é minha amiga.'], ["They're my parents.", 'Eles são meus pais.'], ['Nice to meet you!', 'Prazer em conhecer!']]),

 7009802: dict(
    t='Na fila do embarque · Are you…?', sub='Conversando no aeroporto: pergunte com Are you…?',
    say='O Sam e a Ana esperam o voo. Será que os dois são do mesmo país?',
    hook=['Hi! Are you from Brazil?', 'Oi! Você é do Brasil?'],
    rs='airport2', cast=('Sam', 'Ana'),
    lines=[('Sam', 'Hi! Are you from Brazil?', 'Oi! Você é do Brasil?'),
           ('Ana', 'Yes, I am! Are you from Brazil too?', 'Sim, sou! Você também é do Brasil?'),
           ('Sam', "No, I'm not. I'm from Mexico.", 'Não, não sou. Sou do México.'),
           ('Ana', 'Nice! Are you a student?', 'Legal! Você é estudante?'),
           ('Sam', 'Yes, I am. Are you a teacher?', 'Sim, sou. Você é professora?'),
           ('Ana', "No, I'm not. I'm a student too!", 'Não, não sou. Também sou estudante!')],
    fact='Na resposta curta, o verbo **não encolhe**: dizemos **“Yes, I am.”**, nunca “Yes, I\'m.”. E o **from** nunca fica de fora: **I\'m from Brazil**, e não “I\'m Brazil”.',
    prompt="Você conversa com alguém no aeroporto. **Pergunte se a pessoa é do Brasil, pergunte se ela é estudante e diga de onde você é.**",
    ph="Ex.: Are you from Brazil? Are you a student? I'm from Mexico.", chips=['Are you from', 'Are you a', "I'm from"],
    model="Are you from Brazil? Are you a student? I'm from Mexico.",
    check=['Perguntei se é do Brasil?', 'Perguntei se é estudante?', 'Disse de onde eu sou?'],
    kw=[r"\bAre you\b.*\bfrom\b", r"\bAre you\s+(?:a|an)\s+\w+", I_AM + r"\s+from\s+\w+"],
    tips=[[['Are you from Brazil?', 'Você é do Brasil?'], ['Are you from Mexico?', 'Você é do México?'], ['Are you from here?', 'Você é daqui?']],
          [['Are you a student?', 'Você é estudante?'], ['Are you a teacher?', 'Você é professor(a)?'], ['Are you a tourist?', 'Você é turista?']],
          [["I'm from Mexico.", 'Sou do México.'], ["I'm from Brazil.", 'Sou do Brasil.'], ["I'm from Portugal.", 'Sou de Portugal.']]],
    ok=['Primeira pergunta! ❓', 'Segunda pergunta! 🎓', 'Agora você contou de onde é! 🌎'],
    reply=["Yes, I'm from Brazil! And yes, I'm a student. Nice to meet you!", 'Sim, sou do Brasil! E sim, sou estudante. Prazer em conhecer você!', 'Ana', '👩‍🦰'],
    recap=[['Are you from Brazil?', 'Você é do Brasil?'], ['Yes, I am.', 'Sim, sou.'], ["No, I'm not.", 'Não, não sou.'], ["I'm from Mexico.", 'Sou do México.']]),

 7070003: dict(
    t='Check-in com sono · Are you…?', sub='Chegando ao hotel: pergunte e responda com Are you…?',
    say='O Kenji chegou ao hotel depois de um voo longo. A Rosa quer saber como ele está.',
    hook=['Welcome, Kenji! Are you tired?', 'Bem-vindo, Kenji! Você está cansado?'],
    rs='lobby1', cast=('Rosa', 'Kenji'),
    lines=[('Rosa', 'Welcome, Kenji! Are you tired?', 'Bem-vindo, Kenji! Você está cansado?'),
           ('Kenji', "Yes, I am. It's a long trip.", 'Sim, estou. É uma viagem longa.'),
           ('Rosa', 'Are you hungry too?', 'Você também está com fome?'),
           ('Kenji', "No, I'm not. I'm just sleepy.", 'Não, não estou. Só estou com sono.'),
           ('Rosa', 'Are you alone?', 'Você está sozinho?'),
           ('Kenji', "No, I'm not. My friends are here too.", 'Não. Meus amigos também estão aqui.')],
    fact='Para dizer “não”, o inglês coloca **not** depois do verbo be: **I\'m not**, **he isn\'t**, **we aren\'t**. Em português, o “não” vem antes: “não estou”.',
    prompt="Você recebe um hóspede cansado no hotel. **Pergunte se a pessoa está cansada, pergunte se ela está com fome e diga que você não está.**",
    ph="Ex.: Are you tired? Are you hungry? I'm not tired.", chips=['Are you tired', 'Are you hungry', "I'm not"],
    model="Are you tired? Are you hungry? I'm not tired, I'm just happy.",
    check=['Perguntei se está cansado(a)?', 'Perguntei se está com fome?', "Disse algo com I'm not?"],
    kw=[r"\bAre you\s+(?:very |so )?tired\b", r"\bAre you\s+(?:very |so )?hungry\b", I_AM + r"\s+not\b"],
    tips=[[['Are you tired?', 'Você está cansado(a)?'], ['Are you so tired?', 'Você está tão cansado(a)?'], ['Are you very tired?', 'Você está muito cansado(a)?']],
          [['Are you hungry?', 'Você está com fome?'], ['Are you very hungry?', 'Você está com muita fome?'], ['Are you so hungry?', 'Você está com tanta fome?']],
          [["I'm not tired.", 'Não estou cansado(a).'], ["I'm not hungry.", 'Não estou com fome.'], ["I'm not sleepy.", 'Não estou com sono.']]],
    ok=['Cansaço! 😴', 'Fome! 🍽️', "Negativa com I'm not! 🙅"],
    reply=["Yes, I am a little tired, but I'm happy! Your hotel is great.", 'Sim, estou um pouco cansado, mas feliz! Seu hotel é ótimo.', 'Kenji', '🧑'],
    recap=[['Are you tired?', 'Você está cansado(a)?'], ['Are you hungry?', 'Você está com fome?'], ["I'm not hungry.", 'Não estou com fome.'], ['Yes, I am.', 'Sim, estou.']]),

 7030002: dict(
    t='A nova aluna · Is he…? Is she…?', sub='Quem é quem na escola: pergunte com Is he…? e Is she…?',
    say='Tem uma garota e um garoto novos na escola. A Ana e o Leo querem descobrir quem são.',
    hook=['Ana, who is that girl? Is she a student?', 'Ana, quem é aquela garota? Ela é estudante?'],
    rs='school', cast=('Leo', 'Ana'),
    lines=[('Leo', 'Ana, who is that girl? Is she a student?', 'Ana, quem é aquela garota? Ela é estudante?'),
           ('Ana', "Yes, she is. She's Mei. She's from China.", 'Sim, é. Ela é a Mei. Ela é da China.'),
           ('Leo', 'Is she in our class?', 'Ela está na nossa turma?'),
           ('Ana', "Yes, she is! And that boy? He isn't in our class.", 'Sim, está! E aquele garoto? Ele não está na nossa turma.'),
           ('Leo', 'Is he from Canada?', 'Ele é do Canadá?'),
           ('Ana', "No, he isn't. He's from India.", 'Não, não é. Ele é da Índia.')],
    fact='Na resposta curta, o verbo vem **inteiro**: **“Yes, she is.”**, nunca “Yes, she\'s.”. Já no “não”, a forma curta é natural: **“No, he isn\'t.”**',
    prompt="Você vê dois alunos novos na escola. **Pergunte sobre uma garota com Is she, pergunte sobre um garoto com Is he e responda com uma resposta curta.**",
    ph="Ex.: Is she from China? Is he from India? Yes, she is.", chips=['Is she', 'Is he', 'Yes, she is.'],
    model="Is she from China? Is he from India? Yes, she is. No, he isn't.",
    check=['Perguntei sobre uma garota?', 'Perguntei sobre um garoto?', 'Dei uma resposta curta?'],
    kw=[r"\bIs she\b", r"\bIs he\b", r"\b(?:yes|no)\b\W+(?:she|he|it)\s+(?:is|isn['’]t)\b"],
    tips=[[['Is she from China?', 'Ela é da China?'], ['Is she a student?', 'Ela é estudante?'], ['Is she your friend?', 'Ela é sua amiga?']],
          [['Is he from India?', 'Ele é da Índia?'], ['Is he a teacher?', 'Ele é professor?'], ['Is he your brother?', 'Ele é seu irmão?']],
          [['Yes, she is.', 'Sim, ela é.'], ["No, he isn't.", 'Não, ele não é.'], ['Yes, he is.', 'Sim, ele é.']]],
    ok=['Is she…? 👧', 'Is he…? 👦', 'Resposta curta! ✅'],
    reply=["Yes, she is, and he isn't. Great questions, detective!", 'Sim, ela é, e ele não é. Ótimas perguntas, detetive!', 'Ana', '👩‍🦰'],
    recap=[['Is she a student?', 'Ela é estudante?'], ['Is he from India?', 'Ele é da Índia?'], ['Yes, she is.', 'Sim, ela é.'], ["No, he isn't.", 'Não, ele não é.']]),

 7070004: dict(
    t='O time de futebol · Is he / she / it?', sub='No campo: pergunte com Is he…?, Is she…? e Is it…?',
    say='O Leo e a Mei olham o time de futebol da escola. Quem é o jogador novo?',
    hook=['Leo, who is that player? Is he from Argentina?', 'Leo, quem é aquele jogador? Ele é da Argentina?'],
    rs='school', cast=('Mei', 'Leo'),
    lines=[('Mei', 'Leo, who is that player? Is he from Argentina?', 'Leo, quem é aquele jogador? Ele é da Argentina?'),
           ('Leo', "Yes, he is! He's a great player.", 'Sim, é! Ele é um ótimo jogador.'),
           ('Mei', 'Is she his sister?', 'Ela é irmã dele?'),
           ('Leo', "No, she isn't. She's his coach.", 'Não, não é. Ela é a técnica dele.'),
           ('Mei', 'Is the coach from Germany?', 'A técnica é da Alemanha?'),
           ('Leo', "Yes, she is! And the ball? It isn't new.", 'Sim, é! E a bola? Ela não é nova.')],
    fact='Em inglês, **it** serve para **coisas e animais** (**it\'s new**), e **he / she** para pessoas. Por isso a bola é “it”, e não “ela”.',
    prompt="Você olha o time de futebol da escola. **Pergunte sobre um jogador com Is he, sobre uma técnica com Is she e sobre a bola com Is it.**",
    ph="Ex.: Is he from Argentina? Is she the coach? Is it new?", chips=['Is he', 'Is she', 'Is it'],
    model="Is he from Argentina? Is she the coach? Is it new?",
    check=['Perguntei sobre o jogador?', 'Perguntei sobre a técnica?', 'Perguntei sobre a bola?'],
    kw=[r"\bIs he\b", r"\bIs she\b", r"\bIs it\b"],
    tips=[[['Is he from Argentina?', 'Ele é da Argentina?'], ['Is he a good player?', 'Ele é um bom jogador?'], ['Is he your friend?', 'Ele é seu amigo?']],
          [['Is she the coach?', 'Ela é a técnica?'], ['Is she from Germany?', 'Ela é da Alemanha?'], ['Is she your sister?', 'Ela é sua irmã?']],
          [['Is it new?', 'É novo?'], ['Is it big?', 'É grande?'], ['Is it your ball?', 'É a sua bola?']]],
    ok=['Jogador! ⚽', 'Técnica! 📣', 'A bola! 🥅'],
    reply=["Yes, yes, and no! The ball isn't new, but it's great. Come and play!", 'Sim, sim e não! A bola não é nova, mas é ótima. Venha jogar!', 'Leo', '🧑‍🦱'],
    recap=[['Is he from Argentina?', 'Ele é da Argentina?'], ['Is she the coach?', 'Ela é a técnica?'], ['Is it new?', 'É novo?'], ["No, it isn't.", 'Não, não é.']]),

 7009803: dict(
    t='No balcão: seu nome, letra por letra', sub='Dar seus dados em inglês: What\'s…? It\'s…',
    say='A Mei chega ao balcão. O atendente precisa do nome, do sobrenome e da cidade dela.',
    hook=["Hello! What's your name?", 'Olá! Qual é o seu nome?'],
    rs='counter', cast=('Agent', 'Mei'),
    lines=[('Agent', "Hello! What's your name?", 'Olá! Qual é o seu nome?'),
           ('Mei', "My name is Mei. It's M-E-I.", 'Meu nome é Mei. É M-E-I.'),
           ('Agent', "Thank you. What's your last name?", 'Obrigado. Qual é o seu sobrenome?'),
           ('Mei', "It's Chen. C-H-E-N.", 'É Chen. C-H-E-N.'),
           ('Agent', "What's your city?", 'Qual é a sua cidade?'),
           ('Mei', "It's Shanghai. My city is big!", 'É Xangai. Minha cidade é grande!')],
    fact='**What\'s** é **What is** encurtado, e **It\'s** é **It is**. Ao soletrar, diga cada letra separada: **S-I-L-V-A**. Em inglês, a letra **E** se diz “i”, e a letra **I** se diz “ai”.',
    prompt="No balcão, o atendente anota seus dados. **Diga seu nome com My name is, diga seu sobrenome com It's e diga sua cidade com My city is.**",
    ph="Ex.: My name is Ana. It's Silva, S-I-L-V-A. My city is Recife.", chips=['My name is', "It's", 'My city is'],
    model="My name is Ana. It's Silva, S-I-L-V-A. My city is São Paulo.",
    check=['Disse meu nome?', 'Disse meu sobrenome?', 'Disse minha cidade?'],
    kw=[r"\bMy name(?:['’]s| is)\s+\w+", r"\bIt(?:['’]s| is)\s+[A-Za-z]", r"\bMy city(?:['’]s| is)\s+\w+"],
    tips=[[['My name is Ana.', 'Meu nome é Ana.'], ['My name is Leo.', 'Meu nome é Leo.'], ['My name is Mei.', 'Meu nome é Mei.']],
          [["It's Silva, S-I-L-V-A.", 'É Silva, S-I-L-V-A.'], ["It's Santos, S-A-N-T-O-S.", 'É Santos, S-A-N-T-O-S.'], ["It's Lima, L-I-M-A.", 'É Lima, L-I-M-A.']],
          [['My city is São Paulo.', 'Minha cidade é São Paulo.'], ['My city is Recife.', 'Minha cidade é Recife.'], ['My city is Lisbon.', 'Minha cidade é Lisboa.']]],
    ok=['Seu nome! 🪪', 'Seu sobrenome soletrado! 🔤', 'Sua cidade! 🏙️'],
    reply=['Perfect, thank you! Everything is here. Welcome!', 'Perfeito, obrigado! Está tudo aqui. Bem-vindo(a)!', 'Agent', '🧑‍💼'],
    recap=[["What's your name?", 'Qual é o seu nome?'], ['My name is Ana.', 'Meu nome é Ana.'], ["It's Silva.", 'É Silva.'], ['My city is Recife.', 'Minha cidade é Recife.']]),

 7070005: dict(
    t='O e-mail e o endereço · My / your', sub='Dar contato no hotel: What\'s your…? It\'s… My… Your…',
    say='A Mei faz o check-in. A Ana precisa do e-mail e do endereço dela.',
    hook=["Hi! What's your email, please?", 'Oi! Qual é o seu e-mail, por favor?'],
    rs='lobby1', cast=('Ana', 'Mei'),
    lines=[('Ana', "Hi! What's your email, please?", 'Oi! Qual é o seu e-mail, por favor?'),
           ('Mei', "It's mei at mail dot com.", 'É mei arroba mail ponto com.'),
           ('Ana', "Thanks! What's your address?", 'Obrigada! Qual é o seu endereço?'),
           ('Mei', 'My address is 5 Main Street.', 'Meu endereço é Main Street, 5.'),
           ('Ana', 'Perfect. This is your card, and this is your key.', 'Perfeito. Este é o seu cartão, e esta é a sua chave.'),
           ('Mei', 'Thank you! My room is great!', 'Obrigada! O meu quarto é ótimo!')],
    fact='Em inglês, **@** se diz **at** e o ponto se diz **dot**: **ana@mail.com** vira **“ana at mail dot com”**.',
    prompt="No balcão do hotel, o atendente pede seus dados. **Diga seu e-mail com It's, diga seu endereço com My address is e agradeça.**",
    ph="Ex.: It's ana at mail dot com. My address is 10 Main Street. Thank you!", chips=["It's", 'My address is', 'Thank you!'],
    model="It's ana at mail dot com. My address is 10 Main Street. Thank you!",
    check=['Disse meu e-mail?', 'Disse meu endereço?', 'Agradeci?'],
    kw=[r"\bIt(?:['’]s| is)\s+\S+\s+(?:at|@)\b|\b\S+@\S+", r"\bMy address(?:['’]s| is)\s+\w+", r"\b(?:thanks|thank you)\b"],
    tips=[[["It's ana at mail dot com.", 'É ana arroba mail ponto com.'], ["It's leo at mail dot com.", 'É leo arroba mail ponto com.'], ["It's mei at mail dot com.", 'É mei arroba mail ponto com.']],
          [['My address is 10 Main Street.', 'Meu endereço é Main Street, 10.'], ['My address is 5 Park Avenue.', 'Meu endereço é Park Avenue, 5.'], ['My address is 22 Sun Street.', 'Meu endereço é Sun Street, 22.']],
          [['Thank you!', 'Obrigado(a)!'], ['Thanks!', 'Valeu!'], ['Thank you very much!', 'Muito obrigado(a)!']]],
    ok=['E-mail! 📧', 'Endereço! 🏠', 'Educação! 🙏'],
    reply=["You're welcome! Everything is ready. Have a nice stay!", 'De nada! Está tudo pronto. Boa estadia!', 'Ana', '👩‍🦰'],
    recap=[["What's your email?", 'Qual é o seu e-mail?'], ["It's ana at mail dot com.", 'É ana arroba mail ponto com.'], ['My address is 10 Main Street.', 'Meu endereço é Main Street, 10.'], ['Thank you!', 'Obrigado(a)!']]),

 7030003: dict(
    t='A chave do quarto · Can I / Can you', sub='Pedindo com educação: Can I…? e Can you…?',
    say='O Ben chega tarde ao hotel e precisa da chave. Como pedir com educação?',
    hook=['Good evening! Can I have my room key, please?', 'Boa noite! Posso pegar a chave do meu quarto, por favor?'],
    rs='lobby2', cast=('Ben', 'Clerk'),
    lines=[('Ben', 'Good evening! Can I have my room key, please?', 'Boa noite! Posso pegar a chave do meu quarto, por favor?'),
           ('Clerk', 'Sure! Can I see your passport?', 'Claro! Posso ver o seu passaporte?'),
           ('Ben', 'Here you are. Can you help me with my bag?', 'Aqui está. Você pode me ajudar com a mala?'),
           ('Clerk', 'Of course! It is a nice room, with a view.', 'Claro! É um quarto bonito, com vista.'),
           ('Ben', 'Great! Can I have breakfast in the morning?', 'Ótimo! Posso tomar café da manhã de manhã?'),
           ('Clerk', 'Yes, you can! Breakfast is at seven.', 'Sim, pode! O café da manhã é às sete.')],
    fact='**Can I…?** pede permissão para **você** fazer algo; **Can you…?** pede que **a outra pessoa** faça. Com **please**, o pedido fica ainda mais simpático.',
    prompt="Você chega ao hotel à noite. **Peça a chave com Can I, peça ajuda com a mala com Can you e agradeça.**",
    ph="Ex.: Can I have my key, please? Can you help me with my bag? Thank you!", chips=['Can I have', 'Can you help', 'Thank you!'],
    model="Can I have my key, please? Can you help me with my bag? Thank you!",
    check=['Pedi a chave com Can I?', 'Pedi ajuda com Can you?', 'Agradeci?'],
    kw=[r"\bCan I\b", r"\bCan you\b", r"\b(?:thanks|thank you)\b"],
    tips=[[['Can I have my key, please?', 'Posso pegar a minha chave, por favor?'], ['Can I have a room, please?', 'Posso ficar com um quarto, por favor?'], ['Can I have breakfast?', 'Posso tomar café da manhã?']],
          [['Can you help me with my bag?', 'Você pode me ajudar com a mala?'], ['Can you help me, please?', 'Você pode me ajudar, por favor?'], ['Can you carry my bag?', 'Você pode carregar a minha mala?']],
          [['Thank you!', 'Obrigado(a)!'], ['Thanks a lot!', 'Muito obrigado(a)!'], ['Thank you very much!', 'Muito obrigado(a)!']]],
    ok=['Pedido educado! 🔑', 'Ajuda pedida! 🧳', 'Gentileza! 🙏'],
    reply=['Of course! Here is your key. Can I help you with anything else?', 'Claro! Aqui está a sua chave. Posso ajudar com mais alguma coisa?', 'Clerk', '🧑‍💼'],
    recap=[['Can I have my key?', 'Posso pegar a minha chave?'], ['Can you help me?', 'Você pode me ajudar?'], ['Of course!', 'Claro!'], ['Thank you!', 'Obrigado(a)!']]),

 7070006: dict(
    t='Ligando para a recepção · Can I / Can you', sub='No quarto do hotel: peça o que precisa com Can I…? e Can you…?',
    say='A Ana já está no quarto e precisa de duas coisas. Ela liga para a recepção.',
    hook=['Hello! Can I have the Wi-Fi password, please?', 'Olá! Posso ter a senha do Wi-Fi, por favor?'],
    rs='bedroom', cast=('Ana', 'Clerk'),
    lines=[('Ana', 'Hello! Can I have the Wi-Fi password, please?', 'Olá! Posso ter a senha do Wi-Fi, por favor?'),
           ('Clerk', "Sure! It's on your card.", 'Claro! Está no seu cartão.'),
           ('Ana', 'Thanks! Can you bring an extra card, please?', 'Obrigada! Você pode trazer um cartão extra, por favor?'),
           ('Clerk', 'Of course! Can I bring breakfast too?', 'Claro! Posso levar o café da manhã também?'),
           ('Ana', 'Yes, please! Can you bring it at seven?', 'Sim, por favor! Você pode trazer às sete?'),
           ('Clerk', 'Yes, I can. See you at seven!', 'Sim, posso. Até as sete!')],
    fact='Em inglês, **please** deixa qualquer pedido educado e pode ir no começo ou no fim: **Please, can I…?** ou **Can I…, please?**',
    prompt="Você liga para a recepção do hotel. **Peça a senha do Wi-Fi com Can I, peça um cartão extra com Can you e diga please.**",
    ph="Ex.: Can I have the Wi-Fi password, please? Can you bring an extra card?", chips=['Can I have', 'Can you bring', 'please'],
    model="Can I have the Wi-Fi password, please? Can you bring an extra card?",
    check=['Pedi a senha com Can I?', 'Pedi o cartão com Can you?', 'Disse please?'],
    kw=[r"\bCan I\b", r"\bCan you\b", r"\bplease\b"],
    tips=[[['Can I have the Wi-Fi password?', 'Posso ter a senha do Wi-Fi?'], ['Can I have a towel?', 'Posso ter uma toalha?'], ['Can I have water?', 'Posso ter água?']],
          [['Can you bring an extra card?', 'Você pode trazer um cartão extra?'], ['Can you bring my bag?', 'Você pode trazer a minha mala?'], ['Can you bring breakfast?', 'Você pode trazer o café da manhã?']],
          [['Please!', 'Por favor!'], ['Yes, please!', 'Sim, por favor!'], ['Can I have it, please?', 'Posso ter, por favor?']]],
    ok=['Wi-Fi pedido! 📶', 'Cartão extra! 💳', 'Please! ✨'],
    reply=['Of course! The password is on the card. I can bring the extra card now.', 'Claro! A senha está no cartão. Posso levar o cartão extra agora.', 'Clerk', '🧑‍💼'],
    recap=[['Can I have the Wi-Fi password?', 'Posso ter a senha do Wi-Fi?'], ['Can you bring an extra card?', 'Você pode trazer um cartão extra?'], ['Yes, I can.', 'Sim, posso.'], ['Please!', 'Por favor!']]),
}


def parts(prompt, count):
    bold = (re.search(r'\*\*(.+?)\*\*', prompt) or [None, ''])[1]
    ps = [p.strip() for p in re.split(r',\s*|\s+e\s+(?=[a-zà-ú])', re.sub(r'[.!?]+$', '', bold), flags=re.I) if p.strip()]
    return ps if len(ps) == count else None


def selftest(n, s):
    errs = []
    for i, rx in enumerate(s['kw']):
        r = re.compile(rx, re.I)
        if r.search(''):
            errs.append(f'{n}: kw[{i}] casa com texto vazio')
        if not r.search(s['model']):
            errs.append(f'{n}: kw[{i}] não casa com o modelo')
        for k, tip in enumerate(s['tips'][i]):
            if not r.search(tip[0]):
                errs.append(f'{n}: kw[{i}] não casa com a dica {k}: {tip[0]}')
    for i in range(len(s['kw'])):
        others = ' '.join(s['model'].split('. ')[j] for j in range(len(s['kw'])) if j != i and j < len(s['model'].split('. ')))
    if len(s['kw']) != len(s['check']) or len(s['tips']) != len(s['check']) or len(s['ok']) != len(s['check']):
        errs.append(f'{n}: check/kw/tips/ok com tamanhos diferentes')
    if not parts(s['prompt'], len(s['check'])):
        errs.append(f'{n}: o trecho em negrito da missão não tem {len(s["check"])} partes; os rótulos usarão o texto longo')
    return errs


def build(d, s, idx):
    e = d[idx]
    byk = {}
    for f in e['fr']:
        byk.setdefault(f['k'], f)
    cover = dict(byk['cover'])
    cover.update({'sub': s['sub'], 'say': s['say'], 'hook': s['hook']})
    sc0 = byk.get('scene', {})
    cast = {nm: CAST[nm] for nm in s['cast']}
    scene = {'k': 'scene', 'art': sc0.get('art') or {'s': 'street', 'items': [], 'seed': 'm2d%d' % e['n']},
             'cast': cast, 'lines': [list(x) for x in s['lines']], 'rs': s['rs']}
    cult = {'k': 'culttl', 'title': '🗣️ Você sabia?', 'pa': PA, 'fact': s['fact'], 'works': []}
    nxt = d[idx + 1] if idx + 1 < len(d) else None
    produce = {
        'k': 'produce', 'title': 'Sua vez!', 'prompt': s['prompt'], 'ph': s['ph'], 'chips': s['chips'], 'model': s['model'],
        'check': s['check'], 'kw': s['kw'], 'tips': s['tips'], 'ok': s['ok'], 'reply': s['reply'],
        'cul': ['🎤', 'Sua vez', 'Produzir é a melhor forma de lembrar: fale em voz alta e depois escreva.'],
        'then': [{'k': 'wrap', 'title': 'Para levar na mochila', 'recap': s['recap'],
                  **({'teaser': {'t': nxt['t'], 'd': nxt['fr'][0].get('sub') or ''}} if nxt else {})}],
    }
    mid = [byk[k] for k in ('rdgplay', 'rdg', 'pat') if k in byk]
    rest = [byk[k] for k in ('sbuild', 'xpr', 'scenebuild') if k in byk]
    e['t'] = s['t']
    e['fr'] = [cover, scene] + mid + [cult] + rest + [produce]


d = json.loads(subprocess.check_output(['git', 'show', ORIGINAL_REV + ':' + F]).decode('utf-8'))
pos = {x['n']: i for i, x in enumerate(d)}
errs, done = [], []
for n, s in SPECS.items():
    if n not in pos:
        continue
    errs += selftest(n, s)
    build(d, s, pos[n])
    done.append(n)
hard = [x for x in errs if 'rótulos usarão' not in x]
for x in errs:
    print('AVISO' if x not in hard else 'ERRO', x)
if hard:
    sys.exit('Corrija os erros acima; nada foi gravado.')
json.dump(d, open(F, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('ok:', len(done), 'continuações reescritas em', F)
