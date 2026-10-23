#!/usr/bin/env python3
"""Gera os ESQUELETOS dos episódios de inglês regular que ainda não estão no modelo piloto.
Saída: data/skel/en-<nível>.json (o app não lê) + docs/esqueletos/en-<nível>.md.
Cada esqueleto planeja os 19 quadros do modelo piloto a partir do conteúdo do episódio (obra, cena, vocabulário, gramática)."""
import sys, os, re, json
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools/audit')); sys.path.insert(0, os.path.join(ROOT, 'tools/gram'))
from en_audit import load
from syllabus import S
LV = ['en-a1', 'en-a2', 'en-b1', 'en-b2', 'en-c1', 'en-c2']
VERBS = set('run walk go come eat drink sleep wake work play study read write speak talk say tell ask answer call help buy sell pay cook clean wash open close take give bring send get make do have see watch look listen hear feel think know learn teach meet visit travel drive ride fly swim jump climb carry hold carry build break fix change choose decide plan try start stop finish wait stay leave arrive return find lose win share borrow lend order book check join invite offer accept refuse agree explain describe compare discuss argue suggest recommend avoid manage achieve improve develop create design produce launch invest save spend earn owe claim apply attend perform deliver negotiate persuade convince inspire challenge confront resolve overcome embrace pursue'.split())
SOUND = [  # (regex nas palavras do vocabulário, tema do laboratório de sons)
 (r'^(th)|th', 'o “th”: língua entre os dentes (think × sink)'), (r'^r|rr', 'o “r” inglês (right × light)'),
 (r'ed$', 'o final “-ed”: /t/, /d/ ou /id/'), (r's$', 'o final “-s”: /s/, /z/ ou /iz/'),
 (r'ee|ea|ie', 'vogal longa × curta (sheep × ship)'), (r'^h', 'o “h” aspirado'),
 (r'ough|augh', '“ough”: sete sons para as mesmas letras'), (r'tion|sion', 'o final “-tion” (/shn/)'),
 (r'^w|wh', 'o “w” (west × vest)'), (r'ch|sh', '“ch” × “sh” (chip × ship)'), (r'^(sp|st|sk)', 'encontros s+consoante no início'),
 (r'ng|nk', 'o final “-ng”'), (r'oo', '“oo” longo × curto (food × good)'), (r'ight', 'o “-ight” mudo')]
def sound(words):
    for rx, t in SOUND:
        if any(re.search(rx, w.lower()) for w in words): return t
    return 'ritmo e acento da frase (palavras fortes × fracas)'
def verbs_of(vs):
    c = [w for w in vs if w.lower() in VERBS or w.lower().split()[0] in VERBS]
    return c

def pair_of(it, x, by):
    o = x.get('xn') or x.get('xof')
    return by.get(o)


def choices(x, mate):
    """Escolhas já existentes nos dados do par (principal + continuação): 4 verbos e até 4 expressões. Nada é inventado."""
    fr = list(x['fr']) + (list(mate['fr']) if mate else [])
    verbs, seen = [], set()
    for f in fr:
        if f['k'] in ('verbs', 'vplay'):
            for i in f.get('items') or []:
                v = (i.get('v') or '').strip()
                if v and v.lower() not in seen:
                    seen.add(v.lower()); verbs.append([v, i.get('pt') or ''])
    exps, seen = [], set()
    def add(a, b):
        a = re.sub(r'\*\*|\{\{|\}\}', '', str(a or '')).strip()
        if a and a.lower() not in seen:
            seen.add(a.lower()); exps.append([a, b or ''])
    for f in fr:
        if f['k'] == 'cexp':
            for i in f.get('items') or []: add(i.get('x') or i.get('en'), i.get('pt'))
    for f in fr:
        if f['k'] == 'lexpack':
            for i in f.get('items') or []: add(i.get('en'), i.get('pt'))
    for l in (x.get('lx') or []) + ((mate or {}).get('lx') or []):
        add(l[0] if isinstance(l, (list, tuple)) else l, '')
    return verbs[:4], exps[:4]


def load_level(c):
    it = sorted(load(c), key=lambda x: x['o'])
    return it
def struct(c, x):
    t = ((x.get('g') or {}).get('t', '')).strip()
    for sid, a, b, mn, rx, can, fn in S[c]:
        if x.get('regram') and can == t: return sid, can, fn
    return None, t, x.get('fn') or ''
def build():
    gi = 0; all_out = {}; off = {}; acc = 0
    for l in LV: off[l] = acc; acc += len(load(l))
    for c in LV:
        it = load_level(c); out = []
        names = {x['n']: x for x in it}
        by = names
        last_pilot = max([i for i, x in enumerate(it) if x.get('pilot')], default=-1)
        for i, x in enumerate(it):
            gi_ = off[c] + i + 1
            if x.get('pilot') or i <= last_pilot or (c == 'en-a1' and i < 51): continue
            ws = [w[0] for w in x.get('v') or []]
            sid, gt, fn = struct(c, x)
            role = 'continuação' if x.get('xof') else 'principal'
            prev = it[i - 1] if i else None
            nxt = it[i + 1] if i + 1 < len(it) else None
            ob = x.get('a') or {}; h = x.get('h') or {}
            mate = pair_of(it, x, by)
            vb4, ex4 = choices(x, mate)
            vb = [v[0] for v in vb4]
            vlist = ', '.join('%s (%s)' % (v[0], v[1]) if v[1] else v[0] for v in vb4) or 'sem verbo no esqueleto original'
            elist = '; '.join('«%s»%s' % (e[0], (' (%s)' % e[1]) if e[1] else '') for e in ex4) or 'sem expressão no esqueleto original'
            wlist = ', '.join('%s (%s)' % (w[0], w[1]) for w in (x.get('v') or []))
            obra = '%s (%s, %s)' % (ob.get('w'), ob.get('k'), ob.get('y'))
            fr = [
             ('cover', 'Capa: obra %s; gancho «%s» (%s); subtítulo: %s em 10 minutos.' % (obra, h.get('l'), h.get('tr'), gt)),
             ('review', 'Mochila do episódio anterior: «%s» → recap das 3 frases-chave, bolsos Padrão/Palavras/Expressões; fecha com «Hoje: **%s**».' % (prev and prev['t'], gt)),
             ('hotscene', 'Cena clicável (cenário %s). Palavras da cena: %s.' % (x.get('rs') or x.get('sc'), wlist)),
             ('pgscene', 'Cena da obra com %s: 6–8 falas no cenário, usando «%s» e %s.' % (ob.get('w'), h.get('l'), gt.split(':')[0])),
             ('pgsheet', 'Você entendeu? 4 perguntas de compreensão da cena.'),
             ('pgrule', 'Regra: %s — forma, exemplo com a obra, pergunta de checagem.' % gt),
             ('pgmold', 'Molde de frases: peças de %s (sujeito/auxiliar/verbo/complemento) com 6 combinações.' % gt.split(':')[0]),
             ('pgsheet', 'Palavras da cena: %s.' % ', '.join(ws)),
             ('verbs', 'Verbos escolhidos: %s.' % vlist),
             ('vplay', 'Mesmos verbos: %s.' % ', '.join(vb) if vb else 'Mesmos verbos do quadro anterior.'),
             ('pgexp', 'Expressões escolhidas: %s.' % elist),
             ('pgscene', 'Na conversa de verdade: as mesmas expressões em uso: %s.' % '; '.join('«%s»' % e[0] for e in ex4)),
             ('pgsheet', 'Complete as falas com %s.' % gt.split(':')[0]),
             ('pgsheet', 'Qual está certa? Pares certo × errado do erro típico de brasileiros em %s.' % gt.split(':')[0]),
             ('pglab', 'Laboratório de sons: %s; pares mínimos, frase-modelo com «%s».' % (sound(ws), h.get('l'))),
             ('pgsheet', 'Caça-sons: ouvir e tocar a palavra.'),
             ('pgspeak', 'Sua vez de falar: %s e 3 frases do episódio.' % h.get('l')),
             ('pgmission', 'Missões: (1) cena da obra, (2) situação real — %s, (3) criar frase com %s.' % (fn or x.get('s'), gt.split(':')[0])),
             ('wrap', 'Para levar: recap + selo «%s»; teaser: %s.' % (ob.get('w'), nxt and ('%s — %s' % (nxt['t'], (nxt.get('g') or {}).get('t'))) or 'fim do nível')),
            ]
            out.append({'ep': gi_, 'n': x['n'], 'o': x['o'], 'papel': role, 'par': x.get('xn') or x.get('xof'),
                        'titulo': x['t'], 'tema': x.get('s'), 'obra': obra, 'cenario': x.get('rs') or x.get('sc'),
                        'gramatica': {'id': sid, 'estrutura': gt, 'funcao': fn},
                        'vocabulario': ws, 'vocabulario_pt': [[w[0], w[1]] for w in (x.get('v') or [])], 'verbos': vb4, 'expressoes': ex4, 'status': 'esqueleto', 'frase_gancho': [h.get('l'), h.get('tr')],
                        'quadros': [{'k': k, 'plano': p} for k, p in fr]})
        all_out[c] = out
    return all_out
def main():
    allo = build(); os.makedirs(os.path.join(ROOT, 'docs/esqueletos'), exist_ok=True)
    tot = 0
    for c, out in allo.items():
        json.dump(out, open(os.path.join(ROOT, 'data/skel/%s.json' % c), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        L = ['# Esqueletos — %s (%d episódios)\n' % (c, len(out)),
             'Só identificação das escolhas (nada foi escrito): estrutura gramatical, vocabulário da cena, 4 verbos e expressões vindos dos dados do episódio.\n',
             '| ep | título | estrutura gramatical | vocabulário (palavras da cena) | 4 verbos | expressões |', '|---|---|---|---|---|---|']
        for e in out:
            L.append('| %d | %s | %s | %s | %s | %s |' % (e['ep'], e['titulo'], e['gramatica']['estrutura'], ', '.join(e['vocabulario']),
                                                       ', '.join(v[0] for v in e['verbos']) or '—', '; '.join(x[0] for x in e['expressoes']) or '—'))
        open(os.path.join(ROOT, 'docs/esqueletos/%s.md' % c), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
        v4 = sum(1 for e in out if len(e['verbos']) == 4); e4 = sum(1 for e in out if len(e['expressoes']) >= 3)
        print(c, len(out), '| 4 verbos:', v4, '| ≥3 expressões:', e4)
        tot += len(out)
    print('total', tot)
    status = ['# Situação dos 3.000 episódios de inglês regular\n', '| nível | episódios | prontos (modelo piloto) | em produção (formato antigo) | esqueleto (a fazer) |', '|---|---|---|---|---|']
    off = 0
    for c in LV:
        it = load_level(c); n = len(it)
        pil = [i + 1 + off for i, x in enumerate(it) if x.get('pilot')]
        sk = len(allo[c])
        prod = (51 - 5 - 25) if False else 0
        status.append('| %s | %d | %d | %s | %d |' % (c, n, len(pil), '85 (eps 6–51 e 77–115, formato antigo, não mexidos)' if c == 'en-a1' else '0', sk))
        off += n
    open(os.path.join(ROOT, 'docs/esqueletos/SITUACAO.md'), 'w', encoding='utf-8').write('\n'.join(status) + '\n')


if __name__ == '__main__': main()
