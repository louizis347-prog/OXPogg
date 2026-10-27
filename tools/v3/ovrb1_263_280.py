# Reescrita dos episódios B1 263–280 (ver ovrb1.py e ovrb1_251_262.py).
from v3.ovrb1 import OVR, L
from v3.ovrb1_251_262 import C, F, W, WORKS


# ---------------------------------------------------------------- 263 / 264
F(82170, [['I start writing at six every morning.', 'Começo a escrever às seis toda manhã.'], ['Do you prefer writing or reading?', 'Você prefere escrever ou ler?'],
          ['I prefer to write, but I continue reading after.', 'Prefiro escrever, mas continuo lendo depois.'], ['Then begin today with one page.', 'Então comece hoje com uma página.']])

W(7082170, 'The Adventures of Huckleberry Finn', '📚 Livro · 1884', 'As Aventuras de Huckleberry Finn é um romance de Mark Twain, publicado em 1884: o menino Huck desce o rio Mississippi numa jangada.', ['🛶', '🌊', '🪢'], 'jungle')
C(7082170, ('Huck', 'Tom'), ['huck', 'tom'], 'lake', 'Na margem do rio, Huck e Tom falam de parar e de lembrar antes de sair de jangada.',
  ('🧺', 'basket', 'cesta', 'I stop to pack the basket.', 'Paro para arrumar a cesta.'),
  [('🛶', 'raft', 'jangada', 'Soa como “RÁFT”.'), ('🌊', 'river', 'rio', 'Soa como “RÍ-ver”.'), ('🪢', 'rope', 'corda', 'Soa como “RÔUP”.'),
   ('🧱', 'fence', 'cerca', 'Soa como “FÉNS”.'), ('🎣', 'fishing', 'pesca', 'Soa como “FÍ-shin”.'), ('🌅', 'sunset', 'pôr do sol', 'Soa como “SÂN-sét”.')],
  [('stop', '✋', 'parar', 'Stop talking.', 'Stop talk.', 'I stopped.', 'Parei.', 'stop **+ -ing** = deixar de.'),
   ('remember', '🧠', 'lembrar', 'Remember to bring it.', 'Remember bring it.', 'I remembered.', 'Lembrei.', 'remember **to** = não esquecer.'),
   ('forget', '🤦', 'esquecer', 'Do not forget to lock it.', 'Do not forget lock it.', 'I forgot.', 'Esqueci.', 'forget → **forgot**.'),
   ('paddle', '🛶', 'remar', 'Paddle to the bank.', 'Paddle at the bank.', 'I paddled.', 'Remei.', 'paddle **to**.')],
  [['Tom', 'Huck, stop talking for a minute.', 'Huck, pare de falar um minuto.'], ['Huck', 'I stopped to look at the river.', 'Parei para olhar o rio.'],
   ['Tom', 'Remember to bring the rope.', 'Lembre-se de trazer a corda.'], ['Huck', 'I remember seeing it in the boat.', 'Lembro de tê-la visto no barco.'],
   ['Tom', 'Then stop looking and go get it.', 'Então pare de olhar e vá pegá-la.'], ['Huck', 'I will stop to eat first, though.', 'Vou parar para comer primeiro, porém.'],
   ['Tom', 'Did you remember to tell Aunt Polly?', 'Você lembrou de avisar a tia Polly?'], ['Huck', 'Yes, I remember telling her this morning.', 'Sim, lembro de ter contado a ela hoje cedo.']],
  [('What does Tom want Huck to stop?', 'O que Tom quer que Huck pare?', [('🗣️', 'Talking'), ('🏃', 'Running'), ('🍎', 'Eating')], 0, 0, 'Tom diz: “stop talking for a minute.”'),
   ('What must Huck remember to bring?', 'O que Huck deve lembrar de trazer?', [('🪢', 'The rope'), ('🎣', 'A fish'), ('🧱', 'A fence')], 0, 2, 'Tom diz: “Remember to bring the rope.”'),
   ('Where does Huck remember seeing it?', 'Onde Huck lembra de tê-la visto?', [('🚣', 'In the boat'), ('🏠', 'At home'), ('🌳', 'In a tree')], 0, 3, 'Huck diz: “seeing it in the boat.”')],
  L('hf', 'Laboratório de sons: raft, river e fence', 'a soa á; i soa í; e soa é.', 'Em raft, o a soa á.',
    [('raft', 'RÁFT', 'jangada', 'a = á', 'rift', 'RÍFT'), ('river', 'RÍ-ver', 'rio', 'i = í', 'rover', 'RÔU-ver'), ('fence', 'FÉNS', 'cerca', 'e = é', 'fins', 'FÍNZ')]),
  [['Aunt Polly is calling us for supper.', 'A tia Polly está nos chamando para a ceia.'], ['Tell her we are painting the fence.', 'Diga a ela que estamos pintando a cerca.'],
   ['She will not believe that at all.', 'Ela não vai acreditar nisso.'], ['Then we paint first and fish later.', 'Então pintamos primeiro e pescamos depois.']])

F(82172, [['Swimming here is a pleasure in summer.', 'Nadar aqui é um prazer no verão.'], ['Walking around the lake is better for me.', 'Caminhar em volta do lago é melhor para mim.'],
          ['Living simply costs very little.', 'Viver com simplicidade custa muito pouco.'], ['And it makes you healthier, I think.', 'E deixa você mais saudável, acho.']])

W(7082172, 'Moby-Dick', '📚 Livro · 1851', 'Moby-Dick é um romance de Herman Melville, publicado em 1851: o capitão Ahab persegue uma grande baleia branca, e o marinheiro Ishmael conta a viagem.', ['🐋', '⚓', '🚢'], 'ship')
C(7082172, ('Ahab', 'Ishmael'), ['ahab', 'ishmael'], 'pier', 'No cais, Ishmael tenta convencer o capitão Ahab de que perseguir a baleia não vale o risco.',
  ('🧭', 'compass', 'bússola', 'It is no use losing the compass.', 'Não adianta perder a bússola.'),
  [('🐋', 'whale', 'baleia', 'Soa como “UÊIL”.'), ('🔱', 'harpoon', 'arpão', 'Soa como “har-PÚN”.'), ('⛈️', 'storm', 'tempestade', 'Soa como “STÓRM”.'),
   ('⚓', 'anchor', 'âncora', 'Soa como “ÉN-ker”.'), ('👥', 'crew', 'tripulação', 'Soa como “KRÚ”.'), ('⛵', 'mast', 'mastro', 'Soa como “MÉST”.')],
  [('chase', '🏃', 'perseguir', 'It is no use chasing the whale.', 'It is no use to chase the whale.', 'I chased it.', 'Persegui.', 'no use **+ -ing**.'),
   ('sail', '⛵', 'navegar', 'It is worth sailing farther.', 'It is worth to sail farther.', 'We sailed.', 'Navegamos.', 'worth **+ -ing**.'),
   ('risk', '⚠️', 'arriscar', 'Is it worth risking the crew?', 'Is it worth risk the crew?', 'I risked it.', 'Arrisquei.', 'worth **+ -ing**.'),
   ('wait', '⏳', 'esperar', 'There is no point waiting.', 'There is no point to wait.', 'I waited.', 'Esperei.', 'no point **+ -ing**.')],
  [['Ishmael', 'Captain, it is no use chasing the whale in this storm.', 'Capitão, não adianta perseguir a baleia nesta tempestade.'], ['Ahab', 'There is no point giving up now, Ishmael.', 'Não adianta desistir agora, Ishmael.'],
   ['Ishmael', 'Is it worth risking the whole crew?', 'Vale a pena arriscar toda a tripulação?'], ['Ahab', 'It is worth sailing farther for what I want.', 'Vale a pena navegar mais longe pelo que eu quero.'],
   ['Ishmael', 'It is no use asking the sea for mercy.', 'Não adianta pedir clemência ao mar.'], ['Ahab', 'There is no point waiting at the pier.', 'Não adianta esperar no cais.'],
   ['Ishmael', 'Then check the harpoon and the anchor.', 'Então verifique o arpão e a âncora.'], ['Ahab', 'Already done. Raise the mast!', 'Já feito. Levantem o mastro!']],
  [('Why is it no use chasing the whale?', 'Por que não adianta perseguir a baleia?', [('⛈️', 'There is a storm'), ('🌞', 'It is sunny'), ('😴', 'Everyone sleeps')], 0, 0, 'Ishmael diz: “in this storm.”'),
   ('What is worth risking, asks Ishmael?', 'O que Ishmael pergunta se vale arriscar?', [('👥', 'The whole crew'), ('🐟', 'A fish'), ('💰', 'Money')], 0, 2, 'Ishmael diz: “risking the whole crew?”'),
   ('What is there no point doing at the pier?', 'O que não adianta fazer no cais?', [('⏳', 'Waiting'), ('🎣', 'Fishing'), ('🍽️', 'Eating')], 0, 5, 'Ahab diz: “no point waiting at the pier.”')],
  L('md', 'Laboratório de sons: whale, storm e crew', 'wh soa u; or soa ór; ew soa ú.', 'Em whale, o wh soa u.',
    [('whale', 'UÊIL', 'baleia', 'wh = u', 'veil', 'VÊIL'), ('storm', 'STÓRM', 'tempestade', 'or = ór', 'steam', 'STÍM'), ('crew', 'KRÚ', 'tripulação', 'ew = ú', 'cry', 'KRÁI')]),
  [['Is it true he lost his leg to the whale?', 'É verdade que ele perdeu a perna para a baleia?'], ['So the sailors say on every ship.', 'É o que os marinheiros dizem em todo navio.'],
   ['Then no wonder he never gives up.', 'Então não admira que ele nunca desista.'], ['Or never forgives, I would say.', 'Ou nunca perdoa, eu diria.']])

# ---------------------------------------------------------------- 265 / 266
F(930038, [['Do you follow me so far, Daniel?', 'Você está me acompanhando até aqui, Daniel?'], ['Not really. What do you mean by wax on?', 'Na verdade, não. O que você quer dizer com passar cera?'],
           ['Could you repeat the movement slowly?', 'Você poderia repetir o movimento devagar?'], ['Watch my hands, then copy them.', 'Observe minhas mãos e depois copie.']])

W(7930038, 'My Fair Lady', '🎬 Filme · 1964', 'My Fair Lady é um filme musical de 1964, dirigido por George Cukor e baseado em Pigmalião, de Bernard Shaw: o professor Higgins ensina uma vendedora de flores a falar com elegância.', ['💐', '🎩', '🗣️'], 'library')
C(7930038, ('Higgins', 'Eliza'), ['tom', 'polly'], 'living', 'Na sala de estudos, o professor Higgins e Eliza tentam se fazer entender.',
  ('🎩', 'phonetics', 'fonética', 'Let me explain phonetics.', 'Deixe-me explicar a fonética.'),
  [('🗣️', 'accent', 'sotaque', 'Soa como “ÉK-sent”.'), ('💐', 'flower', 'flor', 'Soa como “FLÁU-er”.'), ('📓', 'lesson', 'lição', 'Soa como “LÉ-son”.'),
   ('👸', 'lady', 'dama', 'Soa como “LÊI-di”.'), ('🔤', 'vowel', 'vogal', 'Soa como “VÁU-el”.'), ('🎤', 'speech', 'fala', 'Soa como “SPÍTCH”.')],
  [('teach', '👨‍🏫', 'ensinar', 'He teaches me every day.', 'He teach me every day.', 'He taught me.', 'Ele me ensinou.', 'teach → **taught**.'),
   ('sell', '💐', 'vender', 'I sell flowers.', 'I sells flowers.', 'I sold them.', 'Vendi.', 'sell → **sold**.'),
   ('pronounce', '🔤', 'pronunciar', 'I pronounce it slowly.', 'I pronounce it slow.', 'I pronounced.', 'Pronunciei.', 'pronounce **+ objeto**.'),
   ('practise', '🔁', 'praticar', 'Practise every day.', 'Practise in every day.', 'I practised.', 'Pratiquei.', 'practise **+ objeto**.')],
  [['Higgins', 'Eliza, say it again, slowly.', 'Eliza, diga de novo, devagar.'], ['Eliza', 'What I mean is, I want to speak properly.', 'O que eu quero dizer é que quero falar corretamente.'],
   ['Higgins', 'In other words, you want to sound like a lady.', 'Em outras palavras, você quer soar como uma dama.'], ['Eliza', 'Exactly. Let me explain: I sell flowers and nobody listens.', 'Exatamente. Deixe-me explicar: vendo flores e ninguém me ouve.'],
   ['Higgins', 'Let me put it this way: your accent is the problem.', 'Deixe-me dizer assim: o seu sotaque é o problema.'], ['Eliza', 'What I mean is, I want a better job in a shop.', 'O que eu quero dizer é que quero um emprego melhor numa loja.'],
   ['Higgins', 'In other words, a lesson every morning. Repeat after me.', 'Em outras palavras, uma lição toda manhã. Repita comigo.'], ['Eliza', 'The weather is lovely today.', 'O tempo está lindo hoje.']],
  [('What does Eliza want?', 'O que Eliza quer?', [('🗣️', 'To speak properly'), ('💰', 'To be rich'), ('🏠', 'To move')], 0, 1, 'Eliza diz: “I want to speak properly.”'),
   ('What is the problem, says Higgins?', 'Qual é o problema, diz Higgins?', [('🎩', 'Her accent'), ('👗', 'Her dress'), ('🚪', 'The door')], 0, 4, 'Higgins diz: “your accent is the problem.”'),
   ('What does Eliza sell?', 'O que Eliza vende?', [('💐', 'Flowers'), ('🍞', 'Bread'), ('📚', 'Books')], 0, 3, 'Eliza diz: “I sell flowers.”')],
  L('mf', 'Laboratório de sons: accent, flower e lesson', 'a soa é; ow soa áu; e soa é.', 'Em flower, o ow soa áu.',
    [('accent', 'ÉK-sent', 'sotaque', 'a = é', 'ascent', 'a-SÉNT'), ('flower', 'FLÁU-er', 'flor', 'ow = áu', 'floor', 'FLÓR'), ('lesson', 'LÉ-son', 'lição', 'e = é', 'listen', 'LÍ-son')]),
  [['Did Eliza practise the vowels last night?', 'Eliza praticou as vogais ontem à noite?'], ['She said them forty times, I believe.', 'Ela as repetiu muitas vezes, acredito.'],
   ['Then she is ready for the party.', 'Então ela está pronta para a festa.'], ['Ready, yes. Nervous, also yes.', 'Pronta, sim. Nervosa, também.']])

# ---------------------------------------------------------------- 267 / 268
F(82173, [['I came here to learn English properly.', 'Vim aqui para aprender inglês direito.'], ['In order to improve, you must speak daily.', 'Para melhorar, você precisa falar todo dia.'],
          ['I buy a notebook so as to write new words.', 'Compro um caderno para anotar palavras novas.'], ['Good. Courage is the only thing you need.', 'Bom. Coragem é a única coisa de que precisa.']])

W(7082173, 'Robin Hood', '🏹 Lenda · Inglaterra', 'Robin Hood é uma lenda inglesa sobre um arqueiro que vive na floresta de Sherwood e ajuda os pobres, enfrentando o xerife de Nottingham.', ['🏹', '🌲', '🦌'], 'jungle')
C(7082173, ('Robin', 'Little John'), ['robin', 'tom'], 'yard', 'Na floresta, Robin e Little John explicam para que serve cada coisa do acampamento.',
  ('🌳', 'oak', 'carvalho', 'Meet me at the oak to talk.', 'Encontre-me no carvalho para conversar.'),
  [('🏹', 'bow', 'arco', 'Soa como “BÔU”.'), ('🌲', 'forest', 'floresta', 'Soa como “FÓ-rest”.'), ('🦌', 'deer', 'veado', 'Soa como “DÍR”.'),
   ('🪙', 'coin', 'moeda', 'Soa como “KÓIN”.'), ('🛡️', 'sheriff', 'xerife', 'Soa como “SHÉ-rif”.'), ('🎒', 'bag', 'sacola', 'Soa como “BÉG”.')],
  [('hunt', '🦌', 'caçar', 'We use the bow to hunt.', 'We use the bow for hunt.', 'I hunted.', 'Caçei.', '**to** + verbo = finalidade.'),
   ('share', '🤝', 'dividir', 'We share it so that nobody is hungry.', 'We share it for that nobody is hungry.', 'We shared.', 'Dividimos.', 'so that **+ frase**.'),
   ('rescue', '🛟', 'resgatar', 'I went there to rescue him.', 'I went there for rescue him.', 'I rescued him.', 'Eu o resgatei.', '**to** + verbo.'),
   ('hide', '🫥', 'esconder', 'We hide to stay safe.', 'We hide for stay safe.', 'We hid.', 'Nos escondemos.', 'hide → **hid**.')],
  [['John', 'What is the bow for, Robin?', 'Para que serve o arco, Robin?'], ['Robin', 'We use it to hunt, not to fight.', 'Usamos para caçar, não para lutar.'],
   ['John', 'And the bag? What is it for?', 'E a sacola? Para que serve?'], ['Robin', 'It is for carrying coins to the poor.', 'Serve para levar moedas aos pobres.'],
   ['John', 'We share the food so that nobody goes hungry.', 'Dividimos a comida para que ninguém passe fome.'], ['Robin', 'I came to the forest to help the poor.', 'Vim para a floresta para ajudar os pobres.'],
   ['John', 'And I stay to help you.', 'E eu fico para ajudar você.'], ['Robin', 'Then hide the bag before the sheriff comes.', 'Então esconda a sacola antes que o xerife chegue.']],
  [('What do they use the bow for?', 'Para que usam o arco?', [('🦌', 'To hunt'), ('⚔️', 'To fight'), ('🎵', 'To play music')], 0, 1, 'Robin diz: “We use it to hunt.”'),
   ('What is the bag for?', 'Para que serve a sacola?', [('🪙', 'Carrying coins to the poor'), ('🍞', 'Carrying bread home'), ('🎒', 'School')], 0, 3, 'Robin diz: “for carrying coins to the poor.”'),
   ('Why do they share the food?', 'Por que dividem a comida?', [('🍽️', 'So nobody goes hungry'), ('💰', 'To sell it'), ('🎁', 'As a gift')], 0, 4, 'John diz: “so that nobody goes hungry.”')],
  L('rh', 'Laboratório de sons: forest, deer e sheriff', 'o soa ó; ee soa í; sh soa x.', 'Em deer, o ee soa í.',
    [('forest', 'FÓ-rest', 'floresta', 'o = ó', 'first', 'FÉRST'), ('deer', 'DÍR', 'veado', 'ee = í', 'door', 'DÓR'), ('sheriff', 'SHÉ-rif', 'xerife', 'sh = x', 'chef', 'SHÉF')]),
  [['Did the sheriff send men to the oak?', 'O xerife mandou homens ao carvalho?'], ['Not yet, but a scout was seen nearby.', 'Ainda não, mas um batedor foi visto por perto.'],
   ['Then we move the camp tonight.', 'Então mudamos o acampamento esta noite.'], ['I will tell the others quietly.', 'Avisarei os outros em silêncio.']])

# ---------------------------------------------------------------- 269 / 270
F(82175, [['Get in the car, we are late.', 'Entre no carro, estamos atrasados.'], ['Wait, I need to get off at the next stop.', 'Espere, preciso descer na próxima parada.'],
          ['The police told us to pull over.', 'A polícia mandou a gente encostar.'], ['Then let us set off after the check.', 'Então partimos depois da vistoria.']])

W(7082175, 'Harry Potter and the Prisoner of Azkaban', '📚 Livro · 1999', 'Harry Potter e o Prisioneiro de Azkaban é o terceiro livro da série de J. K. Rowling, publicado em 1999; nele, Harry viaja num ônibus mágico, o Nôitibus.', ['🚌', '🧳', '🪄'], 'castle')
C(7082175, ('Harry', 'Stan'), ['harry', 'tom'], 'street', 'Numa rua escura de Londres, Harry conversa com o cobrador do ônibus mágico.',
  ('🔦', 'lamp', 'poste de luz', 'Pull up under the lamp.', 'Pare sob o poste de luz.'),
  [('🚌', 'conductor', 'cobrador', 'Soa como “kon-DÂK-ter”.'), ('🛏️', 'bed', 'cama', 'Soa como “BÉD”.'), ('🧳', 'trunk', 'baú', 'Soa como “TRÂNK”.'),
   ('🌃', 'corner', 'esquina', 'Soa como “KÓR-ner”.'), ('🧙', 'wizard', 'bruxo', 'Soa como “UÍ-zerd”.'), ('🚏', 'stop', 'ponto', 'Soa como “STÓP”.')],
  [('wave', '👋', 'acenar', 'We wave goodbye.', 'We wave goodbye to.', 'We waved.', 'Acenamos.', 'wave **goodbye**.'),
   ('hold', '🤲', 'segurar', 'Hold on tight.', 'Hold in tight.', 'I held on.', 'Segurei firme.', 'hold → **held**.'),
   ('stop', '🛑', 'parar', 'The bus stops here.', 'The bus stop here.', 'It stopped.', 'Parou.', 'he/she/it **stops**.'),
   ('park', '🅿️', 'estacionar', 'Park near the gate.', 'Park at near the gate.', 'I parked.', 'Estacionei.', 'park **+ lugar**.')],
  [['Harry', 'Please pull up at the next corner.', 'Por favor, encoste na próxima esquina.'], ['Stan', 'We pull up there in a minute.', 'Encostamos lá em um minuto.'],
   ['Harry', 'Can you drop me off near the inn?', 'Pode me deixar perto da estalagem?'], ['Stan', 'We drop you off first, then we pick up the next wizard.', 'Deixamos você primeiro, depois pegamos o próximo bruxo.'],
   ['Harry', 'My friends will see me off at the station.', 'Meus amigos vão se despedir de mim na estação.'], ['Stan', 'Who will pick you up when you come back?', 'Quem vai buscar você quando voltar?'],
   ['Harry', 'Hagrid will pick me up with the trunk.', 'Hagrid me busca com o baú.'], ['Stan', 'Hold on tight! Here we go!', 'Segure firme! Lá vamos nós!']],
  [('Where does Harry want the bus to pull up?', 'Onde Harry quer que o ônibus encoste?', [('🌃', 'At the next corner'), ('🏫', 'At school'), ('🏠', 'At home')], 0, 0, 'Harry diz: “pull up at the next corner.”'),
   ('Who will see Harry off?', 'Quem vai se despedir de Harry?', [('👫', 'His friends'), ('👮', 'The police'), ('🐱', 'A cat')], 0, 4, 'Harry diz: “My friends will see me off.”'),
   ('Who will pick Harry up?', 'Quem vai buscar Harry?', [('🧔', 'Hagrid'), ('🧙', 'Stan'), ('👩', 'Hermione')], 0, 6, 'Harry diz: “Hagrid will pick me up.”')],
  L('hp', 'Laboratório de sons: conductor, trunk e corner', 'u soa â; or soa ór; ck soa k.', 'Em trunk, o u soa â.',
    [('conductor', 'kon-DÂK-ter', 'cobrador', 'u = â', 'contractor', 'KÓN-trak-ter'), ('trunk', 'TRÂNK', 'baú', 'u = â', 'trick', 'TRÍK'), ('corner', 'KÓR-ner', 'esquina', 'or = ór', 'corn', 'KÓRN')]),
  [['Is the bus really that fast?', 'O ônibus é mesmo tão rápido?'], ['Faster than any car you have seen.', 'Mais rápido que qualquer carro que você já viu.'],
   ['And does it stop for every passenger?', 'E para para todos os passageiros?'], ['Only if they wave at the right moment.', 'Só se acenarem na hora certa.']])

F(82176, [['Look up the word in the dictionary.', 'Procure a palavra no dicionário.'], ['Can you look after my dog on Friday?', 'Pode cuidar do meu cachorro na sexta?'],
          ['Look out! There is a bike coming.', 'Cuidado! Vem uma bicicleta.'], ['I look forward to the weekend already.', 'Já estou ansioso pelo fim de semana.']])

W(7082176, 'Aladdin', '🎬 Filme · 1992', 'Aladdin é uma animação da Disney de 1992, inspirada num conto das Mil e Uma Noites: um jovem pobre encontra uma lâmpada mágica e conhece a princesa Jasmine.', ['🪔', '🧞', '🐒'], 'bakery')
C(7082176, ('Aladdin', 'Jasmine'), ['aladdin', 'jasmine'], 'street', 'No mercado de Agrabah, Aladdin e Jasmine falam de quem olha de cima e de quem se admira.',
  ('🪄', 'carpet', 'tapete', 'Look over the carpet first.', 'Examine o tapete primeiro.'),
  [('🪔', 'lamp', 'lâmpada', 'Soa como “LÉMP”.'), ('🧞', 'genie', 'gênio', 'Soa como “DJÍ-ni”.'), ('🧺', 'stall', 'barraca', 'Soa como “STÓL”.'),
   ('🛒', 'market', 'mercado', 'Soa como “MAR-kit”.'), ('📜', 'scroll', 'pergaminho', 'Soa como “SKRÔUL”.'), ('👑', 'sultan', 'sultão', 'Soa como “SÂL-ten”.')],
  [('trust', '🤝', 'confiar', 'I trust you.', 'I trust to you.', 'I trusted you.', 'Confiei em você.', 'trust **+ objeto**.'),
   ('steal', '🫳', 'roubar', 'He did not steal it.', 'He did not stole it.', 'He stole.', 'Ele roubou.', 'steal → **stole**.'),
   ('wish', '🌠', 'desejar', 'I wish for freedom.', 'I wish freedom for.', 'I wished.', 'Desejei.', 'wish **for**.'),
   ('respect', '🙌', 'respeitar', 'I respect honest people.', 'I respect to honest people.', 'I respected.', 'Respeitei.', 'respect **+ objeto**.')],
  [['Jasmine', 'The guards look down on you, Aladdin.', 'Os guardas desprezam você, Aladdin.'], ['Aladdin', 'I know. But I look up to people who help others.', 'Eu sei. Mas admiro quem ajuda os outros.'],
   ['Jasmine', 'Look over this scroll before we go.', 'Examine este pergaminho antes de irmos.'], ['Aladdin', 'Let me look through the market stalls first.', 'Deixe-me olhar as barracas do mercado primeiro.'],
   ['Jasmine', 'Do not let the sultan look down on us.', 'Não deixe o sultão nos menosprezar.'], ['Aladdin', 'Do you look up to your father?', 'Você admira seu pai?'],
   ['Jasmine', 'I do, but I look over every law he signs.', 'Admiro, mas examino cada lei que ele assina.'], ['Aladdin', 'Then look over this plan with me.', 'Então examine este plano comigo.']],
  [('Who looks down on Aladdin?', 'Quem despreza Aladdin?', [('💂', 'The guards'), ('🧞', 'The genie'), ('🐒', 'The monkey')], 0, 0, 'Jasmine diz: “The guards look down on you.”'),
   ('Who does Aladdin look up to?', 'Quem Aladdin admira?', [('🤝', 'People who help others'), ('👑', 'Kings'), ('💰', 'Rich men')], 0, 1, 'Aladdin diz: “I look up to people who help others.”'),
   ('What does Jasmine look over?', 'O que Jasmine examina?', [('📜', 'Every law her father signs'), ('🍎', 'Fruit'), ('🪔', 'A lamp')], 0, 6, 'Jasmine diz: “I look over every law he signs.”')],
  L('al', 'Laboratório de sons: lamp, genie e sultan', 'a soa é; g soa dj; u soa â.', 'Em genie, o g soa dj.',
    [('lamp', 'LÉMP', 'lâmpada', 'a = é', 'limp', 'LÍMP'), ('genie', 'DJÍ-ni', 'gênio', 'g = dj', 'jeans', 'DJÍNZ'), ('sultan', 'SÂL-ten', 'sultão', 'u = â', 'salton', 'SÓL-ten')]),
  [['Where did the street boy find the lamp?', 'Onde o menino de rua achou a lâmpada?'], ['In a cave, guarded by a tiger.', 'Numa caverna, guardada por um tigre.'],
   ['And he gave a wish to a friend?', 'E ele deu um desejo a um amigo?'], ['He did. That is why people respect him.', 'Deu. Por isso as pessoas o respeitam.']])

# ---------------------------------------------------------------- 271 / 272
F(82177, [['The plane takes off in ten minutes.', 'O avião decola em dez minutos.'], ['She wants to take up the piano this year.', 'Ela quer começar piano este ano.'],
          ['He takes after his father, you know.', 'Ele puxa ao pai, sabe.'], ['Another pilot will take over after landing.', 'Outro piloto assume depois do pouso.']])

W(7082177, 'A Study in Scarlet', '📚 Livro · 1887', 'Um Estudo em Vermelho é o primeiro romance com Sherlock Holmes, de Arthur Conan Doyle, publicado em 1887: Holmes e o doutor Watson investigam um crime em Londres.', ['🔍', '🕰️', '🎩'], 'library')
C(7082177, ('Sherlock', 'Watson'), ['sherlock', 'watson'], 'living', 'Na casa da Baker Street, Sherlock e Watson examinam um relógio com um segredo.',
  ('🧶', 'clue', 'pista', 'Take in every clue.', 'Observe cada pista.'),
  [('🔍', 'magnifier', 'lupa', 'Soa como “MÉG-ni-fái-er”.'), ('🕰️', 'clock', 'relógio de parede', 'Soa como “KLÓK”.'), ('📓', 'notebook', 'caderno', 'Soa como “NÔUT-buk”.'),
   ('✉️', 'note', 'bilhete', 'Soa como “NÔUT”.'), ('🧩', 'detail', 'detalhe', 'Soa como “di-TÊIL”.'), ('🕵️', 'detective', 'detetive', 'Soa como “di-TÉK-tiv”.')],
  [('examine', '🔎', 'examinar', 'Examine the clock.', 'Examine to the clock.', 'I examined it.', 'Examinei.', 'examine **+ objeto**.'),
   ('notice', '👀', 'notar', 'I notice a small note.', 'I notice to a small note.', 'I noticed.', 'Notei.', 'notice **+ objeto**.'),
   ('solve', '🧩', 'resolver', 'We solve the case.', 'We solves the case.', 'We solved it.', 'Resolvemos.', 'solve **+ objeto**.'),
   ('open', '📂', 'abrir', 'Open the clock.', 'Open to the clock.', 'I opened it.', 'Abri.', 'open **+ objeto**.')],
  [['Watson', 'Holmes, take back what you said about the case.', 'Holmes, retire o que disse sobre o caso.'], ['Sherlock', 'I take nothing back. Take out your notebook.', 'Não retiro nada. Tire seu caderno.'],
   ['Watson', 'I took it out. Where do I start?', 'Já tirei. Por onde começo?'], ['Sherlock', 'Take in every detail of the room first.', 'Absorva primeiro cada detalhe da sala.'],
   ['Watson', 'And the clock? It looks old.', 'E o relógio? Parece velho.'], ['Sherlock', 'Take it apart, Watson, slowly.', 'Desmonte, Watson, devagar.'],
   ['Watson', 'I took it apart. There is a note inside!', 'Desmontei. Há um bilhete dentro!'], ['Sherlock', 'Take it out. Now the case comes together.', 'Tire-o. Agora o caso se encaixa.']],
  [('What must Watson take out?', 'O que Watson deve tirar?', [('📓', 'His notebook'), ('🔍', 'A magnifier'), ('🧥', 'His coat')], 0, 1, 'Sherlock diz: “Take out your notebook.”'),
   ('What does Sherlock tell him to take apart?', 'O que Sherlock manda desmontar?', [('🕰️', 'The clock'), ('📻', 'A radio'), ('🚪', 'A door')], 0, 5, 'Sherlock diz: “Take it apart, Watson.”'),
   ('What is inside?', 'O que há dentro?', [('✉️', 'A note'), ('💎', 'A jewel'), ('🗝️', 'A key')], 0, 6, 'Watson diz: “There is a note inside!”')],
  L('sh', 'Laboratório de sons: clock, detail e magnifier', 'o soa ó; ai soa êi; a soa é.', 'Em detail, o ai soa êi.',
    [('clock', 'KLÓK', 'relógio', 'o = ó', 'clack', 'KLÉK'), ('detail', 'di-TÊIL', 'detalhe', 'ai = êi', 'detain', 'di-TÊIN'), ('magnifier', 'MÉG-ni-fái-er', 'lupa', 'a = é', 'manifest', 'MÉ-ni-fést')]),
  [['Who wound the clock last night?', 'Quem deu corda no relógio ontem à noite?'], ['Nobody. The maid says it stopped on Monday.', 'Ninguém. A empregada diz que parou na segunda.'],
   ['Then the note was hidden before that.', 'Então o bilhete foi escondido antes disso.'], ['Elementary, my dear Watson.', 'Elementar, meu caro Watson.']])

F(930039, [['Can you keep a secret, Katie?', 'Você sabe guardar um segredo, Katie?'], ['Of course. We keep in touch every day.', 'Claro. A gente se fala todo dia.'],
           ['Keep calm and keep going, whatever happens.', 'Mantenha a calma e siga em frente, aconteça o que acontecer.'], ['Okay. I will not tell a soul.', 'Certo. Não conto a ninguém.']])

W(7930039, 'The Secret Garden', '📚 Livro · 1911', 'O Jardim Secreto é um romance de Frances Hodgson Burnett, publicado em 1911: a menina Mary descobre um jardim trancado numa casa grande e o traz de volta à vida.', ['🌹', '🔑', '🌱'], 'bakery')
C(7930039, ('Mary', 'Dickon'), ['mary', 'tommy'], 'yard', 'Junto ao muro do jardim, Mary e Dickon combinam o que fazer e o que evitar.',
  ('🚪', 'gate', 'portão', 'Keep away from the gate.', 'Fique longe do portão.'),
  [('🌹', 'rose', 'rosa', 'Soa como “RÔUZ”.'), ('🔑', 'key', 'chave', 'Soa como “KÍ”.'), ('🧱', 'wall', 'muro', 'Soa como “UÓL”.'),
   ('⛏️', 'spade', 'pá', 'Soa como “SPÊID”.'), ('🌱', 'seed', 'semente', 'Soa como “SÍD”.'), ('🐦', 'robin', 'tordo', 'Soa como “RÓ-bin”.')],
  [('dig', '⛏️', 'cavar', 'Dig by the wall.', 'Dig at by the wall.', 'I dug.', 'Cavei.', 'dig → **dug**.'),
   ('plant', '🌱', 'plantar', 'We plant seeds.', 'We plants seeds.', 'We planted.', 'Plantamos.', 'plural: **plant**.'),
   ('water', '💧', 'regar', 'Water the roses.', 'Water to the roses.', 'I watered.', 'Reguei.', 'water **+ objeto**.'),
   ('grow', '🌿', 'crescer', 'Roses grow in spring.', 'Roses grows in spring.', 'They grew.', 'Cresceram.', 'grow → **grew**.')],
  [['Mary', 'Keep away from the garden wall, Dickon.', 'Fique longe do muro do jardim, Dickon.'], ['Dickon', 'Why? The sign only says keep off the grass.', 'Por quê? A placa só diz para não pisar na grama.'],
   ['Mary', 'Keep off the grass, and keep quiet.', 'Não pise na grama e fique quieto.'], ['Dickon', 'Keep up, then. I walk fast.', 'Acompanhe, então. Eu ando rápido.'],
   ['Mary', 'I will keep up. Keep on digging by the roses.', 'Eu acompanho. Continue cavando junto às rosas.'], ['Dickon', 'I keep on working until the sun goes down.', 'Continuo trabalhando até o sol se pôr.'],
   ['Mary', 'Keep it up, and spring will arrive.', 'Continue assim, e a primavera chega.'], ['Dickon', 'Keep away from the gate, and nobody knows.', 'Fique longe do portão, e ninguém sabe.']],
  [('What must Dickon keep away from?', 'De que Dickon deve ficar longe?', [('🧱', 'The garden wall'), ('🏠', 'The house'), ('🐦', 'The bird')], 0, 0, 'Mary diz: “Keep away from the garden wall.”'),
   ('What does Mary want Dickon to keep on doing?', 'O que Mary quer que Dickon continue fazendo?', [('⛏️', 'Digging'), ('🎵', 'Singing'), ('😴', 'Sleeping')], 0, 4, 'Mary diz: “Keep on digging by the roses.”'),
   ('What arrives if they keep it up?', 'O que chega se continuarem?', [('🌸', 'Spring'), ('❄️', 'Winter'), ('🌧️', 'Rain')], 0, 6, 'Mary diz: “spring will arrive.”')],
  L('sg', 'Laboratório de sons: rose, seed e spade', 'o soa ôu; ee soa í; a soa êi.', 'Em spade, o a soa êi.',
    [('rose', 'RÔUZ', 'rosa', 'o = ôu', 'rise', 'RÁIZ'), ('seed', 'SÍD', 'semente', 'ee = í', 'said', 'SÉD'), ('spade', 'SPÊID', 'pá', 'a = êi', 'spied', 'SPÁID')]),
  [['Did the gardener see the open door?', 'O jardineiro viu a porta aberta?'], ['No, the robin kept watch for us.', 'Não, o tordo vigiou por nós.'],
   ['Then the secret is safe for now.', 'Então o segredo está seguro por ora.'], ['Safe until the roses start to bloom.', 'Seguro até as rosas começarem a florescer.']])

# ---------------------------------------------------------------- 279 / 280
F(82178, [['I will never give up on this fight.', 'Nunca vou desistir desta luta.'], ['Then do not give in to the pain.', 'Então não ceda à dor.'],
          ['After the match I give away my gloves.', 'Depois da luta, dou minhas luvas.'], ['Give back the belt when you lose.', 'Devolva o cinturão quando perder.']])

W(7082178, 'Oliver Twist', '📚 Livro · 1838', 'Oliver Twist é um romance de Charles Dickens, publicado em 1838: o órfão Oliver vive num asilo de pobres e ousa pedir mais comida.', ['🥣', '🕯️', '🧥'], 'library')
C(7082178, ('Oliver', 'Mr Bumble'), ['oliver', 'bumble'], 'hall', 'No refeitório do asilo, o Sr. Bumble e Oliver falam de quem distribui a sopa.',
  ('🥣', 'bowl', 'tigela', 'Give out a bowl to each boy.', 'Distribua uma tigela a cada menino.'),
  [('🥄', 'spoon', 'colher', 'Soa como “SPÚN”.'), ('🍲', 'pot', 'panela', 'Soa como “PÓT”.'), ('🪑', 'bench', 'banco', 'Soa como “BÉNTCH”.'),
   ('🕯️', 'candle', 'vela', 'Soa como “KÉN-dol”.'), ('🧥', 'blanket', 'cobertor', 'Soa como “BLÉN-kit”.'), ('🌅', 'dawn', 'amanhecer', 'Soa como “DÓN”.')],
  [('serve', '🍽️', 'servir', 'The cook serves the soup.', 'The cook serve the soup.', 'He served it.', 'Ele serviu.', 'he/she **serves**.'),
   ('smell', '👃', 'cheirar', 'The pot smells warm.', 'The pot smell warm.', 'It smelled.', 'Cheirou.', 'he/she/it **smells**.'),
   ('queue', '🧍', 'fazer fila', 'We queue at noon.', 'We queue to noon.', 'We queued.', 'Fizemos fila.', 'queue **at + hora**.'),
   ('shiver', '🥶', 'tremer', 'I shiver at dawn.', 'I shivers at dawn.', 'I shivered.', 'Tremi.', 'I **shiver**.')],
  [['Bumble', 'The cook gives out the soup at noon.', 'A cozinheira distribui a sopa ao meio-dia.'], ['Oliver', 'The pot gives off a warm smell.', 'A panela exala um cheiro quente.'],
   ['Bumble', 'Give way to the older boys at the bench.', 'Dê passagem aos meninos mais velhos no banco.'], ['Oliver', 'The line gives way to nobody, sir.', 'A fila não cede a ninguém, senhor.'],
   ['Bumble', 'Give over, Oliver! No more asking for more.', 'Pare com isso, Oliver! Chega de pedir mais.'], ['Oliver', 'The candle gives off a poor light.', 'A vela dá uma luz fraca.'],
   ['Bumble', 'The master gives out the work at dawn.', 'O diretor distribui o trabalho ao amanhecer.'], ['Oliver', 'Then I give over, sir, and I wait.', 'Então paro, senhor, e espero.']],
  [('When does the cook give out the soup?', 'Quando a cozinheira distribui a sopa?', [('🕛', 'At noon'), ('🌅', 'At dawn'), ('🌙', 'At night')], 0, 0, 'Bumble diz: “gives out the soup at noon.”'),
   ('What does the pot give off?', 'O que a panela exala?', [('👃', 'A warm smell'), ('💨', 'Smoke'), ('🔊', 'A loud noise')], 0, 1, 'Oliver diz: “gives off a warm smell.”'),
   ('What does Bumble tell Oliver to give over?', 'O que Bumble manda Oliver parar?', [('🙅', 'Asking for more'), ('🏃', 'Running'), ('🎵', 'Singing')], 0, 4, 'Bumble diz: “Give over, Oliver! No more asking for more.”')],
  L('ot', 'Laboratório de sons: candle, blanket e dawn', 'a soa é; a soa é; aw soa ó.', 'Em dawn, o aw soa ó.',
    [('candle', 'KÉN-dol', 'vela', 'a = é', 'handle', 'HÉN-dol'), ('blanket', 'BLÉN-kit', 'cobertor', 'a = é', 'blinking', 'BLÍN-kin'), ('dawn', 'DÓN', 'amanhecer', 'aw = ó', 'down', 'DÁUN')]),
  [['Is there enough soup for every boy?', 'Há sopa suficiente para cada menino?'], ['Barely. The pot is almost empty.', 'Mal. A panela está quase vazia.'],
   ['Then the youngest should be served first.', 'Então os mais novos devem ser servidos primeiro.'], ['That is not the rule here, I fear.', 'Essa não é a regra aqui, receio.']])
