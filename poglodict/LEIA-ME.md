# Pogolo Dict · edição offline

1. Extraia o ZIP inteiro.
2. Abra a pasta PoggloDict e dê duplo clique em index.html.
3. Escolha o idioma. Em português brasileiro, escolha American English ou Español como idioma de apoio.

Esta edição reúne 16.800 lições, dicionário e guias de escrita dos oito cursos. Cada curso tem 350 lições por nível, de A1 a C2. Na aba Lições, cada nível tem sete arcos de 50 lições, em blocos de dez. Cada lição abre em uma tela com endereço próprio. As mini-histórias abrem em lições múltiplas de 10. O conteúdo funciona sem servidor. As fontes externas e as vozes do navegador dependem do navegador e do dispositivo. Favoritos, revisão e progresso são locais e podem ficar separados dos dados da versão web.

As lições têm fotos licenciadas por tema e por fala, com créditos em FOTOS.md. Há áudio por fala, palavra e exemplo, com reprodução contínua e controle de velocidade. A prática reúne 14 exercícios em sete áreas, com pistas, progresso por exercício e modelos de resposta após a tentativa. Os blocos abrem com uma orientação sobre como estudar o conteúdo. O vocabulário da cena traz uma foto licenciada, expressões conectadas e uma continuação com áudio. As seções de cada lição abrem sob demanda a partir de cartões com fotos e podem ocupar a tela inteira pelo botão Tela cheia no cartão. A versão usa a tela cheia do navegador quando disponível e amplia o cartão na página nos demais casos. As cenas de revisão compartilhadas entre lições estão identificadas. Em Palavra em uso, você completa duas situações e escreve uma fala própria. A gramática tem explicação, exemplos alinhados e desafios. No início do A1 de inglês, as frases usam formas completas. As contrações entram em etapas, com explicações nos blocos de gramática correspondentes. A conversa guiada inclui quatro rodadas para completar um diálogo novo, além de uma atividade de escrita com dois moldes. No A1 e no A2, os moldes ficam visíveis. A partir do B1, eles ficam na ajuda opcional. Cada lição oferece uma dica de pronúncia com uma atividade e duas palavras com áudio. O teste de inglês inclui seis etapas. As questões de escuta dependem da voz em inglês instalada no navegador. Para verificar autoria e licença das fotografias, consulte FOTOS.md.

Inglês americano para brasileiros: as lições A1 de 1 a 50 têm leituras e diálogos próprios com tradução, gramática em contexto e exercícios. O bloco de pronúncia dessas lições traz três exemplos sonorizados com voz sintética americana, animação articulatória, modo lento e desafio de escuta. Os áudios funcionam offline.

Os arquivos em dados/ contêm o acervo integral da edição, encapsulado em JavaScript para funcionar ao abrir index.html diretamente. O ZIP também inclui o HTML, CSS, JavaScript e SVG da interface. Não é preciso instalar programas.

Alguns verbetes de corpus têm exemplos em revisão. Traduções e pinyin produzidos com apoio automático podem precisar de conferência em textos ambíguos. Os exemplos com fonte preservam links para consulta quando houver internet.

## Créditos e fontes

- [Wiktionary](https://en.wiktionary.org/) e [Kaikki / Wiktextract](https://kaikki.org/), verbetes adaptados sob [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- [CC-CEDICT](https://www.mdbg.net/chinese/dictionary?page=cc-cedict), dicionário chinês-inglês da comunidade publicado por MDBG. Dados adaptados sob [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- [Tatoeba](https://tatoeba.org/), exemplos de corpus com links para as frases. Consulte os [termos de uso](https://tatoeba.org/en/terms_of_use).
- [Wikipédia](https://www.wikipedia.org/), exemplos creditados aos artigos correspondentes, sob [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).


## Inglês americano A1 · lições 1–180 (piloto reescrito)
- Lições 1–50 reescritas e 51–180 novas: gramática em ordem cumulativa, 8–10 palavras por lição, leitura de 6 frases, diálogo de 8–10 falas, exercício de lacuna e mini-quiz de 4 itens (lacuna, escuta, duas montagens). Os erros do quiz voltam como revisão nas lições seguintes.
- Cada tema aparece uma vez e o vocabulário-alvo não se repete entre as lições (conferido por script).
- Lições 51–180 não têm foto licenciada (usam a ilustração do tema) nem o laboratório animado de pronúncia (só texto).
- Fonte e ferramentas: `tools/a1/` (`build.py` valida e gera os arquivos do app; `curriculum_51_130.json` é o currículo).
- Não houve revisão humana de naturalidade nem de traduções.

## Inglês A1 181–350 e A2 1–80 (autorais)
As lições A1 181–350 e A2 1–80 (nº 351–430 em sequência A1+A2) seguem o padrão das 50 primeiras e **não repetem nenhum termo de vocabulário nem frase** das lições A1 1–180 e A2 81–210 (431–560). Dados: `fontes/a1-181-350/*.json` e `fontes/a2-1-80/*.json` (um arquivo por lição). `tools/poglodict_build_a1.py` gera `english-a1-extra.js`, `english-a2-extra.js` e as planilhas `plano-ingles-a1-181-350.csv` e `plano-ingles-a2-01-80.csv`. `fontes/validar.py` confere formato, nível CEFR-J e repetições (usa listas em `fontes/*.json`; os caminhos de trabalho apontam para /tmp/pd). Para corrigir uma lição, edite o JSON e rode o script. Limites: sem foto própria (foto provisória), sem áudio gravado nem laboratório de pronúncia animado, sem revisão humana; o vocabulário livre do dicionário era escasso, então algumas lições ensinam palavras menos comuns ou cenas improvisadas.

## Inglês americano A2 · lições 431–560 (autorais)
- As lições 431–560 (A2 nº 81–210, com A1 = 1–350 e A2 = 351–700) têm conteúdo próprio no mesmo formato das lições 1–180 do A1: 8–10 palavras, leitura de 6 frases, diálogo de 8–10 falas, exercício de lacuna e mini-quiz de 4 itens (erros voltam como revisão). Mini-história nas lições 440, 450 … 560.
- Gramática A2 em ordem: present perfect, past continuous, used to, will, condicionais, modais, comparativos, quantificadores, orações relativas, passiva, verbos frasais, perguntas indiretas, tags, discurso indireto e wish; 13 revisões.
- Sem foto licenciada (ilustração do tema) e sem laboratório de pronúncia animado. Fonte e ferramentas: `tools/a1/a2.py` e `tools/a1/curriculum_a2_431_560.json`; saída em `english-a2.js`.
- Não conferido: o que as lições 351–430 (outra sessão) já ensinam; a ponte pode repetir estruturas. Sem revisão humana de naturalidade e traduções.

## Inglês americano A2 · lições 211–330 (autorais)
- As lições 561–680 na sequência A1+A2 (A2 nº 211–330) seguem o formato das lições A2 81–210: 8–10 palavras novas, leitura de 6 frases, diálogo de 8–10 falas, exercício de lacuna, mini-quiz de 4 itens, exemplos, dica de pronúncia e mini-história nas lições 570, 580 … 680. Os temas são telefone e atendimento, trabalho, corpo e hábitos, casa e consertos, dinheiro e compras online, tecnologia, cultura e viagem, comida, escola e idiomas, natureza e clima, cultura e lazer, pessoas e convivência (revisão final do A2 na 680).
- Nenhum termo de vocabulário novo repete outro do curso (as palavras foram reservadas com `tools/a1/claim.py` antes do uso). Em troca, o vocabulário livre estava quase esgotado: boa parte das palavras novas são expressões de 2–3 palavras e algumas lições ficaram com 8 itens, com cenas ou palavras menos naturais. Vale revisão humana.
- Fonte e ferramentas: `tools/a1/curriculum_a2_561_680.json`, `tools/a1/out/a2_block14..25.json`, `tools/a1/a2.py build` (valida e gera `english-a2.js` e `plano-ingles-a2-431-680.csv`). Sem foto licenciada, sem áudio gravado, sem laboratório de pronúncia animado e sem revisão humana de naturalidade e traduções.
