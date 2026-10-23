#!/usr/bin/env python3
"""Valida a redação de um lote do piloto A1.  Uso: python3 tools/en_pilot_validate.py NN  (lê in_NN.json e out_NN.json)"""
import json, os, re, sys

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pilot_a1')


def check(inp, out):
    err = []
    by = {o['n']: o for o in out}
    for r in inp:
        o = by.get(r['n'])
        if not o:
            err.append('%s: faltando' % r['n']); continue
        lines = r['scene']
        dq = o.get('dquiz')
        if not isinstance(dq, list) or len(dq) != 3:
            err.append('%s: dquiz precisa de 3 itens' % r['n'])
        else:
            usedline = set()
            for i, it in enumerate(dq):
                p = '%s dquiz[%d]' % (r['n'], i)
                for k in ('q', 'pt', 'opts', 'a', 'line', 'why'):
                    if k not in it:
                        err.append('%s: falta %s' % (p, k))
                if any(k not in it for k in ('q', 'pt', 'opts', 'a', 'line', 'why')):
                    continue
                if not (isinstance(it['opts'], list) and len(it['opts']) == 3 and all(isinstance(x, list) and len(x) == 2 and all(isinstance(y, str) and y.strip() for y in x) for x in it['opts'])):
                    err.append('%s: opts deve ser 3 pares [emoji, texto]' % p)
                elif len({x[1].lower() for x in it['opts']}) != 3:
                    err.append('%s: opções repetidas' % p)
                if it['a'] != 0:
                    err.append('%s: a deve ser 0 (a correta vem primeiro)' % p)
                if not isinstance(it['line'], int) or not 0 <= it['line'] < len(lines):
                    err.append('%s: line fora da cena' % p)
                else:
                    quote = re.findall(r'“([^”]+)”', it['why'])
                    if not quote or not any(q.strip(' .!?,').lower() in lines[it['line']][1].lower() for q in quote):
                        err.append('%s: why deve citar entre “ ” um trecho da fala %d (%s)' % (p, it['line'], lines[it['line']][1]))
                    usedline.add(it['line'])
                if not re.search(r'[A-Za-z]', it['q']) or not it['q'].strip().endswith('?'):
                    err.append('%s: q deve ser uma pergunta em inglês terminada em ?' % p)
            if len(usedline) < 2:
                err.append('%s: use falas diferentes nas perguntas' % r['n'])
        pr = o.get('produce')
        if not isinstance(pr, dict):
            err.append('%s: produce ausente' % r['n']); continue
        for k in ('prompt', 'ph', 'chips', 'model', 'check'):
            if k not in pr:
                err.append('%s produce: falta %s' % (r['n'], k))
        if all(k in pr for k in ('prompt', 'ph', 'chips', 'model', 'check')):
            if '**' not in pr['prompt']:
                err.append('%s produce: prompt precisa de **tarefa em negrito**' % r['n'])
            if not (isinstance(pr['chips'], list) and len(pr['chips']) == 3):
                err.append('%s produce: 3 chips' % r['n'])
            if not (isinstance(pr['check'], list) and len(pr['check']) == 3):
                err.append('%s produce: 3 itens em check' % r['n'])
            if isinstance(pr['chips'], list):
                low = pr['model'].lower()
                for c in pr['chips']:
                    if c.lower().strip('.?!') not in low:
                        err.append('%s produce: o modelo deve conter o chip “%s”' % (r['n'], c))
            if len(pr['model'].split()) < 6:
                err.append('%s produce: modelo muito curto' % r['n'])
    return err


if __name__ == '__main__':
    n = sys.argv[1]
    inp = json.load(open(os.path.join(D, 'in_%s.json' % n), encoding='utf-8'))
    out = json.load(open(os.path.join(D, 'out_%s.json' % n), encoding='utf-8'))
    e = check(inp, out)
    print('OK: %d episódios' % len(out) if not e else '\n'.join(e[:60]) + '\n%d erros' % len(e))
    sys.exit(1 if e else 0)
