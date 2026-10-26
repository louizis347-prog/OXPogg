#!/usr/bin/env python3
"""Checagem cruzada (sem gravar) dos itens 241–474 do A2: monta todos os módulos a2_239_243 … a2_472_474 em memória e aponta,
entre vizinhos, obra/palavras/verbos/sons/objetos repetidos (critério K8 da auditoria) e falas de enchimento (K9).
Uso: COURSE=en-a2 python3 tools/v3/chk_a2b.py [lo] [hi]"""
import glob, importlib, json, os, re, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, 'v3'))
import model_v2 as M
from v3 import lib
import model_v3 as MV
from v3.check import check
os.environ.setdefault('COURSE', 'en-a2')
lo = int(sys.argv[1]) if len(sys.argv) > 1 else 239; hi = int(sys.argv[2]) if len(sys.argv) > 2 else 474
chunks, where = {}, {}
for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'en-a2_*.json'))):
    d = json.load(open(f, encoding='utf-8')); chunks[f] = d
    for i, e in enumerate(d): where[e['n']] = (f, i)
order = sorted(where, key=lambda n: chunks[where[n][0]][where[n][1]]['o'])
pos = {n: i + 1 for i, n in enumerate(order)}
eps = []
for f in sorted(glob.glob(os.path.join(HERE, 'v3', 'a2_*.py'))):
    a, b = map(int, re.findall(r'a2_(\d+)_(\d+)', f)[0])
    if b < lo or a > hi: continue
    eps += importlib.import_module('v3.' + os.path.basename(f)[:-3]).EPS
eps.sort(key=lambda e: pos[e['n']])
built = []; bad = 0
for k, E in enumerate(eps):
    f, i = where[E['n']]; old = chunks[f][i]; P = eps[k - 1] if k else None
    if P and pos[P['n']] == pos[E['n']] - 1: prev = (P['v2'], P['extra'], P['verbs'])
    else:
        pf, pj = where[order[pos[E['n']] - 2]]; pit = chunks[pf][pj]
        prev = MV.prev_from_pilot(pit) if any(x['k'] == 'pgrule' for x in pit['fr']) else MV.prev_from_old(pit)
    M.HOTPT.update(lib.SAYPT)
    b = M.build(old, E['v2'], E['extra'], E['verbs'], prev, E['more']); built.append((pos[E['n']], b))
    for q in check(b): bad += 1; print('PROBLEMA', pos[E['n']], E['n'], q)
def sets(e):
    F = {}
    for f in e['fr']: F.setdefault(f['k'], []).append(f)
    return dict(obra={(e.get('a') or {}).get('w', '')} - {''}, vocab={w[0].lower() for w in (e.get('v') or [])},
                verbos={v['v'].lower() for v in F.get('verbs', [{}])[0].get('items', [])}, lab={x[0].lower() for x in F.get('pglab', [{}])[0].get('ex', [])},
                hot={h.get('en', '').lower() for h in F.get('hotscene', [{}])[0].get('hot', [])})
FILL = {'Good.', 'Coffee?', 'Please.', 'Here.'}
rep = 0; strict = 0
for (pa, a), (pb, b) in zip(built, built[1:]):
    A, B = sets(a), sets(b)
    for k in A:
        com = A[k] & B[k]; lim = 1 if k == 'obra' else 2
        if len(com) >= lim: rep += 1; print('K8', pb, b['n'], k, sorted(com))
        elif com and k != 'hot': strict += 1; print('  (1 palavra)', pb, b['n'], k, sorted(com))
fl = 0
for p, b in built:
    for f in b['fr']:
        if f['k'] == 'pgscene' and f.get('title') == 'Na conversa de verdade' and sum(1 for l in f['lines'] if l[1] in FILL) >= 2:
            fl += 1; print('K9', p, b['n'])
# --- nenhum quadro (exceto a revisão) pode citar a obra, o elenco ou as palavras antigas de um episódio reescrito ---
from v3.ova2b import OLD, OVR, GX
STOP = set('the and with from that this have what when your you are for not but can will was were all its his her they them their who how where which there here some more most very just about into over than then also only each other every'.split())
tk = lambda t: set(w for w in re.findall(r"[a-zà-ú']+", t.lower()) if len(w) > 3 and w not in STOP)
leaks = 0
for p_, b in built:
    o = OLD.get(b['n'])
    if not o: continue
    texts = {}
    for f in b['fr']:
        if f['k'] == 'review': continue
        texts.setdefault(f['k'], '')
        texts[f['k']] += ' ' + json.dumps(f, ensure_ascii=False)
    new = tk(' '.join(texts.values()) if False else '')
    allnew = set()
    for f in b['fr']:
        if f['k'] in ('pgscene', 'hotscene', 'cover'): allnew |= tk(json.dumps(f, ensure_ascii=False))
    old = tk(o['obra']) | set(w for n_ in o['names'] for w in tk(n_)) | set(w for v in o['vocab'] for w in tk(v)) | set(w for h in o['hot'] for w in tk(h))
    cur_names = tk(' '.join(set(x[0] for f in b['fr'] if f['k'] == 'pgscene' for x in f['lines'])))
    old -= cur_names
    allnew |= tk(repr(OVR.get(b['n']))) | tk(repr(GX.get(b['n'])))
    old -= allnew | tk(' '.join(w[0] for w in (b.get('v') or [])))
    for kind, t in texts.items():
        hit = sorted(w for w in old if w in tk(t))
        if hit: leaks += 1; print('CITA-ANTIGO', p_, b['n'], kind, hit)
        if hit and os.environ.get('LEAKDBG') == str(b['n']):
            for f in b['fr']:
                if f['k'] == kind and not f['k'] == 'review':
                    tt = json.dumps(f, ensure_ascii=False)
                    for w in hit:
                        m = re.search(r'\b' + w + r'\b', tt, re.I)
                        if m: print('    >>', f.get('title'), tt[max(0, m.start() - 120):m.start() + 80])
print('quadros citando a obra/palavras antigas:', leaks)
print('problemas:', bad, '| K8:', rep, '| 1 palavra:', strict, '| K9:', fl, '| episódios:', len(built))
# --- obras repetidas dentro do curso (e contra o A1 e o B1 já gravados) ---
import collections
seen = collections.defaultdict(list)
for p_, b in built:
    if p_ >= 241: seen[(b.get('a') or {}).get('w', '')].append(p_)
for p_, e in enumerate(sorted([x for f in glob.glob(os.path.join(ROOT, 'data', 'en-a2_*.json')) for x in json.load(open(f, encoding='utf-8'))], key=lambda e: e['o']), 1):
    if p_ < 241 or p_ > 474: seen[(e.get('a') or {}).get('w', '')].append(p_) if p_ < 241 else None
other = collections.defaultdict(list)
for c in ('en-a1', 'en-b1'):
    for f in glob.glob(os.path.join(ROOT, 'data', c + '_*.json')):
        for x in json.load(open(f, encoding='utf-8')): other[(x.get('a') or {}).get('w', '')].append(c + '#' + str(x['n']))
dups = {w: v for w, v in seen.items() if w and len(v) > 1}
print('obras repetidas dentro do A2:', {w: v for w, v in dups.items()})
print('obras do A2 241–474 também no A1/B1:', {w: other[w][:3] for w in seen if w in other and any(p >= 241 for p in seen[w])})
