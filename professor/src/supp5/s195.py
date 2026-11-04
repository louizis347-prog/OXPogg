"""Suplemento Quest v5 · aula 195: Bowling night + regular Play cards (Carmen)."""
SUPP = {
 'reg': 182,
 'badge': {'icon': '🎳', 'name': 'Strike Star', 'desc': 'Rent shoes, pick a ball and play bowling with friends'},
 'culture': {
  'hook': 'A bowling alley in the USA is a place for friends and family. You rent shoes at the desk, pick a ball, and cheer for everyone, even after a bad throw.',
  'mythfact': [
   {'s': 'In many bowling alleys, you can rent special shoes at the desk.', 'ans': True, 'why': 'Most alleys ask you to use their shoes on the lane.'},
   {'s': 'A strike means you knock down all ten pins with the first ball.', 'ans': True, 'why': 'It is the best result in one turn.'},
   {'s': 'In bowling, the heaviest ball is always the best for a beginner.', 'ans': False, 'why': 'A lighter ball is easier to use at first.'},
   {'s': 'A ball in the gutter gets many points.', 'ans': False, 'why': 'The gutter is the side channel, and the ball knocks down no pins there.'},
   {'s': '“Carmen” is an opera by Georges Bizet.', 'ans': True, 'why': 'It is from 1875.'}],
  'wild': [
   {'kind': 'Sign at the desk', 'lines': ['**Rental shoes: $4**', 'Socks required', 'Lanes 1–8: families', 'Ask for help'], 'decode': {'q': 'How much are rental shoes?', 'opts': ['$4', '$8', 'Free'], 'ans': 0, 'why': 'The sign says “Rental shoes: $4.”'}},
   {'kind': 'Score screen', 'lines': ['**Lane 6**', 'Maya: X (strike)', 'Leo: 7 /', 'Next: Ana'], 'decode': {'q': 'Who bowls next?', 'opts': ['Ana', 'Maya', 'Leo'], 'ans': 0, 'why': 'The screen says “Next: Ana.”'}}],
  'compare': {'br': 'In Brazil, bowling is a popular night out in malls and clubs, and many alleys also rent shoes and sell snacks.', 'us': 'In the USA, many bowling alleys have leagues and family nights, with lane numbers, rental shoes and an automatic score screen.', 'tip': 'Say: “Four players, please. Lane number six?”', 'ask': 'Who do you go out with at night? Say one sentence.'},
  'quiz': [
   {'q': 'You say how many people play. You say…', 'opts': ['Four players, please.', 'Four players, we.', 'We are four of players.'], 'ans': 0, 'why': 'Say the number + players, please.'},
   {'q': 'You want to know who starts. You ask…', 'opts': ['Who goes first?', 'Who is going first?', 'Who first goes?'], 'ans': 0, 'why': 'Use Who goes first? as a fixed question.'},
   {'q': 'You ask about the ball. You say…', 'opts': ['Which ball should I use?', 'Which ball I should use?', 'What ball should I to use?'], 'ans': 0, 'why': 'Which + noun + should + I + verb.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Strike!',
  'text': ['On Friday night, four friends go to a bowling alley. The room is loud, with music and the sound of falling pins. A young man named Evan works at the desk. “**Welcome! How many players?**” he asks. “**Four players, please.**”', '“**Do you need shoes?**” “**Yes, size nine and size seven.**” “**Here you go. Lane number six.**” The friends change their shoes and walk to the lane.', '“**Thanks. Which ball should I use?**” “**Try the blue one. It’s lighter.**” “**Okay. Who goes first?**” “**Ladies first!**” Maya rolls the ball, and it hits all ten pins. “Strike!” everyone shouts.', 'Then Leo throws the ball, but it goes into the gutter. He laughs, and his friends clap for him anyway. In the next turn he gets a spare. Everyone has fun, and nobody worries about the score.', 'After the game, they sit at a table and play cards. It reminds Maya of the opera “Carmen” from 1875. In one scene, Carmen and her friends read their future in the cards. “Shuffle the deck,” Maya says, and she deals the cards. It is a great night, and they decide to come back next week.'],
  'glossary': [{'w': 'bowling alley', 'pt': 'pista de boliche'}, {'w': 'pins', 'pt': 'pinos'}, {'w': 'lane', 'pt': 'pista'}, {'w': 'lighter', 'pt': 'mais leve'}, {'w': 'rolls', 'pt': 'rola'}, {'w': 'gutter', 'pt': 'canaleta'}, {'w': 'clap', 'pt': 'batem palmas'}, {'w': 'score', 'pt': 'placar'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Four friends have fun at a bowling alley', 'Four friends cook dinner', 'Four friends go to school'], 'ans': 0, 'why': 'They rent shoes, pick a ball and play.'},
  'scan': [{'q': 'Which lane do they get?', 'ans': 'lane six', 'alt': ['number six', 'six', 'lane number six']}, {'q': 'Which ball is lighter?', 'ans': 'the blue one', 'alt': ['blue', 'the blue ball']}, {'q': 'What do they play after the game?', 'ans': 'cards', 'alt': ['they play cards']}],
  'tf': [{'s': 'There are four players.', 'ans': True, 'why': 'The friends say, “Four players.”'}, {'s': 'Maya gets a strike.', 'ans': True, 'why': 'She hits all ten pins.'}, {'s': 'Leo’s ball goes to the gutter and everyone is angry.', 'ans': False, 'why': 'His friends clap for him.'}, {'s': 'The friends leave right after the game.', 'ans': False, 'why': 'They stay and play cards.'}],
  'order': ['The friends get shoes at the desk.', 'Evan gives them lane six.', 'Maya gets a strike.', 'Leo’s ball goes into the gutter.', 'They play cards after the game.'],
  'ctx': [{'sent': 'The ball goes into the gutter.', 'w': 'gutter', 'opts': ['the side channel of the lane', 'a kind of shoe', 'a snack'], 'ans': 0, 'why': 'The gutter is the channel on each side of a lane.'}, {'sent': 'It’s lighter.', 'w': 'lighter', 'opts': ['not so heavy', 'not so big', 'not so old'], 'ans': 0, 'why': 'Lighter means less heavy.'}, {'sent': 'His friends clap for him.', 'w': 'clap', 'opts': ['hit hands together to cheer', 'run to the door', 'drink water'], 'ans': 0, 'why': 'Clap means hit your hands together to cheer.'}],
  'chunkHunt': ['How many players?', 'Which ball should I use?', 'Who goes first?', 'Ladies first!'],
  'think': 'Do you like to play games with friends? What do you play?'},
 'convo': {'npc': {'name': 'Evan'}, 'story': 'You go to a bowling alley with three friends. Evan works at the desk and helps you.', 'turns': [
  {'npc': 'Welcome! How many players?', 'pt': 'Bem-vindos! Quantos jogadores?', 'opts': [
   {'en': 'Four players, please.', 'pt': 'Quatro jogadores, por favor.', 'ok': True, 'fb': 'Number + players, with please.'},
   {'en': 'We are four of players.', 'pt': 'Somos quatro de jogadores.', 'ok': False, 'fb': 'Do not use of here.'},
   {'en': 'Yes, thank you.', 'pt': 'Sim, obrigado.', 'ok': False, 'fb': 'It does not answer how many.'}]},
  {'npc': 'Do you need shoes?', 'pt': 'Precisam de sapatos?', 'opts': [
   {'en': 'No, I need bowling.', 'pt': 'Não, eu preciso boliche.', 'ok': False, 'fb': 'It does not make sense.'},
   {'en': 'Yes, size nine and size seven.', 'pt': 'Sim, tamanho quarenta e três e quarenta.', 'ok': True, 'fb': 'Yes + sizes.'},
   {'en': 'Yes, I am nine and seven.', 'pt': 'Sim, eu sou nove e sete.', 'ok': False, 'fb': 'Say size nine, not I am nine.'}]},
  {'npc': 'Here you go. Lane number six.', 'pt': 'Aqui estão. Pista número seis.', 'opts': [
   {'en': 'Thanks. Which ball should I use?', 'pt': 'Valeu. Qual bola devo usar?', 'ok': True, 'fb': 'Thanks + a useful question.'},
   {'en': 'Thanks. Which ball I should use?', 'pt': 'Valeu. Qual bola eu devo usar?', 'ok': False, 'fb': 'In questions: should I.'},
   {'en': 'Four players, please.', 'pt': 'Quatro jogadores, por favor.', 'ok': False, 'fb': 'You already said that.'}]},
  {'npc': 'Try the blue one. It’s lighter.', 'pt': 'Tente a azul. É mais leve.', 'opts': [
   {'en': 'It is lighter.', 'pt': 'É mais leve.', 'ok': False, 'fb': 'It repeats Evan, with no question.'},
   {'en': 'Okay. Who goes first?', 'pt': 'Ok. Quem começa?', 'ok': True, 'fb': 'Accepts and asks the next question.'},
   {'en': 'Okay. Who is going first?', 'pt': 'Ok. Quem está indo primeiro?', 'ok': False, 'fb': 'The usual question is Who goes first?'}]},
  {'npc': 'Ladies first!', 'pt': 'As damas primeiro!', 'opts': [
   {'en': 'Thanks, Evan!', 'pt': 'Obrigado, Evan!', 'ok': False, 'fb': 'It is kind, but the game starts now: cheer up.'},
   {'en': 'No, I am the boss.', 'pt': 'Não, eu sou o chefe.', 'ok': False, 'fb': 'It sounds rude.'},
   {'en': 'Go, Maya! You can do it!', 'pt': 'Vai, Maya! Você consegue!', 'ok': True, 'fb': 'Friendly cheer for a friend.'}]}]},
 'errors': [
  {'wrong': 'We are four of players.', 'fix': 'Four players, please.', 'alt': 'We are four player.', 'why': 'Use number + players, with no of.'},
  {'wrong': 'Which ball I should use?', 'fix': 'Which ball should I use?', 'alt': 'Which ball should use I?', 'why': 'In questions, should comes before I.'},
  {'wrong': 'Who is going first?', 'fix': 'Who goes first?', 'alt': 'Who go first?', 'why': 'The set question is Who goes first? (who = he/she, so goes).'},
  {'wrong': 'I am size nine.', 'fix': 'Size nine, please.', 'alt': 'I have size nine shoe.', 'why': 'Say the size, not I am.'}],
 'homework': 'Write a short dialogue at a bowling alley: say how many players, shoe sizes and ask which ball to use.',
 'homework_items': ['Write the numbers one to ten.', 'Say aloud: Which ball should I use?', 'Listen to the dialogue and shadow Evan.', 'Review: bowling / strike / gutter / spare.']}
