#!/usr/bin/env python3
"""Redesenho do episódio 1 do inglês (en-a1, id 9801 "Hello, New York!").

Base: o episódio autoral original (commit f7a5b55), cujo conteúdo foi trocado por falas genéricas
("Today, we are talking about this situation.") e ícones aleatórios pelos scripts de densidade. Restaura o que
era bom (cena, leitura, vocabulário com ícones certos, verbos reais, sons do "h", situações, conversa e produção)
e amplia com conteúdo novo: cena de 12 falas, leitura de 12 frases, 2 rodadas de som, 4ª pergunta do quiz,
linha do tempo com 3 marcos (poema, estátua, Ellis Island) e fechamento com as frases do diálogo.
"""
import copy, json, os, subprocess

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
FILE = 'en-a1_01.json'
ORIG = 'f7a5b55'


def orig_frames():
    d = json.loads(subprocess.check_output(['git', 'show', '%s:data/%s' % (ORIG, FILE)]))
    e = next(x for x in d if x['n'] == 9801)
    return {x['k']: x for x in e['fr']}


SCENE_NEW = [
    ['Mia', 'Look! A yellow taxi!', 'Olhe! Um táxi amarelo!'],
    ['Sam', 'Taxi! Over here!', 'Táxi! Aqui!'],
    ['Mia', 'It stops! Hi! To the hotel, please.', 'Ele parou! Oi! Para o hotel, por favor.'],
    ['Sam', "Let's go. This is your first day in New York!", 'Vamos. Este é o seu primeiro dia em Nova York!'],
    ['Mia', 'I love it! Thank you, Sam.', 'Eu adoro! Obrigada, Sam.'],
]
READ_NEW = [
    ['“Thank you, Sam!” says Mia.', '“Obrigada, Sam!”, diz a Mia.'],
    ['A {{bus}} goes by, but they take the taxi.', 'Um ônibus passa, mas eles pegam o táxi.'],
    ['Mia smiles. It is her first day in New York.', 'A Mia sorri. É o primeiro dia dela em Nova York.'],
]
LPLAY_NEW = [
    {'t': 'w', 'say': 'hat', 'opts': ['at', 'hat'], 'a': 1,
     'why': '“hat” (chapéu) começa com um sopro de ar, “hhh”; “at” começa direto na vogal.'},
    {'t': 'p', 'say': 'hand', 'opts': [['✋', 'hand'], ['🐟', 'fish'], ['🌳', 'tree']], 'a': 0, 'pt': 'mão'},
]
WRAP = [
    ['Hi! I’m Sam. Welcome to New York!', 'Oi! Eu sou o Sam. Bem-vinda a Nova York!'],
    ['Nice to meet you.', 'Prazer em conhecer você.'],
    ['How’s it going? — Not bad!', 'E aí, tudo bem? — Nada mal!'],
    ['Let’s have coffee first.', 'Primeiro vamos tomar um café.'],
    ['Here is a map of the street.', 'Aqui está um mapa da rua.'],
    ['Taxi! Over here!', 'Táxi! Aqui!'],
]
TIMELINE = [
    {'n': 'The New Colossus', 'k': '📜 Poema', 'y': 1883,
     'd': 'Soneto de Emma Lazarus, escrito em 1883 para arrecadar fundos para o pedestal da Estátua da Liberdade. Nele, a própria estátua dá boas-vindas a quem chega.',
     't': 'main work'},
    {'n': 'Statue of Liberty', 'k': '🗽 Monumento', 'y': 1886,
     'd': 'Presente da França aos Estados Unidos, projetada por Bartholdi e inaugurada em 1886 na entrada do porto de Nova York.',
     't': 'context'},
    {'n': 'Ellis Island', 'k': '🚢 Lugar', 'y': 1892,
     'd': 'Ilha ao lado da estátua onde funcionou o centro de imigração de 1892 a 1954. Milhões de pessoas passaram por lá ao chegar a Nova York.',
     't': 'context'},
]


def main():
    p = os.path.join(ROOT, FILE)
    data = json.load(open(p, encoding='utf-8'))
    e = next(x for x in data if x['n'] == 9801)
    o = orig_frames()
    cur = {x['k']: x for x in e['fr']}
    idx = {x['k']: i for i, x in enumerate(e['fr'])}

    def put(k, new):
        keep = {q: v for q, v in cur[k].items() if q in ('coach', 'levelProgression', 'banner')}
        for q, v in keep.items():
            new.setdefault(q, v)
        e['fr'][idx[k]] = new

    scene = copy.deepcopy(o['scene'])
    scene['lines'] += copy.deepcopy(SCENE_NEW)
    scene['full'] = copy.deepcopy(scene['lines'])
    put('scene', scene)

    rd = copy.deepcopy(o['read'])
    rd['s'] += copy.deepcopy(READ_NEW)
    put('read', rd)

    lp = copy.deepcopy(o['lplay'])
    lp['rounds'] += copy.deepcopy(LPLAY_NEW)
    put('lplay', lp)

    for k in ('words', 'wsent', 'verbs', 'vplay', 'ctxv', 'tdlg'):
        put(k, copy.deepcopy(o[k]))

    pr = copy.deepcopy(o['produce'])
    pr['chips'] = ['Hi!', 'How’s it going?', 'It’s my first time in New York.']
    put('produce', pr)

    dq = copy.deepcopy(cur['dquiz'])
    dq['lines'] = copy.deepcopy(scene['lines'])
    dq['cast'] = copy.deepcopy(scene['cast'])
    if len(dq['items']) == 3:
        dq['items'].append({'q': 'How do they go to the hotel?', 'pt': 'Como eles vão até o hotel?',
                            'opts': [['🚕', 'By taxi'], ['🚌', 'By bus'], ['🚶', 'On foot']], 'a': 0, 'line': 8,
                            'why': 'Sam diz: “Taxi! Over here!”'})
    e['fr'][idx['dquiz']] = dq

    # cultura: o poema fica no quadro de cena; as frases da história saem dele
    cc = cur['cultcena']
    cc['lines'] = [l for l in cc['lines'] if l[1] == 'Estátua da Liberdade']
    cur['cultob']['kind'] = 'Poema'

    tl = cur['culttl']
    tl['works'] = copy.deepcopy(TIMELINE)
    tl['title'] = 'Linha do tempo: do poema ao porto'

    wr = cur['wrap']
    wr['recap'] = copy.deepcopy(WRAP)
    wr['teaser']['d'] = 'Next: Where Are You From?'

    br = cur['bridge']
    br['kind'] = '📜 Poema'
    br['why'] = ('Você acabou de conhecer **The New Colossus**, o poema que dá boas-vindas a quem chega a Nova York. '
                 'Agora vamos usar a mesma ideia, **welcome**, em situações do dia a dia.')
    br['from'] = ['Glows world-wide **welcome**', 'Brilha uma acolhida mundial']
    br['to'] = ['**Welcome** to New York!', 'Bem-vinda a Nova York!']
    br['words'] = ['Hi', 'Coffee', 'Taxi', 'Map', 'Street', 'bus']
    br['cast'] = ['Mia', 'Sam']
    br['tail'] = ('O poema diz **welcome** para quem chega ao porto; o Sam diz **Welcome to New York!** para a Mia. '
                  'É a mesma palavra, só que agora na vida real.')
    e['a'] = {'k': '📜 Poema', 'w': 'The New Colossus', 'y': '1883',
              'd': 'Soneto de Emma Lazarus que dá boas-vindas a quem chega a Nova York.'}

    open(p, 'w', encoding='utf-8').write(json.dumps(data, ensure_ascii=False, separators=(',', ':')))
    print('episódio 9801 redesenhado:', len(e['fr']), 'quadros')


if __name__ == '__main__':
    main()
