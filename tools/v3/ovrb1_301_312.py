# Reescrita dos episódios B1 301–312 (ver ovrb1.py e ovrb1_251_262.py).
from v3.ovrb1 import OVR, L
from v3.ovrb1_251_262 import C, F, W, WORKS

# ---------------------------------------------------------------- 301 / 302
F(82195, [['I am all ears, tell me everything.', 'Sou todo ouvidos, conte tudo.'], ['It is late, let us call it a day.', 'Está tarde, vamos encerrar por hoje.'],
          ['Does that name ring a bell?', 'Esse nome lhe diz alguma coisa?'], ['We hit the road at dawn.', 'Pegamos a estrada ao amanhecer.']])

W(7082195, 'Friends', '📺 Série · 1994', 'Friends é uma série de comédia americana de 1994 sobre um grupo de amigos que vivem em Nova York e se encontram num café.', ['☕', '🛋️', '🏢'], 'rainycafe')
C(7082195, ('Rachel', 'Ross'), ['polly', 'tom'], 'cafe2', 'No café do bairro, Rachel e Ross combinam a noite com expressões do dia a dia.',
  ('☕', 'mug', 'caneca', 'No worries, take my mug.', 'Sem problema, pegue minha caneca.'),
  [('🛋️', 'couch', 'sofá', 'Soa como “KÁUTCH”.'), ('🏢', 'apartment', 'apartamento', 'Soa como “a-PAR-t-ment”.'), ('🃏', 'joke', 'piada', 'Soa como “DJÔUK”.'),
   ('📺', 'episode', 'episódio', 'Soa como “É-pi-sôud”.'), ('🎭', 'audition', 'teste de elenco', 'Soa como “o-DÍ-shon”.'), ('👋', 'neighbor', 'vizinho', 'Soa como “NÊI-ber”.')],
  [('borrow', '🤲', 'pegar emprestado', 'Can I borrow your keys?', 'Can I borrow to you keys?', 'I borrowed.', 'Peguei emprestado.', 'borrow **+ objeto**.'),
   ('order', '🍕', 'pedir', 'Let us order pizza.', 'Let us order for pizza.', 'We ordered.', 'Pedimos.', 'order **+ objeto**.'),
   ('meet', '🤝', 'encontrar', 'Meet me at the café.', 'Meet to me at the café.', 'We met.', 'Nos encontramos.', 'meet → **met**.'),
   ('plan', '📝', 'planejar', 'We plan the night.', 'We plans the night.', 'We planned.', 'Planejamos.', 'plural: **plan**.')],
  [['Rachel', 'Speak of the devil, here comes Ross!', 'Falando no diabo, lá vem o Ross!'], ['Ross', 'No worries, I was only five minutes late.', 'Sem problema, só me atrasei cinco minutos.'],
   ['Rachel', 'Are we on the same page about tonight?', 'Estamos combinados sobre esta noite?'], ['Ross', 'Pizza at my apartment and a movie. Same page.', 'Pizza no meu apartamento e um filme. Combinado.'],
   ['Rachel', 'The pizza there is top notch.', 'A pizza de lá é de primeira.'], ['Ross', 'Can I borrow your mug? Mine is dirty.', 'Posso pegar sua caneca? A minha está suja.'],
   ['Rachel', 'No worries, take it.', 'Sem problema, pegue.'], ['Ross', 'Then we meet at eight. Same page?', 'Então nos vemos às oito. Combinado?']],
  [('Who comes in?', 'Quem chega?', [('👨', 'Ross'), ('👩', 'Monica'), ('👴', 'The waiter')], 0, 0, 'Rachel diz: “here comes Ross!”'),
   ('What do they have tonight?', 'O que terão esta noite?', [('🍕', 'Pizza and a movie'), ('🎳', 'Bowling'), ('🎤', 'Karaoke')], 0, 3, 'Ross diz: “Pizza at my apartment and a movie.”'),
   ('What does Ross want to borrow?', 'O que Ross quer pegar emprestado?', [('☕', 'A mug'), ('🔑', 'Keys'), ('🧥', 'A jacket')], 0, 5, 'Ross diz: “Can I borrow your mug?”')],
  L('fr', 'Laboratório de sons: couch, apartment e neighbor', 'ou soa áu; ar soa ar; ei soa êi.', 'Em couch, o ou soa áu.',
    [('couch', 'KÁUTCH', 'sofá', 'ou = áu', 'coach', 'KÔUTCH'), ('apartment', 'a-PAR-t-ment', 'apartamento', 'ar = ar', 'department', 'di-PAR-t-ment'), ('neighbor', 'NÊI-ber', 'vizinho', 'ei = êi', 'number', 'NÂM-ber')]),
  [['Is the new neighbor friendly?', 'O vizinho novo é simpático?'], ['Very, he brought a pie on day one.', 'Muito, trouxe uma torta no primeiro dia.'],
   ['Then invite him to the couch night.', 'Então convide-o para a noite do sofá.'], ['I already did. He said yes.', 'Já convidei. Ele disse que sim.']])

# ---------------------------------------------------------------- 303 / 304
F(82197, [['In my opinion, he is not guilty.', 'Na minha opinião, ele não é culpado.'], ['Personally, I need more proof.', 'Pessoalmente, preciso de mais provas.'],
          ['I believe the story has holes.', 'Acredito que a história tem furos.'], ['It seems we must vote again.', 'Parece que vamos precisar votar de novo.']])

W(7082197, 'The Hound of the Baskervilles', '📚 Livro · 1902', 'O Cão dos Baskerville é um romance de Arthur Conan Doyle, publicado em 1902: Sherlock Holmes e o doutor Watson investigam uma lenda sobre um cão misterioso numa charneca inglesa.', ['🐕', '🌫️', '🔦'], 'cave')
C(7082197, ('Holmes', 'Watson'), ['sherlock', 'watson'], 'street', 'Na charneca enevoada, Holmes e Watson discutem o que é certo e o que é só provável.',
  ('🐕', 'hound', 'cão de caça', 'I am sure the hound is a dog.', 'Tenho certeza de que o cão é um cachorro.'),
  [('🌫️', 'fog', 'névoa', 'Soa como “FÓG”.'), ('🏞️', 'moor', 'charneca', 'Soa como “MÚR”.'), ('👣', 'footprint', 'pegada', 'Soa como “FÚT-print”.'),
   ('🔦', 'lantern', 'lanterna', 'Soa como “LÉN-tern”.'), ('🧐', 'suspect', 'suspeito', 'Soa como “SÂS-pékt”.'), ('📜', 'legend', 'lenda', 'Soa como “LÉ-djend”.')],
  [('suspect', '🧐', 'suspeitar', 'I suspect the butler.', 'I suspect to the butler.', 'I suspected.', 'Suspeitei.', 'suspect **+ objeto**.'),
   ('track', '👣', 'rastrear', 'We track the footprints.', 'We track to the footprints.', 'We tracked.', 'Rastreamos.', 'track **+ objeto**.'),
   ('guess', '🎲', 'adivinhar', 'Guess who it is.', 'Guess who is it.', 'I guessed.', 'Adivinhei.', 'guess **who it is**.'),
   ('warn', '⚠️', 'avisar', 'I warn you.', 'I warn to you.', 'I warned you.', 'Avisei você.', 'warn **+ objeto**.')],
  [['Watson', 'Do you think the hound is real, Holmes?', 'Você acha que o cão é real, Holmes?'], ['Holmes', 'I am sure it is not a ghost.', 'Tenho certeza de que não é um fantasma.'],
   ['Watson', 'I suppose someone trains it.', 'Suponho que alguém o treine.'], ['Holmes', 'Probably, yes. A man with a plan.', 'Provavelmente, sim. Um homem com um plano.'],
   ['Watson', 'Is it the neighbour? I doubt it.', 'É o vizinho? Duvido.'], ['Holmes', 'I doubt it too, but he probably knows more.', 'Eu também duvido, mas ele provavelmente sabe mais.'],
   ['Watson', 'I am sure we are close.', 'Tenho certeza de que estamos perto.'], ['Holmes', 'I suppose we go to the moor tonight.', 'Suponho que iremos à charneca esta noite.']],
  [('What is Holmes sure of?', 'De que Holmes tem certeza?', [('👻', 'It is not a ghost'), ('🐉', 'It is a dragon'), ('🐱', 'It is a cat')], 0, 1, 'Holmes diz: “I am sure it is not a ghost.”'),
   ('Does Watson think it is the neighbour?', 'Watson acha que é o vizinho?', [('🙅', 'He doubts it'), ('🙆', 'He is sure'), ('🤷', 'He does not care')], 0, 4, 'Watson diz: “I doubt it.”'),
   ('Where do they go tonight?', 'Aonde vão esta noite?', [('🏞️', 'To the moor'), ('🏠', 'Home'), ('🏖️', 'To the beach')], 0, 7, 'Holmes diz: “we go to the moor tonight.”')],
  L('hh', 'Laboratório de sons: fog, moor e lantern', 'o soa ó; oo soa ú; a soa é.', 'Em moor, o oo soa ú.',
    [('fog', 'FÓG', 'névoa', 'o = ó', 'fig', 'FÍG'), ('moor', 'MÚR', 'charneca', 'oo = ú', 'more', 'MÓR'), ('lantern', 'LÉN-tern', 'lanterna', 'a = é', 'lender', 'LÉN-der')]),
  [['Is the fog thick over the moor tonight?', 'A névoa está espessa sobre a charneca esta noite?'], ['Thick enough to hide a whole house.', 'Espessa o bastante para esconder uma casa inteira.'],
   ['Then take the lantern and stay close.', 'Então leve a lanterna e fique perto.'], ['I will, and I will keep my revolver ready.', 'Vou ficar, e manterei o revólver pronto.']])

# ---------------------------------------------------------------- 305 / 306
F(930043, [['I also handle the phones.', 'Eu também cuido dos telefones.'], ['Additionally, I update the calendar.', 'Além disso, atualizo a agenda.'],
           ['Likewise, I welcome the new interns.', 'Da mesma forma, recebo os novos estagiários.'], ['Good work, as well as good manners.', 'Bom trabalho, além de boas maneiras.']])

W(7930043, 'The Devil Wears Prada', '🎬 Filme · 2006', 'O Diabo Veste Prada é um filme de 2006, baseado no romance de Lauren Weisberger: uma jovem assistente trabalha para a exigente editora de uma revista de moda.', ['👗', '📰', '☕'], 'toyshop')
C(7930043, ('Miranda', 'Andy'), ['misshoney', 'polly'], 'office', 'Na redação da revista, Miranda lista cobranças com conectores formais, e Andy responde no mesmo tom.',
  ('🖨️', 'printer', 'impressora', 'In addition, fix the printer.', 'Além disso, conserte a impressora.'),
  [('📰', 'magazine', 'revista', 'Soa como “MÉ-ga-zín”.'), ('👗', 'dress', 'vestido', 'Soa como “DRÉS”.'), ('📅', 'schedule', 'agenda', 'Soa como “SKÉ-djul”.'),
   ('☕', 'coffee', 'café', 'Soa como “KÓ-fi”.'), ('🧑‍💼', 'assistant', 'assistente', 'Soa como “a-SÍS-tent”.'), ('📞', 'client', 'cliente', 'Soa como “KLÁI-ent”.')],
  [('print', '🖨️', 'imprimir', 'Print the report.', 'Print to the report.', 'I printed it.', 'Imprimi.', 'print **+ objeto**.'),
   ('deliver', '📦', 'entregar', 'Deliver it by noon.', 'Deliver to it by noon.', 'I delivered it.', 'Entreguei.', 'deliver **+ objeto**.'),
   ('fetch', '🏃', 'buscar', 'Fetch the coffee.', 'Fetch to the coffee.', 'I fetched it.', 'Busquei.', 'fetch **+ objeto**.'),
   ('approve', '✅', 'aprovar', 'She approves the design.', 'She approve the design.', 'She approved it.', 'Ela aprovou.', 'he/she **approves**.')],
  [['Miranda', 'Furthermore, the report is late.', 'Além disso, o relatório está atrasado.'], ['Andy', 'In addition, the printer is broken.', 'Além disso, a impressora quebrou.'],
   ['Miranda', 'What is more, the client is waiting.', 'Mais ainda, o cliente está esperando.'], ['Andy', 'Not only did I call him, but I also sent an email.', 'Não só liguei para ele, como também enviei um e-mail.'],
   ['Miranda', 'Furthermore, I want it on my desk by noon.', 'Além disso, quero isso na minha mesa até o meio-dia.'], ['Andy', 'In addition to the report, I bring your coffee.', 'Além do relatório, trago o seu café.'],
   ['Miranda', 'What is more, bring the schedule too.', 'Mais ainda, traga a agenda também.'], ['Andy', 'Not only the schedule, but also the dresses are ready.', 'Não só a agenda, mas também os vestidos estão prontos.']],
  [('What is late?', 'O que está atrasado?', [('📄', 'The report'), ('☕', 'The coffee'), ('👗', 'The dress')], 0, 0, 'Miranda diz: “the report is late.”'),
   ('What is broken?', 'O que está quebrado?', [('🖨️', 'The printer'), ('📞', 'The phone'), ('💻', 'The computer')], 0, 1, 'Andy diz: “the printer is broken.”'),
   ('When does Miranda want the report?', 'Quando Miranda quer o relatório?', [('🕛', 'By noon'), ('🌙', 'At night'), ('📅', 'Next week')], 0, 4, 'Miranda diz: “by noon.”')],
  L('dp', 'Laboratório de sons: magazine, schedule e client', 'a soa é; sch soa sk; i soa ái.', 'Em schedule, o sch soa sk.',
    [('magazine', 'MÉ-ga-zín', 'revista', 'a = é', 'imagine', 'i-MÉ-djin'), ('schedule', 'SKÉ-djul', 'agenda', 'sch = sk', 'shed', 'SHÉD'), ('client', 'KLÁI-ent', 'cliente', 'i = ái', 'clean', 'KLÍN')]),
  [['Did the new assistant survive the first week?', 'A nova assistente sobreviveu à primeira semana?'], ['She did, and she even learned the schedule.', 'Sobreviveu e até aprendeu a agenda.'],
   ['Then she may stay for the next issue.', 'Então pode ficar para a próxima edição.'], ['That is the best praise we give here.', 'Esse é o melhor elogio que damos aqui.']])

# ---------------------------------------------------------------- 307 / 308
F(82198, [['I agree, it was a lovely evening.', 'Concordo, foi uma noite adorável.'], ['Exactly, and the music was perfect.', 'Exatamente, e a música estava perfeita.'],
          ['Absolutely, I think so too.', 'Com certeza, também acho.'], ['Same here, let us dance again.', 'Comigo também, vamos dançar de novo.']])

W(7082198, 'Emma', '📚 Livro · 1815', 'Emma é um romance de Jane Austen, publicado em 1815: a jovem Emma gosta de arranjar casamentos para os amigos, e o amigo Mr Knightley discorda de seus planos.', ['💍', '🎹', '🏡'], 'library')
C(7082198, ('Emma', 'Mr Knightley'), ['polly', 'tom'], 'living', 'Na sala de uma casa de campo, Emma e Mr Knightley discordam, com educação, sobre um noivado.',
  ('💌', 'letter', 'carta', 'I see your point about the letter.', 'Entendo o seu argumento sobre a carta.'),
  [('🏡', 'estate', 'propriedade', 'Soa como “is-TÊIT”.'), ('💍', 'engagement', 'noivado', 'Soa como “en-GUÊIDJ-ment”.'), ('🎹', 'piano', 'piano', 'Soa como “pi-É-nôu”.'),
   ('🏘️', 'village', 'vila', 'Soa como “VÍ-lidj”.'), ('👒', 'bonnet', 'chapéu de aba', 'Soa como “BÓ-nit”.'), ('💡', 'advice', 'conselho', 'Soa como “ed-VÁIS”.')],
  [('advise', '💡', 'aconselhar', 'I advise you to wait.', 'I advise you wait.', 'I advised.', 'Aconselhei.', 'advise **+ to**.'),
   ('decline', '🙅', 'recusar', 'She declines the offer.', 'She decline the offer.', 'She declined.', 'Ela recusou.', 'he/she **declines**.'),
   ('accept', '✅', 'aceitar', 'Accept the offer.', 'Accept to the offer.', 'I accepted.', 'Aceitei.', 'accept **+ objeto**.'),
   ('regret', '😔', 'lamentar', 'I regret nothing.', 'I regrets nothing.', 'I regretted it.', 'Lamentei.', 'I **regret**.')],
  [['Knightley', 'Emma, I think Harriet should decline him.', 'Emma, acho que Harriet deve recusá-lo.'], ['Emma', 'I see your point, but I am not so sure.', 'Entendo seu argumento, mas não tenho tanta certeza.'],
   ['Knightley', 'I disagree. He is not a good match.', 'Discordo. Ele não é um bom partido.'], ['Emma', 'True, but she likes him.', 'É verdade, mas ela gosta dele.'],
   ['Knightley', 'True, but liking is not enough.', 'É verdade, mas gostar não basta.'], ['Emma', 'I see your point. I am not so sure I was right.', 'Entendo seu argumento. Não tenho tanta certeza de que eu estava certa.'],
   ['Knightley', 'Then we disagree less than we think.', 'Então discordamos menos do que pensamos.'], ['Emma', 'Perhaps. Let us talk tomorrow.', 'Talvez. Conversamos amanhã.']],
  [('What does Knightley think Harriet should do?', 'O que Knightley acha que Harriet deve fazer?', [('🙅', 'Decline him'), ('💍', 'Accept him'), ('🏃', 'Leave town')], 0, 0, 'Knightley diz: “Harriet should decline him.”'),
   ('How does Emma answer first?', 'Como Emma responde primeiro?', [('🤔', 'I am not so sure'), ('😡', 'You are wrong'), ('😴', 'Nothing')], 0, 1, 'Emma diz: “I am not so sure.”'),
   ('When do they talk again?', 'Quando voltam a conversar?', [('📅', 'Tomorrow'), ('🌙', 'Tonight'), ('📆', 'Next year')], 0, 7, 'Emma diz: “Let us talk tomorrow.”')],
  L('em', 'Laboratório de sons: estate, advice e village', 'e soa i; ice soa áis; i soa i.', 'Em advice, o ice soa áis.',
    [('estate', 'is-TÊIT', 'propriedade', 'e = i', 'state', 'STÊIT'), ('advice', 'ed-VÁIS', 'conselho', 'ice = áis', 'advise', 'ed-VÁIZ'), ('village', 'VÍ-lidj', 'vila', 'i = í', 'valley', 'VÉ-li')]),
  [['Does Harriet already know his answer?', 'Harriet já sabe a resposta dele?'], ['Not yet, and she is very nervous.', 'Ainda não, e está muito nervosa.'],
   ['Then Emma should not interfere again.', 'Então Emma não deve interferir de novo.'], ['That is easier said than done.', 'Isso é mais fácil de dizer do que de fazer.']])

# ---------------------------------------------------------------- 309 / 310
F(82201, [['He is guilty because he ran away.', 'Ele é culpado porque fugiu.'], ['Since nobody saw him, we cannot be sure.', 'Como ninguém o viu, não podemos ter certeza.'],
          ['That is why I voted not guilty.', 'É por isso que votei inocente.'], ['The reason is simple: there is doubt.', 'A razão é simples: há dúvida.']])

W(7082201, 'Murder on the Orient Express', '📚 Livro · 1934', 'Assassinato no Expresso do Oriente é um romance policial de Agatha Christie, publicado em 1934: o detetive Hercule Poirot investiga um crime num trem parado pela neve.', ['🚂', '❄️', '🔒'], 'viaduct')
C(7082201, ('Poirot', 'Bouc'), ['tom', 'tommy'], 'office', 'Num vagão parado pela neve, Poirot e o amigo Bouc explicam os motivos de cada pista.',
  ('🧣', 'scarf', 'cachecol', 'Because of the scarf, I know.', 'Por causa do cachecol, eu sei.'),
  [('🚂', 'train', 'trem', 'Soa como “TRÊIN”.'), ('❄️', 'snow', 'neve', 'Soa como “SNÔU”.'), ('🔒', 'lock', 'tranca', 'Soa como “LÓK”.'),
   ('🧳', 'passenger', 'passageiro', 'Soa como “PÉ-sen-djer”.'), ('🪪', 'passport', 'passaporte', 'Soa como “PÉS-pórt”.'), ('🎯', 'motive', 'motivo', 'Soa como “MÔU-tiv”.')],
  [('lock', '🔒', 'trancar', 'Lock the door.', 'Lock to the door.', 'I locked it.', 'Tranquei.', 'lock **+ objeto**.'),
   ('question', '❓', 'interrogar', 'Question the passengers.', 'Question to the passengers.', 'I questioned them.', 'Interroguei.', 'question **+ objeto**.'),
   ('delay', '⏳', 'atrasar', 'Snow delays the train.', 'Snow delay the train.', 'It delayed us.', 'Nos atrasou.', 'he/she/it **delays**.'),
   ('arrest', '👮', 'prender', 'They arrest him.', 'They arrests him.', 'They arrested him.', 'Prenderam-no.', 'plural: **arrest**.')],
  [['Bouc', 'Due to the snow, the train has stopped.', 'Devido à neve, o trem parou.'], ['Poirot', 'Because of the snow, nobody can leave.', 'Por causa da neve, ninguém pode sair.'],
   ['Bouc', 'Thanks to you, we have a chance to solve it.', 'Graças a você, temos uma chance de resolver.'], ['Poirot', 'Owing to the locked doors, the killer is still here.', 'Devido às portas trancadas, o assassino ainda está aqui.'],
   ['Bouc', 'Because of that, everyone is a suspect.', 'Por causa disso, todos são suspeitos.'], ['Poirot', 'Due to one small clue, I know more.', 'Devido a uma pequena pista, sei mais.'],
   ['Bouc', 'Thanks to your clue, we are close.', 'Graças à sua pista, estamos perto.'], ['Poirot', 'Owing to luck, and a little thinking.', 'Devido à sorte e a um pouco de raciocínio.']],
  [('Why has the train stopped?', 'Por que o trem parou?', [('❄️', 'Due to the snow'), ('🔧', 'It broke'), ('⛽', 'No fuel')], 0, 0, 'Bouc diz: “Due to the snow, the train has stopped.”'),
   ('Why is the killer still here?', 'Por que o assassino ainda está aqui?', [('🔒', 'The doors are locked'), ('🚪', 'The doors are open'), ('🌙', 'It is night')], 0, 3, 'Poirot diz: “Owing to the locked doors.”'),
   ('Thanks to what are they close?', 'Graças a quê estão perto?', [('🧩', 'A clue'), ('🍀', 'A coin'), ('📞', 'A call')], 0, 6, 'Bouc diz: “Thanks to your clue, we are close.”')],
  L('oe', 'Laboratório de sons: train, snow e passport', 'ai soa êi; ow soa ôu; a soa é.', 'Em train, o ai soa êi.',
    [('train', 'TRÊIN', 'trem', 'ai = êi', 'tray', 'TRÊI'), ('snow', 'SNÔU', 'neve', 'ow = ôu', 'now', 'NÁU'), ('passport', 'PÉS-pórt', 'passaporte', 'a = é', 'pasta', 'PÉS-ta')]),
  [['Who has the room next to the victim?', 'Quem está no quarto ao lado da vítima?'], ['A lady who says she heard nothing.', 'Uma senhora que diz não ter ouvido nada.'],
   ['Then ask her about the scarf again.', 'Então pergunte a ela de novo sobre o cachecol.'], ['I will, once the snow stops falling.', 'Perguntarei, quando a neve parar de cair.']])

# ---------------------------------------------------------------- 311 / 312
F(82202, [['What do you think of the plan?', 'O que você acha do plano?'], ['How do you feel about moving?', 'O que você sente sobre a mudança?'],
          ['Any ideas for the garden?', 'Alguma ideia para o jardim?'], ['I think we should wait a month.', 'Acho que devemos esperar um mês.']])

W(7082202, 'The Tale of Peter Rabbit', '📚 Livro · 1902', 'O Conto do Coelho Pedro (The Tale of Peter Rabbit) é um livro infantil de Beatrix Potter, publicado em 1902: o coelho Peter entra na horta do Sr. McGregor e precisa fugir.', ['🐰', '🥕', '🧺'], 'bakery')
C(7082202, ('Peter', 'Flopsy'), ['peterrabbit', 'rabbit'], 'yard', 'Na toca, Peter e Flopsy sugerem passeios e escolhem o que fazer.',
  ('🧺', 'basket', 'cesta', 'How about the basket?', 'Que tal a cesta?'),
  [('🥬', 'lettuce', 'alface', 'Soa como “LÉ-tis”.'), ('🥕', 'carrot', 'cenoura', 'Soa como “KÉ-rot”.'), ('🧥', 'jacket', 'casaco', 'Soa como “DJÉ-kit”.'),
   ('🌿', 'parsley', 'salsa', 'Soa como “PAR-sli”.'), ('👨‍🌾', 'gardener', 'jardineiro', 'Soa como “GAR-de-ner”.'), ('🐇', 'bunny', 'coelhinho', 'Soa como “BÂ-ni”.')],
  [('nibble', '🐰', 'mordiscar', 'I nibble a carrot.', 'I nibbles a carrot.', 'I nibbled.', 'Mordisquei.', 'I **nibble**.'),
   ('hop', '🐇', 'pular', 'We hop over the gate.', 'We hop to the gate.', 'We hopped.', 'Pulamos.', 'hop **over**.'),
   ('squeeze', '🤏', 'espremer-se', 'Squeeze under the gate.', 'Squeeze to under the gate.', 'I squeezed.', 'Espremi-me.', 'squeeze **under**.'),
   ('lose', '😢', 'perder', 'I lose my jacket.', 'I loses my jacket.', 'I lost it.', 'Perdi.', 'lose → **lost**.')],
  [['Flopsy', 'How about a walk in the garden?', 'Que tal um passeio no jardim?'], ['Peter', 'Shall we go through the gate?', 'Vamos passar pelo portão?'],
   ['Flopsy', 'Do you think we should wait for the gardener to leave?', 'Você acha que devemos esperar o jardineiro sair?'], ['Peter', 'Would you like some lettuce first?', 'Quer um pouco de alface primeiro?'],
   ['Flopsy', 'How about carrots instead?', 'Que tal cenouras no lugar?'], ['Peter', 'Should we take the little basket?', 'Devemos levar a cestinha?'],
   ['Flopsy', 'Shall we ask Mopsy to come too?', 'Vamos chamar a Mopsy também?'], ['Peter', 'Would you like to hurry? He is coming!', 'Quer se apressar? Ele está vindo!']],
  [('Where does Flopsy suggest a walk?', 'Onde Flopsy sugere um passeio?', [('🌱', 'In the garden'), ('🏖️', 'On the beach'), ('🏫', 'At school')], 0, 0, 'Flopsy diz: “How about a walk in the garden?”'),
   ('What does Peter offer first?', 'O que Peter oferece primeiro?', [('🥬', 'Lettuce'), ('🥕', 'Carrots'), ('🍞', 'Bread')], 0, 3, 'Peter diz: “some lettuce first?”'),
   ('Who is coming?', 'Quem está vindo?', [('👨‍🌾', 'The gardener'), ('🐱', 'A cat'), ('🐺', 'A wolf')], 0, 7, 'Peter diz: “He is coming!”')],
  L('pr', 'Laboratório de sons: lettuce, carrot e bunny', 'e soa é; a soa é; u soa â.', 'Em bunny, o u soa â.',
    [('lettuce', 'LÉ-tis', 'alface', 'e = é', 'let us', 'LÉ-tâs'), ('carrot', 'KÉ-rot', 'cenoura', 'a = é', 'cart', 'KÁRT'), ('bunny', 'BÂ-ni', 'coelhinho', 'u = â', 'bonnie', 'BÓ-ni')]),
  [['Where did Peter lose his jacket?', 'Onde Peter perdeu o casaco?'], ['Somewhere near the cabbages, I fear.', 'Em algum lugar perto dos repolhos, receio.'],
   ['Then Mother will ask him about it.', 'Então a mãe vai perguntar a ele sobre isso.'], ['And he will say he has no idea.', 'E ele vai dizer que não faz ideia.']])
