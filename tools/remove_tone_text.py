#!/usr/bin/env python3
"""Remove dos cursos regulares os textos de "tom e registro" (instruções de escolher tom/registro e de refazer a
resposta em duas versões): cauda fixa do quadro de produção, itens de checklist de intenção/registro, trecho do
diálogo guiado e as frases dos textos de apoio (coach). Reexecutável."""
import json, os, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
TAIL = re.compile(r'\s*Explique a intenção, escolha o registro adequado.*?antes de escolher a versão final\.', re.S)
INTENT = re.compile(r'\s*y explica tu intención en español')
TDLG = re.compile(r'\s*(Em seguida, justifique a escolha|Luego, justifica la elección|Depois, justifique a escolha).*$', re.S)
COACH1 = re.compile(r'(Transfira a habilidade .*?): tente uma versão natural e outra mais cuidadosa\.')
COACH2 = re.compile(r'(Use este repertório em .*?); confira pronúncia, intenção e registro\.')
SAY = re.compile(r'\s*(e|y)\s+(reformule a fala em outro registro|reformula la frase en otro registro|reformula la frase en otro registro)\.?')
DROP_CHECK = {'Intenção clara', 'Intención clara', 'Klare Absicht', 'Clear intent', 'Une intention claire',
              'Intenzione chiara', 'Registro adecuado', 'Un registre cohérent', 'Resposta adequada à situação'}


def clean(x):
    ch = 0
    k = x.get('k')
    if k == 'produce':
        p = x.get('prompt')
        if isinstance(p, str):
            n = INTENT.sub('', TAIL.sub('', p))
            if n != p:
                x['prompt'] = n.strip(); ch += 1
        c = x.get('check')
        if isinstance(c, list):
            keep = [i for i in c if i not in DROP_CHECK]
            if keep and len(keep) != len(c):
                x['check'] = keep; ch += 1
    if k == 'tdlg' and isinstance(x.get('intro'), str):
        n = TDLG.sub('', x['intro'])
        if n != x['intro']:
            x['intro'] = n.strip(); ch += 1
    sy = x.get('say')
    if isinstance(sy, str) and 'registro' in sy:
        n = SAY.sub('.', sy)
        n = n.replace('..', '.')
        if n != sy:
            x['say'] = n; ch += 1
    c = x.get('coach')
    if isinstance(c, str):
        n = COACH2.sub(r'\1; confira a pronúncia.', COACH1.sub(r'\1.', c))
        if n != c:
            x['coach'] = n; ch += 1
    return ch


def main():
    m = json.load(open(os.path.join(ROOT, 'manifest.json'), encoding='utf-8'))
    tot = files = 0
    for course in sorted(m):
        if course.startswith('nb'):
            continue
        for b in m[course]:
            p = os.path.join(ROOT, b)
            d = json.load(open(p, encoding='utf-8'))
            ch = 0
            for e in d:
                for x in e.get('fr', []):
                    ch += clean(x)
            if ch:
                open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
                tot += ch; files += 1
        print(course, flush=True)
    print('textos ajustados:', tot, 'em', files, 'blocos')


if __name__ == '__main__':
    main()
