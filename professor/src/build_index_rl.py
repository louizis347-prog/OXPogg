#!/usr/bin/env python3
"""Lista as aulas Real-Life existentes em data/v3/available.json (usado pelo painel). Uso: python3 src/build_index_rl.py"""
import glob, json, os, re
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
ns = sorted(int(re.search(r'(\d+)\.json$', f).group(1)) for f in glob.glob(os.path.join(ROOT, 'data', 'v3', '[0-9][0-9][0-9].json')))
json.dump(ns, open(os.path.join(ROOT, 'data', 'v3', 'available.json'), 'w'))
print('aulas disponíveis:', len(ns))
