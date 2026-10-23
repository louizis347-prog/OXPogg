#!/usr/bin/env python3
"""Aplica a redação do piloto A1 (tools/pilot_a1/out_NN.json) nas aulas de regra do inglês A1.

Em cada aula: a "linha do tempo" de uma só obra (culttl) dá lugar a um quiz de compreensão da cena (dquiz) e o
quadro de escrita de 2 palavras (wlat) dá lugar à produção guiada (produce, com chips, modelo e checklist),
mantendo 20 quadros. Aulas que já tinham `produce` só ganham o quiz.
"""
import copy, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import en_pilot_validate as V

ROOT = os.path.join(HERE, '..', 'data')
D = os.path.join(HERE, 'pilot_a1')


def kw_for(chip):
    chip = chip.strip().strip('.?!,')
    toks = [re.escape(t).replace("\\'", "['’]").replace("’", "['’]") for t in chip.split()]
    return r'\b' + r'\s+'.join(toks) + r'\b'


def reorder(e):
    """o quiz vem logo depois da cena que ele pergunta; a produção fecha a prática (antes do fio da história)"""
    fr = e['fr']
    ks = [x['k'] for x in fr]
    if 'scene' not in ks:
        return False
    before = list(ks)
    if 'dquiz' in ks:
        dq = fr.pop(ks.index('dquiz'))
        fr.insert([x['k'] for x in fr].index('scene') + 1, dq)
    ks = [x['k'] for x in fr]
    if 'produce' in ks and 'fio' in ks:
        pr = fr.pop(ks.index('produce'))
        fr.insert([x['k'] for x in fr].index('fio'), pr)
    return [x['k'] for x in fr] != before


def main():
    out = {}
    for f in sorted(glob.glob(os.path.join(D, 'out_*.json'))):
        n = os.path.basename(f)[4:6]
        inp = json.load(open(os.path.join(D, 'in_%s.json' % n), encoding='utf-8'))
        data = json.load(open(f, encoding='utf-8'))
        err = V.check(inp, data)
        if err:
            print('lote', n, 'com erros:', len(err)); print('\n'.join(err[:10])); sys.exit(1)
        out.update({o['n']: o for o in data})
    m = json.load(open(os.path.join(ROOT, 'manifest.json'), encoding='utf-8'))
    done = 0
    for b in m['en-a1']:
        p = os.path.join(ROOT, b)
        d = json.load(open(p, encoding='utf-8'))
        ch = False
        for e in d:
            o = out.get(e['n'])
            if not o:
                continue
            idx = {x['k']: i for i, x in enumerate(e['fr'])}
            sc = e['fr'][idx['scene']]
            s = e.get('s') or e['t']
            if 'dquiz' not in idx and 'culttl' in idx:
                e['fr'][idx['culttl']] = {'k': 'dquiz', 'title': 'Você entendeu?', 'items': copy.deepcopy(o['dquiz']),
                                          'cast': copy.deepcopy(sc['cast']), 'lines': copy.deepcopy(sc['lines']),
                                          'rs': sc.get('rs', 'cafe'),
                                          'coach': 'Transfira a habilidade para %s: tente uma versão natural e outra mais cuidadosa.' % s}
                ch = True
            if 'produce' not in idx and 'wlat' in idx:
                pr = o['produce']
                e['fr'][idx['wlat']] = {'k': 'produce', 'title': 'Sua vez!', 'prompt': pr['prompt'], 'ph': pr['ph'],
                                        'chips': pr['chips'], 'model': pr['model'], 'check': pr['check'],
                                        'kw': [kw_for(c) for c in pr['chips']],
                                        'cul': ['🎤', 'Sua vez', 'Produzir é a melhor forma de lembrar: fale em voz alta e depois escreva.'],
                                        'coach': 'Fechamento do episódio: retome %s e prepare a próxima situação.' % s}
                ch = True
            if o and reorder(e):
                ch = True
            if ch:
                done += 1
        if ch:
            open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
    print('aulas atualizadas:', done)


if __name__ == '__main__':
    main()
