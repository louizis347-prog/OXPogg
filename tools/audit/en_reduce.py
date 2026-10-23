#!/usr/bin/env python3
"""Reduz o inglês regular (en-a1…en-c2) de 5.000 para 3.000 episódios, proporcionalmente por nível e por arco.

Regras:
 - o corte é feito em PARES (principal + continuação), nunca separa um do outro;
 - o início de cada arco (e o par dele) fica sempre;
 - pares com episódios no modelo piloto (pilot=1) e os pares ligados a eles ficam sempre;
 - dentro de cada arco, escolhe os pares que mais preservam o vocabulário (palavras, padrões e obras ainda não cobertos);
 - o quadro `review` ("episódio anterior") dos episódios mantidos é refeito a partir do novo episódio anterior.
Uso: python3 tools/audit/en_reduce.py [--apply]   (sem --apply só imprime o relatório)
"""
import collections, copy, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from en_audit import ROOT, LV, load, arcs, words, pairs_of  # noqa: E402
import reg3  # noqa: E402

TARGET = {'en-a1': 466, 'en-a2': 474, 'en-b1': 530, 'en-b2': 510, 'en-c1': 510, 'en-c2': 510}  # itens (=2 por par), soma 3.000
HOLD = 0.6


def pattern_of(x):
    return (x.get('g') or {}).get('t') or x.get('pattern') or x['t']


def work_of(x):
    return (x.get('a') or {}).get('w') or ''


def split_arcs(P, starts):
    """Agrupa os pares em arcos pelo n do principal que abre cada arco."""
    idx = {g[0]['n']: i for i, g in enumerate(P)}
    cuts = sorted(idx[n] for n in starts if n in idx)
    out = []
    for a, b in zip(cuts, cuts[1:] + [len(P)]):
        out.append(list(range(a, b)))
    return out


def quotas(sizes, forced, total):
    """Cota de pares por arco: proporcional a 60% do tamanho, respeitando o mínimo dos pares obrigatórios."""
    q = list(forced)
    rest = total - sum(q)
    w = [max(0.0, HOLD * s - f) for s, f in zip(sizes, forced)]
    tw = sum(w) or 1
    raw = [rest * x / tw for x in w]
    base = [int(r) for r in raw]
    left = rest - sum(base)
    order = sorted(range(len(raw)), key=lambda i: raw[i] - base[i], reverse=True)
    for i in order[:left]:
        base[i] += 1
    return [a + b for a, b in zip(q, base)]


def choose(c, it, A):
    P, orph = pairs_of(it)
    assert not orph
    starts = [a[0] for a in A[c]]
    arcs_ = split_arcs(P, starts)
    assert sum(len(a) for a in arcs_) == len(P), (c, sum(len(a) for a in arcs_), len(P))
    pilot_idx = {i for i, g in enumerate(P) if any(x.get('pilot') for x in g)}
    # pares vizinhos que formam a cadeia de revisão dos pilotos (o episódio anterior de um piloto)
    keep_forced = set(pilot_idx)
    for i in list(pilot_idx):
        if i - 1 >= 0 and i - 1 not in pilot_idx and any(x.get('pilot') and x['fr'][1]['k'] == 'review' and x['fr'][1].get('prev') == P[i - 1][0]['t'] for x in P[i]):
            keep_forced.add(i - 1)
    for a in arcs_:
        keep_forced.add(a[0])
    keep_forced.add(len(P) - 1)  # fechamento do nível (os níveis seguintes revisam esse episódio)
    df = collections.Counter(w for g in P for w in set(words(g[0])))
    total_pairs = TARGET[c] // 2
    forced_by_arc = [sum(1 for i in a if i in keep_forced) for a in arcs_]
    qs = quotas([len(a) for a in arcs_], forced_by_arc, total_pairs)
    covered, pats, works = set(), set(), set()
    sel = set()
    for i in sorted(keep_forced):
        sel.add(i)
        covered |= set(words(P[i][0])); pats.add(pattern_of(P[i][0])); works.add(work_of(P[i][0]))
    for a, q in zip(arcs_, qs):
        have = [i for i in a if i in sel]
        while len(have) < q:
            best, bs = None, -1
            for i in a:
                if i in sel:
                    continue
                g = P[i][0]
                s = sum(1.0 / df[w] for w in set(words(g)) if w not in covered)
                s += 0.8 * (pattern_of(g) not in pats) + 0.5 * (work_of(g) not in works) + 0.01 * (len(a) - a.index(i)) / len(a)
                if s > bs:
                    best, bs = i, s
            g = P[best][0]
            sel.add(best); have.append(best)
            covered |= set(words(g)); pats.add(pattern_of(g)); works.add(work_of(g))
    return P, arcs_, sel, qs


def stats(items):
    voc = collections.Counter(w for x in items for w in words(x))
    return dict(items=len(items), vocab=len(voc), pats=len({pattern_of(x) for x in items}), works=len({work_of(x) for x in items}))


def main(apply):
    A = arcs()
    summary = {}
    new_data = {}
    for c in LV:
        it = load(c)
        P, arcs_, sel, qs = choose(c, it, A)
        kept = [x for i, g in enumerate(P) for x in g if i in sel]
        before, after = stats(it), stats(kept)
        summary[c] = (before, after, len(arcs_))
        print('%s: itens %d → %d | pares %d → %d | arcos %d (todos mantidos) | vocabulário único %d → %d (%.1f%%) | padrões %d → %d (%.1f%%) | obras %d → %d (%.1f%%)' % (
            c, before['items'], after['items'], len(P), len(sel), len(arcs_), before['vocab'], after['vocab'], 100 * after['vocab'] / before['vocab'],
            before['pats'], after['pats'], 100 * after['pats'] / before['pats'], before['works'], after['works'], 100 * after['works'] / before['works']))
        # revisão do episódio anterior: segue a cadeia original (x → episódio que x revisa)
        pos = {x['n']: i for i, x in enumerate(it)}
        pred = {}
        for i, x in enumerate(it):
            rv = next((f for f in x['fr'] if f['k'] == 'review'), None)
            if rv:
                for j in range(i - 1, -1, -1):
                    if it[j]['t'] == rv.get('prev'):
                        pred[x['n']] = it[j]['n']
                        break
        succ_review = {}
        for n, q in pred.items():
            succ_review.setdefault(q, next(f for f in it[pos[n]]['fr'] if f['k'] == 'review'))
        keptset = {x['n'] for x in kept}
        fixed = dropped = 0
        out = []
        for x in kept:
            rv = next((f for f in x['fr'] if f['k'] == 'review'), None)
            if rv and x['n'] in pred and pred[x['n']] not in keptset:
                a_ = pred[x['n']]
                while a_ in pred and a_ not in keptset:
                    a_ = pred[a_]
                x = copy.deepcopy(x)
                src = succ_review.get(a_) if a_ in keptset else None
                if src:
                    new = copy.deepcopy(src)
                    new['next'] = rv.get('next', new.get('next'))
                    if 'coach' in rv:
                        new['coach'] = rv['coach']
                    x['fr'][x['fr'].index(next(f for f in x['fr'] if f['k'] == 'review'))] = new
                    fixed += 1
                else:
                    x['fr'] = [f for f in x['fr'] if f['k'] != 'review']
                    dropped += 1
            out.append(x)
        print('   revisões refeitas: %d | removidas (sem origem): %d' % (fixed, dropped))
        new_data[c] = out
    tot = sum(len(v) for v in new_data.values())
    print('TOTAL itens:', tot)
    if apply:
        for c, out in new_data.items():
            tmp = '/tmp/_red_%s.json' % c
            json.dump(out, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
            reg3.data(c, tmp)
        print('gravado')


if __name__ == '__main__':
    main('--apply' in sys.argv)
