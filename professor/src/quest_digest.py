"""Gera as entradas dos agentes de conteúdo Quest: src/quest_work/in/c1..c4.json (50 aulas cada)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(HERE, '..')
cur = json.load(open(os.path.join(R, 'data/v4/curriculum.json')))
W = {}
for c in cur:
    n = c['n']; d = json.load(open(os.path.join(R, 'data/v4/%03d.json' % n)))
    words, ex, verbs = [], [], []
    for p in d['pages']:
        if p.get('x'): continue
        if p['kind'] == 'vocab': words += [(w[0], w[1], w[2]) for w in p['words']]
        if p['kind'] == 'exprs': ex += [i['en'] for i in p['items']]
        if p['kind'] == 'verbs': verbs += [v['v'] for v in p['verbs']]
    W[n] = {'title': d['title'], 'topic': d.get('topic'), 'words': words, 'exprs': ex, 'verbs': verbs}
ids = sorted(W)
for k in range(4):
    part = {}
    for n in ids[k * 50:(k + 1) * 50]:
        i = ids.index(n); nb = [w[0] for m in ids[max(0, i - 2):i + 3] if m != n for w in W[m]['words']][:18]
        part[n] = dict(W[n], neighbors=nb)
    json.dump(part, open(os.path.join(HERE, 'quest_work/in/c%d.json' % (k + 1)), 'w'), ensure_ascii=False)
print(len(ids), 'aulas')
