X = dict(
 key=dict(big="Can you help me write an email?", label="Escrever um e-mail de trabalho", sub="Peça ajuda, diga para quem é, escreva uma mensagem curta e termine com obrigado."),
 mini=[
  dict(who="You", en="Can you help me {write|read|send} an email?", pt="Pode me ajudar a {escrever|ler|enviar} um e-mail?"),
  dict(who="Victor", en="Sure. Start with “{Hello|Hi|Dear}” and her name.", pt="Claro. Comece com “{Olá|Oi|Prezada}” e o nome dela."),
  dict(who="You", en="Then I write my {message|subject|question}.", pt="Depois escrevo minha {mensagem|assunto|pergunta}."),
  dict(who="Victor", en="Good. End with “{Thank you|Thanks|Best regards}.”", pt="Boa. Termine com “{Obrigado|Valeu|Atenciosamente}”."),
 ],
 dlg=[
  dict(who="Victor", en="Can you help me write an {email?|message?}", pt="Pode me ajudar a escrever um {e-mail?|mensagem?}"),
  dict(who="You", en="Sure. Who is it for?", pt="Claro. Para quem é?"),
  dict(who="Victor", en="It's for my {manager.|boss.}", pt="É para minha {gerente.|chefe.}"),
  dict(who="You", en="OK. Start with “{Hello|Hi}” and her name.", pt="Ok. Comece com “{Olá|Oi}” e o nome dela."),
  dict(who="Victor", en="{Hello|Hi}, Marta. Then what?", pt="{Olá|Oi}, Marta. E depois?"),
  dict(who="You", en="Write your {message.|subject.} Keep it short.", pt="Escreva sua {mensagem.|assunto.} Seja breve."),
  dict(who="Victor", en="I need the {report|file} by {Friday.|Monday.}", pt="Preciso d{o relatório|o arquivo} até {sexta.|segunda.}"),
  dict(who="You", en="Good. End with “{Thank you.|Thanks.}”", pt="Boa. Termine com “{Obrigado.|Valeu.}”"),
  dict(who="Victor", en="Do I add an {attachment?|link?}", pt="Preciso anexar {um anexo?|um link?}"),
 ],
 vocab=[
  dict(w="greeting", pt="saudação", e="👋", ex=["Hello is a greeting.", "Start with a greeting."]),
  dict(w="subject", pt="assunto", e="🏷️", ex=["The subject is short.", "Write the subject first."]),
  dict(w="attachment", pt="anexo", e="📎", ex=["Open the attachment.", "The attachment is a report."]),
  dict(w="inbox", pt="caixa de entrada", e="📥", ex=["A new email is in my inbox.", "My inbox is full."]),
  dict(w="reply", pt="responder", e="↩️", ex=["Please reply today.", "I will reply soon."]),
  dict(w="draft", pt="rascunho", e="📝", ex=["This is my first draft.", "Read my draft, please."]),
 ],
 molds=[
  dict(title="Pedir ajuda", frame="Can you help me {verb} an email?", slots=[dict(key="verb", opts=["write", "read", "send"])], model="Can you help me write an email?", note="Help me + verbo base, sem 'to'."),
  dict(title="Pedir com prazo", frame="I need the {thing} by {day}.", slots=[dict(key="thing", opts=["report", "file", "form"]), dict(key="day", opts=["Monday", "Friday", "Tuesday"])], model="I need the report by Monday.", note="By = no máximo até. Diferente de 'until'."),
  dict(title="Escrever e-mail", frame="Hello {name}, I need the {thing} by {day}. Thank you.", slots=[dict(key="name", opts=["Marta", "Sam", "Ana"]), dict(key="thing", opts=["report", "form", "file"]), dict(key="day", opts=["Monday", "Friday", "noon"])], model="Hello Marta, I need the report by Monday. Thank you.", note="Cumprimento + pedido curto + obrigado."),
 ],
 sounds=[
  dict(say="Keep it short.", tag="ligação: keep·it", tip="Junte o p com 'it': 'kee-pit short'. Sem pausa entre as palavras."),
  dict(say="Can you help me write an email?", tag="ligação: write·an", tip="O t de 'write' vai para 'an': 'wri-tan email'."),
  dict(say="Send it now.", tag="ligação: send·it", tip="Soa 'sen-dit now'. O d gruda no 'it'."),
 ],
 role=dict(turns=[
  dict(npc="Hi! Do you need help?", opts=[
   dict(en="Yes. Can you help me write an email?", pt="Sim. Pode me ajudar a escrever um e-mail?", reply="Sure. Who is it for?"),
   dict(en="Yes, please. I need to send an email.", pt="Sim, por favor. Preciso enviar um e-mail.", reply="Sure. Who is it for?"),
   dict(en="Yes. How do I write an email in English?", pt="Sim. Como escrevo um e-mail em inglês?", reply="It's easy. Who is it for?")]),
  dict(npc="Who is it for?", opts=[
   dict(en="It's for my manager.", pt="É para minha gerente.", reply="OK. Start with “Hello” and her name."),
   dict(en="It's for my boss, Marta.", pt="É para minha chefe, a Marta.", reply="OK. Start with “Hello, Marta.”"),
   dict(en="It's for a client.", pt="É para um cliente.", reply="OK. Start with “Hello” and his name.")]),
  dict(npc="Now write your message. Keep it short.", opts=[
   dict(en="I need the report by Friday.", pt="Preciso do relatório até sexta.", reply="Good. End with “Thank you.”"),
   dict(en="Can you check the subject?", pt="Pode conferir o assunto?", reply="Sure. “Report for Friday” is good."),
   dict(en="Is this message OK?", pt="Esta mensagem está boa?", reply="Yes, it's short and clear.")]),
  dict(npc="Almost done.", opts=[
   dict(en="Do I add an attachment?", pt="Preciso anexar algo?", reply="Yes. Click the paperclip."),
   dict(en="Where is the Send button?", pt="Onde fica o botão Enviar?", reply="It's at the bottom left."),
   dict(en="Can I send it now?", pt="Posso enviar agora?", reply="Yes. Click Send.")]),
 ], change=["Marta é uma cliente nova: peça ajuda para um começo mais formal.", "Você esqueceu o anexo: diga isso e pergunte como adicionar.", "O e-mail precisa ser urgente: peça ajuda para colocar o prazo no assunto."]),
 writing=dict(task="Escreva um e-mail curto para sua gerente: cumprimente, peça o relatório até uma data e agradeça.", model="Hello Marta, I need the report by Friday. Please send it with the form. Thank you, Victor", kw=["hello", "report", "friday", "thank"], checks=["Começou com Hello e o nome.", "Pediu algo com um prazo.", "Terminou com thank you."]),
 scenes=dict(pool=["office", "lobby", "meetingroom", "hall"], npc=dict(g="m", role="coworker"), you=dict(g="f")),
 convo=dict(npc=dict(name="Victor"), story="Você precisa escrever um e-mail para sua gerente. O Victor, colega, ajuda.", turns=[
  dict(npc="Hi! Do you need help?", pt="Oi! Você precisa de ajuda?", opts=[
   dict(en="Yes. Can you help me write an email?", pt="Sim. Pode me ajudar a escrever um e-mail?", ok=True, fb="Peça ajuda com Can you help me…?"),
   dict(en="Sure. Who is it for?", pt="Claro. Para quem é?", ok=False, fb="Essa é a pergunta de quem ajuda."),
   dict(en="Thank you.", pt="Obrigada.", ok=False, fb="Ainda não recebeu ajuda.")]),
  dict(npc="Sure. Who is it for?", pt="Claro. Para quem é?", opts=[
   dict(en="Do I add an attachment?", pt="Preciso anexar algo?", ok=False, fb="Cedo demais; ele perguntou para quem é."),
   dict(en="Hello, Marta.", pt="Olá, Marta.", ok=False, fb="Ele quer saber a pessoa, não o início do e-mail."),
   dict(en="It's for my manager.", pt="É para minha gerente.", ok=True, fb="It's for + pessoa.")]),
  dict(npc="OK. Start with “Hello” and her name.", pt="Ok. Comece com “Olá” e o nome dela.", opts=[
   dict(en="Hello, Marta. Then what?", pt="Olá, Marta. E depois?", ok=True, fb="Mostra o passo e pergunta o próximo."),
   dict(en="It's for my manager.", pt="É para minha gerente.", ok=False, fb="Você já disse isso."),
   dict(en="End with “Thank you.”", pt="Termine com “Obrigada”.", ok=False, fb="É conselho de quem ajuda.")]),
  dict(npc="Write your message. Keep it short.", pt="Escreva sua mensagem. Seja breve.", opts=[
   dict(en="Can you help me write an email?", pt="Pode me ajudar a escrever um e-mail?", ok=False, fb="Você já pediu isso."),
   dict(en="Hello, Marta.", pt="Olá, Marta.", ok=False, fb="Esse passo já foi feito."),
   dict(en="I need the report by Friday.", pt="Preciso do relatório até sexta.", ok=True, fb="Curta, clara e com prazo.")]),
  dict(npc="Good. End with “Thank you.”", pt="Boa. Termine com “Obrigada”.", opts=[
   dict(en="Okay. Do I add an attachment?", pt="Ok. Preciso anexar algo?", ok=True, fb="Pergunta natural para o próximo passo."),
   dict(en="Start with “Hello.”", pt="Comece com “Olá”.", ok=False, fb="Esse passo já passou."),
   dict(en="Sure. Who is it for?", pt="Claro. Para quem é?", ok=False, fb="Quem pergunta isso é o Victor.")]),
 ]),
)
