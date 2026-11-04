X = dict(
 key=dict(big="I like your jacket", label="Elogiar e agradecer", sub="Elogie algo simples e responda a um elogio com thank you mais um comentário curto."),
 mini=[
  dict(who="Omar", en="Hey! I like your {jacket|bag|shirt}.", pt="Oi! Gosto da sua {jaqueta|bolsa|camisa}."),
  dict(who="You", en="Thank you! It's {new|a gift|from the mall}.", pt="Obrigada! {É nova|Foi presente|É do shopping}."),
  dict(who="Omar", en="The {color|style|blue} looks great on you.", pt="{A cor|O estilo|O azul} fica ótimo em você."),
  dict(who="You", en="You're so {kind.|nice.|sweet.} I like your bag.", pt="Você é muito {gentil.|legal.|querido.} Gosto da sua bolsa."),
 ],
 dlg=[
  dict(who="Omar", en="Hey! I like your {jacket.|bag.}", pt="Oi! Gosto da sua {jaqueta.|bolsa.}"),
  dict(who="You", en="Thank you! It's {new.|nice.}", pt="Obrigada! É {nova.|legal.}"),
  dict(who="Omar", en="Where did you {get|buy} it?", pt="Onde você {comprou|comprou} isso?"),
  dict(who="You", en="At the {mall,|store,} downtown.", pt="No {shopping|loja} do centro."),
  dict(who="Omar", en="The {color|style} looks great on you.", pt="{A cor|O estilo} fica ótimo em você."),
  dict(who="You", en="You're so {kind.|sweet.} I like your bag.", pt="Você é muito {gentil.|querido.} Gosto da sua bolsa."),
  dict(who="Omar", en="Thanks! It was a {gift.|present.}", pt="Valeu! Foi {presente.|presente.}"),
  dict(who="You", en="It's really {beautiful.|pretty.}", pt="É muito {bonita.|linda.}"),
  dict(who="Omar", en="Your {hair|jacket} looks nice, too.", pt="Seu {cabelo|casaco} está bonito também."),
 ],
 vocab=[
  dict(w="color", pt="cor", e="🎨", ex=["I like this color.", "What color is your bag?"]),
  dict(w="pretty", pt="bonito(a)", e="🌸", ex=["Your bag is pretty.", "That is a pretty color."]),
  dict(w="nice", pt="legal, bonito", e="👍", ex=["Your hair looks nice.", "What a nice jacket!"]),
  dict(w="beautiful", pt="lindo(a)", e="✨", ex=["The gift is beautiful.", "You look beautiful today."]),
  dict(w="style", pt="estilo", e="👗", ex=["I like your style.", "This is my style."]),
  dict(w="compliment", pt="elogio", e="💬", ex=["Thank you for the compliment.", "She gives me a compliment."]),
 ],
 molds=[
  dict(title="Elogiar algo", frame="I like your {thing}.", slots=[dict(key="thing", opts=["jacket", "bag", "shirt", "hair"])], model="I like your jacket.", note="I like your + coisa. Não use 'of' depois de like."),
  dict(title="Elogiar a cor", frame="The {thing} looks {adj} on you.", slots=[dict(key="thing", opts=["color", "jacket", "shirt"]), dict(key="adj", opts=["great", "nice", "good"])], model="The color looks great on you.", note="Looks great on you = fica ótimo em você."),
  dict(title="Escrever uma resposta", frame="Thank you! It's {adj}. I got it {where}.", slots=[dict(key="adj", opts=["new", "a gift", "my favorite"]), dict(key="where", opts=["at the mall", "downtown", "last week"])], model="Thank you! It's new. I got it at the mall.", note="Agradeça e acrescente um detalhe: onde ou quando você comprou."),
 ],
 sounds=[
  dict(say="Thank you! It's new.", tag="o th de thank", tip="Ponha a ponta da língua entre os dentes e solte o ar: 'thank', não 'tank' nem 'fank'."),
  dict(say="I like your jacket.", tag="ligação: like your", tip="Una like e your: 'laik-yor'. Acentue LIKE e JACK."),
  dict(say="Looks great on you.", tag="ligação: looks great on", tip="Una great on: 'greit-on'. Acentue LOOKS e GREAT."),
 ],
 role=dict(turns=[
  dict(npc="Hey! I like your jacket.", opts=[
   dict(en="Thank you! It's new.", pt="Obrigada! É nova.", reply="Where did you get it?"),
   dict(en="Thanks! It's a gift.", pt="Valeu! Foi presente.", reply="Where did you get it?"),
   dict(en="Thank you! I like it, too.", pt="Obrigada! Eu também gosto.", reply="Where did you get it?")]),
  dict(npc="Where did you get it?", opts=[
   dict(en="At the mall, downtown.", pt="No shopping do centro.", reply="The color looks great on you."),
   dict(en="At a small store near here.", pt="Em uma lojinha aqui perto.", reply="The color looks great on you."),
   dict(en="My sister gave it to me.", pt="Minha irmã me deu.", reply="The color looks great on you.")]),
  dict(npc="The color looks great on you.", opts=[
   dict(en="You're so kind. I like your bag.", pt="Você é muito gentil. Gosto da sua bolsa.", reply="Thanks! It was a gift."),
   dict(en="Thank you! I like your bag.", pt="Obrigada! Gosto da sua bolsa.", reply="Thanks! It was a gift."),
   dict(en="That's so sweet. Nice bag!", pt="Que gentil. Que bolsa legal!", reply="Thanks! It was a gift.")]),
  dict(npc="Thanks! It was a gift.", opts=[
   dict(en="It's really beautiful.", pt="É muito bonita.", reply="Your hair looks nice, too."),
   dict(en="It's so pretty.", pt="É tão bonita.", reply="Your hair looks nice, too."),
   dict(en="What a nice gift!", pt="Que presente legal!", reply="Your hair looks nice, too.")]),
 ], change=["Omar diz que a jaqueta é bonita, mas você não gosta dela: agradeça sem mentir muito.", "Omar pergunta o preço: responda de forma educada ou mude de assunto.", "Você quer elogiar o sapato dele: faça um elogio e pergunte onde comprou."]),
 writing=dict(task="Um colega elogiou sua jaqueta. Escreva 2 ou 3 frases: agradeça, diga onde comprou e elogie algo dele.", model="Thank you! It's new. I got it at the mall. I like your bag, too!", kw=["thank", "jacket", "mall", "like"], checks=["Agradeceu o elogio.", "Disse onde comprou.", "Elogiou algo do colega."]),
 scenes=dict(pool=["cafe", "cafe2", "cafe3", "street", "shop"], npc=dict(g="m", role="friend"), you=dict(g="f")),
 convo=dict(npc=dict(name="Omar"), story="Você está em um café em Austin com a jaqueta nova. O Omar puxa conversa.", turns=[
  dict(npc="Hey! I like your jacket.", pt="Oi! Gosto da sua jaqueta.", opts=[
   dict(en="Where did you get it?", pt="Onde você comprou?", ok=False, fb="Quem pergunta isso é ele."),
   dict(en="Thank you! It's new.", pt="Obrigada! É nova.", ok=True, fb="Agradecer e dar um detalhe."),
   dict(en="I like your jacket, too.", pt="Gosto da sua jaqueta também.", ok=False, fb="Ele não falou da jaqueta dele.")]),
  dict(npc="Where did you get it?", pt="Onde você comprou?", opts=[
   dict(en="Thank you for the question.", pt="Obrigada pela pergunta.", ok=False, fb="Estranho para uma pergunta simples."),
   dict(en="It was a gift.", pt="Foi presente.", ok=False, fb="Não combina com o diálogo: você disse que é nova e a pergunta é o lugar."),
   dict(en="At the mall, downtown.", pt="No shopping do centro.", ok=True, fb="Responde o lugar.")]),
  dict(npc="The color looks great on you.", pt="A cor fica ótima em você.", opts=[
   dict(en="You're so kind. I like your bag.", pt="Você é muito gentil. Gosto da sua bolsa.", ok=True, fb="Agradece e devolve o elogio."),
   dict(en="At the mall, downtown.", pt="No shopping do centro.", ok=False, fb="Já respondeu isso."),
   dict(en="No, the color is bad.", pt="Não, a cor é ruim.", ok=False, fb="Negar o elogio soa estranho.")]),
  dict(npc="Thanks! It was a gift.", pt="Valeu! Foi presente.", opts=[
   dict(en="You're so kind.", pt="Você é muito gentil.", ok=False, fb="Ele não elogiou você agora."),
   dict(en="It's really beautiful.", pt="É muito bonita.", ok=True, fb="Elogia a bolsa."),
   dict(en="I like your hair.", pt="Gosto do seu cabelo.", ok=False, fb="Fora de contexto: a conversa é sobre a bolsa.")]),
  dict(npc="Your hair looks nice, too.", pt="Seu cabelo está bonito também.", opts=[
   dict(en="Thank you! That's so sweet.", pt="Obrigada! Que gentil.", ok=True, fb="Resposta natural e simpática."),
   dict(en="It was a gift.", pt="Foi presente.", ok=False, fb="Cabelo não é presente."),
   dict(en="Where did you get it?", pt="Onde você comprou?", ok=False, fb="Não se compra cabelo.")]),
 ]),
)
