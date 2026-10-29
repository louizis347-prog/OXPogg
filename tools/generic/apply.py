#!/usr/bin/env python3
"""Aplica lotes de tools/generic/out/<lote>.json nos dados: troca a obra do episódio (mantendo a aula), atualiza descrição/ponte,
grava as fichas em tools/ficha/work/en-<nivel>_gen_<lote>.json e sincroniza o plano. Uso: python3 tools/generic/apply.py <lote> [...]"""
import glob, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# só troca textos-modelo da ponte (nunca o texto da aula): a string inteira é o título, ou contém marcas de frase-modelo
MARK = re.compile(r"referência|reference|cultural|\bobra\b|program notes|lens|lente|contexto|context|inspirada|scene names|carries an idea|cena da|retome|noticed|gives us|opens the mission|abre a missão|oferece um ponto", re.I)

def swap(v, old, new, hits):
    if isinstance(v, dict): return {k: swap(x, old, new, hits) for k, x in v.items()}
    if isinstance(v, list): return [swap(x, old, new, hits) for x in v]
    if not isinstance(v, str) or old not in v: return v
    if v == old or v.startswith(old + ' (') or v.startswith(old + ' ·') or MARK.search(v):
        hits[0] += 1; return v.replace(old, new)
    hits[1] += 1; return v   # ocorrência no texto da aula: não mexe (fica para revisão)

def main(lotes):
    by_course = {}
    for l in lotes:
        out = json.load(open(os.path.join(ROOT, 'tools/generic/out', l + '.json'), encoding='utf-8'))
        lv = l.split('_')[0]
        fich = {}
        for n, x in out.items(): by_course.setdefault('en-' + lv, {})[int(n)] = x; fich[n] = x['ficha']
        json.dump(fich, open(os.path.join(ROOT, 'tools/ficha/work/en-%s_gen_%s.json' % (lv, l.split('_')[1])), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    stale = []
    for course, M in by_course.items():
        for f in sorted(glob.glob(os.path.join(ROOT, 'data', course + '_*.json'))):
            d = json.load(open(f, encoding='utf-8')); dirty = False
            for i, e in enumerate(d):
                if e['n'] not in M: continue
                x = M[e['n']]; ob = x['obra']; old = e['a']['w']; oy = e['a'].get('y', '')
                hits = [0, 0]
                new = swap(e, f"{old} ({oy})", f"{ob['nome']} ({ob['ano']})", hits)
                new = swap(new, old, ob['nome'], hits)
                new['a'].update({'w': ob['nome'], 'y': str(ob['ano']), 'k': ob['tipo'], 'd': x['desc']}); new['h']['src'] = ob['nome']
                d[i] = new; dirty = True
                if hits[1]: stale.append((e['n'], old, hits[1]))
            if dirty: open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
    cur = {}
    for f in glob.glob(os.path.join(ROOT, 'data', 'en-*_*.json')):
        for e in json.load(open(f, encoding='utf-8')): cur[e['n']] = e
    for f in glob.glob(os.path.join(ROOT, 'tools/plan/map/en-*.json')):
        d = json.load(open(f, encoding='utf-8')); dirty = False
        for m in d:
            e = cur.get(m['n'])
            if e and m['obra']['nome'] != e['a']['w']: m['obra'].update({'nome': e['a']['w'], 'ano': e['a'].get('y', ''), 'tipo': e['a']['k']}); dirty = True
        if dirty: open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
    print('aplicado:', {c: len(m) for c, m in by_course.items()}, '| episódios com o título antigo ainda no texto da aula:', len(stale))
    for s in stale[:15]: print('  revisar', s)
if __name__ == '__main__': main(sys.argv[1:])
