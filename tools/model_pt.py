#!/usr/bin/env python3
"""Português (Brasil) A1 para hispanofalantes no modelo piloto: tools/pt/ep_*.py (interface em espanhol). Uso: python3 tools/model_pt.py [n ...]"""
import glob, importlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import model_v2 as M  # noqa: E402
from v3 import lib  # noqa: E402

FIX = {'é': 'es', 'tem': 'tiene', 'quer': 'quiere', 'faz': 'hace', 'vai': 'va', 'vê': 've'}


def wrong(v, form):
    return FIX.get(form, form + 's')


UI = {
    'Explore a cena': 'Explora la escena', 'Toque nos objetos brilhantes!': '¡Toca los objetos brillantes!',
    'Abra cada bolso da mochila e relembre o episódio anterior!': '¡Abre cada bolsillo de la mochila y recuerda el episodio anterior!',
    'Bora relembrar o episódio anterior antes de seguir!': '¡Vamos a recordar el episodio anterior antes de seguir!', 'Hoje: **%s**': 'Hoy: **%s**',
    'Ouça a cena e leia junto.': 'Escucha la escena y lee con ella.', 'Você entendeu?': '¿Entendiste?',
    'Veja o padrão com figuras e ouça os exemplos.': 'Mira el patrón con figuras y escucha los ejemplos.', 'Molde de frases': 'Moldes de frases',
    'Toque nas peças e veja várias frases.': 'Toca las piezas y mira varias frases.', 'Palavras da cena': 'Palabras de la escena', 'Qual é a palavra?': '¿Cuál es la palabra?',
    'Vamos ver os verbos de hoje!': '¡Vamos a ver los verbos de hoy!', 'Missão dos verbos': 'Misión de los verbos', 'Missão dos verbos: 7 passos. Eu ajudo você!': 'Misión de los verbos: 7 pasos. ¡Yo te ayudo!',
    'Expressões e gírias': 'Expresiones y jergas', 'Toque para ouvir cada expressão.': 'Toca para escuchar cada expresión.', 'Na conversa de verdade': 'En la conversación de verdad',
    'Veja as expressões em uso. Elas estão destacadas.': 'Mira las expresiones en uso. Están resaltadas.', 'Complete as falas': 'Completa las frases', 'Qual está certa?': '¿Cuál es la correcta?',
    'Caça-sons': 'Caza-sonidos', 'Sua vez de falar': 'Tu turno de hablar', 'Ouça cada frase e repita em voz alta.': 'Escucha cada frase y repítela en voz alta.',
    'Cena da obra': 'Escena de la obra', 'Fale como os personagens.': 'Habla como los personajes.', 'Escreva a sua resposta aqui…': 'Escribe tu respuesta aquí…',
    'Missão: sua vez!': 'Misión: ¡tu turno!', 'Escolha uma missão e mostre o que você aprendeu!': '¡Elige una misión y muestra lo que aprendiste!', 'Para levar': 'Para llevar',
    'Padrão': 'Patrón', 'Palavras': 'Palabras', 'Verbos': 'Verbos', 'Expressões': 'Frases', 'Sons': 'Sonidos',
}
M.LG.update(
    ui=UI, hint='Toca los objetos brillantes para escuchar el nombre en portugués.', badge='A1',
    remember=('O que você lembra?', '¿Qué recuerdas?'), swap=('Troque as peças e monte frases!', '¡Cambia las piezas y arma frases!'),
    words=('Ouça e escolha a palavra!', '¡Escucha y elige la palabra!'), verbs=('Estes são os verbos de hoje!', '¡Estos son los verbos de hoy!'),
    vmission=('Missão dos verbos! Eu ajudo você.', '¡Misión de verbos! Yo te ayudo.'), exps=('É assim que as pessoas falam de verdade!', '¡Así habla la gente de verdad!'),
    complete=('Complete as frases!', '¡Completa las frases!'), careful=('Cuidado! Só uma está certa.', '¡Cuidado! Solo una es correcta.'),
    lab=('Vamos treinar o ouvido!', '¡Vamos a entrenar el oído!'), hunt=('Ouça e cace o som certo!', '¡Escucha y caza el sonido!'),
    pick=('Escolha uma missão! Qual você quer?', '¡Elige una misión! ¿Cuál quieres?'), wrong=wrong, vq='Verbo **%s** (%s) con él/ella.')


def load_eps():
    eps = []
    for f in sorted(glob.glob(os.path.join(HERE, 'pt', 'ep_*.py'))):
        m = importlib.import_module('pt.' + os.path.basename(f)[:-3])
        eps += m.EPS
    return eps


def main(only=None):
    chunks, where = {}, {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'pt-a1_*.json'))):
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
        for fr in e['fr']:
            if fr['k'] == 'pgmission':
                for mm in fr['missions']:
                    mm['data']['ph'] = E['more']['missions'][0]['data']['ph'] if False else mm['data'].get('ph')
                    if mm['data'].get('ph') == 'Escreva a sua resposta aqui…':
                        mm['data']['ph'] = UI['Escreva a sua resposta aqui…']
        chunks[f][i] = e
        done += 1
    for f, d in chunks.items():
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
    print('episódios montados:', done)


if __name__ == '__main__':
    main({int(x) for x in sys.argv[1:]} or None)
