from ext import A
def W(id,s):
    A(id,"\n".join("%s;%s;%s;%s"%tuple(x.split('|')) for x in s.strip().splitlines()))
W('A1-L068',"""morning coffee|café da manhã|Morning coffee.|Café da manhã.
empty desk|mesa vazia|An empty desk.|Uma mesa vazia.""")
W('A1-L069',"""coffee spoon|colher de café|A coffee spoon.|Uma colher de café.""")
W('A1-L072',"""teaching job|emprego de professor|A teaching job.|Um emprego de professor.
plane ticket|passagem aérea|A plane ticket.|Uma passagem aérea.
work visa|visto de trabalho|A work visa.|Um visto de trabalho.""")
W('A1-L078',"""bus route|linha de ônibus|A bus route.|Uma linha de ônibus.""")
W('A1-L089',"""trail run|corrida de trilha|A trail run.|Uma corrida de trilha.
running group|grupo de corrida|A running group.|Um grupo de corrida.""")
W('A1-L090',"""recipe book|livro de receitas|A recipe book.|Um livro de receitas.""")
W('A1-L091',"""weekend party|festa de fim de semana|A weekend party.|Uma festa de fim de semana.""")
W('A1-L092',"""learning app|aplicativo de aprendizado|A learning app.|Um aplicativo de aprendizado.""")
W('A1-L093',"""fast talker|quem fala rápido|A fast talker.|Quem fala rápido.""")
W('A1-L096',"""oven glove|luva de forno|An oven glove.|Uma luva de forno.""")
W('A2-L001',"""hotel breakfast|café do hotel|The hotel breakfast.|O café do hotel.
guided walk|caminhada guiada|A guided walk.|Uma caminhada guiada.
fresh fish|peixe fresco|Fresh fish.|Peixe fresco.
river walk|passeio à beira-rio|A river walk.|Um passeio à beira-rio.
old tram|bonde antigo|An old tram.|Um bonde antigo.
tiled house|casa de azulejos|A tiled house.|Uma casa de azulejos.
city viewpoint|mirante da cidade|A city viewpoint.|Um mirante da cidade.
guest book|livro de visitas|Sign the guest book.|Assine o livro de visitas.
tour bus|ônibus de turismo|A tour bus.|Um ônibus de turismo.
return trip|viagem de volta|A return trip.|Uma viagem de volta.
free map|mapa grátis|A free map.|Um mapa grátis.
welcome drink|bebida de boas-vindas|A welcome drink.|Uma bebida de boas-vindas.""")
W('A2-L002',"""camp stove|fogareiro|A camp stove.|Um fogareiro.
cooking pot|panela|A cooking pot.|Uma panela.
potato peel|casca de batata|A potato peel.|Uma casca de batata.
campfire smoke|fumaça da fogueira|Campfire smoke.|Fumaça da fogueira.
water bottle|garrafa de água|A water bottle.|Uma garrafa de água.
tent|barraca|A small tent.|Uma barraca pequena.
sleeping bag|saco de dormir|A sleeping bag.|Um saco de dormir.
wooden spoon|colher de pau|A wooden spoon.|Uma colher de pau.
dinner time|hora do jantar|Dinner time.|Hora do jantar.
trail mix|mix de castanhas|Trail mix.|Mix de castanhas.""")
W('A2-L003',"""travel plan|plano de viagem|A travel plan.|Um plano de viagem.
airport bus|ônibus do aeroporto|The airport bus.|O ônibus do aeroporto.
cheap flight|voo barato|A cheap flight.|Um voo barato.
window seat|assento na janela|A window seat.|Um assento na janela.
river view|vista para o rio|A river view.|Uma vista para o rio.
room key|chave do quarto|The room key.|A chave do quarto.
boarding gate|portão de embarque|The boarding gate.|O portão de embarque.
lost bag|mala perdida|A lost bag.|Uma mala perdida.
city map|mapa da cidade|A city map.|Um mapa da cidade.
best decision|melhor decisão|The best decision.|A melhor decisão.
long stay|estadia longa|A long stay.|Uma estadia longa.""")
W('A2-L004',"""hotel review|resenha de hotel|A hotel review.|Uma resenha de hotel.
front desk|recepção|At the front desk.|Na recepção.
sea view|vista para o mar|A sea view.|Uma vista para o mar.
room service|serviço de quarto|Room service.|Serviço de quarto.
breakfast buffet|buffet de café|A breakfast buffet.|Um buffet de café.
star rating|classificação por estrelas|A star rating.|Uma classificação por estrelas.
check-out time|hora de saída|Check-out time.|Hora de saída.
poor connection|conexão ruim|A poor connection.|Uma conexão ruim.""")
W('A2-L005',"""mountain trail|trilha de montanha|A mountain trail.|Uma trilha de montanha.
solo trip|viagem sozinho|A solo trip.|Uma viagem sozinho.
mountain hotel|hotel de montanha|A mountain hotel.|Um hotel de montanha.
quiet room|quarto silencioso|A quiet room.|Um quarto silencioso.
three nights|três noites|Three nights.|Três noites.
travel bag|bolsa de viagem|A travel bag.|Uma bolsa de viagem.
new friends|novos amigos|New friends.|Novos amigos.
free time|tempo livre|Free time.|Tempo livre.
sunrise walk|caminhada ao nascer do sol|A sunrise walk.|Uma caminhada ao nascer do sol.
booking form|formulário de reserva|A booking form.|Um formulário de reserva.""")
W('A2-L006',"""train station|estação de trem|The train station.|A estação de trem.
ticket machine|máquina de passagens|A ticket machine.|Uma máquina de passagens.
next train|próximo trem|The next train.|O próximo trem.
morning rush|correria da manhã|The morning rush.|A correria da manhã.
taxi ride|corrida de táxi|A taxi ride.|Uma corrida de táxi.
sweet pastry|doce de padaria|A sweet pastry.|Um doce de padaria.
train timetable|horário de trens|A train timetable.|Um horário de trens.
new plan|novo plano|A new plan.|Um novo plano.
check-out desk|balcão de saída|The check-out desk.|O balcão de saída.
silly mistake|erro bobo|A silly mistake.|Um erro bobo.""")
W('A2-L007',"""storm damage|danos da tempestade|Storm damage.|Danos da tempestade.
broken bridge|ponte quebrada|A broken bridge.|Uma ponte quebrada.
local business|comércio local|A local business.|Um comércio local.
repair work|obras de reparo|Repair work.|Obras de reparo.
tourist season|temporada turística|The tourist season.|A temporada turística.
research report|relatório de pesquisa|A research report.|Um relatório de pesquisa.
coastal town|cidade litorânea|A coastal town.|Uma cidade litorânea.
recovery plan|plano de recuperação|A recovery plan.|Um plano de recuperação.""")
W('A2-L008',"""week-long trip|viagem de uma semana|A week-long trip.|Uma viagem de uma semana.
roman ruins|ruínas romanas|Roman ruins.|Ruínas romanas.
pasta lunch|almoço de massa|A pasta lunch.|Um almoço de massa.
city walk|passeio pela cidade|A city walk.|Um passeio pela cidade.
guided tour|visita guiada|A guided tour.|Uma visita guiada.
tour guide|guia turístico|A tour guide.|Um guia turístico.
travel diary|diário de viagem|A travel diary.|Um diário de viagem.
hotel bill|conta do hotel|The hotel bill.|A conta do hotel.
souvenir shop|loja de lembranças|A souvenir shop.|Uma loja de lembranças.
train pass|passe de trem|A train pass.|Um passe de trem.
last day|último dia|The last day.|O último dia.""")
W('A2-L009',"""verb ending|terminação verbal|A verb ending.|Uma terminação verbal.
past tense|tempo passado|The past tense.|O tempo passado.
voiced sound|som sonoro|A voiced sound.|Um som sonoro.
voiceless sound|som surdo|A voiceless sound.|Um som surdo.
extra syllable|sílaba extra|An extra syllable.|Uma sílaba extra.
minimal pair|par mínimo|A minimal pair.|Um par mínimo.
pronunciation tip|dica de pronúncia|A pronunciation tip.|Uma dica de pronúncia.""")
W('A2-L010',"""small shop|loja pequena|A small shop.|Uma loja pequena.
shop owner|dono da loja|The shop owner.|O dono da loja.
straw hat|chapéu de palha|A straw hat.|Um chapéu de palha.
cash payment|pagamento em dinheiro|A cash payment.|Um pagamento em dinheiro.
thank-you note|bilhete de agradecimento|A thank-you note.|Um bilhete de agradecimento.
tourist group|grupo de turistas|A tourist group.|Um grupo de turistas.
quick visit|visita rápida|A quick visit.|Uma visita rápida.
shop window|vitrine|A shop window.|Uma vitrine.
fitting|prova de roupa|A fitting.|Uma prova de roupa.""")
W('A2-L011',"""pilot license|licença de piloto|A pilot license.|Uma licença de piloto.
flight school|escola de aviação|A flight school.|Uma escola de aviação.
flying lesson|aula de voo|A flying lesson.|Uma aula de voo.
regional airline|companhia aérea regional|A regional airline.|Uma companhia aérea regional.
long form|formulário longo|A long form.|Um formulário longo.
first flight|primeiro voo|Her first flight.|O primeiro voo dela.
night class|aula noturna|A night class.|Uma aula noturna.
airline job|emprego em companhia aérea|An airline job.|Um emprego em companhia aérea.
flight hours|horas de voo|Flight hours.|Horas de voo.""")
W('A2-L012',"""rainy day|dia chuvoso|A rainy day.|Um dia chuvoso.
wet umbrella|guarda-chuva molhado|A wet umbrella.|Um guarda-chuva molhado.
rain song|canção da chuva|A rain song.|Uma canção da chuva.
cold wind|vento frio|A cold wind.|Um vento frio.
open window|janela aberta|An open window.|Uma janela aberta.
evening walk|caminhada noturna|An evening walk.|Uma caminhada noturna.
poem line|verso|A poem line.|Um verso.
quiet street|rua calma|A quiet street.|Uma rua calma.
grey sky|céu cinza|A grey sky.|Um céu cinza.
soft rain|chuva fina|A soft rain.|Uma chuva fina.""")
W('A2-L013',"""birthday cake|bolo de aniversário|A birthday cake.|Um bolo de aniversário.
chocolate icing|cobertura de chocolate|Chocolate icing.|Cobertura de chocolate.
empty plate|prato vazio|An empty plate.|Um prato vazio.
guilty face|cara de culpado|A guilty face.|Uma cara de culpado.
cake crumbs|migalhas de bolo|Cake crumbs.|Migalhas de bolo.
family kitchen|cozinha da família|The family kitchen.|A cozinha da família.
big mystery|grande mistério|A big mystery.|Um grande mistério.
funny scene|cena engraçada|A funny scene.|Uma cena engraçada.
hungry dog|cachorro faminto|A hungry dog.|Um cachorro faminto.
grandmother|avó|My grandmother.|Minha avó.""")
W('A2-L018',"""shopping weekend|fim de semana de compras|A shopping weekend.|Um fim de semana de compras.
market square|praça do mercado|The market square.|A praça do mercado.
free garage|garagem grátis|A free garage.|Uma garagem grátis.
receipt|recibo|Show your receipt.|Mostre seu recibo.
ten percent off|dez por cento de desconto|Ten percent off.|Dez por cento de desconto.
shop sign|placa da loja|A shop sign.|Uma placa de loja.
price drop|queda de preço|A price drop.|Uma queda de preço.
parking spot|vaga de estacionamento|A parking spot.|Uma vaga de estacionamento.
last month|mês passado|Last month.|Mês passado.""")
W('A2-L022',"""lost wallet|carteira perdida|A lost wallet.|Uma carteira perdida.
market vendor|vendedor da feira|A market vendor.|Um vendedor da feira.
old man|senhor idoso|An old man.|Um senhor idoso.
forty dollars|quarenta dólares|Forty dollars.|Quarenta dólares.
family photo|foto de família|A family photo.|Uma foto de família.
bank card|cartão do banco|A bank card.|Um cartão do banco.
honest boy|menino honesto|An honest boy.|Um menino honesto.
sweet reward|recompensa doce|A sweet reward.|Uma recompensa doce.
market stall|barraca de feira|A market stall.|Uma barraca de feira.""")
W('A2-L023',"""power cut|falta de luz|A power cut.|Uma falta de luz.
dark street|rua escura|A dark street.|Uma rua escura.
fallen tree|árvore caída|A fallen tree.|Uma árvore caída.
candle light|luz de vela|Candle light.|Luz de vela.
board game|jogo de tabuleiro|A board game.|Um jogo de tabuleiro.
radio news|notícias do rádio|Radio news.|Notícias do rádio.
neighbors’ voices|vozes dos vizinhos|Neighbors’ voices.|Vozes dos vizinhos.
cold dinner|jantar frio|A cold dinner.|Um jantar frio.""")
W('A2-L034',"""bike accident|acidente de bicicleta|A bike accident.|Um acidente de bicicleta.
ankle pain|dor no tornozelo|Ankle pain.|Dor no tornozelo.
first aid|primeiros socorros|First aid.|Primeiros socorros.
borrowed phone|celular emprestado|A borrowed phone.|Um celular emprestado.
sharp crack|estalo seco|A sharp crack.|Um estalo seco.
running shoes|tênis de corrida|Running shoes.|Tênis de corrida.
park path|trilha do parque|A park path.|Uma trilha do parque.
wet leaves|folhas molhadas|Wet leaves.|Folhas molhadas.""")
W('A2-L035',"""healthy breakfast|café da manhã saudável|A healthy breakfast.|Um café da manhã saudável.
glass of water|copo de água|A glass of water.|Um copo de água.
daily walk|caminhada diária|A daily walk.|Uma caminhada diária.
clinic visit|visita à clínica|A clinic visit.|Uma visita à clínica.
simple remedy|remédio simples|A simple remedy.|Um remédio simples.
check-up day|dia de consulta|A check-up day.|Um dia de consulta.
stress relief|alívio do estresse|Stress relief.|Alívio do estresse.""")
W('A2-L042',"""gym day|dia de academia|A gym day.|Um dia de academia.
swim class|aula de natação|A swim class.|Uma aula de natação.
shopping trip|saída para compras|A shopping trip.|Uma saída para compras.
early return|volta cedo|An early return.|Uma volta cedo.
weekend trip|viagem de fim de semana|A weekend trip.|Uma viagem de fim de semana.""")
