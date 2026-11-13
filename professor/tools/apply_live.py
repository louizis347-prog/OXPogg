#!/usr/bin/env python3
"""Aplica o roteiro do professor (teach) e o plano de 1h30 em todas as aulas de data/v4. Idempotente."""
import glob, json, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')); sys.path.insert(0, os.path.join(ROOT, 'src'))
import live_teach
ns = [int(a) for a in sys.argv[1:]]
for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'v4', '[0-9]*.json'))):
    m = re.search(r'(\d+)\.json$', f); n = int(m.group(1))
    if ns and n not in ns: continue
    L = json.load(open(f, encoding='utf-8')); live_teach.apply(L)
    json.dump(L, open(f, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('ok')
