#!/usr/bin/env python3
"""Revisão do episódio anterior (quadro `review`) nas aulas de regra do inglês, reexecutável.

As aulas 70/79 traziam um `review` de uma linha ("Review the key idea and say it aloud."). Aqui ele passa a
ter o mesmo formato das aulas autorais (mochila de palavras, verbos, coringas, expressões e sons + diálogo
para completar), montado só com o que o episódio ANTERIOR da mesma série já ensinou.
Uso: python3 tools/en_review.py [a1 a2 b1 b2 c1 c2]   (padrão: a1 = piloto)
Também corrige o nome da obra nos textos `coach` (relacione a fala à obra X / referência cultural X).
"""
import json, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
isgen = lambda e: str(e['n']).startswith(('70', '79'))


def F(e):
    fr = {}
    for x in e['fr']:
        fr.setdefault(x['k'], x)
    return fr


def work_of(e):
    h = e.get('h') if isinstance(e.get('h'), dict) else {}
    return h.get('src') or F(e).get('cultob', {}).get('work') or ''


def uniq(items, key):
    seen, out = set(), []
    for it in items:
        k = key(it).lower()
        if k and k not in seen:
            seen.add(k); out.append(it)
    return out


def build_review(e, p):
    fp = F(p)
    recap, words, verbs, wild, expr, sons = [], [], [], [], [], []
    cx = fp.get('cexp')
    if cx:
        for it in cx.get('items', []):
            recap.append([it['x'], it['pt']])
            expr.append({'ic': it.get('ic', '💬'), 't': it['x'], 'pt': it['pt']})
    sc = fp.get('scene')
    lines = [l for l in (sc or {}).get('lines', []) if len(l) >= 3]
    if len(recap) < 4:                                   # aulas de conversa: usa as falas da cena
        recap += [[l[1], l[2]] for l in lines[:4 - len(recap)]]
    for fk in ('vplay', 'words'):
        fr_ = fp.get(fk)
        if not fr_:
            continue
        for it in fr_.get('items', []):
            if isinstance(it, dict):
                words.append({'ic': '🔤', 't': it['v'], 'pt': it.get('pt', '')})
            else:
                words.append({'ic': it[1] if len(it) > 1 else '🔤', 't': it[0], 'pt': it[2] if len(it) > 2 else ''})
    lx = fp.get('lexpack')
    if lx:
        for it in lx.get('items', []):
            words.append({'ic': it.get('ic', '🔤'), 't': it['en'], 'pt': it.get('pt', '')})
    sb = fp.get('sbuild')
    if sb:
        for r in sb.get('rounds', []):
            parts = r.get('b', [])
            sent = ' '.join(b[0] for b in parts)
            for b in parts:
                if b[1] == 'Faz o quê':
                    verbs.append({'ic': '🏃', 't': b[0], 'pt': '', 's': sent})
    xp = fp.get('xpr')
    if xp:
        for it in xp.get('items', []):
            ex = it.get('ex') or []
            wild.append({'ic': it.get('ic', '🃏'), 't': ex[0] if ex else it.get('t', ''), 'pt': it.get('pt', ''),
                         's': (it.get('sw') or [[ex[0] if ex else '']])[0][0] if it.get('sw') else (ex[0] if ex else '')})
    sl = fp.get('soundlab')
    if sl:
        w0 = (sl.get('ex') or [['']])[0][0]
        sons.append({'ic': '🔬', 't': sl.get('short', ''), 'pt': '', 's': w0})
    bag = []
    for ic, lab, its in (('🔤', 'Palavras', words), ('🏃', 'Verbos', verbs), ('🃏', 'Coringas', wild),
                         ('💬', 'Expressões', expr), ('🎧', 'Sons', sons)):
        its = uniq(its, lambda z: z['t'])[:6]
        if its:
            bag.append({'ic': ic, 'l': lab, 'items': its})
    if len(recap) < 2 or len(lines) < 4 or len(bag) < 2:
        return None
    n = len(lines)
    gaps = sorted({1, min(3, n - 1), min(5, n - 1)})
    topic = e.get('s') or e['t']
    return {'k': 'review', 'prev': p['t'], 'work': work_of(p), 'recap': recap[:4], 'bag': bag,
            'lead': 'Abra cada bolso da mochila e relembre o episódio anterior!',
            'next': 'Hoje: **%s**' % topic,
            'say': 'Bora relembrar o episódio anterior antes de seguir!',
            'then': [{'k': 'dfill', 'title': 'Complete o diálogo',
                      'intro': 'Ouça o diálogo do episódio anterior no player. Depois toque numa fala-peça e no espaço onde ela encaixa.',
                      'cast': sc.get('cast', {}), 'lines': lines[:7], 'gaps': [g for g in gaps if g < min(n, 7)],
                      'rs': sc.get('rs', 'cafe3')}]}


COACH_WORK = [re.compile(r'(relacione a fala à obra )(.+?)(\.?)$'), re.compile(r'(referência cultural )(.+?)( a uma escolha)')]


def fix_coach(e):
    X = work_of(e)
    if not X:
        return 0
    n = 0
    for x in e['fr']:
        c = x.get('coach')
        if isinstance(c, str):
            for rx in COACH_WORK:
                m = rx.search(c)
                if m and m.group(2) != X:
                    x['coach'] = rx.sub(lambda mm: mm.group(1) + X + mm.group(3), c); n += 1
    return n


def run(levels):
    m = json.load(open(os.path.join(ROOT, 'manifest.json'), encoding='utf-8'))
    for lv in ['a1', 'a2', 'b1', 'b2', 'c1', 'c2']:
        blocks = [(os.path.join(ROOT, b), json.load(open(os.path.join(ROOT, b), encoding='utf-8'))) for b in m['en-' + lv]]
        eps = [e for _, d in blocks for e in d]
        fixed = built = skipped = 0
        for e in eps:
            fixed += fix_coach(e)
        if lv in levels:
            series = {}
            for e in eps:
                series.setdefault(str(e['n'])[:2], []).append(e)
            for pref, grp in series.items():
                if pref not in ('70', '79'):
                    continue
                grp.sort(key=lambda e: e['n'])
                for i, e in enumerate(grp):
                    rv = next((x for x in e['fr'] if x['k'] == 'review'), None)
                    if rv is None or 'bag' in rv or i == 0:
                        continue
                    new = build_review(e, grp[i - 1])
                    if new is None:
                        skipped += 1
                        continue
                    new['coach'] = rv.get('coach', '')
                    e['fr'][e['fr'].index(rv)] = new
                    built += 1
        for p, d in blocks:
            open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
        print(lv, 'coach corrigidos', fixed, '| revisões novas', built, '| puladas', skipped, flush=True)


if __name__ == '__main__':
    run([a.lower() for a in sys.argv[1:]] or ['a1'])
