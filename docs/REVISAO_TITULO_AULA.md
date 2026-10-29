# Revisão manual — o título da obra bate com a aula? (187 suspeitos)

Critério de seleção: nenhuma palavra do título da obra aparece em `p`, `s`, vocabulário, falas, missões ou exemplos de verbos (fora das frases-modelo). Cada um dos 187 foi lido (obra, tipo/ano, foco, vocabulário e falas). Lista dos que não estão ok: `docs/REVISAO_TITULO_AULA.csv`.

| Veredito | Qtde |
|---|---|
| OK — o título bate (ligação clara ou plausível) | 107 |
| FRACO — ligação frouxa, mas defensável | 34 |
| ERRADO — a aula é claramente sobre OUTRA obra | 20 |
| ERRADO — aula genérica, título sem relação nenhuma | 26 |

## ERRADO — a aula é sobre outra obra (20)
Em 14, essa outra obra **já é título de outro episódio** do curso: trocar só o título recria a obra repetida. Em 6 ela parece livre (checagem fina pendente: Lost in Space, Lego, Gnomeo & Juliet, King Arthur, Marie Kondo, Diário de Anne Frank). Sinal típico: `a.d`/ano descrevem a obra certa, mas o título foi trocado na deduplicação (ex.: 940003 “Hospital Italiano…” com descrição de *To Kill a Mockingbird*).

## ERRADO — genérica (26)
Título sem relação nenhuma com a aula (ex.: “Gießen”, “Hof”, “Ran” em aulas de phrasal verbs). Aqui **só trocar o título** (e a descrição) resolve, sem mexer na aula.

## Observações
- Vários títulos têm tipo/ano errados (“Shrek — Instituição”, “Route 66 — Artista”), sinal de troca automática.
- Nada foi alterado nos dados.

## Aplicado (26 episódios do inglês regular)
- **Genéricas (23):** obra trocada por outra que combina com o tema da aula, sem mexer no conteúdo (descrição, ponte e capa novas; fichas novas em A1/A2).
- **Obra livre (3):** título correto devolvido — Lost in Space, Gnomeo & Juliet, Le Morte d’Arthur.
- **Ficaram de fora (17):** a aula é sobre uma obra que já é título de outro episódio (14 da revisão + Remember the Titans, Dubliners e Kitchen Nightmares, cujos textos culturais dos episódios 950013, 85070 e 960061 descrevem essas obras) e Marie Kondo/Lego/Anne Frank, usadas por outros episódios. Nada foi alterado neles.
