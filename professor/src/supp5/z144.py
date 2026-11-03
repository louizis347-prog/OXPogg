"""Bloco de verbos e expressões da aula 144: museu em Washington."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('visit', '🏛️', 'visitar', ('visit', 'We visit the museum today.', 'Nós visitamos o museu hoje.'), ('visits', 'Ana visits the gallery.', 'A Ana visita a galeria.'), ('visited', 'We visited a museum in D.C.', 'Nós visitamos um museu em D.C.'), ('visiting', 'We are visiting Washington.', 'Estamos visitando Washington.'), 'Visit é verbo regular: visited.'),
  vb('touch', '✋', 'tocar', ('touch', 'Please do not touch the bones.', 'Por favor, não toque nos ossos.'), ('touches', 'Leo touches the glass.', 'O Leo toca no vidro.'), ('touched', 'He touched the sign.', 'Ele tocou na placa.'), ('touching', 'He is touching the glass.', 'Ele está tocando no vidro.'), 'Touch termina em -ch: touches na 3ª pessoa.'),
  vb('point', '👉', 'apontar', ('point', 'I point at the skeleton.', 'Eu aponto para o esqueleto.'), ('points', 'Leo points at the map.', 'O Leo aponta para o mapa.'), ('pointed', 'He pointed to the left.', 'Ele apontou para a esquerda.'), ('pointing', 'He is pointing at a bone.', 'Ele está apontando para um osso.'), 'Point at / point to = apontar para algo.'),
  vb('learn', '🧠', 'aprender', ('learn', 'We learn about dinosaurs.', 'Nós aprendemos sobre dinossauros.'), ('learns', 'Leo learns a new word.', 'O Leo aprende uma palavra nova.'), ('learned', 'We learned about bones.', 'Nós aprendemos sobre ossos.'), ('learning', 'We are learning a lot.', 'Estamos aprendendo muito.'), 'Passado: learned (também se aceita learnt).'),
  vb('enter', '🚪', 'entrar', ('enter', 'We enter on the left.', 'Nós entramos pela esquerda.'), ('enters', 'Ana enters the museum.', 'A Ana entra no museu.'), ('entered', 'They entered the gallery.', 'Eles entraram na galeria.'), ('entering', 'They are entering now.', 'Eles estão entrando agora.'), 'Enter é transitivo: enter the room, sem in.')],
 verb_game=[
  dict(scene='Agora eles estão entrando no museu.', en='They are ___ the museum.', opts=['enter', 'entering', 'entered'], ans=1, pt='Eles estão entrando no museu.', why='“are” + -ing: entering.'),
  dict(scene='Ontem vocês visitaram um museu.', en='Yesterday we ___ a museum.', opts=['visit', 'visits', 'visited'], ans=2, pt='Ontem nós visitamos um museu.', why='“Yesterday” pede passado: visited.'),
  dict(scene='O Leo toca no vidro.', en='Leo ___ the glass.', opts=['touch', 'touches', 'touched'], ans=1, pt='O Leo toca no vidro.', why='Ele (3ª pessoa) leva -es: touches.'),
  dict(scene='Você quer aprender sobre fósseis.', en='I want to ___ about fossils.', opts=['learn', 'learns', 'learning'], ans=0, pt='Quero aprender sobre fósseis.', why='Depois de to, use o verbo base: learn.')],
 expressions=[
  dict(en='Two adults, please.', pt='Dois adultos, por favor.', ex='Hi. Two adults, please.', exp='Para pedir entrada na bilheteria.', c='a'),
  dict(en='Free admission', pt='Entrada grátis', ex='The museum has free admission.', exp='Para falar de museus sem cobrança.', c='b'),
  dict(en='Here’s a map.', pt='Aqui está um mapa.', ex='Welcome! Here’s a map.', exp='Para entregar o mapa a um visitante.', c='c'),
  dict(en='On the first floor', pt='No primeiro andar', ex='The dinosaurs are on the first floor.', exp='Para dizer em que andar algo fica.', c='d'),
  dict(en='No flash, please.', pt='Sem flash, por favor.', ex='You can take photos, but no flash, please.', exp='Para lembrar a regra das fotos.', c='a'),
  dict(en='Take your time.', pt='Sem pressa.', ex='Look at everything. Take your time.', exp='Para dizer que a pessoa pode olhar com calma.', c='b')],
 expr_game=[
  dict(cue='Você pede a entrada para duas pessoas adultas.', opts=['Two adults, please.', 'Here’s a map.', 'Take your time.'], ans=0, why='Pedido de ingresso na bilheteria.'),
  dict(cue='Você diz em qual andar ficam os dinossauros.', opts=['On the first floor.', 'No flash, please.', 'Two adults, please.'], ans=0, why='On the first floor = no primeiro andar.'),
  dict(cue='Você lembra que a câmera não pode usar flash.', opts=['No flash, please.', 'Here’s a map.', 'Take your time.'], ans=0, why='No flash, please é a regra comum.')])
