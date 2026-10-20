# -*- coding: utf-8 -*-
"""Montador dos episódios Neighbors (espanhol, francês, japonês).
Reconstruído a partir dos dados existentes: cada arco é um arquivo com 9 dicts (EPS<NN>) e o montador gera os
episódios completos, a revisão do arco e os passos extras (acentos, ditado, escrita à mão).
Uso:
  python3 tools/nb/buildnb.py test fr f35      # reconstrói o arco e compara com data/ (valida o montador)
Biblioteca: build_arc(lang, arc_idx, eps, nxt) -> lista de episódios (9 + revisão)."""
import json, glob, os, re, random, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
DATA = os.path.join(ROOT, 'data')

PAL = [['#00B894', '#0984E3'], ['#FF7675', '#FDCB6E'], ['#E17055', '#FDCB6E'], ['#0984E3', '#74B9FF'], ['#00B894', '#55EFC4'],
       ['#6C5CE7', '#A29BFE'], ['#E84393', '#FD79A8'], ['#F39C12', '#E17055'], ['#2D98DA', '#20BF6B']]
REVPAL = ['#6C5CE7', '#FF7AA8']
YOU = ['🙂', '#e85d75']
PARTNER_COLOR = '#8F5400'
NUMW = {4: 'quatro', 5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez'}

# prefixos por idioma: título da revisão, "em/à" no mapa do arco, determinantes a retirar do vocabulário
LANG = {
    'es': dict(rev='Repaso del arco %d', at='En %s: %s.', dets=r"^(el|la|los|las|un|una|unos|unas|lo)\s+", close='¡Ya conoces %s lugares! Ahora, a practicar.', hook='Repasemos este arco: %s lugares, %s historias.',
               hookpt='Vamos rever este arco: %s lugares, %s histórias. Toque nas falas para ouvir.', revn=96000),
    'fr': dict(rev="Révision de l'arc %d", at='À %s : %s.', dets=r"^(le|la|les|l'|l’|un|une|des|ce|cet|cette|ces|mon|ma|mes|du|au|aux)\s*", close='Tu connais déjà %s lieux ! Maintenant, on pratique.', hook='Révisons cet arc : %s lieux, %s histoires.',
               hookpt='Vamos rever este arco: %s lugares, %s histórias. Toque nas falas para ouvir.', revn=96100),
    'ja': dict(rev='Revisão · Arco %d', at='%s: %s。', dets=r"^$", close='もう %s の ばしょを しっています! れんしゅうしましょう。', hook='このアークを ふりかえりましょう。%s ばしょ、%s ものがたり。',
               hookpt='Vamos rever este arco: %s lugares, %s histórias. Toque nas falas para ouvir.', revn=97500),
}
NUMJA = {4: 'よっつ', 5: 'いつつ', 6: 'むっつ', 7: 'ななつ', 8: 'やっつ', 9: 'ここのつ', 10: 'とお'}
NUMES = {4: 'cuatro', 5: 'cinco', 6: 'seis', 7: 'siete', 8: 'ocho', 9: 'nueve', 10: 'diez'}
NUMFR = {4: 'quatre', 5: 'cinq', 6: 'six', 7: 'sept', 8: 'huit', 9: 'neuf', 10: 'dix'}


def core(word, lang):
    w = word.strip()
    pat = LANG[lang]['dets']
    c = re.sub(pat, '', w, flags=re.I)
    return c if c else w


def parse_line(s, name, you='You'):
    """'P: texto | pt [| romaji]' -> [falante, texto, pt, (romaji)]"""
    sp, rest = s.split(':', 1)
    parts = [x.strip() for x in rest.split(' | ')]
    who = you if sp.strip() == 'Y' else name
    return [who] + parts


def bold_keys(text, gl):
    """marca em negrito cada expressão da glosa que aparece na fala (primeira ocorrência, sem sobrepor)."""
    t = text.replace('**', '')
    spans = []
    for k in gl:
        i = t.lower().find(k.lower())
        if i >= 0 and not any(i < b and a < i + len(k) for a, b in spans):
            spans.append((i, i + len(k)))
    for a, b in sorted(spans, reverse=True):
        t = t[:a] + '**' + t[a:b] + '**' + t[b:]
    return t


def strip_bold(t):
    return t.replace('**', '')


def corpus_pt(cid_prefix, exclude_n):
    """falas do parceiro (pt) de outros episódios do curso, para distratores do 'quem disse'."""
    out = []
    for f in sorted(glob.glob(os.path.join(DATA, cid_prefix + '-*_*.json'))):
        try:
            for e in json.load(open(f, encoding='utf-8')):
                if e.get('rev') or e['n'] == exclude_n:
                    continue
                for fr in e.get('fr', []) or []:
                    if fr.get('k') == 'nbchat' and fr.get('title') == 'O diálogo-padrão':
                        out += [l[2] for l in fr['lines'] if l[0] != 'You']
        except Exception:
            pass
    return out


_CORPUS = {}


def get_corpus(prefix):
    if prefix not in _CORPUS:
        _CORPUS[prefix] = corpus_pt(prefix, -1)
    return _CORPUS[prefix]


def build_ep(sp, lang, pos, lv, base, corpus_prefix):
    """sp: dict do arquivo de arco; pos: 0..8 posição no arco; base: n base do curso (para 'o')."""
    n = sp['n']
    rnd = random.Random(n)
    pal = PAL[pos % 9]
    name, face, city = sp['name'], sp['face'], sp['city']
    hook = sp['hook'].split('|')
    o = n - base
    ja = lang == 'ja'
    chat = [parse_line(s, name) for s in sp['chat']]
    chat2 = [parse_line(s, name) for s in sp['chat2']]
    # chat2: o primeiro a falar é o aluno (Y), como nos dados existentes
    slang_name, slang_style, slang_lines, gl, ess = sp['slang']
    slang = [parse_line(s.replace('F:', 'P:', 1), slang_name) for s in slang_lines]
    for l in slang:
        l[1] = bold_keys(l[1], gl)
    emo = sp['emo']
    v = sp['v']
    ex = {
        'n': n, 't': sp['t'], 's': sp['s'], 'sc': sp['sc'],
        'a': {'k': 'Cidade', 'w': city, 'y': '', 'd': sp['desc']},
        'h': {'l': hook[0], 'src': city, 'tr': hook[1]},
        'p': 'Hoje você conhece %s, de %s. %s' % (name, city, sp['mission']),
        'g': {'t': sp['goal']}, 'v2': True, 'en': 1, 'baked': True, 'th': 'az', 'mdl': 2, 'lv': lv,
        'v': [[w[0], w[1], w[2]] for w in v], 'rs': sp['rs'], 'std': 3, 'o': o,
    }
    fr = []
    fr.append({'k': 'nbhero', 'g': pal, 'num': o, 'lvl': lv, 'face': face, 'name': name, 'city': city, 'sub': sp['t'], 'emo': emo,
               'mission': sp['mission'], 'hook': hook})
    fr.append({'k': 'nbchat', 'g': pal, 'title': 'O diálogo-padrão', 'intro': 'Toque em “Próxima fala” para abrir cada mensagem.',
               'cast': {name: [face, PARTNER_COLOR], 'You': YOU}, 'lines': chat})
    # nbtap: 3 perguntas do roteiro + 3 "quem disse"
    items = []
    for i, t in enumerate(sp['tap']):
        q, pt, opts, a, line, why = t
        items.append({'q': q, 'pt': pt, 'opts': [[emo[i % len(emo)], o_] for o_ in opts], 'a': a, 'line': line, 'why': why})
    pidx = [i for i, l in enumerate(chat) if l[0] != 'You']
    cps = get_corpus(corpus_prefix)
    mine = {l[2] for l in chat}
    pool = [c for c in cps if c not in mine]
    for li in rnd.sample(pidx, min(3, len(pidx))):
        ok = chat[li][2]
        ds = rnd.sample(pool, 2)
        opts = [ok] + ds
        rnd.shuffle(opts)
        items.append({'pt': 'O que %s disse?' % name, 'opts': [['💬', t] for t in opts], 'a': opts.index(ok), 'line': li})
    fr.append({'k': 'nbtap', 'g': pal, 'title': 'Ouça e toque', 'items': items})
    swtip, pages = sp['swap']
    fr.append({'k': 'nbswap', 'g': pal, 'title': sp['goal'], 'tip': swtip, 'goal': 4,
               'pages': [{'label': p[0], 'S': [list(x) for x in p[1]], 'E': [list(x) for x in p[2]], 'end': p[3]} for p in pages]})
    fr.append({'k': 'nbchat', 'g': pal, 'title': 'Mesma situação, outro jeito', 'intro': 'Variação: o mesmo objetivo com palavras diferentes.',
               'cast': {'You': YOU, name: [face, PARTNER_COLOR]}, 'lines': chat2, 'me': name, 'role': True})
    fr.append({'k': 'nbslang', 'g': pal, 'title': 'Chat com %s: gírias e ditados' % slang_name,
               'cast': {slang_name: list(slang_style), 'You': YOU}, 'lines': slang, 'gl': gl, 'ess': ess})
    # nbctx: uma pergunta por expressão da glosa
    ctx = []
    keys = list(gl.keys())
    for k in keys[:5]:
        line = next((l for l in slang if ('**' + k + '**') in l[1]), None)
        if not line:
            continue
        txt = line[1].replace('**' + k + '**', '____')
        txt = strip_bold(txt)
        others = [x for x in keys if x != k]
        opts = [k] + rnd.sample(others, 2)
        rnd.shuffle(opts)
        ctx.append({'ic': '🎯', 'sit': 'Complete a fala: “%s” (%s)' % (txt, line[2]), 'opts': opts, 'a': opts.index(k), 'why': '“%s” = %s' % (k, gl[k])})
    fr.append({'k': 'nbctx', 'g': pal, 'title': 'Em que contexto?', 'items': ctx})
    vocab = [[core(w[0], lang), w[3], w[1]] for w in v[:5]]
    fr.append({'k': 'nbvocab', 'g': pal, 'title': 'Soletrando', 'items': vocab})
    you_lines = [l for l in chat if l[0] == 'You']
    shadow = [l[1:] for l in you_lines[:4]]
    fr.append({'k': 'nbshadow', 'g': pal, 'title': 'Fale como %s' % name, 'items': [list(x) for x in shadow], 'real': list(sp['real'])})
    fr.append({'k': 'nbfind', 'g': pal, 'title': 'Caça-palavras', 'items': vocab})
    rs = sp['recap_slang'].split(' → ')
    recap = [list(l[1:3]) for l in you_lines[:3]] + [[rs[0], rs[1]]]
    fr.append({'k': 'wrap', 'title': 'Para levar na mochila', 'recap': recap, 'teaser': None})
    ex['fr'] = fr
    return ex


def set_teaser(ep, nxt):
    w = ep['fr'][-1]
    if nxt is None:
        w['teaser'] = {'t': 'Mais vizinhos', 'd': 'A rua continua'}
    else:
        w['teaser'] = {'t': '%s, em %s' % (nxt['name'], nxt['city']), 'd': nxt['s']}


def build_review(lang, arc_idx, built, specs, lv, base_rev, rev_o, corpus_prefix, nxt_spec=None):
    """built: episódios do arco já montados; specs: dicts originais (para v com emoji)."""
    L = LANG[lang]
    n = base_rev + arc_idx
    rnd = random.Random(n)
    k = len(built)
    cities = [e['a']['w'] for e in built]
    nw = {'es': NUMES, 'fr': NUMFR, 'ja': NUMJA}[lang][k]
    nwpt = NUMW[k]
    words = sum(len(e['v']) for e in built)
    title = L['rev'] % arc_idx
    ex = {
        'n': n, 't': title, 's': 'Revisão: %d lugares, %d palavras e as frases do arco' % (k, words), 'sc': 'office',
        'a': {'k': 'Cidade', 'w': 'Mapa do arco', 'y': '',
              'd': 'Neste arco você passou por %s. Agora é hora de rever as palavras e as frases de cada lugar.' % ', '.join(cities)},
        'h': {'l': (L['hook'] % (nw, nw)), 'src': 'Poggie', 'tr': L['hookpt'] % (nwpt, nwpt)},
        'p': 'Hoje você revê os lugares, as palavras e as frases dos últimos %d episódios.' % k,
        'g': {'t': 'Revisão do arco'}, 'v2': True, 'baked': True, 'th': 'az', 'mdl': 2, 'lv': lv, 'v': [], 'rs': 'office', 'std': 3,
        'o': rev_o, 'rev': 1, 'rf': 1,
    }
    g = REVPAL
    lines = [['Poggie', L['hook'] % (nw, nw), L['hookpt'] % (nwpt, nwpt)]]
    for e in built:
        first = e['s']
        d = e['a']['d'].split('. ')[0].rstrip('.') + '.'
        lines.append(['Poggie', L['at'] % (e['a']['w'], e['t']), '%s · %s' % (first, d)])
    lines.append(['Poggie', L['close'] % nw, 'Você já conhece %s lugares! Agora, vamos praticar.' % nwpt])
    fr = [{'k': 'nbchat', 'g': g, 'title': 'Mapa do arco', 'intro': 'Toque em “Próxima fala” para abrir cada mensagem.',
           'cast': {'Poggie': ['🧭', '#6C5CE7'], 'You': YOU}, 'lines': lines}]
    # vocabulário: 1 palavra por episódio (a primeira com emoji), significados erradas vêm de outros episódios
    vv = []
    for sp, e in zip(specs, built):
        w = sp['v'][rnd.randrange(len(sp['v']))]
        vv.append((core(w[0], lang), w[3], w[1], e['fr'][0]['name']))
    pool = [(x[2], x[1]) for x in vv]
    tap = []
    for i, (w, em, pt, nm) in enumerate(vv[:4]):
        ds = [p for p in pool if p[0] != pt]
        ds = rnd.sample(ds, 2)
        opts = [(em, pt)] + ds
        rnd.shuffle(opts)
        tap.append({'pt': 'O que significa “%s”?' % w, 'opts': [[a, b] for a, b in opts], 'a': [b for a, b in opts].index(pt),
                    'ln': [nm, w], 'rv': 1, 'why': '%s = %s' % (w, pt)})
    fr.append({'k': 'nbtap', 'g': g, 'title': 'Ouça e toque: revisão', 'items': tap})
    # contexto: 3 expressões de episódios diferentes
    glall = []
    for e in built:
        sl = [f for f in e['fr'] if f['k'] == 'nbslang'][0]
        for key in list(sl['gl'])[:3]:
            line = next((l for l in sl['lines'] if ('**' + key + '**') in l[1]), None)
            if line:
                glall.append((key, sl['gl'][key], line))
    rnd.shuffle(glall)
    ctx = []
    used = set()
    for key, gm, line in glall:
        if len(ctx) == 3:
            break
        if key in used:
            continue
        used.add(key)
        others = [x[0] for x in glall if x[0] != key]
        opts = [key] + rnd.sample(others, 2)
        rnd.shuffle(opts)
        txt = strip_bold(line[1].replace('**' + key + '**', '____'))
        ctx.append({'ic': '🎯', 'sit': 'Complete a fala: “%s” (%s)' % (txt, line[2]), 'opts': opts, 'a': opts.index(key), 'why': '“%s” = %s' % (key, gm)})
    fr.append({'k': 'nbctx', 'g': g, 'title': 'Em que contexto?', 'items': ctx})
    # vocabulário e caça-palavras: itens de episódios variados
    allv = []
    for sp in specs:
        for w in sp['v']:
            allv.append([core(w[0], lang), w[3], w[1]])
    rnd.shuffle(allv)
    fr.append({'k': 'nbvocab', 'g': g, 'title': 'Soletrando: revisão', 'items': allv[:6]})
    fr.append({'k': 'nbfind', 'g': g, 'title': 'Caça-palavras: revisão', 'items': allv[6:11]})
    sh = []
    for e in built:
        yl = [f for f in e['fr'] if f['k'] == 'nbchat'][0]['lines']
        sh += [l[1:] for l in yl if l[0] == 'You'][:2]
    rnd.shuffle(sh)
    real = built[rnd.randrange(len(built))]['fr']
    real = [f for f in real if f['k'] == 'nbshadow'][0]['real']
    fr.append({'k': 'nbshadow', 'g': g, 'title': 'Fale de novo', 'items': [list(x) for x in sh[:4]], 'real': list(real)})
    recap = [list(x[:2]) for x in sh[:3]]
    pair = rnd.choice(glall)
    recap.append([pair[0], pair[1]])
    nx = {'t': 'Mais vizinhos', 'd': 'A rua continua'} if nxt_spec is None else {'t': '%s, em %s' % (nxt_spec['name'], nxt_spec['city']), 'd': nxt_spec['s']}
    fr.append({'k': 'wrap', 'title': 'Para levar na mochila', 'recap': recap, 'teaser': nx})
    ex['fr'] = fr
    return ex


# ---------- passos extras (acentos, ditado, escrita) ----------
def strip_acc(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


ES_ALT = {'á': 'aeio', 'é': 'aeio', 'í': 'iaeou', 'ó': 'oaeu', 'ú': 'uaeo', 'ñ': 'n', 'ü': 'u'}
FR_ALT = {'é': 'èê', 'è': 'éê', 'ê': 'éè', 'à': 'â', 'â': 'à', 'ô': 'o', 'î': 'i', 'û': 'ù', 'ù': 'û', 'ë': 'e', 'ï': 'i', 'ç': 'c'}
ES_TIPS = [(r'ñ', 'A letra “ñ” é uma letra própria: año (ano) ≠ ano (ânus). Não troque por “n”.'),
           (r'[íÍ]a|[íÍ]o', 'Em -ía / -ío o í é tônico e leva acento (hiato).'),
           (r'ción|sión', 'Palavras terminadas em -ción / -sión levam acento no ó (agudas terminadas em n).'),
           (r'ü', 'O trema (ü) só aparece em güe/güi; o acento (ú) marca a sílaba tônica.'),
           (r'[áéíóú]', 'Em espanhol, o acento escrito marca a sílaba tônica quando foge à regra (agudas em vogal, n, s; esdrújulas sempre).')]
FR_TIPS = [(r'ç', 'O “ç” (cedilha) soa /s/ antes de a, o, u: français, garçon.'), (r'è', 'O acento grave (è) soa aberto /ɛ/: très, mère.'),
           (r'ê', 'O circunflexo (ê) também soa aberto /ɛ/ e costuma indicar um “s” antigo: fête, forêt.'),
           (r'é', 'O acento agudo (é) soa fechado /e/: café, été.')]
FR_GEN = 'Em francês os acentos mudam o som da vogal: é (fechado), è/ê (aberto), à/â, ô, û.'
HAS = re.compile(r'[áéíóúñüàèìòùâêîôûçãõëïœ]', re.I)


def acc_variants(w, lang):
    alt = ES_ALT if lang == 'es' else FR_ALT
    vs = []
    st = strip_acc(w) if lang == 'fr' else None
    if lang == 'es':
        st = w
        for c in 'ñ':
            st = st.replace(c, 'n')
        st = strip_acc(st)
    if st != w:
        vs.append(st)
    for i, c in enumerate(w):
        for a in alt.get(c.lower(), ''):
            if c.isupper():
                a = a.upper()
            vs.append(w[:i] + a + w[i + 1:])
    out = []
    for x in vs:
        if x != w and x not in out:
            out.append(x)
    return out


def acc_tip(w, lang):
    tips = ES_TIPS if lang == 'es' else FR_TIPS
    for p, t in tips:
        if re.search(p, w):
            return t
    return None if lang == 'es' else FR_GEN


def add_dict(x):
    if any(s['k'] == 'nbdict' for s in x['fr']):
        return
    lines = [l for s in x['fr'] if s['k'] == 'nbchat' for l in s['lines']]
    c = [l for l in lines if 3 <= len(l[1].split()) <= 9 and len(l[1]) <= 70]
    if len(c) < 3:
        c = lines
    if len(c) < 3:
        return
    pick = [c[0], c[len(c) // 2], c[-1]]
    seen, out = [], []
    for l in pick + c:
        if l[1] in seen:
            continue
        seen.append(l[1])
        out.append({'t': l[1], 'pt': l[2]})
        if len(out) == 3:
            break
    j = max(k for k, s in enumerate(x['fr']) if s['k'] in ('nbvocab', 'nbacc', 'nbart', 'nbkanji', 'nbwrite'))
    x['fr'].insert(j + 1, {'k': 'nbdict', 'g': ['#2D98DA', '#20BF6B'], 'title': 'Ditado', 'items': out})


def add_acc(x, lang):
    if any(s['k'] == 'nbacc' for s in x['fr']):
        return
    rnd = random.Random(x['n'])
    items, seen = [], set()
    for w in x.get('v', []):
        word = w[0].strip()
        if not HAS.search(word) or word in seen or len(word) > 26:
            continue
        vs = acc_variants(word, lang)
        if not vs:
            continue
        seen.add(word)
        alts = [vs[0]] + (rnd.sample(vs[1:], min(1, len(vs) - 1)) if len(vs) > 1 else [])
        items.append({'w': word, 's': strip_acc(word) if lang == 'fr' else vs[0], 'pt': w[1], 'alts': alts[:2], 'tip': acc_tip(word, lang)})
    if len(items) < 3:
        for sec in x['fr']:
            if sec['k'] != 'nbchat':
                continue
            for l in sec['lines']:
                for tok in re.findall(r"[\w'’]+", l[1]):
                    if not HAS.search(tok) or len(tok) < 4 or tok in seen or len(items) >= 5:
                        continue
                    vs = acc_variants(tok, lang)
                    if not vs:
                        continue
                    seen.add(tok)
                    alts = [vs[0]] + (rnd.sample(vs[1:], min(1, len(vs) - 1)) if len(vs) > 1 else [])
                    items.append({'w': tok, 's': strip_acc(tok) if lang == 'fr' else vs[0], 'pt': 'na frase: «' + (l[2] if len(l) > 2 else '') + '»', 'alts': alts[:2], 'tip': acc_tip(tok, lang)})
    if len(items) < 3:
        return
    j = next(k for k, s in enumerate(x['fr']) if s['k'] == 'nbvocab')
    x['fr'].insert(j + 1, {'k': 'nbacc', 'g': x['fr'][0].get('g'), 'title': 'Acentos e ortografia', 'items': items[:5]})


_KS = None


def kana_set():
    global _KS
    if _KS is None:
        _KS = set(json.load(open(os.path.join(DATA, 'kana-strokes.json'))).keys()) | set(json.load(open(os.path.join(DATA, 'kanji-strokes.json'))).keys())
    return _KS


def add_write(x):
    if any(s['k'] == 'nbwrite' for s in x['fr']):
        return
    it = []
    for w in x.get('v', []):
        word = w[0].strip()
        m = re.search(r'«(.+?)»', w[2] if len(w) > 2 else '')
        if word and all(c in kana_set() for c in word) and m:
            it.append({'w': word, 'm': w[1], 'r': m.group(1), 's': word})
        if len(it) == 3:
            break
    if len(it) < 2:
        return
    j = max(k for k, s in enumerate(x['fr']) if s['k'] in ('nbvocab', 'nbkanji'))
    x['fr'].insert(j + 1, {'k': 'nbwrite', 'g': ['#2D98DA', '#20BF6B'], 'title': 'Escreva à mão', 'items': it})


def finish(x, lang):
    """aplica os passos extras do idioma a um episódio comum (não revisão)."""
    if x.get('rev'):
        return
    if lang in ('fr', 'es'):
        add_acc(x, lang)
        add_dict(x)
    elif lang == 'ja':
        add_write(x)


def build_arc(lang, arc_idx, eps, lv, base, base_rev, rev_o_of, corpus_prefix, nxt_spec=None):
    """eps: lista de dicts (9); devolve [ep1..ep9, revisão] já com os passos extras."""
    built = [build_ep(sp, lang, i, lv, base, corpus_prefix) for i, sp in enumerate(eps)]
    for i, e in enumerate(built):
        set_teaser(e, eps[i + 1] if i + 1 < len(eps) else None)
        if i + 1 == len(eps):
            e['fr'][-1]['teaser'] = {'t': 'Revisão do arco', 'd': 'Rever lugares, palavras e frases'} if False else e['fr'][-1]['teaser']
    rev = build_review(lang, arc_idx, built, eps, lv, base_rev, rev_o_of(built), corpus_prefix, nxt_spec)
    for e in built:
        finish(e, lang)
    return built + [rev]


# ---------- validação ----------
def check_spec(sp):
    errs = []
    n = sp['n']
    if len(sp['v']) != 6:
        errs.append((n, 'v precisa de 6 itens'))
    if len(sp['chat']) != 11:
        errs.append((n, 'chat precisa de 11 falas (%d)' % len(sp['chat'])))
    if len(sp['chat2']) != 6:
        errs.append((n, 'chat2 precisa de 6 falas'))
    if len(sp['slang'][2]) != 6:
        errs.append((n, 'slang precisa de 6 falas'))
    if sp['real'][0] == sp['real'][1]:
        errs.append((n, 'real igual'))
    gl = sp['slang'][3]
    for k in list(gl)[:5]:
        if not any(k.lower() in l.lower() for l in sp['slang'][2]):
            errs.append((n, 'expressão da glosa não aparece nas falas: ' + k))
    chat = [parse_line(s, 'X') for s in sp['chat']]
    for i, t in enumerate(sp['tap']):
        if not (0 <= t[4] < len(chat)) or not (0 <= t[3] < len(t[2])):
            errs.append((n, 'tap %d com linha/resposta inválida' % i))
    for p in sp['swap'][1]:
        if len(p[1]) != 3 or len(p[2]) != 3:
            errs.append((n, 'swap precisa de 3x3'))
    if not re.fullmatch(r"[\s.,!?¡¿:;…。！？、]*", sp['swap'][1][0][3] or ''):
        errs.append((n, 'swap end inválido'))
    return errs


if __name__ == '__main__':
    pass
