# Níveis CEFR do projeto: referência, regra e auditoria

## Referência usada

- **Vocabulário:** CEFR-J Vocabulary Profile v1.5 (Tono Laboratory, dados abertos, repositório `openlanguageprofiles/olp-en-cefrj`). Cópia: `professor/data/cefrj-vocab.json` (≈7 mil palavras, A1–B2).
- **Gramática:** CEFR-J Grammar Profile (2018), com colunas de Core Inventory, EGP e GSELO. Cópia: `professor/data/cefrj-grammar.csv`.
- Os níveis anteriores do projeto (tetos por faixa de aula) eram estimativas minhas e **não** vinham de nenhuma lista oficial.

## Regra do projeto

1. **Vocabulário:** nenhuma palavra do diálogo pode estar acima do nível da aula (A1 → A1; A2 → A1+A2), a menos que a aula a ensine (vocabulário, glossário, verbos ou expressões da própria aula). Nomes próprios são ignorados.
2. **Gramática:** só entra no nível o que a referência classifica nele (tabela abaixo).
3. A checagem roda em `tools/cefr_audit.py` e aparece como `CEFR n ok` no fim do `runbatch.sh`.

## Gramática por nível (CEFR-J)

| Estrutura | Nível CEFR-J | Decisão no A2 |
|---|---|---|
| was/were afirmativo | A1.3 | A2.1 |
| was/were negativo e passado simples (afirmativo) | A1.3 / A2.1 | A2.1 |
| passado simples negativo e perguntas (did/didn't) | A2.1 | A2.1 |
| should | A2.1 | A2.2 |
| present perfect afirmativo | A2.1 | A2.2 (ever/never/already; sem forma negativa) |
| if (condição) | A2.1 | A2.3 |
| passiva (is/was made) | A1.2–A2.1 | A2.3 |
| going to, will, have to, much (incontável), comparativo com more | A2.2 | A2.2 |
| **could, may, might, must** | **B1.1** | **fora do A2** (só como frases prontas) |
| **used to** | **B1.1** | **fora do A2** (trocado por passado com always/often) |
| present perfect negativo e com for/since | B1.1 | fora do A2 |
| segundo condicional | B1.2 | fora do A2 |
| which relativo, discurso indireto com tell | B1–B2 | fora do A2 |

## Resultado da auditoria (depois da correção)

- **A2 (2001–2050):** 0 palavras fora da regra.
- **A1 (500 aulas):** **0 palavras B1/B2** que a aula não ensina (eram 141, em 112 aulas). Restam 274 aulas com palavras de nível A2 (438 palavras): são esperadas, porque 500 aulas de A1 não cabem nas ≈1000 palavras do A1 do CEFR-J.

## Palavras de apoio

As 141 palavras B1/B2 do A1 (por exemplo *passport, refund, parking, press, terminal, miles*) são de situações reais e foram mantidas nos diálogos. Cada uma agora é **ensinada na própria aula**, numa tela extra "Palavras de apoio" (1 a 2 telas por aula, até 3 palavras cada), listada em `professor/src/support_words.json`. O `build_v5.py` insere essas telas automaticamente.
