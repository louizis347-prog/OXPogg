# Atalho de autoria para os episódios B1 491–530 (modelo piloto): recebe os campos escritos à mão em forma compacta
# e monta a chamada de S() (tools/v3/b1h.py). Não começa com b1_ para não ser carregado como módulo de episódios.
import re
from v3.b1h import S

# título de cada episódio na ordem do curso (a vinheta de "próximo" aponta para o seguinte)
ORDER = [(82324, 'Cleaning Day'), (7082324, 'Faxina e tarefas'), (82325, 'Fashion and Style'), (7082325, 'Moda e estilo'),
         (930070, 'Point Out, Sum Up'), (7930070, 'Apresentar ideias'), (82329, 'Review: Past Tenses'), (7082329, 'Revisão do passado'),
         (930071, 'Cost an Arm and a Leg'), (7930071, 'Dinheiro e preços'), (82335, 'Review: Deduction and Advice'), (7082335, 'Dedução e conselho'),
         (930072, 'Hopes and Fears'), (7930072, 'Esperanças e medos'), (82340, 'Real Conversation 4'), (7082340, 'Conversa de viagem'),
         (82341, 'Reading Skills'), (7082341, 'Estratégias de leitura'), (930073, 'Rely On, Count On'), (7930073, 'Contar com alguém'),
         (82342, 'Listening Skills'), (7082342, 'Estratégias de escuta'), (82343, 'Speaking Fluently'), (7082343, 'Falar com fluência'),
         (82344, 'Writing Skills'), (7082344, 'Escrever com clareza'), (82345, 'Pronunciation Tips'), (7082345, 'Dicas de pronúncia'),
         (930074, 'Shopping and Returns'), (7930074, 'Trocas e devoluções'), (81278, 'Word Formation'), (7081278, 'Palavras novas'),
         (82347, 'Learning from Mistakes'), (7082347, 'Aprender com erros'), (82349, 'Looking Back'), (7082349, 'Olhar para trás'),
         (82350, 'Moving Up to B2'), (7082350, 'Rumo ao B2'), (930075, 'Say It Better'), (7930075, 'Diga melhor')]
NEXT = {a[0]: b[1] for a, b in zip(ORDER, ORDER[1:])}
OTHER = ['street', 'hall', 'lobby1', 'cafe2', 'living', 'park', 'office', 'home1', 'kitchen', 'school', 'yard', 'lake', 'shop', 'diner']


def _rx(key):
    return r'\b' + r'\s+'.join(re.escape(p).replace("'", "['’]") for p in key.split()) + r'\b'


def mission(ic, name, desc, prompt, sents):
    """sents = [(emoji, trecho-chave, frase em inglês, tradução)] x3 -> tupla de missão de b1h.S"""
    model = ' '.join(s[2] for s in sents)
    items = [('Usei %s?' % s[1], _rx(s[1]), s[2], s[3], s[1].split()[0].capitalize() + '! ' + s[0]) for s in sents]
    return (ic, name, desc, prompt, sents[0][1], model, items)


def EP(n, title, sub, gs, why, names, ids, rs, obra, cover, rule, fm, vocab, lab, verbs, mold, prod, m2, hot, gaps, traps, lines,
       quiz, exps, fill):
    voc = [(v[0], v[1], v[2], 'Soa como “%s”.' % v[3]) for v in vocab]
    a, b = names
    ln = [[a if i % 2 == 0 else b, x[0], x[1]] for i, x in enumerate(lines)]
    nxt = NEXT.get(n)
    teaser = ('Mais episódios', ('Próximo: ' + nxt) if nxt else 'Próximo: novo nível')
    scenes = [rs] + [s for s in OTHER if s != rs][:5]
    return S(n=n, title=title, sub=sub, pattern=gs, why=why, names=names, ids=ids, rs=rs, obra=obra, hot=hot, gaps=gaps,
             traps=traps, rule=rule, fm=fm, cover=cover, vocab=voc, lines=ln, quiz=quiz, teaser=teaser, exps=exps, lab=lab,
             verbs=verbs, mold=mold, prod=prod, m2=m2, scenes=scenes, fill=fill)


def third(v):
    if re.search(r'(s|sh|ch|x|z|o)$', v):
        return v + 'es', 'es'
    if re.search(r'[^aeiou]y$', v):
        return v[:-1] + 'ies', 'ies'
    return v + 's', 's'


def V(v, ic, pt, eu, eu_pt, ele):
    """Verbo: eu = frase com o verbo no infinitivo; ele = a frase com he/she e o verbo na 3ª pessoa (o sufixo é destacado)."""
    full, suf = third(v)
    base = full[:-len(suf)]
    assert full in ele, (v, ele)
    ele_b = ele.replace(full, base + '**' + suf + '**', 1)
    return (v, ic, pt, eu, ele_b, eu, eu_pt, '**%s** = %s. Com he/she: **%s**.' % (v, pt, full))
