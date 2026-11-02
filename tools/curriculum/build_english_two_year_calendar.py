#!/usr/bin/env python3
"""Curated live anchor map from the real English Regular and Neighbors catalogues.

The calendar intentionally samples the catalogues. It does not imply that all source
episodes fit into 208 meetings. Run from the repository root.
"""
from __future__ import annotations
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'data'
DOC = ROOT / 'docs' / 'CALENDARIO-INGLES-REGULAR-NEIGHBORS-2-ANOS.md'
CSV = ROOT / 'docs' / 'CALENDARIO-INGLES-208-AULAS.csv'
BLOCKS = [
    ('Ano 1 · A1', 'a1', 0, 466, 0, 450, 20),
    ('Ano 1 · A2', 'a2', 0, 474, 0, 450, 22),
    ('Ano 1 · B1 (primeiro quarto)', 'b1', 0, 133, 0, 113, 10),
    ('Ano 2 · B1 (continuação)', 'b1', 133, 530, 113, 450, 22),
    ('Ano 2 · B2', 'b2', 0, 490, 0, 430, 28),
    ('Ano 2 · B2: projetos finais', 'b2', 490, 510, 430, 450, 2),
]
CHECKPOINTS = {10:'A1 inicial',20:'A1',31:'A2 intermediário',42:'A2',52:'B1 inicial — cerca de 1/4 do nível',64:'B1 intermediário',74:'B1',88:'B2 intermediário',102:'B2',104:'projeto final B2'}

def episodes(course: str, level: str):
    result = []
    for path in sorted(DATA.glob(f'{course}-{level}_*.json')):
        data = json.loads(path.read_text())
        for e in data if isinstance(data, list) else data.get('episodes', data.get('e', [])):
            if course == 'nb' and e['n'] >= 96000:
                continue  # arc reviews require their ten source episodes; assign separately
            result.append((e, path.relative_to(ROOT).as_posix()))
    return result

def select(start: int, end: int, index: int, total: int) -> int:
    # More contact with the first episodes at a new level, then progressively wider sampling.
    return start + round((index / (total - 1)) ** 1.4 * (end - start - 1))

def short(value, limit=66):
    value = ' '.join(str(value or '').split()).replace('|', '·')
    return value if len(value) <= limit else value[:limit - 1].rstrip() + '…'

catalog = {(course, level): episodes(course, level) for course in ('en', 'nb') for level in ('a1', 'a2', 'b1', 'b2')}
assert [len(catalog['en', level]) for level in ('a1','a2','b1','b2')] == [466, 474, 530, 510]
assert [len(catalog['nb', level]) for level in ('a1','a2','b1','b2')] == [450] * 4
rows = []
week = 0
for block, level, r0, r1, n0, n1, count in BLOCKS:
    for local_week in range(count):
        week += 1
        for j in range(2):
            slot = local_week * 2 + j
            regular, regular_file = catalog['en', level][select(r0, r1, slot, count * 2)]
            neighbor, neighbor_file = catalog['nb', level][select(n0, n1, slot, count * 2)]
            culture = regular.get('a', {}).get('w', '')
            focus = regular.get('s', regular.get('p', ''))
            situation = neighbor.get('s', neighbor.get('p', ''))
            neighbor_hook = neighbor.get('h', {}).get('l', '')
            regular_hook = regular.get('h', {}).get('l', '')
            regular_words = [str(item[0]) for item in regular.get('v', [])[:3]]
            neighbor_words = [str(item[0]) for item in neighbor.get('v', [])[:3]]
            output_turns = '6' if level in ('a1', 'a2') else '8–10'
            row = {
                'ano': 1 if week <= 52 else 2,
                'semana': week,
                'aula': 'A' if j == 0 else 'B',
                'bloco': block,
                'nivel': level.upper(),
                'regular_curso': f'en-{level}',
                'regular_id': regular['n'],
                'regular_titulo': regular.get('t', ''),
                'regular_obra': culture,
                'regular_foco': focus,
                'regular_fala_gatilho': regular_hook,
                'regular_tres_unidades': '; '.join(regular_words),
                'regular_arquivo': regular_file,
                'neighbors_curso': f'nb-{level}',
                'neighbors_id': neighbor['n'],
                'neighbors_titulo': neighbor.get('t', ''),
                'neighbors_situacao': situation,
                'neighbors_fala_gatilho': neighbor_hook,
                'neighbors_tres_unidades': '; '.join(neighbor_words),
                'neighbors_arquivo': neighbor_file,
                'missao_de_transferencia': f'Use o foco «{short(focus, 95)}» para responder a uma pessoa na situação «{short(situation, 95)}».',
                'produto_observavel': ('Diálogo de 6 turnos com uma mudança de condição e reparo de mal-entendido.' if level in ('a1','a2') else 'Interação de 8–10 turnos com justificativa, negociação e reformulação.'),
                'preparacao_professor': f'Ouvir os dois episódios; conferir a fonte de «{culture}»; escolher duas trocas naturais para «{neighbor_hook}»; prever uma resposta e um reparo.',
                'roteiro_0_8': ('Recuperar duas falas da semana anterior e pedir que o estudante diga quando as usaria.' if j == 0 else 'Sem texto na tela, recuperar a missão da aula A e uma fala que precisou de correção.'),
                'roteiro_8_20': (f'Mostrar «{culture}»; separar fato da obra, interpretação e a fala «{regular_hook}».' if j == 0 else f'Entrar na situação «{situation}»; ouvir «{neighbor_hook}» e prever a resposta.'),
                'roteiro_20_35': (f'Ler ou escutar um trecho do Regular; trabalhar {", ".join(regular_words)} e testar uma troca no padrão «{regular.get("g", {}).get("t", "")}».' if j == 0 else f'Encenar o Neighbors; substituir um elemento da fala e usar {", ".join(neighbor_words)} com pronúncia natural.'),
                'roteiro_35_55': (f'Encenar «{situation}» em {output_turns} turnos; incluir o foco do Regular e trocar os papéis.' if j == 0 else f'Reler a cena do Regular e comparar sua intenção com «{neighbor_hook}»; criar uma segunda resposta em outro contexto.'),
                'roteiro_55_68': (f'Mudar pessoa, objetivo ou informação; pedir esclarecimento e reparar o mal-entendido sem ler.' if j == 0 else f'Resolver livremente uma variação de «{situation}»; um colega questiona a escolha e o estudante a reformula.'),
                'roteiro_68_75': (f'Bilhete de saída: gravar uma fala própria e escrever três linhas sobre o que mudou na situação.' if j == 0 else f'Autoavaliar clareza e adequação; professor registra um acerto, uma correção e a próxima missão.'),
                'estudo_entre_aulas': f'Reouvir os dois âncoras; rever {", ".join(regular_words)}; registrar uma resposta nova a «{neighbor_hook}»; praticar 3 h na semana.',
                'avaliacao': CHECKPOINTS.get(week, ''),
            }
            rows.append(row)
assert len(rows) == 208 and len({(x['regular_curso'], x['regular_id']) for x in rows}) == 208
assert len({(x['neighbors_curso'], x['neighbors_id']) for x in rows}) == 208
assert all(x['nivel'] == 'B1' and x['regular_id'] in {e['n'] for e,_ in catalog['en','b1'][:133]} for x in rows if 43 <= x['semana'] <= 52)
assert all(x['neighbors_id'] in {e['n'] for e,_ in catalog['nb','b1'][:113]} for x in rows if 43 <= x['semana'] <= 52)

with CSV.open('w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n')
    writer.writeheader(); writer.writerows(rows)

lines = [
'# Calendário de inglês — Regular + Neighbors · 2 anos',
'',
'**Carga:** 104 semanas × 2 encontros de 75 minutos = **208 aulas / 260 horas ao vivo**. Prever mais **3 horas semanais de estudo autônomo**. Sem data de início definida: Semana 1 é a primeira semana letiva; feriados deslocam as semanas sem eliminar encontros.',
'',
'**Escopo real:** o Regular inglês tem 466 episódios A1, 474 A2, 530 B1, 510 B2, 510 C1 e 510 C2. Neighbors inglês tem 450 episódios originais + 45 revisões de arco em cada nível A1–B2. Este calendário seleciona **208 episódios-âncora de cada proposta**; os demais são acervo de prática e aprofundamento, não tarefas obrigatórias em massa. As revisões de arco do Neighbors só devem ser usadas após os dez originais correspondentes.',
'',
'**Meta do 1º ano:** A1 (semanas 1–20), A2 (21–42), e o primeiro quarto sequencial do B1 (43–52: episódios regulares dentro dos primeiros 133 de 530; Neighbors dentro dos primeiros 113 de 450). **Meta do 2º:** restante do B1 (53–74), B2 (75–102), projetos de consolidação B2 (103–104). C1/C2 continuam disponíveis no catálogo, mas não são prometidos em 260 horas ao vivo.',
'',
'As metas CEFR são **metas de desempenho**, não certificação automática: o professor ajusta o ritmo após as verificações das semanas 20, 42, 52, 74 e 102. O avanço depende de evidências de escuta, fala, leitura e escrita. Para chegar à meta do 1º ano, as 3 horas de estudo entre aulas são parte do plano.',
'',
'## Como unir as duas propostas',
'',
'- **Regular** fornece obra cultural, leitura, vocabulário e descoberta linguística. O professor escolhe uma cena e uma construção que serão realmente usadas ao falar.',
'- **Neighbors** fornece uma situação com interlocutor, objetivo, consequência e reparo. O estudante transfere a construção do Regular para uma fala própria, com opção de tom quando o contexto pedir.',
'- Cada encontro tem os dois episódios identificados abaixo. **Aula A** começa pela obra e termina numa interação; **Aula B** começa pela conversa e volta ao Regular para explicar o que mudou na fala. Essa alternância impede que uma série vire apenas dever da outra.',
'- A obra cultural não precisa descrever o mesmo lugar da cena Neighbors. A ponte é uma **função comunicativa explícita**: uma palavra, padrão, interpretação ou estratégia da obra passa a ser usada em outra situação. Se a ponte não ficar natural, o professor usa a situação como contraste, sem atribuir à obra uma relação histórica inventada.',
'',
'## Roteiro de cada encontro (75 min)',
'',
'| Minutos | Aula A — Regular → Neighbors | Aula B — Neighbors → Regular |',
'|---|---|---|',
'| 0–8 | Recuperar duas falas da aula anterior; aluno explica onde as usaria. | Recuperar a missão A sem mostrar o texto. |',
'| 8–20 | Observar obra e contexto; separar fato documentado, interpretação e comparação. | Entrar na cena Neighbors; prever a próxima fala e sua intenção. |',
'| 20–35 | Ler/escutar um trecho do Regular; extrair 3–5 unidades úteis, sua pronúncia e um molde variável. | Ouvir diálogo; trocar um elemento da fala (pessoa, propósito, tempo ou condição) e observar a resposta. |',
'| 35–55 | Encenação da situação Neighbors com a linguagem do Regular; duas rodadas com papéis trocados. | Contrastar a fala natural com o padrão e a ponte português–inglês do Regular. |',
'| 55–68 | Nova condição, consequência comunicativa e reparo; professor registra erro que merece nova tentativa. | Tarefa livre: resolver situação semelhante em outro contexto; colegas pedem esclarecimento. |',
'| 68–75 | Bilhete de saída: fala gravada ou 3 linhas escritas + uma dúvida. | Autoavaliação CEFR curta + missão de estudo entre aulas. |',
'',
'**Particular:** professor assume o segundo personagem, dá duas pistas graduais e pede uma segunda versão melhorada. **Grupo:** duplas/trios alternam papéis; observador anota uma fala eficaz, uma quebra de clareza e uma possível reformulação. O objetivo é comunicação, e a gramática entra como ferramenta para melhorar a fala.',
'',
'**Estudo entre semanas (3 h):** 45 min de releitura/escuta Regular, 45 min de repetição e variação Neighbors, 45 min de leitura ou escrita autoral ligada à obra, 45 min de revisão espaçada e registro de áudio. Escolher episódios complementares de acordo com a dificuldade detectada; não impor dezenas de episódios só para “cobrir” o catálogo.',
'',
'## Verificações e produtos',
'',
'| Semana | Evidência de aprendizagem |',
'|---|---|',
'| 10 | A1 inicial: apresentação, pedido simples e escuta de resposta curta. |',
'| 20 | A1: conversa de 3 minutos, leitura curta com informação localizada e mensagem de 60–80 palavras. |',
'| 31 | A2 intermediário: contar acontecimento, pedir esclarecimento e comparar opções. |',
'| 42 | A2: conversa de 5 minutos, leitura funcional e mensagem de 100–120 palavras. |',
'| 52 | B1 inicial: relato com razão e consequência; primeiro quarto do B1 trabalhado por amostragem. |',
'| 64 | B1 intermediário: apresentar opinião, negociar próximo passo e reparar incompreensão. |',
'| 74 | B1: interação de 8 minutos, leitura de duas perspectivas e texto de 150–180 palavras. |',
'| 88 | B2 intermediário: resumir argumentos, discordar com tato, sustentar inferência. |',
'| 102 | B2: debate de 10 minutos, síntese de fonte cultural e texto argumentativo de 220–280 palavras. |',
'| 104 | Projeto final: mediação de situação multicultural, apresentação e portfólio de evolução. |',
'',
'**Protocolo dos marcos:** na Aula A, reservar os minutos 35–68 para uma tarefa nova de interação e uma produção escrita curta, usando as duas âncoras da semana apenas como preparação. Na Aula B, reservar os minutos 20–68 para escuta e leitura inéditas, seguida de reformulação oral. Registrar quatro evidências separadas — compreensão oral, interação, leitura e escrita — com escala 0 (ainda não realiza), 1 (realiza com apoio) ou 2 (realiza de modo autônomo e adequado). Entregar uma próxima missão individual, sem transformar a pontuação em certificado CEFR automático.',
'',
'**Revisões de arco Neighbors:** quando a turma tiver de fato trabalhado os dez originais do arco (em aula ou no estudo orientado), usar a revisão como parte dos 45 minutos semanais de retomada, trocando um episódio complementar; registrar quais dez episódios foram vistos antes. Se isso não ocorreu, fazer uma revisão autoral das falas praticadas, sem apresentar o arc review como concluído.',
'',
'## Calendário semanal',
'',
'Cada célula A/B mostra **Regular ID + Neighbors ID** (IDs sempre acompanhados do curso; alguns números se repetem entre cursos). Os títulos e as falas de partida estão detalhados no [CSV das 208 aulas](CALENDARIO-INGLES-208-AULAS.csv).',
'',
'| Semana | Nível / etapa | Aula A — âncoras reais | Aula B — âncoras reais | Missão da semana |',
'|---:|---|---|---|---|',
]
for i in range(0, len(rows), 2):
    a,b = rows[i:i+2]
    check = f" **[Verificação: {a['avaliacao']}]**" if a['avaliacao'] else ''
    mission = f"{short(a['regular_foco'], 52)} → {short(b['neighbors_situacao'], 58)}{check}"
    lines.append(f"| {a['semana']:03} | {a['bloco']} | `{a['regular_curso']}:{a['regular_id']}` {short(a['regular_titulo'], 30)} + `{a['neighbors_curso']}:{a['neighbors_id']}` {short(a['neighbors_titulo'], 28)} | `{b['regular_curso']}:{b['regular_id']}` {short(b['regular_titulo'], 30)} + `{b['neighbors_curso']}:{b['neighbors_id']}` {short(b['neighbors_titulo'], 28)} | {mission} |")
lines += [
'',
'## Especificação da ficha de cada aula',
'',
'O CSV contém, para as 208 aulas: semana, ano, nível, IDs e caminhos dos dois episódios reais, obra principal do Regular, três unidades de cada episódio, foco linguístico, situação e falas-gatilho, missão de transferência, preparação do professor, **roteiro individual por faixa de minutos**, estudo entre aulas, produto observável e marco de avaliação. O professor deve ler os dois episódios antes de montar os slides e registrar: **(1)** trecho cultural e fonte; **(2)** fala-chave, com áudio; **(3)** duas trocas que preservem naturalidade; **(4)** resposta provável do interlocutor; **(5)** uma hipótese de mal-entendido e reparo; **(6)** critério de sucesso alinhado ao nível.',
'',
'**Exemplo de aula A (semana 1):** partir de `en-a1` e sua obra cultural; pedir ao aluno que se apresente sem ler. Em seguida, entrar no cenário `nb-a1` e fazer um pedido ou apresentação em três etapas: abrir, obter a informação e encerrar. Trocar o interlocutor e repetir com outra intenção. Fechar com uma gravação curta; avaliar clareza e adequação, não apenas acerto de palavras.',
'',
'**Exemplo de aula B (semana 75):** escutar o diálogo B2 Neighbors e anotar hipótese, evidência e contra-argumento. Ler a referência do Regular, identificar o que ela permite afirmar e o que fica incerto. Em trios, um defende uma decisão, outro questiona uma premissa e o terceiro sintetiza a posição mais forte. Cada estudante reformula uma frase para torná-la mais diplomática sem perder precisão.',
'',
'**Atenção editorial:** títulos, ganchos e obras vêm dos arquivos atuais, mas a seleção não substitui a conferência humana de continuidade de personagens, direitos de uso das obras, adequação do episódio e qualidade do áudio. Revisões de arco Neighbors não foram mapeadas automaticamente porque dependem dos dez episódios anteriores; o professor só as atribui quando esse arco foi efetivamente estudado.',
'',
'Gerado por `python3 tools/curriculum/build_english_two_year_calendar.py`. O script valida a quantidade de encontros, a existência dos episódios, a unicidade dos âncoras por curso e a fronteira do primeiro quarto de B1.',
]
DOC.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(DOC.relative_to(ROOT), CSV.relative_to(ROOT), len(rows), 'aulas')
