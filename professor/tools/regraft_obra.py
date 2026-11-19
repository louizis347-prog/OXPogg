#!/usr/bin/env python3
"""Troca a obra ("Cena da obra") de aulas JÁ PUBLICADAS sem mexer no resto da aula.
Fluxo: src/obras.json já tem a obra nova da aula N → reconstrói a aula (build_v5 + enrich_v6) → copia só as páginas
'work' e 'story' e os campos 'sticker' e 'unit' para a aula atual (guardada antes) → atualiza o índice do currículo →
reaplica nomes (correção de vocativos, diversify_learner, diversify_partner).
Uso: python3 tools/regraft_obra.py N [N ...]        (rode de dentro de professor/)"""
import glob, json, os, re, subprocess, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')); V4 = os.path.join(ROOT, 'data', 'v4')
sys.path.insert(0, os.path.join(ROOT, 'src'))

def path(n): return os.path.join(V4, ('%03d' % n) if n < 1000 else str(n)) + '.json'

def rename_pages(cur, n):
    """As páginas recém-construídas trazem os nomes originais do plano; aplica os nomes registrados para a aula (aprendiz e parceiro)."""
    reg_l = json.load(open(os.path.join(ROOT, 'data', 'learner_names.json'))) if os.path.exists(os.path.join(ROOT, 'data', 'learner_names.json')) else {}
    reg_p = json.load(open(os.path.join(ROOT, 'data', 'partner_names.json'))) if os.path.exists(os.path.join(ROOT, 'data', 'partner_names.json')) else {}
    L = reg_l.get(str(n)); pr = reg_p.get(str(n)); names = ['Mia']
    if n >= 4000:
        ns_ = {}; exec(open(os.path.join(ROOT, 'tools', 'plan_b2.py'), encoding='utf-8').read(), ns_)
        if 0 <= n - 4001 < len(ns_['P']): names.append(ns_['P'][n - 4001][3])
    for kind in ('work', 'story'):
        for i, pg in enumerate(cur['pages']):
            if pg['kind'] != kind: continue
            t = json.dumps(pg, ensure_ascii=False)
            if L:
                for nm in names: t = re.sub(r'(?<!Mamma )\b%s\b' % re.escape(nm), L, t)
            if pr and pr['old'] != pr['new']: t = re.sub(r'\b%s\b' % re.escape(pr['old']), pr['new'], t)
            cur['pages'][i] = json.loads(t)
    return cur

def main(ns):
    if not ns: sys.exit('informe os números das aulas')
    done = []; saved = {}
    for n in ns:
        p = path(n); keep = open(p, encoding='utf-8').read()
        try:
            subprocess.run([sys.executable, 'src/build_v5.py', str(n)], cwd=ROOT, check=True, capture_output=True)
            subprocess.run([sys.executable, 'tools/enrich_v6.py'], cwd=ROOT, check=True, capture_output=True)
            new = json.load(open(p, encoding='utf-8'))
        finally:
            open(p, 'w', encoding='utf-8').write(keep)
        cur = json.loads(keep)
        for kind in ('work', 'story'):
            ni = [i for i, x in enumerate(new['pages']) if x['kind'] == kind]; ci = [i for i, x in enumerate(cur['pages']) if x['kind'] == kind]
            if len(ni) == 1 and len(ci) == 1: cur['pages'][ci[0]] = new['pages'][ni[0]]
            else: print('aula', n, 'sem', kind, 'único: pulada'); break
        else:
            for k in ('sticker', 'unit'):
                if k in new: cur[k] = new[k]
            cur = rename_pages(cur, n)
            saved[n] = cur['pages']
            json.dump(cur, open(p, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':')); done.append(n)
    cp = os.path.join(V4, 'curriculum.json'); idx = json.load(open(cp, encoding='utf-8'))
    for x in idx:
        if x['n'] in done:
            x['unit'] = json.load(open(path(x['n']), encoding='utf-8'))['unit']
    json.dump(idx, open(cp, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    import dialog_rewrite as D
    for n in done:
        d = json.load(open(path(n), encoding='utf-8')); D.fix_names_lesson(d); json.dump(d, open(path(n), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    args = [str(n) for n in done]
    subprocess.run([sys.executable, 'tools/apply_live.py'] + args, cwd=ROOT, check=True, capture_output=True)
    for n in done:  # apply_live reescreve o roteiro de todas as páginas; mantém as originais exceto a obra
        d = json.load(open(path(n), encoding='utf-8'))
        for i, pg in enumerate(d['pages']):
            if pg['kind'] not in ('work', 'story'): d['pages'][i] = saved[n][i]
        json.dump(d, open(path(n), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    for tool in ('diversify_learner.py', 'diversify_partner.py'):
        subprocess.run([sys.executable, 'tools/' + tool] + args, cwd=ROOT, check=True)
    print('obras trocadas em', len(done), 'aulas')

if __name__ == '__main__':
    main([int(a) for a in sys.argv[1:]])
