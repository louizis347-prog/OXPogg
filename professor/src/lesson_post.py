"""Pós-processamento comum às aulas Quest (1–50): mochila de revisão no começo, leitura guiada com tradução, laboratório de sons completo,
cartões de cultura, "sem consultar" lúdico, tema de fundo e aula única (sem distinção particular/grupo)."""
import re

TINT = {'cafe': ('#fdf3e4', '#f3dfc4'), 'cafe2': ('#fdf3e4', '#f3dfc4'), 'cafe3': ('#fdf3e4', '#f3dfc4'), 'bakery': ('#fdf3e4', '#f3dfc4'), 'diner': ('#fdeee6', '#f4d6c8'), 'restaurant': ('#fbeee8', '#f2d7cc'),
        'market': ('#f1f7e8', '#e0efcf'), 'supermarket': ('#f1f7e8', '#e0efcf'), 'shop': ('#f6f0fa', '#e7dcf2'), 'street': ('#eaf3fb', '#d6e6f5'), 'busstop': ('#eaf3fb', '#d6e6f5'), 'station': ('#eaf3fb', '#d6e6f5'),
        'subway': ('#eaf3fb', '#d6e6f5'), 'sub2': ('#eaf3fb', '#d6e6f5'), 'airport': ('#eaf3fb', '#d6e6f5'), 'park': ('#eef7ea', '#d8ecd0'), 'park2': ('#eef7ea', '#d8ecd0'), 'living': ('#fdf1e6', '#f3dcc3'), 'home1': ('#fdf1e6', '#f3dcc3'),
        'kitchen': ('#fdf1e6', '#f3dcc3'), 'office': ('#eceff7', '#d8deee'), 'bank': ('#eceff7', '#d8deee'), 'school': ('#fff6e0', '#f5e5b8'), 'lobby': ('#fbf1e4', '#efdcc0')}
FIRST_ITEMS = [('👋', 'Hello! Good morning.', 'Olá! Bom dia.'), ('🙏', 'Thank you!', 'Obrigado!'), ('🙂', 'Nice to meet you.', 'Prazer em conhecer você.')]
norm = lambda s: re.sub(r'\s+', ' ', re.sub(r'\*\*', '', s or '')).strip()

FIRST_WORDS = [('👋', 'hello', 'olá'), ('🙏', 'please', 'por favor'), ('❤️', 'thanks', 'obrigado'), ('😔', 'sorry', 'desculpe'), ('✅', 'yes', 'sim'), ('❌', 'no', 'não')]
FIRST_ITEMS = FIRST_ITEMS + [('🤝', 'How are you?', 'Como vai você?'), ('🙋', 'Excuse me, please.', 'Com licença, por favor.'), ('👋', 'See you later!', 'Até mais!')]

def post(L, n, Y, S, X, prev, vocab_emojis, Z=None):
    pages = L['pages']
    if n == 1:
        import json, os
        art1 = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lesson1_art.json'), encoding='utf-8'))
        for i, p in enumerate(pages):
            if not p.get('art') and i < len(art1): p['art'] = art1[i]
    # ---- tema de fundo
    em = [e for e in vocab_emojis if e][:6] or ['💬', '⭐', '🗣️', '📖']
    ta, tb = TINT.get(L.get('scene'), ('#eaf5f7', '#d9ecef'))
    L['theme'] = {'emojis': em, 'a': ta, 'b': tb}
    # ---- aula única: plano e roleplay iguais
    L['plan']['group'] = L['plan']['solo']
    for p in pages:
        if p.get('kind') == 'role': p['group'] = p['solo']
    # ---- leitura guiada
    src = [norm(t) for t in S['reading']['text']]
    ys = (Y or {}).get('sentences')
    if ys and len(ys) == len(src):
        for p in pages:
            if p.get('kind') == 'reading':
                p['sentences'] = [ys[src.index(norm(t))] if norm(t) in src else None for t in p['paragraphs']]
                if any(x is None for x in p['sentences']): p.pop('sentences')
    # ---- cultura: cartões ricos
    cards = (Y or {}).get('cards')
    fpages = [p for p in pages if p.get('kind') == 'facts']
    if cards and len(fpages) >= 2:
        fa, fb = fpages[0], fpages[1]; first = fa['facts'][0]
        rest = [c for c in cards if norm(c['big']).lower() != norm(first['big']).lower()]
        fa['facts'] = [first] + rest[:2]
        tail = rest[2:4] if len(rest) >= 4 else rest[2:] + [x for x in fb['facts'] if all(x['big'] != c['big'] for c in cards)][:1]
        fb['facts'] = tail or fb['facts']
    # ---- laboratório de sons completo (3 quadros)
    sl = (Y or {}).get('soundlab')
    if sl:
        out = []
        for p in pages:
            if p.get('kind') == 'sound':
                base = dict(t='q1', stage=p['stage'], art=p.get('art'), focus=sl['focus'])
                out.append(dict(base, kind='soundlab', part=1, title='Laboratório de sons · o som', what=sl['what'], how=sl['how'], tip=sl['tip'], words=sl['words']))
                out.append(dict(base, kind='soundlab', part=2, title='Laboratório de sons · ouça e escolha', pairs=sl['pairs']))
                out.append(dict(base, kind='soundlab', part=3, title='Laboratório de sons · diga você', phrase=sl['phrase'], tip=sl['tip']))
            else: out.append(p)
        pages[:] = out
    # ---- "sem consultar": jogo com molde
    oks = []
    for t in (X.get('convo') or S['convo'])['turns']:
        o = [x for x in t['opts'] if x.get('ok')][0]
        oks.append((o['pt'], o['en']))
    for p in pages:
        if p.get('kind') == 'exit':
            p['items'] = [dict(cue=pt, target=en) for pt, en in oks[1:4]] if len(oks) >= 4 else [dict(cue=pt, target=en) for pt, en in oks[:3]]
            p.pop('prompts', None); p.pop('spaced', None)
    # ---- mochila de revisão no começo (4 quadros: expressões, palavras, desafio, fale)
    if prev:
        items = [dict(e=e or '💬', en=en, pt=pt) for e, en, pt in prev['items']][:6]
        words = [dict(e=e or '💬', w=w, pt=pt) for e, w, pt in prev['words']][:6]
        qz = prev['quiz']; say = [dict(en=en, pt=pt) for en, pt in prev['say']][:3]
    else:
        items = [dict(e=e, en=en, pt=pt) for e, en, pt in FIRST_ITEMS][:6]
        words = [dict(e=e, w=w, pt=pt) for e, w, pt in FIRST_WORDS]
        say = [dict(en=en, pt=pt) for _, en, pt in FIRST_ITEMS[:3]]
        qz = [dict(q='Alguém diz “Hello! Good morning.” Você responde…', opts=['Hi! Good morning.', 'Goodbye, see you.', 'I am fine, sorry.'], ans=0, why='Respondemos o cumprimento com outro cumprimento.'),
              dict(q='Alguém ajuda você. Você diz…', opts=['Thank you!', 'See you!', 'Where is it?'], ans=0, why='Thank you! agradece a ajuda.'),
              dict(q='Você quer a atenção de alguém para perguntar algo. Você diz…', opts=['Excuse me, please.', 'Good night.', 'Nice to meet you.'], ans=0, why='Excuse me chama a atenção com educação.'),
              dict(q='Você conhece uma pessoa nova. Você diz…', opts=['Nice to meet you.', 'See you later.', 'You are welcome.'], ans=0, why='Nice to meet you é o que dizemos ao conhecer alguém.')]
    art0 = pages[0].get('art') or {}
    rev = [dict(t='q1', stage='mission', kind='review', title='Mochila · expressões', art=art0, items=items),
           dict(t='q1', stage='mission', kind='reviewwords', title='Mochila · palavras', art=art0, words=words),
           dict(t='q1', stage='mission', kind='quiz', title='Mochila · desafio', art=art0, items=qz, instruction='Antes de começar: lembre o que você já sabe.'),
           dict(t='q1', stage='mission', kind='reviewsay', title='Mochila · fale', art=art0, items=say)]
    pages[1:1] = rev
    # ---- verbos e expressões (depois do vocabulário)
    if Z:
        vi = max([i for i, p in enumerate(pages) if p.get('kind') == 'vocab'] or [len(pages) - 1]) + 1
        art = pages[vi - 1].get('art') or art0
        vs = Z['verbs']
        add = [dict(t='q1', stage='lab', kind='verbs', title='Verbos em ação · 1/2', art=art, verbs=vs[:3]),
               dict(t='q1', stage='lab', kind='verbs', title='Verbos em ação · 2/2', art=art, verbs=vs[3:]),
               dict(t='q1', stage='lab', kind='verbplay', title='Aplique os verbos', art=art, items=Z['verb_game']),
               dict(t='q1', stage='lab', kind='exprs', title='Expressões comuns', art=art, items=Z['expressions']),
               dict(t='q1', stage='lab', kind='exprplay', title='Qual expressão usar?', art=art, items=Z['expr_game'])]
        pages[vi:vi] = add
    # ---- ponte português → inglês: apresenta o vocabulário novo ANTES de ele aparecer nos textos
    vv = [v for v in (X.get('vocab') or []) if v.get('w') and v.get('pt')]
    if len(vv) >= 4:
        wi = next((i for i, p in enumerate(pages) if p.get('kind') == 'work'), 0) + 1
        art_b = pages[wi - 1].get('art') or art0
        bw = [dict(e=v.get('e') or '💬', w=v['w'], pt=v['pt'], ex=(v.get('ex') or [''])[0]) for v in vv[:6]]
        add_b = [dict(t='q1', stage='mission', kind='bridge', title='Ponte · português → inglês', art=art_b, words=bw)]
        er = [e for e in (S.get('errors') or []) if e.get('wrong') and e.get('fix')][:3]
        if len(er) >= 2:
            add_b.append(dict(t='q1', stage='mission', kind='bridge2', title='Ponte · como não traduzir', art=art_b, items=[dict(wrong=e['wrong'], fix=e['fix'], why=e.get('why', '')) for e in er]))
        pages[wi:wi] = add_b
    L['pages'] = pages
    L['fmt'] = 'quest-focus-v1'
