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

## Resultado da auditoria

- **A2 (2001–2050):** 0 palavras fora da regra após a correção.
- **A1 (500 aulas):** 315 aulas com palavras acima do nível que a aula não ensina (579 palavras; 112 aulas com palavras B1 ou B2).
- O que há de grave no A1 é a lista B1/B2 abaixo; as palavras A2 dentro de aulas A1 são esperadas, porque 500 aulas de A1 não cabem nas ≈1000 palavras do nível A1 do CEFR-J.

## A1: palavras B1/B2 que a aula não ensina

| Aula | Palavras |
|---|---|
| 22 | chips (B2) |
| 37 | strawberry (B1) |
| 84 | spin (B2) |
| 85 | working (B1) |
| 92 | including (B1) |
| 96 | pirate (B2) |
| 1001 | lettuce (B1) |
| 1003 | graphic (B1) |
| 101 | chips (B2) |
| 1012 | fifth (B1) |
| 1018 | folk (B1) |
| 1030 | olive (B2) |
| 1032 | absolutely (B1) |
| 1043 | foot (B1) |
| 1055 | lobby (B2) |
| 1058 | discount (B1) |
| 1060 | warning (B1) |
| 1061 | spray (B2) |
| 1062 | safely (B1) |
| 1067 | bubbles (B1) |
| 1071 | press (B1) |
| 1072 | mess (B1), trash (B1), recycling (B1), bin (B1) |
| 1073 | refund (B1), percent (B1) |
| 1074 | rocky (B2), register (B1) |
| 1075 | medium (B1), total (B1) |
| 1079 | counter (B1), register (B1) |
| 1081 | press (B1) |
| 1083 | cabinet (B2) |
| 1086 | comedy (B1) |
| 1087 | chase (B1) |
| 1090 | exit (B1) |
| 1091 | booth (B2), sharp (B1) |
| 1093 | folk (B1), fountain (B1) |
| 1094 | dot (B1) |
| 1095 | press (B1), rail (B1) |
| 1096 | pumpkin (B2) |
| 1099 | niece (B1) |
| 1100 | olives (B2) |
| 1105 | loud (B1), service (B1) |
| 1106 | press (B1) |
| 1110 | link (B1), press (B1) |
| 1111 | signal (B1) |
| 1112 | monthly (B1) |
| 1113 | per (B1), link (B1) |
| 1117 | fold (B1) |
| 112 | passport (B1) |
| 1123 | ginger (B1) |
| 1132 | proof (B1) |
| 1134 | service (B1) |
| 1142 | normally (B1) |
| 1144 | main (B1) |
| 1146 | jazz (B1), tasty (B1) |
| 1152 | county (B1), pie (B1), main (B1) |
| 1158 | rest (B1) |
| 1159 | opening (B1) |
| 1160 | elegant (B2) |
| 1163 | friendly (B2), calm (B1) |
| 1169 | foot (B1) |
| 1174 | total (B1) |
| 118 | backpack (B1) |
| 1180 | service (B1), meanwhile (B1) |
| 1183 | log (B1) |
| 1184 | loud (B1) |
| 1185 | friendly (B2) |
| 1188 | main (B1) |
| 1189 | service (B1) |
| 1190 | fifth (B1) |
| 1193 | feet (B1) |
| 1197 | limit (B1) |
| 120 | trash (B1) |
| 1203 | salty (B2) |
| 1204 | counter (B1) |
| 1205 | cough (B1) |
| 1208 | burning (B1), press (B1) |
| 1209 | calm (B1) |
| 1214 | working (B1) |
| 1216 | total (B1) |
| 1218 | rubber (B1) |
| 1225 | individual (B1) |
| 1231 | sometimes (B1) |
| 1232 | sometimes (B1), calmer (B1), definitely (B1), tiring (B1) |
| 1233 | replacements (B2) |
| 1235 | feet (B1) |
| 1236 | miles (B1), steeper (B1) |
| 1243 | main (B1) |
| 1246 | bare (B1) |
| 1247 | formally (B1) |
| 1249 | foot (B1) |
| 1252 | sore (B1) |
| 135 | parking (B1) |
| 145 | miles (B1) |
| 146 | jazz (B1) |
| 148 | miles (B1) |
| 149 | barrel (B1), racing (B1) |
| 152 | huge (B1) |
| 161 | tiny (B1), adorable (B1) |
| 164 | fifth (B1) |
| 170 | terminal (B1) |
| 173 | medium (B1), pie (B1) |
| 174 | comedy (B1) |
| 180 | completely (B1) |
| 184 | roadside (B1), assistance (B1) |
| 192 | graphic (B1) |
| 194 | boots (B1) |
| 202 | broccoli (B1) |
| 215 | pounds (B1), pound (B1) |
| 232 | designer (B1) |
| 233 | marketing (B2) |
| 236 | parking (B1) |
| 238 | learning (B2) |
| 245 | feet (B1), measure (B1) |
| 247 | sparkling (B2) |
