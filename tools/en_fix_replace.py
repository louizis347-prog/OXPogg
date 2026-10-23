#!/usr/bin/env python3
"""Desfaz o dano da troca de nomes feita por tools/en_repair.py nos textos corridos.

A troca "nome antigo -> obra canônica" era para os textos de apoio (`coach`), mas também alterou frases normais
(ex.: "...no pedestal da Estátua da Liberdade, em Nova York." virou "..., em The New Colossus."). Este script
compara com a versão anterior (commit `BASE`) e restaura cada texto cuja única diferença é essa troca.
"""
import json, os, subprocess

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
BASE = 'c2b8e31d~1'
SK = {'art', 'c', 'seed', 'cam', 'scene', 'pa'}
SKIP_KEYS = {'coach', 'levelProgression', 'work', 'text', 'previous', 'nextLine', 'pragmatics', 'n', 'k', 'y', 'd', 'tag', 'kind', 'chips'}


def olds_of(e):
    o = set()
    for x in e['fr']:
        if x['k'] == 'cultob' and x.get('work'):
            o.add(x['work'])
        if x['k'] == 'culttl':
            for w in x.get('works', []):
                if w.get('t') == 'main work' and w.get('n'):
                    o.add(w['n'])
    return o


def fix(cur, pre, canon, olds, key=None):
    if isinstance(cur, str) and isinstance(pre, str):
        if key in SKIP_KEYS or cur == pre:
            return cur, 0
        for o in olds:
            if o != canon and o in pre and pre.replace(o, canon) == cur:
                return pre, 1
        return cur, 0
    if isinstance(cur, list) and isinstance(pre, list) and len(cur) == len(pre):
        n = 0
        for i in range(len(cur)):
            cur[i], k = fix(cur[i], pre[i], canon, olds, key)
            n += k
        return cur, n
    if isinstance(cur, dict) and isinstance(pre, dict):
        n = 0
        for k in cur:
            if k in pre and k not in SK:
                cur[k], c = fix(cur[k], pre[k], canon, olds, k)
                n += c
        return cur, n
    return cur, 0


def main():
    m = json.load(open(os.path.join(ROOT, 'manifest.json'), encoding='utf-8'))
    total = 0
    for lv in ['a1', 'a2', 'b1', 'b2', 'c1', 'c2']:
        for b in m['en-' + lv]:
            p = os.path.join(ROOT, b)
            new = json.load(open(p, encoding='utf-8'))
            try:
                old = json.loads(subprocess.check_output(['git', 'show', '%s:data/%s' % (BASE, b)], stderr=subprocess.DEVNULL))
            except Exception:
                continue
            ch = 0
            for en, eo in zip(new, old):
                if en['n'] != eo['n']:
                    continue
                olds = olds_of(eo)
                canon = next((x.get('work') for x in en['fr'] if x['k'] == 'cultob'), None)
                if not canon:
                    continue
                for xn, xo in zip(en['fr'], eo['fr']):
                    if xn['k'] == xo['k'] and xn['k'] in ('cultob', 'cultx', 'cultcena', 'cultgame', 'culttl', 'bridge', 'wrap', 'fio'):
                        _, c = fix(xn, xo, canon, olds)
                        ch += c
            if ch:
                open(p, 'w', encoding='utf-8').write(json.dumps(new, ensure_ascii=False, separators=(',', ':')))
                total += ch
    print('textos restaurados:', total)


if __name__ == '__main__':
    main()
