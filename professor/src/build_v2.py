#!/usr/bin/env python3
"""Aulas no formato livro didático (v2): lê v2_*.py (LESSONS) e grava professor/data/v2/NNN.json + index.json"""
import glob, importlib.util, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, '..', 'data', 'v2')
os.makedirs(OUT, exist_ok=True)
NEED = {'opener': ['unit', 'title', 'pt', 'goals', 'think', 'scene', 'cast'], 'photo': ['panels'], 'fill': ['items', 'bank', 'instr'], 'board': ['squares'], 'infogap': ['a', 'b', 'lang', 'instr'], 'reading': ['head', 'text', 'tf', 'qs'], 'review': ['items', 'cando', 'homework']}
FOR = {'board': 'group', 'bingo': 'group', 'mingle': 'group', 'mime': 'group', 'teamquiz': 'group', 'flash': 'solo', 'interview': 'solo', 'dictation': 'solo'}
def load_extras():
    ex = {}
    for fn in sorted(glob.glob(os.path.join(HERE, 'v2x_*.py'))):
        spec = importlib.util.spec_from_file_location('x', fn); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for n, pages in m.EX.items(): ex.setdefault(n, []).extend(pages)
    return ex
def vocab_items(L):
    out = []
    for p in L['pages']:
        if p['t'] == 'vocab': out += [dict(w=i['w'], pt=i['pt'], vis=i['vis']) for i in p['items']]
        if p['t'] == 'matchpic': out += [dict(w=i['w'], pt='', vis=i['vis']) for i in p['items']]
    seen, res = set(), []
    for i in out:
        if i['w'] not in seen and i.get('vis'): seen.add(i['w']); res.append(i)
    return res
def phrase_list(L):
    out = []
    for p in L['pages']:
        if p['t'] == 'phrases':
            for g in p['groups']:
                out += [i['en'] for i in g['items'] if len(i['en'].split()) >= 2 and not any(ch in i['en'] for ch in '…@•')]
    return out
def merge(L, ex):
    pages = L['pages'][:]
    def insert(after, page):
        idx = max([i for i, p in enumerate(pages) if p['t'] == after] or [len(pages) - 2])
        k = idx + 1
        while k < len(pages) and pages[k].get('_ins') == after: k += 1
        page['_ins'] = after; pages.insert(k, page)
    for e in ex:
        e = dict(e); after = e.pop('after'); insert(after, e)
    vi = vocab_items(L); ph = phrase_list(L)
    insert('matchpic', dict(t='flash', title="Flashcards", items=vi))
    insert('matchpic', dict(t='mime', title="Act it out", items=[dict(w=i['w'], vis=i['vis']) for i in vi], rules="One student draws a card and acts or draws the word. The team has 30 seconds to say it in English. Correct = +1 point."))
    insert('chant', dict(t='dictation', title="Dictation", items=ph[2:6] if len(ph) >= 6 else ph[:4]))
    insert('fact', dict(t='bingo', title="Vocabulary bingo", size=3, items=[dict(w=i['w'], vis=i['vis']) for i in vi][:16]))
    qs = []
    for p in L['pages']:
        if p['t'] == 'review': qs = p['items']
    insert('bingo', dict(t='teamquiz', title="Team quiz", items=[dict(q=q[0], opts=q[1], ans=q[2]) for q in qs]))
    for p in pages:
        p.pop('_ins', None)
        if p['t'] in FOR and 'for' not in p: p['for'] = FOR[p['t']]
    L['pages'] = pages
def main():
    idx = []
    EXT = load_extras()
    for fn in sorted(glob.glob(os.path.join(HERE, 'v2_*.py'))):
        spec = importlib.util.spec_from_file_location('m', fn); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for L in m.LESSONS:
            merge(L, EXT.get(L['n'], []))
            for p in L['pages']:
                for k in NEED.get(p['t'], []):
                    assert k in p, (L['n'], p['t'], k)
            L['minutes'] = 75
            json.dump(L, open(os.path.join(OUT, '%03d.json' % L['n']), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
            idx.append(dict(n=L['n'], title=L['title'], pt=L['pt'], level=L.get('level', 'A1'), pages=len(L['pages']), minutes=L['minutes'], scene=L['scene'], tod=L.get('tod', 'day'), cast=L['cast']))
    json.dump(dict(lessons=sorted(idx, key=lambda x: x['n'])), open(os.path.join(OUT, 'index.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    print('aulas v2:', len(idx), [i['pages'] for i in idx])
main()
