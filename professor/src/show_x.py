#!/usr/bin/env python3
"""Mostra o que o agente precisa para escrever o bloco extra da aula N: falas do diálogo (já sem as falas genéricas), vocabulário, convo e cena."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_v5 as B
n = int(sys.argv[1]); nb = B.NB[n - 1]; S = B.supp(n)
base = [f for f in nb['fr'] if f['k'] == 'nbchat'][0]
lines = [l for l in base['lines'] if l[1] not in B.FILLER]
print('AULA %d · %s · cena Neighbors: %s' % (n, nb['t'], nb.get('sc')))
print('DIÁLOGO (índice: quem | en | pt) — o seu dlg precisa ter ESTE número de falas, na mesma ordem e com o mesmo "who":')
for i, (w, e, p) in enumerate(lines): print('  %2d %s | %s | %s' % (i, w, re.sub(r'\*\*', '', e), p))
voc = [f for f in nb['fr'] if f['k'] == 'nbvocab']
print('VOCABULÁRIO do Neighbors:', [(v[0], v[1], v[2]) for v in voc[0]['items']] if voc else '—')
print('CONVO atual (turnos do npc):', [t['npc'] for t in S.get('convo', {}).get('turns', [])])
print('ELENCO: o personagem que atende/fala com o aluno é', [k for k in base['cast'] if k != 'You'][:2], '| o aluno é "You" (se não houver, é o 2º falante)')
