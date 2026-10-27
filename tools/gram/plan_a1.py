#!/usr/bin/env python3
"""Cobertura extra do A1 de inglês: estruturas do programa (tools/gram/syllabus.py) e numerais que ficaram sem episódio dedicado
nos episódios 121–175 e foram transferidos para episódios pendentes. Cada item diz em qual episódio (n) a estrutura PRECISA aparecer
(como seção da regra, do molde e das missões). Uso: python3 tools/gram/plan_a1.py   → mostra o que já foi cumprido e o que falta."""
import glob, json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = [
 # (estrutura, episódio n, ep nº, o que ensinar, regex que deve aparecer no texto do episódio)
 ('freq', 7030034, 180, 'advérbios de frequência na rotina: always, usually, sometimes', r"\b(always|usually)\b"),
 ('freq', 80182, 239, 'every day + always / usually', r"\b(always|usually)\b"),
 ('freq', 7080182, 240, 'rotina da manhã com always / usually / never', r"\b(never|always)\b"),
 ('freq', 7080335, 440, 'jardim: often / sometimes', r"\b(often|sometimes)\b"),
 ('num', 80187, 247, 'números 11–20 e quinze minutos: fifteen, half past', r"\bfifteen\b|\bfourteen\b|\bthirteen\b"),
 ('num', 7080187, 248, 'minutos 16–59 (twenty-five past, ten to)', r"\btwenty[- ]five\b|\bthirty\b|\bforty\b"),
 ('num', 80188, 249, 'números grandes: hundred, thousand, million (salário)', r"\b(thousand|million|hundred)\b"),
 ('num', 10177, 193, 'ordinais e datas: first … thirty-first', r"\b(fifth|sixth|seventh|eighth|ninth|tenth|twentieth)\b"),
 ('num', 7010177, 194, 'ordinais 1–10 e My birthday is on the…', r"\b(seventh|eighth|ninth|tenth)\b"),
 ('num', 10178, 199, 'dezenas 20–100 e preços: twenty, fifty, hundred', r"\b(twenty|thirty|forty|fifty|sixty|ninety|hundred)\b"),
 ('num', 7080188, 250, 'graus e temperatura 30–100', r"\b(thirty|forty|fifty|sixty|seventy|eighty|ninety)\b"),
 ('prep_place', 7070070, 184, 'there is + in / on / under / next to (sala e móveis)', r"\bunder\b|\bnext to\b"),
 ('prep_place', 7080278, 366, 'there isn’t… in the box / on the table / under', r"\bunder\b|\bin the box\b|\bon the table\b"),
 ('conj', 910007, 83, 'because / so: I’m tired because…', r"\bbecause\b"),
 ('conj', 910006, 79, 'and / but / or', r"\bbut\b"),
 ('conj', 7910020, 216, 'both / the same / different: nós dois', r"\bboth\b"),
 ('conj', 7910029, 312, 'because: I feel sad because…', r"\bbecause\b"),
 ('conj', 80264, 347, 'so / but com too: It is too wide, so…', r"\bso\b|\bbut\b"),
]
def load():
    d = {}
    for f in glob.glob(os.path.join(ROOT, 'data/en-a1_*.json')):
        for x in json.load(open(f, encoding='utf-8')): d[x['n']] = x
    return d
def text(x):
    return json.dumps([x.get('fr'), x.get('g'), x.get('gs')], ensure_ascii=False).lower()
if __name__ == '__main__':
    d = load(); falta = 0
    for sid, n, ep, what, rx in PLAN:
        x = d.get(n)
        if not x: print('?? %s ep %d (n=%d) não encontrado' % (sid, ep, n)); continue
        if not x.get('pilot'): st = 'pendente'
        elif re.search(rx, text(x), re.I): st = 'OK'
        else: st = 'FALTA'; falta += 1
        print('%-10s ep %3d  %-9s %s' % (sid, ep, st, what))
    print('faltando em episódios já prontos:', falta)
