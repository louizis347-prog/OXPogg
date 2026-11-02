#!/usr/bin/env python3
"""Utilitários comuns das aulas Real-Life (professor/src/lessons/lNNN.py): plano de 60 minutos, teach() e gravação do JSON."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
PLAN = {
 'solo': [
  dict(id='warm', name='Connection & warm-up', min=5, c='#e8438f', desc='Conversa espontânea e retomada da aula anterior, sem prova de gramática.'),
  dict(id='immersion', name='Real-life immersion', min=7, c='#00a6a6', desc='Cenário, cultura e compreensão inicial: entender a situação antes de analisar regras.'),
  dict(id='notice', name='Notice the language', min=8, c='#f08a2b', desc='Diálogo, expressões funcionais e descoberta de quando cada uma é usada.'),
  dict(id='gram', name='Grammar & pronunciation', min=10, c='#7a3fe0', desc='Padrões presentes no diálogo e um único fenômeno de pronúncia.'),
  dict(id='practice', name='Controlled → guided practice', min=9, c='#f2b01e', desc='Completar, substituir, transformar, responder e escolher a resposta adequada.'),
  dict(id='speak1', name='Personalized roleplay', min=11, c='#e8438f', desc='Situação-problema ligada à vida do estudante, repetida com menos apoio.'),
  dict(id='write', name='Writing & feedback', min=7, c='#4a4fd8', desc='Mensagem curta e correção de 2–3 prioridades, com forma mais natural.'),
  dict(id='exit', name='Exit ticket & homework', min=3, c='#e5484d', desc='Três competências sem consulta e missão de casa.')],
 'group': [
  dict(id='warm', name='Social warm-up', min=6, c='#e8438f', desc='Perguntas rápidas com participação de todos.'),
  dict(id='immersion', name='Cultural immersion', min=7, c='#00a6a6', desc='Cena e discussão coletiva.'),
  dict(id='notice', name='Language discovery', min=8, c='#f08a2b', desc='Diálogo, expressões e identificação de padrões.'),
  dict(id='gram', name='Grammar & pronunciation', min=9, c='#7a3fe0', desc='Explicação curta e prática em pares.'),
  dict(id='speak1', name='Communication lab', min=11, c='#e8438f', desc='Rodadas de conversa com troca de parceiros.'),
  dict(id='speak2', name='Group mission', min=11, c='#2f6fe0', desc='Simulação com objetivo e problema a resolver.'),
  dict(id='write', name='Writing & feedback', min=5, c='#4a4fd8', desc='Produção individual, comparação e correção.'),
  dict(id='exit', name='Exit challenge', min=3, c='#e5484d', desc='Verificação individual e tarefa de continuidade.')]}


def teach(**k):
    return k

def finish(L):
    """Normaliza chaves reservadas do Python (for_ → for, frm → from) e grava data/v3/NNN.json."""
    for pg in L['pages']:
        if 'for_' in pg:
            pg['for'] = pg.pop('for_')
        for lv in pg.get('levels', []):
            for it in lv.get('items', []):
                if 'frm' in it:
                    it['from'] = it.pop('frm')
    os.makedirs(os.path.join(ROOT, 'data', 'v3'), exist_ok=True)
    out = os.path.join(ROOT, 'data', 'v3', '%03d.json' % L['n'])
    json.dump(L, open(out, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    return out
