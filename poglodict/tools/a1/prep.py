#!/usr/bin/env python3
"""Gera os pacotes de entrada (in/blockK.json) para reescrever as 50 lições A1 na nova ordem pedagógica."""
import json, os, re
H = os.path.dirname(os.path.abspath(__file__)); old = json.load(open(H + '/old.json'))
# nova posição (1..50) -> lição antiga (1..50): reordena a gramática; cada cena/foto/áudio de pronúncia anda junto
ORDER = [20,4,1,2,7,10,6,11,23,24, 5,13,14,12,15,25,3,28,33,34, 9,17,21,16,22,27,8,48,41,35, 31,32,30,26,43,36,37,38,29,44, 45,40,42,46,47,39,49,18,19,50]
assert sorted(ORDER) == list(range(1, 51))
CORE = 'mother father sister brother family money color red blue green happy tired hungry big small old new cold hot drink sleep read speak night year birthday'.split()
# primeira lição em que cada estrutura pode aparecer (o resto é bloqueado por script)
FIRST = {'would': 7, 'must': 46, 'does': 36, "doesn't": 99, "don't": 19, 'cannot': 28, 'can': 4}
def words(s): return re.findall(r"[a-z’']+", s.lower())
packets = []
for n, o in enumerate(ORDER, 1):
    p = old['plan'][o - 1]
    pr = old['content'][o - 1][2]; lab = old['pron'][o - 1]
    pw = sorted({w for x in pr[2] for w in words(x)} | {c[0].lower() for c in lab[2]})
    prev = ORDER[max(0, n - 6):n - 1]
    packets.append(dict(
        n=n, old=o, level='A1', title=p['title'], photo=p['file'], grammar=p['grammar'], goal=p['goal'],
        base_words=p['words'],
        core_candidates=[CORE[(n * 2 - 2) % len(CORE)], CORE[(n * 2 - 1) % len(CORE)]],
        grammar_taught_before=[old['plan'][x - 1]['grammar'] for x in ORDER[:n - 1]],
        recycle_from_previous=[w for x in prev for w in old['plan'][x - 1]['words']],
        pron_words=pw, pron_sound=pr[0],
        mini_story=(n % 10 == 0),
        old_reading=[l[0] for l in old['content'][o - 1][0]], old_dialogue=[l[0] for l in old['content'][o - 1][1]],
    ))
os.makedirs(H + '/in', exist_ok=True); os.makedirs(H + '/out', exist_ok=True)
for k in range(5):
    json.dump(packets[k * 10:(k + 1) * 10], open(H + '/in/block%d.json' % (k + 1), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(ORDER, open(H + '/order.json', 'w'))
print('ok', [p['title'] for p in packets[:6]])
