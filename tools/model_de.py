#!/usr/bin/env python3
"""Alemão A1 (para brasileiros) no modelo piloto: reescreve os episódios escritos em tools/de/ep_*.py (mesmo molde do inglês, tools/model_v2.py).
Uso: python3 tools/model_de.py [n ...]"""
import glob, importlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import model_v2 as M  # noqa: E402
from v3 import lib  # noqa: E402

FIX = {'ist': 'bist', 'hat': 'hast'}


def wrong(v, form):
    if form in FIX:
        return FIX[form]
    return form[:-1] + 'st' if form.endswith('t') else form + 'st'


M.LG.update(
    hint='Toque nos objetos brilhantes para ouvir o nome em alemão.', badge='A1',
    remember=('Erinnerst du dich?', 'De que você se lembra?'), swap=('Tausche die Teile und bilde Sätze!', 'Troque as peças e monte frases!'),
    words=('Hör zu und wähle das Wort!', 'Ouça e escolha a palavra da figura!'), verbs=('Das sind die Verben von heute!', 'Estes são os verbos de hoje!'),
    vmission=('Verben-Mission! Ich helfe dir.', 'Missão dos verbos! Eu ajudo você.'), exps=('So spricht man wirklich!', 'É assim que as pessoas falam de verdade!'),
    complete=('Ergänze die Sätze!', 'Complete as frases!'), careful=('Vorsicht! Nur einer ist richtig.', 'Cuidado! Só uma está certa.'),
    lab=('Wir trainieren das Gehör!', 'Vamos treinar o ouvido!'), hunt=('Hör zu und finde den Laut!', 'Ouça e cace o som certo!'),
    pick=('Wähle eine Mission! Welche willst du?', 'Escolha uma missão! Qual você quer?'), wrong=wrong, vq='Verbo **%s** (%s) com ele/ela.')


def load_eps():
    eps = []
    for f in sorted(glob.glob(os.path.join(HERE, 'de', 'ep_*.py'))):
        m = importlib.import_module('de.' + os.path.basename(f)[:-3])
        eps += m.EPS
    return eps


def main(only=None):
    chunks, where = {}, {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'de-a1_*.json'))):
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
