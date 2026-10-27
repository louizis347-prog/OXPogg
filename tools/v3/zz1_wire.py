#!/usr/bin/env python3
"""Troca, nos módulos sem camada (ep_fix_* e ep() longo), o bloco do episódio por zz1_full(n, ...). Idempotente.
Uso (raiz): COURSE=en-a1 python3 tools/v3/zz1_wire.py"""
import sys, os, re, json, importlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, HERE)
from v3 import zz1_lib as Z
Z.load()
loc = json.load(open(os.environ['LOC']))
done = 0
for n in sorted(Z.SPECS):
    if n not in Z.FULL: continue
    mod = loc[str(n)][0]; path = os.path.join(HERE, mod + '.py')
    src = open(path, encoding='utf-8').read()
    if re.search(r'zz1_full\(%d,' % n, src): continue
    m = importlib.import_module('v3.' + mod)
    e = [x for x in m.EPS if x['n'] == n][0]
    base = e['v2']['base']
    call = "EPS.append(zz1_full(%d, pattern=%r, teaser=%r))\n" % (n, base['pattern_label'], (base['teaser']['t'], base['teaser']['d']))
    # início do bloco: 'EPS.append(' seguido de E(/ep( com n=<n>
    mm = re.search(r'EPS\.append\(\s*\w+\(\s*n\s*=\s*%d\s*,' % n, src)
    assert mm, (n, mod)
    start = mm.start()
    nxt = re.search(r'\n(?=# -{8,}|EPS\.append\()', src[mm.end():])
    end = mm.end() + nxt.start() + 1 if nxt else len(src)
    head = re.search(r'# -{8,}[^\n]*\n$', src[:start])
    if head:
        hs = head.start(); src = src[:hs] + "# ---------------------------------------------------------------- %d · %s · %s\n" % (n, base['pattern_label'], Z.SPECS[n]['ob'][0]) + call + "\n" + src[end:]
    else:
        src = src[:start] + call + "\n" + src[end:]
    if 'zz1_full' not in src.split('EPS = []')[0] and 'import full as zz1_full' not in src:
        src = src.replace('EPS = []', 'EPS = []\nfrom v3.zz1_lib import full as zz1_full', 1)
    open(path, 'w', encoding='utf-8').write(src); done += 1; print('ok', n, mod)
print(done)
