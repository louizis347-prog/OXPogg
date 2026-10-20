"""Protótipo da continuação (en-a1, episódio 7009801 "Eu sou → I'm") no modelo aprovado:
gancho de situação, uma história com os mesmos personagens, menos exercícios e fecho com "Sua vez".
Uso: python3 tools/proto_a1_cont.py   (reescreve o episódio em data/en-a1_01.json; rode a partir da raiz)"""
import json
import subprocess

F = 'data/en-a1_01.json'
# parte sempre do episódio original (antes do protótipo), para o script poder rodar de novo
ORIGINAL_REV = 'f170c43'
d = json.loads(subprocess.check_output(['git', 'show', ORIGINAL_REV + ':' + F]).decode('utf-8'))
e = next(x for x in d if x['n'] == 7009801)
old = {i: f for i, f in enumerate(e['fr'])}
byk = {}
for f in e['fr']:
    byk.setdefault(f['k'], f)

nxt = d[[x['n'] for x in d].index(7009801) + 1]  # próximo original: destino do "Próxima parada"

# 1) abertura: gancho de situação (Mia chega ao hotel e precisam saber quem ela é)
cover = dict(byk['cover'])
cover.update({
    'sub': 'Quem é você? Em 10 minutos você se apresenta em inglês',
    'say': 'A Mia acabou de chegar ao hotel. O recepcionista pergunta quem ela é. E agora?',
    'hook': ['Good evening! Welcome to the hotel. And you are…?',
             'Boa noite! Bem-vinda ao hotel. E você é…?'],
})

# 2) a história: mesmos personagens do episódio, no saguão do hotel
scene = {
    'k': 'scene',
    'art': {'s': 'street', 'items': [], 'seed': 'm2d70098'},
    'cast': {'Dan': ['🧑‍💼', '#7C4DFF'], 'Mia': ['👩', '#FF6F59']},
    'lines': [
        ['Dan', 'Good evening! Welcome to the hotel. And you are…?', 'Boa noite! Bem-vinda ao hotel. E você é…?'],
        ['Mia', "Hi! I'm Mia. I'm from Brazil.", 'Oi! Eu sou a Mia. Sou do Brasil.'],
        ['Dan', "Nice to meet you, Mia! I'm Dan.", 'Prazer, Mia! Eu sou o Dan.'],
        ['Mia', "Nice to meet you, Dan. I'm a little tired. It's a long flight!", 'Prazer, Dan. Estou um pouco cansada. É um voo longo!'],
        ['Dan', 'No problem! Your room is ready.', 'Sem problema! Seu quarto está pronto.'],
        ['Mia', "Great! I'm not hungry, just sleepy.", 'Ótimo! Não estou com fome, só com sono.'],
    ],
    'rs': 'lobby1',
}

# 3) um respiro de cultura ligado à regra (no lugar da obra do episódio anterior)
cult = dict(byk['culttl'])
cult.update({
    'title': '🗣️ Você sabia?',
    'fact': 'Na fala de todo dia, quase ninguém diz **I am** inteiro: o normal é **I\'m**. O “I am” completo soa enfático, como em **“I AM tired!”** (eu estou MESMO cansada).',
    'works': [],
})

# 4) fecho: "Sua vez" com o personagem respondendo (mesmo molde dos originais)
produce = {
    'k': 'produce',
    'title': 'Sua vez!',
    'prompt': "No hotel, o recepcionista pergunta quem você é. **Diga seu nome com I'm, diga de onde você é e diga como você está.**",
    'ph': "Ex.: Hi! I'm Ana. I'm from Brazil. I'm a little tired.",
    'chips': ["Hi! I'm", "I'm from", "I'm a little"],
    'model': "Hi! I'm Ana. I'm from Brazil. I'm a little tired, but happy to be here.",
    'check': ["Disse meu nome com I'm?", 'Disse de onde eu sou?', 'Disse como eu estou?'],
    'kw': [
        r"\bI(?:['’]m| am)\s+(?!(?:from|a|an|the|not|very|so|really|fine|good|great|tired|hungry|happy|ok|okay|sleepy|excited|nervous|cold|hot|well|sad|busy)\b)[a-zà-ú]+|\bmy name is\s+\w+",
        r"\bfrom\s+\w+",
        r"\bI(?:['’]m| am)\s+(?:very |so |really |a little |a bit )?(?:fine|good|great|tired|hungry|happy|ok|okay|sleepy|excited|nervous|cold|hot|well|sad|busy)\b|\bnot bad\b",
    ],
    'tips': [
        [["Hi! I'm Ana.", 'Oi! Eu sou a Ana.'], ["Hello, I'm Leo.", 'Olá, eu sou o Leo.'], ["Hey! I'm Mia.", 'E aí! Eu sou a Mia.']],
        [["I'm from Brazil.", 'Eu sou do Brasil.'], ["I'm from São Paulo.", 'Eu sou de São Paulo.'], ["I'm from Portugal.", 'Eu sou de Portugal.']],
        [["I'm a little tired.", 'Estou um pouco cansada.'], ["I'm fine, thanks.", 'Estou bem, obrigada.'], ["I'm so happy to be here!", 'Estou muito feliz de estar aqui!']],
    ],
    'ok': ["Nome com I'm! 🙋", 'Você disse de onde é! 🌎', 'E como você está! 😄'],
    'reply': ["Welcome, and nice to meet you! I'm Dan, at the front desk. Your room is ready. Rest well!",
              'Bem-vindo(a) e prazer! Eu sou o Dan, da recepção. Seu quarto está pronto. Descanse bem!',
              'Dan', '🧑‍💼'],
    'cul': ['🎤', 'Sua vez', 'Produzir é a melhor forma de lembrar: fale em voz alta e depois escreva.'],
    'then': [{
        'k': 'wrap',
        'title': 'Para levar na mochila',
        'recap': [["I'm Mia.", 'Eu sou a Mia.'], ["I'm from Brazil.", 'Eu sou do Brasil.'],
                  ["I'm a little tired.", 'Estou um pouco cansada.'], ['Nice to meet you!', 'Prazer em conhecer você!']],
        'teaser': {'t': nxt['t'], 'd': nxt['fr'][0].get('sub') or ''},
    }],
}

e['t'] = 'Quem é você? · I\'m'
e['fr'] = [cover, scene, old[2], old[3], cult, old[4], old[9], old[12], produce]
json.dump(d, open(F, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('ok:', len(e['fr']), 'quadros; antes:', len(old), '| títulos dos quadros:', [f['k'] for f in e['fr']])
