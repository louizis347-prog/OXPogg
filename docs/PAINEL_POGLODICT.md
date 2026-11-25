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
| Aula | Tema | PoggloDict antes | Depois | Lição nova criada |
|---|---|---|---|---|
| 1 | Café para viagem | 3, 7, 5, 27 | 4, 50 | – |
| 1001 | Sanduíche no deli | 4, 10, 7, 34 | 111, 25 | – |
| 2 | Quatro mangas (preço) | 5, 60, 191, 192 | 54, 193 | – |
| 1002 | Placas do corredor | 54, 19, 193, 197 | 60, 192 | – |
| 3 | Nice to meet you | 1, 12, 14 | 209, 1 | (301 cumprimentos serve também) |
| 1003 | Apresente-se | **308**, 1, 49, 282 | 310, 49 | 308 profissões e locais de trabalho |
| 4 | Soletre o seu nome | **302**, **303**, 18, 328 | 65, 44 | 302 alfabeto; 303 números e telefone |
| 1004 | Soletrando o endereço | **307**, 303, 11, 328 | 65, 14 | 307 soletrar endereço |
| 5 | Where are you from? | **305**, **306**, 1, 14 | 12, 341 | 305 países e nacionalidades; 306 idiomas |
| 1005 | Minha cidade | 14, 20, 30, 125 | 20, 30 | – |

Lições criadas para cobrir lacunas (A1 301–310, bloco “Conhecendo pessoas”): 301 cumprimentos e despedidas, 302 alfabeto, 303 números de 0 a 20 e telefone, 304 idade e números até 100, 305 países e nacionalidades, 306 idiomas, 307 soletrar endereço, 308 profissões, 309 dias da semana, 310 revisão (mini-história). Elas também preparam as aulas ao vivo seguintes (6 “Hello, goodbye”, 7 idade, 9 profissões, 10 dias da semana).

## Limites do piloto
- As lacunas das 10 primeiras aulas foram preenchidas com as lições 301–310 (veja `docs/TRILHA_AO_VIVO.md` para o processo de criar lições sempre que a aula ao vivo exigir algo que o PoggloDict não tem).
- O vocabulário só bate em parte (no A1, 66% dos termos do Painel existem no PoggloDict, mas espalhados; no A2, 13%). A ligação por aula é feita por tema e gramática, escolhida à mão.
- O progresso do PoggloDict é local: o professor ainda não vê quem fez a prévia.
- Os links abrem o PoggloDict em outra aba (`../poglodict/index.html#licao/eng/A1/N`).
