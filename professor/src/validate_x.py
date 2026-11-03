#!/usr/bin/env python3
"""Valida o bloco extra src/supp5/xNNN.py (padrão aula 1). Uso: validate_x.py N [N…] | --all"""
import glob, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build_v5 as B, lesson_focus as LF
SW = re.compile(r'\{([^{}]+)\}')
def groups(t): return [g.split('|') for g in SW.findall(t)]
def check(n):
    E = []; X = B.extras(n)
    if not X: return ['sem bloco extra']
    nb = B.NB[n - 1]; base = [f for f in nb['fr'] if f['k'] == 'nbchat'][0]
    lines = [l for l in base['lines'] if l[1] not in B.FILLER]; who = [l[0] for l in lines]
    k = X.get('key') or {}
    if not (k.get('big') and k.get('label') and k.get('sub')): E.append('key: big/label/sub')
    mini = X.get('mini') or []
    if len(mini) != 4: E.append('mini: exatamente 4 falas')
    sw = 0
    for m in mini:
        ge, gp = groups(m.get('en', '')), groups(m.get('pt', ''))
        sw += len(ge)
        if len(ge) != len(gp) or any(len(a) != len(b) for a, b in zip(ge, gp)): E.append('mini: trocas {a|b|c} do en e do pt precisam ser paralelas (mesma quantidade e opções)')
        if any(len(g) < 2 for g in ge): E.append('mini: cada troca precisa de 2+ opções')
        if m.get('who') not in set(who): E.append('mini: who inválido ' + str(m.get('who')))
    if sw < 3: E.append('mini: pelo menos 3 trocas {a|b|c}')
    d = X.get('dlg') or []
    if len(d) != len(lines): E.append('dlg: precisa ter %d falas (tem %d)' % (len(lines), len(d)))
    else:
        tot = 0
        for i, (a, l) in enumerate(zip(d, lines)):
            if a.get('who') != l[0]: E.append('dlg[%d]: who deve ser %s' % (i, l[0])); break
            ge, gp = groups(a['en']), groups(a['pt']); tot += len(ge)
            if len(ge) != len(gp) or any(len(x) != len(y) for x, y in zip(ge, gp)): E.append('dlg[%d]: trocas en/pt não paralelas' % i)
        if tot < 6: E.append('dlg: pelo menos 6 trocas no total')
    v = X.get('vocab') or []
    if len(v) != 6: E.append('vocab: exatamente 6 palavras')
    for x in v:
        if not (x.get('w') and x.get('pt') and x.get('e') and len(x.get('ex', [])) == 2): E.append('vocab: w/pt/e/ex[2] em ' + str(x.get('w')))
        else:
            for s in x['ex']:
                if x['w'].lower().rstrip('s') not in s.lower(): E.append('vocab: exemplo sem a palavra ' + x['w'])
    mo = X.get('molds') or []
    if len(mo) != 3: E.append('molds: exatamente 3')
    for m in mo:
        keys = re.findall(r'\{(\w+)\}', m.get('frame', '')); sl = {s['key']: s['opts'] for s in m.get('slots', [])}
        if not keys or set(keys) != set(sl): E.append('molds: slots precisam cobrir todos os {key} do frame: ' + m.get('frame', ''))
        if any(len(o) < 3 for o in sl.values()): E.append('molds: cada slot com 3+ opções')
        mdl = m.get('frame', '')
        for kk, o in sl.items(): mdl = mdl.replace('{' + kk + '}', o[0])
        if m.get('model') != mdl: E.append('molds: model deve ser o frame com as primeiras opções: ' + mdl)
        if not m.get('note'): E.append('molds: note (PT)')
    so = X.get('sounds') or []
    if len(so) != 3 or any(not (s.get('say') and s.get('tag') and s.get('tip')) for s in so): E.append('sounds: 3 itens com say/tag/tip')
    r = (X.get('role') or {}); tu = r.get('turns') or []
    if len(tu) != 4: E.append('role.turns: exatamente 4')
    for t in tu:
        if len(t.get('opts', [])) != 3 or any(not (o.get('en') and o.get('pt') and o.get('reply')) for o in t['opts']): E.append('role: cada turno com 3 opções en/pt/reply')
        if len({o['en'] for o in t.get('opts', [])}) < 3: E.append('role: opções diferentes entre si')
    if len(r.get('change', [])) != 3: E.append('role.change: 3 complicações em PT')
    w = X.get('writing') or {}
    if not (w.get('task') and len(re.findall(r'[A-Za-z]+', w.get('model', ''))) >= 12 and len(w.get('kw', [])) >= 4 and len(w.get('checks', [])) == 3): E.append('writing: task, model (12+ palavras), kw (4+), checks (3)')
    sc = X.get('scenes') or {}
    if not (3 <= len(sc.get('pool', [])) <= 6) or any(x not in LF.RS for x in sc.get('pool', [])): E.append('scenes.pool: 3–6 chaves válidas de ' + ' '.join(sorted(LF.RS)))
    if (sc.get('npc') or {}).get('g') not in ('f', 'm') or (sc.get('you') or {}).get('g') not in ('f', 'm') or not (sc.get('npc') or {}).get('role'): E.append('scenes: npc{g,role} e you{g}')
    c = X.get('convo') or {}; tn = c.get('turns', [])
    if len(tn) < 4: E.append('convo: 4+ turnos')
    for t in tn:
        o = t.get('opts', [])
        if len(o) != 3 or sum(1 for x in o if x.get('ok')) != 1: E.append('convo: 3 opções e exatamente 1 ok'); break
        for x in o:
            if not (x.get('en') and x.get('pt') and x.get('fb')): E.append('convo: opção sem en/pt/fb'); break
            if len(re.findall(r'[A-Za-z]+', x['en'])) < 2: E.append('convo: alternativa curta demais: ' + x['en'])
    try: B.build(n)
    except Exception as e: E.append('build falhou: %s' % e)
    return E
if __name__ == '__main__':
    a = sys.argv[1:]; ns = sorted(int(os.path.basename(f)[1:4]) for f in glob.glob(os.path.join(HERE, 'supp5', 'x[0-9][0-9][0-9].py'))) if '--all' in a else [int(x) for x in a]
    bad = 0
    for n in ns:
        e = check(n)
        if e: bad += 1; print('AULA %d:' % n, *['  - ' + x for x in e[:12]], sep='\n')
    print('ok' if not bad else 'aulas com erro: %d' % bad); sys.exit(1 if bad else 0)
