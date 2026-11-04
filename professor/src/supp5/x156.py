X = dict(
 key=dict(big="Would you recommend it?", label="Falar de um livro", sub="No clube do livro, você agradece o convite, diz se terminou, fala do personagem favorito e da história e recomenda (ou não) o livro."),
 mini=[
  dict(who="Ava", en="Welcome! Did you finish the {book|novel|story}?", pt="Bem-vinda! Você terminou o {livro|romance|conto}?"),
  dict(who="You", en="Yes! I loved the {ending|plot|cover}.", pt="Sim! Adorei o {final|enredo|visual da capa}."),
  dict(who="Ava", en="Who's your favorite {character|writer|person}?", pt="Quem é seu {personagem|escritor|pessoa} favorito?"),
  dict(who="You", en="The grandmother. She's so {funny|kind|smart}.", pt="A avó. Ela é muito {engraçada|gentil|inteligente}."),
 ],
 dlg=[
  dict(who="Ava", en="Welcome to {book club!|my home!}", pt="Bem-vindos ao {clube do livro!|meu lar!}"),
  dict(who="You", en="{Thanks|Thank you} for having me.", pt="{Obrigada|Muito obrigada} por me receber."),
  dict(who="Ava", en="Did you finish the {book?|novel?}", pt="Você terminou o {livro?|romance?}"),
  dict(who="You", en="Yes, I {loved the ending.|liked the ending.}", pt="Sim, {adorei o final.|gostei do final.}"),
  dict(who="Ava", en="Who's your favorite {character?|writer?}", pt="Quem é seu {personagem|escritor} favorito?"),
  dict(who="You", en="The grandmother. She's so {funny.|kind.}", pt="A avó. Ela é muito {engraçada.|gentil.}"),
  dict(who="Ava", en="I agree. And the {story?|ending?}", pt="Concordo. E {a história?|o final?}"),
  dict(who="You", en="It's about a {family|town} and a {secret.|trip.}", pt="É sobre {uma família|uma cidade} e {um segredo.|uma viagem.}"),
  dict(who="Ava", en="Would you {recommend|suggest} it?", pt="Você {recomendaria|sugeriria} isso?"),
 ],
 vocab=[
  dict(w="page", pt="página", e="📄", ex=["Read one page, please.", "This page is funny."]),
  dict(w="chapter", pt="capítulo", e="🔖", ex=["I read one chapter today.", "Chapter two is short."]),
  dict(w="novel", pt="romance (livro)", e="📕", ex=["This novel is about a family.", "She reads a new novel."]),
  dict(w="cover", pt="capa", e="📗", ex=["The cover is red.", "What a nice cover!"]),
  dict(w="plot", pt="enredo", e="🧩", ex=["The plot is simple.", "I like the plot."]),
  dict(w="tea", pt="chá", e="🍵", ex=["We have tea and cookies.", "Do you want tea?"]),
 ],
 molds=[
  dict(title="Dizer o que você amou", frame="I loved the {thing}.", slots=[dict(key="thing", opts=["ending", "cover", "story", "plot"])], model="I loved the ending.", note="Loved é passado de love. Use the + parte do livro."),
  dict(title="Falar do personagem", frame="The {who} is so {adj}.", slots=[dict(key="who", opts=["grandmother", "grandfather", "dog"]), dict(key="adj", opts=["funny", "kind", "smart"])], model="The grandmother is so funny.", note="So + adjetivo = muito. Sem 'is' extra: The dog is so funny."),
  dict(title="Escrever uma recomendação", frame="The book is about a {a} and a {b}. I would recommend it to {who}.", slots=[dict(key="a", opts=["family", "boy", "dog"]), dict(key="b", opts=["secret", "trip", "mystery"]), dict(key="who", opts=["my sister", "my friends", "everyone"])], model="The book is about a family and a secret. I would recommend it to my sister.", note="The book is about... resume a história. I would recommend it to... recomenda."),
 ],
 sounds=[
  dict(say="Did you finish the book?", tag="junção: did you", tip="D + you vira 'didja'. Diga 'Di-djú fi-nish...' sem pausa."),
  dict(say="Would you recommend it?", tag="junção: would you", tip="Soa 'wouldja'. Una as duas palavras e acentue REC."),
  dict(say="Did you like the ending?", tag="junção: did you", tip="Mesmo som: 'didja'. Acentue LIKE e END."),
 ],
 role=dict(turns=[
  dict(npc="Welcome to book club!", opts=[
   dict(en="Thanks for having me.", pt="Obrigada por me receber.", reply="Come in! Sit on the sofa."),
   dict(en="Thank you for the invitation.", pt="Obrigada pelo convite.", reply="My pleasure! Have some tea."),
   dict(en="Hi, Ava! Your living room is nice.", pt="Oi, Ava! Sua sala é bonita.", reply="Thanks! Have a cookie.")]),
  dict(npc="Did you finish the book?", opts=[
   dict(en="Yes, I loved the ending.", pt="Sim, adorei o final.", reply="Me too! Who's your favorite character?"),
   dict(en="Yes, and I loved the cover.", pt="Sim, e adorei a capa.", reply="Nice! Who's your favorite character?"),
   dict(en="Almost. I am on the last chapter.", pt="Quase. Estou no último capítulo.", reply="No spoilers! Who's your favorite character?")]),
  dict(npc="Who's your favorite character?", opts=[
   dict(en="The grandmother. She's so funny.", pt="A avó. Ela é muito engraçada.", reply="I agree. And the story?"),
   dict(en="The dog. He's so kind.", pt="O cachorro. Ele é muito gentil.", reply="Aww, me too. And the story?"),
   dict(en="The teacher. She's so smart.", pt="A professora. Ela é muito inteligente.", reply="Good choice. And the story?")]),
  dict(npc="Would you recommend it?", opts=[
   dict(en="Yes! It's a great book.", pt="Sim! É um ótimo livro.", reply="Great. I'll read it next."),
   dict(en="Yes, to my sister.", pt="Sim, para minha irmã.", reply="Nice. Tell her the title!"),
   dict(en="Yes, if you like mysteries.", pt="Sim, se você gosta de mistério.", reply="I do! I'll buy it.")]),
 ], change=["Ava pergunta se você gostou do final, mas você não terminou o livro: diga que está no capítulo cinco.", "Você não gostou do livro: diga com educação que não foi seu favorito.", "Outra pessoa conta o final do livro: diga 'Spoiler alert!'."]),
 writing=dict(task="Escreva 2 ou 3 frases sobre um livro de que você gosta: o título, um personagem e se você recomenda.", model="The book is “Matilda.” My favorite character is Matilda. She is so smart. I would recommend it.", kw=["book", "character", "story", "recommend"], checks=["Disse de que livro fala.", "Falou de um personagem.", "Disse se recomenda."]),
 scenes=dict(pool=["living", "library", "bookshop", "garden"], npc=dict(g="f", role="friend"), you=dict(g="f")),
 convo=dict(npc=dict(name="Ava"), story="Você está pela primeira vez no clube do livro da Ava. Converse sobre o livro.", turns=[
  dict(npc="Welcome to book club!", pt="Bem-vindos ao clube do livro!", opts=[
   dict(en="Good night, see you next week!", pt="Boa noite, até a semana que vem!", ok=False, fb="Isso é despedida; você acabou de chegar."),
   dict(en="Thanks for having me.", pt="Obrigada por me receber.", ok=True, fb="Agradece o convite de forma natural."),
   dict(en="Did you finish the book?", pt="Você terminou o livro?", ok=False, fb="Essa pergunta é da Ava, não sua.")]),
  dict(npc="Did you finish the book?", pt="Você terminou o livro?", opts=[
   dict(en="Yes, I loved the ending.", pt="Sim, adorei o final.", ok=True, fb="Responde sim e dá uma opinião."),
   dict(en="Welcome to book club!", pt="Bem-vindos ao clube do livro!", ok=False, fb="Quem recebe é a anfitriã."),
   dict(en="No, thanks. I'm full.", pt="Não, obrigada. Estou satisfeita.", ok=False, fb="Responde a uma oferta de comida, não à pergunta.")]),
  dict(npc="Who's your favorite character?", pt="Quem é seu personagem favorito?", opts=[
   dict(en="Yes, I loved the ending.", pt="Sim, adorei o final.", ok=False, fb="Ela perguntou 'quem', não uma pergunta de sim ou não."),
   dict(en="Thanks for having me.", pt="Obrigada por me receber.", ok=False, fb="Você já agradeceu; agora responda."),
   dict(en="The grandmother. She's so funny.", pt="A avó. Ela é muito engraçada.", ok=True, fb="Diz quem e por quê.")]),
  dict(npc="I agree. And the story?", pt="Concordo. E a história?", opts=[
   dict(en="Yes, I agree.", pt="Sim, eu concordo.", ok=False, fb="Ela já concordou; pergunta sobre a história."),
   dict(en="It's about a family and a secret.", pt="É sobre uma família e um segredo.", ok=True, fb="Resume a história em uma frase."),
   dict(en="The grandmother again.", pt="A avó de novo.", ok=False, fb="Não fala da história.")]),
  dict(npc="Would you recommend it?", pt="Você recomendaria?", opts=[
   dict(en="It's about a family.", pt="É sobre uma família.", ok=False, fb="Você já contou a história; agora diga se recomenda."),
   dict(en="Yes, I finished it.", pt="Sim, eu terminei.", ok=False, fb="Não responde sobre recomendar."),
   dict(en="Yes, I would. It's a great book.", pt="Sim, recomendaria. É um ótimo livro.", ok=True, fb="Resposta completa e natural.")]),
 ]),
)
