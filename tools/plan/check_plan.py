#!/usr/bin/env python3
"""Valida o mapeamento (tools/plan/map) e o plano gerado. Uso: python3 tools/plan/check_plan.py en-c1 en-c2 [--estrito]
Erros: campos faltando, 4 verbos/4 expressões distintos, obra/gs únicos nos cursos listados e nas obras já em uso no mesmo idioma,
expressão única no curso, vizinhos sem 2+ verbos em comum. --estrito: todo episódio precisa estar mapeado."""
import collections, glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import plan_lib as P

args = [a for a in sys.argv[1:] if not a.startswith('--')]
estrito = '--estrito' in sys.argv
nx = P.fold
erros, avisos = [], []

# obras já em uso nos cursos prontos do mesmo idioma (dados reais)
usadas = collections.defaultdict(list)
langs = {c.split('-')[0] for c in args}
manifest = json.load(open(os.path.join(P.ROOT, 'data', 'manifest.json'), encoding='utf-8'))
for c in manifest:
    if c in args or c.startswith('nb') or c.split('-')[0] not in langs:
        continue
    for e in P.load_course(c):
        if e.get('presentation') == 'regular-pilot-v1' and P.obra_of(e):
            usadas[P.norm(P.obra_of(e))].append(c)

prontos = set()
obras = collections.defaultdict(list)
gss = collections.defaultdict(list)
exps = collections.defaultdict(list)
total = {}
for c in args:
    plan = json.load(open(os.path.join(P.ROOT, 'plano', c + '.json'), encoding='utf-8'))
    ents = plan['entradas']
    total[c] = [0, len(ents)]
    prev = None
    for e in ents:
        lab = '%s #%d (n=%s)' % (c, e['pos'], e['n'])
        if e['estado'] == 'pronto':
            prontos.add(lab)
        if e['estado'] == 'a mapear':
            if estrito:
                erros.append(lab + ': não mapeado')
            prev = None
            continue
        total[c][0] += 1
        ob = e.get('obra') or {}
        if not ob.get('nome'):
            erros.append(lab + ': obra ausente')
        else:
            obras[P.norm(ob['nome'])].append(lab)
            if e['estado'] == 'mapeado':
                if ':' in ob['nome']:
                    erros.append(lab + ': título da obra com ":"')
                for k in ('tipo', 'criador'):
                    if not ob.get(k):
                        erros.append(lab + ': obra sem ' + k)
                if P.norm(ob['nome']) in usadas:
                    avisos.append(lab + ': obra "%s" já usada em %s' % (ob['nome'], ','.join(sorted(set(usadas[P.norm(ob['nome'])])))))
        v = e.get('verbos') or []
        if len({nx(x) for x in v}) != 4 or any(not nx(x) for x in v):
            erros.append(lab + ': precisa de 4 verbos distintos')
        x = e.get('expressoes') or []
        if len({nx(y) for y in x}) != 4 or any(not nx(y) for y in x):
            erros.append(lab + ': precisa de 4 expressões distintas')
        for y in x:
            exps[(c, nx(y))].append(lab)
        if e['estado'] == 'mapeado':
            if not e.get('gs') or not e.get('foco'):
                erros.append(lab + ': gs/foco ausente')
            else:
                gss[(c, nx(e['gs']))].append(lab)
        if prev and e['estado'] == 'mapeado' and len({nx(a) for a in v} & {nx(a) for a in prev}) >= 2:
            erros.append(lab + ': 2+ verbos iguais aos do episódio anterior')
        prev = v if len(v) == 4 else None
for k, v in obras.items():
    if len(v) > 1 and not all(x in prontos for x in v):
        erros.append('obra repetida: ' + ' | '.join(v))
for k, v in gss.items():
    if len(v) > 1:
        erros.append('gs repetido (%s): ' % k[1] + ' | '.join(v))
for k, v in exps.items():
    if len(v) > 1 and not all(x in prontos for x in v):
        erros.append('expressão repetida "%s": ' % k[1] + ' | '.join(v))
for c, (m, t) in total.items():
    print('%s: %d de %d mapeados' % (c, m, t))
print('avisos (obra já usada em outro nível):', len(avisos))
for a in avisos[:5]:
    print('  aviso:', a)
print('erros:', len(erros))
for e in (erros if '--tudo' in sys.argv else erros[:60]):
    print('  ERRO', e)
sys.exit(1 if erros else 0)
