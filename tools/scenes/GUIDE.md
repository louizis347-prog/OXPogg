# Guia — reatribuir o CENÁRIO de cada capa (inglês regular) pela obra e pela situação da aula

**Problema:** só havia 42 cenários para ~3.000 capas; repetiam demais e muitas vezes não tinham relação com a obra. Agora a biblioteca tem **112 cenários** (`tools/scenes/catalogo.json`: nome → descrição e para que serve). Sua tarefa: para cada episódio do seu lote, escolher o cenário (e hora/decoração) que **faz sentido para o aluno ao olhar a capa**: onde a obra se passa, ou o que ela evoca, junto com a situação que a aula ensina. **Elenco e objeto ficam como estão**; só muda o cenário.

## Entrega
`tools/scenes/out/<LOTE>.json`: `{ "<n>": {"scene":"london","tod":"day","decor":[],"motivo":"Paddington vive em Londres"} , ... }` — um item por episódio do brief (`tools/scenes/briefs/<LOTE>.json`, campo `alvo`). Não edite `data/` nem `tools/ficha/`, não faça commit. Valide: `python3 tools/scenes/check.py <LOTE>` até `problemas: 0`.

## Como escolher (nesta ordem de importância)
1. **Relação com a obra:** onde ela acontece ou a sua marca visual (Londres para Paddington/Sherlock/Dickens; Paris; faroeste para westerns; savana para Rei Leão; tribunal para dramas jurídicos; cinema para filmes sobre cinema; etc.). Obras sem lugar específico (canções, ideias, poemas): use o cenário da **situação da aula** (restaurante, aeroporto, consultório/hospital, escritório, supermercado, estádio…) ou um que combine com o clima da obra.
2. **Relação com a aula** (`aula`, `foco`): a situação que o aluno vai treinar (pedir comida → restaurante/cafe/diner; viajar → airport/station/traincar; consulta → hospital/pharmacy; trabalho → office/bank…).
3. **Prefira cenários específicos** (london, courtroom, airport, savanna…) aos genéricos (meadow, village, city, park, hills, plaza). Genéricos só quando não houver nada melhor, e no máximo 10% do lote.
4. **Variedade:** no seu lote, nenhum cenário mais de **8 vezes**, **mínimo de 35 cenários distintos**, e **nunca o mesmo cenário em dois episódios seguidos** (ordem do brief). Não use os apelidos `plaza`, `skyline`, `beach` (use village, city, seaside).
5. **Coerência com o elenco/objeto atuais** (`elenco`, `prop`): se o elenco é um cowboy, o cenário não pode ser um escritório; se o objeto é um barco, procure água (seaside, harbor, piratecove, venice, mississippi, lighthouse).
6. `tod`: `day`, `dawn`, `dusk`, `night` ou `indoor` (use `indoor` nos cenários internos: classroom, kitchen, office, courtroom, cinema, hospital, restaurante, etc.). Combine com o clima da obra (terror → night; Natal → snow/night; final feliz → dusk/dawn).
7. `decor` (opcional): flowers, mushrooms, butterflies, birds, clouds, balloons, stars, hearts, leaves, snow, bubbles, fireflies, sparkles, grass. **Padrão: `[]`** (os cenários novos já são completos). Só use decor onde fizer sentido (nada de `hearts` em tribunal; `snow` só em cenários de neve; `leaves` em outono).
8. Cada `motivo` em português, uma frase curta que explica a escolha (a relação com a obra ou a aula).

## Antes de entregar
`python3 tools/scenes/check.py <LOTE>` com `problemas: 0`. Releia 10 itens ao acaso: o aluno entenderia por que aquele cenário está ali? Responda com um resumo curto (quantos cenários distintos e ressalvas).
