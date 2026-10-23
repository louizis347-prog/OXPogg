#!/usr/bin/env python3
"""Francês A1 (para brasileiros) no modelo piloto: reescreve os episódios escritos em tools/fr/ep_*.py (mesmo molde do inglês, tools/model_v2.py).
Uso: python3 tools/model_fr.py [n ...]"""
import glob, importlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import model_v2 as M  # noqa: E402
from v3 import lib  # noqa: E402

FIX = {'est': 'es'}


def wrong(v, form):
    if form in FIX:
        return FIX[form]
    return form + 's' if form.endswith('e') else (form[:-1] + 's' if form.endswith('t') else form + 's')


M.LG.update(
    hint='Toque nos objetos brilhantes para ouvir o nome em francês.', badge='A1',
    remember=('Tu te souviens ?', 'De que você se lembra?'), swap=('Change les pièces et fais des phrases !', 'Troque as peças e monte frases!'),
    words=('Écoute et choisis le mot !', 'Ouça e escolha a palavra da figura!'), verbs=("Voici les verbes d'aujourd'hui !", 'Estes são os verbos de hoje!'),
    vmission=("Mission des verbes ! Je t'aide.", 'Missão dos verbos! Eu ajudo você.'), exps=('Voilà comment on parle vraiment !', 'É assim que as pessoas falam de verdade!'),
    complete=('Complète les phrases !', 'Complete as frases!'), careful=('Attention ! Une seule est juste.', 'Cuidado! Só uma está certa.'),
    lab=("On entraîne l'oreille !", 'Vamos treinar o ouvido!'), hunt=('Écoute et trouve le son !', 'Ouça e cace o som certo!'),
    pick=('Choisis une mission ! Laquelle veux-tu ?', 'Escolha uma missão! Qual você quer?'), wrong=wrong, vq='Verbo **%s** (%s) com il/elle.')


def load_eps():
    eps = []
    for f in sorted(glob.glob(os.path.join(HERE, 'fr', 'ep_*.py'))):
        m = importlib.import_module('fr.' + os.path.basename(f)[:-3])
        eps += m.EPS
    return eps


def main(only=None):
    chunks, where = {}, {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'frbr-a1_*.json'))):
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
