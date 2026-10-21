#!/usr/bin/env python3
"""Audita rapidamente os requisitos estruturais dos cursos de referência."""
import json, glob, collections

def load(pattern):
    rows=[]
    for path in glob.glob(pattern):
        with open(path, encoding='utf-8') as f: rows.extend(json.load(f))
    return rows

def main():
    print('Neighbors inglês')
    total=0
    for level in ('a1','a2','b1','b2','c1','c2'):
        rows=load(f'data/nb-{level}_*.json'); total+=len(rows)
        missing=[]
        for e in rows:
            kinds={f.get('k') for f in e.get('fr',[])}
            required={'nbtap','nbctx','nbvocab','nbshadow','nbfind','wrap'}
            if not required.issubset(kinds): missing.append(e.get('n'))
        print(f'  {level}: {len(rows)} episódios; {len(missing)} fora do núcleo')
    print(f'  total: {total}')
    print('Regular inglês')
    total=0
    for level in ('a1','a2','b1','b2','c1','c2'):
        rows=load(f'data/en-{level}_*.json'); total+=len(rows); missing=[]
        for e in rows:
            kinds={f.get('k') for f in e.get('fr',[])}
            if not {'cultob','cultx','cultcena'}.issubset(kinds): missing.append(e.get('n'))
        print(f'  {level}: {len(rows)} episódios; {len(missing)} sem sequência cultural')
    print(f'  total: {total}')

if __name__ == '__main__': main()
