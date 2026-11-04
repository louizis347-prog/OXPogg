X = dict(
 key=dict(big="The Wi-Fi is down", label="A internet parou", sub="Frase simples para avisar que a internet não funciona; depois você pergunta e tenta o reinício do roteador."),
 mini=[
  dict(who="Cole", en="Hi! The {Wi-Fi|internet|network} doesn't work.", pt="Oi! {O Wi-Fi|A internet|A rede} não funciona."),
  dict(who="You", en="Let me check. Is the light {green|red|blue}?", pt="Deixe-me ver. A luz está {verde|vermelha|azul}?"),
  dict(who="Cole", en="No, it's {red|white|blue}.", pt="Não, está {vermelha|branca|azul}."),
  dict(who="You", en="Turn it {off and on again|off and wait|off for a minute}.", pt="Desligue e {ligue de novo|espere|deixe um minuto desligado}."),
 ],
 dlg=[
  dict(who="Cole", en="Hi! What's the {Wi-Fi|internet} password?", pt="Oi! Qual é a senha {do Wi-Fi|da internet}?"),
  dict(who="You", en="It's on the {router|box}.", pt="Está no {roteador|aparelho}."),
  dict(who="Cole", en="It {doesn't work.|isn't working.}", pt="{Não está funcionando.|Não está funcionando agora.}"),
  dict(who="You", en="Let me check. Is the light {green?|blue?}", pt="Deixe-me ver. A luz está {verde?|azul?}"),
  dict(who="Cole", en="No, it's {red.|white.}", pt="Não, está {vermelha.|branca.}"),
  dict(who="You", en="Turn it {off and on again.|off, then on.}", pt="Desligue e {ligue de novo.|ligue depois.}"),
  dict(who="Cole", en="OK. Now it {works!|is fast!}", pt="Ok. Agora {funciona!|está rápido!}"),
  dict(who="You", en="Great. Enjoy the {internet!|Wi-Fi!}", pt="Ótimo. Aproveite {a internet!|o Wi-Fi!}"),
  dict(who="Cole", en="Done! Thanks for the {help.|tip.}", pt="Pronto! Valeu pela {ajuda.|dica.}"),
 ],
 vocab=[
  dict(w='website', pt='site', e='🌐', ex=['This website is slow.', 'I open the website.']),
  dict(w="password", pt="senha", e="🔐", ex=["What's the password?", "The password is on the card."]),
  dict(w="internet", pt="internet", e="🌐", ex=["The internet is slow today.", "I need the internet for work."]),
  dict(w="network", pt="rede", e="📶", ex=["Choose the home network.", "The network name is Casa_Lia."]),
  dict(w="plug", pt="tomada / plugue", e="🔌", ex=["Put the plug in the wall.", "The router plug is loose."]),
  dict(w="laptop", pt="notebook", e="💻", ex=["My laptop is on the table.", "The laptop can't find the network."]),
 ],
 molds=[
  dict(title="Avisar o problema", frame="The {thing} is very {state}.", slots=[dict(key="thing", opts=["Wi-Fi", "internet", "network"]), dict(key="state", opts=["slow", "fast", "bad"])], model="The Wi-Fi is very slow.", note="Depois de is, use o adjetivo: slow, fast, bad. Não use slowly aqui."),
  dict(title="Perguntar pela luz", frame="Is the light {color}?", slots=[dict(key="color", opts=["green", "red", "blue", "white"])], model="Is the light green?", note="Pergunta de sim ou não: Is... ? Responda: Yes, it is. / No, it's red."),
  dict(title="Escrever pedindo ajuda", frame="Hi! The {thing} is {problem}. Can you {action}, please?", slots=[dict(key="thing", opts=["Wi-Fi", "internet", "network"]), dict(key="problem", opts=["down", "slow", "not working"]), dict(key="action", opts=["check it", "help me", "send me the password"])], model="Hi! The Wi-Fi is down. Can you check it, please?", note="Can you... , please? é um pedido educado. The Wi-Fi is down = o Wi-Fi caiu."),
 ],
 sounds=[
  dict(say="Turn it off and on again.", tag="ligação: turn it off", tip="Turn it off soa 'tur-ni-toff'. Una o final de cada palavra à vogal seguinte."),
  dict(say="It's on the router.", tag="ligação: it's on", tip="It's on soa 'itson'. Acentue ROU-ter, com o r inglês, sem vibrar."),
  dict(say="Let me check.", tag="redução: let me", tip="Let me soa 'lemi'. Acentue CHECK, a sílaba forte da frase."),
 ],
 role=dict(turns=[
  dict(npc="Hi! What's the Wi-Fi password?", opts=[
   dict(en="It's on the router.", pt="Está no roteador.", reply="Oh, I see it. Thanks!"),
   dict(en="It's on the card.", pt="Está no cartão.", reply="Oh, I see the card. Thanks!"),
   dict(en="It's on the wall.", pt="Está na parede.", reply="Oh, I see it on the wall. Thanks!")]),
  dict(npc="It doesn't work.", opts=[
   dict(en="Let me check. Is the light green?", pt="Deixe-me ver. A luz está verde?", reply="No, it's red."),
   dict(en="Let me look. What color is the light?", pt="Deixe-me olhar. Que cor é a luz?", reply="It's red."),
   dict(en="Sorry! Let me check the router.", pt="Desculpe! Deixe-me ver o roteador.", reply="Thanks. The light is red."),]),
  dict(npc="No, it's red.", opts=[
   dict(en="Turn it off and on again.", pt="Desligue e ligue de novo.", reply="OK. I'm turning it off now."),
   dict(en="Try resetting it.", pt="Tente reiniciá-lo.", reply="OK. I'm resetting it now."),
   dict(en="Please turn it off for a minute.", pt="Por favor, desligue por um minuto.", reply="OK. I'm waiting one minute.")]),
  dict(npc="OK. Now it works!", opts=[
   dict(en="Great. Enjoy the internet!", pt="Ótimo. Aproveite a internet!", reply="Done! Thanks for the help."),
   dict(en="Good! You're welcome.", pt="Bom! De nada.", reply="Thanks! You're a genius."),
   dict(en="Nice! Is it fast now?", pt="Legal! Está rápido agora?", reply="Yes, it's fast. Thanks!")]),
 ], change=["O Wi-Fi funciona, mas está muito lento: diga que está lento e sugira usar o cabo.", "A luz continua vermelha depois do reinício: sugira ligar para a empresa de internet.", "O convidado não sabe o nome da rede: diga qual é e soletre."]),
 writing=dict(task="Um amigo está na sua casa e a internet não funciona. Escreva 2 ou 3 frases: diga o problema, pergunte sobre a luz e sugira desligar e ligar o roteador.", model="Hi! The Wi-Fi doesn't work. Is the light on the router green? Please turn it off and on again.", kw=["wi-fi", "router", "light", "turn"], checks=["Disse que o Wi-Fi não funciona.", "Perguntou sobre a luz.", "Sugeriu desligar e ligar."]),
 scenes=dict(pool=["living", "home1", "lobby", "office"], npc=dict(g="m", role="friend"), you=dict(g="f")),
 convo=dict(npc=dict(name="Cole"), story="Seu amigo Cole está na sua casa e precisa da internet.", turns=[
  dict(npc="Hi! What's the Wi-Fi password?", pt="Oi! Qual é a senha do Wi-Fi?", opts=[
   dict(en="Great. Enjoy the internet!", pt="Ótimo. Aproveite a internet!", ok=False, fb="Esta frase é para o final, quando já funciona."),
   dict(en="It's on the router.", pt="Está no roteador.", ok=True, fb="Responde onde está a senha."),
   dict(en="Turn it off and on again.", pt="Desligue e ligue de novo.", ok=False, fb="Ainda não há problema para consertar.")]),
  dict(npc="It doesn't work.", pt="Não está funcionando.", opts=[
   dict(en="Let me check. Is the light green?", pt="Deixe-me ver. A luz está verde?", ok=True, fb="Mostra que você vai ajudar e faz uma pergunta útil."),
   dict(en="It's on the router.", pt="Está no roteador.", ok=False, fb="Você já disse isso; agora há um problema."),
   dict(en="Thanks for the help.", pt="Valeu pela ajuda.", ok=False, fb="Ninguém ajudou ainda.")]),
  dict(npc="No, it's red.", pt="Não, está vermelha.", opts=[
   dict(en="Now it works!", pt="Agora funciona!", ok=False, fb="Ainda está vermelha; é cedo para dizer isso."),
   dict(en="What's the Wi-Fi password?", pt="Qual é a senha do Wi-Fi?", ok=False, fb="Esta pergunta é do Cole, e já foi respondida."),
   dict(en="Turn it off and on again.", pt="Desligue e ligue de novo.", ok=True, fb="Dica clássica para um problema simples.")]),
  dict(npc="OK. Now it works!", pt="Ok. Agora funciona!", opts=[
   dict(en="Let me check the light.", pt="Deixe-me ver a luz.", ok=False, fb="Já está funcionando; não precisa conferir."),
   dict(en="Great. Enjoy the internet!", pt="Ótimo. Aproveite a internet!", ok=True, fb="Fecha a conversa de forma simpática."),
   dict(en="It doesn't work.", pt="Não está funcionando.", ok=False, fb="O Cole disse o contrário.")]),
  dict(npc="Done! Thanks for the help.", pt="Pronto! Valeu pela ajuda.", opts=[
   dict(en="You're welcome!", pt="De nada!", ok=True, fb="Resposta natural a um agradecimento."),
   dict(en="Is the light green?", pt="A luz está verde?", ok=False, fb="O problema já foi resolvido."),
   dict(en="Hi! Nice to meet you.", pt="Oi! Prazer em conhecer.", ok=False, fb="Vocês já estão conversando há um tempo.")]),
 ]),
)
