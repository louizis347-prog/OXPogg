#!/usr/bin/env python3
"""Italiano A1 (para brasileiros) no modelo piloto: reescreve os episódios escritos em tools/it/ep_*.py (mesmo molde do inglês, tools/model_v2.py).
Uso: python3 tools/model_it.py [n ...]"""
import glob, importlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import model_v2 as M  # noqa: E402
from v3 import lib  # noqa: E402

FIX = {'va': 'vai', 'è': 'sei'}


def wrong(v, form):
    if form in FIX:
        return FIX[form]
    return form[:-1] + 'i' if form[-1] in 'ae' else form + 'i'


M.LG.update(
    hint='Toque nos objetos brilhantes para ouvir o nome em italiano.', badge='A1',
    remember=('Ti ricordi?', 'De que você se lembra?'), swap=('Cambia i pezzi e fai le frasi!', 'Troque as peças e monte frases!'),
    words=('Ascolta e scegli la parola!', 'Ouça e escolha a palavra da figura!'), verbs=('Ecco i verbi di oggi!', 'Estes são os verbos de hoje!'),
    vmission=('Missione dei verbi! Ti aiuto io.', 'Missão dos verbos! Eu ajudo você.'), exps=('Ecco come si parla davvero!', 'É assim que as pessoas falam de verdade!'),
    complete=('Completa le frasi!', 'Complete as frases!'), careful=('Attenzione! Una sola è giusta.', 'Cuidado! Só uma está certa.'),
    lab=("Alleniamo l'orecchio!", 'Vamos treinar o ouvido!'), hunt=('Ascolta e trova il suono!', 'Ouça e cace o som certo!'),
    pick=('Scegli una missione! Quale vuoi?', 'Escolha uma missão! Qual você quer?'), wrong=wrong, vq='Verbo **%s** (%s) com ele/ela.')


def load_eps():
    eps = []
    for f in sorted(glob.glob(os.path.join(HERE, 'it', 'ep_*.py'))):
        m = importlib.import_module('it.' + os.path.basename(f)[:-3])
        eps += m.EPS
    return eps


def main(only=None):
    chunks, where = {}, {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'it-a1_*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        chunks[f] = d
        for i, e in enumerate(d):
            where[e['n']] = (f, i)
    eps = load_eps()
    done = 0
    for k, E in enumerate(eps):
        if only and E['n'] not in only:
            continue
        f, i = where[E['n']]
        old = chunks[f][i]
        prev = (eps[k - 1]['v2'], eps[k - 1]['extra'], eps[k - 1]['verbs']) if k else None
        M.HOTPT.update(lib.SAYPT)
        e = M.build(old, E['v2'], E['extra'], E['verbs'], prev, E['more'])
        e['presentation'] = 'regular-pilot-v1'
        e['g'] = {'t': E['v2']['base']['pattern_label']}
        chunks[f][i] = e
        done += 1
    for f, d in chunks.items():
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
    print('episódios montados:', done)


if __name__ == '__main__':
    main({int(x) for x in sys.argv[1:]} or None)
