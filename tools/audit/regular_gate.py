#!/usr/bin/env python3
"""TRAVA de qualidade dos cursos regulares (nunca Neighbors). Roda em todo PR que mexe em data/ (ver .github/workflows/regular-quality-gate.yml).

Regras:
 1. Todo episódio marcado `regular-pilot-v1`, em QUALQUER curso regular, precisa passar o contrato (19 quadros, 6 palavras, 4 verbos,
    4 expressões, laboratório 3+3, duas cenas densas, 3 missões, mochila, obra própria) — a medida dos episódios 2–5 do inglês.
 2. Obra única entre os episódios marcados do mesmo curso (nome normalizado).
 3. Cursos listados em tools/audit/gate_enforced.json precisam ter 100% dos episódios marcados.
 4. Episódio que já tem mapeamento em tools/plan/map/ e está marcado precisa usar a obra, os 4 verbos e as 4 expressões mapeados.
 5. A PONTE obra↔episódio (tools/audit/bridge_rules.py, docs/PADRAO_PONTE_OBRA.md) é regra de todo episódio marcado: obra nas cenas, missão
    “Cena da obra” ligada à obra, gancho e figurinha da obra, descrição da obra, elenco não genérico, cenário sem 3 repetições seguidas.
 6. Falhas que já existiam (tools/audit/gate_baseline.json) são toleradas; falha nova bloqueia. `--shrink` tira do baseline o que já foi corrigido.
Uso: python3 tools/audit/regular_gate.py [--update-baseline] [--course en-b1 ...]"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, 'tools', 'plan'))
import regular_pilot_contract as C
import plan_lib as P

os.chdir(ROOT)
manifest = json.load(open('data/manifest.json', encoding='utf-8'))
regular = [c for c in manifest if not c.startswith('nb')]
sel = []
a = sys.argv[1:]
while '--course' in a:
    i = a.index('--course'); sel.append(a[i + 1]); del a[i:i + 2]
courses = sel or regular
enforced = json.load(open(os.path.join(HERE, 'gate_enforced.json')))['cursos']
plano_ativo = json.load(open(os.path.join(HERE, 'gate_plan_ativo.json')))['cursos']
bpath = os.path.join(HERE, 'gate_baseline.json')
baseline = set(json.load(open(bpath))['falhas']) if os.path.exists(bpath) else set()
nx = P.fold

found = set()      # (chave, texto)
for c in courses:
    eps = C.load_course(manifest, c)
    pilot_n = {e.get('n') for _, e in eps if e.get('presentation') == 'regular-pilot-v1'}
    for f in C.audit(c, eps):
        m = re.search(r'\((\d+),', f)
        if m and int(m.group(1)) in pilot_n and 'presentation ausente' not in f:
            found.add('%s|%s|%s' % (c, m.group(1), f.split(': ', 1)[1]))
    # obra única entre marcados
    seen = {}
    for _, e in eps:
        if e.get('presentation') == 'regular-pilot-v1':
            o = P.obra_of(e)
            k = P.norm(o)
            if k and k in seen:
                found.add('%s|%s|obra repetida com %s: %s' % (c, e['n'], seen[k], o))
            seen.setdefault(k, e['n'])
    if c in enforced:
        for _, e in eps:
            if e.get('presentation') != 'regular-pilot-v1':
                found.add('%s|%s|curso fechado: episódio fora do modelo piloto' % (c, e['n']))
    # aderência ao plano
    maps = P.read_maps(c) if c in plano_ativo else {}
    for _, e in eps:
        m = maps.get(e['n'])
        if m and e.get('presentation') == 'regular-pilot-v1':
            fr = {}
            for q in e['fr']:
                fr.setdefault(q['k'], []).append(q)
            v = [nx(x.get('v')) for x in (fr.get('verbs') or [{}])[0].get('items', [])]
            x = [nx(y.get('en')) for y in (fr.get('pgexp') or [{}])[0].get('items', [])]
            if P.norm(P.obra_of(e)) != P.norm((m.get('obra') or {}).get('nome')):
                found.add('%s|%s|fora do plano: obra %r (plano: %r)' % (c, e['n'], P.obra_of(e), m['obra']['nome']))
            if sorted(v) != sorted(nx(y) for y in m.get('verbos', [])):
                found.add('%s|%s|fora do plano: verbos' % (c, e['n']))
            if sorted(x) != sorted(nx(y) for y in m.get('expressoes', [])):
                found.add('%s|%s|fora do plano: expressões' % (c, e['n']))

if '--shrink' in sys.argv:  # só remove do baseline o que já foi corrigido; nunca adiciona falha nova
    keep = sorted(baseline & found)
    json.dump({'nota': 'Falhas já existentes toleradas pela trava; só falhas novas bloqueiam. Gerado por regular_gate.py (--update-baseline ou --shrink).', 'falhas': keep},
              open(bpath, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('baseline reduzido de', len(baseline), 'para', len(keep), '(', len(baseline) - len(keep), 'falhas corrigidas )')
    sys.exit(0)
if '--update-baseline' in sys.argv:
    json.dump({'nota': 'Falhas já existentes tolerados pela trava; só falhas novas bloqueiam. Gerado por regular_gate.py --update-baseline.', 'falhas': sorted(found)},
              open(bpath, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('baseline gravado:', len(found), 'falhas toleradas')
    sys.exit(0)
novas = sorted(f for f in found if f not in baseline)
print('cursos regulares auditados:', len(courses), '| falhas atuais:', len(found), '| toleradas (baseline):', len(found & baseline), '| NOVAS:', len(novas))
for f in novas[:80]:
    print('  NOVA FALHA', f)
sys.exit(1 if novas else 0)
