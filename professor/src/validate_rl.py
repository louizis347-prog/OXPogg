#!/usr/bin/env python3
"""Valida as aulas Real-Life (professor/data/v3/NNN.json).
Uso: python3 src/validate_rl.py 3 [5 6 ...]      (números das aulas)
     python3 src/validate_rl.py --all             (todas as aulas existentes + unicidade entre aulas)
Sai com código 1 se houver erro."""
import glob, json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
ELENCO = {p['name'] for p in json.load(open(os.path.join(ROOT, 'data', 'elenco.json'), encoding='utf-8'))}
try:
    SCENES = set(subprocess.run(['node', '-e', "global.window={};require('../js/obra-ficha-lib.js');require('../js/obra-ficha.js');require('../js/obra-ficha-scenes2.js');console.log(window.PogFicha.VOCAB.scene.join(' '))"], capture_output=True, text=True, cwd=HERE).stdout.split())
except Exception:
    SCENES = set()
SOLO = ['rl_open', 'rl_warm', 'rl_culture', 'rl_listen', 'rl_dialog', 'rl_chunks', 'rl_patterns', 'rl_pron', 'rl_challenge', 'rl_role', 'rl_write', 'rl_feedback', 'rl_exit', 'rl_levels']
GROUP = ['rl_open', 'rl_warm', 'rl_culture', 'rl_listen', 'rl_dialog', 'rl_chunks', 'rl_patterns', 'rl_pron', 'rl_challenge', 'rl_lab', 'rl_mission', 'rl_write', 'rl_feedback', 'rl_exit', 'rl_levels']
STAGES_SOLO = ['warm', 'immersion', 'notice', 'gram', 'practice', 'speak1', 'write', 'exit']
STAGES_GROUP = ['warm', 'immersion', 'notice', 'gram', 'speak1', 'speak2', 'write', 'exit']
PT_CH = re.compile(r'[ãõçáéíóúâêôàü]', re.I)
BAD = re.compile(r'\bTODO\b|(?i:\b(lorem|xxx|placeholder|tbd)\b)')


def wc(s): return len(re.findall(r"[A-Za-z’']+", s))


def check(L, curriculum):
    er = []
    def E(m): er.append(m)
    n = L.get('n')
    for k in ('n', 'level', 'topic', 'title', 'pt', 'unit', 'minutes', 'cast', 'scene', 'plan', 'dialog', 'pages'):
        if k not in L: E('falta o campo %s' % k)
    if er: return er
    c = curriculum.get(n)
    if c:
        if L.get('topic') != c['title']: E('topic precisa ser o título do currículo (%r)' % c['title'])
        if L['unit'].get('n') != c['unit']['n'] or L['unit'].get('k') != c['unit']['k']: E('unidade/posição difere do currículo')
    if L['minutes'] != 60: E('minutes precisa ser 60')
    if SCENES and L['scene'] not in SCENES: E('cena inválida %r' % L['scene'])
    for nm in L['cast']:
        if nm not in ELENCO: E('personagem %r não existe em data/elenco.json' % nm)
    for mode, ids in (('solo', STAGES_SOLO), ('group', STAGES_GROUP)):
        pl = L['plan'].get(mode, [])
        if [s['id'] for s in pl] != ids: E('plan.%s precisa ter os estágios %s' % (mode, ids))
        if sum(s.get('min', 0) for s in pl) != 60: E('plan.%s precisa somar 60 minutos' % mode)
    d = L['dialog']; sp = d.get('speakers', {})
    if len(sp) != 2: E('dialog.speakers precisa ter 2 papéis')
    for r, v in sp.items():
        if v.get('name') not in ELENCO: E('speaker %s: %r não está em elenco.json' % (r, v.get('name')))
    lines = d.get('lines', [])
    if not 8 <= len(lines) <= 12: E('dialog precisa ter 8–12 falas (tem %d)' % len(lines))
    marked = 0
    lvl_max = 14 if L['level'].startswith('A1') else 20
    for i, l in enumerate(lines):
        if l.get('who') not in sp: E('fala %d: who %r não está em speakers' % (i + 1, l.get('who')))
        if not l.get('en') or not l.get('pt'): E('fala %d: falta en/pt' % (i + 1))
        if PT_CH.search(l.get('en', '')): E('fala %d: caracteres de português no inglês' % (i + 1))
        if '**' in l.get('en', ''): marked += 1
        if wc(l.get('en', '')) > lvl_max + 6: E('fala %d: longa demais para o nível (%d palavras)' % (i + 1, wc(l['en'])))
    if marked < 4: E('dialog precisa destacar chunks com **…** em ≥4 falas')
    pages = L['pages']
    types_known = set(SOLO + GROUP)
    for i, p in enumerate(pages):
        if p.get('t') not in types_known: E('página %d: tipo desconhecido %r' % (i + 1, p.get('t')))
        if p.get('for') not in (None, 'solo', 'group'): E('página %d: for inválido' % (i + 1))
    for mode, need, ids in (('solo', SOLO, STAGES_SOLO), ('group', GROUP, STAGES_GROUP)):
        seq = [p['t'] for p in pages if p.get('for') in (None, mode)]
        if seq != need: E('ordem das páginas no modo %s deveria ser %s (é %s)' % (mode, need, seq))
        for p in pages:
            if p.get('for') in (None, mode):
                st = p.get('stage'); st = st.get(mode) if isinstance(st, dict) else st
                if st not in ids: E('página %s: stage inválido no modo %s (%r)' % (p['t'], mode, st))
    P = {p['t']: p for p in pages}
    # ---- conteúdo por tipo ----
    o = P.get('rl_open', {})
    if len(o.get('situation', {}).get('text', '')) < 40: E('rl_open: situation.text curto')
    if not 3 <= len(o.get('canDo', [])) <= 5: E('rl_open: canDo precisa ter 3–5 itens')
    if len(o.get('success', [])) < 3: E('rl_open: success precisa ter ≥3')
    if not o.get('think') or not o.get('goal'): E('rl_open: faltam goal/think')
    if len(o.get('unit', {}).get('map', [])) != L['unit'].get('of'): E('rl_open: unit.map precisa listar as %s aulas da unidade' % L['unit'].get('of'))
    w = P.get('rl_warm', {})
    if not 3 <= len(w.get('qs', [])) <= 5 or any(len(q.get('sup', [])) < 2 or not q.get('pt') for q in w.get('qs', [])): E('rl_warm: 3–5 perguntas, cada uma com pt e ≥2 respostas de apoio (sup)')
    if not w.get('recall') or not w.get('intro', {}).get('solo') or not w.get('intro', {}).get('group'): E('rl_warm: faltam recall/intro.solo/intro.group')
    cu = P.get('rl_culture', {})
    if len(cu.get('cards', [])) < 3 or any(not c.get('vis') or not c.get('pt') for c in cu.get('cards', [])): E('rl_culture: ≥3 cartões com vis e pt')
    if len(cu.get('qs', [])) != 3 or any(set(q.get('levels', {})) != {'A1', 'A2', 'B1', 'B2'} for q in cu.get('qs', [])): E('rl_culture: 3 perguntas com respostas-modelo A1, A2, B1 e B2')
    if not cu.get('compare'): E('rl_culture: falta compare (comparação com o Brasil)')
    li = P.get('rl_listen', {})
    p1 = li.get('pass1', {})
    if len(p1.get('opts', [])) != 3 or not isinstance(p1.get('ans'), int) or not 0 <= p1.get('ans', -1) < 3: E('rl_listen.pass1: 3 opções e ans válido')
    t2 = li.get('pass2', {}).get('tasks', [])
    if not 3 <= len(t2) <= 5 or any(not t.get('label') or not t.get('ans') for t in t2): E('rl_listen.pass2: 3–5 tarefas com label e ans')
    for t in t2:
        if t.get('ans') and t['ans'].lower() not in ' '.join(l.get('en', '').replace('**', '') for l in lines).lower(): E('rl_listen.pass2: resposta %r não aparece no diálogo' % t['ans'])
    dg = P.get('rl_dialog', {})
    if len(dg.get('qs', [])) < 4 or any(len(q.get('opts', [])) != 3 or not 0 <= q.get('ans', -1) < 3 for q in dg.get('qs', [])): E('rl_dialog: ≥4 perguntas com 3 opções e ans válido')
    if len(dg.get('retell', {}).get('starters', [])) < 3: E('rl_dialog.retell: ≥3 starters')
    ch = P.get('rl_chunks', {}); its = ch.get('items', [])
    if not 5 <= len(its) <= 8: E('rl_chunks: 5–8 expressões (tem %d)' % len(its))
    pri = [x for x in its if x.get('pri')]
    if not 3 <= len(pri) <= 5: E('rl_chunks: 3–5 prioridades (pri) — regra: poucas expressões usadas com naturalidade')
    for x in its:
        if not x.get('en') or not x.get('pt') or not x.get('use'): E('rl_chunks: item sem en/pt/use')
        if PT_CH.search(x.get('en', '')): E('rl_chunks: português no inglês em %r' % x.get('en'))
    dc = ch.get('discover', {})
    if len(dc.get('items', [])) < 4 or any(i.get('fn') not in dc.get('fns', []) for i in dc.get('items', [])): E('rl_chunks.discover: ≥4 itens com fn dentro de fns')
    pa = P.get('rl_patterns', {}); pt_ = pa.get('patterns', [])
    if not 2 <= len(pt_) <= 4 or sum(1 for x in pt_ if x.get('main')) < 2: E('rl_patterns: 2–4 padrões, ≥2 principais (main)')
    for x in pt_:
        if len(x.get('ex', [])) < 2 or '**' not in x.get('formula', ''): E('rl_patterns: padrão %r precisa de ≥2 exemplos e fórmula com **destaque**' % x.get('name'))
    sw = pa.get('swap', {})
    ph = set(re.findall(r'\{(\w+)\}', sw.get('frame', '')))
    ks = {s.get('k') for s in sw.get('slots', [])}
    if len(ks) < 2 or ph != ks: E('rl_patterns.swap: frame precisa ter {k} igual aos slots (≥2 slots)')
    if set(re.findall(r'\{(\w+)\}', sw.get('tpt', ''))) != ks: E('rl_patterns.swap: tpt precisa usar os mesmos {k}')
    for s in sw.get('slots', []):
        if len(s.get('opts', [])) < 3 or any(not (o.get('en') and o.get('pt')) for o in s.get('opts', [])): E('rl_patterns.swap: slot %r com ≥3 opções en+pt' % s.get('k'))
    if len(pa.get('register', {}).get('rows', [])) < 3: E('rl_patterns.register: ≥3 linhas spoken × written')
    pr = P.get('rl_pron', {})
    if len(pr.get('items', [])) < 2 or any(not set(i.get('rhythm', 'oO')) <= set('oO') or not i.get('say') for i in pr.get('items', [])): E('rl_pron: ≥2 itens com say e rhythm só de o/O')
    if len(pr.get('identify', [])) < 2 or any(not 0 <= q.get('ans', -1) < len(q.get('opts', [])) for q in pr.get('identify', [])): E('rl_pron.identify: ≥2 com ans válido')
    if not pr.get('focus') or not pr.get('tip') or not pr.get('own', {}).get('prompt'): E('rl_pron: faltam focus/tip/own.prompt')
    cg = P.get('rl_challenge', {}); tot = 0
    for lv in cg.get('levels', []):
        for it in lv.get('items', []):
            tot += 1; ty = it.get('type', 'mcq')
            if ty in ('mcq', 'reply'):
                if len(it.get('opts', [])) != 3 or not 0 <= it.get('ans', -1) < 3: E('rl_challenge: mcq/reply com 3 opções e ans válido')
                if len(set(it.get('opts', []))) != len(it.get('opts', [])): E('rl_challenge: opções repetidas')
            elif ty == 'gap':
                if '___' not in it.get('text', '') or not it.get('ans'): E('rl_challenge: gap precisa de ___ e ans')
            elif ty == 'swap':
                if not it.get('instr') or not it.get('from') or not it.get('ans') or not it.get('model'): E('rl_challenge: swap precisa de instr/from/ans/model')
            else: E('rl_challenge: tipo %r desconhecido' % ty)
            if not it.get('why'): E('rl_challenge: item sem why')
    if not 8 <= tot <= 10 or len(cg.get('levels', [])) != 2: E('rl_challenge: 2 níveis (controlled, guided) e 8–10 itens (tem %d)' % tot)
    ro = P.get('rl_role', {})
    if len(ro.get('orders', [])) < 3 or len(ro.get('complications', [])) < 3 or len(ro.get('rounds', [])) != 3 or len(ro.get('success', [])) < 3: E('rl_role: ≥3 orders, ≥3 complications, 3 rounds, ≥3 success')
    if not ro.get('brief', {}).get('teacher') or not ro.get('brief', {}).get('student'): E('rl_role: falta brief.teacher/student')
    lb = P.get('rl_lab', {})
    if len(lb.get('rounds', [])) < 4: E('rl_lab: ≥4 rodadas')
    ig = lb.get('infogap', {})
    ra, rb = ig.get('a', {}).get('rows', []), ig.get('b', {}).get('rows', [])
    if len(ra) < 3 or len(ra) != len(rb) or any(bool(x.get('v')) == bool(y.get('v')) for x, y in zip(ra, rb)): E('rl_lab.infogap: A e B com ≥3 linhas COMPLEMENTARES (onde A sabe, B não sabe)')
    mi = P.get('rl_mission', {})
    if len(mi.get('missions', [])) < 3 or len(mi.get('success', [])) < 3 or any(not m.get('mission') or not m.get('constraint') or not m.get('start') for m in mi.get('missions', [])): E('rl_mission: ≥3 missões com mission/constraint/start e ≥3 success')
    wr = P.get('rl_write', {})
    if not wr.get('task') or len(wr.get('model', '')) < 40 or len(wr.get('steps', [])) < 3 or len(wr.get('checklist', [])) < 3: E('rl_write: task, model (≥40 chars), ≥3 steps e ≥3 checklist')
    fb = P.get('rl_feedback', {})
    if [c.get('k') for c in fb.get('criteria', [])] != ['flu', 'lan', 'pro', 'int'] or len(fb.get('interpret', [])) < 3: E('rl_feedback: critérios flu/lan/pro/int e ≥3 interpretações')
    if set(fb.get('prompts', {})) != {'well', 'improve', 'next'}: E('rl_feedback: prompts well/improve/next')
    ex = P.get('rl_exit', {})
    if len(ex.get('tasks', [])) != 3 or any(not t.get('model') for t in ex.get('tasks', [])): E('rl_exit: 3 tarefas com model')
    if len(ex.get('homework', {}).get('items', [])) != 4: E('rl_exit: homework com 4 itens')
    if set(ex.get('spaced', {})) != {'next', 'week', 'unit'}: E('rl_exit.spaced: next/week/unit')
    lv = P.get('rl_levels', {})
    if [r.get('lv') for r in lv.get('ladder', [])] != ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'] or lv.get('you') not in ('A1', 'A2', 'B1', 'B2', 'C1', 'C2'): E('rl_levels: ladder A1..C2 e you')
    # ---- roteiro do professor ----
    tp = [p for p in pages if p.get('teach')]
    if len(tp) < 12: E('teach: ≥12 páginas com roteiro do professor (tem %d)' % len(tp))
    for p in tp:
        if not p['teach'].get('goal'): E('teach de %s sem goal' % p['t'])
    if sum(1 for p in pages if p.get('teach', {}).get('errors')) < 6: E('teach: ≥6 páginas com "errors" (correções frequentes)')
    if sum(1 for p in pages if p.get('teach', {}).get('support')) < 6: E('teach: ≥6 páginas com "support"')
    if sum(1 for p in pages if p.get('teach', {}).get('extra')) < 8: E('teach: ≥8 páginas com perguntas "extra"')
    for p in pages:
        for e in p.get('teach', {}).get('errors', []):
            if not e.get('w') or not e.get('r'): E('teach.errors com w/r vazios em %s' % p['t'])
    # ---- texto ----
    raw = json.dumps(L, ensure_ascii=False)
    if BAD.search(raw): E('há texto de placeholder (TODO/lorem/xxx)')
    return er


def main():
    a = sys.argv[1:]
    cur = {c['n']: c for c in json.load(open(os.path.join(ROOT, 'data', 'v3', 'curriculum.json'), encoding='utf-8'))} if os.path.exists(os.path.join(ROOT, 'data', 'v3', 'curriculum.json')) else {}
    if '--all' in a:
        files = sorted(glob.glob(os.path.join(ROOT, 'data', 'v3', '[0-9][0-9][0-9].json')))
    else:
        files = [os.path.join(ROOT, 'data', 'v3', '%03d.json' % int(x)) for x in a]
    bad = 0; lessons = []
    for f in files:
        try: L = json.load(open(f, encoding='utf-8'))
        except Exception as e:
            print('ERRO %s: JSON inválido (%s)' % (os.path.basename(f), e)); bad += 1; continue
        lessons.append(L)
        for m in check(L, cur):
            print('ERRO aula %s: %s' % (L.get('n', os.path.basename(f)), m)); bad += 1
    if '--all' in a:
        seen = {}
        for L in lessons:
            for key, val in (('título', L['title']), ('1ª fala', L['dialog']['lines'][0]['en'] if L['dialog']['lines'] else '')):
                if val in seen.get(key, {}): print('ERRO aula %s: %s repetido com a aula %s' % (L['n'], key, seen[key][val])); bad += 1
                seen.setdefault(key, {})[val] = L['n']
            for p in L['pages']:
                if p['t'] == 'rl_chunks':
                    for it in p['items']:
                        if it.get('pri'):
                            k = re.sub(r'[^a-z ]', '', it['en'].lower())
                            if k in seen.setdefault('pri', {}) and seen['pri'][k] != L['n']: print('AVISO aula %s: expressão prioritária %r já era prioridade na aula %s' % (L['n'], it['en'], seen['pri'][k]))
                            seen['pri'].setdefault(k, L['n'])
    print('aulas: %d | erros: %d' % (len(files), bad))
    return 1 if bad else 0


sys.exit(main())
