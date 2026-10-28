"""Authorial Spanish A2 block 289–298, regular-pilot-v1."""
import ast, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TARGETS = [ROOT / "data/es-a2_06.json", ROOT / "data/es-a2_07.json"]

# Reuse only the episode constructor from the established pilot implementation;
# importing the module would also rewrite its old block, so extract definitions.
src = (ROOT / "tools/editorial/es_a2_189_198.py").read_text(encoding="utf-8")
prefix = src.split("data=json.loads", 1)[0]
ns = {"__file__": str(ROOT / "tools/editorial/es_a2_189_198.py")}
exec(prefix, ns)
make = ns["make"]

def mk(n, title, focus, work, year, desc, vocab, verbs, expressions, sound, a, b):
    return {"n": n, "t": title, "focus": focus, "work": work, "year": year,
            "desc": desc, "v": vocab, "vb": verbs, "ex": expressions,
            "sound": sound, "s1": [["Mara" if i % 2 == 0 else "Diego", x, y]
                                     for i, (x, y) in enumerate(a)],
            "s2": [["Mara" if i % 2 == 0 else "Diego", x, y]
                                     for i, (x, y) in enumerate(b)]}

PLANS = [
mk(289, "Una decisión en el mercado", "comparar opciones y justificar una compra", "La estrategia del caracol", "1993",
   "A comédia colombiana de Sergio Cabrera acompanha moradores que defendem sua casa com criatividade. A cena é autoral e mostra vizinhos comparando materiais numa feira.",
   [("puesto","banca","PÊS-to"),("precio","preço","PRÊ-sio"),("calidad","qualidade","ka-li-DÁD"),("trueque","troca","TRUÊ-ke"),("medida","medida","me-DÍ-da"),("vecindario","vizinhança","be-sin-DÁ-rio")],
   ["comparar","elegir","negociar","ahorrar"],
   ["Por un lado","Por um lado","A la larga","A longo prazo","¿Qué te parece?","O que você acha?","Sale mejor","Sai melhor"],
   ("c e z", ["precio","calidad","vecindario"]),
   [("En este puesto comparo dos precios.","Nesta banca comparo dois preços."),("La calidad parece más resistente.","A qualidade parece mais resistente."),("¿Aceptan un trueque por la madera?","Aceitam uma troca pela madeira?"),("Sí, si la medida coincide.","Sim, se a medida coincidir."),("Por un lado, cuesta más.","Por um lado, custa mais."),("Pero dura muchos años.","Mas dura muitos anos."),("Entonces elegimos esta opción.","Então escolhemos esta opção."),("A la larga, vamos a ahorrar.","A longo prazo, vamos economizar.")],
   [("¿Qué te parece comparar otra banca?","O que você acha de comparar outra banca?"),("**Por un lado**, tiene mejor precio.","Por um lado, tem preço melhor."),("**A la larga**, la calidad importa.","A longo prazo, a qualidade importa."),("**Sale mejor** si compramos juntos.","Sai melhor se comprarmos juntos."),("Negociamos sin presionar al vendedor.","Negociamos sem pressionar o vendedor."),("Elegimos la medida necesaria.","Escolhemos a medida necessária."),("El vecindario participa en la decisión.","A vizinhança participa da decisão."),("Así ahorramos y cuidamos el proyecto.","Assim economizamos e cuidamos do projeto.")]),
mk(290, "Uma mensagem de uma aldeia", "relatar uma notícia e confirmar uma informação", "Ixcanul", "2015",
   "O filme guatemalteco de Jayro Bustamante acompanha uma família maia diante de escolhas difíceis. A cena é autoral e trabalha uma mensagem comunitária que precisa ser confirmada.",
   [("aldea","aldeia","al-DÊ-a"),("mensaje","mensagem","men-SÁ-rre"),("fuente","fonte","FUÊN-te"),("noticia","notícia","no-TÍ-sia"),("confirmación","confirmação","kon-fir-ma-SIÓN"),("reunión","reunião","re-u-ni-ÓN")],
   ["recibir","confirmar","avisar","reunirse"],
   ["Según parece","Ao que parece","Que yo sepa","Que eu saiba","En cuanto a","Quanto a","Por lo visto","Pelo visto"],
   ("j e g", ["mensaje","reunión","fuente"]),
   [("Recibí un mensaje de la aldea.","Recebi uma mensagem da aldeia."),("La noticia habla de una reunión.","A notícia fala de uma reunião."),("¿Cuál es la fuente de la información?","Qual é a fonte da informação?"),("La confirma la coordinadora local.","A coordenadora local confirma."),("Según parece, será el viernes.","Ao que parece, será na sexta-feira."),("Por lo visto, todos recibieron el aviso.","Pelo visto, todos receberam o aviso."),("Voy a confirmar la hora.","Vou confirmar o horário."),("Después aviso a mi familia.","Depois aviso minha família.")],
   [("**Según parece**, la reunión empieza temprano.","Ao que parece, a reunião começa cedo."),("**Que yo sepa**, la fuente es segura.","Que eu saiba, a fonte é segura."),("**En cuanto a** la hora, falta confirmar.","Quanto ao horário, falta confirmar."),("**Por lo visto**, ya avisaron a todos.","Pelo visto, já avisaram todos."),("Recibimos una segunda noticia.","Recebemos uma segunda notícia."),("Nos reunimos para aclarar los detalles.","Nós nos reunimos para esclarecer os detalhes."),("La comunidad comparte la información.","A comunidade compartilha a informação."),("Así evitamos un malentendido.","Assim evitamos um mal-entendido.")]),
mk(291, "A trilha depois da chuva", "descrever uma mudança e dar orientações", "El abrazo de la serpiente", "2015",
   "O filme colombiano de Ciro Guerra atravessa rios, memórias e encontros entre culturas. A cena é autoral e acompanha uma trilha que muda depois da chuva.",
   [("sendero","trilha","sen-DÊ-ro"),("lluvia","chuva","JU-bia"),("puente","ponte","PUÊN-te"),("orilla","margem","o-RÍ-ya"),("señal","placa","se-NHÁL"),("corriente","correnteza","ko-RRIÊN-te")],
   ["cambiar","seguir","cruzar","avisar"],
   ["Ten cuidado","Tenha cuidado","A partir de aquí","A partir daqui","En caso de","Em caso de","Por suerte","Por sorte"],
   ("ll e y", ["lluvia","orilla","señal"]),
   [("La lluvia cambió el sendero.","A chuva mudou a trilha."),("Seguimos la señal junto al río.","Seguimos a placa junto ao rio."),("La corriente creció durante la noche.","A correnteza cresceu durante a noite."),("¿Cruzamos el puente pequeño?","Atravessamos a ponte pequena?"),("Ten cuidado con la orilla.","Tenha cuidado com a margem."),("A partir de aquí, vamos despacio.","A partir daqui, vamos devagar."),("Por suerte, encontramos otra ruta.","Por sorte, encontramos outra rota."),("Avisamos al grupo antes de continuar.","Avisamos o grupo antes de continuar.")],
   [("**Ten cuidado** cerca de la corriente.","Tenha cuidado perto da correnteza."),("**A partir de aquí**, el sendero se estrecha.","A partir daqui, a trilha fica estreita."),("**En caso de** lluvia, volvemos al puente.","Em caso de chuva, voltamos à ponte."),("**Por suerte**, hay una señal nueva.","Por sorte, há uma placa nova."),("Seguimos juntos hasta la orilla.","Seguimos juntos até a margem."),("Cruzamos cuando baje el agua.","Atravessamos quando a água baixar."),("Avisamos al guía de la situación.","Avisamos o guia sobre a situação."),("La ruta cambia, pero el plan continúa.","A rota muda, mas o plano continua.")]),
mk(292, "O desenho na parede", "descrever uma imagem e expressar uma hipótese", "La casa lobo", "2018",
   "A animação chilena de Joaquín Cociña e Cristóbal León transforma uma casa em espaço inquietante. A cena é autoral e convida a interpretar um desenho encontrado numa parede.",
   [("dibujo","desenho","di-BÚ-rro"),("pared","parede","pa-RÊD"),("figura","figura","fi-GÚ-ra"),("huella","marca","UÊ-ya"),("sombra","sombra","SÔM-bra"),("interpretación","interpretação","in-ter-pre-ta-SIÓN")],
   ["dibujar","parecer","imaginar","interpretar"],
   ["Tal vez","Talvez","A lo mejor","Pode ser que","No estoy seguro de que","Não tenho certeza de que","Tiene sentido","Faz sentido"],
   ("j e ll", ["dibujo","pared","huella"]),
   [("Encontramos un dibujo en la pared.","Encontramos um desenho na parede."),("La figura parece una casa.","A figura parece uma casa."),("También vemos una huella oscura.","Também vemos uma marca escura."),("Tal vez sea una sombra.","Talvez seja uma sombra."),("No estoy seguro de que sea reciente.","Não tenho certeza de que seja recente."),("Podemos imaginar otra interpretación.","Podemos imaginar outra interpretação."),("¿Tiene sentido para ti?","Faz sentido para você?"),("Sí, la imagen cuenta una historia.","Sim, a imagem conta uma história.")],
   [("**Tal vez**, la figura representa una familia.","Talvez a figura represente uma família."),("**A lo mejor**, la huella estaba antes.","Pode ser que a marca já estivesse ali."),("**No estoy seguro de que** sea una ventana.","Não tenho certeza de que seja uma janela."),("**Tiene sentido** si miramos la sombra.","Faz sentido se olharmos a sombra."),("Interpretamos cada detalle con calma.","Interpretamos cada detalhe com calma."),("El dibujo cambia según la luz.","O desenho muda conforme a luz."),("Comparamos nuestras hipótesis.","Comparamos nossas hipóteses."),("La pared guarda una pregunta.","A parede guarda uma pergunta.")]),
mk(293, "Um jogo no pátio", "explicar regras e propor uma mudança", "Los colores de la montaña", "2010",
   "O filme colombiano de Carlos César Arbeláez acompanha crianças e conflitos num povoado rural. A cena é autoral e organiza um jogo no pátio da escola.",
   [("patio","pátio","PÁ-tio"),("regla","regra","RÊ-gla"),("equipo","equipe","e-KÍ-po"),("turno","vez","TÚR-no"),("balón","bola","ba-LÓN"),("acuerdo","acordo","a-KUÊR-do")],
   ["explicar","formar","respetar","cambiar"],
   ["Primero que nada","Antes de mais nada","Por turnos","Por turnos","¿Te parece bien?","Tudo bem para você?","De acuerdo","De acordo"],
   ("r e rr", ["regla","equipo","acuerdo"]),
   [("Explico la regla antes de empezar.","Explico a regra antes de começar."),("Formamos dos equipos pequeños.","Formamos duas equipes pequenas."),("Cada jugador tiene un turno.","Cada jogador tem uma vez."),("Respetamos el acuerdo del patio.","Respeitamos o acordo do pátio."),("¿Te parece bien cambiar la regla?","Tudo bem mudar a regra?"),("Sí, si todos pueden participar.","Sim, se todos puderem participar."),("De acuerdo, empezamos de nuevo.","De acordo, começamos de novo."),("El juego funciona mejor así.","O jogo funciona melhor assim.")],
   [("**Primero que nada**, explicamos la regla.","Antes de mais nada, explicamos a regra."),("Jugamos **por turnos**.","Jogamos por turnos."),("**¿Te parece bien?** Podemos formar equipos mixtos.","Tudo bem para você? Podemos formar equipes mistas."),("**De acuerdo**, cambiamos el límite.","De acordo, mudamos o limite."),("Respetamos cada turno.","Respeitamos cada vez."),("El patio queda libre para todos.","O pátio fica livre para todos."),("Si hay un problema, hablamos.","Se houver um problema, conversamos."),("El acuerdo protege la diversión.","O acordo protege a diversão.")]),
mk(294, "Uma leitura na praça", "recomendar uma atividade e explicar uma preferência", "Neruda", "2016",
   "O filme de Pablo Larraín aproxima poesia, política e paisagens chilenas. A cena é autoral e mostra leitores escolhendo um livro para uma roda na praça.",
   [("poema","poema","POÊ-ma"),("banco","banco","BÂN-ko"),("verso","verso","BÊR-so"),("lectura","leitura","lek-TÚ-ra"),("preferencia","preferência","pre-fe-RÊN-sia"),("autor","autor","au-TÓR")],
   ["recomendar","elegir","leer","preferir"],
   ["En mi opinión","Na minha opinião","Para empezar","Para começar","Me apetece","Estou com vontade de","Sobre todo","Sobretudo"],
   ("r e rr", ["lectura","verso","autor"]),
   [("Recomiendo este poema para la lectura.","Recomendo este poema para a leitura."),("El verso habla de una plaza.","O verso fala de uma praça."),("¿Qué autor prefieres?","Que autor você prefere?"),("Elijo uno breve para empezar.","Escolho um curto para começar."),("En mi opinión, tiene imágenes fuertes.","Na minha opinião, tem imagens fortes."),("Me apetece leerlo junto al banco.","Estou com vontade de lê-lo junto ao banco."),("Sobre todo, me interesa el final.","Sobretudo, tenho interesse no final."),("Después comentamos nuestras preferencias.","Depois comentamos nossas preferências.")],
   [("**En mi opinión**, este verso es muy claro.","Na minha opinião, este verso é muito claro."),("**Para empezar**, elegimos una lectura corta.","Para começar, escolhemos uma leitura curta."),("**Me apetece** leer otro poema.","Estou com vontade de ler outro poema."),("**Sobre todo**, prefiero las imágenes del mar.","Sobretudo, prefiro as imagens do mar."),("Cada lector puede elegir un autor.","Cada leitor pode escolher um autor."),("Leemos despacio para escuchar el ritmo.","Lemos devagar para ouvir o ritmo."),("La plaza se convierte en una sala.","A praça se transforma em uma sala."),("Compartimos una recomendación final.","Compartilhamos uma recomendação final.")]),
mk(295, "A mala que não chegou", "explicar um problema e pedir uma solução", "El laberinto del fauno", "2006",
   "O filme de Guillermo del Toro mistura fantasia e história na Espanha do pós-guerra. A cena é autoral e acompanha uma pessoa no aeroporto depois de perder a bagagem.",
   [("maleta","mala","ma-LÊ-ta"),("equipaje","bagagem","e-ki-PÁ-rre"),("etiqueta","etiqueta","e-ti-KÊ-ta"),("reclamo","reclamação","re-KLÁ-mo"),("mostrador","balcão","mos-tra-DÓR"),("entrega","entrega","en-TRÊ-ga")],
   ["perder","buscar","reclamar","resolver"],
   ["Por desgracia","Infelizmente","Enseguida","Imediatamente","Lo antes posible","O quanto antes","De momento","Por enquanto"],
   ("r e rr", ["equipaje","reclamo","entrega"]),
   [("Mi equipaje no llegó con el vuelo.","Minha bagagem não chegou com o voo."),("La etiqueta está en mi bolsillo.","A etiqueta está no meu bolso."),("¿Dónde presento un reclamo?","Onde faço uma reclamação?"),("En el mostrador de atención.","No balcão de atendimento."),("Por desgracia, la maleta sigue perdida.","Infelizmente, a mala continua perdida."),("La buscamos enseguida.","Vamos procurá-la imediatamente."),("Necesito una entrega lo antes posible.","Preciso de uma entrega o quanto antes."),("De momento, guardo este comprobante.","Por enquanto, guardo este comprovante.")],
   [("**Por desgracia**, la maleta no aparece.","Infelizmente, a mala não aparece."),("La empresa responde **enseguida**.","A empresa responde imediatamente."),("Busquen el equipaje **lo antes posible**.","Procurem a bagagem o quanto antes."),("**De momento**, tengo el comprobante.","Por enquanto, tenho o comprovante."),("Presento el reclamo con calma.","Faço a reclamação com calma."),("El personal revisa la etiqueta.","A equipe revisa a etiqueta."),("Después me informan la entrega.","Depois me informam a entrega."),("La solución llega esa misma tarde.","A solução chega naquela tarde.")]),
mk(296, "A foto da família", "descrever uma fotografia e comparar épocas", "La jaula de oro", "2013",
   "O filme de Diego Quemada-Díez acompanha jovens migrantes e suas escolhas. A cena é autoral e mostra duas pessoas organizando fotos de família para uma exposição.",
   [("fotografía","fotografia","fo-to-gra-FÍ-a"),("álbum","álbum","ÁL-bum"),("generación","geração","rre-ne-ra-SIÓN"),("parecido","parecido","pa-re-SÍ-do"),("marco","moldura","MÁR-ko"),("recuerdo","lembrança","re-KUÊR-do")],
   ["ordenar","parecerse","comparar","guardar"],
   ["A diferencia de","Diferentemente de","En cambio","Por outro lado","Con el tiempo","Com o tempo","Qué recuerdo","Que lembrança"],
   ("g e j", ["fotografía","generación","parecido"]),
   [("Ordenamos las fotografías por año.","Ordenamos as fotografias por ano."),("Este álbum reúne tres generaciones.","Este álbum reúne três gerações."),("¿A quién se parece la niña?","Com quem a menina se parece?"),("Se parece a su abuela.","Ela se parece com a avó."),("A diferencia de hoy, no había móviles.","Diferentemente de hoje, não havia celulares."),("En cambio, todos escribían cartas.","Por outro lado, todos escreviam cartas."),("Con el tiempo, guardamos cada marco.","Com o tempo, guardamos cada moldura."),("Qué recuerdo tan importante.","Que lembrança tão importante.")],
   [("**A diferencia de** hoy, la familia viajaba menos.","Diferentemente de hoje, a família viajava menos."),("**En cambio**, se reunían cada domingo.","Por outro lado, reuniam-se todo domingo."),("**Con el tiempo**, la fotografía cambió.","Com o tempo, a fotografia mudou."),("**Qué recuerdo** conserva este álbum.","Que lembrança este álbum conserva."),("Comparamos colores y gestos.","Comparamos cores e gestos."),("Guardamos la foto en una nueva carpeta.","Guardamos a foto numa nova pasta."),("La exposición conecta generaciones.","A exposição conecta gerações."),("Cada imagen tiene una historia.","Cada imagem tem uma história.")]),
mk(297, "O caminho até a oficina", "pedir orientações e confirmar um destino", "Y tu mamá también", "2001",
   "O filme de Alfonso Cuarón acompanha uma viagem que transforma uma amizade. A cena é autoral e mostra uma pessoa procurando uma oficina numa cidade desconhecida.",
   [("taller","oficina","ta-YÊR"),("esquina","esquina","es-KÍ-na"),("semáforo","semáforo","se-MÁ-fo-ro"),("dirección","endereço","di-rek-SIÓN"),("cruce","cruzamento","KRÚ-se"),("mapa","mapa","MÁ-pa")],
   ["buscar","girar","seguir","llegar"],
   ["¿Cómo llego a...?","Como chego a...?","Siga recto","Siga em frente","A la vuelta de","Na esquina de","Desde aquí","Daqui"],
   ("g e j", ["taller","girar","dirección"]),
   [("Busco un taller cerca del centro.","Procuro uma oficina perto do centro."),("¿Me puede indicar la dirección?","Pode me indicar o endereço?"),("Siga recto hasta el semáforo.","Siga em frente até o semáforo."),("Gire en la segunda esquina.","Vire na segunda esquina."),("A la vuelta de la plaza, verá un cruce.","Na esquina da praça, você verá um cruzamento."),("Desde aquí, falta poco.","Daqui, falta pouco."),("¿Llego antes del mediodía?","Chego antes do meio-dia?"),("Sí, si sigue el mapa.","Sim, se seguir o mapa.")],
   [("**¿Cómo llego a...?** Busco el taller.","Como chego a...? Procuro a oficina."),("**Siga recto** hasta la avenida.","Siga em frente até a avenida."),("Está **a la vuelta de** la farmacia.","Fica na esquina da farmácia."),("**Desde aquí**, son cinco minutos.","Daqui, são cinco minutos."),("Confirmo la dirección en el mapa.","Confirmo o endereço no mapa."),("Giro con cuidado en el cruce.","Viro com cuidado no cruzamento."),("El taller está abierto.","A oficina está aberta."),("Gracias por la orientación.","Obrigado pela orientação.")]),
mk(298, "Uma receita compartilhada", "explicar um procedimento e pedir confirmação", "El lugar sin límites", "1978",
   "O filme chileno de Arturo Ripstein aborda comunidade, desejo e dignidade. A cena é autoral e mostra duas pessoas preparando uma receita de família para uma festa.",
   [("receta","receita","re-SÊ-ta"),("masa","massa","MÁ-sa"),("horno","forno","ÓR-no"),("relleno","recheio","re-YÊ-no"),("paso","passo","PÁ-so"),("ingrediente","ingrediente","in-gre-di-ÊN-te")],
   ["preparar","mezclar","añadir","comprobar"],
   ["Primero","Primeiro","Después","Depois","Antes de que","Antes que","¿Está claro?","Está claro?"],
   ("r e rr", ["receta","relleno","horno"]),
   [("Primero preparamos la masa.","Primeiro preparamos a massa."),("Después añadimos el relleno.","Depois adicionamos o recheio."),("¿Me pasas el ingrediente?","Você me passa o ingrediente?"),("Sí, está junto al horno.","Sim, está junto ao forno."),("Antes de que se caliente, mezclamos todo.","Antes que aqueça, misturamos tudo."),("Comprobamos cada paso.","Conferimos cada passo."),("¿Está claro el procedimiento?","Está claro o procedimento?"),("Sí, la receta queda lista.","Sim, a receita fica pronta.")],
   [("**Primero**, mezclamos la masa.","Primeiro, misturamos a massa."),("**Después**, añadimos el relleno.","Depois, adicionamos o recheio."),("**Antes de que** se caliente, revisamos el horno.","Antes que aqueça, revisamos o forno."),("**¿Está claro?** Sí, seguimos el paso.","Está claro? Sim, seguimos o passo."),("Preparamos la receta juntos.","Preparamos a receita juntos."),("Comprobamos la cantidad de cada ingrediente.","Conferimos a quantidade de cada ingrediente."),("La mesa está lista para la fiesta.","A mesa está pronta para a festa."),("Compartimos la comida y la historia.","Compartilhamos a comida e a história.")]),
]

PT = {"comparar":"comparar","elegir":"escolher","negociar":"negociar","ahorrar":"economizar","recibir":"receber","confirmar":"confirmar","avisar":"avisar","reunirse":"reunir-se","cambiar":"mudar","seguir":"seguir","cruzar":"atravessar","dibujar":"desenhar","parecer":"parecer","imaginar":"imaginar","interpretar":"interpretar","explicar":"explicar","formar":"formar","respetar":"respeitar","recomendar":"recomendar","leer":"ler","preferir":"preferir","perder":"perder","buscar":"procurar","reclamar":"reclamar","resolver":"resolver","ordenar":"ordenar","parecerse":"parecer-se","girar":"virar","llegar":"chegar","preparar":"preparar","mezclar":"misturar","añadir":"adicionar","comprobar":"conferir"}

def enrich(e, p, prev):
    out = make(e, p, prev)
    out["s"] = f"A2 · {p['focus']} · referencia: {p['work']}"
    out["t"] = p["t"]
    out["a"]["w"] = p["work"]; out["a"]["y"] = p["year"]; out["a"]["d"] = p["desc"]
    out["h"]["src"] = p["work"]
    out["p"] = f"Hoje você aprende a {p['focus']}, em uma situação inspirada por **{p['work']}**."
    # Keep the six entries as words and align every verb card with its real translation.
    out["v"] = [list(x) for x in p["v"]]
    vf = next(f for f in out["fr"] if f.get("k") == "verbs")
    for i, verb in enumerate(p["vb"]):
        if i < len(vf.get("items", [])):
            vf["items"][i]["v"] = verb; vf["items"][i]["pt"] = PT.get(verb, verb)
    # Distinct answer choices prevent the old repeated-placeholder defect.
    for f in out["fr"]:
        if f.get("k") == "pgsheet" and f.get("title") == "Palavras da cena":
            for i, item in enumerate(f.get("items", [])):
                w = p["v"][i % 6][0]; item["opts"] = [w, p["v"][(i+1)%6][0], p["v"][(i+2)%6][0]]; item["a"] = 0
    return out

all_data = {}
for path in TARGETS:
    data = json.loads(path.read_text(encoding="utf-8")); all_data.update({e["n"]: (path, e) for e in data})
for p in PLANS:
    path, old = all_data[p["n"]]
    prev = all_data[p["n"]-1][1] if p["n"]-1 in all_data else None
    all_data[p["n"]] = (path, enrich(old, p, prev))
for path in TARGETS:
    data = json.loads(path.read_text(encoding="utf-8"))
    out = [all_data[e["n"]][1] if e["n"] in all_data else e for e in data]
    path.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print("rewrote", ",".join(str(p["n"]) for p in PLANS))
