# Segundos episódios dos pares (59–66) reescritos com vocabulário, cena e frases próprios.
from v3.short import *
from v3.oldn import N

EPS = []
from v3.zz1_lib import full as zz1_full

# ---------------------------------------------------------------- 7030011 · this · that · The Sneetches
EPS.append(zz1_full(7030011, pattern='this · that', teaser=('Pedir uma explicação', 'Próximo: Can you repeat…? e What does … mean?')))

# ---------------------------------------------------------------- 7070022 · Can you repeat…? · What does … mean? · Fox in Socks
EPS.append(zz1_full(7070022, pattern='Can you repeat…? · What does … mean?', teaser=('Dar ordens com it', 'Próximo: put it, use it, find it.')))

# ---------------------------------------------------------------- 7910005 · verbo + it · Ramona the Pest
EPS.append(zz1_full(7910005, pattern='verbo + it', teaser=('O que é isso?', 'Próximo: It is · It’s para falar de coisas e do tempo.')))

# ---------------------------------------------------------------- 66 · It is · It's
EPS.append(E(
    n=7010152, title='It’s cold up here', sub='falar de coisas e do tempo com it is e it’s (hill, bucket, water, path, rain, cloud)',
    pattern='It is · It’s', why='Hoje você aprende a usar it is e it’s para falar de coisas, do tempo e da hora.',
    **N(7010152),
    hot=[('⛰️', 'hill', 'colina', 'It’s a big hill.', 'É uma colina grande.'),
         ('🪣', 'bucket', 'balde', 'It’s a red bucket.', 'É um balde vermelho.'),
         ('💧', 'water', 'água', 'It’s cold water.', 'É água fria.'),
         ('🛤️', 'path', 'trilha', 'It’s a long path.', 'É uma trilha longa.'),
         ('☁️', 'cloud', 'nuvem', 'It’s a black cloud.', 'É uma nuvem preta.')],
    gaps=[('___ a big hill.', 'É uma colina grande.', ['It’s', 'He’s', 'They’re'], 0, 'Para uma coisa: **it’s**.'),
          ('___ cold water.', 'É água fria.', ['It’s', 'We’re', 'I’m'], 0, 'Para uma coisa: **it’s**.'),
          ('It ___ late.', 'É tarde.', ['is', 'are', 'am'], 0, 'Com it: **is**.'),
          ('It ___ a long path.', 'Não é uma trilha longa.', ['isn’t', 'aren’t', 'don’t'], 0, 'Negativa de it is: **isn’t**.')],
    traps=[('Qual frase está certa?', ['It’s a red bucket.', 'Its a red bucket.', 'It are a red bucket.'], 0, 'it is → **it’s**, com apóstrofo.'),
           ('Qual está certa?', ['It’s cold.', 'It cold.', 'It are cold.'], 0, 'Não esqueça o verbo: **it’s cold**.')],
    rule=R(N(7010152)['ids'][0], 'It is · It’s', 'Falar de coisas, do tempo e da hora.',
           ['It’s a big hill. It’s cold. It’s late.', 'É uma colina grande. Está frio. É tarde.'],
           [([['It is', 1]], [['It’s', 3]], 'It’s', 'Na fala, **it is** vira **it’s**.'),
            ([['É uma colina.', 2]], [['It’s', 3], ['a hill.', 2]], 'It’s a hill.', 'Em inglês, a frase **sempre** tem sujeito: **it**.')],
           [('⛰️', 'It’s', 'It’s a big hill.', 'É uma colina grande.'), ('🪣', 'It’s', 'It’s a red bucket.', 'É um balde vermelho.'),
            ('💧', 'It’s', 'It’s cold water.', 'É água fria.'), ('☁️', 'It’s', 'It’s a black cloud.', 'É uma nuvem preta.')],
           [('sujeito it', 1, '**It** é o sujeito de coisas, tempo e hora: it’s cold, it’s late.', 'It’s cold.'), ('negativa', 3, 'Para negar: **it isn’t**.', 'It isn’t far.')],
           ['Em português “é frio” e “está frio”. Em inglês: **it’s cold**.']),
    cover=('It is e it’s: em 10 minutos você fala de coisas e do tempo', 'Jack e Jill sobem a colina atrás de água. É longe? Está frio? Vai chover?'),
    vocab=[('⛰️', 'hill', 'colina', 'Soa como “RÍL”.'), ('🪣', 'bucket', 'balde', 'Soa como “BÂ-quit”.'), ('💧', 'water', 'água', 'Soa como “UÓ-ter”.'),
           ('🛤️', 'path', 'trilha', 'Soa como “PÉF”.'), ('☁️', 'cloud', 'nuvem', 'Soa como “CLÁUD”.'), ('🌧️', 'rain', 'chuva', 'Soa como “RÊIN”.')],
    lines=[['Jack', 'Jill, look at the hill. It’s big!', 'Jill, olhe a colina. É grande!'],
           ['Jill', 'And it’s a long path. Take the bucket.', 'E é uma trilha longa. Leve o balde.'],
           ['Jack', 'It’s a red bucket. It isn’t heavy.', 'É um balde vermelho. Não é pesado.'],
           ['Jill', 'Look, a black cloud. It’s late, Jack.', 'Olhe, uma nuvem preta. É tarde, Jack.'],
           ['Jack', 'It’s cold up here. Is it far?', 'Está frio aqui em cima. É longe?'],
           ['Jill', 'No, it isn’t far. The water is there.', 'Não, não é longe. A água está ali.'],
           ['Jack', 'Oh no, it’s rain! It’s cold rain!', 'Ah, não, é chuva! É chuva fria!'],
           ['Jill', 'Hurry! It’s water for the bucket!', 'Rápido! É água para o balde!']],
    quiz=[('What is big?', 'O que é grande?', [('⛰️', 'The hill'), ('🪣', 'The bucket'), ('☁️', 'The cloud')], 0, 0, 'Jack diz: “Look at the hill. It’s big!”'),
          ('What color is the bucket?', 'De que cor é o balde?', [('🔴', 'Red'), ('🔵', 'Blue'), ('⚫', 'Black')], 0, 2, 'Jack diz: “It’s a red bucket.”'),
          ('Is the water far?', 'A água é longe?', [('📍', 'No, it isn’t'), ('🌍', 'Yes, it’s far'), ('🤷', 'Maybe')], 0, 5, 'Jill diz: “No, it isn’t far.”')],
    dictate=[['It’s a big hill.', 'É uma colina grande.'], ['It’s cold water.', 'É água fria.'], ['It’s late.', 'É tarde.'], ['It isn’t far.', 'Não é longe.']],
    teaser=('Ele e ela', 'Próximo: his, her e its com um vizinho novo.'),
    exps=[('🥶', 'It’s freezing.', 'Frase útil', 'Está congelando.', '**Exagera** o frio.', 'It’s freezing up here.', 'Está congelando aqui em cima.'),
          ('🌧️', 'It’s raining.', 'Frase útil', 'Está chovendo.', '**Fala** do tempo agora.', 'Oh no, it’s raining!', 'Ah, não, está chovendo!'),
          ('⏰', 'It’s late.', 'Frase útil', 'É tarde.', '**Avisa** da hora.', 'It’s late. Let’s go.', 'É tarde. Vamos.'),
          ('🏃', 'Hurry up!', 'Frase útil', 'Depressa!', '**Apressa** alguém.', 'Hurry up, Jack!', 'Depressa, Jack!')],
    exp_scene=[['Jack', 'Wow, it’s a big hill!', 'Uau, é uma colina grande!'],
               ['Jill', '**It’s late.** Take the bucket.', 'É tarde. Leve o balde.'],
               ['Jack', '**It’s freezing** up here.', 'Está congelando aqui em cima.'],
               ['Jill', 'Look, a black cloud.', 'Olhe, uma nuvem preta.'],
               ['Jack', 'Oh no, **it’s raining!**', 'Ah, não, está chovendo!'],
               ['Jill', '**Hurry up!** The water is near.', 'Depressa! A água está perto.'],
               ['Jack', 'It isn’t far now.', 'Não é longe agora.'],
               ['Jill', 'Good. Let’s go home.', 'Bom. Vamos para casa.']],
    lab=dict(short='ts', title='Laboratório de sons: it’s e its', say='It’s e its soam igual! Vamos ouvir?',
             what='**it’s** (it is) e **its** (dele) soam iguais: **“ÍTS”**. O apóstrofo só aparece na escrita.',
             how='Diga “ÍTS” com o s final bem claro.', pt='Em português não terminamos palavras com ts. Solte o s no fim.',
             ex=[('it’s', 'ÍTS', 'é', 'it is'), ('its', 'ÍTS', 'dele (coisa)', 'posse'), ('hill', 'RÍL', 'colina', 'h aspirado')],
             pairs=[('it’s', 'its', 'iguais'), ('hill', 'ill', 'rríl × íl'), ('cold', 'called', 'cóuld × cóld')],
             tip='Termine com um s leve em it’s.', phrase=['It’s a hill.', 'É uma colina.'],
             rounds=[('it’s', ['it’s', 'its'], 0, '**it’s** e its soam igual.'), ('hill', ['hill', 'ill'], 0, '**hill** começa com h.'), ('cold', ['cold', 'called'], 0, '**cold** soa CÓULD.')]),
    verbs=('Verbos da subida', 'Quatro verbos: go, take, carry e fill.',
           [('go', '🚶', 'ir', 'I go up the hill.', 'He go**es** up the hill.', 'Jack goes up the path.', 'O Jack sobe pela trilha.', '**go** = ir. Com he/she: **goes**.'),
            ('take', '🪣', 'levar', 'I take the bucket.', 'She take**s** the bucket.', 'Jill takes the bucket.', 'A Jill leva o balde.', '**take** = levar. Com he/she: **takes**.'),
            ('carry', '💪', 'carregar', 'I carry the water.', 'He carr**ies** the water.', 'Jack carries the bucket.', 'O Jack carrega o balde.', '**carry** = carregar. Com he/she: **carries**.'),
            ('fill', '💧', 'encher', 'I fill the bucket.', 'She fill**s** the bucket.', 'Jill fills it with water.', 'A Jill enche com água.', '**fill** = encher. Com he/she: **fills**.')]),
    mold=[('Com it’s', [('começo', [['It’s a', 'é um'], ['It’s a big', 'é um grande'], ['It’s a long', 'é um longo']]), ('coisa', [['hill', 'colina'], ['bucket', 'balde'], ['path', 'trilha'], ['cloud', 'nuvem']])], '.'),
          ('Tempo e hora', [('começo', [['It’s cold', 'está frio'], ['It’s late', 'é tarde'], ['It’s raining', 'está chovendo']]), ('fim', [['', ''], [' up here', ' aqui em cima'], [' now', ' agora']])], '.'),
          ('Negar', [('começo', [['It isn’t far', 'não é longe'], ['It isn’t heavy', 'não é pesado'], ['It isn’t late', 'não é tarde']]), ('fim', [['', ''], [', Jack', ', Jack']])], '.')],
    speak=[['It’s a big hill.', 'É uma colina grande.'], ['It isn’t far.', 'Não é longe.']],
    produce=dict(ic='⛰️', name='It is ou it’s?', desc='Use it’s e it isn’t', prompt='Você sobe a colina. **Diga que é uma colina grande, que está frio e que não é longe.**',
                 ph='Ex.: It’s a big hill. It’s cold. It isn’t far.', chips=['It’s a big hill'],
                 model='It’s a big hill. It’s cold. It isn’t far.', check=['Usei it’s para a colina?', 'Usei it’s cold?', 'Usei it isn’t?'],
                 kw=[r"\bit['’]?s\s+a\s+(big\s+)?hill\b", r"\bit['’]?s\s+cold\b", r"\bit\s+isn['’]?t\b|\bit\s+is\s+not\b"],
                 tips=[[['It’s a big hill.', 'É uma colina grande.']], [['It’s cold.', 'Está frio.']], [['It isn’t far.', 'Não é longe.']]],
                 ok=['Hill! ⛰️', 'Cold! 🥶', 'Near! 📍'], reply=['Hurry up!', 'Depressa!']),
    mission2=dict(ic='🌧️', name='Vai chover', desc='Use It’s raining e Hurry up', prompt='O céu escurece. **Diga que é tarde, que está chovendo e peça para ir depressa.**',
                  chips=['It’s raining'], model='It’s late. It’s raining! Hurry up!', check=['Disse It’s late?', 'Disse It’s raining?', 'Disse Hurry up?'],
                  kw=[r"\bit['’]?s\s+late\b", r"\bit['’]?s\s+raining\b|\bit\s+is\s+raining\b", r"\bhurry\b"],
                  tips=[[['It’s late.', 'É tarde.']], [['It’s raining!', 'Está chovendo!']], [['Hurry up!', 'Depressa!']]],
                  ok=['Late! ⏰', 'Rain! 🌧️', 'Hurry! 🏃'], reply=['Run home!', 'Corra para casa!']),
    scenes=['park2', 'lake', 'yard', 'park', 'street', 'cafe2']))
