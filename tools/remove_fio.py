#!/usr/bin/env python3
"""Remove o quadro `fio` ("The story thread" / "Escolha o tom") de todos os episódios dos cursos regulares."""
import json, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')


def main():
    m = json.load(open(os.path.join(ROOT, 'manifest.json'), encoding='utf-8'))
    n = files = 0
    for course in sorted(m):
        for b in m[course]:
            p = os.path.join(ROOT, b)
            d = json.load(open(p, encoding='utf-8'))
            ch = False
            for e in d:
                fr = e.get('fr')
                if fr and any(x.get('k') == 'fio' for x in fr):
                    e['fr'] = [x for x in fr if x.get('k') != 'fio']
                    n += 1
                    ch = True
            if ch:
                open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
                files += 1
        print(course, flush=True)
    print('quadros fio removidos:', n, 'em', files, 'blocos')


if __name__ == '__main__':
    main()
