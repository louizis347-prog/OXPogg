#!/usr/bin/env python3
"""Varia o esqueleto das telas das aulas ao vivo (data/v4), SEM remover conteúdo e SEM sair da etapa de cada tela.
Reordena só dentro de cada etapa (contexto, leitura, laboratório, escrita), de forma determinística por aula e idempotente
(roda quantas vezes quiser; reconstrói sempre a partir de uma ordem canônica). Fica FORA da variação: abertura, diálogo e
telas de resposta, laboratório de sons, missão ao vivo, saída e conclusão.
Uso: python3 professor/tools/vary_skeleton.py [--dry]   (rodar por último, depois de enrich_v6.py)"""
import collections, glob, hashlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); V4 = os.path.join(HERE, '..', 'data', 'v4')
DRY = '--dry' in sys.argv
def h(*a): return int(hashlib.md5('|'.join(map(str, a)).encode()).hexdigest()[:8], 16)

CULT_RANK = {'bridge': 0, 'facts': 1, 'compare': 2, 'artifact': 3}
CULT_ORDERS = [(0, 1, 2, 3), (1, 2, 0, 3), (0, 3, 1, 2), (1, 0, 3, 2), (3, 1, 2, 0), (2, 1, 0, 3)]   # permutações dos 4 tipos
LAB_BLOCK = {'vocab': 'V', 'verbs': 'B', 'verbplay': 'B', 'exprs': 'E', 'exprplay': 'E', 'pattern': 'P'}
LAB_ORDERS = ['VBEP', 'EVBP', 'VEBP', 'BVEP', 'EBVP', 'VBPE', 'PVBE']
WRITE_ORDERS = [('pattern', 'writing', 'me'), ('writing', 'pattern', 'me'), ('pattern', 'writing', 'me')]

def vary(d):
    n = d['n']; pages = d['pages']; out = list(pages); code = []
    def seg(stage):
        idx = [i for i, p in enumerate(pages) if p.get('stage') == stage]
        return idx
    # CONTEXTO: work e story ficam no início; o 'mito ou fato' (último quiz) fecha; o meio gira
    idx = [i for i, p in enumerate(pages) if p['kind'] in ('bridge', 'facts', 'compare', 'artifact') and p['stage'] in ('culture', 'mission')]
    if len(idx) >= 3 and idx == list(range(idx[0], idx[-1] + 1)):
        mid = sorted([pages[i] for i in idx], key=lambda p: (CULT_RANK[p['kind']], pages.index(p)))
        k = h(n, 'c') % len(CULT_ORDERS); order = CULT_ORDERS[k]
        rank_pos = {r: j for j, r in enumerate(order)}
        mid2 = sorted(mid, key=lambda p: (rank_pos[CULT_RANK[p['kind']]], mid.index(p)))
        for j, i in enumerate(idx): out[i] = mid2[j]
        code.append('C%d' % k)
    # LEITURA: os dois quizzes depois dos três trechos podem trocar de ordem
    ridx = [i for i, p in enumerate(pages) if p['stage'] == 'read' and p['kind'] == 'quiz']
    if len(ridx) == 2:
        qs = sorted([pages[i] for i in ridx], key=lambda p: p.get('title', ''))      # ordem canônica por título
        if h(n, 'r') % 2: qs = qs[::-1]; code.append('R1')
        out[ridx[0]], out[ridx[1]] = qs[0], qs[1]
    # LABORATÓRIO: blocos V(ocabulário) B(verbos) E(xpressões) P(adrões); laboratório de sons continua por último
    lidx = [i for i, p in enumerate(pages) if p['stage'] == 'lab' and p['kind'] in LAB_BLOCK]
    if lidx and lidx == list(range(lidx[0], lidx[-1] + 1)):
        base = [pages[i] for i in lidx]
        k = h(n, 'l') % len(LAB_ORDERS); order = LAB_ORDERS[k]
        res = []
        for b in order: res += [p for p in base if LAB_BLOCK[p['kind']] == b]
        for j, i in enumerate(lidx): out[i] = res[j]
        code.append('L%d' % k)
    # ESCRITA: padrão e escrita podem trocar; "Sobre você · final" fecha
    widx = [i for i, p in enumerate(pages) if p['stage'] == 'write']
    kinds = [pages[i]['kind'] for i in widx]
    if sorted(kinds) == ['me', 'pattern', 'writing'] and widx == list(range(widx[0], widx[-1] + 1)):
        k = h(n, 'w') % 3
        order = WRITE_ORDERS[k]; byk = {pages[i]['kind']: pages[i] for i in widx}
        for j, i in enumerate(widx): out[i] = byk[order[j]]
        code.append('W%d' % (k % 2))
    return out, '-'.join(code) or 'base'

if __name__ == '__main__':
    skel = collections.Counter()
    for f in sorted(glob.glob(os.path.join(V4, '[0-9]*.json'))):
        d = json.load(open(f)); old = [p['kind'] for p in d['pages']]
        # reconstrói a partir de uma ordem canônica: aplica a variação sobre as telas na ordem em que estão (permutações só dentro de cada bloco)
        out, code = vary(d)
        assert sorted(map(id, out)) == sorted(map(id, d['pages'])), 'telas perdidas em %s' % f
        d['pages'] = out; d['skel'] = code
        new = [p['kind'] for p in out]; skel[tuple(new)] += 1
        assert sorted(map(id, out)) == sorted(map(id, d['pages'])), 'telas perdidas em %s' % f
        if not DRY: json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    print('aulas:', sum(skel.values()), '| sequências de telas distintas:', len(skel), '| a mais comum cobre %d%%' % round(100 * skel.most_common(1)[0][1] / sum(skel.values())))
