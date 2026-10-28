#!/usr/bin/env python3
"""Sequência de produção do inglês C1 e C2: mostra o que já está escrito por lote e o próximo passo.
  python3 tools/seq/sequencia.py            # painel
  python3 tools/seq/sequencia.py --prompt   # imprime o prompt pronto do próximo lote pendente
Um lote = 51 episódios (posições do plano). Fica 'feito' quando os módulos tools/v3/<c1|c2>_*.py cobrem todos os n do lote."""
import glob, importlib, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
CURSOS = [('en-c1', 'c1', 'briefs_[0-9]*.json', 'GUIDE.md', ''), ('en-c2', 'c2', 'briefs_c2_[0-9]*.json', 'GUIDE_C2.md', 'COURSE_GEN=en-c2 ')]


def escritos(pfx):
    got = set()
    for f in glob.glob(os.path.join(ROOT, 'tools', 'v3', pfx + '_[0-9]*.py')):
        try:
            got |= {e['n'] for e in importlib.import_module('v3.' + os.path.basename(f)[:-3]).EPS}
        except Exception:
            pass
    return got


def lotes():
    out = []
    for curso, pfx, bf, guide, env in CURSOS:
        got = escritos(pfx)
        for f in sorted(glob.glob(os.path.join(ROOT, 'tools', 'c1gen', bf))):
            alvo = json.load(open(f))['alvo']
            falt = [x for x in alvo if x['n'] not in got]
            out.append(dict(curso=curso, pfx=pfx, brief=os.path.relpath(f, ROOT), guide=guide, env=env, total=len(alvo),
                            feitos=len(alvo) - len(falt), a=alvo[0]['pos'], b=alvo[-1]['pos'], faltam=[x['pos'] for x in falt]))
    return out


def main():
    L = lotes()
    if '--prompt' in sys.argv:
        for l in L:
            if l['faltam']:
                print(f"Leia tools/c1gen/{l['guide']} e siga-o à risca. Lote: {l['curso']} posições {l['a']}–{l['b']}, briefs em {l['brief']} (campo alvo). "
                      f"Já existem módulos tools/v3/{l['pfx']}_*.py com {l['feitos']} dos {l['total']} episódios: NÃO reescreva os prontos; escreva só os que faltam (posições {l['faltam'][:3]}…{l['faltam'][-1]}), "
                      f"em novos módulos de 5 episódios, e valide com {l['env']}python3 tools/c1gen/try.py <módulos> até 'problemas: 0'. Não toque em data/, não commite, não rode model_v3. Responda em português, curto.")
                return
        print('Todos os lotes escritos. Próximo: montar os dados (docs/SEQUENCIA_C1_C2.md, passo 2).')
        return
    print('curso  lote        feitos/total')
    for l in L:
        print(f"{l['curso']}  {l['a']:>3}-{l['b']:<3}   {l['feitos']:>2}/{l['total']}  {'ok' if not l['faltam'] else 'pendente'}")
    tot = sum(l['feitos'] for l in L)
    print(f'total escrito: {tot}/{sum(l["total"] for l in L)}')


main()
