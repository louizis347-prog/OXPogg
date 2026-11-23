#!/usr/bin/env python3
"""Remove vocabulário-alvo repetido (mantém a 1ª ocorrência e sempre as base_words) e lista o que falta repor em in/fix.json."""
import glob, json, os, re
H = os.path.dirname(os.path.abspath(__file__))
old = json.load(open(H + '/old.json')); ORDER = json.load(open(H + '/order.json')); cur = {c['n']: c for c in json.load(open(H + '/curriculum_51_130.json'))}
files = sorted(glob.glob(H + '/out/block[0-9]*.json'), key=lambda f: int(re.findall(r'\d+', os.path.basename(f))[0]))
blocks = {f: json.load(open(f)) for f in files if 'fix' not in f}
by = {}
for f, d in blocks.items():
    for k, v in d.items(): by[int(k)] = (f, v)
st = lambda w: re.sub(r'(ing|ed|es|s)$', '', w.lower())
seen = {}; fix = []
allbase = set()
for n in range(1, 131):
    b = old['plan'][ORDER[n - 1] - 1]['words'] if n <= 50 else cur[n]['base_words']
    for w in b: allbase.add(st(w[0]) if len(w[0].split()) == 1 else w[0].lower())
for n in range(1, 131):
    if n not in by: continue
    f, d = by[n]
    base = {w[0].lower() for w in (old['plan'][ORDER[n - 1] - 1]['words'] if n <= 50 else cur[n]['base_words'])}
    keep = []
    for t, pt in d['words']:
        k = st(t) if len(t.split()) == 1 else t.lower()
        isbase = t.lower() in base
        if isbase or (k not in seen and k not in allbase):
            keep.append([t, pt]); seen.setdefault(k, n)
        else: continue
    for t, pt in keep: seen.setdefault(st(t) if len(t.split()) == 1 else t.lower(), n)
    d['words'] = keep
    if len(keep) < 8: fix.append(dict(n=n, title=(old['plan'][ORDER[n - 1] - 1]['title'] if n <= 50 else cur[n]['title']), grammar=(old['plan'][ORDER[n - 1] - 1]['grammar'] if n <= 50 else cur[n]['grammar']), need=8 - len(keep), have=[w[0] for w in keep], reading=[x[0] for x in d['reading']], dialogue=[x[0] for x in d['dialogue']]))
for f, d in blocks.items(): json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(fix, open(H + '/in/fix.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('lições a repor:', len(fix), 'itens:', sum(x['need'] for x in fix))
