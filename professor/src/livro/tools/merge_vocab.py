"""Une saídas dos agentes (vout/b*_N.json) em data/livro/vocab/<ID>.json, com IPA do CMUdict.
Uso: python3 merge_vocab.py <pasta vout>"""
import glob, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import ipa
OUT = sys.argv[1]
ROOT = os.path.join(os.path.dirname(__file__), '..', '..', '..')
DATA = os.path.join(ROOT, 'data', 'livro')
os.makedirs(os.path.join(DATA, 'vocab'), exist_ok=True)
POS = {'noun','verb','adj','adv','prep','pron','conj','det','phrase','interj','num'}
ok = bad = miss = 0
for f in sorted(glob.glob(os.path.join(OUT, 'b*_*.json'))):
    try: d = json.load(open(f))
    except Exception as e: print('JSON inválido', f, e); continue
    for lid, v in d.items():
        lp = os.path.join(DATA, 'lessons', lid + '.json')
        if not os.path.exists(lp): continue
        L = json.load(open(lp)); words = []
        for fr in L['frames']:
            for b in fr['blocks']:
                if b['type'] == 'vocab': words += [x['w'] for x in b['items']]
        items = {}
        for w in words:
            it = (v.get('items') or {}).get(w)
            if not isinstance(it, dict) or not it.get('ex') or not it.get('pt'): miss += 1; continue
            p = it.get('pos'); p = p if p in POS else ''
            items[w] = dict(pos=p, ex=it['ex'].strip(), pt=it['pt'].strip(), ipa=ipa.ipa(w))
        if len(items) < len(words) * 0.9: bad += 1; print('rejeitada', lid, len(items), len(words)); continue
        out = dict(items=items)
        for k, n in (('family', 3), ('colloc', 3), ('syn', 4)):
            out[k] = [x for x in (v.get(k) or []) if isinstance(x, list) and len(x) >= 2][:n]
        c = v.get('classify')
        if isinstance(c, dict) and isinstance(c.get('groups'), dict) and len(c['groups']) == 2 and all(len(g) >= 3 for g in c['groups'].values()):
            out['classify'] = c
        json.dump(out, open(os.path.join(DATA, 'vocab', lid + '.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
        ok += 1
print('aulas:', ok, '| rejeitadas:', bad, '| palavras sem item:', miss)
