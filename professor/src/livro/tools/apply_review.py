"""Aplica correções dos revisores (rout/r*_N.json) sobre data/livro/vocab/<ID>.json.
Uso: python3 apply_review.py <pasta rout> [log.txt]"""
import glob, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import ipa
OUT = sys.argv[1]
LOG = sys.argv[2] if len(sys.argv) > 2 else None
DATA = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'livro')
POS = {'noun', 'verb', 'adj', 'adv', 'prep', 'pron', 'conj', 'det', 'phrase', 'interj', 'num'}
cnt = dict(ex=0, pos=0, family=0, colloc=0, syn=0, classify=0)
logs = []
for f in sorted(glob.glob(os.path.join(OUT, 'r*_*.json'))):
    try: d = json.load(open(f))
    except Exception as e: print('JSON inválido', f, e); continue
    for lid, c in d.items():
        p = os.path.join(DATA, 'vocab', lid + '.json')
        if not os.path.exists(p) or not isinstance(c, dict): continue
        v = json.load(open(p))
        for w, it in (c.get('items') or {}).items():
            if w not in v['items'] or not isinstance(it, dict): continue
            if it.get('ex') and it.get('pt'):
                v['items'][w]['ex'] = it['ex'].strip(); v['items'][w]['pt'] = it['pt'].strip(); cnt['ex'] += 1
            if it.get('pos') in POS and it['pos'] != v['items'][w].get('pos'):
                v['items'][w]['pos'] = it['pos']; cnt['pos'] += 1
        for k, lo, hi in (('family', 2, 3), ('colloc', 2, 3), ('syn', 3, 5)):
            L = [x for x in (c.get(k) or []) if isinstance(x, list) and len(x) >= 2]
            if k == 'syn': L = [x if len(x) >= 3 else x + ['syn'] for x in L]
            if len(L) >= lo:
                v[k] = L[:hi]; cnt[k] += 1
        cl = c.get('classify')
        if isinstance(cl, dict) and isinstance(cl.get('groups'), dict) and len(cl['groups']) == 2 and all(isinstance(g, list) and len(g) >= 3 for g in cl['groups'].values()):
            v['classify'] = cl; cnt['classify'] += 1
        json.dump(v, open(p, 'w'), ensure_ascii=False, separators=(',', ':'))
        for l in c.get('log') or []: logs.append(lid + ': ' + str(l))
print('correções:', cnt)
if LOG: open(LOG, 'w').write('\n'.join(logs))
