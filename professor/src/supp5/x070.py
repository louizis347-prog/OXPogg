X = dict(
 key=dict(big="Whose turn is it?", label="Dividir as tarefas de casa", sub="Pergunte de quem é a vez, ofereça com I'll... e peça ajuda com Can you...?"),
 mini=[
  dict(who="Grace", en="Whose turn is it to {wash the dishes|take out the trash|vacuum the rug}?", pt="De quem é a vez de {lavar a louça|levar o lixo|passar aspirador no tapete}?"),
  dict(who="You", en="It's mine. I'll do it {now|after lunch|tonight}.", pt="É a minha. Faço {agora|depois do almoço|hoje à noite}."),
  dict(who="Grace", en="Thanks. Can you {clean the kitchen|sweep the floor|mop the floor} too?", pt="Valeu. Pode {limpar a cozinha|varrer o chão|passar pano no chão} também?"),
  dict(who="You", en="Sure. We make a great team.", pt="Claro. Formamos um ótimo time."),
 ],
 dlg=[
  dict(who="Grace", en="Whose turn is it to {wash the dishes|clean the kitchen}?", pt="De quem é a vez de {lavar a louça|limpar a cozinha}?"),
  dict(who="You", en="It's mine. I'll do it {now|after lunch}.", pt="É a minha. Faço {agora|depois do almoço}."),
  dict(who="Grace", en="Thanks. I'll take out the {trash|garbage}.", pt="Valeu. Eu levo o {lixo|lixo}."),
  dict(who="You", en="Can you {clean|wipe} the kitchen too?", pt="Pode {limpar|passar um pano na} cozinha também?"),
  dict(who="Grace", en="Sure. Can you {vacuum|sweep} the living room?", pt="Claro. Pode {passar aspirador|varrer} na sala?"),
  dict(who="You", en="Yes, {after lunch|tonight|in ten minutes}.", pt="Sim, {depois do almoço|hoje à noite|em dez minutos}."),
  dict(who="Grace", en="We make a great team.", pt="Formamos um ótimo time."),
  dict(who="You", en="Yes! Then let's {watch a movie|play a game|get pizza}.", pt="Sim! Depois vamos {ver um filme|jogar um jogo|pedir pizza}."),
  dict(who="Grace", en="Thanks for helping out!", pt="Valeu pela ajuda!"),
 ],
 vocab=[
  dict(w="chore", pt="tarefa doméstica", e="📋", ex=["My chore is the dishes.", "Chores are boring."]),
  dict(w='dust', pt='poeira', e='🌫️', ex=['There is dust on the shelf.', 'I clean the dust.']),
  dict(w="bucket", pt="balde", e="🪣", ex=["Fill the bucket with water.", "The bucket is blue."]),
  dict(w='wipe', pt='limpar com pano', e='🧽', ex=['Wipe the table, please.', 'I wipe the sink.']),
  dict(w="rug", pt="tapete", e="🧶", ex=["The rug is in the living room.", "Vacuum the rug, please."]),
  dict(w='broom', pt='vassoura', e='🧹', ex=['I sweep with a broom.', 'The broom is in the closet.']),
 ],
 molds=[
  dict(title="Perguntar de quem é a vez", frame="Whose turn is it to {chore}?", slots=[dict(key="chore", opts=["wash the dishes", "take out the trash", "clean the kitchen", "vacuum the rug"])], model="Whose turn is it to wash the dishes?", note="Whose turn = de quem é a vez. Depois de to, use o verbo simples."),
  dict(title="Pedir ajuda", frame="Can you {chore}, please?", slots=[dict(key="chore", opts=["clean the kitchen", "vacuum the living room", "sweep the floor", "mop the floor"])], model="Can you clean the kitchen, please?", note="Can you...? é um pedido educado. Use please para suavizar."),
  dict(title="Escrever o plano", frame="Ugh, chores! It's my turn. I'll {a} {when}. Can you {b}? We make a great team.", slots=[dict(key="a", opts=["wash the dishes", "take out the trash", "sweep the floor"]), dict(key="when", opts=["now", "after lunch", "tonight"]), dict(key="b", opts=["clean the kitchen", "vacuum the living room", "mop the floor"])], model="Ugh, chores! It's my turn. I'll wash the dishes now. Can you clean the kitchen? We make a great team.", note="Diga que é a sua vez, ofereça e peça ajuda."),
 ],
 sounds=[
  dict(say="Whose turn is it?", tag="som longo: whose", tip="Whose tem o 'u' longo (uuz). Estique o som e arredonde os lábios."),
  dict(say="Let's watch a movie.", tag="som longo: movie", tip="Movie tem 'mu' longo: MOO-vi. Não encurte para 'mo-vi'."),
  dict(say="Get the broom.", tag="som longo: broom", tip="Broom rima com room: bruuum. Segure o 'u' por mais tempo."),
 ],
 role=dict(turns=[
  dict(npc="Whose turn is it to wash the dishes?", opts=[
   dict(en="It's mine. I'll do it now.", pt="É a minha. Faço agora.", reply="Thanks. I'll take out the trash."),
   dict(en="It's mine. I'll do it after lunch.", pt="É a minha. Faço depois do almoço.", reply="Okay. I'll take out the trash now."),
   dict(en="I think it's mine. I'll do it.", pt="Acho que é a minha. Eu faço.", reply="Thanks. I'll take out the trash.")]),
  dict(npc="Thanks. I'll take out the trash.", opts=[
   dict(en="Can you clean the kitchen too?", pt="Pode limpar a cozinha também?", reply="Sure. Can you vacuum the living room?"),
   dict(en="Can you sweep the floor too?", pt="Pode varrer o chão também?", reply="Sure. Can you vacuum the living room?"),
   dict(en="Great. Can you mop the floor after that?", pt="Ótimo. Pode passar pano no chão depois?", reply="Sure. Can you vacuum the living room?")]),
  dict(npc="Can you vacuum the living room?", opts=[
   dict(en="Yes, after lunch.", pt="Sim, depois do almoço.", reply="Great. We make a great team."),
   dict(en="Sure, in ten minutes.", pt="Claro, em dez minutos.", reply="Great. We make a great team."),
   dict(en="Yes, I'll do it tonight.", pt="Sim, faço hoje à noite.", reply="Okay. We make a great team.")]),
  dict(npc="We make a great team.", opts=[
   dict(en="Yes! Then let's watch a movie.", pt="Sim! Depois vamos ver um filme.", reply="Good idea. Thanks for helping out!"),
   dict(en="Yes! Then let's get pizza.", pt="Sim! Depois vamos pedir pizza.", reply="Good idea. Thanks for helping out!"),
   dict(en="Yes! Then let's play a game.", pt="Sim! Depois vamos jogar um jogo.", reply="Good idea. Thanks for helping out!")]),
 ], change=["Grace diz que a vez é sua de levar o lixo: aceite e faça agora.", "Você está cansado: peça para trocar a tarefa por outra.", "Grace esqueceu a vassoura: diga onde ela está."]),
 writing=dict(task="Você divide o apartamento com um amigo. Escreva 2 ou 3 frases: pergunte de quem é a vez, ofereça uma tarefa e peça ajuda.", model="Whose turn is it to wash the dishes? It's mine. I'll do it now. Can you clean the kitchen too?", kw=["turn", "dishes", "clean", "kitchen"], checks=["Perguntou de quem é a vez.", "Ofereceu fazer uma tarefa.", "Pediu ajuda com Can you."]),
 scenes=dict(pool=["kitchen", "living", "home1", "bedroom"], npc=dict(g="f", role="roommate"), you=dict(g="m")),
 convo=dict(npc=dict(name="Grace"), story="Você divide um apartamento com a Grace e vocês dividem as tarefas.", turns=[
  dict(npc="Whose turn is it to wash the dishes?", pt="De quem é a vez de lavar a louça?", opts=[
   dict(en="It's mine. I'll do it now.", pt="É a minha. Faço agora.", ok=True, fb="Diz que é a sua vez e se oferece."),
   dict(en="Thanks for helping out!", pt="Valeu pela ajuda!", ok=False, fb="Ainda é cedo para agradecer."),
   dict(en="We make a great team.", pt="Formamos um ótimo time.", ok=False, fb="Não responde à pergunta.")]),
  dict(npc="Thanks. I'll take out the trash.", pt="Valeu. Eu levo o lixo.", opts=[
   dict(en="Can you clean the kitchen too?", pt="Pode limpar a cozinha também?", ok=True, fb="Pede ajuda com educação."),
   dict(en="It's mine.", pt="É a minha.", ok=False, fb="Você já disse isso."),
   dict(en="Yes, after lunch.", pt="Sim, depois do almoço.", ok=False, fb="Ela ainda não pediu nada.")]),
  dict(npc="Sure. Can you vacuum the living room?", pt="Claro. Pode passar aspirador na sala?", opts=[
   dict(en="Whose turn is it?", pt="De quem é a vez?", ok=False, fb="Ela fez um pedido, não perguntou a vez."),
   dict(en="Yes, after lunch.", pt="Sim, depois do almoço.", ok=True, fb="Aceita e diz quando."),
   dict(en="I'll take out the trash.", pt="Eu levo o lixo.", ok=False, fb="Essa é a fala dela.")]),
  dict(npc="We make a great team.", pt="Formamos um ótimo time.", opts=[
   dict(en="Can you vacuum the living room?", pt="Pode passar aspirador na sala?", ok=False, fb="Essa pergunta é dela."),
   dict(en="Yes! Then let's watch a movie.", pt="Sim! Depois vamos ver um filme.", ok=True, fb="Concorda e sugere algo divertido."),
   dict(en="It's mine. I'll do it now.", pt="É a minha. Faço agora.", ok=False, fb="A louça já foi resolvida.")]),
  dict(npc="Thanks for helping out!", pt="Valeu pela ajuda!", opts=[
   dict(en="Anytime! See you later.", pt="Quando quiser! Até logo.", ok=True, fb="Responde ao agradecimento."),
   dict(en="Whose turn is it?", pt="De quem é a vez?", ok=False, fb="As tarefas já acabaram."),
   dict(en="I'll take out the trash.", pt="Eu levo o lixo.", ok=False, fb="Essa fala é dela, e a tarefa já foi feita.")]),
 ]),
)
