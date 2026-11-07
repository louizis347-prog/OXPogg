"""Une os resultados dos agentes (exemplos de expressões e prática extra por aula) nos dados do curso.
Uso: python3 merge_extras.py <pasta com out/>"""
import glob, json, os, re, sys
OUT = sys.argv[1]
DATA = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'livro')

def norm(k):
    return re.sub(r'\s+', ' ', k.replace('**', '').strip().lower())

# 1) exemplos de expressões
expr = {}
bad = 0
for f in sorted(glob.glob(os.path.join(OUT, 'expr_*_part_*.json'))):
    try:
        d = json.load(open(f))
    except Exception as e:
        print('JSON inválido', f, e); bad += 1; continue
    for k, v in d.items():
        if not isinstance(v, dict) or not v.get('ex') or not v.get('pt'):
            bad += 1; continue
        expr[norm(k)] = dict(ex=v['ex'].strip(), pt=v['pt'].strip(), reg=v.get('reg', 'neutro'), tip=(v.get('tip') or '').strip())
if expr:
    json.dump(expr, open(os.path.join(DATA, 'expr_ex.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
print('expressões com exemplo:', len(expr), '| ignoradas:', bad)

# 2) prática extra e armadilha por aula
os.makedirs(os.path.join(DATA, 'extra'), exist_ok=True)
n = 0
miss = []
for f in sorted(glob.glob(os.path.join(OUT, 'lessons_*_part_*.json'))):
    try:
        d = json.load(open(f))
    except Exception as e:
        print('JSON inválido', f, e); continue
    for lid, v in d.items():
        ok = isinstance(v, dict) and v.get('trap') and len(v.get('mcq', [])) >= 3 and len(v.get('fix', [])) >= 2 and len(v.get('rewrite', [])) >= 2
        for q in v.get('mcq', []) if isinstance(v, dict) else []:
            if not (isinstance(q.get('opts'), list) and isinstance(q.get('ans'), int) and 0 <= q['ans'] < len(q['opts'])):
                ok = False
        if not ok:
            miss.append(lid); continue
        json.dump(v, open(os.path.join(DATA, 'extra', lid + '.json'), 'w'), ensure_ascii=False, indent=0)
        n += 1
print('aulas com extra:', n, '| rejeitadas:', len(miss), miss[:10])
