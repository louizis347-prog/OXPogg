#!/usr/bin/env python3
"""Mostra o que a aula N já tem do Neighbors (diálogo, nota cultural, expressões) e, se já houver 'reg', o episódio regular casado."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_v5 as B
n = int(sys.argv[1]); nb = B.NB[n - 1]
print('=== NEIGHBORS %d: %s | %s' % (n, nb['t'], nb['a'])); 
for f in nb['fr']:
    if f['k'] == 'nbchat': print('DIALOGO:'); [print('  %s: %s  (%s)' % (w, e, p)) for w, e, p in f['lines']]; break
for f in nb['fr']:
    if f['k'] == 'nbslang': print('GIRIAS:', [l[1] for l in f['lines']][:5])
    if f['k'] == 'nbvocab': print('VOCAB:', [i[0] for i in f['items']])
S = B.supp(n)
r = int(sys.argv[2]) if len(sys.argv) > 2 else S.get('reg')
if r:
    en = B.EN[r - 1]; print('=== REGULAR R%d: %s | obra: %s | %s' % (r, en['t'], en['a']['w'], en['a'].get('d', '')[:300]))
    for f in en['fr']:
        if f['k'] == 'rdg': print('LEITURA DA OBRA:', ' '.join(s[0] for s in f['s']))
        if f['k'] == 'pgexp': print('EXPRESSOES:', [i['en'] for i in f['items']])
        if f['k'] == 'pgrule': print('REGRA:', f['rule'].get('head'))
