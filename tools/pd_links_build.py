#!/usr/bin/env python3
"""Gera professor/data/pd_links.json: liga cada aula ao vivo do Painel a mini lições do PoggloDict (antes/depois da aula),
com palavras já vistas e um aquecimento (perguntas tiradas dos mini-quizzes do PoggloDict).
Uso: python3 tools/pd_links_build.py   (precisa de node; lê poglodict/english-a1-*.js; veja docs/PAINEL_POGLODICT.md)
O mapa LINKS é editável: aula do Painel -> lições do PoggloDict (nº da lição A1)."""
import json, os, random
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import subprocess
SEL = json.loads(subprocess.run(['node', os.path.join(ROOT, 'tools', 'pd_sel_export.js')], capture_output=True, text=True, check=True).stdout)
# aula do Painel: antes (preparação), depois (revisão), lacuna (o que o PoggloDict ainda não cobre), prof (dica para o professor)
LINKS = {
 1: dict(antes={3: 'Pedir no balcão com Can I…?', 7: 'I would like… e to go: o pedido educado', 5: 'Quantidades: two rolls, two muffins', 27: 'Perguntar se pode pagar com cartão'},
         depois=[4, 50], lacuna='', prof='Se a turma fez as lições 3 e 7, passe depressa por “Palavras em ação” e gaste o tempo no molde e na conversa.'),
 1001: dict(antes={4: 'A / an com pedidos de comida', 10: 'Some com água e líquidos', 7: 'I would like… para pedir com cortesia', 34: 'Do you like…? para falar de gosto'},
            depois=[111, 25], lacuna='', prof='Quem fez a 4 já conhece “a / an”; foque em “What kind of bread?” e “No onions, please.”, que são do Painel.'),
 2: dict(antes={5: 'Plural com -s: four mangoes', 60: 'Feira: tomato, carrot, fresh fruit', 191: 'How much…? para perguntar o preço', 192: 'How many…? com plural contável'},
         depois=[54, 193], lacuna='', prof='Os números e o dinheiro são do Painel; o PoggloDict já deu plural, How much e How many.'),
 1002: dict(antes={54: 'Do / does no supermercado', 19: 'Ler placas e instruções', 193: 'Some e any na despensa', 197: 'Is there any…? ao procurar um produto'},
            depois=[60, 192], lacuna='', prof='“Where can I find…?” e “What does that sign say?” são o centro da aula; o resto já foi visto.'),
 3: dict(antes={1: 'Am, is e are para se apresentar', 12: 'There are: apresentar a vizinhança', 14: 'In, near e on: onde eu moro'},
         depois=[209, 1], lacuna='', prof='Comece pelos alunos se apresentando com a estrutura da lição 1 e deixe a vizinhança para a oficina.'),
 1003: dict(antes={1: 'Am, is e are em apresentações', 49: 'This is… e Who is…?', 282: 'Thank you e You are welcome'},
            depois=[1, 49], lacuna='Profissões e cargos (designer, team member): o PoggloDict ainda não tem lição só sobre isso.', prof='Para “What’s your role?”, apresente o vocabulário de trabalho na própria aula.'),
 4: dict(antes={18: 'Escrever o nome com please', 44: 'Recados e número de telefone', 49: 'Ligar e confirmar quem é', 328: 'Preencher dados: What is your…?'},
         depois=[65, 44], lacuna='Soletrar com o alfabeto (d-a-n-i-e-l): o PoggloDict ainda não tem lição sobre as letras.', prof='Dedique os primeiros 10 min ao alfabeto, porque a prévia do PoggloDict não cobre as letras.'),
 1004: dict(antes={11: 'Biblioteca: pedir um cartão', 14: 'Onde eu moro: endereço e bairro', 40: 'Dar o nome numa reserva', 328: 'Formulário: What is your…?'},
            depois=[65, 328], lacuna='Soletrar endereço e dizer números de apartamento.', prof='Reforce números e a fala “Can you spell that, please?”.'),
 5: dict(antes={1: 'I’m from… e apresentações', 12: 'Apresentar um lugar: There are', 14: 'Onde eu moro: in, near, on'},
         depois=[14, 341], lacuna='Países e nacionalidades (American, Brazilian): sem lição própria ainda.', prof='A lista de países e nacionalidades precisa ser dada na aula.'),
 1005: dict(antes={14: 'Falar de onde eu moro', 20: 'Descrever uma cidade: adjetivo + substantivo', 30: 'Praia: want to + verbo', 125: 'Perguntar sobre uma viagem'},
            depois=[20, 30], lacuna='', prof='O foco do Painel é “What’s it like there?”; o PoggloDict já preparou os adjetivos.'),
}
rnd = random.Random(7)
def quiz_items(nums):
    out = []
    for n in nums:
        s = SEL.get(str(n))
        if not s: continue
        item = None
        for it in (s.get('quiz') or []):
            if it.get('t') == 'c': item = it; break
        if item:
            opts = list(item['o']); correct = opts[0]; rnd.shuffle(opts)
            out.append(dict(q=item['q'], opts=opts, ans=opts.index(correct), why=(item.get('why') or '') + ' · ' + (item.get('pt') or '')))
        elif s.get('gr'):
            g = s['gr']; opts = [g[1], g[2]]; rnd.shuffle(opts)
            out.append(dict(q=g[0], opts=opts, ans=opts.index(g[1]), why=(g[4] or '') + ' · ' + (g[3] or '')))
    return out
res = {}
for aula, e in LINKS.items():
    antes = []
    for n, why in e['antes'].items():
        s = SEL[str(n)]; antes.append(dict(n=n, t=s['t'], g=s['g'], w=s['w'][:4], why=why))
    depois = []
    for n in e['depois']:
        s = SEL[str(n)]; depois.append(dict(n=n, t=s['t'], g=s['g'], w=s['w'][:4], why='Revise antes da próxima aula'))
    words = []
    for a in antes:
        for w in a['w']:
            if w not in words: words.append(w)
    res[str(aula)] = dict(antes=antes, depois=depois, quiz=quiz_items(list(e['antes'])[:5]), words=words[:12], lacuna=e['lacuna'], prof=e['prof'])
json.dump(res, open(os.path.join(ROOT, 'professor', 'data', 'pd_links.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('aulas ligadas:', len(res), '| perguntas de aquecimento:', sum(len(v['quiz']) for v in res.values()))
