#!/usr/bin/env python3
"""Confere se cada episódio do A1 de inglês tem uma estrutura gramatical diferente das demais.
Prontos: usa o `pattern` do episódio. Pendentes: usa tools/gram/unique_a1.json (se houver) ou a `estrutura` do esqueleto.
Uso: python3 tools/gram/check_unique.py"""
import collections, glob, json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ov = json.load(open(os.path.join(ROOT, 'tools/gram/unique_a1.json'), encoding='utf-8'))
sk = {e['n']: e for e in json.load(open(os.path.join(ROOT, 'data/skel/en-a1.json'), encoding='utf-8'))}
items = []
for f in sorted(glob.glob(os.path.join(ROOT, 'data/en-a1_*.json'))): items += json.load(open(f, encoding='utf-8'))
norm = lambda s: re.sub(r'\s+', ' ', s.lower().strip())
c = collections.defaultdict(list)
for i, e in enumerate(items):
    ep = i + 1
    if e.get('pilot') or ep <= 175: s = e.get('pattern') or (e.get('g') or {}).get('t') or ''
    else: s = ov.get(str(e['n'])) or sk[e['n']]['gramatica']['estrutura']
    c[norm(s)].append(ep)
d = {k: v for k, v in c.items() if len(v) > 1}
for k, v in sorted(d.items(), key=lambda x: x[1][0]): print(v, '|', k[:70])
print('repetidos:', len(d), 'grupos,', sum(len(v) for v in d.values()), 'episódios')
