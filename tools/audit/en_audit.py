#!/usr/bin/env python3
"""Auditoria do curso regular de inglês (en-a1…en-c2): pares, arcos, vocabulário e padrões."""
import glob, json, os, re, sys, collections
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LV = ['en-a1', 'en-a2', 'en-b1', 'en-b2', 'en-c1', 'en-c2']


def load(c):
    it = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', '%s_*.json' % c))):
        it += json.load(open(f, encoding='utf-8'))
    return it


def arcs():
    return json.load(open('/tmp/arcs_en.json'))


def words(x):
    return [w[0].strip().lower() for w in x.get('v') or []]


def pairs_of(it):
    by = {x['n']: x for x in it}
    P = []
    seen = set()
    for x in it:
        if x['n'] in seen:
            continue
        if x.get('xof'):
            continue
        c = by.get(x.get('xn'))
        grp = [x] + ([c] if c else [])
        for g in grp:
            seen.add(g['n'])
        P.append(grp)
    orph = [x for x in it if x['n'] not in seen]
    return P, orph


def report(levels=LV):
    A = arcs()
    tot = dict(items=0, pairs=0, vocab=set())
    for c in levels:
        it = load(c)
        P, orph = pairs_of(it)
        voc = collections.Counter(w for x in it for w in words(x))
        pv = collections.Counter(w for g in P for w in set(words(g[0])))
        starts = [a[0] for a in A[c]]
        nset = {x['n'] for x in it}
        mains_alone = sum(1 for g in P if len(g) == 1)
        print('%s: itens=%d pares=%d (sem continuação=%d, órfãos=%d) vocab únicas=%d, repetidas>1=%d, arcos=%d (inícios presentes=%d)%s' % (
            c, len(it), len(P), mains_alone, len(orph), len(voc), sum(1 for v in pv.values() if v > 1), len(starts), sum(1 for n in starts if n in nset),
            ' pilotos=%d' % sum(1 for x in it if x.get('pilot')) if c == 'en-a1' else ''))
        tot['items'] += len(it)
        tot['pairs'] += len(P)
        tot['vocab'] |= set(voc)
    print('TOTAL itens=%d pares=%d vocab únicas=%d' % (tot['items'], tot['pairs'], len(tot['vocab'])))


if __name__ == '__main__':
    report()
