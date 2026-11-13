# Aulas ao vivo: versões de 1h30 e de 1h

Cada uma das 500 aulas do Painel do Professor é um encontro ao vivo. Todas têm duas durações:

| Etapa | 1h30 | 1h |
|---|---|---|
| Missão | 5 | 3 |
| Contexto | 10 | 8 |
| Leitura | 14 | 11 |
| Conversa | 16 | 13 |
| Pausa | 5 | — |
| Oficina | 12 | 9 |
| Prática | 8 | 6 |
| Interação (jogo de papéis em duplas) | 12 | 5 |
| Escrita | 5 | 3 |
| Retomada e correção coletiva | 3 | 2 |

- A versão de 1h30 é a padrão (botão "Aula de 1h30 / Aula de 1h" no menu do professor; a escolha fica salva no navegador).
- O roteiro do professor (tecla T ou botão "Roteiro do professor") traz, em cada tela, objetivo, como conduzir, respostas e, na versão de 1h30, o bloco "Só na versão de 1h30".
- Fonte: `professor/src/live_teach.py` (gera `teach` por tela e `plan.solo90/group90`). Para reaplicar em todas as aulas: `python3 professor/tools/apply_live.py`. O `build_v5.py` aplica automaticamente.
