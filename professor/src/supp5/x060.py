X = dict(
 key=dict(big="Look both ways!", label="Atravessar a rua com segurança", sub="Espere o sinal verde, olhe para os dois lados e tenha cuidado com carros e bicicletas."),
 mini=[
  dict(who="Carlos", en="Wait! The {light|signal|traffic light} is red.", pt="Espere! O {sinal|sinal|semáforo} está vermelho."),
  dict(who="You", en="Thanks. When can I {cross?|go?|walk?}", pt="Valeu. Quando posso {atravessar?|ir?|andar?}"),
  dict(who="Carlos", en="When the {light is green.|sign says walk.|cars stop.}", pt="Quando {o sinal estiver verde.|a placa disser walk.|os carros pararem.}"),
  dict(who="You", en="Now it's {green|safe}. Let's go.", pt="Agora está {verde|seguro}. Vamos."),
 ],
 dlg=[
  dict(who="Carlos", en="Wait! The {light|signal} is red.", pt="Espere! O {sinal|sinal} está vermelho."),
  dict(who="You", en="Thanks. When can I {cross?|go?}", pt="Valeu. Quando posso {atravessar?|ir?}"),
  dict(who="Carlos", en="When the light is {green.|green, not red.}", pt="Quando o sinal estiver {verde.|verde, não vermelho.}"),
  dict(who="You", en="Now it's {green.|green now.} Let's go.", pt="Agora está {verde.|verde agora.} Vamos."),
  dict(who="Carlos", en="Look both {ways!|sides!}", pt="Olhe para os dois {lados!|lados!}"),
  dict(who="You", en="Good point. {Cars|Buses} are coming.", pt="Boa. Estão vindo {carros.|ônibus.}"),
  dict(who="Carlos", en="Be careful with {bikes|cars} too.", pt="Cuidado com {as bicicletas|os carros} também."),
  dict(who="You", en="Thanks, I {will.|will, thanks.}", pt="Valeu, {vou ter cuidado.|vou ter cuidado, valeu.}"),
  dict(who="Carlos", en="Have a safe {walk!|day!}", pt="Boa {caminhada!|dia!}"),
 ],
 vocab=[
  dict(w="crosswalk", pt="faixa de pedestres", e="🚸", ex=["Cross at the crosswalk.", "The crosswalk is on the corner."]),
  dict(w="careful", pt="cuidadoso", e="⚠️", ex=["Be careful!", "She is careful with bikes."]),
  dict(w="traffic", pt="trânsito", e="🚗", ex=["The traffic is heavy.", "Watch the traffic."]),
  dict(w="sidewalk", pt="calçada", e="🚶", ex=["Walk on the sidewalk.", "The sidewalk is wide."]),
  dict(w="button", pt="botão", e="🔘", ex=["Push the button.", "The button is on the pole."]),
  dict(w='cross', pt='atravessar', e='🚶', ex=['I cross the street here.', 'Cross now, it is green.']),
 ],
 molds=[
  dict(title="Perguntar quando atravessar", frame="When can I {action}?", slots=[dict(key="action", opts=["cross", "go", "walk"])], model="When can I cross?", note="When can I...? = Quando posso...? Depois de can vem o verbo base."),
  dict(title="Avisar do sinal", frame="Wait! The light is {color}.", slots=[dict(key="color", opts=["red", "yellow", "not green"])], model="Wait! The light is red.", note="The light is... = O sinal está... Wait! = Espere!"),
  dict(title="Escrever o aviso", frame="Be careful with {thing}. Look both ways, and {action}.", slots=[dict(key="thing", opts=["bikes", "cars", "traffic"]), dict(key="action", opts=["wait for the green light", "use the crosswalk", "stay on the sidewalk"])], model="Be careful with bikes. Look both ways, and wait for the green light.", note="Be careful with... + coisa; depois um conselho curto."),
 ],
 sounds=[
  dict(say="The light is red.", tag="r e l: light, red", tip="L: a ponta da língua toca atrás dos dentes. R: a língua não encosta em nada, a boca fica redonda."),
  dict(say="Cars are coming.", tag="r: cars, are", tip="Não vibre o R como em 'carro'. Faça um som suave e prolongue o 'ar'."),
  dict(say="Be careful with bikes.", tag="r no meio: careful", tip="CARE-ful: força em CARE; o R fica redondo e o l final é leve."),
 ],
 role=dict(turns=[
  dict(npc="Wait! The light is red.", opts=[
   dict(en="Thanks. When can I cross?", pt="Valeu. Quando posso atravessar?", reply="When the light is green."),
   dict(en="Oh, thanks! When can I go?", pt="Ah, valeu! Quando posso ir?", reply="When the light is green."),
   dict(en="Thanks. How long is the wait?", pt="Valeu. Quanto tempo tenho que esperar?", reply="Just a minute. Wait for green.")]),
  dict(npc="When the light is green.", opts=[
   dict(en="Now it's green. Let's go.", pt="Agora está verde. Vamos.", reply="Look both ways!"),
   dict(en="It's green now. Ready?", pt="Está verde agora. Pronto?", reply="Look both ways!"),
   dict(en="Green! Let's cross.", pt="Verde! Vamos atravessar.", reply="Look both ways!")]),
  dict(npc="Look both ways!", opts=[
   dict(en="Good point. Cars are coming.", pt="Boa. Estão vindo carros.", reply="Be careful with bikes too."),
   dict(en="Good point. A car is coming.", pt="Boa. Está vindo um carro.", reply="Be careful with bikes too."),
   dict(en="Right. I see a bus.", pt="Certo. Estou vendo um ônibus.", reply="Be careful with bikes too.")]),
  dict(npc="Be careful with bikes too.", opts=[
   dict(en="Thanks, I will.", pt="Valeu, vou ter cuidado.", reply="Have a safe walk!"),
   dict(en="Thanks. I'll be careful.", pt="Valeu. Vou ter cuidado.", reply="Have a safe walk!"),
   dict(en="Yes, thanks. Safety first!", pt="Sim, valeu. Segurança em primeiro lugar!", reply="Have a safe walk!")]),
 ], change=["O sinal de pedestres está quebrado: peça ajuda ou diga para esperar os carros pararem.", "Chove forte e há muito trânsito: diga para esperar mais um pouco.", "Um amigo quer atravessar fora da faixa: explique que é melhor usar a faixa."]),
 writing=dict(task="Você explica a um amigo como atravessar a rua. Escreva 2 ou 3 frases: diga para esperar o verde, olhar os dois lados e ter cuidado.", model="Wait for the green light. Look both ways. Be careful with cars and bikes.", kw=["light", "green", "careful", "ways"], checks=["Disse para esperar o sinal verde.", "Disse para olhar os dois lados.", "Pediu cuidado com carros ou bicicletas."]),
 scenes=dict(pool=["street", "nyc", "park2", "busstop"], npc=dict(g="m", role="friend"), you=dict(g="f")),
 convo=dict(npc=dict(name="Carlos"), story="Você está numa esquina em Portland e o Carlos dá dicas para atravessar.", turns=[
  dict(npc="Wait! The light is red.", pt="Espere! O sinal está vermelho.", opts=[
   dict(en="Have a safe walk!", pt="Boa caminhada!", ok=False, fb="Isso se diz no fim."),
   dict(en="Thanks. When can I cross?", pt="Valeu. Quando posso atravessar?", ok=True, fb="Agradece e pergunta quando."),
   dict(en="Look both ways!", pt="Olhe para os dois lados!", ok=False, fb="Essa fala é dele, depois.")]),
  dict(npc="When the light is green.", pt="Quando o sinal estiver verde.", opts=[
   dict(en="Be careful with bikes too.", pt="Cuidado com as bicicletas também.", ok=False, fb="Esse aviso é dele."),
   dict(en="Now it's green. Let's go.", pt="Agora está verde. Vamos.", ok=True, fb="O sinal mudou e você vai."),
   dict(en="Wait! The light is red.", pt="Espere! O sinal está vermelho.", ok=False, fb="Já está verde.")]),
  dict(npc="Look both ways!", pt="Olhe para os dois lados!", opts=[
   dict(en="Good point. Cars are coming.", pt="Boa. Estão vindo carros.", ok=True, fb="Reconhece o aviso."),
   dict(en="When can I cross?", pt="Quando posso atravessar?", ok=False, fb="Você já atravessa."),
   dict(en="Thanks, I will.", pt="Valeu, vou ter cuidado.", ok=False, fb="Cabe depois do aviso das bicicletas.")]),
  dict(npc="Be careful with bikes too.", pt="Cuidado com as bicicletas também.", opts=[
   dict(en="Good point. Cars are coming.", pt="Boa. Estão vindo carros.", ok=False, fb="Isso você já disse."),
   dict(en="Wait! The light is red.", pt="Espere! O sinal está vermelho.", ok=False, fb="Esse aviso é dele e já passou."),
   dict(en="Thanks, I will.", pt="Valeu, vou ter cuidado.", ok=True, fb="I will = vou ter cuidado.")]),
  dict(npc="Have a safe walk!", pt="Boa caminhada!", opts=[
   dict(en="Thanks! You too!", pt="Valeu! Você também!", ok=True, fb="Fecha a conversa."),
   dict(en="When can I cross?", pt="Quando posso atravessar?", ok=False, fb="Você já atravessou."),
   dict(en="Look both ways!", pt="Olhe para os dois lados!", ok=False, fb="Essa fala é do Carlos.")]),
 ]),
)
