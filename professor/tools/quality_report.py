#!/usr/bin/env python3
"""Relatório automático de qualidade por aula (fila de revisão).
Mede, por aula do Painel do Professor (A1/A2/B1/B2): falas curtas, falas repetidas entre aulas, densidade da
estrutura-alvo, vocabulário ensinado, ligação da obra cultural com o tema. NÃO substitui revisão humana.
Uso: python3 tools/quality_report.py   (gera docs/QUALIDADE_AULAS.md e docs/qualidade_aulas.csv)"""
import json, re, glob, os, collections, csv
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
V4 = os.path.join(ROOT, 'data', 'v4'); DOCS = os.path.join(ROOT, '..', 'docs')
STOP = set("a an the of to in on at for and or but is are was were be been being it this that these those with from as by about into over after before you your i we they he she my our their his her me us them do does did have has had will would can could should may might not no yes so if then than there here what who where when why how which".split())
def level(n): return 'B2' if n >= 4000 else 'B1' if n >= 3000 else 'A2' if n >= 2000 else 'A1'
def words(s): return [w for w in re.findall(r"[a-z']+", s.lower().replace('’', "'")) if w not in STOP and len(w) > 2]
lessons = {}
for f in glob.glob(os.path.join(V4, '[0-9]*.json')):
    n = int(re.search(r'(\d+)\.json', f).group(1))
    try: d = json.load(open(f, encoding='utf-8'))
    except Exception: continue
    lessons[n] = d
cur = {x['n'] for x in json.load(open(os.path.join(V4, 'curriculum.json')))}
lessons = {n: d for n, d in lessons.items() if n in cur}
# falas repetidas entre aulas
cnt = collections.Counter()
for n, d in lessons.items():
    for l in d['dialog']['lines']: cnt[re.sub(r'\W+', ' ', l['en'].lower()).strip()] += 1
rows = []
for n, d in sorted(lessons.items()):
    L = [l['en'] for l in d['dialog']['lines']]
    nw = [len(x.split()) for x in L]
    short = sum(1 for k in nw if k <= 4)
    rep = sum(1 for x in L if cnt[re.sub(r'\W+', ' ', x.lower()).strip()] > 1)
    # densidade da estrutura-alvo: palavras-chave do foco (parte em inglês do 'pt' após "Foco da aula:")
    focus = d.get('pt', '')
    key = [w for w in words(re.sub(r'\(.*?\)', ' ', focus)) if w.isascii()]
    key = [w for w in key if w not in {'foco', 'aula', 'passado', 'presente', 'simples', 'perguntas', 'verbo', 'com'}]
    dens = (sum(1 for x in L if any(k in x.lower() for k in key[:4])) / len(L)) if key and L else 0
    # obra: ligação com o tema (sobreposição lexical entre nota e título/diálogo)
    obra = next((p['work'] for p in d['pages'] if p['kind'] == 'work'), None)
    link = 0.0
    if obra:
        nota = set(words(obra.get('d', '') + ' ' + obra.get('title', '')))
        tema = set(words(d['title'] + ' ' + ' '.join(L)))
        link = len(nota & tema) / max(1, len(nota))
    score = 0
    score += 2 if sum(nw) / max(1, len(nw)) < {'A1': 5, 'A2': 7, 'B1': 9, 'B2': 12}[level(n)] else 0
    score += 1 if short >= 3 else 0
    score += 2 if rep >= 3 else 0
    score += 2 if dens >= 0.85 else 0
    score += 1 if link < 0.05 else 0
    rows.append(dict(n=n, nivel=level(n), titulo=d['title'], falas=len(L), media_palavras=round(sum(nw) / max(1, len(nw)), 1),
                     falas_curtas=short, falas_repetidas=rep, densidade_alvo=round(dens, 2), ligacao_obra=round(link, 2), pontos=score))
os.makedirs(DOCS, exist_ok=True)
with open(os.path.join(DOCS, 'qualidade_aulas.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
out = ['# Qualidade automática das aulas (fila de revisão)', '',
       'Gerado por `professor/tools/quality_report.py`. Os pontos somam alertas (mais pontos = aula que merece reescrita ou revisão primeiro): '
       'média de palavras por fala abaixo do esperado do nível (2), 3+ falas curtas (1), 3+ falas repetidas de outras aulas (2), '
       'estrutura-alvo em ≥85% das falas (2), obra com pouca ligação ao tema (1). **É um filtro automático; não substitui revisão humana.**', '']
by = collections.defaultdict(list)
for r in rows: by[r['nivel']].append(r)
out.append('## Resumo por nível'); out.append('')
out.append('| Nível | Aulas | Média de palavras/fala | Aulas com ≥3 pontos | Aulas com ≥5 pontos |'); out.append('|---|---|---|---|---|')
for lv in ('A1', 'A2', 'B1', 'B2'):
    R = by.get(lv, [])
    if not R: continue
    out.append('| %s | %d | %.1f | %d (%.0f%%) | %d |' % (lv, len(R), sum(r['media_palavras'] for r in R) / len(R), sum(1 for r in R if r['pontos'] >= 3), 100 * sum(1 for r in R if r['pontos'] >= 3) / len(R), sum(1 for r in R if r['pontos'] >= 5)))
for lv in ('A1', 'A2', 'B1', 'B2'):
    R = sorted(by.get(lv, []), key=lambda r: (-r['pontos'], r['media_palavras']))[:15]
    if not R: continue
    out += ['', '## %s — 15 aulas para rever primeiro' % lv, '', '| Aula | Título | Pontos | Palavras/fala | Curtas | Repetidas | Densidade alvo | Ligação obra |', '|---|---|---|---|---|---|---|---|']
    for r in R: out.append('| %d | %s | %d | %s | %d | %d | %s | %s |' % (r['n'], r['titulo'].replace('|', '/'), r['pontos'], r['media_palavras'], r['falas_curtas'], r['falas_repetidas'], r['densidade_alvo'], r['ligacao_obra']))
open(os.path.join(DOCS, 'QUALIDADE_AULAS.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(rows), 'aulas medidas')
