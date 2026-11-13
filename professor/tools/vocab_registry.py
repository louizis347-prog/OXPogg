#!/usr/bin/env python3
"""Registro de vocabulário ensinado. Uso: vocab_registry.py N [N…] — mostra palavras, verbos e glossário de N que já apareceram
em aulas anteriores (originais com n menor, e continuações de aulas anteriores). 'build' grava data/vocab-registro.json."""
import glob, json, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')); D = os.path.join(ROOT, 'data', 'v4')
def words(d):
    w = set()
    for p in d['pages']:
        k = p.get('kind')
        if k == 'vocab':
            for x in p.get('words', []): w.add(x[0].lower())
        elif k == 'verbs':
            for x in p.get('verbs', []): w.add((x.get('v') or '').lower())
        elif k == 'reading':
            for g in p.get('glossary', []): w.add(g['w'].lower())
    return {x for x in w if x}
def order(n): return (n // 2000) * 100000 + (n % 1000) * 2 + (1 if 1000 <= n < 2000 else 0)
def load():
    out = {}
    for f in glob.glob(os.path.join(D, '[0-9]*.json')):
        d = json.load(open(f, encoding='utf-8')); out[d['n']] = words(d)
    return out
def check(n, reg=None):
    reg = reg or load(); mine = reg.get(n, set()); seen = {}
    for m, ws in reg.items():
        if m != n and order(m) < order(n):
            for w in ws & mine: seen.setdefault(w, []).append(m)
    return seen
if __name__ == '__main__':
    reg = load()
    if sys.argv[1:] == ['build']:
        json.dump({str(k): sorted(v) for k, v in reg.items()}, open(os.path.join(ROOT, 'data', 'vocab-registro.json'), 'w'), ensure_ascii=False); print(len(reg), 'aulas')
    else:
        for a in sys.argv[1:]:
            n = int(a); r = check(n, reg)
            print(n, len(reg.get(n, [])), 'palavras;', len(r), 'repetidas:', {w: v[:3] for w, v in sorted(r.items())})
