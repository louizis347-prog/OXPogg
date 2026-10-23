#!/usr/bin/env python3
"""Correções mecânicas de conteúdo dos quadros (cursos regulares não ingleses).

 1. remove os metadados `episodeFocus` e `episodeId` de todos os quadros (marca de gabarito
    que nenhum código lê e que repete "Episódio N: ..." em cada quadro);
 2. troca opções de resposta repetidas ou de preenchimento (nome do personagem, "Não agora",
    frase-modelo) no quiz `dquiz`, nos diálogos `tdlg` e na escuta `lplay` por frases reais de
    outros episódios do mesmo nível e idioma;
 3. colapsa palavras repetidas coladas pelo gabarito ("über über" -> "über").
Idempotente: rodar de novo não muda nada. Depois rode tools/build_data_index.py --check.
"""
import json, os, re, sys, zlib, collections

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
LANGS = ['es', 'pt', 'enesh', 'fr', 'frbr', 'de', 'it', 'ja', 'ko', 'zhbr']
UI_ES = {'pt', 'enesh', 'fr'}      # cursos para hispanofalantes
NOREPLY = {'pt': 'Não responde ao que foi dito.', 'es': 'No responde a lo que se dijo.'}
MARK = re.compile(r'\s*·\s*(?:itinéraire|itinerario|parcours|percurso|route|Weg|Folge|recorrido|ルート|코스|路线)\s*\d+', re.I | re.U)
DUP = re.compile(r'\b([^\W\d_]{2,})(\s+)\1\b', re.I | re.U)
STOCK = {'não agora', 'ainda não', 'pode repetir?', 'no ahora', 'todavía no', '¿puedes repetir?'}
H = lambda *a: zlib.crc32('|'.join(map(str, a)).encode())


def load_blocks(course):
    m = json.load(open(os.path.join(ROOT, 'manifest.json'), encoding='utf-8'))
    for b in m[course]:
        p = os.path.join(ROOT, b)
        yield p, json.load(open(p, encoding='utf-8'))


def clean(o, dedupe):
    """remove metadados e colapsa repetições; devolve True se mudou"""
    ch = False
    if isinstance(o, dict):
        for k in ('episodeFocus', 'episodeId'):
            if k in o:
                del o[k]; ch = True
        for k, v in list(o.items()):
            if k in ('art', 'c', 'seed', 'cam', 'scene'):
                continue
            if isinstance(v, str):
                if dedupe:
                    nv = DUP.sub(lambda m: m.group(1), MARK.sub('', v))
                    if nv != v:
                        o[k] = nv; ch = True
            elif clean(v, dedupe):
                ch = True
    elif isinstance(o, list):
        for i, v in enumerate(o):
            if isinstance(v, str):
                if dedupe:
                    nv = DUP.sub(lambda m: m.group(1), MARK.sub('', v))
                    if nv != v:
                        o[i] = nv; ch = True
            elif clean(v, dedupe):
                ch = True
    return ch


def build_pools(eps):
    """devolve (pool, palavras, layout, personagens).
    pool = frases-alvo reais dos diálogos `tdlg` (n[0]) com a tradução; layout 'A' quando o quadro
    `read` traz [personagem, fala] e 'B' quando traz [fala, tradução]."""
    firsts = collections.Counter()
    words = []
    for e in eps:
        for x in e['fr']:
            if x['k'] == 'read':
                for pair in x.get('s', []):
                    firsts[pair[0]] += 1
            elif x['k'] == 'words':
                for it in x.get('items', []):
                    if it and it[0]:
                        words.append(it[0])
    layout = 'A' if len(firsts) < 80 else 'B'
    names = [n for n, c in firsts.most_common(12)] if layout == 'A' else []
    seen, pool = set(), []
    for e in eps:
        for x in e['fr']:
            if x['k'] != 'tdlg':
                continue
            for t in x.get('turns', []):
                n = t.get('n', [])
                if len(n) != 2 or n[0] in seen or not 8 <= len(n[0]) <= 140 or '·' in n[0]:
                    continue
                if not n[1] or n[1] == n[0]:
                    continue
                seen.add(n[0]); pool.append((names[H(n[0]) % len(names)] if names else '', n[0], n[1]))
    for e in eps:                       # frases das listas de vocabulário (com glosa) completam o conjunto
        for x in e['fr']:
            if x['k'] == 'words':
                for it in x.get('items', []):
                    if len(it) > 2 and it[0] not in seen and 8 <= len(it[0]) <= 140 and it[2] \
                            and it[2] != it[0] and not re.search(r'frase[- ]?(clave|chave)', it[2], re.I):
                        seen.add(it[0]); pool.append((names[H(it[0]) % len(names)] if names else '', it[0], it[2]))
    return pool, sorted(set(words)), layout


def pick(pool, n, salt, banned, k):
    out, i = [], 0
    L = len(pool)
    while len(out) < k and i < 60:
        c = pool[H(n, salt, i) % L]; i += 1
        if c[1] in banned or any(c[1] == o[1] for o in out):
            continue
        out.append(c)
    for c in pool:
        if len(out) >= k:
            break
        if c[1] not in banned and not any(c[1] == o[1] for o in out):
            out.append(c)
    return out


def fix_course(course, lang):
    ui = 'es' if lang in UI_ES else 'pt'
    paths = list(load_blocks(course))
    eps = [e for _, d in paths for e in d]
    pool, words, layout = build_pools(eps)
    stock = set(STOCK)
    for e in eps:
        for x in e['fr']:
            if x['k'] == 'read':
                for pair in x.get('s', []):
                    if layout == 'A':
                        stock.add(pair[0].lower())
    changed_files = 0
    for p, d in paths:
        before = json.dumps(d, ensure_ascii=False, separators=(',', ':'))
        for e in d:
            n = e['n']
            for x in e['fr']:
                k = x['k']
                if k == 'dquiz':
                    spk = []
                    for y in e['fr']:
                        if y['k'] == 'read':
                            spk += [p_[0] for p_ in y.get('s', []) if len(p_[0]) <= 24]
                    spk = sorted(set(spk))
                    for qi, it in enumerate(x.get('items', [])):
                        opts = it.get('opts', [])
                        a = it.get('a', 0)
                        texts = [o[0] for o in opts]
                        good = opts[a] if a < len(opts) else opts[0]
                        mode = 'A' if (good[1] in spk or (len(good[1]) <= 24 and len(good[1].split()) <= 3)) and good[1] != good[0] else 'B'
                        bad = [i for i, o in enumerate(opts) if i != a and (
                            texts.index(o[0]) != i or o[0].lower() in stock or o[0] == o[1])]
                        if bad and pool:
                            banned = set(texts) | {good[1]}
                            new = pick(pool, n, 'q%d' % qi, banned, len(bad))
                            extra = [w for w in words if w not in banned and len(w) >= 3]
                            while len(new) < len(bad) and extra:      # sobrou pouca frase: completa com termos do curso
                                w = extra[H(n, 'w', qi, len(new)) % len(extra)]
                                if all(w != z[1] for z in new):
                                    new.append(('', w, w))
                                else:
                                    extra.remove(w)
                            for i, c in zip(bad, new):
                                if mode == 'A':
                                    who = [z for z in spk if z != good[1]] or spk or ['']
                                    opts[i] = [c[1], who[H(n, qi, i) % len(who)]]
                                else:
                                    opts[i] = [c[2], c[1]]
                elif k == 'tdlg':
                    for ti, t in enumerate(x.get('turns', [])):
                        o = t.get('o', [])
                        a = t.get('a', 0)
                        texts = [z[0] for z in o]
                        bad = [i for i, z in enumerate(o) if i != a and (
                            not (z[1] or '').strip() or z[0].lower() in stock or texts.index(z[0]) != i)]
                        if bad and pool:
                            banned = set(texts) | {t['n'][0]}
                            new = pick(pool, n, 't%d' % ti, banned, len(bad))
                            for i, c in zip(bad, new):
                                o[i] = [c[1], c[2] or NOREPLY[ui]]
                elif k == 'lplay' and words:
                    for ri, r in enumerate(x.get('rounds', [])):
                        o = r.get('opts', [])
                        if len(set(map(str, o))) < len(o):
                            keep = set(o)
                            for i, v in enumerate(o):
                                if o.index(v) != i:
                                    for j in range(40):
                                        c = words[H(n, 'l%d' % ri, i, j) % len(words)]
                                        if c not in keep:
                                            o[i] = c; keep.add(c); break
        for e in d:
            clean(e['fr'], lang in ('es', 'pt', 'enesh', 'fr', 'frbr', 'de', 'it'))
        after = json.dumps(d, ensure_ascii=False, separators=(',', ':'))
        if True:
            old = open(p, encoding='utf-8').read().rstrip('\n')
            if old != after:
                open(p, 'w', encoding='utf-8').write(after)
                changed_files += 1
    return changed_files


def clean_neighbors():
    m = json.load(open(os.path.join(ROOT, 'manifest.json'), encoding='utf-8'))
    n = 0
    for course in sorted(m):
        if not (course.startswith('nb') or course.startswith('en-')):
            continue
        for p, d in load_blocks(course):
            ch = False
            for e in d:
                ch |= clean(e.get('fr', []), False)
            if ch:
                open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
                n += 1
    print('neighbors e inglês (só metadados): blocos alterados', n, flush=True)


if __name__ == '__main__':
    only = sys.argv[1:]
    if not only or 'nb' in only:
        clean_neighbors()
        only = [o for o in only if o != 'nb']
        if not only and len(sys.argv) > 1:
            sys.exit(0)
    m = json.load(open(os.path.join(ROOT, 'manifest.json'), encoding='utf-8'))
    for course in sorted(m):
        lang = course.split('-')[0]
        if lang in LANGS and (not only or lang in only):
            print(course, fix_course(course, lang), 'blocos alterados', flush=True)
