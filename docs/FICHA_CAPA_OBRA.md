# Ficha de capa da obra (capa feita para a obra, não gerada ao acaso)

Cada episódio de curso regular tem uma **ficha** que diz ao desenhista da plataforma o que mostrar na capa da obra: quem aparece, o que carrega, onde está, a hora do dia e o **objeto-símbolo**. O gerador (`js/obra-ficha.js`) monta a capa a partir da ficha com as peças ilustradas de `js/obra-ficha-lib.js` (mesmo traço de nanquim das capas desenhadas à mão). Sem ficha, vale o gerador antigo (`js/obra-art.js`); com a trava ligada, toda obra precisa de ficha.

## Objetivo
Quem conhece a obra deve **reconhecê-la só pela capa**: o personagem certo, com a roupa, a cor e o adereço que o tornam inconfundível, o objeto que resume a história, o cenário típico. Duas obras diferentes nunca podem ter a mesma capa.

## Formato (um arquivo JSON por lote, chave = `n` do episódio)
```json
{"7070008": {
  "t": "Dick Whittington and His Cat",
  "scene": "village", "tod": "dawn",
  "cast": [
    {"p": {"hs":"short","hair":"brown","outfit":"coat","top":"#8a5a2b","hat":"cap","hatColor":"#6a3f22","arms":"hold","holds":"suitcase"}},
    {"a": "cat", "c": "#e8923a", "s": 1.4}
  ],
  "prop": {"id": "bell", "at": "sky-right", "s": 1.4},
  "decor": ["birds","clouds"]
}}
```
- `t`: título da obra (só para você conferir a folha).
- `scene`: cenário. `tod`: hora do dia.
- `cast`: 1 a 4 personagens. **Pessoa** = `{"p": {...}}`; **bicho** = `{"a": "<bicho>", "c": "#cor", "c2": "#cor2"}`. Fora de `p`/`a`: `s` (escala), `x` (posição horizontal 40–760), `y` (linha do chão), `flip` (espelha), `back` (desenha atrás).
- `prop`: o **objeto-símbolo** da obra: `{"id","c"(cor),"s"(escala),"at","x","y"}`. `at`: onde fica. Se um personagem segura o objeto, use `p.holds` em vez de `prop` (e `p.arms: "hold"`), ou os dois (objeto-símbolo grande + um personagem segurando outro).
- `decor`: enfeites do cenário (opcional).
- `accent`: cor `#rrggbb` que tinge o cenário (opcional). `falta`: lista de peças que você precisou e **não existem** (veja abaixo).

### Pessoa (`p`): campos aceitos
`hs` (cabelo, obrigatório), `outfit` (roupa, obrigatório), `hair` (cor do cabelo: nome ou `#rrggbb`), `skin` (pele: nome ou `#rrggbb`), `top` (cor da roupa), `bot` (cor da calça), `shirt` (camisa sob macacão), `shoe`, `hat`, `hatColor`, `beard`, `stache` (cor do bigode/barba: nome de cabelo), `glasses` (true), `freckles` (true), `arms`, `holds` (objeto na mão), `holdColor`, `cape` (capa, cor), `wings` (asas, cor), `scarf`, `trim` (barra do vestido), `tie`, `belt`, `band` (faixa), `ribbon` (laço das tranças), `apron` (true: avental no vestido), `skirt` (true: saia da armadura), `emblem`, `stripe`, `num` (número da camisa), `ears` (true: orelhas).

## Vocabulário (só estas peças existem)
- **hs** (cabelo): short, long, bob, braids, pigtails, ponytail, afro, curly, bun, side, spiky, bald
- **outfit** (roupa): shirt, dress, suit, overalls, robe, coat, apron, jersey, armor
- **hat** (chapéu): cowboy, cap, basecap, top, turban, crown, witch, wizard, helmet, beret, hood, bonnet, party, chef, sailor, pirate, flower, bow, santa, headscarf, fez, leaf, ears, deerstalker, bowler, tricorn
- **skin** (pele): pale, light, tan, brown, dark, deep
- **hair** (cor do cabelo): blond, brown, black, red, gray, white, auburn, blue, pink, green
- **arms**: down, wave, up, out, point, hold, hug, fly
- **a** (bichos): rabbit, cat, dog, bear, pig, duck, fox, wolf, lion, mouse, owl, frog, bird, horse, sheep, cow, dragon, elephant, monkey, turtle, penguin, fish, snail, bee, dinosaur, hen, rooster, goose, crow, stork, goat, hare, caterpillar, gorilla, panda, ladybug, spider, whale, giraffe, crocodile, squirrel, deer, parrot, camel, kangaroo, snake, bat, ghost, elf, unicorn, kitten, puppy, chick, lamb
- **prop.id / p.holds** (objetos): clock, key, lamp, book, crown, wand, star, apple, slipper, umbrella, balloon, boat, ship, sword, shield, magnifier, flower, cake, teapot, cup, suitcase, kite, drum, guitar, bell, lantern, chest, map, compass, mirror, basket, bone, ball, rocket, moon, sun, heart, egg, carrot, pumpkin, snowman, tree, house, castle, bicycle, train, airplane, paintbrush, pencil, trophy, camera, telephone, envelope, feather, acorn, mushroom, bread, cheese, icecream, sandwich, pizza, soccerball, scissors, hammer, ladder, ring, bowl, trumpet, piano, microphone, cloud, rainbow, lightning, snowflake, anchor, hourglass, gift, poster, well, windmill, signpost, pie, cauldron, cookie, grapes, jug, boot, candle, harp, wheel, flag, tent, car, bus, turnip, beanstalk, feast, tophat, spoon, muffin, porridge, shoehouse, eggs, pearl, bagpipe
- **prop.at**: front, sky, left, right, between, sky-left, sky-right, held
- **scene** (cenário): meadow, forest, hills, castle, village, farm, seaside, harbor, ship, mountain, snow, desert, jungle, city, park, school, classroom, kitchen, livingroom, bedroom, library, market, station, circus, stage, garden, pond, cave, space, underwater, bakery, playground, barn, bridge, camp, skyline, beach, attic, throne, workshop, plaza, road
- **tod** (hora): day, dawn, dusk, night, indoor
- **decor**: flowers, mushrooms, butterflies, birds, clouds, balloons, stars, hearts, leaves, snow, bubbles, fireflies, sparkles, grass

## Regras de qualidade (a trava confere o que dá para conferir)
1. **Fiel à obra.** Escolha o que torna a obra reconhecível: personagem principal com a **cor e o adereço** típicos (chapéu vermelho, vestido azul, capa, coroa…), o **bicho certo** na cor certa, o objeto-símbolo (relógio, abóbora, chinelo de cristal, pé de feijão…), o cenário típico (castelo, fazenda, barco, jardim…). Só fatos que você sabe que são verdadeiros; em dúvida, fique no que é geral.
2. **Elenco = a obra.** Os personagens da capa são os da obra (e do episódio: `elenco` no brief). Nada de pessoas genéricas.
3. **Para música, cantiga, poema, lugar ou tradição:** mostre quem a obra evoca (as crianças da cantiga, o animal do poema, o monumento no cenário mais próximo) com o objeto-símbolo.
4. **Personagens adultos** usam `s` de 1.25 a 1.35; crianças `s` 1; bichos pequenos (rato, pato, aranha, sapo) `s` 1.6 a 2.2; bichos grandes (vaca, elefante, urso) `s` 0.9 a 1.2. Evite que um personagem cubra o outro; com 3+, abra espaço com `x`.
5. **Variedade obrigatória:** nenhuma ficha pode repetir a combinação **personagens + objeto + cenário** de outra do curso, nem o mesmo objeto na mesma cena, nem o mesmo elenco na mesma cena. Varie hora do dia, cores e enfeites também.
6. **Todo objeto-símbolo existe no vocabulário.** Se a obra pede uma peça que não existe (ex.: uma tocha da Estátua da Liberdade, um barco a vapor), escolha o mais próximo e anote em `falta` (`"falta": ["tocha"]`). Não invente ids.
7. **Cores** sempre `#rrggbb` (exceto os nomes de pele/cabelo do vocabulário).
8. Não copie personagens protegidos traço a traço: a ficha descreve uma **versão estilizada** (cores e adereços, não rostos nem logotipos).

## Ferramentas
- Folha de capas (PNG) do seu lote: `NODE_PATH=$(npm root -g) node tools/ficha/render_sheet.js tools/ficha/work/<seu>.json /tmp/<seu>.png 4`, depois **abra o PNG** e confira se cada capa é reconhecível, sem sobreposição estranha.
- Exemplos prontos: `tools/ficha/exemplos.json` e a imagem `tools/ficha/exemplos.png`.
- Validar: `python3 tools/ficha/validate.py --meu tools/ficha/work/<seu>.json` (confere vocabulário e unicidade contra todos os lotes).
- Biblioteca visual: `tools/ficha/lib.html?k=animals|props|hats|people` (abra com um servidor local se quiser) ou veja os PNG em `tools/ficha/`.
