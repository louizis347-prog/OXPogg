#!/usr/bin/env python3
"""Valida src/supp5/yNNN.py. Uso: validate_y.py N [N…] | --all"""
import glob, importlib.util, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build_v5 as B
def load(n):
    f = os.path.join(HERE, 'supp5', 'y%03d.py' % n)
    if not os.path.exists(f): return {}
    spec = importlib.util.spec_from_file_location('y5%03d' % n, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.Y
norm = lambda s: re.sub(r'\s+', ' ', re.sub(r'\*\*', '', s)).strip()
def check(n):
    E = []; Y = load(n)
    if not Y: return ['sem bloco y']
    S = B.supp(n); tx = S['reading']['text']; ss = Y.get('sentences') or []
    if len(ss) != len(tx): E.append('sentences: precisa de %d parágrafos (tem %d)' % (len(tx), len(ss)))
    else:
        for i, (par, t) in enumerate(zip(ss, tx)):
            if not par or any(not (x.get('en') and x.get('pt')) for x in par): E.append('sentences[%d]: en/pt em todas as frases' % i); continue
            if norm(' '.join(x['en'] for x in par)) != norm(t): E.append('sentences[%d]: os en juntos precisam reproduzir o parágrafo exatamente' % i)
    s = Y.get('soundlab') or {}
    for k in ('focus', 'what', 'how', 'tip'):
        if not s.get(k): E.append('soundlab.' + k)
    if len(s.get('words', [])) != 3 or any(not (w.get('w') and w.get('pt')) for w in s.get('words', [])): E.append('soundlab.words: 3 × {w, pt}')
    if len(s.get('pairs', [])) != 3 or any(not (p.get('a') and p.get('b') and p['a'] != p['b']) for p in s.get('pairs', [])): E.append('soundlab.pairs: 3 × {a, b} diferentes')
    if not ((s.get('phrase') or {}).get('en') and (s.get('phrase') or {}).get('pt')): E.append('soundlab.phrase {en, pt}')
    c = Y.get('cards') or []
    if len(c) != 4: E.append('cards: exatamente 4')
    for x in c:
        if not (x.get('icon') and x.get('big') and x.get('label') and 20 <= len(re.findall(r'\w+', x.get('sub', ''))) <= 60): E.append('cards: icon/big/label e sub de 20–60 palavras (%s)' % x.get('big'))
    return E
if __name__ == '__main__':
    a = sys.argv[1:]; ns = sorted(int(os.path.basename(f)[1:4]) for f in glob.glob(os.path.join(HERE, 'supp5', 'y[0-9][0-9][0-9].py'))) if '--all' in a else [int(x) for x in a]
    bad = 0
    for n in ns:
        e = check(n)
        if e: bad += 1; print('AULA %d:' % n, *['  - ' + x for x in e[:10]], sep='\n')
    print('ok' if not bad else 'aulas com erro: %d' % bad); sys.exit(1 if bad else 0)
