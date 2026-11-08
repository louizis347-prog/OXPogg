"""Converte grafia britânica -> americana nos dados e fontes do livro.
Pula textos que comparam as variantes (britânico/UK/AmE...). Uso: python3 us_spelling.py [--dry]"""
import glob, json, os, re, sys, collections
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
DRY = '--dry' in sys.argv
DATA_ONLY = '--data-only' in sys.argv
OUR = 'neighb|col|favo|hono|behavi|hum|lab|flav|harb|rum|sav|rig|vap|od|endeav'
RULES = [
    (r'\b(' + OUR + r')our(s|ed|ing|ful|less|able|ite|ites|hood|ly|ist|ists)?\b', lambda m: m.group(1) + 'or' + (m.group(2) or '')),
    (r'\b(cent|fib|lit|met|kilomet|millimet|centimet|calib|sombr|theat|spectr)re(s|d)?\b', lambda m: m.group(1) + 'er' + (m.group(2) or '')),
    (r'\b(organi|reali|recogni|apologi|critici|emphasi|summari|speciali|memori|minimi|maximi|prioriti|familiari|customi|utili|generali|visuali|authori|categori|characteri|moderni|sociali|civili|capitali|finali|real|digiti|standardi|stabili|energi|mobili|normali|personali|publici|criminali|legali|equali|initiali|jeopardi|sympathi|patroni|terrori|hospitali|globali|commercialı|colonı|fertili|harmoni|idoli|itemi|lobbi|localı|neutrali|penali|pasteuri|popuları|polari|sanitı|scrutini|subsidi|tantali|tenderi|traumati|vandali|vaporı|westerni)(?:se|sed|ses|sing|sation|sations|ser|sers)\b', None),
]
# regra -ise/-yse feita por lista explícita (evita falsos positivos como "promise", "exercise", "advise")
ISE = 'organ recogn apolog critic emphas summar special memor minim maxim priorit familiar custom util general visual author categor character modern social civil capital standard stabil mobil normal personal public legal equal initial sympath hospital global'.split()
ISE += ['real']
YSE = ['analy', 'paraly', 'catalyse']
EXACT = {'grey': 'gray', 'greys': 'grays', 'greyish': 'grayish', 'programme': 'program', 'programmes': 'programs', 'defence': 'defense', 'offence': 'offense',
         'pretence': 'pretense', 'pyjamas': 'pajamas', 'tyre': 'tire', 'tyres': 'tires', 'kerb': 'curb', 'aluminium': 'aluminum', 'learnt': 'learned', 'spelt': 'spelled',
         'burnt': 'burned', 'dreamt': 'dreamed', 'whilst': 'while', 'mum': 'mom', 'mummy': 'mommy', 'maths': 'math', 'behavioural': 'behavioral', 'licence': 'license',
         'travelled': 'traveled', 'travelling': 'traveling', 'traveller': 'traveler', 'travellers': 'travelers', 'cancelled': 'canceled', 'cancelling': 'canceling',
         'labelled': 'labeled', 'labelling': 'labeling', 'modelled': 'modeled', 'modelling': 'modeling', 'levelled': 'leveled', 'counsellor': 'counselor',
         'counsellors': 'counselors', 'jewellery': 'jewelry', 'ageing': 'aging', 'artefact': 'artifact', 'artefacts': 'artifacts', 'sceptical': 'skeptical',
         'sceptic': 'skeptic', 'draught': 'draft', 'plough': 'plow', 'storey': 'story', 'enquiry': 'inquiry', 'enquire': 'inquire', 'fulfil': 'fulfill',
         'instalment': 'installment', 'cosy': 'cozy', 'mould': 'mold', 'smoulder': 'smolder', 'manoeuvre': 'maneuver', 'oestrogen': 'estrogen', 'paediatric': 'pediatric',
         'anaemia': 'anemia', 'diarrhoea': 'diarrhea', 'foetus': 'fetus', 'judgement': 'judgment', 'acknowledgement': 'acknowledgment', 'catalogue': 'catalog',
         'kilometre': 'kilometer', 'kilometres': 'kilometers', 'wellies': 'rain boots'}
for stem in ISE:
    for suf in ('se', 'sed', 'ses', 'sing', 'sation', 'sations', 'ser', 'sers'):
        pass
SKIP = re.compile(r'brit[âa]nic|british|\bUK\b|\bBrE\b|\bAmE\b|reino unido|ingl[êe]s brit|americano|american|inglaterra|england', re.I)
CT = collections.Counter()

def case(src, dst):
    if src.isupper() and len(src) > 1: return dst.upper()
    if src[0].isupper(): return dst[0].upper() + dst[1:]
    return dst

PATS = [(re.compile(RULES[0][0], re.I), lambda m: case(m.group(0), (m.group(1) + 'or' + (m.group(2) or '')).lower())),
        (re.compile(RULES[1][0], re.I), lambda m: case(m.group(0), (m.group(1) + 'er' + (m.group(2) or '')).lower())),
        (re.compile(r'\b(' + '|'.join(ISE) + r')i?(se|sed|ses|sing|sation|sations|ser|sers)\b', re.I), None),
        (re.compile(r'\b(' + '|'.join(YSE[:2]) + r')(se|sed|ses|sing)\b', re.I), None),
        (re.compile(r'\b(' + '|'.join(map(re.escape, EXACT)) + r')\b', re.I), lambda m: case(m.group(0), EXACT[m.group(0).lower()]))]
ISEPAT = re.compile(r'\b(organi|reali|recogni|apologi|critici|emphasi|summari|speciali|memori|minimi|maximi|prioriti|familiari|customi|utili|generali|visuali|authori|categori|characteri|moderni|sociali|civili|capitali|standardi|stabili|mobili|normali|personali|publici|legali|equali|initiali|sympathi|hospitali|globali)(se|sed|ses|sing|sation|sations|ser|sers)\b', re.I)
YSEPAT = re.compile(r'\b(analy|paraly)(se|sed|sing|ser|sers)\b', re.I)
def ise(m): return case(m.group(0), (m.group(1) + {'se': 'ze', 'sed': 'zed', 'ses': 'zes', 'sing': 'zing', 'sation': 'zation', 'sations': 'zations', 'ser': 'zer', 'sers': 'zers'}[m.group(2).lower()]).lower())
def yse(m): return case(m.group(0), (m.group(1) + {'se': 'ze', 'sed': 'zed', 'ses': 'zes', 'sing': 'zing', 'ser': 'zer', 'sers': 'zers'}[m.group(2).lower()]).lower())
ALL = [(PATS[0][0], PATS[0][1]), (PATS[1][0], PATS[1][1]), (ISEPAT, ise), (YSEPAT, yse), (PATS[4][0], PATS[4][1])]

def conv(s, force=False):
    if not force and SKIP.search(s): return s
    o = s
    for p, f in ALL:
        s = p.sub(lambda m: (CT.update([m.group(0).lower()]) or f(m)), s)
    return s

def walk(x, key=False):
    if isinstance(x, str): return conv(x)
    if isinstance(x, list): return [walk(i) for i in x]
    if isinstance(x, dict): return {conv(k, True): walk(v) for k, v in x.items()}
    return x

changed = 0
for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'livro', '**', '*.json'), recursive=True)):
    t = open(f, encoding='utf-8').read()
    d = json.loads(t)
    n = walk(d)
    if n != d:
        changed += 1
        if not DRY:
            ind = 0 if '/extra/' in f else None
            if ind == 0: json.dump(n, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
            else: json.dump(n, open(f, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
pychanged = 0
for f in ([] if DATA_ONLY else sorted(glob.glob(os.path.join(ROOT, 'src', 'livro', '*.py')))) + sorted(glob.glob(os.path.join(ROOT, 'src', 'livro', 'tools', 'gen_sons.py'))):
    L = open(f, encoding='utf-8').read().split('\n')
    N = [conv(l) for l in L]
    if N != L:
        pychanged += 1
        if not DRY: open(f, 'w', encoding='utf-8').write('\n'.join(N))
print('json alterados:', changed, '| py alterados:', pychanged, '| dry' if DRY else '')
print(CT.most_common(40))
