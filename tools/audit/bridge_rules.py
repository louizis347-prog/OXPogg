"""Regras da PONTE obra↔episódio (parte da trava de qualidade dos cursos regulares). Padrão: docs/PADRAO_PONTE_OBRA.md.
bridge_failures(episode) -> lista de mensagens de falha (vazia = ponte ok). Só vale para episódios marcados regular-pilot-v1;
os 4 episódios de referência do inglês A1 (modelo do padrão) ficam de fora."""
import json, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'tools', 'plan'))
import plan_lib as P

REF = set()  # os 4 episódios de referência do A1 também seguem a ponte (atualizados)
GEN = {'woman', 'man', 'girl', 'boy', 'mother', 'father', 'teacher', 'student', 'friend', 'customer', 'waiter', 'clerk', 'lady', 'guy', 'person',
       'mulher', 'homem', 'mujer', 'hombre', 'chica', 'chico', 'femme', 'homme'}
STOP = {'the', 'and', 'with', 'from', 'that', 'this', 'filme', 'livro', 'série', 'serie', 'peça', 'poema', 'música', 'musica', 'quadro', 'jogo', 'uma', 'esta', 'este',
        'essa', 'esse', 'aula', 'cena', 'onde', 'como', 'para', 'sobre', 'mais', 'muito', 'entre', 'depois', 'antes', 'quando', 'também', 'tambem', 'ainda', 'cada', 'seus',
        'suas', 'dele', 'dela', 'obra', 'história', 'historia', 'sendo', 'pelo', 'pela', 'foram', 'desde', 'após'}
fold = P.fold


def _toks(s, mn=4):
    return {t for t in fold(s).split() if len(t) >= mn and t not in STOP}


def _caps(s):
    return {fold(t) for t in re.findall(r"\b[A-ZÀ-Ý][\wÀ-ÿ'’-]{3,}", s or '')} - STOP


def bridge_failures(e):
    if e.get('n') in REF or e.get('presentation') != 'regular-pilot-v1':
        return []
    fr = {}
    for f in e.get('fr', []):
        fr.setdefault(f['k'], []).append(f)
    a = e.get('a') or {}
    w = a.get('w', '')
    title = re.sub(r'\(.*?\)', '', w)
    words = _toks(title) | _caps(a.get('d', '')) | _toks((e.get('h') or {}).get('src', ''))
    sc = fr.get('pgscene') or []
    cast = list((sc[0].get('cast') or {}).keys()) if sc else []
    castn = {fold(c) for c in cast}
    st = ((fr.get('wrap') or [{}])[0].get('sticker')) or {}
    obra_txt = fold(w + ' ' + a.get('d', '') + ' ' + (e.get('h') or {}).get('src', '') + ' ' + json.dumps(st, ensure_ascii=False))
    cast_obra = {c for c in castn if c and c in obra_txt}
    lines = fold(' '.join(l[1] for s in sc for l in s.get('lines', [])))
    out = []
    if not any(t in lines for t in (words | cast_obra) if len(t) >= 4):
        out.append('ponte: nenhuma fala das cenas cita a obra ou um personagem dela')
    ms = (fr.get('pgmission') or [{}])[0].get('missions') or [{}]
    m0d = ms[0].get('data', {})
    mtxt = fold(str(m0d.get('prompt', '')) + ' ' + str(m0d.get('model', '')))   # só a tarefa e o modelo da 1ª missão (“Cena da obra”) contam
    if not (fold(ms[0].get('name', '')) == 'cena da obra' and (any(c in mtxt for c in cast_obra) or any(t in mtxt for t in words))):
        out.append('ponte: a missão “Cena da obra” (1ª missão) não cita a obra ou um personagem dela')
    g = (fr.get('cover') or [{}])[0].get('gancho')
    if not (g and P.norm((e.get('h') or {}).get('src')) == P.norm(title)):
        out.append('ponte: o gancho da capa não é da obra do episódio')
    if not (st.get('chars') and P.norm(title) in P.norm(st.get('sub', '') + ' ' + st.get('title', ''))):
        out.append('ponte: a figurinha do fechamento não mostra a obra')
    if len(a.get('d', '')) < 90:
        out.append('ponte: descrição da obra ausente ou curta (mín. 90 caracteres)')
    if castn & GEN:
        out.append('ponte: elenco genérico (Woman/Man/…): use personagens da obra')
    rss = [f.get('rs') for f in e.get('fr', []) if f.get('rs')]
    if any(x == y == z for x, y, z in zip(rss, rss[1:], rss[2:])):
        out.append('ponte: o mesmo cenário em 3 quadros seguidos')
    return out
