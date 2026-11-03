#!/usr/bin/env python3
"""Registro do que já foi ensinado (para não repetir situação, vocabulário, verbos ou episódio regular).
Uso: python3 src/registry.py            -> resumo
     python3 src/registry.py vocab      -> palavras de vocabulário já ensinadas (aulas com x*.py)
     python3 src/registry.py verbs      -> contagem de verbos por aula (z*.py)
     python3 src/registry.py R          -> episódios regulares (R) já usados / livres
     python3 src/registry.py claim N R  -> reserva o R para a aula N (evita colisão entre agentes)"""
import glob, importlib.util, os, re, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(HERE, 'supp5')
def mod(f, key):
    spec = importlib.util.spec_from_file_location('m' + os.path.basename(f)[:-3], f); m = importlib.util.module_from_spec(spec)
    try: spec.loader.exec_module(m)
    except Exception: return {}
    return getattr(m, key, {})
def lessons(prefix): return sorted(glob.glob(os.path.join(D, prefix + '[0-9][0-9][0-9].py')))
def vocab():
    out = collections.OrderedDict()
    for f in lessons('x'):
        n = int(os.path.basename(f)[1:4])
        for v in mod(f, 'X').get('vocab', []) or []: out.setdefault(v['w'].lower(), n)
    return out
def verbs():
    c = collections.defaultdict(list)
    for f in lessons('z'):
        n = int(os.path.basename(f)[1:4])
        for v in mod(f, 'Z').get('verbs', []) or []: c[v['v'].lower()].append(n)
    return c
def rused():
    r = {}
    for f in lessons('s'):
        n = int(os.path.basename(f)[1:4]); k = mod(f, 'SUPP').get('reg')
        if k: r[k] = n
    cl = os.path.join(D, '_R_claims.txt')
    if os.path.exists(cl):
        for line in open(cl):
            a = line.split()
            if len(a) == 2: r[int(a[1])] = int(a[0])
    return r
if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['vocab']:
        v = vocab(); print(len(v), 'palavras:'); print(', '.join('%s(%d)' % (w, n) for w, n in v.items()))
    elif a[:1] == ['verbs']:
        for w, ns in sorted(verbs().items(), key=lambda x: -len(x[1])): print('%-10s %2d aulas: %s' % (w, len(ns), ns))
    elif a[:1] == ['R']:
        sys.path.insert(0, HERE); import build_v5 as B
        u = rused(); print('R usados:', sorted(u)); print('R livres:', [i for i in range(1, len(B.EN) + 1) if i not in u])
    elif a[:1] == ['claim']:
        open(os.path.join(D, '_R_claims.txt'), 'a').write('%s %s\n' % (a[1], a[2])); print('ok')
    else:
        print(len(vocab()), 'palavras;', len(verbs()), 'verbos;', len(rused()), 'R usados')
