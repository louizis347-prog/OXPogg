# Auditoria #3 — o título da obra bate com a aula? (inglês regular)

Script: `tools/audit/auditoria_titulo_aula.py` → `docs/AUDITORIA_TITULO_AULA.csv` (episódios não coerentes) e `.json`.
Método (heurístico): o episódio é **COERENTE** se as cenas/missões/exemplos citam a obra fora das frases-modelo; senão, é **PRESA_A_OUTRA_OBRA** quando o vocabulário e as falas raras coincidem com o de outro episódio que cita uma obra; caso contrário, **GENERICA**.

| Nível | Coerente | Presa a outra obra | Genérica |
|---|---|---|---|
| A1 | 412 | 2 | 52 |
| A2 | 398 | 3 | 73 |
| B1 | 465 | 4 | 61 |
| B2 | 447 | 5 | 58 |
| C1 | 201 | 135 | 174 |
| C2 | 172 | 136 | 202 |

## Leitura honesta
- **Genéricas (620):** a aula não é sobre uma obra específica → dá para **só trocar o título** (e a descrição/ponte) para uma obra única que combine com o tema, sem mexer no conteúdo. Exige escolher a obra por episódio (julgamento) e refazer a ficha da capa.
- **Presas a outra obra:** no A1–B2 são poucas (14); no C1/C2 (271) a maior parte é **cópia de conteúdo entre episódios pareados** (ex.: 84001 × 7084001), não título trocado. Aí trocar o título não resolve: o conteúdo repete.
- **A2 inicial (29 aulas):** vocabulário preso a obras que se repetiam em outro nível (moinho/cavaleiro = Dom Quixote). Título-só recriaria a duplicata; essas 29 foram **reescritas** com obras únicas (PR desta entrega).
- Esta heurística pode errar nos dois sentidos; serve para priorizar a revisão, não como prova.

## Corrigido nesta entrega
- 29 aulas do A2 reescritas (obra única, conteúdo e fichas de capa novos, expressões únicas em todo o A2).
- Etiqueta da capa: dizia "A1" em 1.514 episódios de A2/B1/B2; agora mostra o nível correto.
