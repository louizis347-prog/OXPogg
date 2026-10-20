# -*- coding: utf-8 -*-
"""Monta um arco do Neighbors a partir de um arquivo de especificação e grava nos blocos data/<cid>_NN.json.
uso: python3 tools/nb/run_arc.py SPEC.py LANG CID ARCO BASE REVBASE [--dry]
SPEC.py define EPS = [dict(...)] (9 episódios). Substitui os esqueletos (mesmo n) ou acrescenta ao fim do curso."""
import sys, os, json, glob, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import buildnb as B
DATA = os.path.join(HERE, '..', '..', 'data')

def main():
    spec, lang, cid, arc, base, revbase = sys.argv[1:7]
    arc, base, revbase = int(arc), int(base), int(revbase)
    dry = '--dry' in sys.argv
    sp = importlib.util.spec_from_file_location('spec', spec)
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    eps = m.EPS
    errs = []
    for e in eps:
        errs += B.check_spec(e)
    if errs:
        for x in errs: print('ERRO', x)
        sys.exit(1)
    lv = cid.split('-')[1].upper() if cid.split('-')[1] != 'kana' else 'A1'
    lv = getattr(m, 'LV', lv)
    prefix = cid.split('-')[0]
    out = B.build_arc(lang, arc, eps, lv, base, revbase, lambda built: built[-1]['o'] + .5, prefix)
    if dry:
        print('ok', [e['n'] for e in out]); return
    files = sorted(glob.glob(os.path.join(DATA, cid + '_*.json')))
    blocks = {f: json.load(open(f, encoding='utf-8')) for f in files}
    if not files:
        files = [os.path.join(DATA, cid + '_01.json')]; blocks[files[0]] = []
    where = {e['n']: f for f, b in blocks.items() for e in b}
    for e in out:
        f = where.get(e['n'])
        if f:
            b = blocks[f]
            b[[x['n'] for x in b].index(e['n'])] = e
        else:
            f = files[-1]
            if len(blocks[f]) >= 25:
                f = os.path.join(DATA, '%s_%02d.json' % (cid, len(files) + 1)); files.append(f); blocks[f] = []
            blocks[f].append(e)
    for f, b in blocks.items():
        json.dump(b, open(f, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    for fn, v in (('manifest.json', [os.path.basename(f) for f in files]), ('counts.json', sum(len(b) for b in blocks.values()))):
        pth = os.path.join(DATA, fn); d = json.load(open(pth, encoding='utf-8')); d[cid] = v
        json.dump(d, open(pth, 'w', encoding='utf-8'), ensure_ascii=False, separators=(', ', ': '))
    print('gravado', [e['n'] for e in out])

main()
