X = dict(
 key=dict(big="I'd like a library card", label="Pedir a carteirinha", sub="Na biblioteca, diga que quer a carteirinha, mostre um documento e uma conta com seu endereço, preencha o formulário e pergunte se é grátis."),
 mini=[
  dict(who="You", en="Hi! I'd like a {library card|new card|book}, please.", pt="Oi! Eu gostaria de {uma carteirinha da biblioteca|uma carteirinha nova|um livro}, por favor."),
  dict(who="Carlos", en="Sure. Do you have {an ID?|a passport?|a bill?}", pt="Claro. Você tem {um documento?|um passaporte?|uma conta?}"),
  dict(who="You", en="Yes, here's my {passport.|ID.|phone bill.}", pt="Tenho, aqui está {meu passaporte.|meu documento.|minha conta de telefone.}"),
  dict(who="Carlos", en="Great. Please fill out this {form.|page.|card.}", pt="Ótimo. Preencha {este formulário.|esta página.|esta ficha.}"),
 ],
 dlg=[
  dict(who="Carlos", en="Hi! I'd like a {library card,|new card,} please.", pt="Oi! Eu gostaria de {uma carteirinha da biblioteca,|uma carteirinha nova,} por favor."),
  dict(who="You", en="Sure. Do you have an {ID?|passport?}", pt="Claro. Você tem um {documento?|passaporte?}"),
  dict(who="Carlos", en="Yes, here's my {passport.|ID.}", pt="Tenho, aqui está {meu passaporte.|meu documento.}"),
  dict(who="You", en="And a {bill|letter} with your address?", pt="E uma {conta|carta} com seu endereço?"),
  dict(who="Carlos", en="Here's my {phone|water} bill.", pt="Aqui está minha conta de {telefone.|água.}"),
  dict(who="You", en="Great. Please {fill out|sign} this {form.|page.}", pt="Ótimo. Por favor, {preencha|assine} {este formulário.|esta página.}"),
  dict(who="Carlos", en="OK. Is the card {free?|ready?}", pt="Ok. A carteirinha é {grátis?|pronta?}"),
  dict(who="You", en="Yes, it's {free.|ready.}", pt="Sim, é {grátis.|grátis.}"),
  dict(who="Carlos", en="Here's your {card.|book.}", pt="Aqui está sua {carteirinha.|carteirinha.}"),
 ],
 vocab=[
  dict(w="library", pt="biblioteca", e="🏛️", ex=["The library is quiet.", "I go to the library on Saturday."]),
  dict(w="librarian", pt="bibliotecário(a)", e="🧑‍🏫", ex=["The librarian is kind.", "Ask the librarian."]),
  dict(w="borrow", pt="pegar emprestado", e="🤝", ex=["I borrow two books.", "Can I borrow this book?"]),
  dict(w="due date", pt="data de devolução", e="📅", ex=["The due date is Friday.", "What is the due date?"]),
  dict(w="form", pt="formulário", e="📋", ex=["Fill out the form.", "This form is short."]),
  dict(w="author", pt="autor(a)", e="✍️", ex=["Who is the author?", "She is my favorite author."]),
 ],
 molds=[
  dict(title="Pedir a carteirinha", frame="Hi! I'd like a {thing}, please.", slots=[dict(key="thing", opts=["library card", "new card", "book", "form"])], model="Hi! I'd like a library card, please.", note="I'd like... é educado. Library card = carteirinha da biblioteca."),
  dict(title="Mostrar documentos", frame="Here's my {doc}.", slots=[dict(key="doc", opts=["passport", "ID", "phone bill", "water bill"])], model="Here's my passport.", note="Here's my... ao entregar algo. Phone bill = conta de telefone."),
  dict(title="Escrever o recado", frame="I'd like to borrow {n} {thing}. When is the due date?", slots=[dict(key="n", opts=["two", "three", "four"]), dict(key="thing", opts=["books", "movies", "magazines"])], model="I'd like to borrow two books. When is the due date?", note="Borrow = pegar emprestado. Due date = último dia para devolver."),
 ],
 sounds=[
  dict(say="I'd like a library card.", tag="ritmo: I'd LIKE a LI-brary CARD", tip="Acentue LIKE, LI e CARD. A palavra library tem o r forte no meio: LAI-brer-i."),
  dict(say="Here's my passport.", tag="ligação: Here's my", tip="Junte Here's e my sem pausa. O s liga ao m: 'hirz-mai'."),
  dict(say="Is the card free?", tag="som: th de the", tip="Ponha a ponta da língua entre os dentes em 'the'. Não diga 'zi' nem 'di'."),
 ],
 role=dict(turns=[
  dict(npc="Hi! Can I help you?", opts=[
   dict(en="Yes. I'd like a library card, please.", pt="Sim. Eu gostaria de uma carteirinha da biblioteca, por favor.", reply="Sure. Do you have an ID?"),
   dict(en="Hi! How do I get a library card?", pt="Oi! Como eu consigo uma carteirinha?", reply="You need an ID. Do you have one?"),
   dict(en="Hello. I want to join the library.", pt="Olá. Quero me inscrever na biblioteca.", reply="Great. Do you have an ID?")]),
  dict(npc="Do you have an ID and a bill with your address?", opts=[
   dict(en="Yes, here's my passport and my phone bill.", pt="Tenho, aqui estão meu passaporte e minha conta de telefone.", reply="Great. Please fill out this form."),
   dict(en="I have an ID, but no bill. Is that OK?", pt="Tenho documento, mas não tenho conta. Tudo bem?", reply="Hmm, you can use a letter with your address."),
   dict(en="Here's my ID. My bill is online.", pt="Aqui está meu documento. Minha conta é online.", reply="That's fine. Show it on your phone.")]),
  dict(npc="Please fill out this form.", opts=[
   dict(en="OK. Is the card free?", pt="Ok. A carteirinha é grátis?", reply="Yes, it's free."),
   dict(en="OK. Do you have a pen?", pt="Ok. Você tem uma caneta?", reply="Sure, here's a pen."),
   dict(en="OK. Is it long?", pt="Ok. É longo?", reply="No, it's very short.")]),
  dict(npc="Here's your card.", opts=[
   dict(en="Thank you! Can I borrow books now?", pt="Obrigado! Posso pegar livros agora?", reply="Yes. You can borrow five books."),
   dict(en="Thanks! What is the due date?", pt="Obrigado! Qual é a data de devolução?", reply="Books are due in three weeks."),
   dict(en="Great! Where are the movies?", pt="Ótimo! Onde ficam os filmes?", reply="On the second floor.")]),
 ], change=["Você esqueceu o documento: pergunte se pode voltar amanhã.", "A conta não tem o seu nome: explique e pergunte o que mais serve.", "O livro que você quer já foi emprestado: pergunte se pode reservar."]),
 writing=dict(task="Escreva 2 ou 3 frases para a bibliotecária: peça uma carteirinha, mostre seu documento e pergunte se é grátis.", model="Hi! I'd like a library card, please. Here's my passport. Is the card free?", kw=["library", "card", "passport", "free"], checks=["Pediu a carteirinha.", "Falou do documento.", "Perguntou se é grátis."]),
 scenes=dict(pool=["library", "lobby", "counter", "bookshop"], npc=dict(g="f", role="librarian"), you=dict(g="m")),
 convo=dict(npc=dict(name="Ms. Hill"), story="Você quer uma carteirinha da biblioteca. A Ms. Hill atende no balcão.", turns=[
  dict(npc="Hi! Can I help you?", pt="Oi! Posso ajudar?", opts=[
   dict(en="Sure. Do you have an ID?", pt="Claro. Você tem um documento?", ok=False, fb="Quem pergunta isso é ela."),
   dict(en="Yes. I'd like a library card, please.", pt="Sim. Eu gostaria de uma carteirinha, por favor.", ok=True, fb="Primeiro passo: dizer o que você quer."),
   dict(en="Here's your card.", pt="Aqui está sua carteirinha.", ok=False, fb="Ela dá a carteirinha, não você.")]),
  dict(npc="Sure. Do you have an ID?", pt="Claro. Você tem um documento?", opts=[
   dict(en="Yes, here's my passport.", pt="Tenho, aqui está meu passaporte.", ok=True, fb="Responde e entrega o documento."),
   dict(en="Please fill out this form.", pt="Preencha este formulário.", ok=False, fb="Quem entrega o formulário é ela."),
   dict(en="Is the card free?", pt="A carteirinha é grátis?", ok=False, fb="Ainda não é o momento; ela perguntou do documento.")]),
  dict(npc="And a bill with your address?", pt="E uma conta com seu endereço?", opts=[
   dict(en="I'd like a library card.", pt="Eu gostaria de uma carteirinha.", ok=False, fb="Você já pediu isso."),
   dict(en="Here's my phone bill.", pt="Aqui está minha conta de telefone.", ok=True, fb="Mostra a conta com o endereço."),
   dict(en="Yes, it's free.", pt="Sim, é grátis.", ok=False, fb="Não responde à pergunta.")]),
  dict(npc="Great. Please fill out this form.", pt="Ótimo. Preencha este formulário.", opts=[
   dict(en="Do you have an ID?", pt="Você tem um documento?", ok=False, fb="Ela já viu seu documento."),
   dict(en="OK. Is the card free?", pt="Ok. A carteirinha é grátis?", ok=True, fb="Pergunta natural sobre o preço."),
   dict(en="Here's my passport.", pt="Aqui está meu passaporte.", ok=False, fb="Você já mostrou.")]),
  dict(npc="Yes, it's free. Here's your card.", pt="Sim, é grátis. Aqui está sua carteirinha.", opts=[
   dict(en="Thank you very much!", pt="Muito obrigado!", ok=True, fb="Agradecimento natural."),
   dict(en="And a bill with your address?", pt="E uma conta com seu endereço?", ok=False, fb="Essa pergunta é dela."),
   dict(en="Please fill out this form.", pt="Preencha este formulário.", ok=False, fb="Você já preencheu.")]),
 ]),
)
