#!/usr/bin/env python3
"""Aplica lotes de tools/generic/out/<lote>.json nos dados: troca a obra do episódio (mantendo a aula), atualiza descrição/ponte,
grava as fichas em tools/ficha/work/en-<nivel>_gen_<lote>.json e sincroniza o plano. Uso: python3 tools/generic/apply.py <lote> [...]"""
import glob, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# só troca textos-modelo da ponte (nunca o texto da aula): a string inteira é o título, ou contém marcas de frase-modelo
MARK = re.compile(r"referência|reference|cultural|\bobra\b|program notes|lens|lente|contexto|context|inspirada|scene names|carries an idea|cena da|retome|noticed|gives us|opens the mission|abre a missão|oferece um ponto", re.I)

def swap_all(v, rx, new, skip=()):
    """troca o título antigo (palavra inteira) em TODOS os textos; as chaves em `skip` são sobrescritas depois"""
    if isinstance(v, dict): return {k: (x if k in skip else swap_all(x, rx, new, skip)) for k, x in v.items()}
    if isinstance(v, list): return [swap_all(x, rx, new, skip) for x in v]
    return rx.sub(lambda m: new, v) if isinstance(v, str) else v

def course_of(n):
    for f in glob.glob(os.path.join(ROOT, 'data', 'en-*_*.json')):
        if any(e['n'] == n for e in json.load(open(f, encoding='utf-8'))): return os.path.basename(f).rsplit('_', 1)[0]
    raise KeyError(n)

def main(lotes):
    EXC = set()
    by_course = {}
    for l in lotes:
        out = json.load(open(os.path.join(ROOT, 'tools/generic/out', l + '.json'), encoding='utf-8'))
        fich = {}
        for n, x in out.items():
            if int(n) in EXC: continue
            by_course.setdefault(course_of(int(n)), {})[int(n)] = x
            if x.get('ficha'): fich.setdefault(course_of(int(n)), {})[n] = x['ficha']
        for c, F in fich.items():
            json.dump(F, open(os.path.join(ROOT, 'tools/ficha/work/%s_gen_%s.json' % (c, l)), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    stale = []
    for course, M in by_course.items():
        for f in sorted(glob.glob(os.path.join(ROOT, 'data', course + '_*.json'))):
            d = json.load(open(f, encoding='utf-8')); dirty = False
            for i, e in enumerate(d):
                if e['n'] not in M: continue
                x = M[e['n']]; ob = x['obra']; old = e['a']['w']; oy = e['a'].get('y', '')
                rx = re.compile(r'(?<![\w])' + re.escape(old) + r'(?![\w])')
                new = swap_all(e, rx, ob['nome'], skip=('d', 'text'))
                a = new['a']; a.update({'w': ob['nome'], 'y': str(ob['ano']), 'k': ob['tipo'], 'd': x['desc']}); new['h']['src'] = ob['nome']
                for fr in new['fr']:
                    if isinstance(fr.get('obra'), str): fr['obra'] = f"{ob['nome']} · {ob['ano']}"
                    elif isinstance(fr.get('obra'), dict):
                        fr['obra']['name'] = ob['nome']; fr['obra']['text'] = x['desc']
                        fr['obra']['line'] = [f"This lesson uses {ob['nome']} as a cultural lens.", f"Esta aula usa {ob['nome']} como lente cultural."]
                    if isinstance(fr.get('sticker'), dict): fr['sticker']['title'] = ob['nome']; fr['sticker']['sub'] = f"{ob['nome']} · {ob['ano']}"
                    for h in fr.get('hot', []) if fr['k'] == 'hotscene' else []:
                        if h.get('pt') == 'obra em foco': h['en'] = ob['nome']
                rest = []; walk = lambda v: rest.extend([1] for _ in [0] if isinstance(v, str) and rx.search(v)) if isinstance(v, str) else ([walk(y) for y in v.values()] if isinstance(v, dict) else [walk(y) for y in v] if isinstance(v, list) else None)
                walk(new)
                d[i] = new; dirty = True
                if rest: stale.append((e['n'], old, len(rest)))
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
