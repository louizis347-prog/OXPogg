X = dict(
 key=dict(big="Can you help me?", label="Pedir ajuda no trabalho", sub="Peça ajuda a um colega, diga o que você não consegue fazer e peça para ver os passos de novo."),
 mini=[
  dict(who="You", en="Excuse me, can you {help|show|call} me?", pt="Com licença, pode {me ajudar|me mostrar|me chamar}?"),
  dict(who="Ravi", en="Sure. What do you {need?|want?}", pt="Claro. O que você {precisa?|quer?}"),
  dict(who="You", en="I can't {open|find|save} this file.", pt="Não consigo {abrir|achar|salvar} este arquivo."),
  dict(who="Ravi", en="Let me see. {Click|Press|Open} here.", pt="Deixe-me ver. {Clique|Aperte|Abra} aqui."),
 ],
 dlg=[
  dict(who="Ravi", en="Excuse me, can you {help|show} me?", pt="Com licença, pode {me ajudar?|me mostrar?}"),
  dict(who="You", en="Sure. What do you {need?|want?}", pt="Claro. Do que você {precisa?|quer?}"),
  dict(who="Ravi", en="I can't open this {file.|folder.}", pt="Não consigo abrir este {arquivo.|pasta.}"),
  dict(who="You", en="Let me see. {Click|Press} here.", pt="Deixe-me ver. {Clique|Aperte} aqui."),
  dict(who="Ravi", en="It's {working|ready} now!", pt="Agora está {funcionando!|pronto!}"),
  dict(who="You", en="Great. Is it {clear?|okay?}", pt="Ótimo. Ficou {claro?|bom?}"),
  dict(who="Ravi", en="Yes. Can you {show|tell} me again?", pt="Sim. Pode {me mostrar|me dizer} de novo?"),
  dict(who="You", en="Of course. First, open the {folder.|file.}", pt="Claro. Primeiro, abra {a pasta.|o arquivo.}"),
  dict(who="Ravi", en="Then double-click the {file.|link.}", pt="Depois clique duas vezes {no arquivo.|no link.}"),
 ],
 vocab=[
  dict(w="file", pt="arquivo", e="📁", ex=["I can't open this file.", "Save the file, please."]),
  dict(w="mouse", pt="mouse", e="🖱️", ex=["The mouse is on the desk.", "Click with the mouse."]),
  dict(w="click", pt="clicar", e="🖱️", ex=["Click here.", "Click the link."]),
  dict(w="question", pt="pergunta", e="❓", ex=["I have a question.", "That is a good question."]),
  dict(w="link", pt="link", e="🔗", ex=["Click the link.", "The link is in the email."]),
  dict(w="update", pt="atualizar", e="🔄", ex=["Please update the file.", "I update my computer."]),
 ],
 molds=[
  dict(title="Pedir ajuda", frame="Can you {verb} me?", slots=[dict(key="verb", opts=["help", "show", "teach"])], model="Can you help me?", note="Can you + verbo base. Não coloque 'to' depois de can."),
  dict(title="Dizer o problema", frame="I can't {verb} this {thing}.", slots=[dict(key="verb", opts=["open", "find", "save"]), dict(key="thing", opts=["file", "folder", "link"])], model="I can't open this file.", note="I can't + verbo. A forma curta é can't, nunca 'no can'."),
  dict(title="Escrever pedido", frame="Hi {name}! Can you help me? I can't {verb} the {thing}.", slots=[dict(key="name", opts=["Mia", "Sam", "Ravi"]), dict(key="verb", opts=["open", "find", "save"]), dict(key="thing", opts=["file", "folder", "link"])], model="Hi Mia! Can you help me? I can't open the file.", note="Primeiro peça ajuda, depois diga o problema."),
 ],
 sounds=[
  dict(say="Can you help me?", tag="redução: can fraco", tip="Em pergunta, 'can' é fraco: 'kn you HELP me'. A força vai em HELP."),
  dict(say="I can't open this file.", tag="redução: can't forte", tip="Can't é forte, com vogal aberta: 'kænt'. Bata forte em CAN'T e OPEN."),
  dict(say="Can you show me again?", tag="redução: can you → kn-ya", tip="Una 'can you' e deixe fraco: 'kn-ya'. Acentue SHOW e A-GAIN."),
 ],
 role=dict(turns=[
  dict(npc="Hi! You look worried.", opts=[
   dict(en="Excuse me, can you help me?", pt="Com licença, pode me ajudar?", reply="Sure. What do you need?"),
   dict(en="Yes. Can you help me, please?", pt="Sim. Pode me ajudar, por favor?", reply="Sure. What do you need?"),
   dict(en="Hi. I have a question.", pt="Oi. Tenho uma pergunta.", reply="Sure. What is it?")]),
  dict(npc="What's the problem?", opts=[
   dict(en="I can't open this file.", pt="Não consigo abrir este arquivo.", reply="Let me see. Click here."),
   dict(en="I can't find the folder.", pt="Não consigo achar a pasta.", reply="Let me see. It's here."),
   dict(en="I can't open this link.", pt="Não consigo abrir este link.", reply="Let me see. Click here.")]),
  dict(npc="Is it working now?", opts=[
   dict(en="Yes, it's working now!", pt="Sim, agora está funcionando!", reply="Great. Is it clear?"),
   dict(en="Yes! Thank you!", pt="Sim! Obrigado!", reply="You're welcome. Is it clear?"),
   dict(en="Yes, it opens now.", pt="Sim, agora abre.", reply="Good. Is it clear?")]),
  dict(npc="Is it clear?", opts=[
   dict(en="Yes. Can you show me again?", pt="Sim. Pode me mostrar de novo?", reply="Of course. First, open the folder."),
   dict(en="Not yet. Can you show me again?", pt="Ainda não. Pode me mostrar de novo?", reply="Of course. First, open the folder."),
   dict(en="Yes, thanks. I can do it now.", pt="Sim, valeu. Agora eu consigo.", reply="Great job!")]),
 ], change=["O arquivo ainda não abre: diga que ainda não consegue e peça outra ajuda.", "Seu colega está ocupado: pergunte quando ele pode ajudar.", "Você quer anotar os passos: peça para ele falar mais devagar."]),
 writing=dict(task="Escreva 2 ou 3 frases para um colega: peça ajuda e diga qual arquivo ou pasta você não consegue abrir.", model="Hi Mia! Can you help me? I can't open the file. Thanks!", kw=["help", "can't", "file", "open"], checks=["Pediu ajuda com educação.", "Disse o que não consegue fazer.", "Agradeceu."]),
 scenes=dict(pool=["office", "lobby", "meetingroom", "hall"], npc=dict(g="m", role="coworker"), you=dict(g="f")),
 convo=dict(npc=dict(name="Ravi"), story="Você é novo no escritório e seu computador tem um problema. O Ravi, colega, ajuda.", turns=[
  dict(npc="Hi! You look worried.", pt="Oi! Você parece preocupada.", opts=[
   dict(en="Let me see. Click here.", pt="Deixe-me ver. Clique aqui.", ok=False, fb="Quem diz isso é quem ajuda."),
   dict(en="Excuse me, can you help me?", pt="Com licença, pode me ajudar?", ok=True, fb="Peça ajuda com educação."),
   dict(en="Yes, it's clear.", pt="Sim, está claro.", ok=False, fb="Ninguém perguntou isso.")]),
  dict(npc="Sure. What do you need?", pt="Claro. Do que você precisa?", opts=[
   dict(en="I can't open this file.", pt="Não consigo abrir este arquivo.", ok=True, fb="Diga o problema com I can't."),
   dict(en="Yes, I need.", pt="Sim, eu preciso.", ok=False, fb="Ele pediu o problema, não sim ou não."),
   dict(en="It's working now!", pt="Agora está funcionando!", ok=False, fb="Ainda não resolveu.")]),
  dict(npc="Let me see. Click here.", pt="Deixe-me ver. Clique aqui.", opts=[
   dict(en="What do you need?", pt="Do que você precisa?", ok=False, fb="Você é quem precisa de ajuda."),
   dict(en="I can't open this file.", pt="Não consigo abrir este arquivo.", ok=False, fb="Você já disse isso."),
   dict(en="Thanks! It's working now!", pt="Valeu! Agora está funcionando!", ok=True, fb="Agradeça e diga o resultado.")]),
  dict(npc="Great. Is it clear?", pt="Ótimo. Ficou claro?", opts=[
   dict(en="Yes. Can you show me again?", pt="Sim. Pode me mostrar de novo?", ok=True, fb="Peça para ver de novo, com educação."),
   dict(en="Sure. What do you need?", pt="Claro. Do que você precisa?", ok=False, fb="Essa é a fala de quem ajuda."),
   dict(en="Click here.", pt="Clique aqui.", ok=False, fb="Não responde à pergunta.")]),
  dict(npc="Of course. First, open the folder. Then double-click the file.", pt="Claro. Primeiro, abra a pasta. Depois clique duas vezes no arquivo.", opts=[
   dict(en="Can you help me?", pt="Pode me ajudar?", ok=False, fb="Ele já está ajudando."),
   dict(en="I can't open this file.", pt="Não consigo abrir este arquivo.", ok=False, fb="Já foi resolvido."),
   dict(en="Okay, I understand. Thanks a lot!", pt="Ok, entendi. Muito obrigado!", ok=True, fb="Confirme que entendeu e agradeça.")]),
 ]),
)
