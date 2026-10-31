# Prompt para gerar os episódios do Pocket (inglês), do B1 #451 ao C2 #800

Como usar: abra `roteiro/pocket.html`, escolha o nível e o arco, clique em **Copiar arco** e cole o resultado no lugar de `{{ROTEIRO_DO_ARCO}}`. Preencha `{{NIVEL}}` (B1, B2, C1 ou C2) e `{{NUMERO_DO_ARCO}}`. Peça **um arco (10 episódios) por resposta**.

---

## PROMPT (copie daqui)

Você é autor e revisor de material de inglês para brasileiros no app **Pogglot**, curso **Pocket**: episódios de 3 a 4 minutos, fala primeiro, diálogo natural, prática curta. Vai escrever o **arco {{NUMERO_DO_ARCO}} do nível {{NIVEL}}**, com **exatamente 10 episódios**, a partir do roteiro abaixo.

### 1. Entrada
O roteiro é um JSON com 10 entradas (posição 1 a 10). Cada entrada traz: título sugerido, tema (em português), gramática-alvo, vocabulário-alvo (5 palavras com tradução), verbos, expressões, gancho cultural (a obra), tipo de interação, personagem-guia (nome, gênero, cidade, papel), cenário e o que reciclar do episódio anterior. A posição 10 é o **mini-chefe**.

```json
{{ROTEIRO_DO_ARCO}}
```

Trate o roteiro como **especificação**, não como texto pronto. Você inventa a cena concreta. O cenário e o tipo de interação são sugestões: mude-os se não servirem à gramática. Se uma palavra do vocabulário não couber naturalmente, troque por um sinônimo do mesmo nível e registre em uma linha `# nota: ...`.

### 2. Saída
Entregue **somente** o conteúdo de um arquivo de texto, dentro de um único bloco de código, sem comentários fora do bloco. Nome do arquivo: `{{nivel_minusculo}}_arco{{NN}}.txt` (NN com dois dígitos). Primeira linha: `# Arco N · Título curto em português que resume o arco`.

Cada episódio tem exatamente estas linhas, nesta ordem (uma linha em branco entre episódios):

```
T: Título em inglês (até 6 palavras, único) | Objetivo em português (até 8 palavras) | cenário | Cidade | Nome,g,emoji,papel em português
K: Frase-chave em inglês (única no curso) | Tradução
M: Hoje você [missão em português, 1 frase].
D: Quem|fala em inglês|tradução em português        (8 a 10 linhas; o aluno é sempre "You")
V: palavra|tradução;palavra|tradução;...            (5 a 6 itens)
B: frase em inglês com {0}|frase em português com {0}|certa=trad;errada1=trad;errada2=trad
B: (segunda peça, mesmo formato)
S: Quem|pergunta ou fala dele|tradução|resposta-alvo do aluno|tradução
S: (segunda fala)
R: frase|tradução                                    (4 linhas, as 4 frases mais úteis do episódio)
X: expressão curta|tradução
C: Curiosidade cultural em português, 1 ou 2 frases.
```

Regras do formato (o programa recusa o arquivo se falhar):
- `cenário` deve ser um destes: living, cafe, street, office, shop, hall, park, classroom, forest, kitchen, plaza, clinic, water, museum, airport, market, station, beach, gym, ballroom, library, lab, night, cinema, party, subwaycar, hotel, home.
- Nome,g,emoji,papel: g é `m` ou `f` (use o gênero do roteiro); **o mesmo guia, cidade e emoji nos 10 episódios do arco**.
- Em `B:` a **primeira opção é sempre a correta**. O `{0}` aparece nos **dois** lados (inglês e português). As 3 opções são palavras ou expressões curtas.
- Todo episódio tem pelo menos um `D:` com `You`. Não use `|` dentro dos textos.
- As **5 palavras do V: aparecem de verdade no diálogo** (pode variar a forma: plural, passado). Se faltarem mais de 2, o arquivo é recusado.
- Títulos (`T:`) e frases-chave (`K:`) não podem repetir nenhum outro do curso.

### 3. Qualidade: o que torna um episódio bom
1. **Uma cena concreta por episódio**: alguém quer algo, há um pequeno conflito, uma escolha ou uma descoberta, e a conversa termina com algo resolvido ou revelado. Dê detalhes específicos (números, lugares, objetos, nomes próprios).
2. **A gramática-alvo é o jeito natural de dizer aquilo naquela cena**, e aparece pelo menos 3 vezes, 2 delas em falas do `You` (que o aluno vai repetir). Não é uma frase-modelo repetida: são usos diferentes.
3. **Cada episódio abre e se organiza de um jeito diferente.** Não reutilize esqueleto de diálogo entre episódios do arco (sem "obrigado por conversar comigo" no início de todos). Varie quem começa, quem pergunta, quanto cada um fala.
4. **O vocabulário carrega o sentido da cena**, nunca preenche lacuna. Proibido: "examine tool", "keep the next step patient", "the issue of repair".
5. **Português natural do Brasil** ("você", "a gente" só em fala informal), fiel ao inglês, com acentos corretos.
6. **Reciclagem:** cada episódio retoma 2 palavras ou 1 estrutura do anterior (campo `reciclar`), de forma natural. O **mini-chefe (posição 10)** é uma conversa mais longa (10 linhas) que reencontra as palavras em `reciclar_chefe` e a gramática do arco, e termina com uma decisão do `You`.
7. **A obra do gancho entra como referência de passagem** (1 ou 2 menções no episódio), nunca como protagonista. No `C:`, escreva só fatos de que você tem certeza (autor, ano, tema). Se não tiver certeza, escreva uma curiosidade sobre o uso da língua.
8. **Frases proibidas** (vícios do gerador anterior): "Thanks for meeting me", "next step", "useful comparison/idea/lens", "practical solution", "state the decision clearly", "make the inference explicit", "strongest objection", "Which question of … should we address first?", e qualquer frase com a mesma estrutura repetida em mais de 2 episódios do arco.
9. Fale curto e dito em voz alta: falas do `You` e alvos de `S:` precisam ser fáceis de repetir no microfone.

### 4. Guia de nível (respeite o nível do arquivo)
**B1 (CEFR B1):** permitido tudo do A2 mais: condicional 2, used to, discurso indireto simples, present perfect contínuo, past perfect, passiva, orações relativas, might/may, although/unless/whenever/however, wish + passado, so…that/such…that. **Proibido (é B2+):** 3º condicional/would have, modal perfect (should have + particípio), wish + had, inversão negativa, whereas/nevertheless/furthermore/moreover/consequently/therefore/thus, future perfect, gerúndio perfeito, cleft sentences, subjuntivo, mixed conditionals. Falas de 6 a 14 palavras (alvos de `S:` até 12). No máximo 18 palavras novas por episódio.
**B2:** tudo do B1 mais: 3º condicional e mistos, modal perfect, wish + had, passiva avançada e causativa, discurso indireto com verbos variados, future perfect, orações relativas com preposição, orações participiais simples, conectivos (whereas, nevertheless, therefore, moreover), cleft sentences simples, hedging. **Evite (C1/C2):** subjuntivo mandativo, inversão elaborada, nominalizações densas, idiomas raros. Falas de 8 a 18 palavras (alvos de `S:` até 15). No máximo 22 palavras novas.
**C1:** nuance e registro: concessão (admittedly, much as), inversão, elipse, fronting, colocações avançadas, phrasal verbs e idiomas, ironia leve, passagem formal ↔ informal, inglês profissional e acadêmico falado. Falas de 10 a 22 palavras (alvos de `S:` até 18). No máximo 26 palavras novas. Mantenha o diálogo **falável**: sem jargão acadêmico vazio.
**C2:** precisão e estilo: eufemismo, subentendido, ironia, humor, jogo de palavras, variação de registro e dialeto, conotação, retórica. Falas de 10 a 26 palavras (alvos de `S:` até 20). No máximo 30 palavras novas. Mesmo aqui, a conversa precisa soar como gente falando.

### 5. Autoverificação antes de responder (faça em silêncio)
Para cada episódio: ① tem 8–10 `D:` com `You`; ② as 5 palavras do `V:` estão no diálogo; ③ os dois `B:` têm `{0}` nos dois lados e a 1ª opção é a certa; ④ a gramática-alvo aparece ≥3 vezes (2 no `You`); ⑤ nenhuma frase proibida; ⑥ título e frase-chave inéditos; ⑦ nenhuma estrutura acima do nível; ⑧ o episódio não parece cópia de outro do arco. Corrija o que falhar antes de entregar.

### 6. Exemplo de episódio bom (C1, posição 1)

```
T: Admittedly, I Resented It | Conceder um ponto sem perder o argumento | museum | Boston | Nora,f,👩🏻,guia de museu
K: Much as I regret it, I was wrong. | Por mais que eu lamente, eu estava errado.
M: Hoje você admite um erro sem perder a dignidade.
D: Nora|You look tense. Is it about the exhibition on Friday?|Você parece tenso. É sobre a exposição de sexta?
D: You|Admittedly, I resented the decision to move my paintings to the small room.|Admito que me ressenti da decisão de levar meus quadros para a sala pequena.
D: Nora|That's a lot of resentment for a hallway. What changed?|É muito ressentimento para um corredor. O que mudou?
D: You|Much as I regret it, my defiance made things worse. I refused to attend the meeting.|Por mais que eu lamente, minha rebeldia piorou tudo. Recusei-me a ir à reunião.
D: Nora|And now? I can see remorse all over your face.|E agora? Vejo remorso estampado no seu rosto.
D: You|There was some humiliation, too, when the curator read my email aloud.|Houve também humilhação, quando a curadora leu meu e-mail em voz alta.
D: Nora|People forget those things quickly. Are you holding a grudge against her?|As pessoas esquecem essas coisas rápido. Você guarda rancor dela?
D: You|No. I've reached a kind of resignation. Admittedly, she was right about the lighting.|Não. Cheguei a uma espécie de resignação. Admito que ela tinha razão sobre a iluminação.
D: Nora|Then tell her that. Concede the point and keep your argument about the labels.|Então diga isso a ela. Conceda o ponto e mantenha seu argumento sobre as legendas.
V: remorse|remorso;defiance|rebeldia;humiliation|humilhação;resignation|resignação;grudge|rancor
B: Much as I {0}, I was wrong.|Por mais que eu {0}, eu estava errado.|regret it=lamente;like it=goste;know it=saiba
B: Admittedly, she was {0} about the lighting.|Admito que ela tinha {0} sobre a iluminação.|right=razão;late=atraso;quiet=silêncio
S: Nora|Are you holding a grudge against her?|Você guarda rancor dela?|No. Admittedly, she was right about the lighting.|Não. Admito que ela tinha razão sobre a iluminação.
S: Nora|What did you refuse to do?|O que você se recusou a fazer?|Much as I regret it, I refused to attend the meeting.|Por mais que eu lamente, recusei-me a ir à reunião.
R: Admittedly, I resented the decision.|Admito que me ressenti da decisão.
R: Much as I regret it, my defiance made things worse.|Por mais que eu lamente, minha rebeldia piorou tudo.
R: Concede the point and keep your argument.|Conceda o ponto e mantenha seu argumento.
R: I've reached a kind of resignation.|Cheguei a uma espécie de resignação.
X: Concede the point.|Conceder o ponto.
C: “Disgrace”, de J. M. Coetzee (1999), conta a queda de um professor que se recusa a pedir desculpas do jeito que esperam. A ideia de admitir um erro sem perder o argumento é o centro desta aula.
```

### 7. Entrega
Responda só com o bloco de código do arquivo do arco (10 episódios). Se o roteiro tiver algo inconsistente, avise em uma linha `# nota:` dentro do bloco.

---

## Depois de gerar (você, no repositório)

```bash
cd tools/pocket
# 1. salve o arquivo, por exemplo: b2_arco01.txt  (B1 usa arcos 46 a 80)
python3 dedupe.py b2_arco01.txt          # renomeia títulos/frases-chave repetidos
python3 validate.py | grep -v "^[0-9]"   # estrutura dos 7 quadros
python3 audit_vocab.py -v | grep -E "b2_|achados"   # carga de vocabulário
python3 audit_b1.py 'b1_arco*.txt' -v              # só para B1: bloqueia estruturas B2+
python3 revisar.py                        # repetições, pontuação, inglês solto no PT
# 2. integra só os arcos novos (o resto do nível fica intacto)
POCKET_REBUILD=b2 POCKET_ARCS=1-1 python3 build.py
# 3. publica
bash ship.sh "Pocket B2: arco 1 reescrito"
```

Observações: os níveis B2, C1 e C2 ainda **não têm porta automática de gramática** (só o B1 tem). Para esses níveis, a conferência de gramática depende do que o guia de nível do prompt pede e da revisão humana. Não rode `build.py` sem `POCKET_ARCS`: ele recusa reconstruir um nível inteiro quando isso apagaria episódios.
