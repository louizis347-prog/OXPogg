#!/usr/bin/env python3
"""Alinha a obra mostrada nos quadros culturais dos episódios 70/79 do inglês à obra do gancho (`h.src`).

Em ~740 episódios o gancho da lição cita uma obra (ex.: Friends) mas cultob/cultx/cultcena mostravam outra.
Para cada um, procura outro episódio do mesmo nível já consistente com essa obra (doador), reaproveita só o
texto neutro dela (sem as frases amarradas à lição do doador) e mantém os textos de ligação do próprio
episódio. Reexecutável: episódios já consistentes não mudam.
"""
import copy, json, os, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
LV = ['a1', 'a2', 'b1', 'b2', 'c1', 'c2']
BOUND = re.compile(r'(Essa ideia|Aqui a obra|A lição|os tópicos|Na aula de hoje|Na lição|combina com|serve de ponto|serve para|ajuda a observar|expressões como|frases como|conversa diretamente)', re.I)
isgen = lambda e: str(e['n']).startswith(('70', '79'))


def F(e):
    fr = {}
    for x in e['fr']:
        fr.setdefault(x['k'], x)
    return fr


def consistent(e):
    f, X = F(e), e['h']['src']
    return f['cultcena']['work'] == X and f['cultob']['work'] == X and f['cultx']['work'] == X


def lesson_tokens(e):
    t = set()
    for s in [e.get('s') or '', (e.get('g') or {}).get('t', '') if isinstance(e.get('g'), dict) else '',
              (e.get('h') or {}).get('l', '')]:
        t |= {w.lower() for w in re.findall(r'[\w’\']{5,}', s)}
    for x in e['fr']:
        if x['k'] == 'words':
            for it in x.get('items', []):
                t |= {w.lower() for w in re.findall(r'[\w’\']{5,}', it[0])}
    return t


def neutral(d):
    """texto sobre a obra sem as frases amarradas à lição do doador"""
    f = F(d)
    toks = lesson_tokens(d)
    cands = []
    if f['cultob'].get('panels'):
        cands.append(f['cultob']['panels'][0])
    cx = f['cultx'].get('tiles') or []
    if cx:
        cands.append(cx[0].get('t', ''))
    cands.append(f['cultcena'].get('ctx', ''))
    cw = f['cover'].get('cw') or {}
    if isinstance(cw.get('fact'), list) and len(cw['fact']) > 2:
        cands.append(cw['fact'][2])
    best = ''
    for c in cands:
        if isinstance(c, list):
            c = ' '.join(str(z) for z in c)
        sents = re.split(r'(?<=[.!?])\s+', c or '')
        keep = [s for s in sents if s and not BOUND.search(s) and not any(t in s.lower() for t in toks)]
        txt = ' '.join(keep).strip()
        if len(txt) > len(best):
            best = txt
    return best


def run():
    m = json.load(open(os.path.join(ROOT, 'manifest.json'), encoding='utf-8'))
    changed = skipped = 0
    for lv in LV:
        blocks = [(os.path.join(ROOT, b), json.load(open(os.path.join(ROOT, b), encoding='utf-8'))) for b in m['en-' + lv]]
        eps = [e for _, d in blocks for e in d]
        donors = {}
        for e in eps:
            if consistent(e):
                prev = donors.get(e['h']['src'])
                if prev is None or (isgen(e) and not isgen(prev)):   # prefere doador da própria série 70/79 (texto neutro)
                    donors[e['h']['src']] = e
        for e in eps:
            if not isgen(e) or consistent(e):
                continue
            X = e['h']['src']
            d = donors.get(X)
            if not d:
                skipped += 1
                continue
            txt = neutral(d)
            if len(txt) < 40:
                skipped += 1
                continue
            f, fd = F(e), F(d)
            old = {f['cultob']['work'], f['cultcena']['work']}
            kind = (fd['cultob'].get('kind') or '')
            ob = f['cultob']
            link = ob['panels'][1:] if ob.get('panels') else []
            ob.update(work=X, chips=copy.deepcopy(fd['cultob'].get('chips')), kind=kind,
                      facts=copy.deepcopy(fd['cultob'].get('facts')), panels=[txt] + link)
            cx = f['cultx']
            cx['work'] = X
            cx['tag'] = fd['cultx'].get('tag')
            if cx.get('tiles'):
                cx['tiles'][0]['t'] = txt
            cc = f['cultcena']
            cc['work'] = X
            cc['tag'] = fd['cultcena'].get('tag')
            cc['ctx'] = txt
            if cc.get('leitura'):
                cc['leitura'] = [txt] + cc['leitura'][1:]
            for w in f['culttl'].get('works', []):
                if w.get('t') == 'main work':
                    w.update(n=X, k=fd['cultob'].get('kind') or w.get('k'), d=txt)
                    if fd['culttl'].get('works'):
                        w['y'] = fd['culttl']['works'][0].get('y', w.get('y'))
            f['bridge']['work'] = X
            if fd['bridge'].get('kind'):
                f['bridge']['kind'] = fd['bridge']['kind']
            if isinstance(e.get('a'), dict):
                e['a'].update(w=X, k=kind or e['a'].get('k'))
            def sub(t):
                for o in old:
                    if o and o != X:
                        t = t.replace(o, X)
                return t
            for x in e['fr']:
                if x['k'] in ('cultob', 'cultx', 'cultcena', 'culttl', 'bridge', 'wrap', 'fio', 'cultgame'):
                    for q, v in list(x.items()):
                        if q in ('art', 'c', 'seed', 'cam', 'scene'):
                            continue
                        x[q] = _walk(v, sub)
            changed += 1
        for e in eps:                        # cabeçalho `a` (obra do episódio) acompanha a obra mostrada
            if consistent(e) and isinstance(e.get('a'), dict):
                f = F(e)
                p0 = (f['cultob'].get('panels') or [''])[0]
                if isinstance(p0, list):
                    p0 = ' '.join(str(z) for z in p0)
                yr = next((w.get('y') for w in f['culttl'].get('works', []) if w.get('t') == 'main work'), None)
                first = re.split(r'(?<=[.!?])\s+', p0)[0] if p0 else ''
                e['a'].update(w=e['h']['src'], k=f['cultob'].get('kind') or e['a'].get('k'))
                if yr:
                    e['a']['y'] = yr
                if first:
                    e['a']['d'] = first
        for p, dd in blocks:
            open(p, 'w', encoding='utf-8').write(json.dumps(dd, ensure_ascii=False, separators=(',', ':')))
    print('alinhados:', changed, '| sem doador utilizável:', skipped)


def _walk(o, fn):
    if isinstance(o, str):
        return fn(o)
    if isinstance(o, list):
        return [_walk(v, fn) for v in o]
    if isinstance(o, dict):
        return {k: (v if k in ('art', 'c', 'seed', 'cam', 'scene') else _walk(v, fn)) for k, v in o.items()}
    return o


if __name__ == '__main__':
    run()
