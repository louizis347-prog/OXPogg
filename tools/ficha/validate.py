#!/usr/bin/env python3
"""Valida fichas de capa (tools/ficha/work/*.json ou js/fichas-*.js já gerado) contra o vocabulário da biblioteca e a regra de unicidade.
Uso: python3 tools/ficha/validate.py [arquivos .json ...] [--curso en-a1] [--todos]   (sem arquivos: valida tools/ficha/work/<curso>_*.json)
Regras: vocabulário válido; 1–4 personagens; pessoa/bicho; prop válido; cena e hora válidas; sem combinação repetida
(personagens + prop + cena), nem mesma cena+prop, nem mesmo elenco de bichos/roupas; toda obra do curso (sem arte à mão) tem ficha."""
import glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
V = json.load(open(os.path.join(HERE, 'vocab.json')))
HAND = {9801, 82019, 70001, 7070001, 30001, 7030001, 9802, 7009802, 30002, 7030002}
HEX = re.compile(r'^#[0-9a-fA-F]{6}$|^#[0-9a-fA-F]{3}$')
PERSON_KEYS = {'hs', 'hair', 'skin', 'outfit', 'top', 'bot', 'shirt', 'shoe', 'hat', 'hatColor', 'beard', 'stache', 'glasses', 'freckles', 'arms', 'holds',
               'holdColor', 'holdS', 'holdDx', 'holdDy', 'cape', 'wings', 'scarf', 'trim', 'tie', 'belt', 'band', 'ribbon', 'apron', 'skirt', 'emblem', 'stripe', 'num',
               'ears', 'sleeve', 'legs', 'wide'}
ANIMAL_KEYS = {'a', 'c', 'c2', 's', 'x', 'y', 'flip', 'back'}
FICHA_KEYS = {'t', 'scene', 'tod', 'cast', 'prop', 'decor', 'accent', 'sunx', 'propOver', 'falta'}


def color_ok(v):
    return isinstance(v, str) and (HEX.match(v) is not None)


def check(n, f):
    er = []
    for k in f:
        if k not in FICHA_KEYS:
            er.append('campo desconhecido %r' % k)
    if f.get('scene') not in V['scene']: er.append('cena inválida %r' % f.get('scene'))
    if f.get('tod') not in V['tod']: er.append('hora inválida %r' % f.get('tod'))
    cast = f.get('cast')
    if not isinstance(cast, list) or not 1 <= len(cast) <= 4: er.append('elenco precisa ter 1 a 4 personagens')
    for i, m in enumerate(cast or []):
        if not isinstance(m, dict): er.append('personagem %d inválido' % i); continue
        if ('p' in m) == ('a' in m): er.append('personagem %d: use "p" (pessoa) OU "a" (bicho)' % i); continue
        if 'p' in m:
            p = m['p']
            for k, v in p.items():
                if k not in PERSON_KEYS: er.append('personagem %d: campo de pessoa desconhecido %r' % (i, k))
            if p.get('hs') not in V['hs']: er.append('personagem %d: hs inválido %r' % (i, p.get('hs')))
            if p.get('outfit') not in V['outfit']: er.append('personagem %d: outfit inválido %r' % (i, p.get('outfit')))
            if 'hat' in p and p['hat'] not in V['hat']: er.append('personagem %d: chapéu inválido %r' % (i, p['hat']))
            if 'skin' in p and p['skin'] not in V['skin'] and not color_ok(p['skin']): er.append('personagem %d: pele inválida' % i)
            if 'hair' in p and p['hair'] not in V['hair'] and not color_ok(p['hair']): er.append('personagem %d: cabelo inválido %r' % (i, p['hair']))
            if 'arms' in p and p['arms'] not in V['arms']: er.append('personagem %d: arms inválido' % i)
            if 'holds' in p and p['holds'] not in V['prop']: er.append('personagem %d: holds inválido %r' % (i, p['holds']))
            for k in ('top', 'bot', 'shirt', 'shoe', 'hatColor', 'cape', 'wings', 'scarf', 'trim', 'tie', 'belt', 'band', 'ribbon', 'holdColor', 'emblem', 'stripe', 'sleeve', 'legs'):
                if k in p and not color_ok(p[k]): er.append('personagem %d: %s precisa ser cor #rrggbb' % (i, k))
        else:
            for k in m:
                if k not in ANIMAL_KEYS: er.append('personagem %d: campo de bicho desconhecido %r' % (i, k))
            if m['a'] not in V['animal']: er.append('personagem %d: bicho inválido %r' % (i, m['a']))
            for k in ('c', 'c2'):
                if k in m and not color_ok(m[k]): er.append('personagem %d: %s precisa ser cor #rrggbb' % (i, k))
    pr = f.get('prop')
    if pr is not None:
        if not isinstance(pr, dict) or pr.get('id') not in V['prop']: er.append('prop inválido %r' % (pr.get('id') if isinstance(pr, dict) else pr))
        elif pr.get('at', 'front') not in V['propAt']: er.append('prop.at inválido %r' % pr.get('at'))
        elif 'c' in pr and not color_ok(pr['c']): er.append('prop.c precisa ser cor #rrggbb')
        if pr and pr.get('at') == 'held':
            if not any(isinstance(m, dict) and m.get('p', {}).get('holds') == pr.get('id') for m in cast or []): er.append('prop held sem personagem que segure (holds)')
    if not pr and not any(isinstance(m, dict) and m.get('p', {}).get('holds') for m in cast or []): er.append('falta o objeto-símbolo da obra (prop ou holds)')
    for d in f.get('decor', []):
        if d not in V['decor']: er.append('decor inválido %r' % d)
    return er


def signature(f):
    def who(m):
        if 'a' in m: return 'a:%s:%s' % (m['a'], m.get('c', ''))
        p = m['p']; return 'p:%s:%s:%s:%s:%s' % (p.get('hs'), p.get('outfit'), p.get('hat', ''), p.get('top', ''), p.get('hair', ''))
    cast = '+'.join(sorted(who(m) for m in f['cast']))
    pr = (f.get('prop') or {}).get('id', '') or ','.join(sorted({m['p']['holds'] for m in f['cast'] if 'p' in m and m['p'].get('holds')}))
    return cast, pr, f['scene']


def main():
    a = sys.argv[1:]
    curso = 'en-a1'
    if '--curso' in a: i = a.index('--curso'); curso = a[i + 1]; del a[i:i + 2]
    todos = '--todos' in a; a = [x for x in a if x != '--todos']
    meu = None
    if '--meu' in a: i = a.index('--meu'); meu = a[i + 1]; del a[i:i + 2]
    files = a or sorted(glob.glob(os.path.join(HERE, 'work', curso + '_*.json')))
    F = {}
    for fn in files:
        for n, f in json.load(open(fn, encoding='utf-8')).items(): F[int(n)] = f
    mine = {int(k) for k in json.load(open(meu, encoding='utf-8'))} if meu else None
    bad = 0
    for n, f in sorted(F.items()):
        if mine is not None and n not in mine: continue
        for e in check(n, f): print('ERRO %s: %s' % (n, e)); bad += 1
    seen, seen2, seen3 = {}, {}, {}
    for n, f in sorted(F.items()):
        try: c, p, s = signature(f)
        except Exception: continue
        for tab, key, msg in ((seen, (c, p, s), 'mesma combinação personagem+objeto+cena'), (seen2, (p, s), 'mesmo objeto e mesma cena'), (seen3, (c, s), 'mesmo elenco e mesma cena')):
            if key in tab:
                if mine is None or n in mine or tab[key] in mine: print('ERRO %s: %s que o episódio %s' % (n, msg, tab[key])); bad += 1
            else: tab[key] = n
    if todos:
        man = json.load(open(os.path.join(ROOT, 'data', 'manifest.json')))
        miss = []
        for fn in man[curso]:
            for e in json.load(open(os.path.join(ROOT, 'data', fn), encoding='utf-8')):
                if e['n'] not in F and e['n'] not in HAND: miss.append(e['n'])
        if miss: print('ERRO: %d obras sem ficha (ex.: %s)' % (len(miss), miss[:8])); bad += len(miss)
    print('fichas: %d | erros: %d' % (len(F), bad))
    return 1 if bad else 0


sys.exit(main())
