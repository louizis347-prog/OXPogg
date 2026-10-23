#!/usr/bin/env python3
"""Espanhol A1 (para brasileiros) no modelo piloto: reescreve os episódios escritos em tools/es/ep_*.py (mesmo molde do inglês, tools/model_v2.py).
Uso: python3 tools/model_es.py [n ...]"""
import glob, importlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import model_v2 as M  # noqa: E402
from v3 import lib  # noqa: E402

FIX = {'es': 'eres'}


def wrong(v, form):
    if form in FIX:
        return FIX[form]
    return form[:-1] + 'n' if form.endswith('s') else form + 's'


M.LG.update(
    hint='Toque nos objetos brilhantes para ouvir o nome em espanhol.', badge='A1',
    remember=('¿Qué recuerdas?', 'De que você se lembra?'), swap=('¡Cambia las piezas y forma frases!', 'Troque as peças e monte frases!'),
    words=('¡Escucha y elige la palabra!', 'Ouça e escolha a palavra da figura!'), verbs=('¡Estos son los verbos de hoy!', 'Estes são os verbos de hoje!'),
    vmission=('¡Misión de verbos! Yo te ayudo.', 'Missão dos verbos! Eu ajudo você.'), exps=('¡Así habla la gente de verdad!', 'É assim que as pessoas falam de verdade!'),
    complete=('¡Completa las frases!', 'Complete as frases!'), careful=('¡Cuidado! Solo una es correcta.', 'Cuidado! Só uma está certa.'),
    lab=('¡Vamos a entrenar el oído!', 'Vamos treinar o ouvido!'), hunt=('¡Escucha y caza el sonido!', 'Ouça e cace o som certo!'),
    pick=('¡Elige una misión! ¿Cuál quieres?', 'Escolha uma missão! Qual você quer?'), wrong=wrong, vq='Verbo **%s** (%s) com él/ella.')


def load_eps():
    eps = []
    for f in sorted(glob.glob(os.path.join(HERE, 'es', 'ep_*.py'))):
        m = importlib.import_module('es.' + os.path.basename(f)[:-3])
        eps += m.EPS
    return eps


def main(only=None):
    chunks, where = {}, {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'es-a1_*.json'))):
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
