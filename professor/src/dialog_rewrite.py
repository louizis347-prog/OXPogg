"""Reescrita dos diálogos das aulas ao vivo do Painel (data/v4/NNNN.json).
  python3 dialog_rewrite.py select            -> escolhe as aulas ruins e grava src/dialog_work/in/dK.json (pacotes de ~23 aulas)
  python3 dialog_rewrite.py apply [pasta out] -> aplica src/dialog_work/out/dK.json nas aulas (valida antes; rejeita o que não passa)
  python3 dialog_rewrite.py check             -> métricas de diálogo de todas as aulas (repetição de estrutura, falas curtas, nomes)
Atualiza TODOS os lugares onde o diálogo aparece: dialog.lines, telas de conversa (+ trocas de palavras),
telas 'Sua resposta' (opções erradas plausíveis em vez de embaralhadas), frases-chave da capa, missão ao vivo e saída."""
import collections, glob, json, os, re, statistics, sys
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(HERE, '..')
WORK = os.path.join(HERE, 'dialog_work'); os.makedirs(os.path.join(WORK, 'in'), exist_ok=True); os.makedirs(os.path.join(WORK, 'out'), exist_ok=True)
FLOOR = {'A1': 5.5, 'A2': 8.5, 'B1': 11, 'B2': 15}
CEIL = {'A1': 8, 'A2': 12.5, 'B1': 16.5, 'B2': 22.5}
def words(s): return re.findall(r"[A-Za-z’']+", re.sub(r'\*\*', '', s or ''))
def norm(s): return re.sub(r'\s+', ' ', (s or '').replace('’', "'")).strip().lower()
def load(n): return json.load(open(os.path.join(R, 'data/v4/%03d.json' % n)))
def save(d): json.dump(d, open(os.path.join(R, 'data/v4/%03d.json' % d['n']), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
def lesson_ids(): return sorted(int(os.path.basename(f)[:-5]) for f in glob.glob(os.path.join(R, 'data/v4/[0-9]*.json')))

def metrics(d):
    en = [l['en'] for l in d['dialog']['lines']]; wl = [len(words(x)) for x in en] or [0]
    tri = collections.Counter(); per = []
    for x in en:
        w = [t.lower().replace('’', "'") for t in words(x)]; s = {' '.join(w[i:i + 3]) for i in range(len(w) - 2)}; per.append(s); tri.update(s)
    top = tri.most_common(1)[0] if tri else ('', 0)
    sp = d['dialog']['speakers']; allowed = {v['name'] for v in sp.values()} | {k for k in sp}
    bad = []
    for l in d['dialog']['lines']:
        who = sp.get(l['who'], {}).get('name')
        for m in re.finditer(r'\b(?:Hi|Hey|Hello|Thanks|Thank you|Sorry|Goodbye|Bye|See you),? ([A-Z][a-z]{2,})\b[!?.,]|, ([A-Z][a-z]{2,})[!?.](?:\s|$)', l['en']):
            nm = m.group(1) or m.group(2)
            if nm in allowed or nm == 'Mia': 
                if l['who'] != 'You' and nm == who: bad.append('autossaudação ' + nm)
                continue
            bad.append(nm)
    return dict(avg=statistics.mean(wl), top=top[0], share=top[1] / max(1, len(en)), bad=sorted(set(bad)), n=len(en))


_NAMES = None
def names():
    global _NAMES
    if _NAMES is None:
        S = set()
        for n in lesson_ids():
            sp = load(n)['dialog']['speakers']
            for k, v in sp.items():
                if k != 'You': S.add(k)
                S.add(v['name'])
        try:
            for e in json.load(open(os.path.join(R, 'data/elenco.json'))): S.add(e['name'])
        except Exception: pass
        S -= {'You', 'Yes', 'No', 'May', 'Will', 'Mark', 'Bill', 'Rose', 'Joy', 'Hope', 'Grace', 'Ray', 'Max', 'Sue'}  # ambíguos com palavras comuns; tratados abaixo
        S |= {'Mia'}
        _NAMES = S
    return _NAMES
AMBIG = {'Joy', 'Rose', 'Grace', 'Hope', 'Ray', 'Max', 'Mark', 'Bill', 'Sue', 'Will', 'May'}
GREET = r'(?:Hi|Hey|Hello|Thanks|Thank you|Sorry|Goodbye|Bye|See you|Oi|Olá|Ei|Obrigad[oa]|Tchau|Desculp[ae]|Até logo)'

STOPCAP = set("""Yes No Look Listen Well Oh Wow Thanks Sorry First Okay OK Right Sure Maybe Honestly Actually Still Instead Today Tomorrow Also Anyway Please Hey Hi Hello Good Great Fine Next Then Now Really Yeah Excuse Exactly Agreed True Fair Finally However However Unfortunately Luckily Personally Frankly Seriously Obviously Definitely Perhaps Sometimes Usually Often Meanwhile Tonight Later Soon Sadly Thankfully Clearly Hmm Ah Ouch Hold Wait Stop Come Go Welcome Congratulations Cheers Nope Yep Absolutely Certainly Basically Overall Besides Alright Nice Cool Awesome Perfect Lovely Excellent Monday Tuesday Wednesday Thursday Friday Saturday Sunday January February March April June July August September October November December Spring Summer Fall Autumn Winter Christmas Easter Chicago Paris London Tokyo Brazil America
Sim Não Olha Olhe Claro Verdade Obrigado Obrigada Desculpe Desculpa Certo Pois Enfim Aliás Então Ainda Hoje Amanhã Justo Exato Concordo Talvez Sinceramente Infelizmente Felizmente Bom Ótimo Legal Perfeito Cuidado Calma Espere Vamos Ei Oi Olá Tchau Até Primeiro Depois Agora Mesmo Segunda Terça Quarta Quinta Sexta Sábado Domingo Janeiro Fevereiro Março Abril Maio Junho Julho Agosto Setembro Outubro Novembro Dezembro Primavera Verão Outono Inverno Natal Páscoa Mom Dad Mama Papa Grandma Grandpa Mommy Daddy Mãe Pai Vovó Vovô""".split())

_VOC = None
def vocseen():
    """Nomes que aparecem como vocativo com saudação (Hi, X!) em qualquer aula + nomes de personagens."""
    global _VOC
    if _VOC is None:
        S = set(names())
        for n in lesson_ids():
            for l in load(n)['dialog']['lines']:
                for m in re.finditer(r'\b(?:Hi|Hey|Hello),? ([A-Z][a-z]{2,})\b[!?.,]', l['en']): S.add(m.group(1))
        _VOC = S - STOPCAP
    return _VOC
def fix_vocative(text, addressee):
    """Troca por 'addressee' o nome usado como vocativo (saudação+nome, nome+vírgula no começo, nome no fim)."""
    N = names() | AMBIG
    def rp(m):
        nm = m.group('nm')
        return m.group(0) if (nm == addressee or nm not in N) else m.group(0).replace(nm, addressee, 1)
    t = re.sub(r'\b' + GREET + r',? (?P<nm>[A-Z][a-zà-ú]{2,})\b(?=[!?.,])', rp, text)
    def rp2(m):
        nm = m.group('nm')
        return m.group(0) if (nm == addressee or nm in STOPCAP or nm not in vocseen()) else m.group(0).replace(nm, addressee, 1)
    t = re.sub(r'^(?P<nm>[A-Z][a-zà-ú]{2,}),(?= [A-Za-zà-ú])', rp2, t)
    t = re.sub(r', (?P<nm>[A-Z][a-zà-ú]{2,})(?=[!?.](?:\s|$))', rp, t)
    return t

def fix_names_lesson(d):
    """Corrige vocativos em dialog.lines, telas de conversa/trocas, 'Sua resposta', capa, missão ao vivo e saída. Devolve nº de falas alteradas."""
    sp = d['dialog']['speakers']
    if 'You' not in sp: return 0
    npc = [k for k in sp if k != 'You'][0]
    nn, ln = sp[npc]['name'], sp['You']['name']
    adr = lambda who: nn if who == 'You' else ln
    old = [dict(l) for l in d['dialog']['lines']]; changed = 0
    for l in d['dialog']['lines']:
        e, pt = fix_vocative(l['en'], adr(l['who'])), fix_vocative(l['pt'], adr(l['who']))
        if (e, pt) != (l['en'], l['pt']): changed += 1
        l['en'], l['pt'] = e, pt
    new = d['dialog']['lines']; mp = {}
    for o, n in zip(old, new):
        mp[norm(o['en'])] = n['en']; mp[norm(o['pt'])] = n['pt']
    for p in d['pages']:
        k = p['kind']
        if k == 'dialog':
            p['lines'] = [[w, fix_vocative(e, adr(w)), fix_vocative(t, adr(w))] for w, e, t in p['lines']]
            for sw in p.get('swaps', []): sw['en'] = fix_vocative(sw['en'], adr(sw['who'])); sw['pt'] = fix_vocative(sw['pt'], adr(sw['who']))
        elif k == 'choice':
            t = p['turn']; t['npc'] = fix_vocative(t['npc'], ln); t['pt'] = fix_vocative(t.get('pt', ''), ln)
            for o in t['opts']: o['en'] = fix_vocative(o['en'], nn); o['pt'] = fix_vocative(o.get('pt', ''), nn)
            tc = p.get('teach') or {}
            if tc.get('answers'): tc['answers'] = [fix_vocative(a, nn) for a in tc['answers']]
            g = tc.get('group') or []
            if g and g[0].startswith('Leia a fala de'): g[0] = 'Leia a fala de %s: “%s”.' % (nn, trunc(t['npc']))
        elif k in ('cover', 'role', 'exit'):
            def walk(x):
                if isinstance(x, str): return mp.get(norm(x), x)
                if isinstance(x, list): return [walk(i) for i in x]
                if isinstance(x, dict): return {kk: (walk(v) if kk not in ('art', 'teach') else v) for kk, v in x.items()}
                return x
            for kk in list(p):
                if kk not in ('art', 'teach'): p[kk] = walk(p[kk])
    return changed

def select():
    sel = []
    for n in lesson_ids():
        d = load(n); m = metrics(d); why = []
        if m['share'] >= .4 and m['top']: why.append('estrutura “%s” em %d%% das falas' % (m['top'], round(100 * m['share'])))
        if d['level'] == 'A2' and m['avg'] < 7.5: why.append('A2 raso (média %.1f palavras/fala)' % m['avg'])
        if why and d['level'] != 'A1': sel.append((n, '; '.join(why)))
    packs = []
    for n, why in sel:
        d = load(n); sp = d['dialog']['speakers']
        if 'You' not in sp: continue
        npc = [k for k in sp if k != 'You'][0]
        vocab = [w[0] for p in d['pages'] if p['kind'] == 'vocab' for w in p['words']]
        exprs = [i['en'] for p in d['pages'] if p['kind'] == 'exprs' for i in p['items']]
        pats = [p.get('model') for p in d['pages'] if p['kind'] == 'pattern' and p.get('model')]
        cover = d['pages'][0]; work = next((p['work']['title'] for p in d['pages'] if p['kind'] == 'work'), '')
        packs.append(dict(n=n, level=d['level'], title=d['title'], goal=cover.get('goal', ''), motivo=why, npc_nome=sp[npc]['name'], aprendiz_nome=sp['You']['name'],
                          falas=len(d['dialog']['lines']), vocabulario=vocab, expressoes=exprs, estruturas=pats, obra=work,
                          falas_atuais=[{'quem': 'NPC' if l['who'] != 'You' else 'APRENDIZ', 'en': l['en'], 'pt': l['pt']} for l in d['dialog']['lines']]))
    per = 23; k = (len(packs) + per - 1) // per
    for i in range(k): json.dump(packs[i * per:(i + 1) * per], open(os.path.join(WORK, 'in/d%d.json' % (i + 1)), 'w'), ensure_ascii=False)
    print(len(packs), 'aulas em', k, 'pacotes'); c = collections.Counter(p['level'] for p in packs); print(dict(c))

def fixnames(dry=False):
    tot = les = 0
    for n in lesson_ids():
        d = load(n); raw = json.dumps(d, ensure_ascii=False, separators=(',', ':')); c = fix_names_lesson(d)
        if json.dumps(d, ensure_ascii=False, separators=(',', ':')) != raw:
            if not dry: save(d)
            tot += c; les += 1
    print('falas corrigidas:', tot, 'em', les, 'aulas', '(ensaio)' if dry else '')

def check():
    rows = collections.defaultdict(list)
    for n in lesson_ids():
        d = load(n); m = metrics(d); rows[d['level']].append((n, m))
    for lv, rs in rows.items():
        print(lv, len(rs), 'aulas | média %.1f palavras/fala' % statistics.mean(m['avg'] for _, m in rs),
              '| estrutura ≥40%%: %d' % sum(1 for _, m in rs if m['share'] >= .4), '| nomes inconsistentes: %d' % sum(1 for _, m in rs if m['bad']))

def slot_ok(s, who):
    m = re.findall(r'\{([^{}|]+(?:\|[^{}|]+){2})\}', s or '')
    return len(m) == 1 and '{' not in re.sub(r'\{[^{}]*\}', '', s)

def validate(pk, o):
    err = []; N = pk['falas']; L = o.get('lines') or []
    if len(L) != N: return ['número de falas %d != %d' % (len(L), N)]
    for i, l in enumerate(L):
        for k in ('en', 'pt', 'sw_en', 'sw_pt'):
            if not isinstance(l.get(k), str) or not l[k].strip(): err.append('fala %d sem %s' % (i, k))
        if l.get('sw_en') and not slot_ok(l['sw_en'], 'en'): err.append('fala %d sw_en precisa de 1 bloco {a|b|c}' % i)
        if l.get('sw_pt') and not slot_ok(l['sw_pt'], 'pt'): err.append('fala %d sw_pt precisa de 1 bloco {a|b|c}' % i)
        if l.get('sw_en') and re.sub(r'\{([^{}|]+)\|[^{}]*\}', r'\1', l['sw_en']).strip() != l['en'].strip(): err.append('fala %d: 1ª alternativa do sw_en deve reproduzir a fala' % i)
    turns = (N - 1) // 2; W = o.get('wrong') or []
    if len(W) != turns: err.append('wrong precisa de %d turnos' % turns)
    for i, w in enumerate(W):
        if not (isinstance(w, list) and len(w) == 2 and all(isinstance(x, dict) and x.get('en') and x.get('fb') and x.get('pt') for x in w)): err.append('wrong[%d] inválido' % i)
    can = o.get('can') or []
    if len(can) != 3 or any(c not in [l['en'] for l in L] for c in can): err.append('can: 3 falas do APRENDIZ copiadas exatamente')
    tri = collections.Counter()
    for l in L:
        w = [t.lower().replace('’', "'") for t in words(l['en'])]; tri.update({' '.join(w[i:i + 3]) for i in range(len(w) - 2)})
    top = tri.most_common(1)[0] if tri else ('', 0)
    if top[1] > max(3, .35 * N): err.append('estrutura “%s” em %d falas (máx %d)' % (top[0], top[1], max(3, int(.35 * N))))
    avg = statistics.mean(len(words(l['en'])) for l in L)
    if avg < FLOOR.get(pk['level'], 6): err.append('média %.1f palavras/fala abaixo de %s' % (avg, FLOOR[pk['level']]))
    if avg > CEIL.get(pk['level'], 30): err.append('média %.1f palavras/fala acima de %s (nível %s)' % (avg, CEIL[pk['level']], pk['level']))
    txt = ' '.join(l['en'] + ' ' + l['sw_en'] for l in L) + ' ' + ' '.join(x['en'] for w in W for x in w)
    br = sorted(set(m.group(0).lower() for m in re.finditer(r"\b(flatmates?|flat|takeaway|lift|queue[sd]?|queuing|rubbish|mum|petrol|whilst|trousers|biscuits?|boot|lorry|motorway|pavement|fortnight|cheers|brilliant|mobile phone|holiday|holidays|colour\w*|neighbour\w*|favourite\w*|centre|programme)\b", txt, re.I)))
    if br: err.append('vocabulário/grafia britânica: ' + ', '.join(br))
    for nm in re.findall(r'\b[A-Z][a-z]{2,}\b', txt):
        pass
    return err

def trunc(s, n=118): return s if len(s) <= n else s[:n - 1].rstrip() + '…'
def apply_one(pk, o):
    n = pk['n']; d = load(n); sp = d['dialog']['speakers']; npc = [k for k in sp if k != 'You'][0]
    old = d['dialog']['lines']; L = o['lines']; N = len(old)
    for i, l in enumerate(L): l['who'] = old[i]['who']          # mantém a alternância original
    newl = [{'who': old[i]['who'], 'en': L[i]['en'].strip(), 'pt': L[i]['pt'].strip()} for i in range(N)]
    d['dialog']['lines'] = newl
    # telas de conversa (+ trocas)
    dp = [p for p in d['pages'] if p['kind'] == 'dialog']; pos = 0
    for p in dp:
        k = len(p['lines']); p['lines'] = [[newl[i]['who'], newl[i]['en'], newl[i]['pt']] for i in range(pos, pos + k)]
        p['swaps'] = [{'who': newl[i]['who'], 'en': L[i]['sw_en'].strip(), 'pt': L[i]['sw_pt'].strip()} for i in range(pos, pos + k)]
        pos += k
    # telas 'Sua resposta'
    ch = [p for p in d['pages'] if p['kind'] == 'choice']
    for i, p in enumerate(ch):
        npcl, you = newl[2 * i], newl[2 * i + 1]; w = o['wrong'][i]
        t = p['turn']; t['npc'] = npcl['en']; t['pt'] = npcl['pt']
        t['opts'] = [{'en': you['en'], 'fb': 'Natural e claro.', 'ok': True, 'pt': you['pt']}] + [{'en': x['en'].strip(), 'fb': x['fb'].strip(), 'ok': False, 'pt': x['pt'].strip()} for x in w]
        tc = p.get('teach') or {}
        tc['answers'] = [you['en']]
        g = tc.get('group') or []
        if g and g[0].startswith('Leia a fala de'): g[0] = 'Leia a fala de %s: “%s”.' % (sp[npc]['name'], trunc(npcl['en']))
    # mapa de substituição exata para outros campos (capa, missão ao vivo, saída...)
    rep = {}
    for i in range(N):
        rep[norm(old[i]['en'])] = (newl[i]['en'], 'en'); rep[norm(old[i]['pt'])] = (newl[i]['pt'], 'pt')
    def walk(x, key=None):
        if isinstance(x, str):
            r = rep.get(norm(x));
            return r[0] if r else x
        if isinstance(x, list): return [walk(i) for i in x]
        if isinstance(x, dict): return {k: (v if k in ('turn', 'swaps', 'lines') and False else walk(v, k)) for k, v in x.items()}
        return x
    for p in d['pages']:
        if p['kind'] in ('cover', 'role', 'exit'):
            for k in list(p):
                if k not in ('art', 'teach'): p[k] = walk(p[k])
    cover = d['pages'][0]; cover['can'] = list(o['can'])
    # saída: cue (pt) acompanha o alvo (en)
    ex = [p for p in d['pages'] if p['kind'] == 'exit']
    byen = {l['en']: l['pt'] for l in newl}
    for p in ex:
        for it in p.get('items', []):
            if it.get('target') in byen: it['cue'] = byen[it['target']]
    save(d); return d

def apply(folder=None):
    folder = folder or os.path.join(WORK, 'out'); ok = bad = 0; rej = []
    packs = {}
    for f in glob.glob(os.path.join(WORK, 'in/d*.json')):
        for pk in json.load(open(f)): packs[str(pk['n'])] = pk
    for f in sorted(glob.glob(os.path.join(folder, 'd*.json'))):
        try: data = json.load(open(f))
        except Exception as e: print('JSON inválido', f, e); continue
        for n, o in data.items():
            pk = packs.get(str(n))
            if not pk: continue
            err = validate(pk, o)
            if err: bad += 1; rej.append((n, err[:3])); continue
            apply_one(pk, o); ok += 1
    print('aplicadas:', ok, '| rejeitadas:', bad)
    for n, e in rej[:12]: print(' ', n, e)
    json.dump(rej, open(os.path.join(WORK, 'rejeitadas.json'), 'w'), ensure_ascii=False)

def validate_pack(k):
    packs = {str(pk['n']): pk for pk in json.load(open(os.path.join(WORK, 'in/d%s.json' % k)))}
    try: data = json.load(open(os.path.join(WORK, 'out/d%s.json' % k)))
    except Exception as e: print('JSON inválido:', e); return
    ok = 0
    for n, pk in packs.items():
        o = data.get(n)
        if not o: print(n, 'AUSENTE'); continue
        err = validate(pk, o)
        if err: print(n, err)
        else: ok += 1
    print('%d de %d aulas passam no validador' % (ok, len(packs)))

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'check'
    {'validate': lambda: validate_pack(sys.argv[2]), 'select': select, 'check': check, 'fixnames': fixnames, 'dryfix': lambda: fixnames(True)}.get(cmd, lambda: apply(sys.argv[2] if len(sys.argv) > 2 else None))()
