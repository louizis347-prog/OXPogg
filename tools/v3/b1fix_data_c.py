# Itens 53–85 do B1 (continuações e falas próprias dos originais), lidos por v3/b1fix.py.
from v3.b1fix_data_a import O, FIX


def F(n, **kw):
    FIX.setdefault(n, {}).update(kw)


# ---- originais: só a segunda cena ("Na conversa de verdade") precisava de falas próprias
F(82027, fill=[['Did your jacket get wet?', 'Sua jaqueta molhou?'], ['Soaked. Even my socks.', 'Ensopado. Até as meias.'], ['Let us dry them by the fire.', 'Vamos secá-las perto do fogo.'], ['Good idea. I will bring the tea.', 'Boa ideia. Eu levo o chá.']])
F(930007, fill=[['Where was I? The client deadline.', 'Onde eu estava? O prazo do cliente.'], ['Friday, if I remember well.', 'Sexta, se bem me lembro.'], ['Then let us split the tasks now.', 'Então vamos dividir as tarefas agora.'], ['Fine. I will take the report.', 'Certo. Eu fico com o relatório.']])
F(82041, fill=[['Is our luggage here yet?', 'Nossa bagagem já está aqui?'], ['Not yet. The belt only just started.', 'Ainda não. A esteira acabou de começar.'], ['Then I will wait by the door.', 'Então espero perto da porta.'], ['Good. I will watch for the red bag.', 'Certo. Eu fico de olho na mala vermelha.']])
F(82042, fill=[['Next time, leave your boots by the door.', 'Da próxima vez, deixe as botas perto da porta.'], ['I will. I hate losing things.', 'Deixo. Detesto perder coisas.'], ['Shall I help you look in the hall?', 'Quer que eu ajude a olhar no corredor?'], ['Yes, and then we can have tea.', 'Quero, e depois tomamos chá.']])
F(82048, fill=[['Did you manage to fix the alarm?', 'Você conseguiu consertar o despertador?'], ['After three tries, yes.', 'Depois de três tentativas, sim.'], ['I could not have done it without help.', 'Eu não teria conseguido sem ajuda.'], ['You were able to, with a little patience.', 'Você foi capaz, com um pouco de paciência.']])
F(930010, fill=[['Who sits next to me?', 'Quem senta ao meu lado?'], ['The team from marketing.', 'A equipe de marketing.'], ['Great. I want to meet everyone.', 'Ótimo. Quero conhecer todo mundo.'], ['Lunch is at one. We go together.', 'O almoço é à uma. Vamos juntos.']])
F(82049, fill=[['When can you start?', 'Quando você pode começar?'], ['Next Monday, if you like.', 'Na segunda, se vocês quiserem.'], ['We will send the contract tomorrow.', 'Mandamos o contrato amanhã.'], ['I will read it carefully tonight.', 'Vou ler com atenção hoje à noite.']])
F(82050, fill=[['Drink more water this week.', 'Beba mais água esta semana.'], ['Good advice. I forget it often.', 'Bom conselho. Eu esqueço sempre.'], ['Try a short walk after lunch.', 'Tente uma caminhada curta depois do almoço.'], ['I will start tomorrow morning.', 'Começo amanhã de manhã.']])
F(82053, fill=[['Will they have a big wedding?', 'Eles vão fazer um casamento grande?'], ['Only close family, I heard.', 'Só a família próxima, ouvi dizer.'], ['That sounds lovely.', 'Parece lindo.'], ['We should send flowers.', 'Devíamos mandar flores.']])
F(930011, fill=[['Do you need a day to think?', 'Você precisa de um dia para pensar?'], ['Yes, if that is possible.', 'Preciso, se for possível.'], ['Take tomorrow off. We talk on Monday.', 'Fique em casa amanhã. Conversamos na segunda.'], ['I appreciate your honesty with me.', 'Agradeço a sua sinceridade comigo.']])
F(82054, fill=[['Should we save something every month?', 'Devemos guardar algo todo mês?'], ['Yes. A small fixed amount is enough.', 'Sim. Um valor fixo pequeno basta.'], ['I will set up an automatic transfer.', 'Vou programar uma transferência automática.'], ['Perfect. Then we will not forget.', 'Perfeito. Assim não esquecemos.']])
O(7930010, 'Legally Blonde', '🎬 Filme · 2001', 'Legally Blonde é uma comédia de 2001 dirigida por Robert Luketic, sobre uma jovem que chega a uma faculdade de direito e precisa aprender tudo do zero. Combina com falar do começo num trabalho novo.',
  'Legally Blonde: The first month at law school.', 'Legalmente Loira: O primeiro mês na faculdade de direito.', 'library', ['⚖️', '📚', '💼'], ('Elle', 'Emmett', 'polly', 'tom'),
  'Na faculdade, Elle e Emmett falam do primeiro mês e de aprender o trabalho, como em Legalmente Loira.',
  vocab=[('🦶', 'find my feet', 'me adaptar', 'Soa como “FÁIND mái FÍT”.'), ('🌊', 'deep end', 'situação difícil (fundo da piscina)', 'Soa como “DÍP END”.'), ('🏋️', 'pull your weight', 'fazer sua parte', 'Soa como “PUL iór UÊIT”.'),
         ('🧵', 'the ropes', 'os macetes', 'Soa como “dhe RÔUPS”.'), ('💬', 'feedback', 'retorno', 'Soa como “FÍD-béc”.'), ('📆', 'probation', 'período de experiência', 'Soa como “pro-BÊI-xn”.')],
  fill=[['What do I wear on the first day?', 'O que eu visto no primeiro dia?'], ['Smart casual is fine here.', 'Um traje esporte fino serve aqui.'], ['I will bring a notebook too.', 'Vou levar um caderno também.'], ['Good. Write down every name.', 'Bom. Anote todos os nomes.']])
O(7082049, 'The Social Network', '🎬 Filme · 2010', 'The Social Network é um filme de 2010 dirigido por David Fincher, sobre a criação de uma rede social na universidade e os sócios que a lançaram. Combina com resumir uma carreira até agora.',
  'The Social Network: A launch night.', 'A Rede Social: Uma noite de lançamento.', 'library', ['💻', '🚀', '👥'], ('Eduardo', 'Erica', 'tom', 'polly'),
  'Num alojamento da universidade, Eduardo e Erica resumem o que já fizeram até agora, como em A Rede Social.',
  vocab=[('📊', 'so far', 'até agora', 'Soa como “SÔU FÁR”.'), ('🔁', 'several times', 'várias vezes', 'Soa como “SÉ-vrâl TÁIMZ”.'), ('🚫', 'never', 'nunca', 'Soa como “NÉ-vâr”.'),
         ('🖊️', 'sign', 'assinar', 'Soa como “SÁIN”.'), ('🏆', 'achievement', 'conquista', 'Soa como “â-TCHÍV-mênt”.'), ('📈', 'career', 'carreira', 'Soa como “kâ-RÍR”.')],
  fill=[['Show me the numbers from this month.', 'Mostre os números deste mês.'], ['Signups grew every week.', 'As inscrições cresceram toda semana.'], ['Then the launch was a success.', 'Então o lançamento foi um sucesso.'], ['Let us celebrate with the team.', 'Vamos comemorar com a equipe.']])
O(7082050, 'Rocky', '🎬 Filme · 1976', 'Rocky é um filme de 1976 dirigido por John G. Avildsen, sobre um boxeador que treina com disciplina para uma grande luta. Combina com contar o que mudou nos seus hábitos de saúde.',
  'Rocky: Training at dawn.', 'Rocky: Treino ao amanhecer.', 'bakery', ['🥊', '🏃', '🥚'], ('Rocky', 'Adrian', 'tom', 'polly'),
  'Numa manhã de treino, Rocky e Adrian contam o que mudou nos hábitos dele, como em Rocky.',
  vocab=[('🥦', 'diet', 'dieta', 'Soa como “DÁI-et”.'), ('🍬', 'sugar', 'açúcar', 'Soa como “XÚ-gâr”.'), ('⚖️', 'kilo', 'quilo', 'Soa como “KÍ-lôu”.'),
         ('⚡', 'energy', 'energia', 'Soa como “É-nâr-dji”.'), ('🌅', 'morning', 'manhã', 'Soa como “MÓR-ning”.'), ('🏃', 'routine', 'rotina', 'Soa como “ru-TÍN”.')],
  fill=[['Did you sleep well last night?', 'Você dormiu bem ontem à noite?'], ['Yes, eight hours without waking up.', 'Sim, oito horas sem acordar.'], ['Keep that routine this week.', 'Mantenha essa rotina esta semana.'], ['I will, and stretch every morning.', 'Vou manter, e me alongar toda manhã.']])
O(7082052, 'Lost in Translation', '🎬 Filme · 2003', 'Lost in Translation é um filme de 2003 dirigido por Sofia Coppola, sobre dois americanos que se sentem deslocados em Tóquio e criam uma amizade. Combina com falar de saudade e adaptação a um lugar novo.',
  'Lost in Translation: Two strangers in Tokyo.', 'Encontros e Desencontros: Dois estranhos em Tóquio.', 'rainycafe', ['🗼', '🍸', '🌃'], ('Charlotte', 'Bob', 'polly', 'tom'),
  'Num bar de hotel, Charlotte e Bob falam de saudade e de se acostumar com o país, como em Encontros e Desencontros.',
  vocab=[('💭', 'miss', 'sentir falta', 'Soa como “MÍS”.'), ('👨‍👩‍👧', 'family', 'família', 'Soa como “FÉ-mâ-li”.'), ('🏡', 'feel at home', 'sentir-se em casa', 'Soa como “FÍL ét HÔUM”.'),
         ('🌍', 'country', 'país', 'Soa como “KÂN-tri”.'), ('🤗', 'kind', 'gentil', 'Soa como “KÁIND”.'), ('📞', 'call home', 'ligar para casa', 'Soa como “KÓL HÔUM”.')],
  fill=[['Which festival do people celebrate here?', 'Que festival as pessoas celebram aqui?'], ['The harvest fair in autumn.', 'A feira da colheita no outono.'], ['I would like to join the dancing.', 'Eu gostaria de participar da dança.'], ['Everyone is welcome.', 'Todos são bem-vindos.']])
O(7082053, 'Emma', '📚 Romance · 1815', 'Emma é um romance da escritora inglesa Jane Austen, publicado em 1815, cheio de conversas sobre casamentos, noivados e velhos conhecidos. Combina com falar de pessoas que você conhece há muito tempo.',
  'Emma: News of old friends.', 'Emma: Notícias de velhos amigos.', 'library', ['💌', '🏡', '💍'], ('Emma', 'Mr. Knightley', 'polly', 'tom'),
  'Numa sala do campo, Emma e o Sr. Knightley falam de velhos conhecidos, como em Emma.',
  vocab=[('🤝', 'in touch', 'em contato', 'Soa como “in TÂTCH”.'), ('👭', 'sister', 'irmã', 'Soa como “SÍS-târ”.'), ('👦', 'son', 'filho', 'Soa como “SÂN”.'),
         ('🌱', 'grow up', 'crescer', 'Soa como “GRÔU ÂP”.'), ('🗓️', 'ten years', 'dez anos', 'Soa como “TÉN IÍRZ”.'), ('📅', 'this week', 'esta semana', 'Soa como “DHÍS UÍK”.')],
  fill=[['Send her my love when you write.', 'Mande lembranças minhas quando escrever.'], ['I will. She misses everybody.', 'Mando. Ela sente falta de todo mundo.'], ['We should plan a family dinner.', 'Devíamos marcar um jantar em família.'], ['Yes, before the holidays.', 'Sim, antes das festas.']])
O(7930011, 'Billy Elliot', '🎬 Filme · 2000', 'Billy Elliot é um filme britânico de 2000 dirigido por Stephen Daldry, sobre um menino que sonha com a dança enquanto sua família enfrenta tempos difíceis. Combina com reagir a más notícias com empatia.',
  'Billy Elliot: Bad news at home.', 'Billy Elliot: Más notícias em casa.', 'rainycafe', ['🩰', '🏘️', '🤝'], ('Debbie', 'Billy', 'polly', 'tommy'),
  'Na rua de casa, Debbie ouve uma má notícia de Billy e reage com empatia, como em Billy Elliot.',
  vocab=[('😔', 'sorry', 'sinto muito', 'Soa como “SÓ-ri”.'), ('😢', 'terrible', 'terrível', 'Soa como “TÉ-ri-bl”.'), ('🤝', 'support', 'apoio', 'Soa como “sa-PÓRT”.'),
         ('💬', 'news', 'notícia', 'Soa como “NIÚZ”.'), ('🕊️', 'comfort', 'confortar', 'Soa como “KÂM-fârt”.'), ('🙏', 'be there', 'estar presente', 'Soa como “BI DHÉR”.')])

# ---- verbos próprios (sem repetir os do episódio vizinho)
F(82035, verbs=[('know', '🤝', 'conhecer', 'I have known her for years.', 'I know her for years.', 'I knew her at school.', 'Eu a conhecia da escola.', 'have **known** + for.'),
                ('stay', '🏨', 'ficar', 'How long have you stayed here?', 'How long you have stayed here?', 'I stayed a week.', 'Fiquei uma semana.', 'have **stayed**.'),
                ('wait', '⏳', 'esperar', 'I have waited since noon.', 'I wait since noon.', 'I waited an hour.', 'Esperei uma hora.', 'have **waited**.'),
                ('teach', '🍎', 'ensinar', 'She has taught here for years.', 'She has teached here for years.', 'I taught him.', 'Eu o ensinei.', 'teach → **taught**.')])
