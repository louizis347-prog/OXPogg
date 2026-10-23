#!/usr/bin/env python3
"""Piloto do modelo "Padrão do dia, em uma obra" (A1 de inglês, 5 episódios).

Reescreve os 5 episódios abaixo em 18 quadros, todos com ilustração (banner `pa`
no formato dos pôsteres procedurais que o app já usa). Mantém dos episódios
originais o cabeçalho técnico, o `soundlab` e o `snd` da capa.
Uso: python3 tools/model_pilot.py
"""
import json, glob, os, re, copy, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def pa(t, e, p='a', v=0):
    return {'pa': {'t': t, 'p': p, 'e': e, 'v': v}}


def cast_(*a):
    return {n: [i, c] for n, i, c in a}


def build_episode(old, X):
    fr_old = {f['k']: f for f in old['fr']}
    T = X['themes']  # nome do quadro -> (tema, emojis, paleta)

    def bn(k):
        t, e, p = T[k]
        return pa(t, e, p)

    fr = []
    cv = {'art': X['cover_art'], 'sub': X['cover_sub'], 'badge': 'A1',
          'snd': fr_old['cover'].get('snd', 'bell'), 'say': X['cover_say'], 'hook': X['hook']}
    fr.append(dict(k='cover', **cv))
    w = X['work']
    fr.append(dict(k='cultob', title='A obra de hoje', work=w['name'], chips=w['chips'], hook=None,
                   panels=w['panels'], say='Conheça a obra de hoje!', facts=w['facts'],
                   pa=pa(*T['cultob'])['pa'],
                   kind=w['chips'][0]))
    fr.append(dict(k='rdg', title='Descubra o padrão', s=X['rdg_s'], rule=X['rule'], q=X['rdg_q'],
                   say='Toque nas frases da obra. O que se repete? Depois, uma perguntinha!'))
    fr.append(dict(k='pat', title=X['pat_title'], sub=X['pat_sub'], tip=X['pat_tip'], pages=X['pat_pages']))
    fr.append(dict(k='vplay', title='Palavras da obra', items=X['vplay'], plan=[[i, 0] for i in range(len(X['vplay']))],
                   say='Estas palavras vêm da cena de hoje. Ouça e repita!'))
    fr.append(dict(k='sbuild', title='Trem da frase', rounds=X['sbuild'],
                   say='Trem da frase! Monte cada frase na ordem certa.'))
    fr.append(dict(k='build', title='Monte a frase', items=X['build']))
    fr.append(dict(k='order', title='Ordene o diálogo', cast=X['order_cast'], lines=X['order_lines'],
                   extra=X['order_extra']))
    fr.append(dict(k='balloons', title='Estoure os balões', ban=X['balloons_ban'], say='Ouça a pista e estoure o balão certo.',
                   intro='Listen to the clue. Pop the right balloon.', introPt='Ouça a pista. Estoure o balão certo.',
                   balloons=X['balloons'], clues=X['clues']))
    fr.append(dict(k='dictate', title='Ouça e escreva', lines=X['dictate']))
    sl = copy.deepcopy(fr_old['soundlab'])
    fr.append(dict(sl, k='soundlab'))
    fr.append(dict(k='scene', art=X['scene_art'], cast=X['cast'], lines=X['lines'], rs=X['rs']['scene']))
    fr.append(dict(k='dquiz', title='Você entendeu?', items=X['quiz'], cast=X['cast'], lines=X['lines'],
                   rs=X['rs']['scene']))
    cx = X['cultx']
    fr.append(dict(k='cultx', title='Por dentro da obra', pa=pa(*T['cultx'])['pa'],
                   work=w['name'], tag=w['chips'][0], tiles=cx, say='Abra cada cartão e descubra mais!'))
    fr.append(dict(k='scenebuild', title='Monte a cena', say='Ouça as ordens e coloque cada objeto no lugar certo.',
                   intro='Ouça com atenção. Toque no objeto e depois no lugar.', items=X['sb_items'], spots=X['sb_spots'],
                   rounds=X['sb_rounds']))
    pr = dict(X['produce'])
    fr.append(dict(k='produce', title='Sua vez!', **pr))
    fr.append(dict(k='review', prev=X['review']['prev'], work=X['review']['work'], recap=X['review']['recap'],
                   bag=X['review']['bag'], lead='Abra cada bolso da mochila e relembre o episódio anterior!',
                   next='Hoje: **%s**' % X['pattern_label'], say='Bora relembrar o episódio anterior antes de seguir!'))
    fr.append(dict(k='wrap', title='Para levar', recap=X['wrap_recap'], teaser=X['teaser']))
    RS_K = X['rs']
    for f in fr:
        if f['k'] in RS_K and f['k'] not in ('scene',):
            f['rs'] = RS_K[f['k']]
    e = copy.deepcopy(old)
    e['t'] = X['title']
    e['s'] = X['sub']
    e['a'] = {'k': w['chips'][0], 'w': w['name'], 'y': w['year'], 'd': w['panels'][0]}
    e['h'] = {'l': X['hook'][0], 'src': w['name'], 'tr': X['hook'][1]}
    e['p'] = X['why']
    e['v'] = X['vocab']
    e['fr'] = fr
    e['pilot'] = 1
    if X.get('sc'):
        e['sc'] = X['sc']
    return e


def L(en, pt):
    return [en, pt]


# ---------------------------------------------------------------------------
from model_pilot_data import EPISODES  # noqa: E402


def main():
    by_file = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'en-a1_*.json'))):
        by_file[f] = json.load(open(f, encoding='utf-8'))
    done = 0
    for X in EPISODES:
        for f, d in by_file.items():
            for i, e in enumerate(d):
                if e['n'] == X['n']:
                    d[i] = build_episode(e, X)
                    done += 1
    for f, d in by_file.items():
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
    print('episódios reescritos:', done)


if __name__ == '__main__':
    main()
