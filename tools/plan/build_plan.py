#!/usr/bin/env python3
"""Gera plano/<curso>.json (âncoras de data/ + mapeamento de tools/plan/map/ + quadros vazios). Uso: python3 tools/plan/build_plan.py en-c1 [en-c2 ...]"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import plan_lib as P

for c in sys.argv[1:]:
    plan = P.build(c)
    os.makedirs(os.path.join(P.ROOT, 'plano'), exist_ok=True)
    json.dump(plan, open(os.path.join(P.ROOT, 'plano', c + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    est = {}
    for e in plan['entradas']:
        est[e['estado']] = est.get(e['estado'], 0) + 1
    print(c, plan['episodios'], est)
