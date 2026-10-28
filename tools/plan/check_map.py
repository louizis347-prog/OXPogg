#!/usr/bin/env python3
"""Valida um arquivo de mapeamento (tools/plan/map/<curso>_<parte>.json) sem montar o plano.
Uso: python3 tools/plan/check_map.py <arquivo.json> [--pool A,B,..] [--evitar obras_em_uso.json] [--ancoras ancoras.json ...]"""
import collections, glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import plan_lib as P

a = sys.argv[1:]
f = a[0]
pool = None; evitar = None; anc = []
i = 1
while i < len(a):
    if a[i] == '--pool': pool = set(a[i + 1].split(',')); i += 2
    elif a[i] == '--evitar': evitar = json.load(open(a[i + 1])); i += 2
    elif a[i] == '--ancoras': anc.append(a[i + 1]); i += 2
    else: i += 1
nx = P.fold
rows = json.load(open(f, encoding='utf-8'))
erros = []
need = set()
for x in anc:
    need |= {e['n'] for e in json.load(open(x))}
got = {r['n'] for r in rows}
if need:
    for n in sorted(need - got): erros.append('episódio sem mapeamento: %s' % n)
    for n in sorted(got - need): erros.append('episódio fora da lista: %s' % n)
ev = {P.norm(o) for o in (evitar or [])}
# obras e expressões dos outros arquivos de mapa já existentes (outros agentes/cursos)
outras_obras = collections.defaultdict(str); outras_exp = {}; outras_gs = {}
curso = os.path.basename(f).split('_')[0]
for g in glob.glob(os.path.join(P.ROOT, 'tools', 'plan', 'map', '*.json')):
    if os.path.abspath(g) == os.path.abspath(f): continue
    for r in json.load(open(g, encoding='utf-8')):
        outras_obras[P.norm((r.get('obra') or {}).get('nome'))] = os.path.basename(g)
        for e in r.get('expressoes', []): outras_exp[nx(e)] = os.path.basename(g)
        if os.path.basename(g).split('_')[0] == curso: outras_gs[nx(r.get('gs'))] = os.path.basename(g)
ob, gs, ex = {}, {}, {}
prev = None
for r in sorted(rows, key=lambda r: need and sorted(need).index(r['n']) if r['n'] in need else r['n']):
    lab = 'n=%s' % r['n']
    o = r.get('obra') or {}
    nome = o.get('nome') or ''
    if not nome or not o.get('tipo') or not o.get('criador'): erros.append(lab + ': obra incompleta (nome, tipo, criador)')
    if ':' in nome: erros.append(lab + ': nome da obra com ":"')
    k = P.norm(nome)
    if k in ob: erros.append(lab + ': obra repetida com n=%s: %s' % (ob[k], nome))
    ob.setdefault(k, r['n'])
    if k in ev: erros.append(lab + ': obra já em uso: ' + nome)
    if k in outras_obras: erros.append(lab + ': obra já mapeada em ' + outras_obras[k] + ': ' + nome)
    if pool:
        first = ((P.fold(nome.split(':')[0]) and re.sub(r'^(the|a|an|el|la|los|las|un|una|le|les|il|der|die|das|o|os|as) ', '', P.fold(nome.split(':')[0]))) or ' ')[0].upper()
        if first not in pool: erros.append(lab + ': inicial %s fora do pool %s: %s' % (first, sorted(pool), nome))
    if not r.get('foco') or not r.get('gs'): erros.append(lab + ': foco/gs ausente')
    g = nx(r.get('gs'))
    if g in gs: erros.append(lab + ': gs repetido com n=%s' % gs[g])
    if g in outras_gs: erros.append(lab + ': gs já mapeado em ' + outras_gs[g])
    gs.setdefault(g, r['n'])
    v = r.get('verbos') or []
    if len(v) != 4 or len({nx(y) for y in v}) != 4: erros.append(lab + ': precisa de 4 verbos distintos')
    e = r.get('expressoes') or []
    if len(e) != 4 or len({nx(y) for y in e}) != 4: erros.append(lab + ': precisa de 4 expressões distintas')
    for y in e:
        if nx(y) in ex: erros.append(lab + ': expressão repetida "%s" (n=%s)' % (y, ex[nx(y)]))
        if nx(y) in outras_exp: erros.append(lab + ': expressão "%s" já mapeada em %s' % (y, outras_exp[nx(y)]))
        ex.setdefault(nx(y), r['n'])
    if prev is not None and len({nx(y) for y in v} & {nx(y) for y in prev}) >= 2: erros.append(lab + ': 2+ verbos iguais aos do anterior')
    prev = v
print('episódios:', len(rows), '| erros:', len(erros))
for e in erros[:50]: print('  ERRO', e)
sys.exit(1 if erros else 0)
