#!/usr/bin/env python3
"""Confere o lote A do A1 (zz1_d*.py): obras fora de obras_em_uso, sem repetição entre os alvos nem com obras de outras camadas,
e sem repetição de palavras, verbos, laboratório e obra com os episódios vizinhos do curso (dados publicados + novas especificações).
Uso (da raiz): python3 tools/v3/chk_obras_a1_a.py <a1_targets_a.json>"""
import json, re, sys, unicodedata, os, glob
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, HERE)
from v3 import zz1_lib as Z
Z.load()
norm = lambda s: re.sub(r"[^a-z0-9]", "", unicodedata.normalize('NFD', s.lower()).encode('ascii', 'ignore').decode())
d = json.load(open(sys.argv[1], encoding='utf-8'))
alvos = {t['n'] for t in d['targets']}
uso = {norm(x) for x in d['obras_em_uso']}
bad = 0
mine = {}
for n in alvos:
    s = Z.SPECS.get(n)
    if not s: bad += 1; print('SEM ESPECIFICAÇÃO:', n); continue
    k = norm(s['ob'][0])
    if k in uso: bad += 1; print('COLIDE com obras_em_uso:', n, s['ob'][0])
    if k in mine: bad += 1; print('REPETIDA entre alvos:', n, mine[k], s['ob'][0])
    mine[k] = n
    if ':' in s['ob'][0]: bad += 1; print('título com dois-pontos:', n)
# coerência interna das especificações: palavra-chave dentro da fala do objeto, expressão dentro do exemplo, perguntas sobre falas existentes
for n, s_ in Z.SPECS.items():
    for (hi, key, w1, w2) in s_['gp']:
        if key not in s_['hot'][hi][0]: bad += 1; print('GAP: chave fora da fala', n, key, '|', s_['hot'][hi][0])
        if len({key, w1, w2}) < 3: bad += 1; print('GAP: opções repetidas', n, key)
    for (e, x, pt, use, en, ept) in s_['ex']:
        if x.lower() not in en.lower(): bad += 1; print('EXPRESSÃO fora do exemplo', n, x)
    for q in s_['quiz']:
        if not (0 <= q[2] < 8): bad += 1; print('QUIZ: fala inválida', n)
    if len({v[1] for v in s_['voc']}) != 6: bad += 1; print('vocabulário repetido', n)
# obras de outras camadas (outros lotes) e de outros cursos
other = {}
for f in glob.glob(os.path.join(HERE, 'obras_new_a1_*.json')):
    if f.endswith('obras_new_a1_zz_a.json'): continue
    for n, o in json.load(open(f, encoding='utf-8')).items(): other.setdefault(norm(o['name']), []).append((os.path.basename(f), n))
for k, n in mine.items():
    if k in other: bad += 1; print('COLIDE com outro lote A1:', n, other[k])
soft = {}
for f in glob.glob(os.path.join(HERE, 'obras_new_a2_*.json')) + glob.glob(os.path.join(HERE, 'obras_new_b1_*.json')):
    for n, o in json.load(open(f, encoding='utf-8')).items(): soft.setdefault(norm(o['name']), []).append(os.path.basename(f))
for k, n in mine.items():
    if k in soft: print('aviso (A2/B1 usa a mesma obra):', n, Z.SPECS[n]['ob'][0], soft[k][:2])
# vizinhos no curso
items = []
for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'en-a1_*.json'))):
    for e in json.load(open(f, encoding='utf-8')): items.append(e)
items.sort(key=lambda e: e['o'])
def sets_from_item(e):
    F = {}
    for fr in e['fr']: F.setdefault(fr['k'], []).append(fr)
    return dict(vocab={w[0].lower() for w in (e.get('v') or [])}, verbos={v['v'].lower() for v in F.get('verbs', [{}])[0].get('items', [])},
                lab={x[0].lower() for x in F.get('pglab', [{}])[0].get('ex', [])}, obra={norm((e.get('a') or {}).get('w', ''))})
def sets_from_spec(s):
    return dict(vocab={v[1].lower() for v in s['voc']}, verbos={v[0].lower() for v in s['vb']}, lab={w[0].lower() for w in s['lab'][4]}, obra={norm(s['ob'][0])})
S = {}
for i, e in enumerate(items):
    S[i] = sets_from_spec(Z.SPECS[e['n']]) if e['n'] in alvos and e['n'] in Z.SPECS else sets_from_item(e)
for i, e in enumerate(items):
    if e['n'] not in alvos: continue
    for j in (i - 1, i + 1):
        if 0 <= j < len(items):
            for key in ('vocab', 'verbos', 'lab', 'obra'):
                com = S[i][key] & S[j][key]
                if com: bad += 1; print('REPETIDO', e['n'], 'x', items[j]['n'], key, sorted(com))
# obras: nenhuma obra de alvo repetida em nenhum outro episódio do curso
alln = {}
for i, e in enumerate(items):
    for o in S[i]['obra']: alln.setdefault(o, []).append(e['n'])
for k, n in mine.items():
    if len(alln.get(k, [])) > 1: bad += 1; print('OBRA em mais de um episódio do curso:', n, alln[k])
print('alvos:', len(alvos), '| com especificação:', sum(1 for n in alvos if n in Z.SPECS), '| obras distintas:', len(mine), '| problemas:', bad)
