#!/usr/bin/env python3
"""Reduz o curso regular de inglês de 5.000 para 3.000 episódios e grava o plano de cada um.

Unidade = par (episódio autoral + episódio-regra que o acompanha, ligados por xn/xof).
Todo padrão gramatical e toda obra autoral são mantidos; sai a maior parte dos episódios-regra,
e o que eles tinham (expressões, laboratório de sons) vai para o plano do autoral.
Os cinco primeiros episódios (já refeitos) ficam intactos e não recebem plano.
  python3 tools/plan_en3000.py          # regrava data/en-*_NN.json + docs/PLANO_INGLES_3000.md
  python3 tools/plan_en3000.py --dry    # só mostra os números
"""
import glob, json, os, re, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
TARGET = {'a1': 466, 'a2': 475, 'b1': 529, 'b2': 510, 'c1': 510, 'c2': 510}
FIRST5 = {9801, 7009801, 70001, 7070001, 30001}
CH = 25
dump = lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':'))


def load(lv):
    out = []
    for f in sorted(glob.glob(f'{ROOT}/data/en-{lv}_*.json')):
        out += json.load(open(f, encoding='utf-8'))
    return out


def fr(e, k):
    return next((f for f in e['fr'] if f.get('k') == k), None)


def plan_of(A, C, role):
    verbs, words, exps, ctx = [], [], [], []
    f = fr(A, 'verbs')
    for it in (f or {}).get('items', [])[:4]:
        verbs.append({'v': it['v'], 'pt': it['pt']})
    f = fr(A, 'words')
    for it in (f or {}).get('items', [])[:8]:
        words.append({'en': it[0], 'pt': it[2]})
    if not words:
        words = [{'en': w[0], 'pt': w[1]} for w in (A.get('v') or [])[:8]]
    if C:
        f = fr(C, 'cexp')
        for it in (f or {}).get('items', [])[:4]:
            exps.append({'en': it['x'], 'pt': it['pt']})
        f = fr(C, 'xpr')
        for it in (f or {}).get('items', []):
            if len(exps) >= 6: break
            ex = it.get('ex')
            if ex and not any(x['en'] == ex[0] for x in exps):
                exps.append({'en': ex[0], 'pt': ex[1]})
    f = fr(A, 'wsent')
    for it in (f or {}).get('items', [])[:6]:
        ctx.append({'en': it['en'].replace('{{', '').replace('}}', ''), 'pt': it['pt']})
    sound = None
    s = fr(C, 'soundlab') if C else None
    if s:
        sound = {'short': s.get('short'), 'title': s.get('title')}
    else:
        s = fr(A, 'lplay')
        if s:
            sound = {'short': s.get('short'), 'title': s.get('title')}
    todo = []
    if len(verbs) < 4: todo.append('verbos')
    if len(exps) < 4: todo.append('expressões e gírias')
    if not sound: todo.append('laboratório de sons')
    if len(words) < 6: todo.append('vocabulário')
    if len(ctx) < 6: todo.append('frases de contexto')
    a = A.get('a') or {}
    return {'v': 1, 'role': role, 'pattern': (A.get('g') or {}).get('t') or A.get('s'),
            'obra': {'k': a.get('k'), 'w': a.get('w'), 'y': a.get('y')}, 'rs': A.get('rs'),
            'verbs': verbs, 'exps': exps, 'sound': sound, 'words': words, 'ctx': ctx, 'todo': todo}


def main():
    dry = '--dry' in sys.argv
    report, keep_map, removed_to = {}, {}, {}
    new = {}
    for lv, T in TARGET.items():
        eps = load(lv)
        byn = {e['n']: e for e in eps}
        units, seen = [], set()
        for e in eps:
            if e['n'] in seen: continue
            if e.get('xn') and e['xn'] in byn:
                units.append((e, byn[e['xn']])); seen |= {e['n'], e['xn']}
            elif not e.get('xof'):
                units.append((e, None)); seen.add(e['n'])
        orphan = [e['n'] for e in eps if e['n'] not in seen]
        P = len(units); D = T - sum(1 for u in units if not u[1]) - P + sum(1 for u in units if not u[1])
        D = T - P
        assert 0 <= D <= sum(1 for u in units if u[1]), (lv, T, P)
        forced = {i for i, (a, c) in enumerate(units) if c and (a['n'] in FIRST5 or c['n'] in FIRST5)}
        cand = [i for i, (a, c) in enumerate(units) if c and i not in forced]
        # prefere dobrar onde o par traz uma obra que nenhum autoral usa (mais obras distintas)
        wa = {(a['a'] or {}).get('w') for a, c in units}
        seenw = set()
        novel = []
        for i in cand:
            w = (units[i][1]['a'] or {}).get('w')
            if w not in wa and w not in seenw:
                novel.append(i); seenw.add(w)
        need0 = D - len(forced)
        if len(novel) >= need0: cand = novel
        need = D - len(forced)
        pick = set(forced)
        if need > 0:
            for k in range(need):
                pick.add(cand[int((k + .5) * len(cand) / need)])
        out = []
        for i, (a, c) in enumerate(units):
            pil = a['n'] in FIRST5 or (c and c['n'] in FIRST5)
            ka = [a] + ([c] if c and i in pick else [])
            for e in ka:
                if e['n'] not in FIRST5:
                    e['plan'] = plan_of(a, c, 'autoral' if e is a else 'regra')
                out.append(e)
            if c and i not in pick:
                removed_to[c['n']] = a['n']
        assert len(out) == T, (lv, len(out), T)
        new[lv] = out
        works = {(e['a'] or {}).get('w') for e in out}
        todo = sum(1 for e in out if e.get('plan') and e['plan']['todo'])
        report[lv] = dict(antes=len(eps), depois=len(out), pares=P, dobrados=len(pick), obras=len(works), plano_incompleto=todo, orfaos=orphan)
        print(lv, report[lv])
    if dry: return
    for lv, out in new.items():
        for f in glob.glob(f'{ROOT}/data/en-{lv}_*.json'): os.remove(f)
        for i in range(0, len(out), CH):
            open(f'{ROOT}/data/en-{lv}_{i // CH + 1:02d}.json', 'w', encoding='utf-8').write(dump(out[i:i + CH]) + '\n')
    json.dump({'removidos': {str(k): v for k, v in removed_to.items()}, 'relatorio': report}, open(f'{ROOT}/docs/plano_en3000.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('removidos', len(removed_to))

main()
