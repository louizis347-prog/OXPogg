# Aulas ao vivo ligadas ao PoggloDict (piloto: 10 primeiras aulas)

Ideia: o PoggloDict é a espinha dorsal de estudo; a aula ao vivo (Painel do Professor) se liga a ele sem perder o conteúdo já feito.
Cada aula ligada ganha 3 quadros, que entram em tempo de execução (a aula original não é alterada):
1. **PoggloDict · antes da aula**: cartões com as mini lições a fazer antes (cada um abre a lição certa), palavras já vistas e, em “Para o professor”, a dica de ritmo e o que o PoggloDict ainda não cobre.
2. **Aquecimento · PoggloDict**: 3 a 4 perguntas tiradas dos mini-quizzes das lições indicadas.
3. **PoggloDict · depois da aula**: mini lições para revisar.

## Como funciona
- Dados: `professor/data/pd_links.json` (gerado por `python3 tools/pd_links_build.py`; o mapa editável fica no próprio script, em `LINKS`).
- `professor/js/pdlink.js` injeta os quadros quando a aula tem entrada no arquivo; `professor/js/lesson1.js` desenha o quadro `pdlink`; `professor/js/deck2.js` carrega o arquivo.
- Para ligar outra aula: acrescente uma entrada em `LINKS` (aula do Painel → lições do PoggloDict) e rode o script.

## As 10 primeiras aulas ao vivo (ordem do currículo do Painel)
| Aula | Tema | PoggloDict antes | Depois | Lacuna do PoggloDict |
|---|---|---|---|---|
| 1 | Café para viagem | 3, 7, 5, 27 | 4, 50 | – |
| 1001 | Sanduíche no deli | 4, 10, 7, 34 | 111, 25 | – |
| 2 | Quatro mangas (preço) | 5, 60, 191, 192 | 54, 193 | – |
| 1002 | Placas do corredor | 54, 19, 193, 197 | 60, 192 | – |
| 3 | Nice to meet you | 1, 12, 14 | 209, 1 | – |
| 1003 | Apresente-se | 1, 49, 282 | 1, 49 | profissões e cargos |
| 4 | Soletre o seu nome | 18, 44, 49, 328 | 65, 44 | alfabeto e soletrar |
| 1004 | Soletrando o endereço | 11, 14, 40, 328 | 65, 328 | soletrar endereço e números |
| 5 | Where are you from? | 1, 12, 14 | 14, 341 | países e nacionalidades |
| 1005 | Minha cidade | 14, 20, 30, 125 | 20, 30 | – |

## Limites do piloto
- O PoggloDict A1 começa por lugares, objetos e pedidos, e não tem lições sobre alfabeto, países, profissões, idade, cumprimentos nem dias da semana. Esses temas aparecem nas aulas ao vivo 4, 5, 6, 7 e seguintes: ou entram lições novas no PoggloDict, ou a aula os cobre sozinha.
- O vocabulário só bate em parte (no A1, 66% dos termos do Painel existem no PoggloDict, mas espalhados; no A2, 13%). A ligação por aula é feita por tema e gramática, escolhida à mão.
- O progresso do PoggloDict é local: o professor ainda não vê quem fez a prévia.
- Os links abrem o PoggloDict em outra aba (`../poglodict/index.html#licao/eng/A1/N`).
