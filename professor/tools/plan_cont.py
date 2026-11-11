#!/usr/bin/env python3
"""Plano das continuações: para cada aula original n (1–248), define a continuação 1000+n:
domínio CEFR A1 (can-do), teto gramatical (nunca acima do bloco da aula original), âncora (estrutura da original)
e o episódio Neighbors proposto. Saída: data/plano-continuacoes.json e ../docs/PLANO_CONTINUACOES.md."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, os.path.join(ROOT, 'src'))
import build_v5 as B
DOM = [
 ('Dados pessoais e apresentações', 'Consigo me apresentar, dizer nome, origem, idade e família e fazer perguntas simples sobre isso.', r'meet|name|spell|from|old|family|friend|introduc|hello|goodbye|neighbor|describ|pet|birthday|hometown|congrat|roll call'),
 ('Compras e dinheiro', 'Consigo pedir, perguntar preços e pagar em lojas, usando números e quantidades.', r'buy|shop|store|price|money|dollar|cash|return|sale|market|mall|clothes|shoe|gift|exchange|checkout|register|sold|garage|flower|butcher|book|watch|headphone|earring|souvenir|ticket|vending|toy|nail|tailor|copy|printing|charger|bike|used'),
 ('Comida e bebida', 'Consigo pedir comida e bebida, escolher e perguntar ingredientes.', r'coffee|food|lunch|dinner|breakfast|pizza|burger|bowl|cook|restaurant|cafe|diner|bakery|ice cream|water|menu|order|sandwich|deli|donut|tea|smoothie|brunch|meal|snack|cake|egg|toast|pasta|potluck|barbecue|vegetarian|hungry'),
 ('Lugares, direções e transporte', 'Consigo perguntar e entender direções e usar transporte público ou táxi.', r'where|bus|train|subway|taxi|ride|car|park|gas|street|turn|lost|far|map|airport|flight|ferry|road|traffic|toll|parking|drive|bike|uber|station|way|crossing'),
 ('Viagem e hospedagem', 'Consigo fazer check-in, pedir informações turísticas e resolver pequenos problemas em viagem.', r'hotel|room|hostel|check|passport|baggage|tour|tourist|museum|trip|travel|beach|camp|festival|visit|welcome to|city|zoo|aquarium|national|college tour'),
 ('Casa e rotina', 'Consigo falar da casa, das tarefas e da rotina diária com frases simples.', r'home|house|apartment|kitchen|laundry|chore|clean|routine|morning|bed|sleep|trash|wi-fi|furniture|landlord|rent|moving|dish|window|lawn|microwave|thermostat|plumber|smoke|power|heater|key|locked'),
 ('Saúde e corpo', 'Consigo dizer como me sinto e pedir ajuda em uma consulta ou farmácia.', r'doctor|sick|body|health|dentist|glasses|eye|pharmacy|drugstore|medicine|flu|pain|feel|yoga|gym|appointment|help|emergency|bandage|pressure|vet'),
 ('Trabalho e estudo', 'Consigo falar de trabalho e estudo e fazer pedidos simples no escritório ou na escola.', r'work|job|office|class|school|teacher|study|homework|coworker|meeting|email|call|print|library|enroll|volunteer|interview|team|boss|test|project|badge|business|supplies|college|english class'),
 ('Lazer, festas e eventos', 'Consigo convidar, aceitar ou recusar e falar de passatempos e eventos.', r'party|movie|music|concert|game|bowling|golf|picnic|photo|halloween|thanksgiving|christmas|year|bowl|wedding|baby|kite|book club|basketball|dance|art|hobby|karaoke|video|dog park|playground|fishing|skate|ice|hiking|valentine|mother|easter|fireworks|trick|block|festival|weekend|plan'),
 ('Tempo, horas e telefone', 'Consigo falar de dias, horas, clima e usar o telefone para recados simples.', r'time|day|week|month|weather|snow|fog|rain|phone|text|message|late|date|calendar|wrong number|cancel|forecast|color|wear|repeat|sorry|excuse|elevator|small talk'),
]
TIER = [
 (100, 'A1.1', 'be, have, can, would like/I’d like, there is/are, imperativos, presente simples (like, want, need), presente contínuo básico, going to simples'),
 (150, 'A1.2', 'tudo do bloco anterior + can/could para pedir, should, advérbios de frequência, preposições de lugar e tempo, some/any'),
 (210, 'A1.3', 'tudo do bloco anterior + must/mustn’t, I’ll (decidir na hora), going to, perguntas com how long/how far/how much'),
 (220, 'A1.4', 'passado simples (was/were, regulares e irregulares comuns, did/didn’t) — plano 211–220'),
 (230, 'A1.4', 'tempo e deslocamento: how long/how far, at/in/on, next/last, ago — plano 221–230'),
 (240, 'A1.5', 'comparação e preferência: comparativos, superlativos, prefer/I’d rather, frequência — plano 231–240'),
 (999, 'A1.5', 'regras e conselho: have to/don’t have to, must/can’t, should, too/enough, there is/are — plano 241–250'),
]
def dom(txt):
    for name, cd, rx in DOM:
        if re.search(rx, txt.lower()): return name, cd
    return DOM[0][0], DOM[0][1]
def tier(n):
    for lim, t, d in TIER:
        if n <= lim: return t, d
DONE_OWN = {1008, 1009, 1010}
def main():
    rows = json.load(open('/tmp/orig_focus.json')) if os.path.exists('/tmp/orig_focus.json') else []
    cur = {x['n']: x for x in json.load(open(os.path.join(ROOT, 'data/v4/curriculum.json')))}
    fixed = {1001: 244, 1002: 349, 1003: 369, 1004: 303, 1005: 326, 1006: 330, 1007: 233}
    MAN = {8: 339, 9: 373, 10: 370, 11: 343, 12: 304, 13: 345, 14: 381, 15: 329, 16: 403, 17: 331, 18: 342, 19: 286, 20: 325, 21: 216, 22: 334, 23: 223, 24: 347, 25: 366, 26: 361, 27: 285, 28: 310, 29: 424, 30: 365, 31: 364, 32: 355, 33: 367, 34: 375, 35: 302, 36: 362, 37: 387}
    fixed.update({1000 + k: v for k, v in MAN.items()})
    used = {B.nb_index(n) for n in range(1, 249)} | set(fixed.values())
    free = [i for i in range(1, len(B.NB) + 1) if i not in used]
    fdom = {i: dom(B.NB[i - 1]['t'])[0] for i in free}
    plan = []; taken = set(fixed.values())
    for n in range(1, 249):
        t = cur[n]['title']; anchor = next((f for a, b, f in rows if a == n), '')
        d, cd = dom(t); tr, ceil = tier(n)
        nb = fixed.get(1000 + n)
        if nb is None:
            c = [i for i in free if i not in taken and fdom[i] == d] or [i for i in free if i not in taken]
            nb = c[(n * 7) % len(c)] if c else None
        if nb: taken.add(nb)
        rev = 'feita (diálogo do Neighbors)' if (1000 + n) in range(1001, 1008) else ('feita (diálogo próprio)' if (1000 + n) in DONE_OWN else 'a fazer: diálogo próprio; tema sugerido')
        plan.append(dict(n=n, cont=1000 + n, original=t, domain=d, cando=cd, level=tr, ceiling=ceil, anchor=anchor, nb=nb, nb_title=B.NB[nb - 1]['t'] if nb else '', status=rev))
    json.dump(plan, open(os.path.join(ROOT, 'data/plano-continuacoes.json'), 'w'), ensure_ascii=False, indent=1)
    md = ['# Plano das continuações (aulas 1001–1248)', '', '**Meta: 500 aulas de nível A1** (248 originais + 252 continuações: as 248 do mapa + 4 aulas extras de revisão a definir). **Daqui para a frente as continuações não usam mais o Neighbors**: o diálogo de cada uma é escrito para a aula.', '', 'Cada continuação respeita três regras: (1) **estrutura**: nunca acima do teto do bloco da aula original; (2) **CEFR A1**: cobre um descritor “Consigo…” do domínio indicado; (3) **vocabulário**: palavras e verbos novos, conferidos pelo registro (`tools/vocab_registry.py`).', '', '## Tetos gramaticais por bloco', '']
    for lim, t, dd in TIER: md.append('- até a aula %s (%s): %s' % (lim if lim < 999 else 248, t, dd))
    md += ['', '## Mapa', '', '| Original | Continuação | Domínio CEFR A1 | Estrutura-âncora da original | Tema sugerido (ideia, não obrigatório) | Status |', '|---|---|---|---|---|---|']
    for p in plan: md.append('| %d %s | %d | %s | %s | %s | %s |' % (p['n'], p['original'], p['cont'], p['domain'], p['anchor'] or '—', p['nb_title'] or '—', p['status']))
    open(os.path.join(ROOT, '..', 'docs', 'PLANO_CONTINUACOES.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
    print(len(plan), 'linhas;', sum(1 for p in plan if not p['nb']), 'sem nb')
main()
