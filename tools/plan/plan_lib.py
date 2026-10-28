"""Plano por episódio dos cursos regulares: o que cada episódio vai ensinar, mapeado ANTES de escrever o conteúdo.

Cada entrada guarda foco/padrão (gs), obra cultural, 4 verbos, 4 expressões e os 19 quadros já formatados (vazios), de acordo com o contrato
`tools/audit/regular_pilot_contract.py`. Os dados vêm de `tools/plan/map/<curso>_*.json` (escritos à mão) e a âncora (n, ordem, título atual) vem de data/.
"""
import glob, json, os, re, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXPECTED = ['cover', 'review', 'hotscene', 'pgscene', 'pgsheet', 'pgrule', 'pgmold', 'pgsheet', 'verbs', 'vplay', 'pgexp', 'pgscene',
            'pgsheet', 'pgsheet', 'pglab', 'pgsheet', 'pgspeak', 'pgmission', 'wrap']

# O que cada quadro exige (o contrato verifica contagens; o resto é o formato do modelo dos episódios 2–5).
QUADROS = [
    ('cover', 'Capa', {'sub': 'contém "em 10 minutos você …"', 'obra': 'obra do episódio', 'say': 'abertura falada'}),
    ('review', 'Mochila de revisão', {'auto': 'gerada do episódio anterior (fix_mechanical.py); única retomada permitida'}),
    ('hotscene', 'Explore a cena', {'hot': 5, 'campos': 'e, x, y, en, pt, say, sayPt', 'obra': '5 objetos ligados à cena'}),
    ('pgscene', 'Cena 1', {'falas': 8, 'personagens': 2, 'obs': 'usa o padrão (gs) várias vezes'}),
    ('pgsheet', 'Você entendeu?', {'itens': 3}),
    ('pgrule', 'Regra do padrão', {'rule': 'head, sub, usos', 'q': 4}),
    ('pgmold', 'Molde de frases', {'paginas': 3}),
    ('pgsheet', 'Palavras da cena', {'itens': 6, 'obs': 'exatamente 6 palavras'}),
    ('verbs', 'Verbos do episódio', {'itens': 4, 'preenchido': 'verbos do plano', 'quiz': 4}),
    ('vplay', 'Missão dos verbos', {'itens': 4}),
    ('pgexp', 'Expressões e gírias', {'itens': 4, 'preenchido': 'expressões do plano', 'quiz': 4}),
    ('pgscene', 'Cena 2: na conversa de verdade', {'falas': '8 (A1/A2: 6+)', 'obs': 'mostra as 4 expressões em uso'}),
    ('pgsheet', 'Complete as falas', {'itens': 6}),
    ('pgsheet', 'Qual está certa?', {'itens': 4}),
    ('pglab', 'Laboratório de sons', {'sons': 3, 'desafios': 3}),
    ('pgsheet', 'Caça-sons', {'itens': 5}),
    ('pgspeak', 'Sua vez de falar', {'itens': 5}),
    ('pgmission', 'Missão: sua vez!', {'missoes': 3, 'primeira': 'Cena da obra'}),
    ('wrap', 'Para levar', {'recap': 4, 'teaser': 'título do próximo episódio', 'sticker': 'obra do episódio'}),
]


def fold(s):
    """minúsculas sem acento (á→a, ñ→n) e só letras/números separados por espaço."""
    s = unicodedata.normalize('NFKD', (s or '').lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


def norm(s):
    s = fold((s or '').split(':')[0])
    s = re.sub(r'^(the|a|an|el|la|los|las|un|una|le|les|il|der|die|das|o|os|as)\s+', '', s)
    return s.replace(' ', '')


def quadros_vazios(verbos=None, expressoes=None, obra=None):
    out = []
    for i, (k, titulo, exige) in enumerate(QUADROS, 1):
        q = {'ordem': i, 'k': k, 'titulo': titulo, 'estado': 'vazio'}
        if k == 'verbs' and verbos:
            q['verbos'] = list(verbos); q['estado'] = 'mapeado'
        if k == 'pgexp' and expressoes:
            q['expressoes'] = list(expressoes); q['estado'] = 'mapeado'
        if k in ('cover', 'wrap') and obra:
            q['obra'] = obra.get('nome'); q['estado'] = 'mapeado'
        if k == 'review':
            q['estado'] = 'auto'
        out.append(q)
    return out


def load_course(course):
    eps = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', course + '_*.json'))):
        eps += json.load(open(f, encoding='utf-8'))
    eps.sort(key=lambda e: e['o'])
    return eps


def obra_of(e):
    for fr in e.get('fr', []):
        if fr.get('k') == 'wrap' and fr.get('sticker'):
            return fr['sticker']['sub'].split(' · ')[0].strip()
    return (e.get('a') or {}).get('w')


def read_maps(course):
    m = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'tools', 'plan', 'map', course + '_*.json'))):
        for x in json.load(open(f, encoding='utf-8')):
            m[x['n']] = x
    return m


def build(course):
    eps = load_course(course)
    maps = read_maps(course)
    entries = []
    for i, e in enumerate(eps, 1):
        m = maps.get(e['n'])
        done = e.get('presentation') == 'regular-pilot-v1'
        ent = {'pos': i, 'n': e['n'], 'titulo_atual': e.get('t'), 'tema_atual': e.get('s'), 'par': i % 2 == 0, 'estado': 'pronto' if done else 'a mapear'}
        if done:
            fr = {}
            for f in e['fr']:
                fr.setdefault(f['k'], []).append(f)
            ent['gs'] = e.get('gs')
            ent['obra'] = {'nome': obra_of(e)}
            ent['verbos'] = [v.get('v') for v in (fr.get('verbs') or [{}])[0].get('items', [])]
            ent['expressoes'] = [x.get('en') for x in (fr.get('pgexp') or [{}])[0].get('items', [])]
        elif m:
            ent['estado'] = 'mapeado'
            ent['foco'] = m.get('foco')
            ent['gs'] = m.get('gs')
            ent['obra'] = m.get('obra')
            ent['verbos'] = m.get('verbos')
            ent['expressoes'] = m.get('expressoes')
            ent['quadros'] = quadros_vazios(m.get('verbos'), m.get('expressoes'), m.get('obra'))
        else:
            ent['quadros'] = quadros_vazios()
        entries.append(ent)
    return {'curso': course, 'episodios': len(entries), 'contrato': 'tools/audit/regular_pilot_contract.py',
            'modelo_quadros': [{'ordem': i, 'k': k, 'titulo': t, 'exige': ex} for i, (k, t, ex) in enumerate(QUADROS, 1)], 'entradas': entries}
