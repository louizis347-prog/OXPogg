#!/usr/bin/env python3
"""Valida módulos de reescrita do A2 (tools/v3/a2_fix_*.py) SEM gravar em data/: monta em memória e roda o contrato.
  python3 tools/a2fix/try.py a2_fix_NN [outro ...]   (obra única em todo o inglês regular, expressão única no A2, contrato regular-pilot-v1)"""
import glob, importlib, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools')); sys.path.insert(0, os.path.join(ROOT, 'tools', 'audit'))
os.environ['COURSE'] = 'en-a2'
import model_v2 as M, model_v3 as V
from v3 import lib
import regular_pilot_contract as C

import unicodedata
_STOP = {'the', 'a', 'an', 'of', 'o', 'a', 'os', 'as', 'de', 'do', 'da', 'dos', 'das', 'e', 'and', 'la', 'le', 'el', 'torre', 'tower', 'museum', 'museu', 'filme', 'film'}


def _toks(n):
    n = unicodedata.normalize('NFKD', n.casefold()).encode('ascii', 'ignore').decode()
    return {t for t in re.findall(r'[a-z0-9]+', n) if t not in _STOP}


def similar(a, b):
    """Mesma obra com grafia diferente (ex.: Torre Eiffel × Eiffel Tower): um nome contém o outro ou os termos coincidem."""
    ta, tb = _toks(a), _toks(b)
    if not ta or not tb:
        return a.casefold() == b.casefold()
    if min(len(ta), len(tb)) < 2:  # um só termo (ex.: “room”) contido em outro título não é a mesma obra
        return ta == tb
    return ta <= tb or tb <= ta


RS = set('cafe living market airport lobby station subway park pier lake nyc flags cafe2 airport2 lobby1 lobby2 sub2 tick cafe3 diner home1 yard park2 school shop office clinic kitchen bedroom bath counter gym hall street beach zoo farm playground busstop bakery supermarket bookshop postoffice bank pharmacy restaurant hotelroom mountain forest snow stage library museum castlehall garden fair pool stadium harbor chefkitchen musicroom traincar soccerfield fishing artroom nightcity meetingroom christmas pilotlibrary pilotelevator pilotsearch pilotstorm pilotmorning pilotautumn'.split())
NAMED = set(re.findall(r"^\s*([A-Za-z0-9_]+):\s*\(\)\s*=>", ''.join(open(os.path.join(ROOT, 'js', f), encoding='utf-8').read() for f in ('chars.js', 'chars2.js', 'chars3.js', 'chars5.js')), re.M))
NAMED |= set('bear mrs alice rabbit cat dorothy scarecrow lion wendy peter tinker hook cowboy ranger'.split())
PARAM = re.compile(r'p:(short|long|bun|curly|bald|cap):[0-9a-fA-F]{6}:[0-9a-fA-F]{6}:[0-9a-fA-F]{6}:(none|glasses|hat|crown|scarf|beard|bow):(shirt|dress|suit)')


def mods_works(skip):
    w = {}
    fixed = set()  # episódios substituídos por módulos a2_fix_*: a versão antiga não conta
    for f in glob.glob(os.path.join(ROOT, 'tools', 'v3', 'a2_fix_*.py')):
        try:
            fixed |= {e['n'] for e in importlib.import_module('v3.' + os.path.basename(f)[:-3]).EPS}
        except Exception:
            pass
    for f in glob.glob(os.path.join(ROOT, 'tools', 'v3', 'a2_*.py')):
        name = os.path.basename(f)[:-3]
        if name in skip or name == 'b2lib':
            continue
        try:
            m = importlib.import_module('v3.' + name)
        except Exception:
            continue
        for e in getattr(m, 'EPS', []):
            if e['n'] in fixed and not name.startswith('a2_fix_'):
                continue
            w.setdefault(e['v2']['obra']['name'].casefold(), []).append(e['n'])
    return w


def main(names):
    data, where = {}, {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'en-a2_*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        for i, e in enumerate(d):
            where[e['n']] = (f, e)
    order = sorted(where, key=lambda n: where[n][1]['o'])
    mine = []
    for nm in names:
        m = importlib.import_module('v3.' + nm)
        mine += [(nm, e) for e in m.EPS]
    mine.sort(key=lambda t: order.index(t[1]['n']))
    ns = {e['n'] for _, e in mine}
    problems = []
    other = mods_works(set(names))
    datawork = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'en-*_*.json'))):  # obra única em TODO o inglês regular (A1–C2)
        for e in json.load(open(f, encoding='utf-8')):
            if e['n'] not in ns:
                datawork.setdefault(((e.get('a') or {}).get('w', '')).split(':')[0].strip().casefold(), []).append(e['n'])
    seen = {}
    seen_names = set()
    built = []
    for k, (nm, E) in enumerate(mine):
        n = E['n']
        if n not in where:
            problems.append('%s: n=%s não existe no A2' % (nm, n)); continue
        f, old = where[n]
        idx = order.index(n)
        P = mine[k - 1][1] if k else None
        if P and order.index(P['n']) == idx - 1:
            prev = (P['v2'], P['extra'], P['verbs'])
        elif idx == 0:
            prev = None
        else:
            pit = where[order[idx - 1]][1]
            prev = V.prev_from_pilot(pit) if any(x['k'] == 'pgrule' for x in pit['fr']) else V.prev_from_old(pit)
        M.HOTPT.update(lib.SAYPT)
        b = M.build(old, E['v2'], E['extra'], E['verbs'], prev, E['more'])
        b['presentation'] = 'regular-pilot-v1'
        built.append((nm, n, b))
        w = E['v2']['obra']['name'].split(':')[0].strip().casefold()
        if w in datawork:
            problems.append('%s ep%s: obra “%s” já é usada no inglês regular (episódios %s) — escolha outra' % (nm, n, E['v2']['obra']['name'], datawork[w][:4]))
        if w in other:
            problems.append('%s ep%s: obra “%s” já usada em outro módulo (%s)' % (nm, n, E['v2']['obra']['name'], other[w]))
        for ow in list(datawork) + list(other):
            if ow != w and similar(w, ow):
                problems.append('%s ep%s: obra “%s” parece a mesma de “%s” (outro episódio) — escolha outra' % (nm, n, E['v2']['obra']['name'], ow))
                break
        for ow in list(seen_names):
            if ow != w and similar(w, ow):
                problems.append('%s ep%s: obra “%s” parece repetida no mesmo módulo (“%s”)' % (nm, n, E['v2']['obra']['name'], ow))
        seen_names.add(w)
        if w in seen:
            problems.append('%s ep%s: obra “%s” repetida no mesmo módulo (ep%s)' % (nm, n, E['v2']['obra']['name'], seen[w]))
        seen[w] = n
        # cenários e personagens
        for fr in b['fr']:
            rs = fr.get('rs')
            if rs and rs not in RS:
                problems.append('ep%s: cenário inexistente %r no quadro %s' % (n, rs, fr['k']))
            for ch in (fr.get('chars') or []) + ((fr.get('stage') or {}).get('chars') or []):
                if ch[0] not in NAMED and not PARAM.fullmatch(ch[0]) and not ch[0].startswith('e:'):
                    problems.append('ep%s: personagem inexistente %r' % (n, ch[0]))
        for ch in E['v2']['speakers'].values():
            if ch not in NAMED and not PARAM.fullmatch(ch) and not ch.startswith('e:'):
                problems.append('ep%s: personagem (speakers) inexistente %r' % (n, ch))
        # respostas e opções
        for fr in b['fr']:
            for it in (fr.get('items') or []):
                if isinstance(it, dict) and 'opts' in it and 'a' in it:
                    o = it['opts']
                    if not (0 <= it['a'] < len(o)):
                        problems.append('ep%s %s: resposta fora das opções' % (n, fr['k']))
                    if len({json.dumps(x, ensure_ascii=False) for x in o}) != len(o):
                        problems.append('ep%s %s: opções repetidas %s' % (n, fr['k'], o))
        for fr in b['fr']:
            if fr['k'] == 'pgmission':
                for ms in fr['missions']:
                    d = ms['data']
                    for r in d['kw']:
                        if not re.search(r, d['model'], re.I):
                            problems.append('ep%s missão %s: o modelo não casa com %s' % (n, ms['name'], r))
    # expressões únicas no B2: nenhuma expressão de um episódio pode aparecer em outro episódio já pronto
    usedx = {}
    for n2, (f2, e2) in where.items():
        if n2 in ns or e2.get('presentation') != 'regular-pilot-v1':
            continue
        for fr2 in e2['fr']:
            if fr2['k'] == 'pgexp':
                for x in fr2['items']:
                    usedx.setdefault(x['en'].casefold().strip(), n2)
    mine_x = {}
    for nm, n, b in built:
        for fr2 in b['fr']:
            if fr2['k'] == 'pgexp':
                for x in fr2['items']:
                    k2 = x['en'].casefold().strip()
                    if k2 in usedx:  # no A2 a expressão é única contra TODOS os outros episódios (antes e depois)
                        problemas_x = '%s ep%s: expressão “%s” já é ensinada no episódio %s — troque por outra' % (nm, n, x['en'], usedx[k2])
                        problems.append(problemas_x)
                    elif k2 in mine_x and mine_x[k2] != n:
                        problems.append('%s ep%s: expressão “%s” repetida no episódio %s do módulo — troque' % (nm, n, x['en'], mine_x[k2]))
                    mine_x.setdefault(k2, n)
    for nm, n, b in built:
        for p in C.audit('en-a2', [(nm, b)]):
            if 'obra repetida' in p:
                continue
            problems.append(p.replace('en-a2 1 ', ''))
    print('episódios montados:', len(built), '| problemas:', len(problems))
    for p in problems:
        print(' -', p)
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
