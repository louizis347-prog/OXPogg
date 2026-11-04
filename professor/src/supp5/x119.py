X = dict(
 key=dict(big="Job application", label="Ficha de emprego", sub="Diga que veio pela vaga, receba o formulário e informe nome, telefone e e-mail em inglês."),
 mini=[
  dict(who="You", en="Hello! I'm here for the {job application.|interview.|job.}", pt="Olá! Estou aqui para a {ficha de emprego.|entrevista.|vaga.}"),
  dict(who="Malik", en="Great. Please take this {form.|paper.|pen.}", pt="Ótimo. Pegue este {formulário.|papel.|caneta.}"),
  dict(who="You", en="Here is my {name|address|phone number}.", pt="Aqui está meu {nome|endereço|telefone}."),
  dict(who="Malik", en="What's your {email?|address?|phone number?}", pt="Qual é seu {e-mail?|endereço?|telefone?}"),
 ],
 dlg=[
  dict(who="Malik", en="Hello! I'm here for the job {application.|interview.}", pt="Olá! Estou aqui para a {ficha de emprego.|entrevista.}"),
  dict(who="You", en="Great. Please take this {form.|paper.}", pt="Ótimo. Pegue este {formulário.|papel.}"),
  dict(who="Malik", en="What do I write {first?|next?}", pt="O que escrevo {primeiro?|em seguida?}"),
  dict(who="You", en="Your name and {address.|phone number.}", pt="Seu nome e {endereço.|telefone.}"),
  dict(who="Malik", en="Here is my name: {Noor Ali.|Sara Lee.}", pt="Aqui está meu nome: {Noor Ali.|Sara Lee.}"),
  dict(who="You", en="And your {phone number?|email?}", pt="E seu {telefone?|e-mail?}"),
  dict(who="Malik", en="It's five five five, one four two two.", pt="É cinco cinco cinco, um quatro dois dois."),
  dict(who="You", en="What's your {email?|address?}", pt="Qual é seu {e-mail?|endereço?}"),
  dict(who="Malik", en="It's {noor|sara} at {mail|web} dot com.", pt="É {noor|sara} arroba {mail|web} ponto com."),
 ],
 vocab=[
  dict(w="signature", pt="assinatura", e="🖋️", ex=["I need your signature.", "Write your signature here."]),
  dict(w="application", pt="ficha de candidatura", e="📝", ex=["I have a job application.", "The application is on the desk."]),
  dict(w="experience", pt="experiência", e="🏅", ex=["Do you have experience?", "I have some experience."]),
  dict(w="part-time", pt="meio período", e="🕒", ex=["I want a part-time job.", "This is a part-time job."]),
  dict(w="hire", pt="contratar", e="🧑‍💼", ex=["They hire me today.", "We hire new workers."]),
  dict(w="interview", pt="entrevista", e="🤝", ex=["I have an interview today.", "The interview is at ten."]),
 ],
 molds=[
  dict(title="Dizer por que veio", frame="Hello! I'm here for the {thing}.", slots=[dict(key="thing", opts=["job application", "interview", "job", "form"])], model="Hello! I'm here for the job application.", note="I'm here for... = Vim para... Use para dizer o motivo."),
  dict(title="Dizer seus dados", frame="My {item} is {value}.", slots=[dict(key="item", opts=["name", "phone number", "email"]), dict(key="value", opts=["Noor Ali", "five five five", "noor at mail dot com"])], model="My name is Noor Ali.", note="Cuidado ao combinar: nome com name, número com phone number."),
  dict(title="Escrever uma mensagem", frame="Hello. I want to apply for the {job} job. My email is {email}. I have {exp}.", slots=[dict(key="job", opts=["cashier", "store", "cleaning"]), dict(key="email", opts=["noor at mail dot com", "sara at mail dot com", "tom at mail dot com"]), dict(key="exp", opts=["some experience", "no experience", "one year of experience"])], model="Hello. I want to apply for the cashier job. My email is noor at mail dot com. I have some experience.", note="Apply for = candidatar-se a. Termine dizendo a experiência."),
 ],
 sounds=[
  dict(say="I'm here for the job application.", tag="acento: applicaTION", tip="Palavras com -tion têm força antes do final: apliCAtion. Diga ap-li-CA-tion."),
  dict(say="What's your email?", tag="ritmo: WHAT'S your EMail", tip="Acentue WHAT'S e E; your fica fraco, quase 'yer'."),
  dict(say="It's five five five.", tag="ritmo: FIVE FIVE FIVE", tip="Diga cada número com força igual, devagar, como em um telefone."),
 ],
 role=dict(turns=[
  dict(npc="Hello. Can I help you?", opts=[
   dict(en="Hello! I'm here for the job application.", pt="Olá! Estou aqui para a ficha de emprego.", reply="Great. Please take this form."),
   dict(en="Hi! I want to apply for the job.", pt="Oi! Quero me candidatar à vaga.", reply="Great. Please take this form."),
   dict(en="Hello! I'm here for the interview.", pt="Olá! Estou aqui para a entrevista.", reply="Great. Please sit down. First, take this form.")]),
  dict(npc="Please take this form.", opts=[
   dict(en="Thanks. What do I write first?", pt="Obrigado. O que escrevo primeiro?", reply="Your name and address."),
   dict(en="Thank you. Where do I start?", pt="Obrigado. Por onde começo?", reply="Your name and address."),
   dict(en="Thanks. Do I use a pen?", pt="Obrigado. Uso caneta?", reply="Yes, a pen. Start with your name and address.")]),
  dict(npc="And your phone number?", opts=[
   dict(en="It's five five five, one four two two.", pt="É cinco cinco cinco, um quatro dois dois.", reply="Thanks. What's your email?"),
   dict(en="It's five five five, nine zero one one.", pt="É cinco cinco cinco, nove zero um um.", reply="Thanks. What's your email?"),
   dict(en="Sure. It's five five five, two three four four.", pt="Claro. É cinco cinco cinco, dois três quatro quatro.", reply="Thanks. What's your email?")]),
  dict(npc="What's your email?", opts=[
   dict(en="It's noor at mail dot com.", pt="É noor arroba mail ponto com.", reply="Great. I have everything."),
   dict(en="It's sara at mail dot com.", pt="É sara arroba mail ponto com.", reply="Great. I have everything."),
   dict(en="Let me spell it: n-o-o-r at mail dot com.", pt="Vou soletrar: n-o-o-r arroba mail ponto com.", reply="Great. I have everything.")]),
 ], change=["O gerente não entendeu o e-mail: soletre devagar.", "Ele pergunta sobre experiência: responda que tem pouca.", "Você errou o telefone: peça outro formulário."]),
 writing=dict(task="Escreva uma mensagem curta para uma loja: diga que quer a vaga, dê seu e-mail e fale sobre sua experiência.", model="Hello. I want to apply for the cashier job. My email is noor at mail dot com. I have some experience.", kw=["apply", "job", "email", "experience"], checks=["Disse que quer a vaga.", "Deu o e-mail em inglês.", "Falou da experiência."]),
 scenes=dict(pool=["lobby", "office", "shop", "counter", "hall"], npc=dict(g="f", role="manager"), you=dict(g="m")),
 convo=dict(npc=dict(name="Malik"), story="Você quer uma vaga em uma loja e fala com a gerente, que entrega o formulário.", turns=[
  dict(npc="Hello. Can I help you?", pt="Olá. Posso ajudar?", opts=[
   dict(en="Great. Please take this form.", pt="Ótimo. Pegue este formulário.", ok=False, fb="Quem entrega o formulário é a gerente."),
   dict(en="Hello! I'm here for the job application.", pt="Olá! Estou aqui para a ficha de emprego.", ok=True, fb="Diz o motivo da visita."),
   dict(en="It's five five five, one four two two.", pt="É cinco cinco cinco, um quatro dois dois.", ok=False, fb="Ela ainda não pediu o telefone.")]),
  dict(npc="Great. Please take this form.", pt="Ótimo. Pegue este formulário.", opts=[
   dict(en="Your name and address.", pt="Seu nome e endereço.", ok=False, fb="Quem diz isso é a gerente."),
   dict(en="I'm here for the job application.", pt="Estou aqui para a ficha de emprego.", ok=False, fb="Você já disse isso."),
   dict(en="Thanks. What do I write first?", pt="Obrigado. O que escrevo primeiro?", ok=True, fb="Pergunta o primeiro passo.")]),
  dict(npc="Your name and address.", pt="Seu nome e endereço.", opts=[
   dict(en="Here is my name: Noor Ali.", pt="Aqui está meu nome: Noor Ali.", ok=True, fb="Responde com o seu nome."),
   dict(en="What's your email?", pt="Qual é seu e-mail?", ok=False, fb="Quem pergunta isso é a gerente."),
   dict(en="Please take this form.", pt="Pegue este formulário.", ok=False, fb="Você já tem o formulário.")]),
  dict(npc="And your phone number?", pt="E seu telefone?", opts=[
   dict(en="What do I write first?", pt="O que escrevo primeiro?", ok=False, fb="Você já começou a escrever."),
   dict(en="It's five five five, one four two two.", pt="É cinco cinco cinco, um quatro dois dois.", ok=True, fb="Diz os dígitos um a um."),
   dict(en="Here is my name.", pt="Aqui está meu nome.", ok=False, fb="Já falou o nome.")]),
  dict(npc="What's your email?", pt="Qual é seu e-mail?", opts=[
   dict(en="It's noor at mail dot com.", pt="É noor arroba mail ponto com.", ok=True, fb="@ = at e . = dot."),
   dict(en="It's five five five, one four two two.", pt="É cinco cinco cinco, um quatro dois dois.", ok=False, fb="Esse é o telefone, e não o e-mail."),
   dict(en="Great. Please take this form.", pt="Ótimo. Pegue este formulário.", ok=False, fb="Essa fala é da gerente.")]),
 ]),
)
