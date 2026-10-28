# Padrão da ponte obra ↔ episódio

**Objetivo:** a obra do episódio não pode ficar só na capa e na figurinha. Ela precisa aparecer DENTRO da aula, ligada ao padrão do dia. Modelo de bom resultado: o episódio 7940066 (B2, *Fargo*).

## O que é a ponte (3 peças, todas obrigatórias)
1. **Uma fala da cena 1** (ou da cena 2) que fale da obra — personagem, lugar ou fato do enredo — **usando o padrão do dia**. Não é uma fala solta: é uma fala natural do diálogo, com o mesmo nível de língua do episódio.
2. **A missão “Cena da obra”** (a 1ª das 3 missões) reescrita: o enunciado cita a obra/personagem e pede uma frase que use o padrão do dia; o `model` mistura obra + padrão; os 3 `kw` são regex que casam com o `model` (e não casam com qualquer frase); `check`, `tips`, `ok` e `reply` combinam com isso.
3. **Elenco = personagens da obra** (nome e, quando existir, arte). Nesta rodada só medimos; trocar elenco genérico exige reconstruir o episódio (fica para outra etapa).

## Regras de qualidade
- **Só fatos verdadeiros e seguros** sobre a obra (personagem, cidade, objeto, evento central). Nada de ano, número ou detalhe do qual você não tenha certeza. Em dúvida, use algo geral (“o tornado leva Dorothy para Oz”).
- **Sem citar trechos protegidos:** paráfrase curta; no máximo 8 palavras iguais ao original.
- **Nível do episódio:** A1 frases curtas e concretas; A2 rotina/passado simples; B1 planos e opiniões; B2 nuance. Não suba o nível.
- **Mesmo padrão (`gs`) e mesmas palavras do episódio:** a fala e a missão ENSINAM o padrão do dia (não o do vizinho). Reuse vocabulário e verbos do episódio.
- **Troque só 1–2 falas** (2 no máximo). Não troque a fala que as perguntas de compreensão citam em “why” (o validador avisa). Mantenha o falante e a coerência com as falas ao redor.
- **Traduções:** português do Brasil natural, fiel, e consistente com o resto do curso.
- **Missão:** `prompt` em português com a tarefa em **negrito**; `model` em inglês (idioma-alvo); 3 `check` (“Usei …?”), 3 `kw` (regex em inglês que casam com o `model`; o 1º cobre o padrão, o 2º a obra/personagem, o 3º o complemento), 3 `tips` (listas de `[frase, tradução]`), 3 `ok` (reações curtas com emoji), `reply` `[frase, tradução]`.

## Formato do patch (`tools/audit/bridge_patches/<curso>_<parte>.json`)
```json
[{"n": 7010178,
  "cena": [{"cena": 1, "i": 5, "en": "…", "pt": "…"}],
  "missao": {"prompt": "…", "model": "…", "chips": ["…"], "check": ["…","…","…"], "kw": ["\\b…\\b","\\b…\\b","\\b…\\b"],
             "tips": [[["…","…"]],[["…","…"]],[["…","…"]]], "ok": ["…","…","…"], "reply": ["…","…"]}}]
```
`i` é o índice (começa em 0) da fala dentro da cena; `cena` é 1 ou 2.

## Como validar e aplicar
- Simular (não grava): `python3 tools/audit/apply_bridge_patches.py --check tools/audit/bridge_patches/<arquivo>.json`
- Aplicar: `python3 tools/audit/apply_bridge_patches.py` (idempotente; reaplicar depois de qualquer reconstrução dos dados)
- Medir: `python3 tools/audit/regular_bridge_audit.py` (P2 = obra nas cenas, P3 = missão ligada à obra) e `python3 tools/audit/regular_pilot_contract.py`.

## Exemplo antes/depois (A1, episódio 7010178, *It’s a Wonderful Life*, padrão save · spend · earn)
Antes: cena genérica de banco (“I work at the bank. I earn money.”) e missão “Fale como na obra. Diga: Eu trabalho no banco…” sem citar a obra.
Depois (modelo): fala — *“George: At the Bailey building and loan, I earn a little and I save a little.”* (George Bailey dirige uma cooperativa de crédito na obra); missão — *“Você é George Bailey. **Diga que você ganha pouco, que você guarda dinheiro e que a cidade gasta menos que você.**”*, `model` “I earn a little. I save money for my family. I do not spend much.”
