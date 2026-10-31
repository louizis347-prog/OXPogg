#!/usr/bin/env python3
"""Aulas no formato livro didático (v2): lê v2_*.py (LESSONS) e grava professor/data/v2/NNN.json + index.json"""
import glob, importlib.util, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, '..', 'data', 'v2')
os.makedirs(OUT, exist_ok=True)
NEED = {'opener': ['unit', 'title', 'pt', 'goals', 'think', 'scene', 'cast'], 'photo': ['panels'], 'fill': ['items', 'bank', 'instr'], 'board': ['squares'], 'infogap': ['a', 'b', 'lang', 'instr'], 'reading': ['head', 'text', 'tf', 'qs'], 'review': ['items', 'cando', 'homework']}
def main():
    idx = []
    for fn in sorted(glob.glob(os.path.join(HERE, 'v2_*.py'))):
        spec = importlib.util.spec_from_file_location('m', fn); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for L in m.LESSONS:
            for p in L['pages']:
                for k in NEED.get(p['t'], []):
                    assert k in p, (L['n'], p['t'], k)
            L['minutes'] = L.get('minutes', 60)
            json.dump(L, open(os.path.join(OUT, '%03d.json' % L['n']), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
            idx.append(dict(n=L['n'], title=L['title'], pt=L['pt'], level=L.get('level', 'A1'), pages=len(L['pages']), minutes=L['minutes'], scene=L['scene'], tod=L.get('tod', 'day'), cast=L['cast']))
    json.dump(dict(lessons=sorted(idx, key=lambda x: x['n'])), open(os.path.join(OUT, 'index.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    print('aulas v2:', len(idx), [i['pages'] for i in idx])
main()
