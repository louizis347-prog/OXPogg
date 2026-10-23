#!/usr/bin/env python3
"""Prepara os lotes de redação do piloto A1 (aulas de regra 70/79): entrada para os redatores (um arquivo por lote)."""
import json, os, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
OUT = os.path.join(ROOT, 'tools', 'pilot_a1')
NB = 8


def main():
    m = json.load(open(os.path.join(ROOT, 'data', 'manifest.json'), encoding='utf-8'))
    rows = []
    for b in m['en-a1']:
        for e in json.load(open(os.path.join(ROOT, 'data', b), encoding='utf-8')):
            if not str(e['n']).startswith(('70', '79')):
                continue
            fr = {x['k']: x for x in e['fr']}
            if 'soundlab' not in fr or 'scene' not in fr:
                continue
            cexp = [it['x'] for it in (fr.get('cexp') or {}).get('items', [])]
            words = [it['v'] for it in (fr.get('vplay') or {}).get('items', []) if isinstance(it, dict)]
            rows.append({'n': e['n'], 'title': e['t'], 'subject': e.get('s'),
                         'grammar': (e.get('g') or {}).get('t') if isinstance(e.get('g'), dict) else None,
                         'scene': [[l[0], l[1], l[2]] for l in fr['scene']['lines']],
                         'phrases': cexp, 'words': words})
    rows.sort(key=lambda r: r['n'])
    per = (len(rows) + NB - 1) // NB
    for i in range(NB):
        chunk = rows[i * per:(i + 1) * per]
        json.dump(chunk, open(os.path.join(OUT, 'in_%02d.json' % (i + 1)), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('lote', i + 1, len(chunk), 'episódios')


if __name__ == '__main__':
    main()
