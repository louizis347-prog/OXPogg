#!/usr/bin/env python3
"""Valida src/supp5/zNNN.py. Uso: validate_z.py N [N…] | --all"""
import glob, importlib.util, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
def load(n):
    f = os.path.join(HERE, 'supp5', 'z%03d.py' % n)
    if not os.path.exists(f): return {}
    spec = importlib.util.spec_from_file_location('z5%03d' % n, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.Z
def check(n):
    E = []; Z = load(n)
    if not Z: return ['sem bloco z']
    v = Z.get('verbs') or []
    if len(v) != 5: E.append('verbs: exatamente 5')
    for x in v:
        if not (x.get('v') and x.get('ic') and x.get('pt') and x.get('note')): E.append('verbs: v/ic/pt/note em ' + str(x.get('v')))
        f = x.get('forms') or []
        if [a.get('k') for a in f] != ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']: E.append('verbs: forms com k na ordem exata (eu · você · nós · eles / ele · ela / passado / -ing) em ' + str(x.get('v')))
        for a in f:
            if not (a.get('en') and a.get('ex') and a.get('pt')): E.append('verbs: en/ex/pt em ' + str(x.get('v'))); break
            if a['en'].lower() not in a['ex'].lower(): E.append('verbs: o exemplo precisa conter “%s”' % a['en'])
    g = Z.get('verb_game') or []
    if len(g) != 4: E.append('verb_game: exatamente 4')
    for x in g:
        if not (x.get('scene') and '___' in x.get('en', '') and x.get('pt') and x.get('why')): E.append('verb_game: scene, en com ___, pt, why')
        if len(x.get('opts', [])) != 3 or not isinstance(x.get('ans'), int) or not 0 <= x['ans'] < 3 or len(set(x['opts'])) < 3: E.append('verb_game: 3 opções diferentes e ans 0-2')
    e = Z.get('expressions') or []
    if len(e) != 6: E.append('expressions: exatamente 6')
    for x in e:
        if not (x.get('en') and x.get('pt') and x.get('ex') and x.get('exp') and x.get('c') in ('a', 'b', 'c', 'd')): E.append('expressions: en/pt/ex/exp/c em ' + str(x.get('en')))
    q = Z.get('expr_game') or []
    if len(q) != 3: E.append('expr_game: exatamente 3')
    for x in q:
        if not (x.get('cue') and x.get('why')) or len(x.get('opts', [])) != 3 or not isinstance(x.get('ans'), int) or not 0 <= x['ans'] < 3: E.append('expr_game: cue, why, 3 opções, ans')
    return E
if __name__ == '__main__':
    a = sys.argv[1:]; ns = sorted(int(os.path.basename(f)[1:4]) for f in glob.glob(os.path.join(HERE, 'supp5', 'z[0-9][0-9][0-9].py'))) if '--all' in a else [int(x) for x in a]
    bad = 0
    for n in ns:
        e = check(n)
        if e: bad += 1; print('AULA %d:' % n, *['  - ' + x for x in e[:10]], sep='\n')
    print('ok' if not bad else 'aulas com erro: %d' % bad); sys.exit(1 if bad else 0)
