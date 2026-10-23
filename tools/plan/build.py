#!/usr/bin/env python3
"""Planejamento por episódio dos cursos regulares (exceto inglês, que usa tools/roteiro).
Entrada: tools/plan/<curso>/<nivel>_NN.txt, uma linha por episódio:
  n|título|tema|estrutura gramatical|6 palavras (palavra{leitura}=pt;...)|4 verbos (v=pt;...)|4 expressões (x=pt;...)|2 gírias/coloquiais (x=pt;...)
Saída: data/plan/<curso>.json  {n: {...}}  (lido pela tela de pré-episódio e pelo PDF). Também confere repetição."""
import glob, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
LV = ['a1', 'a2', 'b1', 'b2', 'c1', 'c2']
M = json.load(open('data/manifest.json'))

def pairs(t):
    out = []
    for p in (x.strip() for x in t.split(';')):
        if p:
            a, _, b = p.partition('=')
            out.append([a.strip(), b.strip()])
    return out

def build(cid):
    plan, err = {}, []
    for f in sorted(glob.glob('tools/plan/%s/*.txt' % cid)):
        for i, ln in enumerate(open(f, encoding='utf-8'), 1):
            ln = ln.strip()
            if not ln: continue
            p = ln.split('|')
            if len(p) != 8: err.append((f, i, 'campos', len(p))); continue
            n, ti, te, es, vo, vb, ex, gi = p
            d = dict(t=ti, tema=te, gram=es, vocab=pairs(vo), verbos=pairs(vb), exp=pairs(ex), gir=pairs(gi))
            if len(d['vocab']) != 6 or len(d['verbos']) != 4 or len(d['exp']) != 4 or len(d['gir']) != 2:
                err.append((f, i, 'contagem', len(d['vocab']), len(d['verbos']), len(d['exp']), len(d['gir']))); continue
            plan[int(n)] = d
    json.dump(plan, open('data/plan/%s.json' % cid, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    rep = {}
    seen = {}
    for n, d in plan.items():
        k = tuple(w[0] for w in d['vocab'])
        seen.setdefault(k, []).append(n)
    dup = sum(len(v) for v in seen.values() if len(v) > 1)
    tot = {lv: sum(1 for f in M['%s-%s' % (cid, lv)] for x in json.load(open('data/' + f))) for lv in LV}
    have = {lv: sum(1 for f in M['%s-%s' % (cid, lv)] for x in json.load(open('data/' + f)) if x['n'] in plan) for lv in LV}
    return plan, err, dup, tot, have

if __name__ == '__main__':
    for cid in (sys.argv[1:] or [d for d in os.listdir('tools/plan') if os.path.isdir('tools/plan/' + d)]):
        plan, err, dup, tot, have = build(cid)
        print(cid, 'episódios com roteiro:', len(plan), ' '.join('%s %d/%d' % (lv, have[lv], tot[lv]) for lv in LV), '| vocab repetido:', dup, '| erros:', err[:5])
