#!/usr/bin/env python3
"""Gera data/manifest.json e data/counts.json a partir dos blocos que existem em data/.

Fonte da verdade = os arquivos data/<curso>_NN.json. Nunca edite o manifesto nem os
contadores à mão: apagar ou criar um bloco e rodar este script basta.
  python3 tools/build_data_index.py          # regrava os dois arquivos
  python3 tools/build_data_index.py --check  # só confere (sai com 1 se estiverem fora de sincronia)
"""
import json, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
BLOCK = re.compile(r'^([a-z]+(?:-[a-z0-9]+)?)_(\d+)\.json$')


def build():
    blocks = {}
    for f in sorted(os.listdir(ROOT)):
        m = BLOCK.match(f)
        if m:
            blocks.setdefault(m.group(1), []).append(f)
    manifest, counts = {}, {}
    for course in sorted(blocks):
        manifest[course] = blocks[course]
        n = 0
        for f in blocks[course]:
            with open(os.path.join(ROOT, f), encoding='utf-8') as fh:
                n += len(json.load(fh))
        counts[course] = n
    return manifest, counts


def dump(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(',', ':')) + '\n'


def main():
    manifest, counts = build()
    out = {'manifest.json': dump(manifest), 'counts.json': dump(counts)}
    stale = []
    for name, text in out.items():
        path = os.path.join(ROOT, name)
        cur = open(path, encoding='utf-8').read() if os.path.exists(path) else ''
        if cur != text:
            stale.append(name)
            if '--check' not in sys.argv:
                open(path, 'w', encoding='utf-8').write(text)
    if stale:
        print(('FORA DE SINCRONIA: ' if '--check' in sys.argv else 'Atualizado: ') + ', '.join(stale))
        sys.exit(1 if '--check' in sys.argv else 0)
    print('manifest.json e counts.json em sincronia (%d cursos, %d episódios)' % (len(counts), sum(counts.values())))


if __name__ == '__main__':
    main()
