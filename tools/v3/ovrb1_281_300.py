# Reescrita dos episódios B1 281–300 (ver ovrb1.py e ovrb1_251_262.py).
from v3.ovrb1 import OVR, L
from v3.ovrb1_251_262 import C, F, W, WORKS

# ---------------------------------------------------------------- 281 / 282
F(82180, [['I came across an old letter yesterday.', 'Encontrei uma carta antiga ontem.'], ['Can you come up with a better idea?', 'Você consegue ter uma ideia melhor?'],
          ['I came down with a cold this week.', 'Peguei um resfriado esta semana.'], ['Come back when you feel better.', 'Volte quando estiver melhor.']])

W(7082180, 'The Lion King', '🎬 Filme · 1994', 'O Rei Leão é uma animação da Disney de 1994: o filhote Simba cresce longe de casa e depois volta à savana para assumir seu lugar.', ['🦁', '🌅', '🪨'], 'jungle')
C(7082180, ('Simba', 'Nala'), ['simba', 'polly'], 'yard', 'Na savana, Nala chama Simba para sair do esconderijo e acompanhar o grupo.',
  ('🪨', 'rock', 'rocha', 'Come out from behind the rock.', 'Saia de trás da rocha.'),
  [('🦁', 'mane', 'juba', 'Soa como “MÊIN”.'), ('🌅', 'savanna', 'savana', 'Soa como “sa-VÉ-na”.'), ('🦓', 'herd', 'manada', 'Soa como “HÉRD”.'),
   ('💧', 'waterhole', 'poço de água', 'Soa como “UÓ-ter-hôul”.'), ('📣', 'roar', 'rugido', 'Soa como “RÓR”.'), ('🐗', 'warthog', 'javali africano', 'Soa como “UÓRT-hóg”.')],
  [('roar', '🦁', 'rugir', 'The lion roars.', 'The lion roar.', 'He roared.', 'Ele rugiu.', 'he/she **roars**.'),
   ('follow', '👣', 'seguir', 'Follow me.', 'Follow to me.', 'I followed.', 'Segui.', 'follow **+ objeto**.'),
   ('return', '🔙', 'voltar', 'I return home.', 'I return to home.', 'I returned.', 'Voltei.', 'return **+ lugar**.'),
   ('learn', '🎓', 'aprender', 'Learn from the past.', 'Learn of the past.', 'I learned.', 'Aprendi.', 'learn **from**.')],
  [['Nala', 'Simba, come out from behind that rock.', 'Simba, saia de trás daquela rocha.'], ['Simba', 'Come over here, Nala. The view is great.', 'Venha aqui, Nala. A vista é ótima.'],
   ['Nala', 'Come along, the others are waiting at the waterhole.', 'Venha junto, os outros esperam no poço de água.'], ['Simba', 'Will they come round to my idea?', 'Será que eles vão mudar de ideia sobre o meu plano?'],
   ['Nala', 'They will come round when they see you.', 'Vão mudar de ideia quando virem você.'], ['Simba', 'The sun comes out after the rain, right?', 'O sol aparece depois da chuva, certo?'],
   ['Nala', 'Yes. Come over for dinner tonight.', 'Sim. Venha jantar esta noite.'], ['Simba', 'I will come along, but a little late.', 'Eu vou, mas um pouco tarde.']],
  [('Where must Simba come out from?', 'De onde Simba deve sair?', [('🪨', 'Behind a rock'), ('🌳', 'Under a tree'), ('🏠', 'Inside a house')], 0, 0, 'Nala diz: “come out from behind that rock.”'),
   ('Where are the others waiting?', 'Onde os outros esperam?', [('💧', 'At the waterhole'), ('🏔️', 'On a mountain'), ('🌊', 'At sea')], 0, 2, 'Nala diz: “waiting at the waterhole.”'),
   ('When will they come round?', 'Quando vão mudar de ideia?', [('👀', 'When they see Simba'), ('🌙', 'Tomorrow'), ('🍖', 'After lunch')], 0, 4, 'Nala diz: “when they see you.”')],
  L('lk', 'Laboratório de sons: mane, herd e roar', 'a soa êi; er soa é; oa soa ó.', 'Em mane, o a soa êi.',
    [('mane', 'MÊIN', 'juba', 'a = êi', 'men', 'MÉN'), ('herd', 'HÉRD', 'manada', 'er = é', 'hard', 'HÁRD'), ('roar', 'RÓR', 'rugido', 'oa = ó', 'rare', 'RÉR')]),
  [['Why does Simba hide from the pride?', 'Por que Simba se esconde do bando?'], ['He thinks the past is his fault.', 'Ele acha que o passado é culpa dele.'],
   ['Then he needs a friend to listen.', 'Então ele precisa de uma amiga para ouvir.'], ['I am here, and I am not leaving.', 'Estou aqui e não vou embora.']])

# ---------------------------------------------------------------- 283 / 284
F(82181, [['Go on, tell me the whole story.', 'Continue, conte a história toda.'], ['I went through a very hard year.', 'Passei por um ano muito difícil.'],
          ['Let us go over the plan once more.', 'Vamos rever o plano mais uma vez.'], ['Tonight we go out and celebrate.', 'Hoje à noite saímos para comemorar.']])

W(7082181, 'Frozen', '🎬 Filme · 2013', 'Frozen é uma animação da Disney de 2013: a rainha Elsa tem o poder de criar gelo e neve, e sua irmã Anna tenta se aproximar dela.', ['❄️', '🏰', '🧤'], 'castle')
C(7082181, ('Elsa', 'Anna'), ['elsa', 'polly'], 'bedroom', 'No quarto do castelo, Anna bate à porta e Elsa pede um pouco de silêncio.',
  ('🧤', 'gloves', 'luvas', 'Go down with your gloves.', 'Desça com as suas luvas.'),
  [('⏰', 'alarm', 'alarme', 'Soa como “a-LARM”.'), ('❄️', 'snowflake', 'floco de neve', 'Soa como “SNÔU-fleik”.'), ('🏰', 'castle', 'castelo', 'Soa como “KÁ-sol”.'),
   ('🧊', 'ice', 'gelo', 'Soa como “ÁIS”.'), ('🌡️', 'temperature', 'temperatura', 'Soa como “TÉM-pra-tcher”.'), ('🪟', 'window', 'janela', 'Soa como “UÍN-dôu”.')],
  [('freeze', '🥶', 'congelar', 'The lake freezes.', 'The lake freeze.', 'It froze.', 'Congelou.', 'freeze → **froze**.'),
   ('melt', '🫠', 'derreter', 'Ice melts in spring.', 'Ice melt in spring.', 'It melted.', 'Derreteu.', 'he/she/it **melts**.'),
   ('ring', '🔔', 'tocar', 'The alarm rings.', 'The alarm ring.', 'It rang.', 'Tocou.', 'ring → **rang**.'),
   ('knock', '🚪', 'bater', 'Knock on the door.', 'Knock at to the door.', 'I knocked.', 'Bati.', 'knock **on**.')],
  [['Anna', 'Elsa, the alarm went off an hour ago.', 'Elsa, o alarme tocou há uma hora.'], ['Elsa', 'Go away, Anna. I need to think.', 'Vá embora, Anna. Preciso pensar.'],
   ['Anna', 'The temperature goes down every night here.', 'A temperatura cai toda noite aqui.'], ['Elsa', 'Then the ice goes up the windows.', 'Então o gelo sobe pelas janelas.'],
   ['Anna', 'Do not go away from me. Let us go down to the hall.', 'Não se afaste de mim. Vamos descer ao salão.'], ['Elsa', 'I will go down, but my gloves stay on.', 'Eu desço, mas as luvas ficam.'],
   ['Anna', 'Prices go up in winter, and so does my worry.', 'Os preços sobem no inverno, e minha preocupação também.'], ['Elsa', 'Then do not let the alarm go off again.', 'Então não deixe o alarme tocar de novo.']],
  [('What went off an hour ago?', 'O que tocou há uma hora?', [('⏰', 'The alarm'), ('🔔', 'The church bell'), ('📞', 'The phone')], 0, 0, 'Anna diz: “the alarm went off an hour ago.”'),
   ('What goes down every night?', 'O que cai toda noite?', [('🌡️', 'The temperature'), ('🌙', 'The moon'), ('🚪', 'The door')], 0, 2, 'Anna diz: “The temperature goes down every night.”'),
   ('What stays on?', 'O que fica?', [('🧤', 'Elsa’s gloves'), ('👑', 'The crown'), ('🧣', 'The scarf')], 0, 5, 'Elsa diz: “my gloves stay on.”')],
  L('fz', 'Laboratório de sons: alarm, ice e window', 'a soa a; i soa ái; w soa u.', 'Em ice, o i soa ái.',
    [('alarm', 'a-LARM', 'alarme', 'a = a', 'alarming', 'a-LAR-min'), ('ice', 'ÁIS', 'gelo', 'i = ái', 'is', 'ÍZ'), ('window', 'UÍN-dôu', 'janela', 'w = u', 'wind', 'UÍND')]),
  [['Does the ice melt when Elsa is calm?', 'O gelo derrete quando Elsa está calma?'], ['A little, if she breathes slowly.', 'Um pouco, se ela respirar devagar.'],
   ['Then Anna should wait quietly outside.', 'Então Anna deve esperar do lado de fora, em silêncio.'], ['She will. She always does in the end.', 'Vai esperar. Sempre espera no fim.']])

# ---------------------------------------------------------------- 285 / 286
F(930040, [['Hit me up when you are free tonight.', 'Me chama quando estiver livre hoje à noite.'], ['Text me the address, okay?', 'Me manda o endereço por mensagem, ok?'],
           ['Chill, the party is legit.', 'Relaxa, a festa é de verdade.'], ['Cool, I add you to the group chat.', 'Beleza, te coloco no grupo.']])

W(7930040, 'Clueless', '🎬 Filme · 1995', 'As Patricinhas de Beverly Hills (Clueless) é uma comédia de 1995, escrita e dirigida por Amy Heckerling, sobre uma estudante popular que tenta ajudar os amigos.', ['📱', '👗', '💬'], 'toyshop')
C(7930040, ('Cher', 'Dionne'), ['polly', 'misshoney'], 'school', 'No corredor da escola, Cher e Dionne trocam mensagens curtas pelo celular.',
  ('🙂', 'emoji', 'emoji', 'Send an emoji, not a long text.', 'Mande um emoji, não um texto longo.'),
  [('📱', 'phone', 'celular', 'Soa como “FÔUN”.'), ('💌', 'message', 'mensagem', 'Soa como “MÉ-sidj”.'), ('🔌', 'charger', 'carregador', 'Soa como “TCHAR-djer”.'),
   ('😂', 'laugh', 'rir', 'Soa como “LÉF”.'), ('🛜', 'wifi', 'wi-fi', 'Soa como “UÁI-fai”.'), ('😳', 'shy', 'tímido', 'Soa como “SHÁI”.')],
  [('answer', '📞', 'atender', 'Answer the call.', 'Answer to the call.', 'I answered.', 'Atendi.', 'answer **+ objeto**.'),
   ('type', '⌨️', 'digitar', 'Type a short reply.', 'Type to short reply.', 'I typed.', 'Digitei.', 'type **+ objeto**.'),
   ('laugh', '😂', 'rir', 'I laugh at the joke.', 'I laugh the joke.', 'I laughed.', 'Ri.', 'laugh **at**.'),
   ('send', '📤', 'enviar', 'Send me a message.', 'Send to me a message.', 'I sent it.', 'Enviei.', 'send → **sent**.')],
  [['Cher', 'omg, did you see Josh’s message?', 'omg, você viu a mensagem do Josh?'], ['Dionne', 'idk, my phone died. brb, I am charging it.', 'sei lá, meu celular morreu. já volto, estou carregando.'],
   ['Cher', 'lol, you always say brb and disappear.', 'rs, você sempre diz já volto e some.'], ['Dionne', 'I am back. What did he say?', 'Voltei. O que ele disse?'],
   ['Cher', 'He wrote ttyl. Talk to you later!', 'Ele escreveu falo com você depois. Até mais!'], ['Dionne', 'lol, that means he is busy.', 'rs, isso quer dizer que ele está ocupado.'],
   ['Cher', 'idk, maybe he is shy. omg, he is calling!', 'sei lá, talvez ele seja tímido. omg, ele está ligando!'], ['Dionne', 'Answer it! ttyl, Cher!', 'Atenda! Até mais, Cher!']],
  [('What does brb mean here?', 'O que brb significa aqui?', [('🔙', 'I will be right back'), ('😂', 'I laugh'), ('🔌', 'Battery died')], 0, 1, 'Dionne diz: “brb, I am charging it.”'),
   ('What did Josh write?', 'O que Josh escreveu?', [('👋', 'ttyl'), ('❤️', 'I love you'), ('🍕', 'Pizza?')], 0, 4, 'Cher diz: “He wrote ttyl.”'),
   ('What does Dionne tell Cher to do?', 'O que Dionne manda Cher fazer?', [('📞', 'Answer the call'), ('📵', 'Ignore it'), ('🔌', 'Charge it')], 0, 7, 'Dionne diz: “Answer it!”')],
  L('cl', 'Laboratório de sons: phone, laugh e shy', 'o soa ôu; augh soa éf; y soa ái.', 'Em laugh, o augh soa éf.',
    [('phone', 'FÔUN', 'celular', 'o = ôu', 'fan', 'FÉN'), ('laugh', 'LÉF', 'rir', 'augh = éf', 'leaf', 'LÍF'), ('shy', 'SHÁI', 'tímido', 'y = ái', 'she', 'SHÍ')]),
  [['Did Josh reply to your last message?', 'O Josh respondeu à sua última mensagem?'], ['Only with a thumbs up, nothing else.', 'Só com um joinha, mais nada.'],
   ['Then call him instead of typing.', 'Então ligue para ele em vez de digitar.'], ['Maybe tomorrow, when I feel brave.', 'Talvez amanhã, quando eu me sentir corajosa.']])

# ---------------------------------------------------------------- 287 / 288
F(82184, [['My car broke down this morning.', 'Meu carro quebrou hoje de manhã.'], ['They broke up after the summer.', 'Eles terminaram depois do verão.'],
          ['Someone broke into the old house.', 'Alguém invadiu a casa velha.'], ['A fire broke out near the hill.', 'Um incêndio começou perto do morro.']])

W(7082184, 'Chicken Run', '🎬 Filme · 2000', 'A Fuga das Galinhas (Chicken Run) é uma animação em massinha de 2000, dos estúdios Aardman: galinhas de uma fazenda planejam escapar antes que virem torta.', ['🐔', '🥚', '🚜'], 'bakery')
C(7082184, ('Ginger', 'Rocky'), ['polly', 'tom'], 'yard', 'No galinheiro, Ginger e Rocky planejam a fuga.',
  ('🔗', 'wire', 'arame', 'Break through the wire.', 'Atravesse o arame.'),
  [('🐔', 'chicken', 'galinha', 'Soa como “TCHÍ-kin”.'), ('🥚', 'egg', 'ovo', 'Soa como “ÉG”.'), ('🚜', 'farmer', 'fazendeiro', 'Soa como “FAR-mer”.'),
   ('🏚️', 'coop', 'galinheiro', 'Soa como “KÚP”.'), ('🛫', 'plane', 'avião', 'Soa como “PLÊIN”.'), ('🕳️', 'tunnel', 'túnel', 'Soa como “TÂ-nol”.')],
  [('escape', '🏃', 'fugir', 'We escape at night.', 'We escape in night.', 'We escaped.', 'Fugimos.', 'escape **at night**.'),
   ('build', '🔨', 'construir', 'We build a plane.', 'We builds a plane.', 'We built it.', 'Construímos.', 'build → **built**.'),
   ('flap', '🪽', 'bater as asas', 'I flap my wings.', 'I flap my wing.', 'I flapped.', 'Bati as asas.', 'plural: **wings**.'),
   ('hatch', '🐣', 'chocar', 'The egg hatches.', 'The egg hatch.', 'It hatched.', 'Chocou.', 'he/she/it **hatches**.')],
  [['Ginger', 'We must break free from this farm.', 'Precisamos nos libertar desta fazenda.'], ['Rocky', 'Break through the wire at night.', 'Atravesse o arame à noite.'],
   ['Ginger', 'I tried to break away last week.', 'Tentei fugir semana passada.'], ['Rocky', 'A piece of the fence broke off in my wing.', 'Um pedaço da cerca se soltou na minha asa.'],
   ['Ginger', 'Then we break through there, by the coop.', 'Então atravessamos ali, perto do galinheiro.'], ['Rocky', 'Do not break away from the group.', 'Não se afaste do grupo.'],
   ['Ginger', 'We break off the talk when the farmer comes.', 'Interrompemos a conversa quando o fazendeiro chega.'], ['Rocky', 'Tonight we break free, I promise.', 'Esta noite nos libertamos, eu prometo.']],
  [('What do they want to break free from?', 'De que querem se libertar?', [('🚜', 'The farm'), ('🏫', 'School'), ('🏙️', 'The city')], 0, 0, 'Ginger diz: “break free from this farm.”'),
   ('Where do they break through?', 'Por onde atravessam?', [('🏚️', 'By the coop'), ('🌊', 'By the sea'), ('🌲', 'In the forest')], 0, 4, 'Ginger diz: “break through there, by the coop.”'),
   ('When do they break free?', 'Quando se libertam?', [('🌙', 'Tonight'), ('☀️', 'In summer'), ('📅', 'Next year')], 0, 7, 'Rocky diz: “Tonight we break free.”')],
  L('cr', 'Laboratório de sons: chicken, tunnel e farmer', 'ch soa tch; u soa â; ar soa ar.', 'Em chicken, o ch soa tch.',
    [('chicken', 'TCHÍ-kin', 'galinha', 'ch = tch', 'kitchen', 'KÍ-tchin'), ('tunnel', 'TÂ-nol', 'túnel', 'u = â', 'tennis', 'TÉ-nis'), ('farmer', 'FAR-mer', 'fazendeiro', 'ar = ar', 'former', 'FÓR-mer')]),
  [['How many hens know about the plan?', 'Quantas galinhas sabem do plano?'], ['Only the ones in the red coop.', 'Só as do galinheiro vermelho.'],
   ['Then tell them to stay quiet.', 'Então diga a elas para ficarem quietas.'], ['They are the quietest hens on the farm.', 'São as galinhas mais quietas da fazenda.']])

# ---------------------------------------------------------------- 289 / 290
F(82186, [['She brought up three children alone.', 'Ela criou três filhos sozinha.'], ['Bring back the book by Friday.', 'Devolva o livro até sexta.'],
          ['Bad weather brought about the delay.', 'O mau tempo causou o atraso.'], ['The new shop brings in good money.', 'A loja nova rende bom dinheiro.']])

W(7082186, 'Downton Abbey', '📺 Série · 2010', 'Downton Abbey é uma série britânica de 2010, ambientada numa mansão no interior da Inglaterra do início do século XX, com a família nobre e seus criados.', ['🏰', '🫖', '🤵'], 'castle')
C(7082186, ('Mary', 'Carson'), ['mary', 'tom'], 'hall', 'No saguão da mansão, Lady Mary dá ordens ao mordomo Carson para o jantar.',
  ('🍵', 'tray', 'bandeja', 'Bring down the tray.', 'Traga a bandeja lá embaixo.'),
  [('🫖', 'teapot', 'bule', 'Soa como “TÍ-pót”.'), ('🏰', 'manor', 'mansão', 'Soa como “MÉ-ner”.'), ('🤵', 'butler', 'mordomo', 'Soa como “BÂT-ler”.'),
   ('📋', 'guest list', 'lista de convidados', 'Soa como “GÉST LÍST”.'), ('🍽️', 'dinner', 'jantar', 'Soa como “DÍ-ner”.'), ('🛞', 'carriage', 'carruagem', 'Soa como “KÉ-ridj”.')],
  [('arrange', '🗂️', 'organizar', 'Arrange the table.', 'Arrange to the table.', 'I arranged it.', 'Organizei.', 'arrange **+ objeto**.'),
   ('welcome', '🤝', 'receber', 'Welcome the guests.', 'Welcome to the guests.', 'I welcomed them.', 'Recebi.', 'welcome **+ objeto**.'),
   ('polish', '✨', 'polir', 'Polish the silver.', 'Polish to the silver.', 'I polished it.', 'Poli.', 'polish **+ objeto**.'),
   ('announce', '📣', 'anunciar', 'Announce the dinner.', 'Announce to dinner.', 'I announced it.', 'Anunciei.', 'announce **+ objeto**.')],
  [['Mary', 'Carson, bring down the tea tray, please.', 'Carson, traga a bandeja de chá, por favor.'], ['Carson', 'Bring it down myself? Very well, my lady.', 'Trazer eu mesmo? Muito bem, milady.'],
   ['Mary', 'Bring over the guest list as well.', 'Traga também a lista de convidados.'], ['Carson', 'Shall I bring round the carriage now?', 'Devo trazer a carruagem agora?'],
   ['Mary', 'Yes. And bring forward the dinner to seven.', 'Sim. E antecipe o jantar para as sete.'], ['Carson', 'Bringing forward dinner will upset the cook.', 'Antecipar o jantar vai chatear a cozinheira.'],
   ['Mary', 'Then bring her round to the idea gently.', 'Então convença-a com jeito.'], ['Carson', 'I shall bring her over a cup of tea.', 'Levarei a ela uma xícara de chá.']],
  [('What does Mary ask Carson to bring down?', 'O que Mary pede que Carson traga?', [('🍵', 'The tea tray'), ('📚', 'A book'), ('🧥', 'A coat')], 0, 0, 'Mary diz: “bring down the tea tray.”'),
   ('What is brought forward?', 'O que é antecipado?', [('🍽️', 'The dinner'), ('🚗', 'The carriage'), ('🎵', 'The music')], 0, 4, 'Mary diz: “bring forward the dinner to seven.”'),
   ('Who must be brought round to the idea?', 'Quem deve ser convencido?', [('👩‍🍳', 'The cook'), ('🤵', 'Carson'), ('👑', 'The queen')], 0, 6, 'Mary diz: “bring her round to the idea.”')],
  L('da', 'Laboratório de sons: butler, manor e carriage', 'u soa â; a soa é; ia soa i.', 'Em butler, o u soa â.',
    [('butler', 'BÂT-ler', 'mordomo', 'u = â', 'battle', 'BÉ-tol'), ('manor', 'MÉ-ner', 'mansão', 'a = é', 'minor', 'MÁI-ner'), ('carriage', 'KÉ-ridj', 'carruagem', 'a = é', 'courage', 'KÂ-ridj')]),
  [['Will the guests arrive before dinner?', 'Os convidados chegam antes do jantar?'], ['Most will, if the roads are dry.', 'A maioria chega, se as estradas estiverem secas.'],
   ['Then the house must look perfect.', 'Então a casa precisa estar perfeita.'], ['It will, my lady. Leave it to us.', 'Estará, milady. Deixe conosco.']])

# ---------------------------------------------------------------- 291 / 292
F(930041, [['You stand out in that bright jacket.', 'Você se destaca nessa jaqueta colorida.'], ['I always stand up for my friends.', 'Sempre defendo meus amigos.'],
           ['I will stand by you, whatever happens.', 'Vou apoiar você, aconteça o que acontecer.'], ['What does this logo stand for?', 'O que esse logotipo significa?']])

W(7930041, 'Spartacus', '🎬 Filme · 1960', 'Spartacus é um filme de 1960, dirigido por Stanley Kubrick: um gladiador escravizado lidera uma revolta contra Roma.', ['⚔️', '🛡️', '🏛️'], 'castle')
C(7930041, ('Spartacus', 'Varinia'), ['tom', 'polly'], 'hall', 'No acampamento dos rebeldes, Spartacus e Varinia combinam quem fala e quem espera.',
  ('🚩', 'banner', 'estandarte', 'Stand up under the banner.', 'Levante-se sob o estandarte.'),
  [('⚔️', 'sword', 'espada', 'Soa como “SÓRD”.'), ('🏟️', 'arena', 'arena', 'Soa como “a-RÍ-na”.'), ('⛓️', 'chain', 'corrente', 'Soa como “TCHÊIN”.'),
   ('🛡️', 'shield', 'escudo', 'Soa como “SHÍLD”.'), ('🏛️', 'Rome', 'Roma', 'Soa como “RÔUM”.'), ('✊', 'rebel', 'rebelde', 'Soa como “RÉ-bol”.')],
  [('fight', '🥊', 'lutar', 'We fight for freedom.', 'We fight to freedom.', 'We fought.', 'Lutamos.', 'fight → **fought**.'),
   ('refuse', '🙅', 'recusar', 'They refuse to obey.', 'They refuse obey.', 'They refused.', 'Recusaram.', 'refuse **to**.'),
   ('lead', '🧭', 'liderar', 'He leads the men.', 'He lead the men.', 'He led them.', 'Ele os liderou.', 'lead → **led**.'),
   ('shout', '📢', 'gritar', 'They shout together.', 'They shout together to.', 'They shouted.', 'Gritaram.', 'shout **+ advérbio**.')],
  [['Varinia', 'Spartacus, stand up and speak to the men.', 'Spartacus, levante-se e fale aos homens.'], ['Spartacus', 'I will stand in for the old leader today.', 'Hoje eu substituo o antigo líder.'],
   ['Varinia', 'Then stand aside when the guards come.', 'Então dê passagem quando os guardas vierem.'], ['Spartacus', 'We do not stand down for the guards.', 'Nós não recuamos diante dos guardas.'],
   ['Varinia', 'Will the others stand up with you?', 'Os outros vão se levantar com você?'], ['Spartacus', 'One by one, they stand up and say it.', 'Um a um, eles se levantam e dizem.'],
   ['Varinia', 'And if the guard says stand down?', 'E se o guarda mandar recuar?'], ['Spartacus', 'We stand aside, then stand up again.', 'Damos passagem, depois nos levantamos de novo.']],
  [('What does Varinia ask Spartacus to do?', 'O que Varinia pede a Spartacus?', [('🗣️', 'Stand up and speak'), ('😴', 'Sleep'), ('🏃', 'Run away')], 0, 0, 'Varinia diz: “stand up and speak to the men.”'),
   ('Who does Spartacus stand in for?', 'Quem Spartacus substitui?', [('👴', 'The old leader'), ('👮', 'The guard'), ('👸', 'The queen')], 0, 1, 'Spartacus diz: “stand in for the old leader.”'),
   ('Who do they not stand down for?', 'Diante de quem não recuam?', [('💂', 'The guards'), ('👨‍👩‍👧', 'Their families'), ('🐴', 'The horses')], 0, 3, 'Spartacus diz: “We do not stand down for the guards.”')],
  L('sp', 'Laboratório de sons: sword, chain e shield', 'w mudo; ch soa tch; ie soa í.', 'Em sword, o w é mudo.',
    [('sword', 'SÓRD', 'espada', 'w mudo', 'sort', 'SÓRT'), ('chain', 'TCHÊIN', 'corrente', 'ch = tch', 'chin', 'TCHÍN'), ('shield', 'SHÍLD', 'escudo', 'ie = í', 'should', 'SHÚD')]),
  [['Do the men trust Spartacus as their leader?', 'Os homens confiam em Spartacus como líder?'], ['They do, because he asks for nothing.', 'Confiam, porque ele não pede nada.'],
   ['Then Rome will have a hard winter.', 'Então Roma terá um inverno difícil.'], ['Let us hope the winter is short.', 'Esperemos que o inverno seja curto.']])

# ---------------------------------------------------------------- 293 / 294
F(82191, [['My brother is a real night owl.', 'Meu irmão é uma verdadeira coruja noturna.'], ['Mum is busy as a bee today.', 'Mamãe está ocupadíssima hoje.'],
          ['I take a cat nap after lunch.', 'Tiro um cochilo depois do almoço.'], ['Nobody calls him the black sheep now.', 'Ninguém o chama de ovelha negra agora.']])

W(7082191, 'The Jungle Book', '📚 Livro · 1894', 'O Livro da Selva é um conjunto de contos de Rudyard Kipling, publicado em 1894, sobre o menino Mowgli, criado na selva por lobos, com o urso Baloo e a pantera Bagheera.', ['🌴', '🐻', '🐅'], 'jungle')
C(7082191, ('Mowgli', 'Baloo'), ['tommy', 'bear'], 'park', 'Na selva, Mowgli e Baloo guardam o segredo do mel e fogem do tigre.',
  ('🪵', 'log', 'tronco', 'Sit on the log and hold your horses.', 'Sente no tronco e calma aí.'),
  [('🌴', 'jungle', 'selva', 'Soa como “DJÂN-gol”.'), ('🍯', 'honey', 'mel', 'Soa como “HÂ-ni”.'), ('🐆', 'panther', 'pantera', 'Soa como “PÉN-ther”.'),
   ('🐅', 'tiger', 'tigre', 'Soa como “TÁI-ger”.'), ('🐍', 'snake', 'cobra', 'Soa como “SNÊIK”.'), ('🍌', 'banana', 'banana', 'Soa como “ba-NÉ-na”.')],
  [('swing', '🐒', 'balançar', 'We swing from the vine.', 'We swing of the vine.', 'We swung.', 'Balançamos.', 'swing → **swung**.'),
   ('growl', '🐯', 'rosnar', 'The tiger growls.', 'The tiger growl.', 'It growled.', 'Rosnou.', 'he/she/it **growls**.'),
   ('whisper', '🤫', 'sussurrar', 'Whisper to me.', 'Whisper me.', 'I whispered.', 'Sussurrei.', 'whisper **to**.'),
   ('sneak', '🥷', 'esgueirar-se', 'Sneak past the tiger.', 'Sneak the tiger past.', 'I sneaked past.', 'Passei de fininho.', 'sneak **past**.')],
  [['Mowgli', 'Baloo, do not let the cat out of the bag.', 'Baloo, não deixe escapar o segredo.'], ['Baloo', 'Hold your horses, Mowgli. What bag?', 'Calma aí, Mowgli. Que segredo?'],
   ['Mowgli', 'The secret about the honey tree.', 'O segredo da árvore do mel.'], ['Baloo', 'The tiger wants the lion’s share of the jungle.', 'O tigre quer a maior parte da selva.'],
   ['Mowgli', 'Looking for him is a wild goose chase.', 'Procurar por ele é uma busca inútil.'], ['Baloo', 'Hold your horses; I have a plan.', 'Calma aí; tenho um plano.'],
   ['Mowgli', 'A plan? Or another wild goose chase?', 'Um plano? Ou outra busca inútil?'], ['Baloo', 'Trust me. The cat is still in the bag.', 'Confie em mim. O segredo continua guardado.']],
  [('What must Baloo not let out of the bag?', 'O que Baloo não deve deixar escapar?', [('🤫', 'The secret'), ('🐱', 'A real cat'), ('🍌', 'The bananas')], 0, 0, 'Mowgli diz: “do not let the cat out of the bag.”'),
   ('What does the tiger want?', 'O que o tigre quer?', [('🌴', 'The lion’s share of the jungle'), ('🍯', 'Only honey'), ('🏠', 'A house')], 0, 3, 'Baloo diz: “the lion’s share of the jungle.”'),
   ('What does Mowgli call looking for the tiger?', 'Como Mowgli chama procurar o tigre?', [('🪿', 'A wild goose chase'), ('🎮', 'A game'), ('🎉', 'A party')], 0, 4, 'Mowgli diz: “a wild goose chase.”')],
  L('jb', 'Laboratório de sons: jungle, tiger e panther', 'j soa dj; i soa ái; a soa é.', 'Em tiger, o i soa ái.',
    [('jungle', 'DJÂN-gol', 'selva', 'j = dj', 'jingle', 'DJÍN-gol'), ('tiger', 'TÁI-ger', 'tigre', 'i = ái', 'tigger', 'TÍ-ger'), ('panther', 'PÉN-ther', 'pantera', 'a = é', 'pencil', 'PÉN-sol')]),
  [['Where does Bagheera sleep at night?', 'Onde Bagheera dorme à noite?'], ['High in the trees, away from the tiger.', 'No alto das árvores, longe do tigre.'],
   ['Then we meet him there at dawn.', 'Então o encontramos lá ao amanhecer.'], ['Agreed. Bring a banana for the road.', 'Combinado. Leve uma banana para o caminho.']])

# ---------------------------------------------------------------- 295 / 296
F(82192, [['I have been feeling blue lately.', 'Tenho me sentido triste ultimamente.'], ['She was green with envy at the news.', 'Ela ficou verde de inveja com a notícia.'],
          ['We meet once in a blue moon.', 'Nos vemos uma vez na vida, outra na morte.'], ['Red tape slows every request here.', 'A burocracia atrasa todo pedido aqui.']])

W(7082192, 'The Great Gatsby', '📚 Livro · 1925', 'O Grande Gatsby é um romance de F. Scott Fitzgerald, publicado em 1925: o milionário Gatsby dá festas enormes e olha todas as noites para uma luz verde do outro lado da baía.', ['💚', '🥂', '🏰'], 'lighthouse')
C(7082192, ('Gatsby', 'Daisy'), ['tom', 'polly'], 'lake', 'À beira da baía, Gatsby mostra a Daisy a luz verde que ele olha toda noite.',
  ('🎷', 'jazz', 'jazz', 'Give the green light to the jazz.', 'Dê sinal verde ao jazz.'),
  [('🏰', 'mansion', 'mansão', 'Soa como “MÉN-shon”.'), ('🌉', 'bay', 'baía', 'Soa como “BÊI”.'), ('🥂', 'toast', 'brinde', 'Soa como “TÔUST”.'),
   ('🎉', 'party', 'festa', 'Soa como “PAR-ti”.'), ('🎩', 'gentleman', 'cavalheiro', 'Soa como “DJÉN-tol-men”.'), ('✨', 'glow', 'brilho', 'Soa como “GLÔU”.')],
  [('invite', '💌', 'convidar', 'I invite you.', 'I invite to you.', 'I invited you.', 'Convidei você.', 'invite **+ objeto**.'),
   ('glance', '👀', 'olhar de relance', 'She glances at him.', 'She glance at him.', 'She glanced.', 'Ela olhou.', 'he/she **glances**.'),
   ('hope', '🤞', 'esperar', 'I hope to see you.', 'I hope see you.', 'I hoped.', 'Esperei.', 'hope **to**.'),
   ('dance', '💃', 'dançar', 'They dance all night.', 'They dances all night.', 'They danced.', 'Dançaram.', 'plural: **dance**.')],
  [['Gatsby', 'Every night I look at the green light across the bay.', 'Toda noite olho a luz verde do outro lado da baía.'], ['Daisy', 'Why the green light?', 'Por que a luz verde?'],
   ['Gatsby', 'To me, a green light means go ahead.', 'Para mim, luz verde significa pode seguir.'], ['Daisy', 'Then I give you the green light.', 'Então eu lhe dou sinal verde.'],
   ['Gatsby', 'Do you see red when I mention Tom?', 'Você fica furiosa quando menciono o Tom?'], ['Daisy', 'Sometimes. He came home out of the blue last week.', 'Às vezes. Ele chegou em casa do nada semana passada.'],
   ['Gatsby', 'The butler was caught red-handed with my best bottle.', 'O mordomo foi pego com a mão na massa com a minha melhor garrafa.'], ['Daisy', 'Then give the green light to the party anyway.', 'Então dê sinal verde à festa mesmo assim.']],
  [('What does Gatsby look at every night?', 'O que Gatsby olha toda noite?', [('💚', 'A green light'), ('🌕', 'The moon'), ('🚢', 'A ship')], 0, 0, 'Gatsby diz: “I look at the green light.”'),
   ('What does a green light mean to him?', 'O que significa luz verde para ele?', [('➡️', 'Go ahead'), ('✋', 'Stop'), ('😴', 'Sleep')], 0, 2, 'Gatsby diz: “a green light means go ahead.”'),
   ('Who was caught red-handed?', 'Quem foi pego com a mão na massa?', [('🤵', 'The butler'), ('👑', 'The king'), ('🧒', 'A child')], 0, 6, 'Gatsby diz: “The butler was caught red-handed.”')],
  L('gg', 'Laboratório de sons: mansion, bay e gentleman', 'a soa é; ay soa êi; g soa dj.', 'Em bay, o ay soa êi.',
    [('mansion', 'MÉN-shon', 'mansão', 'a = é', 'mission', 'MÍ-shon'), ('bay', 'BÊI', 'baía', 'ay = êi', 'buy', 'BÁI'), ('gentleman', 'DJÉN-tol-men', 'cavalheiro', 'g = dj', 'general', 'DJÉ-ne-ral')]),
  [['Does Daisy come to the party tonight?', 'Daisy vem à festa esta noite?'], ['She says she may, if the night is warm.', 'Ela diz que talvez, se a noite estiver quente.'],
   ['Then tell the band to start early.', 'Então diga à banda para começar cedo.'], ['The jazz will be heard across the bay.', 'O jazz será ouvido do outro lado da baía.']])

# ---------------------------------------------------------------- 297 / 298
F(930042, [['Just bite the bullet and sign it.', 'Engula o choro e assine.'], ['You made the mistake, so face the music.', 'Você errou, então encare as consequências.'],
           ['I am tired, but I soldier on.', 'Estou cansado, mas sigo em frente.'], ['That is the spirit, champion.', 'Esse é o espírito, campeão.']])

W(7930042, 'The Old Man and the Sea', '📚 Livro · 1952', 'O Velho e o Mar é uma novela de Ernest Hemingway, publicada em 1952: um velho pescador cubano enfrenta sozinho um enorme peixe no mar, e o menino Manolin o admira.', ['🎣', '🐟', '⛵'], 'lighthouse')
C(7930042, ('Santiago', 'Manolin'), ['tom', 'tommy'], 'pier', 'No cais, Manolin tenta animar o velho Santiago depois de muitos dias sem pescar.',
  ('🪢', 'line', 'linha de pesca', 'Hold the line and go the distance.', 'Segure a linha e vá até o fim.'),
  [('🐟', 'marlin', 'marlim', 'Soa como “MAR-lin”.'), ('🎣', 'hook', 'anzol', 'Soa como “HÚK”.'), ('⛵', 'skiff', 'barquinho', 'Soa como “SKÍF”.'),
   ('🦈', 'shark', 'tubarão', 'Soa como “SHÁRK”.'), ('🌊', 'current', 'correnteza', 'Soa como “KÂ-rent”.'), ('⚓', 'harbor', 'porto', 'Soa como “HAR-ber”.')],
  [('row', '🚣', 'remar', 'I row at dawn.', 'I rows at dawn.', 'I rowed.', 'Remei.', 'I/we/they **row**.'),
   ('struggle', '💪', 'lutar', 'I struggle with the line.', 'I struggle the line.', 'I struggled.', 'Lutei.', 'struggle **with**.'),
   ('catch', '🎣', 'pegar', 'I catch a fish.', 'I catches a fish.', 'I caught it.', 'Peguei.', 'catch → **caught**.'),
   ('drift', '🌊', 'ir à deriva', 'The boat drifts.', 'The boat drift.', 'It drifted.', 'Foi à deriva.', 'he/she/it **drifts**.')],
  [['Manolin', 'Santiago, you have caught nothing for many days.', 'Santiago, você não pesca nada há muitos dias.'], ['Santiago', 'A fisherman learns to roll with the punches.', 'Um pescador aprende a lidar com os golpes.'],
   ['Manolin', 'Will you throw in the towel now?', 'Você vai jogar a toalha agora?'], ['Santiago', 'Never. I go the distance, boy.', 'Nunca. Eu vou até o fim, garoto.'],
   ['Manolin', 'With your back against the wall, will you go alone?', 'Com as costas na parede, você vai sozinho?'], ['Santiago', 'Yes. I roll with the punches and try again.', 'Vou. Aguento os golpes e tento de novo.'],
   ['Manolin', 'Do not throw in the towel because of one bad week.', 'Não jogue a toalha por causa de uma semana ruim.'], ['Santiago', 'I will not. I go the distance.', 'Não vou. Vou até o fim.']],
  [('How long has Santiago caught nothing?', 'Há quanto tempo Santiago não pesca nada?', [('📅', 'For many days'), ('⏰', 'For one hour'), ('🌙', 'One night')], 0, 0, 'Manolin diz: “caught nothing for many days.”'),
   ('Will Santiago throw in the towel?', 'Santiago vai jogar a toalha?', [('🙅', 'No, never'), ('🙆', 'Yes, today'), ('🤷', 'Maybe')], 0, 3, 'Santiago diz: “Never. I go the distance.”'),
   ('Does he go alone?', 'Ele vai sozinho?', [('🚣', 'Yes'), ('👥', 'With a crew'), ('🐕', 'With a dog')], 0, 5, 'Santiago diz: “Yes. I roll with the punches.”')],
  L('os', 'Laboratório de sons: marlin, shark e harbor', 'ar soa ar; sh soa x; h soa r aspirado.', 'Em shark, o sh soa x.',
    [('marlin', 'MAR-lin', 'marlim', 'ar = ar', 'martin', 'MAR-tin'), ('shark', 'SHÁRK', 'tubarão', 'sh = x', 'sharp', 'SHÁRP'), ('harbor', 'HAR-ber', 'porto', 'h aspirado', 'arbor', 'AR-ber')]),
  [['Will the boy go out with him tomorrow?', 'O menino vai sair com ele amanhã?'], ['His parents say no, for now.', 'Os pais dele dizem que não, por enquanto.'],
   ['Then he helps from the shore instead.', 'Então ele ajuda da margem.'], ['That is how a good friend helps.', 'É assim que um bom amigo ajuda.']])

# ---------------------------------------------------------------- 299 / 300
F(82193, [['Time flies when we talk like this.', 'O tempo voa quando conversamos assim.'], ['It is about time you called me.', 'Já era hora de você me ligar.'],
          ['Better late than never, my friend.', 'Antes tarde do que nunca, meu amigo.'], ['I will finish this in no time.', 'Termino isso num instante.']])

W(7082193, 'Alice’s Adventures in Wonderland', '📚 Livro · 1865', 'Alice no País das Maravilhas é um livro de Lewis Carroll, publicado em 1865: Alice persegue um coelho apressado e cai num mundo de coisas estranhas.', ['🐇', '⌚', '🕳️'], 'library')
C(7082193, ('White Rabbit', 'Alice'), ['whiterabbit', 'alice'], 'park', 'No jardim, o Coelho Branco corre atrasado e Alice tenta acompanhar.',
  ('⌚', 'watch', 'relógio de bolso', 'Check your watch from time to time.', 'Olhe o relógio de bolso de vez em quando.'),
  [('🕳️', 'hole', 'buraco', 'Soa como “HÔUL”.'), ('🫖', 'teacup', 'xícara', 'Soa como “TÍ-kâp”.'), ('👑', 'queen', 'rainha', 'Soa como “KUÍN”.'),
   ('🃏', 'card', 'carta', 'Soa como “KÁRD”.'), ('🍄', 'mushroom', 'cogumelo', 'Soa como “MÂSH-rum”.'), ('🧥', 'waistcoat', 'colete', 'Soa como “UÊIS-kôut”.')],
  [('hurry', '🏃', 'apressar-se', 'I hurry to the garden.', 'I hurry at the garden.', 'I hurried.', 'Apressei-me.', 'hurry **to**.'),
   ('fall', '🕳️', 'cair', 'Alice falls down the hole.', 'Alice fall down the hole.', 'She fell.', 'Ela caiu.', 'fall → **fell**.'),
   ('shrink', '🔬', 'encolher', 'I shrink in the room.', 'I shrinks in the room.', 'I shrank.', 'Encolhi.', 'shrink → **shrank**.'),
   ('wonder', '🤔', 'imaginar', 'I wonder where it goes.', 'I wonder where does it go.', 'I wondered.', 'Imaginei.', 'wonder **+ frase**.')],
  [['White Rabbit', 'I am late! I am behind schedule!', 'Estou atrasado! Estou fora do cronograma!'], ['Alice', 'Behind schedule for what?', 'Fora do cronograma para quê?'],
   ['White Rabbit', 'The Queen’s party. I should arrive ahead of time.', 'A festa da Rainha. Eu devia chegar com antecedência.'], ['Alice', 'Then why do you stop to kill time?', 'Então por que você para para matar tempo?'],
   ['White Rabbit', 'I do not kill time. I check my watch from time to time.', 'Não mato tempo. Olho meu relógio de vez em quando.'], ['Alice', 'Your watch looks very busy.', 'Seu relógio parece muito ocupado.'],
   ['White Rabbit', 'We finish ahead of time if you run with me.', 'Terminamos antes do prazo se você correr comigo.'], ['Alice', 'Fine, but I still have time to kill.', 'Tudo bem, mas ainda tenho tempo de sobra.']],
  [('Why is the Rabbit worried?', 'Por que o Coelho está preocupado?', [('⏰', 'He is behind schedule'), ('🍰', 'He is hungry'), ('🌧️', 'It is raining')], 0, 0, 'White Rabbit diz: “I am behind schedule!”'),
   ('What does he check from time to time?', 'O que ele olha de vez em quando?', [('⌚', 'His watch'), ('📖', 'A book'), ('🗺️', 'A map')], 0, 4, 'White Rabbit diz: “I check my watch from time to time.”'),
   ('Whose party is it?', 'De quem é a festa?', [('👑', 'The Queen’s'), ('🐱', 'The Cat’s'), ('🎩', 'The Hatter’s')], 0, 2, 'White Rabbit diz: “The Queen’s party.”')],
  L('aw', 'Laboratório de sons: rabbit, queen e mushroom', 'a soa é; qu soa ku; u soa â.', 'Em queen, o qu soa ku.',
    [('rabbit', 'RÉ-bit', 'coelho', 'a = é', 'robot', 'RÔU-bót'), ('queen', 'KUÍN', 'rainha', 'qu = ku', 'clean', 'KLÍN'), ('mushroom', 'MÂSH-rum', 'cogumelo', 'u = â', 'mission', 'MÍ-shon')]),
  [['Does Alice follow the Rabbit down the hole?', 'Alice segue o Coelho buraco abaixo?'], ['She does, and she lands very softly.', 'Segue, e cai bem de leve.'],
   ['Then the real adventure begins now.', 'Então a aventura de verdade começa agora.'], ['And nobody here keeps good time.', 'E ninguém aqui marca bem as horas.']])
