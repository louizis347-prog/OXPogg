#!/usr/bin/env python3
"""Reatribui a gramática (g.t/gs/fn) de pares 'livres' para cobrir o programa de tools/gram/syllabus.py, em ordem de progressão.
Uso: python3 tools/gram/assign.py [--apply]"""
import sys, os, re, json, copy
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools')); sys.path.insert(0, os.path.join(ROOT, 'tools/audit'))
from en_audit import load, pairs_of
from syllabus import S
import reg3
LEX = re.compile(r"idiom|collocation|phrasal|gíria|slang|binomial|review|revisão|checkpoint|exam|mock|wrap|farewell|despedida|brinde|toast|dialect|accent|english\b|englishes|sotaque|regional|verbos e|phrasal verbs|vocabulary|vocabulário|preposition", re.I)
def gt(x): return ((x.get('g') or {}).get('t', '') + ' ' + (x.get('gs') or '')).lower()
def classify(P, lv):
    return [{sid for sid, a, b, mn, rx, *_ in lv if re.search(rx, gt(g[0]))} for g in P]
def run(apply):
    out_all = {}
    for c, lv in S.items():
        it = load(c); P, orph = pairs_of(it); N = len(P)
        cls = classify(P, lv)
        pilot = [any(x.get('pilot') for x in g) for g in P]
        # fecha o nível/arco: mantém inalterado o primeiro (arc start sem g.t) e o último par
        cnt = {sid: sum(1 for s in cls if sid in s) for sid, *_ in lv}
        free = [i for i, g in enumerate(P) if not cls[i] and not pilot[i] and not LEX.search(gt(g[0])) and i not in (0, N - 1)]
        # pares de estruturas sobrerrepresentadas também podem ceder (acima de 2x o mínimo)
        over = {sid for sid, a, b, mn, *_ in lv if cnt[sid] > max(2 * mn, mn + 6)}
        for i, g in enumerate(P):
            if cls[i] and cls[i] <= over and not pilot[i] and i not in (0, N - 1):
                free.append(i)
        free = sorted(set(free)); used = set(); plan = {}
        need = [(sid, a, b, mn - cnt[sid], can, fn) for sid, a, b, mn, rx, can, fn in lv if cnt[sid] < mn]
        # ordena os pedidos pelo início da janela; cada pedido pega os livres mais perto do ponto ideal
        for sid, a, b, k, can, fn in sorted(need, key=lambda r: r[1]):
            lo, hi = a * N, b * N
            for j in range(k):
                tgt = lo + (hi - lo) * (j + .5) / k
                cand = [i for i in free if i not in used and lo - 5 <= i <= hi + 5]
                if not cand: cand = [i for i in free if i not in used]
                if not cand: print('  sem par livre para', c, sid); break
                i = min(cand, key=lambda i: abs(i - tgt)); used.add(i); plan[i] = (sid, can, fn)
        print(c, 'pares', N, '| livres', len(free), '| trocas', len(plan), '| pedidos', sum(r[3] for r in need))
        if apply:
            for i, (sid, can, fn) in plan.items():
                for x in P[i]:
                    x['g'] = dict(x.get('g') or {}); x['g']['t'] = can; x['gs'] = can; x['fn'] = fn; x['regram'] = 1
            out_all[c] = it
        # relatório de cobertura final
        cls2 = classify(P, lv)
        low = [(sid, sum(1 for s in cls2 if sid in s), mn) for sid, a, b, mn, *_ in lv if sum(1 for s in cls2 if sid in s) < mn]
        print('   abaixo do mínimo após troca:', low)
    if apply:
        for c, it in out_all.items():
            tmp = '/tmp/_gram_%s.json' % c
            json.dump(it, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
            reg3.data(c, tmp)
        print('gravado')
if __name__ == '__main__':
    run('--apply' in sys.argv)
