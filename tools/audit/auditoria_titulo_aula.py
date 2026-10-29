#!/usr/bin/env python3
"""Auditoria #3 — o título da obra bate com a aula? (inglês regular, 3.000 episódios)
Classes: COERENTE (a aula cita a obra fora das frases-modelo) · PRESA_A_OUTRA_OBRA (sem menção, mas o conteúdo temático
coincide com o de outro episódio que cita uma obra: o título foi trocado) · GENERICA (sem menção e sem vínculo: dá para só trocar o título).
Uso: python3 tools/audit/auditoria_titulo_aula.py  → docs/AUDITORIA_TITULO_AULA.json/.csv"""
import csv, glob, json, math, os, re, unicodedata
from collections import Counter, defaultdict
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TPL = re.compile(r"program notes|cultural lens|cultural reference|contexto d[ea]|referência cultural|lente cultural|nas notas do programa|scene carries an idea|cena da obra|retome|returns to|reference to .* gives|this lesson uses|noticed", re.I)
STOP = set("this that with from have they them were what when your about there their would could should which these those into than then some more most very just also like been being does done will shall might must".split())
def fold(s):
    s = unicodedata.normalize('NFKD', (s or '').lower()); return ''.join(c for c in s if not unicodedata.combining(c))
def words(txt): return {w for w in re.findall(r"[a-z]{4,}", fold(txt)) if w not in STOP}
def lesson_text(e):
    out = []
    for fr in e['fr']:
        k = fr['k']
        if k in ('pgscene', 'hotscene'):
            for ln in fr.get('lines', []): out.append(ln[1])
        if k == 'pgmission':
            for m in fr.get('missions', []): out.append((m.get('data') or {}).get('model', ''))
        if k in ('verbs', 'vplay'):
            for it in fr.get('items', []): out += [x for x in (it.get('ex') or [''])[:1]]
    return [t for t in out if not TPL.search(t)]
E = []
for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'en-*_*.json'))):
    lv = re.search(r'en-(\w\d)_', f).group(1)
    for e in json.load(open(f, encoding='utf-8')): E.append((lv, e))
rows = []; theme = {}
for lv, e in E:
    w = re.sub(r'\(.*?\)', '', e['a']['w']).split(':')[0]
    toks = [t for t in words(w)][:3]
    body = fold(' '.join(lesson_text(e)))
    mentions = bool(toks) and any(t in body for t in toks)
    th = words(' '.join([v[0] for v in e['v']] + [x for x in lesson_text(e)]))
    theme[e['n']] = th
    rows.append(dict(lv=lv, n=e['n'], t=e['t'], w=e['a']['w'], mentions=mentions))
df = Counter(w for th in theme.values() for w in th)
by = {r['n']: r for r in rows}
inv = defaultdict(set)
for n, th in theme.items():
    for w in th:
        if df[w] <= 6: inv[w].add(n)
for r in rows:
    if r['mentions']: r['cls'] = 'COERENTE'; continue
    score = Counter()
    for w in theme[r['n']]:
        if df[w] <= 6:
            for m in inv[w]:
                if m != r['n'] and by[m]['mentions']: score[m] += 1
    best = score.most_common(1)
    if best and best[0][1] >= 3:
        r['cls'] = 'PRESA_A_OUTRA_OBRA'; r['outra'] = by[best[0][0]]['w']; r['ep_outra'] = best[0][0]; r['compartilha'] = best[0][1]
    else: r['cls'] = 'GENERICA'
c = Counter((r['lv'], r['cls']) for r in rows)
res = {lv: {k: c[(lv, k)] for k in ('COERENTE', 'PRESA_A_OUTRA_OBRA', 'GENERICA')} for lv in ['a1', 'a2', 'b1', 'b2', 'c1', 'c2']}
os.makedirs(os.path.join(ROOT, 'docs'), exist_ok=True)
json.dump(res, open(os.path.join(ROOT, 'docs', 'AUDITORIA_TITULO_AULA.json'), 'w'), indent=1)
with open(os.path.join(ROOT, 'docs', 'AUDITORIA_TITULO_AULA.csv'), 'w', newline='') as fh:
    wr = csv.writer(fh); wr.writerow(['nivel', 'ep', 'titulo_episodio', 'obra', 'classe', 'obra_do_conteudo', 'ep_da_outra'])
    for r in rows:
        if r['cls'] != 'COERENTE': wr.writerow([r['lv'], r['n'], r['t'], r['w'], r['cls'], r.get('outra', ''), r.get('ep_outra', '')])
print(json.dumps(res))
