#!/usr/bin/env python3
"""Aulas Quest: enxuga os quadros, acrescenta 'Sobre você' (início e fim) e 'Cena da obra',
liga o cenário pintado (data/paint.json) e indexa no currículo as aulas que existem mas estavam fora dele. Idempotente."""
import glob, json, os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
D = os.path.join(ROOT, 'data', 'v4')
PAINT = json.load(open(os.path.join(ROOT, 'data', 'paint.json'), encoding='utf-8'))
DROP_TITLES = ('Mochila · palavras', 'Mochila · desafio', 'Mochila · fale', 'Ponte · como não traduzir',
               'Mito ou fato? · 2/2', 'Encontre as informações', 'Palavras pelo contexto', 'Confira as pistas',
               'Verbos em ação · 2/2', 'Laboratório de sons · ouça e escolha', 'Transferência de contexto')
def first_sentences(s, mx=250):
    s = re.sub(r'\s+', ' ', s or '').strip(); out = ''
    for part in re.split(r'(?<=[.!?])\s+', s):
        if len(out) + len(part) > mx and out: break
        out += (' ' if out else '') + part
    return out[:mx + 40]
def enrich(d):
    pg = d['pages']
    if any(p.get('kind') in ('me', 'story') for p in pg): return False
    cover = next(p for p in pg if p.get('kind') == 'cover')
    pats = [p for p in pg if p.get('kind') == 'pattern' and p.get('slots')]
    work = next(p for p in pg if p.get('kind') == 'work')
    # 1) enxugar
    keep, seen_art, seen_facts = [], 0, 0
    for p in pg:
        t = p.get('title', '')
        if t in DROP_TITLES: continue
        if p.get('kind') == 'artifact':
            seen_art += 1
            if seen_art > 1: continue
        if p.get('kind') == 'facts':
            seen_facts += 1
            if seen_facts > 1: continue
        keep.append(p)
    pg = keep
    art = cover.get('art') or {}
    pnt = PAINT.get(str(d['n']))
    # 2) Sobre você (início)
    fr0 = pats[0] if pats else None
    me0 = {'t': 'q1', 'stage': 'mission', 'kind': 'me', 'mode': 'start', 'title': 'Sobre você · começo',
           'model': (fr0.get('model') if fr0 and fr0.get('model') else (cover.get('can') or [''])[0]), 'frame': fr0['frame'] if fr0 else '', 'slots': fr0['slots'] if fr0 else [],
           'goal': cover.get('goal', ''), 'art': art}
    # 3) Cena da obra
    lines = [{'who': l['who'], 'name': d['dialog']['speakers'].get(l['who'], {}).get('name', l['who']), 'en': l['en'], 'pt': l['pt']} for l in d['dialog']['lines'][:3]]
    story = {'t': 'q1', 'stage': 'culture', 'kind': 'story', 'title': 'Cena da obra', 'work': {'title': work['work']['title'], 'year': work['work'].get('year', '')},
             'narr': first_sentences(work['work'].get('note', '')), 'lines': lines, 'art': art}
    # 4) Sobre você (fim): as duas formas + falas do começo
    fr = [{'frame': p['frame'], 'slots': p['slots'], 'model': p.get('model', '')} for p in pats[:2]]
    me1 = {'t': 'q1', 'stage': 'write', 'kind': 'me', 'mode': 'end', 'title': 'Sobre você · final', 'frames': fr, 'art': art}
    i = next(k for k, p in enumerate(pg) if p.get('kind') == 'cover'); pg.insert(i + 1, me0)
    i = next(k for k, p in enumerate(pg) if p.get('kind') == 'work'); pg.insert(i + 1, story)
    i = next(k for k, p in enumerate(pg) if p.get('kind') == 'exit'); pg.insert(i, me1)
    d['pages'] = pg
    if pnt and not os.path.exists(os.path.join(ROOT, '..', 'img', 'scenes', pnt['name'] + '.webp')): pnt = dict(pnt, name=re.sub(r'-v-?(\d)', r'-v\1', pnt['name']).replace('-v-', '-'))
    if pnt and not os.path.exists(os.path.join(ROOT, '..', 'img', 'scenes', pnt['name'] + '.webp')): pnt = dict(pnt, name=pnt['theme'] + '-day')
    if pnt: d['paint'] = pnt
    return True
changed = 0
for f in sorted(glob.glob(os.path.join(D, '[0-9]*.json'))):
    d = json.load(open(f, encoding='utf-8'))
    if enrich(d):
        json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':')); changed += 1
# currículo: inclui as aulas existentes que faltavam no índice
cp = os.path.join(D, 'curriculum.json'); cur = json.load(open(cp, encoding='utf-8')); have = {x['n'] for x in cur}; add = 0
for f in sorted(glob.glob(os.path.join(D, '[0-9]*.json'))):
    d = json.load(open(f, encoding='utf-8'))
    if d['n'] in have: continue
    cur.append({'n': d['n'], 'unit': d['unit'], 'level': d['level'], 'title': d['title'], 'pt': d['pt'], 'scene': d['scene'], 'cast': d['cast']}); add += 1
cur.sort(key=lambda x: (x['n'] >= 2000, x['n'] % 1000, x['n'] >= 1000 and x['n'] < 2000)); json.dump(cur, open(cp, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('aulas alteradas', changed, '| indexadas', add, '| total no índice', len(cur))
