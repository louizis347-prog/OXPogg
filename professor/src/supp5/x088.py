"""Bloco extra da aula 88: na praia."""
X = dict(
 key=dict(big="I need sunscreen", label="Pedir o que falta", sub="Pergunte da água, diga o que você precisa e pergunte onde está cada coisa. Need não leva -ing."),
 mini=[
  dict(who="Serena", en="What a beautiful {beach|day|view}!", pt="Que {praia|dia|vista} linda!"),
  dict(who="You", en="Yes! Is the water {cold|warm|clear}?", pt="Sim! A água está {fria|morna|limpa}?"),
  dict(who="Serena", en="No, it's {warm|cool|clear}. Let's swim!", pt="Não, está {morna|fresca|limpa}. Vamos nadar!"),
  dict(who="You", en="Wait. I need {sunscreen|my towel|my hat}.", pt="Espera. Preciso {de protetor solar|da minha toalha|do meu chapéu}."),
 ],
 dlg=[
  dict(who="Serena", en="What a beautiful {beach!|day!}", pt="Que {praia|dia} linda!"),
  dict(who="You", en="Yes! Is the water {cold?|warm?}", pt="Sim! A água está {fria?|morna?}"),
  dict(who="Serena", en="No, it's warm. Let's {swim!|go!}", pt="Não, está morna. Vamos {nadar!|lá!}"),
  dict(who="You", en="Wait. I need {sunscreen.|a hat.}", pt="Espera. Preciso de {protetor solar.|um chapéu.}"),
  dict(who="Serena", en="Here, use {mine.|this one.}", pt="Toma, use {o meu.|este.}"),
  dict(who="You", en="Thanks. Where is the {towel?|umbrella?}", pt="Valeu. Onde está {a toalha?|o guarda-sol?}"),
  dict(who="Serena", en="It's under the {umbrella.|chair.}", pt="Está debaixo {do guarda-sol.|da cadeira.}"),
  dict(who="You", en="{Perfect.|Great.} Let's go!", pt="{Perfeito.|Ótimo.} Vamos!"),
  dict(who="Serena", en="Have fun at the {beach!|party!}", pt="Divirta-se na {praia!|festa!}"),
 ],
 vocab=[
  dict(w="beach", pt="praia", e="🏖️", ex=["The beach is beautiful.", "We go to the beach today."]),
  dict(w="sand", pt="areia", e="🏜️", ex=["The sand is hot.", "My feet are in the sand."]),
  dict(w="wave", pt="onda", e="🌊", ex=["The wave is small.", "I jump over the wave."]),
  dict(w="umbrella", pt="guarda-sol", e="⛱️", ex=["The umbrella is red.", "Sit under the umbrella."]),
  dict(w="sunscreen", pt="protetor solar", e="🧴", ex=["I need sunscreen.", "Use sunscreen every day."]),
  dict(w="lifeguard", pt="salva-vidas", e="🛟", ex=["The lifeguard watches the water.", "Ask the lifeguard."]),
 ],
 molds=[
  dict(title="Perguntar da água", frame="Is the {thing} {adj}?", slots=[dict(key="thing", opts=["water", "sand", "sea"]), dict(key="adj", opts=["cold", "warm", "clear"])], model="Is the water cold?", note="Pergunta com Is vem primeiro: Is the water cold?"),
  dict(title="Dizer o que você precisa", frame="I need {thing}.", slots=[dict(key="thing", opts=["sunscreen", "a towel", "a hat", "water"])], model="I need sunscreen.", note="I need + coisa. Nada de -ing: não é 'I am needing'."),
  dict(title="Escrever uma mensagem", frame="Hi! The beach is {adj} today. The water is {temp}. Bring {thing}!", slots=[dict(key="adj", opts=["sunny", "windy", "busy"]), dict(key="temp", opts=["warm", "cool", "clear"]), dict(key="thing", opts=["a towel", "sunscreen", "an umbrella"])], model="Hi! The beach is sunny today. The water is warm. Bring a towel!", note="Bring + coisa dá uma ordem amigável. Today = hoje."),
 ],
 sounds=[
  dict(say="Is the water cold?", tag="som: th em the", tip="Ponha a ponta da língua entre os dentes em 'the'. Não diga 'de'."),
  dict(say="Where is the towel?", tag="ligação: where is", tip="Una where e is: 'uérizz'. Acentue WHERE e TOW."),
  dict(say="It's under the umbrella.", tag="ritmo: UN-der the um-BREL-la", tip="Acentue UN e BREL; 'the' fica fraco."),
 ],
 role=dict(turns=[
  dict(npc="What a beautiful beach!", opts=[
   dict(en="Yes! Is the water cold?", pt="Sim! A água está fria?", reply="No, it's warm. Let's swim!"),
   dict(en="Yes! Is the water warm?", pt="Sim! A água está morna?", reply="Yes, it's warm. Let's swim!"),
   dict(en="Wow! Is the sea clear?", pt="Uau! O mar está limpo?", reply="Yes, it's clear and warm. Let's swim!")]),
  dict(npc="Let's swim!", opts=[
   dict(en="Wait. I need sunscreen.", pt="Espera. Preciso de protetor solar.", reply="Here, use mine."),
   dict(en="Wait. I need my hat.", pt="Espera. Preciso do meu chapéu.", reply="It's in the bag. Here you go."),
   dict(en="Wait. I need water first.", pt="Espera. Preciso de água primeiro.", reply="Here, take mine.")]),
  dict(npc="Here, use mine.", opts=[
   dict(en="Thanks. Where is the towel?", pt="Valeu. Onde está a toalha?", reply="It's under the umbrella."),
   dict(en="Thanks. Where is the umbrella?", pt="Valeu. Onde está o guarda-sol?", reply="It's over there, near the sand."),
   dict(en="Thank you! Where are our bags?", pt="Obrigado! Onde estão nossas bolsas?", reply="They're under the umbrella.")]),
  dict(npc="It's under the umbrella.", opts=[
   dict(en="Perfect. Let's go!", pt="Perfeito. Vamos!", reply="Have fun at the beach!"),
   dict(en="Great. Let's swim now!", pt="Ótimo. Vamos nadar agora!", reply="Have fun at the beach!"),
   dict(en="Thanks. See you in the water!", pt="Valeu. Te vejo na água!", reply="Have fun at the beach!")]),
 ], change=["As ondas estão grandes: pergunte se é seguro nadar.", "O guarda-sol voou com o vento: peça ajuda para achá-lo.", "A água está muito fria: diga que você prefere ficar na areia."]),
 writing=dict(task="Escreva 2 ou 3 frases para um amigo: diga como está a praia hoje, como está a água e peça que ele traga uma toalha.", model="Hi! The beach is sunny today. The water is warm. Bring a towel!", kw=["beach", "water", "warm", "bring"], checks=["Falou da praia ou do tempo.", "Falou da água.", "Pediu que ele trouxesse algo."]),
 scenes=dict(pool=["beach", "pier", "harbor", "park2"], npc=dict(g="f", role="friend"), you=dict(g="m")),
 convo=dict(npc=dict(name="Serena"), story="Você chega à praia com sua amiga Serena.", turns=[
  dict(npc="What a beautiful beach!", pt="Que praia linda!", opts=[
   dict(en="Have fun at the beach!", pt="Divirta-se na praia!", ok=False, fb="É despedida; vocês acabaram de chegar."),
   dict(en="Yes! Is the water cold?", pt="Sim! A água está fria?", ok=True, fb="Concorda e pergunta algo útil."),
   dict(en="Where is the towel?", pt="Onde está a toalha?", ok=False, fb="Ainda é cedo; primeiro a água.")]),
  dict(npc="No, it's warm. Let's swim!", pt="Não, está morna. Vamos nadar!", opts=[
   dict(en="Is the water cold?", pt="A água está fria?", ok=False, fb="Ela acabou de responder."),
   dict(en="Wait. I need sunscreen.", pt="Espera. Preciso de protetor solar.", ok=True, fb="Pede para esperar e diz o motivo."),
   dict(en="It's under the umbrella.", pt="Está debaixo do guarda-sol.", ok=False, fb="Ninguém perguntou onde está algo.")]),
  dict(npc="Here, use mine.", pt="Toma, use o meu.", opts=[
   dict(en="I need sunscreen.", pt="Preciso de protetor solar.", ok=False, fb="Ela já te deu o protetor."),
   dict(en="Perfect. Let's go!", pt="Perfeito. Vamos!", ok=False, fb="Você ainda precisa da toalha."),
   dict(en="Thanks. Where is the towel?", pt="Valeu. Onde está a toalha?", ok=True, fb="Agradece e pergunta.")]),
  dict(npc="It's under the umbrella.", pt="Está debaixo do guarda-sol.", opts=[
   dict(en="Perfect. Let's go!", pt="Perfeito. Vamos!", ok=True, fb="Tudo pronto."),
   dict(en="Here, use mine.", pt="Toma, use o meu.", ok=False, fb="É fala dela."),
   dict(en="Is the water cold?", pt="A água está fria?", ok=False, fb="Já foi respondido.")]),
  dict(npc="Have fun at the beach!", pt="Divirta-se na praia!", opts=[
   dict(en="Thanks! You too!", pt="Obrigado! Você também!", ok=True, fb="Resposta natural."),
   dict(en="I need sunscreen.", pt="Preciso de protetor solar.", ok=False, fb="Não responde ao desejo dela."),
   dict(en="Where is the towel?", pt="Onde está a toalha?", ok=False, fb="Fora de contexto.")]),
 ]),
)
