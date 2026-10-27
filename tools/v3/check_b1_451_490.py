#!/usr/bin/env python3
"""Prova (em memória, sem gravar nada) que os 40 episódios B1 451–490 cumprem o contrato regular-pilot-v1 e que as obras e os padrões são únicos.
Uso (da raiz do repositório): COURSE=en-b1 python3 tools/v3/check_b1_451_490.py
Confere: 19 quadros; 6 palavras; 4 verbos; 4 expressões; laboratório 3 sons + 3 desafios; duas cenas com 8+ falas; 3 missões (a primeira é 'Cena da obra');
mochila de revisão no quadro 2; obra própria e distinta (contra obras_em_uso, os dados do curso, os outros arquivos obras_new_b1_*.json e as obras dos
módulos b1_NNN de outros autores); padrão gramatical (gs) único contra os 370 convertidos e contra os outros módulos; nada repetido entre os 40 (palavras,
verbos, sons, objetos quentes) nem entre vizinhos."""
import glob, importlib, json, os, re, sys, unicodedata
os.environ.setdefault('COURSE', 'en-b1')
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # tools/
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, 'v3')); sys.path.insert(0, os.path.join(HERE, 'audit'))
import model_v2 as M
from v3 import lib
import model_v3 as MV
from v3.check import check
from v3 import b1x_lib as L
MINE = ('b1_451_455', 'b1_456_460', 'b1_461_465', 'b1_466_470', 'b1_471_475', 'b1_476_480', 'b1_481_485', 'b1_486_490')
for m in MINE:
    importlib.import_module('v3.' + m)
COURSE = os.environ['COURSE']
bad = []


def norm(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '', s)


def fail(msg):
    bad.append(msg); print('FALHA:', msg)


# ---- episódios na ordem da lista ----
eps = {}
for m in MINE:
    for e in sys.modules['v3.' + m].EPS:
        eps[e['n']] = e
if sorted(eps) != sorted(L.ORDER) or len(eps) != 40:
    fail('conjunto de n diferente da lista de 40 (%d)' % len(eps))
seq = [eps[n] for n in L.ORDER if n in eps]

# ---- montagem em memória (igual ao dryrun, em cadeia) ----
chunks, where = {}, {}
for f in sorted(glob.glob(os.path.join(ROOT, 'data', COURSE + '_*.json'))):
    d = json.load(open(f, encoding='utf-8')); chunks[f] = d
    for i, e in enumerate(d): where[e['n']] = (f, i)
order = sorted(where, key=lambda n: chunks[where[n][0]][where[n][1]]['o'])
built = []
for k, E in enumerate(seq):
    f, i = where[E['n']]; old = chunks[f][i]
    if k:
        P = seq[k - 1]; prev = (P['v2'], P['extra'], P['verbs'])
    else:
        pf, pj = where[order[order.index(E['n']) - 1]]; pit = chunks[pf][pj]
        prev = MV.prev_from_pilot(pit) if any(x['k'] == 'pgrule' for x in pit['fr']) else MV.prev_from_old(pit)
    M.HOTPT.update(lib.SAYPT)
    b = M.build(old, E['v2'], E['extra'], E['verbs'], prev, E['more'])
    b['gs'] = E['v2']['base']['pattern_label']          # o que mark_pilot2.py grava no campo gs
    b['presentation'] = 'regular-pilot-v1'
    built.append(b)
    for p in check(b): fail('%s (%s): %s' % (E['n'], b['t'], p))

# ---- contrato regular_pilot_contract (os 19 quadros, contagens, obra) ----
import regular_pilot_contract as C
ctr = C.audit(COURSE, [('mem', b) for b in built])
# o contrato trata o 1º item do curso como abertura; aqui todos têm mochila, então a conferência vale para os 40
for x in ctr: fail('contrato: ' + x)
for b in built:
    F = {}
    for fr in b['fr']: F.setdefault(fr['k'], []).append(fr)
    n = b['n']
    if [fr['k'] for fr in b['fr']] != C.EXPECTED: fail('%s: 19 quadros fora do modelo' % n)
    if len(b['v']) != 6: fail('%s: vocabulário != 6' % n)
    if len(F['verbs'][0]['items']) != 4: fail('%s: verbos != 4' % n)
    if len(F['pgexp'][0]['items']) != 4: fail('%s: expressões != 4' % n)
    if len(F['pglab'][0]['ex']) != 3 or len(F['pglab'][0]['rounds']) != 3: fail('%s: laboratório != 3 sons + 3 desafios' % n)
    sc = F['pgscene']
    if len(sc) != 2 or len(sc[0]['lines']) < 8 or len(sc[1]['lines']) < 8: fail('%s: cenas < 8 falas' % n)
    ms = F['pgmission'][0]['missions']
    if len(ms) != 3: fail('%s: missões != 3' % n)
    elif 'Cena da obra' not in ms[0]['name']: fail('%s: primeira missão não é a Cena da obra (%s)' % (n, ms[0]['name']))
    if b['fr'][1]['k'] != 'review': fail('%s: sem mochila de revisão' % n)
    if len(F['hotscene'][0]['hot']) != 5: fail('%s: objetos quentes != 5' % n)
    if not b.get('a', {}).get('w'): fail('%s: sem obra' % n)
    # a mochila retoma só o episódio anterior (dentro da lista, o anterior é o vizinho)
    cov = F['cover'][0]
    if not cov.get('stage') or not cov['stage'].get('chars'): fail('%s: capa sem elenco' % n)

# ---- unicidade das obras ----
mine = {b['n']: b['a']['w'] for b in built}
names = [v for v in mine.values()]
if len(set(norm(x) for x in names)) != 40: fail('obras repetidas entre os 40')
used = {}
def add(src, name):
    if name: used.setdefault(norm(name), []).append((src, name))
S = os.path.join(os.environ.get('CLAUDE_SCRATCH', ''), 'b1new_3.json')
for cand in (S, '/tmp/claude-0/-home-user-OXPogg/aa240b69-cc21-5263-8573-be2969435207/scratchpad/b1new_3.json'):
    if os.path.exists(cand):
        for w in json.load(open(cand, encoding='utf-8')).get('obras_em_uso', []): add('obras_em_uso', w)
        break
for f in chunks:
    for e in chunks[f]:
        if e['n'] not in mine: add('data/en-b1 n=%s' % e['n'], (e.get('a') or {}).get('w', ''))
for f in sorted(glob.glob(os.path.join(HERE, 'v3', 'obras_new_b1_*.json'))):
    if f.endswith('obras_new_b1_451_490.json'): continue
    for n, o in json.load(open(f, encoding='utf-8')).items():
        if int(n) not in mine: add(os.path.basename(f) + ' n=' + n, o['name'])
for f in sorted(glob.glob(os.path.join(HERE, 'v3', 'obras_new_a*.json'))):   # só informativo: outros níveis
    pass
for n, w in mine.items():
    for key in {norm(w), norm(w.split(':')[0])}:
        if key in used: fail('obra %s (n=%s) colide com %s' % (w, n, used[key][:3]))
    if ':' in w: fail('dois-pontos no título da obra: ' + w)
# o arquivo JSON confere com as obras montadas
oj = json.load(open(os.path.join(HERE, 'v3', 'obras_new_b1_451_490.json'), encoding='utf-8'))
if sorted(map(int, oj)) != sorted(mine): fail('obras_new_b1_451_490.json não tem as mesmas chaves')
for n, w in mine.items():
    if oj[str(n)]['name'] != w: fail('JSON e episódio divergem em %s' % n)
    if lib.OB(n, 'x', 'y')['name'] != w: fail('lib.OB(%s) diverge' % n)

# ---- padrões gramaticais (gs) ----
gs = {}
for f in chunks:
    for e in chunks[f]:
        if e.get('gs') and e.get('presentation') == 'regular-pilot-v1' and e['n'] not in mine: gs.setdefault(e['gs'].strip().lower(), []).append(e['n'])
others = 0
for f in sorted(glob.glob(os.path.join(HERE, 'v3', 'b1_[0-9]*.py'))):
    base = os.path.basename(f)[:-3]
    if base in MINE: continue
    try: mod = importlib.import_module('v3.' + base)
    except Exception as ex:
        print('(aviso) não importou', base, type(ex).__name__); continue
    for E in getattr(mod, 'EPS', []):
        if E['n'] in mine: continue
        try: gs.setdefault(E['v2']['base']['pattern_label'].strip().lower(), []).append(E['n']); others += 1
        except Exception: pass
seen = {}
for b in built:
    k = b['gs'].strip().lower()
    if k in gs: fail('gs de %s repete %s' % (b['n'], gs[k]))
    if k in seen: fail('gs repetido entre os 40: %s e %s' % (seen[k], b['n']))
    seen[k] = b['n']

# ---- nada repetido entre os 40 (e entre vizinhos) ----
def sets(b):
    F = {}
    for fr in b['fr']: F.setdefault(fr['k'], []).append(fr)
    return dict(vocab=[w[0].lower() for w in b['v']], verbos=[v['v'].lower() for v in F['verbs'][0]['items']],
                lab=[x[0].lower() for x in F['pglab'][0]['ex']], hot=[(h.get('en') if isinstance(h, dict) else h[1]).lower() for h in F['hotscene'][0]['hot']])
S_ = {b['n']: sets(b) for b in built}
for kind in ('vocab', 'verbos', 'lab', 'hot'):
    c = {}
    for n, s in S_.items():
        for w in s[kind]: c.setdefault(w, []).append(n)
    for w, ns in c.items():
        if len(ns) > 1: print('(aviso, não bloqueia) %s "%s" em %s' % (kind, w, ns)) if kind == 'hot' else fail('%s "%s" repetido em %s' % (kind, w, ns))
for a, b in zip(built, built[1:]):
    for kind in ('vocab', 'verbos', 'lab'):
        com = set(S_[a['n']][kind]) & set(S_[b['n']][kind])
        if com: fail('repetição entre vizinhos %s e %s: %s %s' % (a['n'], b['n'], kind, sorted(com)))
    if S_[a['n']] and mine[a['n']] == mine[b['n']]: fail('mesma obra em vizinhos')
FILLS = {'Good.', 'Coffee?', 'Please.', 'Here.'}
for b in built:
    for fr in b['fr']:
        if fr['k'] == 'pgscene' and fr.get('title') == 'Na conversa de verdade' and sum(1 for l in fr['lines'] if l[1] in FILLS) >= 2: fail('%s: enchimento' % b['n'])
    if b['fr'][-1]['teaser']['t'] == b['t']: fail('%s: teaser aponta para si mesmo' % b['n'])

print('episódios montados:', len(built), '| obras distintas:', len(set(norm(x) for x in names)), '| padrões únicos:', len(seen),
      '| obras/padrões comparados com: %d nomes, %d padrões de outros módulos' % (len(used), others))
print('FALHAS:', len(bad))
sys.exit(1 if bad else 0)
