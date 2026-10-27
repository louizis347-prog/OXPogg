# Reescrita dos episódios B1 111–140 (ver ovrb1.py).
from v3.ovrb1 import OVR, L

# ---------------------------------------------------------------- 111–115
OVR[930016] = dict(fill=[['Who carries the flag at the start?', 'Quem leva a bandeira na largada?'], ['I will. You hold the rope.', 'Eu levo. Você segura a corda.'],
                         ['The crowd is loud today.', 'A multidão está barulhenta hoje.'], ['Then we start with a smile.', 'Então começamos sorrindo.']])

OVR[7930016] = dict(
    names=('Athos', 'D’Artagnan'), ids=['athos', 'dartagnan'], rs='yard',
    cv='Num pátio de Paris, Athos e D’Artagnan dividem as tarefas da missão.',
    obra=('Who will take the lead on this mission?', 'Quem vai assumir a frente desta missão?'),
    vocab=[('⚔️', 'sword', 'espada', 'Soa como “SÓRD”.'), ('🐴', 'horse', 'cavalo', 'Soa como “HÓRS”.'), ('👑', 'king', 'rei', 'Soa como “KÍNG”.'),
           ('🛡️', 'guard', 'guarda', 'Soa como “GÁRD”.'), ('✉️', 'message', 'mensagem', 'Soa como “MÉ-sidj”.'), ('🤝', 'oath', 'juramento', 'Soa como “ÔUTH”.')],
    hot4=('⚔️', 'sword', 'espada', 'We draw our swords together.', 'Sacamos nossas espadas juntos.'),
    lines=[['D’Artagnan', 'Who will take the lead on this mission?', 'Quem vai assumir a frente desta missão?'],
           ['Athos', 'I will. Keep me in the loop.', 'Eu assumo. Mantenha-me informado.'],
           ['D’Artagnan', 'Can you lend a hand with the horses?', 'Pode dar uma mão com os cavalos?'],
           ['Athos', 'Sure.', 'Claro.'],
           ['D’Artagnan', 'We must pull together this week.', 'Precisamos unir forças esta semana.'],
           ['Athos', 'Yes. The message for the king is near.', 'Sim. A mensagem para o rei está próxima.'],
           ['D’Artagnan', 'Great teamwork.', 'Ótimo trabalho em equipe.'],
           ['Athos', 'One for all, and all for one.', 'Um por todos, e todos por um.']],
    quiz=[('Who takes the lead?', 'Quem assume a frente?', [('🛡️', 'Athos'), ('🗡️', 'D’Artagnan'), ('👑', 'The king')], 0, 1, 'Athos diz: “I will.”'),
          ('What does he ask for?', 'O que ele pede?', [('🐴', 'A hand with the horses'), ('💰', 'Money'), ('🍕', 'Lunch')], 0, 2, 'D’Artagnan diz: “lend a hand with the horses.”'),
          ('What must they do this week?', 'O que precisam fazer esta semana?', [('🪢', 'Pull together'), ('😴', 'Rest'), ('✈️', 'Travel')], 0, 4, 'D’Artagnan diz: “pull together.”')],
    fill=[['The horses are ready at dawn.', 'Os cavalos estarão prontos ao amanhecer.'], ['Then I will bring the message.', 'Então levo a mensagem.'],
          ['Keep it dry and out of sight.', 'Mantenha-a seca e fora de vista.'], ['You have my word.', 'Tem a minha palavra.']])

OVR[82076] = dict(fill=[['Do not forget your keys.', 'Não esqueça as chaves.'], ['They are in my coat pocket.', 'Estão no bolso do casaco.'],
                        ['Then drive carefully.', 'Então dirija com cuidado.'], ['I will. Talk to you tonight.', 'Vou dirigir. Falo com você hoje à noite.']])

OVR[7082076] = dict(
    names=('Pinocchio', 'Geppetto'), ids=['pinocchio', 'geppetto'], rs='hall',
    cv='Na oficina, Pinocchio e Geppetto combinam a saída para a escola.',
    obra=('When can we leave? After I finish my lesson.', 'Quando podemos sair? Depois que eu terminar a lição.'),
    vocab=[('🪆', 'puppet', 'marionete', 'Soa como “PÂ-pit”.'), ('🏫', 'school', 'escola', 'Soa como “SKÚL”.'), ('🪚', 'workshop', 'oficina', 'Soa como “UÔRK-shop”.'),
           ('🌙', 'dark', 'escuro', 'Soa como “DÁRK”.'), ('🧵', 'string', 'fio', 'Soa como “STRÍNG”.'), ('📖', 'lesson', 'lição', 'Soa como “LÉ-son”.')],
    hot4=('🪆', 'puppet', 'marionete', 'A puppet cannot be late.', 'Uma marionete não pode se atrasar.'),
    verbs=[('study', '📖', 'estudar', 'After I study, I will rest.', 'After I will study, I will rest.', 'I studied.', 'Estudei.', 'after + **presente**.'),
           ('finish', '✅', 'terminar', 'After I finish, I will rest.', 'After I will finish, I will rest.', 'I finished.', 'Terminei.', 'after I **finish**.'),
           ('end', '🔚', 'acabar', 'The moment it ends, we leave.', 'The moment it will end, we leave.', 'It ended.', 'Acabou.', 'the moment it **ends**.'),
           ('hurry', '🏃', 'apressar-se', 'Let us hurry.', 'Let us hurrying.', 'I hurried.', 'Apressei-me.', 'let us **hurry**.')],
    lines=[['Geppetto', 'When can we leave for school?', 'Quando podemos sair para a escola?'],
           ['Pinocchio', 'After I finish my lesson.', 'Depois que eu terminar a lição.'],
           ['Geppetto', 'Once you finish, tell me.', 'Assim que terminar, me avise.'],
           ['Pinocchio', 'The moment I finish, I will tell you.', 'No momento em que terminar, aviso.'],
           ['Geppetto', 'By the time we arrive, it will be dark.', 'Quando chegarmos, estará escuro.'],
           ['Pinocchio', 'Then let us hurry.', 'Então vamos depressa.'],
           ['Geppetto', 'Good idea. Take your book.', 'Boa ideia. Leve seu livro.'],
           ['Pinocchio', 'Done!', 'Pronto!']],
    quiz=[('When can they leave?', 'Quando podem sair?', [('✅', 'After the lesson'), ('🌙', 'At night'), ('☀️', 'At noon')], 0, 1, 'Pinocchio diz: “After I finish my lesson.”'),
          ('When will he tell Geppetto?', 'Quando ele vai avisar?', [('⚡', 'The moment he finishes'), ('🌅', 'Tomorrow'), ('📅', 'Next week')], 0, 3, 'Pinocchio diz: “The moment I finish.”'),
          ('What will it be by then?', 'Como estará quando chegarem?', [('🌙', 'Dark'), ('☀️', 'Sunny'), ('🌧️', 'Rainy')], 0, 4, 'Geppetto diz: “it will be dark.”')],
    fill=[['Did you pack your spelling book?', 'Você guardou seu abecedário?'], ['Yes, it is in my bag.', 'Sim, está na minha mochila.'],
          ['Then put on your coat. It is cold.', 'Então vista o casaco. Está frio.'], ['I will. See you after school.', 'Vou vestir. Até depois da escola.']])

OVR[82077] = dict(fill=[['Which job will robots do first?', 'Que trabalho os robôs farão primeiro?'], ['The boring ones, I think.', 'Os chatos, acho.'],
                        ['Then people will have more time.', 'Então as pessoas terão mais tempo.'], ['Let us hope you are right.', 'Vamos torcer para você ter razão.']])

# ---------------------------------------------------------------- 116–120
OVR[7082077] = dict(
    names=('Leia', 'Luke'), ids=['polly', 'tommy'], rs='hall',
    cv='Numa base rebelde, Leia e Luke discutem o futuro dos robôs.',
    obra=('I think robots will help us a lot.', 'Acho que robôs vão nos ajudar muito.'),
    vocab=[('🚀', 'starship', 'nave espacial', 'Soa como “STÁR-ship”.'), ('🤖', 'droid', 'andróide', 'Soa como “DRÓID”.'), ('⚔️', 'lightsaber', 'sabre de luz', 'Soa como “LÁIT-sêi-ber”.'),
           ('🌌', 'galaxy', 'galáxia', 'Soa como “GÉ-lak-si”.'), ('✊', 'rebel', 'rebelde', 'Soa como “RÉ-bel”.'), ('👑', 'empire', 'império', 'Soa como “ÉM-páir”.')],
    hot4=('🤖', 'droid', 'andróide', 'The droid is fast.', 'O andróide é rápido.'),
    lab=L('dr2', 'Laboratório de sons: think, droid e bet', 'th é língua entre os dentes; oi soa ói; e soa é.', 'Em droid, o oi soa ói.',
          [('think', 'THÍNK', 'achar', 'th = língua', 'sink', 'SÍNK'), ('droid', 'DRÓID', 'andróide', 'oi = ói', 'void', 'VÓID'), ('bet', 'BÉT', 'apostar', 'e = é', 'bit', 'BÍT')]),
    lines=[['Luke', 'What do you think about robots?', 'O que você acha dos robôs?'],
           ['Leia', 'I think robots will help us a lot.', 'Acho que robôs vão nos ajudar muito.'],
           ['Luke', 'Will they take over the galaxy?', 'Eles vão dominar a galáxia?'],
           ['Leia', 'I do not think they will take over.', 'Não acho que vão dominar tudo.'],
           ['Luke', 'I doubt our starship is safe.', 'Duvido que nossa nave seja segura.'],
           ['Leia', 'I bet new technology will improve it.', 'Aposto que a tecnologia nova vai melhorar isso.'],
           ['Luke', 'Maybe.', 'Talvez.'],
           ['Leia', 'We will see.', 'Veremos.']],
    quiz=[('What does she think robots will do?', 'O que ela acha que os robôs farão?', [('🤝', 'Help us'), ('😈', 'Take over'), ('😴', 'Sleep')], 0, 1, 'Leia diz: “robots will help us.”'),
          ('Does she think they will take over?', 'Ela acha que dominarão?', [('🙅', 'No'), ('✅', 'Yes'), ('🤷', 'Maybe')], 0, 3, 'Leia diz: “I do not think they will take over.”'),
          ('What does he doubt?', 'Do que ele duvida?', [('🚀', 'The starship is safe'), ('🤖', 'Robots exist'), ('☀️', 'The weather')], 0, 4, 'Luke diz: “I doubt our starship is safe.”')],
    fill=[['The droid found a message today.', 'O andróide achou uma mensagem hoje.'], ['Play it. I bet it is important.', 'Toque. Aposto que é importante.'],
          ['I think the rebels need us.', 'Acho que os rebeldes precisam de nós.'], ['Then we leave at dawn.', 'Então partimos ao amanhecer.']])

OVR[82078] = dict(fill=[['Shall I buy the tickets online?', 'Compro as passagens pela internet?'], ['Yes, two seats by the window.', 'Sim, dois lugares na janela.'],
                        ['I will send you the receipt.', 'Mando o recibo para você.'], ['Then we are all set.', 'Então está tudo certo.']])

OVR[7082078] = dict(
    names=('Ann', 'Joe'), ids=['polly', 'tom'], rs='street',
    cv='Numa praça de Roma, Ann e Joe trocam o plano de transporte.',
    obra=('The car is broken. Let us walk instead.', 'O carro quebrou. Vamos a pé.'),
    vocab=[('🛵', 'scooter', 'lambreta', 'Soa como “SKÚ-ter”.'), ('🗺️', 'map', 'mapa', 'Soa como “MÉP”.'), ('🏛️', 'square', 'praça', 'Soa como “SKUÉR”.'),
           ('🍦', 'ice cream', 'sorvete', 'Soa como “ÁIS KRÍM”.'), ('⛲', 'fountain', 'fonte', 'Soa como “FÁUN-ten”.'), ('🎟️', 'ticket', 'passagem', 'Soa como “TÍ-kit”.')],
    hot4=('🛵', 'scooter', 'lambreta', 'Let us take a scooter.', 'Vamos de lambreta.'),
    lines=[['Joe', 'The car is broken.', 'O carro quebrou.'],
           ['Ann', 'Let us walk instead of driving.', 'Vamos andar em vez de dirigir.'],
           ['Joe', 'It is far. What about the bus?', 'É longe. E que tal o ônibus?'],
           ['Ann', 'Fine. I would rather not wait long.', 'Tudo bem. Prefiro não esperar muito.'],
           ['Joe', 'Hurry, or else we miss it.', 'Depressa, senão perdemos.'],
           ['Ann', 'Is there an alternative?', 'Há uma alternativa?'],
           ['Joe', 'A taxi.', 'Um táxi.'],
           ['Ann', 'Or a scooter! Let us go.', 'Ou uma lambreta! Vamos.']],
    quiz=[('What do they do instead of driving?', 'O que fazem em vez de dirigir?', [('🚶', 'Walk'), ('✈️', 'Fly'), ('🚲', 'Cycle')], 0, 1, 'Ann diz: “walk instead of driving.”'),
          ('What does Joe suggest?', 'O que Joe sugere?', [('🚌', 'The bus'), ('🚆', 'The train'), ('🛵', 'A scooter')], 0, 2, 'Joe diz: “What about the bus?”'),
          ('What is the last idea?', 'Qual é a última ideia?', [('🛵', 'A scooter'), ('🚲', 'A bike'), ('🚕', 'A taxi')], 0, 7, 'Ann diz: “Or a scooter!”')],
    fill=[['Look! A scooter is free over there.', 'Olhe! Tem uma lambreta livre ali.'], ['Let us take it instead of the taxi.', 'Vamos nela em vez do táxi.'],
          ['I would rather ride than wait.', 'Prefiro andar a esperar.'], ['Hold on tight, or else you fall.', 'Segure firme, senão você cai.']])

OVR[82080] = dict(fill=[['Set the alarm for seven tomorrow.', 'Programe o despertador para as sete amanhã.'], ['I will. Breakfast is at eight.', 'Vou programar. O café é às oito.'],
                        ['Then I will pack the bags tonight.', 'Então arrumo as malas hoje à noite.'], ['Perfect. Sleep well.', 'Perfeito. Durma bem.']])

OVR[7082080] = dict(
    names=('Ferris', 'Cameron'), ids=['tommy', 'tom'], rs='kitchen',
    cv='Na cozinha, Ferris e Cameron combinam o dia de amanhã.',
    obra=('Will you call me later?', 'Você me liga mais tarde?'),
    vocab=[('🚘', 'convertible', 'conversível', 'Soa como “kon-VÉR-ti-bol”.'), ('🖼️', 'museum', 'museu', 'Soa como “miu-ZÍ-um”.'), ('🎺', 'parade', 'desfile', 'Soa como “pa-RÊID”.'),
           ('🚫', 'absent', 'ausente', 'Soa como “ÉB-sent”.'), ('🏫', 'principal', 'diretor', 'Soa como “PRÍN-si-pal”.'), ('🍽️', 'lunch', 'almoço', 'Soa como “LÂNTCH”.')],
    verbs=[('skip', '🏫', 'faltar', 'Will you skip school?', 'Will you skipping school?', 'I skipped.', 'Faltei.', 'will you **skip**?'),
           ('forget', '🧠', 'esquecer', 'I will not forget.', 'I will not to forget.', 'I forgot.', 'Esqueci.', 'will not + **forget**.'),
           ('help', '🤝', 'ajudar', 'Are you going to help?', 'Are you going to helping?', 'I helped.', 'Ajudei.', 'going to + **help**.'),
           ('say', '💬', 'dizer', 'She is not going to say no.', 'She is not going to saying no.', 'She said.', 'Ela disse.', 'going to + **say**.')],
    lines=[['Cameron', 'Will you call me later?', 'Você me liga mais tarde?'],
           ['Ferris', 'Yes. I will not forget.', 'Sim. Não vou esquecer.'],
           ['Cameron', 'Are you going to start the plan tomorrow morning?', 'Você vai começar o plano amanhã de manhã?'],
           ['Ferris', 'Yes. Are you going to help?', 'Sim. Você vai ajudar?'],
           ['Cameron', 'I am not going to be free.', 'Não vou estar livre.'],
           ['Ferris', 'Then Sloane will help.', 'Então a Sloane ajuda.'],
           ['Cameron', 'She is not going to say no.', 'Ela não vai dizer não.'],
           ['Ferris', 'Great. The principal will not notice.', 'Ótimo. O diretor não vai notar.']],
    quiz=[('What will he not do?', 'O que ele não vai fazer?', [('🧠', 'Forget'), ('📞', 'Call'), ('🏃', 'Run')], 0, 1, 'Ferris diz: “I will not forget.”'),
          ('When does the plan start?', 'Quando o plano começa?', [('🌅', 'Tomorrow morning'), ('🌙', 'Tonight'), ('📅', 'Next week')], 0, 2, 'Cameron diz: “tomorrow morning.”'),
          ('Who will help?', 'Quem vai ajudar?', [('👩', 'Sloane'), ('👧', 'The principal'), ('👨', 'Paul')], 0, 5, 'Ferris diz: “Then Sloane will help.”')],
    fill=[['Is the convertible ready for tomorrow?', 'O conversível está pronto para amanhã?'], ['It is not going to start without gas.', 'Ele não vai pegar sem gasolina.'],
          ['Then I will fill it up at dawn.', 'Então encho o tanque ao amanhecer.'], ['Fine. We will not be late for the parade.', 'Certo. Não vamos nos atrasar para o desfile.']])

# ---------------------------------------------------------------- 121–125
OVR[930017] = dict(fill=[['Let us go home and rest.', 'Vamos para casa descansar.'], ['I will make a pot of tea.', 'Faço um bule de chá.'],
                         ['Wake me up at noon.', 'Me acorde ao meio-dia.'], ['Deal. Sweet dreams.', 'Combinado. Bons sonhos.']])

OVR[7930017] = dict(
    names=('Rip', 'Dame'), ids=['tom', 'polly'], rs='bedroom',
    cv='Na vila, Rip e a esposa reclamam de uma manhã difícil.',
    obra=('I overslept and I feel drained.', 'Dormi demais e estou sem energia.'),
    vocab=[('⛰️', 'mountain', 'montanha', 'Soa como “MÁUN-ten”.'), ('🏘️', 'village', 'vila', 'Soa como “VÍ-lidj”.'), ('🌄', 'dawn', 'amanhecer', 'Soa como “DÓN”.'),
           ('🧔', 'beard', 'barba', 'Soa como “BÍRD”.'), ('😴', 'snore', 'roncar', 'Soa como “SNÓR”.'), ('💭', 'dream', 'sonho', 'Soa como “DRÍM”.')],
    hot4=('⛰️', 'mountain', 'montanha', 'I fell asleep on the mountain.', 'Adormeci na montanha.'),
    lines=[['Dame', 'You look rough this morning.', 'Você está péssimo hoje de manhã.'],
           ['Rip', 'I overslept and I feel drained.', 'Dormi demais e estou sem energia.'],
           ['Dame', 'I am sluggish too.', 'Eu também estou lenta.'],
           ['Rip', 'I am dead on my feet.', 'Estou morrendo em pé.'],
           ['Dame', 'The whole village is running on empty.', 'A vila inteira está no limite.'],
           ['Rip', 'Time for a siesta?', 'Hora de uma sesta?'],
           ['Dame', 'Coffee first.', 'Café primeiro.'],
           ['Rip', 'Deal.', 'Fechado.']],
    quiz=[('Why does he feel drained?', 'Por que ele está sem energia?', [('⏰', 'He overslept'), ('🏃', 'He ran'), ('🎬', 'He watched a film')], 0, 1, 'Rip diz: “I overslept.”'),
          ('How is the village?', 'Como está a vila?', [('⛽', 'Running on empty'), ('🤩', 'Full of energy'), ('😴', 'Asleep')], 0, 4, 'Dame diz: “running on empty.”'),
          ('What comes first?', 'O que vem primeiro?', [('☕', 'Coffee'), ('🌴', 'A siesta'), ('📋', 'Work')], 0, 6, 'Dame diz: “Coffee first.”')],
    fill=[['I will milk the cow after my nap.', 'Vou ordenhar a vaca depois da soneca.'], ['You always nap, Rip.', 'Você sempre tira soneca, Rip.'],
          ['The mountain air makes me sleepy.', 'O ar da montanha me dá sono.'], ['Then breathe a little less.', 'Então respire um pouco menos.']])

OVR[82081] = dict(fill=[['Write down the temperature every minute.', 'Anote a temperatura a cada minuto.'], ['It is rising slowly.', 'Ela está subindo devagar.'],
                        ['Then the ice will melt soon.', 'Então o gelo vai derreter logo.'], ['Let us record the time.', 'Vamos registrar a hora.']])

OVR[7082081] = dict(
    names=('Sam', 'Frodo'), ids=['sam', 'frodo'], rs='lake',
    cv='Num acampamento, Sam e Frodo trocam dicas para o frio.',
    obra=('If you feel cold, wear a coat.', 'Se sentir frio, vista um casaco.'),
    vocab=[('🧥', 'cloak', 'manto', 'Soa como “KLÔUK”.'), ('🔥', 'campfire', 'fogueira', 'Soa como “KÉMP-fáir”.'), ('🌨️', 'snow', 'neve', 'Soa como “SNÔU”.'),
           ('🧣', 'scarf', 'cachecol', 'Soa como “SKÁRF”.'), ('🍲', 'stew', 'ensopado', 'Soa como “STIÚ”.'), ('🛖', 'inn', 'estalagem', 'Soa como “ÍN”.')],
    hot4=('🧣', 'scarf', 'cachecol', 'Wear a scarf if it is windy.', 'Use um cachecol se ventar.'),
    lines=[['Frodo', 'It is freezing today.', 'Está congelante hoje.'],
           ['Sam', 'If you feel cold, wear a coat.', 'Se sentir frio, vista um casaco.'],
           ['Frodo', 'Whenever it rains, I feel cold.', 'Sempre que chove, sinto frio.'],
           ['Sam', 'If it is hot inside the inn, open the window.', 'Se estiver quente na estalagem, abra a janela.'],
           ['Frodo', 'Every time you cook, the camp gets hot.', 'Toda vez que você cozinha, o acampamento esquenta.'],
           ['Sam', 'Then I will boil the water outside.', 'Então ferverei a água lá fora.'],
           ['Frodo', 'Thank you, Sam.', 'Obrigado, Sam.'],
           ['Sam', 'Hobbits love a warm fire.', 'Hobbits adoram uma fogueira quente.']],
    quiz=[('What should you do if you feel cold?', 'O que fazer se sentir frio?', [('🧥', 'Wear a coat'), ('🪟', 'Open the window'), ('🏃', 'Run')], 0, 1, 'Sam diz: “If you feel cold, wear a coat.”'),
          ('What happens whenever it rains?', 'O que acontece sempre que chove?', [('🥶', 'He feels cold'), ('🤩', 'He feels happy'), ('😴', 'He sleeps')], 0, 2, 'Frodo diz: “Whenever it rains, I feel cold.”'),
          ('What should you do if it is hot inside?', 'O que fazer se estiver quente lá dentro?', [('🪟', 'Open the window'), ('🧥', 'Wear a coat'), ('🔥', 'Light a fire')], 0, 3, 'Sam diz: “open the window.”')],
    fill=[['The fire is almost out.', 'A fogueira está quase apagada.'], ['Then we add more wood.', 'Então colocamos mais lenha.'],
          ['If you are hungry, there is stew.', 'Se estiver com fome, tem ensopado.'], ['Thank you, Sam.', 'Obrigado, Sam.']])

OVR[82083] = dict(fill=[['Would you quit your job?', 'Você largaria o emprego?'], ['If I won, I would quit tomorrow.', 'Se eu ganhasse, largaria amanhã.'],
                        ['I would buy a house by the sea.', 'Eu compraria uma casa à beira-mar.'], ['Dreams are free, as you said.', 'Sonhar é de graça, como você disse.']])

# ---------------------------------------------------------------- 126–130
OVR[7082083] = dict(
    names=('Damiel', 'Marion'), ids=['tom', 'polly'], rs='park',
    cv='Num parque de Berlim, Damiel e Marion imaginam encontrar um anjo.',
    obra=('What would you do if you met an angel?', 'O que você faria se conhecesse um anjo?'),
    vocab=[('🪽', 'wings', 'asas', 'Soa como “UÍNGZ”.'), ('🏙️', 'city', 'cidade', 'Soa como “SÍ-ti”.'), ('🎪', 'circus', 'circo', 'Soa como “SÉR-kus”.'),
           ('🤸', 'trapeze', 'trapézio', 'Soa como “tra-PÍZ”.'), ('🧱', 'wall', 'muro', 'Soa como “UÓL”.'), ('🌤️', 'sky', 'céu', 'Soa como “SKÁI”.')],
    lab=L('wg2', 'Laboratório de sons: wings, angel e apologize', 'w soa u; a soa êi; g soa dj.', 'Em angel, o a soa êi.',
          [('wings', 'UÍNGZ', 'asas', 'w = u', 'wins', 'UÍNZ'), ('angel', 'ÊIN-djel', 'anjo', 'a = êi', 'angle', 'ÉNG-gol'), ('apologize', 'a-PÓ-lo-djáiz', 'pedir desculpas', 'g = dj', 'apology', 'a-PÓ-lo-dji')]),
    lines=[['Damiel', 'What would you do if you met an angel?', 'O que você faria se conhecesse um anjo?'],
           ['Marion', 'I would say thank you.', 'Eu diria obrigada.'],
           ['Damiel', 'Would you ask for money?', 'Você pediria dinheiro?'],
           ['Marion', 'No, I would not. I would ask for wisdom.', 'Não. Eu pediria sabedoria.'],
           ['Damiel', 'Would you apologize for your mistakes?', 'Você pediria desculpas pelos seus erros?'],
           ['Marion', 'Yes, I would apologize first.', 'Sim, pediria desculpas primeiro.'],
           ['Damiel', 'Wonderful answer.', 'Resposta maravilhosa.'],
           ['Marion', 'And you? Would you give up your wings?', 'E você? Abriria mão das suas asas?']],
    quiz=[('What would she say to the angel?', 'O que ela diria ao anjo?', [('🙏', 'Thank you'), ('🏃', 'Goodbye'), ('😡', 'Go away')], 0, 1, 'Marion diz: “I would say thank you.”'),
          ('Would she ask for money?', 'Ela pediria dinheiro?', [('🙅', 'No'), ('✅', 'Yes'), ('🤷', 'Maybe')], 0, 3, 'Marion diz: “No, I would not.”'),
          ('What would she do first?', 'O que ela faria primeiro?', [('🙏', 'Apologize'), ('🏃', 'Run'), ('😴', 'Sleep')], 0, 5, 'Marion diz: “I would apologize first.”')],
    fill=[['Would you stay in Berlin forever?', 'Você ficaria em Berlim para sempre?'], ['I would, if the circus stayed too.', 'Ficaria, se o circo também ficasse.'],
          ['Would you leave the trapeze behind?', 'Você deixaria o trapézio para trás?'], ['No, I would not. It is my sky.', 'Não. É o meu céu.']])

OVR[81163] = dict(fill=[['Is the dress ready for tonight?', 'O vestido está pronto para esta noite?'], ['Almost. I only need the shoes.', 'Quase. Só preciso dos sapatos.'],
                        ['Then try them on before dark.', 'Então experimente antes de escurecer.'], ['I will. Thank you for helping.', 'Vou experimentar. Obrigada por ajudar.']])

OVR[7081163] = dict(
    names=('Mia', 'Lilly'), ids=['matilda', 'polly'], rs='bedroom',
    cv='No quarto, Lilly e Mia sonham com o baile real.',
    obra=('If I were a princess, I could go to the ball.', 'Se eu fosse princesa, poderia ir ao baile.'),
    vocab=[('👑', 'crown', 'coroa', 'Soa como “KRÁUN”.'), ('🚘', 'limousine', 'limusine', 'Soa como “LÍ-mu-zín”.'), ('💇', 'makeover', 'transformação', 'Soa como “MÊIK-ô-ver”.'),
           ('🗄️', 'locker', 'armário', 'Soa como “LÓ-ker”.'), ('💃', 'waltz', 'valsa', 'Soa como “UÓLTS”.'), ('👵', 'grandmother', 'avó', 'Soa como “GRÉN-mâ-ther”.')],
    hot4=('👑', 'crown', 'coroa', 'I would wear a crown.', 'Eu usaria uma coroa.'),
    lines=[['Lilly', 'What do you dream about?', 'Com o que você sonha?'],
           ['Mia', 'If I were a princess, I could go to the ball.', 'Se eu fosse princesa, poderia ir ao baile.'],
           ['Lilly', 'What else?', 'O que mais?'],
           ['Mia', 'If I had magic, I might change my dress.', 'Se eu tivesse magia, talvez mudasse meu vestido.'],
           ['Lilly', 'And at the ball?', 'E no baile?'],
           ['Mia', 'I could dance all night.', 'Eu poderia dançar a noite toda.'],
           ['Lilly', 'You might meet a prince.', 'Você talvez conhecesse um príncipe.'],
           ['Mia', 'Maybe. I would settle for a waltz.', 'Talvez. Eu me contentaria com uma valsa.']],
    quiz=[('What would she be?', 'O que ela seria?', [('👸', 'A princess'), ('🧙', 'A witch'), ('👩‍🏫', 'A teacher')], 0, 1, 'Mia diz: “If I were a princess.”'),
          ('What might she change?', 'O que ela talvez mudasse?', [('👗', 'Her dress'), ('🏠', 'Her house'), ('🚗', 'Her car')], 0, 3, 'Mia diz: “I might change my dress.”'),
          ('What could she do at the ball?', 'O que ela poderia fazer no baile?', [('💃', 'Dance all night'), ('😴', 'Sleep'), ('🍕', 'Eat pizza')], 0, 5, 'Mia diz: “I could dance all night.”')],
    fill=[['Do you have your crown yet?', 'Você já tem sua coroa?'], ['Not yet. My grandmother has it.', 'Ainda não. Minha avó está com ela.'],
          ['Then the waltz can start.', 'Então a valsa pode começar.'], ['Wait for me. I need my shoes.', 'Espere por mim. Preciso dos sapatos.']])

OVR[930018] = dict(fill=[['Did the form arrive by mail?', 'O formulário chegou pelo correio?'], ['Yes, the postmark is from Friday.', 'Sim, o carimbo é de sexta.'],
                         ['Then the application is in time.', 'Então a inscrição está no prazo.'], ['I will file it today.', 'Vou arquivar hoje.']])

OVR[7930018] = dict(
    names=('Raymond', 'Charlie'), ids=['tom', 'tommy'], rs='street',
    cv='Num posto de gasolina, Raymond e Charlie conversam sobre a viagem.',
    obra=('To fill up the tank. I do it on Fridays.', 'Encher o tanque. Faço isso às sextas.'),
    vocab=[('🛣️', 'highway', 'rodovia', 'Soa como “HÁI-uêi”.'), ('⛽', 'gas station', 'posto de gasolina', 'Soa como “GÉS STÊI-shon”.'), ('🧳', 'suitcase', 'mala', 'Soa como “SÚT-kêis”.'),
           ('🃏', 'cards', 'cartas', 'Soa como “KÁRDZ”.'), ('🧭', 'journey', 'jornada', 'Soa como “DJÉR-ni”.'), ('🧾', 'receipt', 'recibo', 'Soa como “ri-SÍT”.')],
    hot4=('🛣️', 'highway', 'rodovia', 'The highway is empty.', 'A rodovia está vazia.'),
    verbs=[('drive', '🚗', 'dirigir', 'I drive on Fridays.', 'I driving on Fridays.', 'I drove.', 'Dirigi.', 'drive → **drove**.'),
           ('tell', '📰', 'contar', 'Tell me about the trip.', 'Tell me of the trip.', 'He told me.', 'Ele me contou.', 'tell me **about**.'),
           ('spend', '⏳', 'passar', 'We spend the time with games.', 'We spend the time to games.', 'We spent it.', 'Passamos.', 'spend **+ tempo**.'),
           ('check', '🔍', 'conferir', 'Check the tank first.', 'Check to the tank first.', 'I checked.', 'Conferi.', 'check **+ objeto**.')],
    lines=[['Charlie', 'Where are you going?', 'Aonde você vai?'],
           ['Raymond', 'To fill up the tank. I do it on Fridays.', 'Encher o tanque. Faço isso às sextas.'],
           ['Charlie', 'Fill me in on the trip.', 'Me ponha a par da viagem.'],
           ['Raymond', 'Well, you should fill in the gaps yourself.', 'Bem, você deve preencher as lacunas sozinho.'],
           ['Charlie', 'What did you do on the way?', 'O que você fez no caminho?'],
           ['Raymond', 'We filled the time with games.', 'Passamos o tempo com jogos.'],
           ['Charlie', 'Which game did you like most?', 'De qual jogo você mais gostou?'],
           ['Raymond', 'Cards. I always win.', 'Cartas. Eu sempre ganho.']],
    quiz=[('When does he fill up the tank?', 'Quando ele enche o tanque?', [('📅', 'On Fridays'), ('🌙', 'At night'), ('☀️', 'Every day')], 0, 1, 'Raymond diz: “I do it on Fridays.”'),
          ('What does Charlie want?', 'O que Charlie quer?', [('📰', 'To be filled in on the trip'), ('🚗', 'To drive'), ('🍕', 'To cook')], 0, 2, 'Charlie diz: “Fill me in on the trip.”'),
          ('How did they fill the time?', 'Como passaram o tempo?', [('🎲', 'With games'), ('📚', 'With books'), ('😴', 'Sleeping')], 0, 5, 'Raymond diz: “with games.”')],
    fill=[['We need to buy snacks for the road.', 'Precisamos comprar lanches para a estrada.'], ['Get peanuts and a bottle of water.', 'Pegue amendoim e uma garrafa de água.'],
          ['I will keep the receipt.', 'Eu guardo o recibo.'], ['Of course. You always do.', 'Claro. Você sempre guarda.']])

# ---------------------------------------------------------------- 131–135
OVR[82085] = dict(fill=[['Do you still keep those old photos?', 'Você ainda guarda aquelas fotos antigas?'], ['Yes, in a box under the bed.', 'Sim, numa caixa debaixo da cama.'],
                        ['Let us look at them tonight.', 'Vamos olhar hoje à noite.'], ['I will make some tea.', 'Eu faço um chá.']])

OVR[7082085] = dict(
    names=('Rick', 'Ilsa'), ids=['tom', 'polly'], rs='cafe2',
    cv='No café de Rick, Rick e Ilsa falam do que teriam feito se fossem diferentes.',
    obra=('If I were braver, I would have told her.', 'Se eu fosse mais corajoso, teria contado a ela.'),
    vocab=[('🍸', 'café', 'café (casa)', 'Soa como “ka-FÊI”.'), ('🎹', 'piano', 'piano', 'Soa como “pi-É-nou”.'), ('🛫', 'airport', 'aeroporto', 'Soa como “ÉR-pórt”.'),
           ('🌫️', 'fog', 'neblina', 'Soa como “FÓG”.'), ('🎫', 'visa', 'visto', 'Soa como “VÍ-za”.'), ('🛂', 'passport', 'passaporte', 'Soa como “PÉS-pórt”.')],
    hot4=('🛫', 'airport', 'aeroporto', 'We would have met at the airport.', 'Teríamos nos encontrado no aeroporto.'),
    verbs=[('tell', '🗣️', 'contar', 'I would have told her.', 'I would have tell her.', 'I told her.', 'Contei.', 'would have + **told**.'),
           ('help', '🩺', 'ajudar', 'He would have helped.', 'He would have help.', 'He helped.', 'Ele ajudou.', 'would have + **helped**.'),
           ('buy', '🛍️', 'comprar', 'I would have bought it.', 'I would have buy it.', 'I bought it.', 'Comprei.', 'would have + **bought**.'),
           ('leave', '✈️', 'partir', 'I would have left.', 'I would have leave.', 'I left.', 'Parti.', 'would have + **left**.')],
    lines=[['Ilsa', 'Why did you not tell her the truth?', 'Por que você não contou a verdade a ela?'],
           ['Rick', 'If I were braver, I would have told her.', 'Se eu fosse mais corajoso, teria contado a ela.'],
           ['Ilsa', 'Sam was hurt in the fall.', 'O Sam se machucou na queda.'],
           ['Rick', 'If I were a doctor, I would have helped.', 'Se eu fosse médico, teria ajudado.'],
           ['Ilsa', 'Did you buy that watch?', 'Você comprou aquele relógio?'],
           ['Rick', 'If I were rich, I would have bought it.', 'Se eu fosse rico, teria comprado.'],
           ['Ilsa', 'You are in trouble then.', 'Então você está em apuros.'],
           ['Rick', 'And if I were free, I would have left.', 'E se eu fosse livre, teria partido.']],
    quiz=[('Why did he not tell her?', 'Por que ele não contou a ela?', [('🦁', 'He was not brave'), ('😴', 'He forgot'), ('🏃', 'He ran')], 0, 1, 'Rick diz: “If I were braver.”'),
          ('What would he have done as a doctor?', 'O que ele teria feito como médico?', [('🩺', 'Helped'), ('🏃', 'Left'), ('🍕', 'Eaten')], 0, 3, 'Rick diz: “I would have helped.”'),
          ('Why did he not buy the watch?', 'Por que ele não comprou o relógio?', [('💰', 'He is not rich'), ('⌚', 'It was broken'), ('😴', 'He slept')], 0, 5, 'Rick diz: “If I were rich.”')],
    fill=[['The last plane leaves at dawn.', 'O último avião sai ao amanhecer.'], ['Then there is no time to lose.', 'Então não há tempo a perder.'],
          ['Take the passport and the visa.', 'Pegue o passaporte e o visto.'], ['Goodbye, Rick. I will remember.', 'Adeus, Rick. Vou lembrar.']])

OVR[82086] = dict(fill=[['Can you hear the water under the dock?', 'Você ouve a água embaixo do cais?'], ['Yes. It sounds like singing.', 'Sim. Parece uma canção.'],
                        ['I wish I could stay here all night.', 'Queria poder ficar aqui a noite toda.'], ['Come back tomorrow, then.', 'Volte amanhã, então.']])

OVR[7082086] = dict(
    names=('Marge', 'Homer'), ids=['polly', 'tom'], rs='kitchen',
    cv='Na cozinha, Marge e Homer desejam que as coisas mudem.',
    obra=('I wish you would help.', 'Queria que você ajudasse.'),
    vocab=[('🍩', 'donut', 'rosquinha', 'Soa como “DÔU-nat”.'), ('🛋️', 'couch', 'sofá', 'Soa como “KÁUTCH”.'), ('📺', 'cartoon', 'desenho animado', 'Soa como “kar-TÚN”.'),
           ('🛹', 'skateboard', 'skate', 'Soa como “SKÊIT-bórd”.'), ('🏘️', 'neighbour', 'vizinho', 'Soa como “NÊI-ber”.'), ('🔊', 'noise', 'barulho', 'Soa como “NÓIZ”.')],
    hot4=('🛋️', 'couch', 'sofá', 'I wish you would leave the couch.', 'Queria que você saísse do sofá.'),
    fill=[['Where did you leave the car keys?', 'Onde você deixou as chaves do carro?'], ['On the couch, next to the donuts.', 'No sofá, ao lado das rosquinhas.'],
          ['I wish you would put them on the hook.', 'Queria que você as pendurasse no gancho.'], ['I will, starting tomorrow.', 'Eu penduro, a partir de amanhã.']])

OVR[82087] = dict(fill=[['Maria sent a letter last week.', 'Maria mandou uma carta semana passada.'], ['What did she write?', 'O que ela escreveu?'],
                        ['She asked why I stayed silent.', 'Perguntou por que fiquei em silêncio.'], ['Then answer her now.', 'Então responda agora.']])

# ---------------------------------------------------------------- 136–140
OVR[7082087] = dict(
    names=('Romeo', 'Benvolio'), ids=['tom', 'tommy'], rs='street',
    cv='Em Verona, Romeo e Benvolio lamentam uma briga.',
    obra=('I wish I had not said that.', 'Queria não ter dito aquilo.'),
    vocab=[('🎭', 'feud', 'rixa entre famílias', 'Soa como “FIÚD”.'), ('🏛️', 'balcony', 'sacada', 'Soa como “BÉL-ko-ni”.'), ('⚔️', 'duel', 'duelo', 'Soa como “DIÚ-el”.'),
           ('🍽️', 'feast', 'banquete', 'Soa como “FÍST”.'), ('🎭', 'mask', 'máscara', 'Soa como “MÁSK”.'), ('🧑', 'cousin', 'primo', 'Soa como “KÂ-zin”.')],
    hot4=('⚔️', 'duel', 'duelo', 'I wish I had not joined the duel.', 'Queria não ter entrado no duelo.'),
    verbs=[('say', '🤐', 'dizer', 'I wish I had not said that.', 'I wish I had not say that.', 'I said it.', 'Eu disse.', 'had not + **said**.'),
           ('shout', '📢', 'gritar', 'I should not have shouted.', 'I should not have shout.', 'I shouted.', 'Gritei.', 'should not have + **shouted**.'),
           ('argue', '🗣️', 'discutir', 'You argued with him.', 'You argued him.', 'I argued.', 'Discuti.', 'argue **with**.'),
           ('feel', '💔', 'sentir', 'How did he feel?', 'How did he felt?', 'He felt sad.', 'Ele se sentiu triste.', 'did + **feel**.')],
    lines=[['Benvolio', 'You argued with Tybalt yesterday.', 'Você discutiu com Teobaldo ontem.'],
           ['Romeo', 'I wish I had not said that.', 'Queria não ter dito aquilo.'],
           ['Benvolio', 'You shouted at him.', 'Você gritou com ele.'],
           ['Romeo', 'I should not have shouted.', 'Eu não devia ter gritado.'],
           ['Benvolio', 'You left the feast early.', 'Você saiu cedo do banquete.'],
           ['Romeo', 'I would have liked to stay.', 'Eu gostaria de ter ficado.'],
           ['Benvolio', 'Talk to him.', 'Fale com ele.'],
           ['Romeo', 'If only I had known how he felt.', 'Se ao menos eu soubesse como ele se sentia.']],
    quiz=[('What does he wish he had not done?', 'O que ele queria não ter feito?', [('🤐', 'Said that'), ('🏃', 'Ran'), ('🍕', 'Eaten')], 0, 1, 'Romeo diz: “I wish I had not said that.”'),
          ('What should he not have done?', 'O que ele não devia ter feito?', [('📢', 'Shouted'), ('🏠', 'Stayed'), ('📞', 'Called')], 0, 3, 'Romeo diz: “I should not have shouted.”'),
          ('What would he have liked to do?', 'O que ele gostaria de ter feito?', [('🏠', 'Stay at the feast'), ('✈️', 'Travel'), ('😴', 'Sleep')], 0, 5, 'Romeo diz: “I would have liked to stay.”')],
    fill=[['Tybalt will not forgive me now.', 'Teobaldo não vai me perdoar agora.'], ['Then ask for peace before dark.', 'Então peça paz antes de escurecer.'],
          ['I will go to the old church tonight.', 'Vou à igreja velha esta noite.'], ['Take a friend with you.', 'Leve um amigo com você.']])

OVR[930019] = dict(fill=[['Would you like another coffee?', 'Aceita outro café?'], ['Yes, and a slice of cake.', 'Sim, e uma fatia de bolo.'],
                         ['Then I will order for both of us.', 'Então peço para nós dois.'], ['What a lovely afternoon.', 'Que tarde agradável.']])

OVR[7930019] = dict(
    names=('Rita', 'Phil'), ids=['polly', 'tom'], rs='office',
    cv='Na redação, Rita e Phil acertam um mal-entendido sobre a data.',
    obra=('No, actually, it is on Tuesday.', 'Não, na verdade é na terça.'),
    vocab=[('📅', 'calendar', 'calendário', 'Soa como “KÁ-len-dar”.'), ('🐿️', 'groundhog', 'marmota', 'Soa como “GRÁUND-hóg”.'), ('⏰', 'alarm clock', 'despertador', 'Soa como “a-LÁRM KLÓK”.'),
           ('🌨️', 'blizzard', 'nevasca', 'Soa como “BLÍ-zerd”.'), ('🌦️', 'weatherman', 'meteorologista', 'Soa como “UÉ-ther-mén”.'), ('🔁', 'repeat', 'repetir', 'Soa como “ri-PÍT”.')],
    hot4=('📅', 'calendar', 'calendário', 'Check the calendar.', 'Veja o calendário.'),
    lab=L('tu2', 'Laboratório de sons: Tuesday, meant e frankly', 'ue soa iu; ea soa é; a soa é.', 'Em meant, o ea soa é.',
          [('Tuesday', 'TIÚZ-dei', 'terça-feira', 'ue = iu', 'chooses', 'TCHÚ-ziz'), ('meant', 'MÉNT', 'quis dizer', 'ea = é', 'meat', 'MÍT'), ('frankly', 'FRÉNK-li', 'francamente', 'a = é', 'freely', 'FRÍ-li')]),
    lines=[['Phil', 'The meeting is on Monday, right?', 'A reunião é na segunda, certo?'],
           ['Rita', 'No, actually, it is on Tuesday.', 'Não, na verdade é na terça.'],
           ['Phil', 'I thought Wednesday.', 'Pensei que fosse quarta.'],
           ['Rita', 'I mean Tuesday, at ten.', 'Quer dizer, terça às dez.'],
           ['Phil', 'That was my assumption, sorry.', 'Era minha suposição, desculpe.'],
           ['Rita', 'What I meant was, check the email.', 'O que eu quis dizer foi: veja o e-mail.'],
           ['Phil', 'Frankly, I never read it.', 'Francamente, nunca leio.'],
           ['Rita', 'Then write the date on your hand.', 'Então escreva a data na mão.']],
    fill=[['Set your alarm for seven o clock.', 'Programe o despertador para as sete.'], ['I always set it, but it rings again.', 'Eu sempre programo, mas ele toca de novo.'],
          ['Then write the date on your hand.', 'Então escreva a data na mão.'], ['Tuesday, ten. Got it.', 'Terça, dez horas. Entendi.']])

OVR[82089] = dict(fill=[['Do you have the money yet?', 'Você já tem o dinheiro?'], ['Not all of it, unless the mayor helps.', 'Não todo, a menos que o prefeito ajude.'],
                        ['Then ask him today, otherwise it is too late.', 'Então peça a ele hoje, senão é tarde.'], ['I will go right away.', 'Vou agora mesmo.']])

OVR[7082089] = dict(
    names=('Mary', 'Bert'), ids=['polly', 'tom'], rs='park',
    cv='Num parque de Londres, Mary e Bert conferem as regras do passeio.',
    obra=('Unless you hurry, you miss the bus.', 'A menos que você se apresse, perde o ônibus.'),
    vocab=[('🪁', 'kite', 'pipa', 'Soa como “KÁIT”.'), ('🌬️', 'wind', 'vento', 'Soa como “UÍND”.'), ('🏠', 'rooftop', 'telhado', 'Soa como “RÚF-top”.'),
           ('🎠', 'carousel', 'carrossel', 'Soa como “ká-ro-SÉL”.'), ('🥄', 'spoonful', 'colherada', 'Soa como “SPÚN-ful”.'), ('👜', 'carpetbag', 'mala de tapete', 'Soa como “KÁR-pit-bég”.')],
    hot4=('🪁', 'kite', 'pipa', 'We fly the kite unless it rains.', 'Soltamos a pipa a menos que chova.'),
    verbs=[('fly', '🪁', 'soltar (pipa)', 'We fly the kite.', 'We flying the kite.', 'We flew it.', 'Soltamos.', 'we **fly**.'),
           ('miss', '🚌', 'perder', 'You miss the bus.', 'You missing the bus.', 'I missed it.', 'Perdi.', 'you **miss**.'),
           ('clear', '🌤️', 'abrir (o tempo)', 'It clears at noon.', 'It clearing at noon.', 'It cleared.', 'Abriu.', 'it **clears**.'),
           ('bring', '🧺', 'trazer', 'Bring some snacks.', 'Bring to some snacks.', 'I brought some.', 'Trouxe.', 'bring → **brought**.')],
    lines=[['Bert', 'The bus leaves soon.', 'O ônibus sai logo.'],
           ['Mary', 'Unless you hurry, you miss it.', 'A menos que você se apresse, perde.'],
           ['Bert', 'You mean, if I do not hurry?', 'Quer dizer, se eu não me apressar?'],
           ['Mary', 'Exactly. Same meaning.', 'Exato. Mesmo sentido.'],
           ['Bert', 'And the kite day?', 'E o dia da pipa?'],
           ['Mary', 'We stay unless it clears.', 'Ficamos a menos que o tempo abra.'],
           ['Bert', 'Provided that you bring snacks, I come.', 'Desde que você traga lanches, eu vou.'],
           ['Mary', 'Deal. And bring the kite.', 'Fechado. E traga a pipa.']],
    quiz=[('What happens unless he hurries?', 'O que acontece se ele não se apressar?', [('🚌', 'He misses the bus'), ('🍕', 'He eats'), ('😴', 'He sleeps')], 0, 1, 'Mary diz: “Unless you hurry, you miss it.”'),
          ('Are the two sentences the same?', 'As duas frases são iguais?', [('✅', 'Yes, same meaning'), ('❌', 'No'), ('🤷', 'Maybe')], 0, 3, 'Mary diz: “Same meaning.”'),
          ('What must she bring?', 'O que ela deve trazer?', [('🍪', 'Snacks'), ('☂️', 'An umbrella'), ('📚', 'Books')], 0, 6, 'Bert diz: “Provided that you bring snacks.”')],
    fill=[['Bring a kite and a warm scarf.', 'Traga uma pipa e um cachecol.'], ['Unless the wind drops, we will fly it.', 'A menos que o vento diminua, vamos soltá-la.'],
          ['Provided that you hold the string tight.', 'Desde que você segure bem o fio.'], ['Agreed. Meet me at four.', 'Combinado. Encontre-me às quatro.']])
