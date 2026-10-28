#!/usr/bin/env python3
"""Autoteste da trava (em memória, não grava nada): um episódio bom precisa passar e cada defeito conhecido precisa reprovar.
Uso: python3 tools/audit/test_gate.py   (sai com código 1 se algum teste falhar)"""
import copy, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), 'tools', 'plan'))
os.chdir(os.path.dirname(os.path.dirname(HERE)))
import plan_lib as P
import regular_pilot_contract as C
from bridge_rules import bridge_failures

bom = next(e for e in P.load_course('en-b2') if e['n'] == 7940066)   # B2 'Fargo': modelo de ponte
anterior = next(e for e in P.load_course('en-b2') if e['n'] == 940066)   # vizinho anterior: o 2º episódio da lista não é isento da mochila
fr = lambda e, k: [f for f in e['fr'] if f['k'] == k]
casos = []


def caso(nome, mut, esperado):
    e = copy.deepcopy(bom); mut(e); falhas = bridge_failures(e) + C.audit('en-b2', [('x', anterior), ('x', e)], ponte=False)
    casos.append((nome, esperado, any(esperado in f for f in falhas), falhas))


caso('episódio bom passa', lambda e: None, None)
caso('missão sem “Cena da obra”', lambda e: fr(e, 'pgmission')[0]['missions'][0].update(name='Missão 1'), 'ponte: a missão')
caso('missão sem citar a obra', lambda e: fr(e, 'pgmission')[0]['missions'][0]['data'].update(prompt='Fale.', model='Hello.', chips=['Hello.']), 'ponte: a missão')
caso('elenco genérico', lambda e: fr(e, 'pgscene')[0].update(cast={'Woman': ['👩', '#000'], 'Man': ['🧑', '#111']}), 'ponte: elenco genérico')
caso('cenas sem a obra', lambda e: [s.update(lines=[[l[0], 'Hello there my friend.', l[2]] for l in s['lines']]) for s in fr(e, 'pgscene')], 'ponte: nenhuma fala')
caso('gancho de outra obra', lambda e: e['h'].update(src='Outra Obra'), 'ponte: o gancho')
caso('figurinha de outra obra', lambda e: fr(e, 'wrap')[0]['sticker'].update(sub='Outra Obra · 2000', title='Outro'), 'ponte: a figurinha')
caso('obra sem descrição', lambda e: e['a'].update(d='curta'), 'ponte: descrição')
caso('cenário 3× seguido', lambda e: [f.update(rs='cafe') for f in e['fr'][2:6]], 'ponte: o mesmo cenário')
caso('só 3 verbos (estrutura)', lambda e: fr(e, 'verbs')[0].update(items=fr(e, 'verbs')[0]['items'][:3]), 'precisa de exatamente 4 verbos')
caso('sem a mochila (estrutura)', lambda e: e['fr'].pop(1), 'mochila')
# expressões únicas (tools/audit/expr_rules.py)
from expr_rules import expr_repetidas
def exp_casos():
    out = []
    a = copy.deepcopy(bom); b = copy.deepcopy(anterior)
    out.append(('expressões distintas passam', not expr_repetidas([b, a])))
    ia = fr(a, 'pgexp')[0]['items']; ib = fr(b, 'pgexp')[0]['items']
    ib[0]['en'] = ia[0]['en'].upper().rstrip('.!?') + ' !'   # mesma expressão, outra caixa/pontuação, em outro episódio
    out.append(('expressão repetida em outro episódio reprova', any(r[0] == a['n'] for r in expr_repetidas([b, a]))))
    a2 = copy.deepcopy(bom); it = fr(a2, 'pgexp')[0]['items']; it[1]['en'] = it[0]['en'] + ' '
    out.append(('expressão duplicada no mesmo episódio reprova', bool(expr_repetidas([a2]))))
    return out
for nome, res in exp_casos():
    casos.append((nome, 'x', res, [] if res else ['falhou']))
ruim = 0
for nome, esp, ok, falhas in casos:
    if esp is None:
        res = not falhas
    else:
        res = ok
    print(('OK  ' if res else 'XX  ') + nome + ('' if res else '  -> %s' % falhas[:2]))
    ruim += not res
print('testes:', len(casos), '| falharam:', ruim)
sys.exit(1 if ruim else 0)
