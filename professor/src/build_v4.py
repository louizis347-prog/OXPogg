#!/usr/bin/env python3
"""Monta as aulas Quest (data/v4/NNN.json) = aula Real-Life (data/v3/NNN.json) + suplemento (src/supp/sNNN.py → SUPP).
Uso: python3 src/build_v4.py 3 [4 5 …]   |   python3 src/build_v4.py --all   (todas as aulas que têm suplemento)"""
import glob, importlib.util, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
sys.path.insert(0, HERE)
CH = {'mission': ('🏁', 'Mission', '#0e1b3d'), 'culture': ('🌍', 'Culture', '#2da44e'), 'read': ('📖', 'Reading quest', '#00a6a6'), 'talk': ('💬', 'Conversation', '#2f6fe0'), 'lab': ('🧩', 'Language lab', '#7a3fe0'),
      'arcade': ('🎮', 'Practice arcade', '#f2b01e'), 'boss': ('⚔️', 'Boss mission', '#e8438f'), 'write': ('✍️', 'Writing & feedback', '#4a4fd8'), 'wrap': ('🏆', 'Mission complete', '#e5484d')}
MIN = {'solo': dict(mission=4, culture=5, read=8, talk=10, lab=9, arcade=8, boss=9, write=5, wrap=2), 'group': dict(mission=5, culture=5, read=7, talk=9, lab=8, arcade=6, boss=14, write=4, wrap=2)}
DESC = {'mission': 'Missão, aquecimento e retomada.', 'culture': 'Cultura aprofundada: fatos, mito ou verdade, vida real e comparação.', 'read': 'Leitura densa com tarefas de skim, scan, verdadeiro/falso, ordem e contexto.', 'talk': 'Escuta, diálogo e escolha da resposta natural.',
        'lab': 'Chunks, padrões com troca de palavras e pronúncia.', 'arcade': 'Prática guiada e mini-jogos com combo.', 'boss': 'Chefe da fase: roleplay, rodízio ou missão em grupo.', 'write': 'Escrita curta, devolutiva e rubrica.', 'wrap': 'Exit ticket, medalha, figurinha e próxima parada.'}
CHAP = {'q_cover': 'mission', 'rl_warm': 'mission', 'q_culture': 'culture', 'q_read': 'read', 'rl_listen': 'talk', 'rl_dialog': 'talk', 'q_choose': 'talk', 'rl_chunks': 'lab', 'rl_patterns': 'lab', 'rl_pron': 'lab',
        'rl_challenge': 'arcade', 'q_arcade': 'arcade', 'rl_role': 'boss', 'rl_lab': 'boss', 'rl_mission': 'boss', 'rl_write': 'write', 'rl_feedback': 'write', 'rl_exit': 'wrap', 'rl_levels': 'wrap', 'q_wrap': 'wrap'}
ORDER = ['q_cover', 'rl_warm', 'q_culture', 'q_read', 'rl_listen', 'rl_dialog', 'q_choose', 'rl_chunks', 'rl_patterns', 'rl_pron', 'rl_challenge', 'q_arcade', 'rl_role', 'rl_lab', 'rl_mission', 'rl_write', 'rl_feedback', 'rl_exit', 'rl_levels', 'q_wrap']


def load_supp(n):
    f = os.path.join(HERE, 'supp', 's%03d.py' % n)
    spec = importlib.util.spec_from_file_location('s%03d' % n, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.SUPP


def build(n):
    L = json.load(open(os.path.join(ROOT, 'data', 'v3', '%03d.json' % n), encoding='utf-8')); S = load_supp(n)
    P = {p['t']: p for p in L['pages']}
    pages = {}
    o = dict(P['rl_open']); o['t'] = 'q_cover'; pages['q_cover'] = o
    for t in ('rl_warm', 'rl_listen', 'rl_dialog', 'rl_chunks', 'rl_patterns', 'rl_pron', 'rl_challenge', 'rl_role', 'rl_lab', 'rl_mission', 'rl_write', 'rl_feedback', 'rl_exit', 'rl_levels'):
        if t in P: pages[t] = P[t]
    c = dict(S['culture']); c['t'] = 'q_culture'; c['title'] = c.get('title') or 'Cultural spotlight'; c.setdefault('teach', {'goal': 'Cultura de verdade: o que as pessoas fazem, dizem e esperam nessa situação.'}); pages['q_culture'] = c
    r = dict(S['reading']); r['t'] = 'q_read'; r['title_page'] = r.get('title'); r['title'] = 'Reading quest'; pages['q_read'] = r
    r['title'] = 'Reading quest — ' + (r.get('title_page') or '')
    ch = dict(S['convo']); ch['t'] = 'q_choose'; ch['title'] = 'Choose your reply'; pages['q_choose'] = ch
    a = {'t': 'q_arcade', 'title': 'Practice arcade', 'games': S['arcade']}; pages['q_arcade'] = a
    w = {'t': 'q_wrap', 'title': 'Mission complete', 'homework': S.get('homework', ''), 'next': S.get('next')}; pages['q_wrap'] = w
    out = []
    for t in ORDER:
        if t not in pages: continue
        p = dict(pages[t]); p['stage'] = CHAP[t]
        if t in ('rl_role',): p['for'] = 'solo'
        if t in ('rl_lab', 'rl_mission'): p['for'] = 'group'
        out.append(p)
    plan = {m: [dict(id=k, name=CH[k][1], ic=CH[k][0], c=CH[k][2], min=MIN[m][k], desc=DESC[k]) for k in CH] for m in MIN}
    LL = dict(L); LL.update(pages=out, plan=plan, badge=S['badge'], sticker=S['sticker'], fmt='quest')
    os.makedirs(os.path.join(ROOT, 'data', 'v4'), exist_ok=True)
    f = os.path.join(ROOT, 'data', 'v4', '%03d.json' % n)
    json.dump(LL, open(f, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    return f


if __name__ == '__main__':
    a = sys.argv[1:]
    ns = sorted(int(os.path.basename(f)[1:4]) for f in glob.glob(os.path.join(HERE, 'supp', 's[0-9][0-9][0-9].py'))) if '--all' in a else [int(x) for x in a]
    for n in ns: print('ok', build(n))
