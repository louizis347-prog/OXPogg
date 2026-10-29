#!/usr/bin/env python3
"""Confere um lote de cenários (tools/scenes/out/<lote>.json). Uso: python3 tools/scenes/check.py <lote> [<lote> ...]"""
import collections, glob, importlib.util, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
spec = importlib.util.spec_from_file_location('fv', os.path.join(ROOT, 'tools', 'ficha', 'validate.py')); fv = importlib.util.module_from_spec(spec); spec.loader.exec_module(fv)
V = json.load(open(os.path.join(ROOT, 'tools/ficha/vocab.json'), encoding='utf-8'))
ALIAS = {'plaza', 'skyline', 'beach'}
GEN = {'meadow', 'village', 'city', 'park', 'hills', 'road', 'forest', 'garden'}

def main(lotes):
    probs = []; tot = 0
    for l in lotes:
        brief = json.load(open(os.path.join(ROOT, 'tools/scenes/briefs', l + '.json'), encoding='utf-8'))['alvo']
        out = json.load(open(os.path.join(ROOT, 'tools/scenes/out', l + '.json'), encoding='utf-8'))
        order = [a['n'] for a in brief]
        miss = [n for n in order if str(n) not in out]
        if miss: probs.append('%s: faltam %d episódios (ex.: %s)' % (l, len(miss), miss[:3]))
        extra = [n for n in out if int(n) not in set(order)]
        if extra: probs.append('%s: episódios fora do lote: %s' % (l, extra[:3]))
        cnt = collections.Counter(); prev = None
        for n in order:
            x = out.get(str(n))
            if not x: continue
            tot += 1; sc = x.get('scene')
            if sc not in V['scene']: probs.append('%s: cena inválida %r' % (n, sc)); continue
            if sc in ALIAS: probs.append('%s: não use o apelido %s' % (n, sc))
            if x.get('tod') not in V['tod']: probs.append('%s: hora inválida %r' % (n, x.get('tod')))
            for d in x.get('decor') or []:
                if d not in V['decor']: probs.append('%s: decor inválido %r' % (n, d))
            if not (x.get('motivo') or '').strip(): probs.append('%s: sem motivo' % n)
            cnt[sc] += 1
            if sc == prev: probs.append('%s: mesmo cenário (%s) do episódio anterior' % (n, sc))
            prev = sc
        for sc, k in cnt.items():
            if k > 8: probs.append('%s: cenário %s usado %d vezes (máx. 8)' % (l, sc, k))
        if len(cnt) < 35: probs.append('%s: só %d cenários distintos (mín. 35)' % (l, len(cnt)))
        g = sum(k for sc, k in cnt.items() if sc in GEN)
        if g > 0.12 * max(1, sum(cnt.values())): probs.append('%s: %d%% de cenários genéricos (máx. 12%%)' % (l, round(100 * g / sum(cnt.values()))))
    print('episódios:', tot, '| problemas:', len(probs))
    for p in probs[:60]: print(' -', p)
    return 1 if probs else 0

if __name__ == '__main__': sys.exit(main(sys.argv[1:]))
