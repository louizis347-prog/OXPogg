X = dict(
 key=dict(big="How do I use the printer?", label="Usar a impressora", sub="Pergunte como usar a máquina, diga o que a tela mostra e peça as cópias que precisa."),
 mini=[
  dict(who="You", en="Excuse me, how do I {use|find|fix} the printer?", pt="Com licença, como eu {uso|acho|conserto} a impressora?"),
  dict(who="Grace", en="{Click Print|Press the button|Open the tray} first.", pt="{Clique em Imprimir|Aperte o botão|Abra a bandeja} primeiro."),
  dict(who="You", en="It says “No {paper|ink|power}.” Can you help?", pt="Diz “Sem {papel|tinta|energia}”. Pode ajudar?"),
  dict(who="Grace", en="Sure. Paper goes {here|there|in the tray}.", pt="Claro. O papel vai {aqui|ali|na bandeja}."),
 ],
 dlg=[
  dict(who="Grace", en="Excuse me, how do I use the {printer?|copier?}", pt="Com licença, como uso a {impressora?|copiadora?}"),
  dict(who="You", en="{Click|Press} Print on your computer.", pt="{Clique|Aperte} em Imprimir no computador."),
  dict(who="Grace", en="Then I go to the {printer?|machine?}", pt="Depois eu vou até a {impressora?|máquina?}"),
  dict(who="You", en="Yes. Press the {green|blue} button.", pt="Sim. Aperte o botão {verde.|azul.}"),
  dict(who="Grace", en="It says “No {paper.|ink.}”", pt="Diz “Sem {papel.|tinta.}”"),
  dict(who="You", en="Let me help. Paper goes {here.|there.}", pt="Deixe eu ajudar. O papel vai {aqui.|ali.}"),
  dict(who="Grace", en="Thanks. I need {five|two|ten} copies.", pt="Valeu. Preciso de {cinco|duas|dez} cópias."),
  dict(who="You", en="Press the number {five,|two,|ten,} then Start.", pt="Aperte o número {cinco|dois|dez} e depois Iniciar."),
  dict(who="Grace", en="It works! Where is my {document?|copy?}", pt="Funcionou! Onde está meu {documento?|cópia?}"),
 ],
 vocab=[
  dict(w="printer", pt="impressora", e="🖨️", ex=["The printer is in the hall.", "This printer is new."]),
  dict(w="copy", pt="cópia", e="📑", ex=["I need one copy.", "Make a copy, please."]),
  dict(w="document", pt="documento", e="📄", ex=["Where is my document?", "This document is short."]),
  dict(w="paperclip", pt="clipe de papel", e="📎", ex=["I need a paperclip.", "The paperclip is on the desk."]),
  dict(w="ink", pt="tinta", e="🖋️", ex=["The ink is low.", "We need black ink."]),
  dict(w="print", pt="imprimir", e="🗂️", ex=["Click Print.", "I print two pages."]),
 ],
 molds=[
  dict(title="Pedir instrução", frame="How do I {verb} the {thing}?", slots=[dict(key="verb", opts=["use", "find", "fix"]), dict(key="thing", opts=["printer", "stapler", "copier"])], model="How do I use the printer?", note="How do I + verbo base. Depois do 'do I', o verbo não leva -s."),
  dict(title="Pedir cópias", frame="I need {num} copies of the {doc}.", slots=[dict(key="num", opts=["two", "five", "ten"]), dict(key="doc", opts=["document", "form", "letter"])], model="I need two copies of the document.", note="Mais de uma: copies, não 'copys'."),
  dict(title="Escrever pedido de ajuda", frame="Hi {name}! Can you help me? The printer says “No {thing}.”", slots=[dict(key="name", opts=["Grace", "Quinn", "Sam"]), dict(key="thing", opts=["paper", "ink", "power"])], model="Hi Grace! Can you help me? The printer says “No paper.”", note="Can you help me? é um pedido educado. A mensagem da tela fica entre aspas."),
 ],
 sounds=[
  dict(say="How do I use the printer?", tag="ritmo: HOW … USE … PRIN-ter", tip="Dê força em HOW, USE e PRIN. 'do I' e 'the' ficam fracos e rápidos."),
  dict(say="Paper goes here.", tag="ritmo: PA-per GOES HERE", tip="PA-per tem acento na primeira sílaba. 'goes' e 'here' são fortes e curtos."),
  dict(say="I need five copies.", tag="acento: NEED FIVE COP-ies", tip="Bata nas três: NEED, FIVE, COP. O 'I' fica quase mudo."),
 ],
 role=dict(turns=[
  dict(npc="Hi! Can I help you?", opts=[
   dict(en="Yes, how do I use the printer?", pt="Sim, como uso a impressora?", reply="Click Print, then press the green button."),
   dict(en="Yes, please. I can't print this.", pt="Sim, por favor. Não consigo imprimir isto.", reply="Click Print, then press the green button."),
   dict(en="Excuse me, where is the printer?", pt="Com licença, onde fica a impressora?", reply="It is here. Click Print, then press the green button.")]),
  dict(npc="Did it work?", opts=[
   dict(en="It says “No paper.”", pt="Diz “Sem papel”.", reply="Let me help. Paper goes in the tray."),
   dict(en="The screen says “No paper.”", pt="A tela diz “Sem papel”.", reply="Let me help. Paper goes in the tray."),
   dict(en="No. There is no paper.", pt="Não. Não tem papel.", reply="Let me help. Paper goes in the tray.")]),
  dict(npc="Now what do you need?", opts=[
   dict(en="I need five copies.", pt="Preciso de cinco cópias.", reply="Press the number five, then Start."),
   dict(en="Five copies, please.", pt="Cinco cópias, por favor.", reply="Press the number five, then Start."),
   dict(en="I need two copies.", pt="Preciso de duas cópias.", reply="Press the number two, then Start.")]),
  dict(npc="How is it now?", opts=[
   dict(en="It works! Thanks!", pt="Funcionou! Valeu!", reply="You're welcome!"),
   dict(en="It works! Where is my document?", pt="Funcionou! Onde está meu documento?", reply="It's in the output tray."),
   dict(en="Great. Thanks for your help.", pt="Ótimo. Obrigado pela ajuda.", reply="No problem!")]),
 ], change=["A tela agora diz “Low ink”: peça ajuda a Grace e pergunte onde fica a tinta.", "Você precisa de dez cópias em vez de cinco: diga o número novo.", "O documento não saiu: pergunte onde ele está."]),
 writing=dict(task="Você é novo no escritório. Escreva 2 ou 3 frases para um colega: peça ajuda com a impressora e diga quantas cópias precisa.", model="Hi Grace! Can you help me? I need five copies of this document.", kw=["help", "printer", "copies", "document"], checks=["Pediu ajuda com educação.", "Disse quantas cópias precisa.", "Usou a palavra document ou printer."]),
 scenes=dict(pool=["office", "lobby", "hall", "counter"], npc=dict(g="f", role="coworker"), you=dict(g="m")),
 convo=dict(npc=dict(name="Grace"), story="Você é novo no escritório. A Grace, colega, ajuda você a imprimir.", turns=[
  dict(npc="Hi! You look lost. Can I help?", pt="Oi! Você parece perdido. Posso ajudar?", opts=[
   dict(en="Yes, how do I use the printer?", pt="Sim, como uso a impressora?", ok=True, fb="Pergunta direta com How do I…?"),
   dict(en="It works!", pt="Funcionou!", ok=False, fb="Ainda não tentou imprimir."),
   dict(en="Let me help.", pt="Deixe eu ajudar.", ok=False, fb="Quem ajuda é a Grace, não você.")]),
  dict(npc="Click Print on your computer. Then press the green button.", pt="Clique em Imprimir no computador. Depois aperte o botão verde.", opts=[
   dict(en="Paper goes here.", pt="O papel vai aqui.", ok=False, fb="Essa frase é de quem explica."),
   dict(en="Okay, thanks. I click Print first.", pt="Ok, obrigado. Primeiro clico em Imprimir.", ok=True, fb="Repetir o passo confirma que você entendeu."),
   dict(en="Yes, I'd love to!", pt="Quero sim!", ok=False, fb="Não é um convite.")]),
  dict(npc="What does the screen say?", pt="O que diz a tela?", opts=[
   dict(en="Press the number five.", pt="Aperte o número cinco.", ok=False, fb="Ela pergunta a mensagem da tela."),
   dict(en="Where is my document?", pt="Onde está meu documento?", ok=False, fb="Ainda não imprimiu nada."),
   dict(en="It says “No paper.”", pt="Diz “Sem papel”.", ok=True, fb="It says + mensagem da tela.")]),
  dict(npc="Paper goes in the tray. Do you need copies?", pt="O papel vai na bandeja. Você precisa de cópias?", opts=[
   dict(en="Yes, I need five copies.", pt="Sim, preciso de cinco cópias.", ok=True, fb="I need + número + copies."),
   dict(en="No, it says “No paper.”", pt="Não, diz “Sem papel”.", ok=False, fb="Isso já foi resolvido."),
   dict(en="Click Print.", pt="Clique em Imprimir.", ok=False, fb="Não responde à pergunta.")]),
  dict(npc="Press the number five, then Start.", pt="Aperte o número cinco e depois Iniciar.", opts=[
   dict(en="Excuse me, how do I use it?", pt="Com licença, como uso?", ok=False, fb="Ela acabou de explicar."),
   dict(en="Yes, here it is.", pt="Sim, aqui está.", ok=False, fb="Não combina com a explicação."),
   dict(en="It works! Thanks for your help!", pt="Funcionou! Obrigado pela ajuda!", ok=True, fb="Agradeça depois que deu certo.")]),
 ]),
)
