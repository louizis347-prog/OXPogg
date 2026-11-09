from ext import A
def W(id,s):
    A(id,"\n".join("%s;%s;%s;%s"%tuple(x.split('|')) for x in s.strip().splitlines()))
W('A1-L090',"""family breakfast|café da manhã em família|A family breakfast.|Um café da manhã em família.""")
W('A1-L097',"""new lamp|abajur novo|A new lamp.|Um abajur novo.
blue shirt|camisa azul|A blue shirt.|Uma camisa azul.""")
W('A1-L103',"""pasta dinner|jantar de macarrão|A pasta dinner.|Um jantar de macarrão.
favorite hobby|hobby favorito|My favorite hobby.|Meu hobby favorito.""")
W('A1-L104',"""bank corner|esquina do banco|The bank corner.|A esquina do banco.
house number|número da casa|The house number.|O número da casa.
spare key|chave reserva|A spare key.|Uma chave reserva.
party address|endereço da festa|The party address.|O endereço da festa.
directions|indicações|Give directions.|Dê indicações.""")
W('A1-L105',"""film review|crítica de filme|A film review.|Uma crítica de filme.
football fan|torcedor de futebol|A football fan.|Um torcedor de futebol.
weekend plans|planos de fim de semana|Weekend plans.|Planos de fim de semana.
free evening|noite livre|A free evening.|Uma noite livre.
home cooking|comida caseira|Home cooking.|Comida caseira.
board game night|noite de jogos|A board game night.|Uma noite de jogos.""")
W('A1-L106',"""ride request|pedido de corrida|A ride request.|Um pedido de corrida.
luggage tag|etiqueta de bagagem|A luggage tag.|Uma etiqueta de bagagem.
early pickup|busca cedo|An early pickup.|Uma busca cedo.
phone number|telefone|My phone number.|Meu telefone.
airport gate|portão do aeroporto|An airport gate.|Um portão do aeroporto.
shared ride|corrida compartilhada|A shared ride.|Uma corrida compartilhada.""")
W('A1-L107',"""cake recipe|receita de bolo|A cake recipe.|Uma receita de bolo.
birthday party|festa de aniversário|A birthday party.|Uma festa de aniversário.
sugar bowl|açucareiro|A sugar bowl.|Um açucareiro.
cake stand|prato de bolo|A cake stand.|Um prato de bolo.
oven door|porta do forno|The oven door.|A porta do forno.
baking pan|assadeira|A baking pan.|Uma assadeira.""")
W('A1-L108',"""stress mark|marca de acento|A stress mark.|Uma marca de acento.
weekend rest|descanso de fim de semana|Weekend rest.|Descanso de fim de semana.
quiet walk|caminhada tranquila|A quiet walk.|Uma caminhada tranquila.
reading time|hora da leitura|Reading time.|Hora da leitura.
friend visit|visita de amigo|A friend visit.|Uma visita de amigo.
spend time|passar tempo|Spend time together.|Passem tempo juntos.""")
W('A1-L110',"""door color|cor da porta|The door color.|A cor da porta.
house paint|tinta de casa|House paint.|Tinta de casa.
street life|vida de rua|Street life.|Vida de rua.
tea party|chá com amigos|A tea party.|Um chá com amigos.
good neighbor|bom vizinho|A good neighbor.|Um bom vizinho.
warm light|luz aconchegante|Warm light.|Luz aconchegante.""")
W('A1-L111',"""shopping bag|sacola|A shopping bag.|Uma sacola.
new jacket|jaqueta nova|A new jacket.|Uma jaqueta nova.
small purchase|compra pequena|A small purchase.|Uma compra pequena.
spending limit|limite de gasto|A spending limit.|Um limite de gasto.
cash only|só dinheiro|Cash only.|Só dinheiro.
saving plan|plano de economia|A saving plan.|Um plano de economia.""")
W('A1-L112',"""class bag|bolsa da aula|A class bag.|Uma bolsa da aula.
note-taking|tomar notas|Note-taking helps.|Tomar notas ajuda.
study snack|lanche de estudo|A study snack.|Um lanche de estudo.
class dictionary|dicionário da turma|A class dictionary.|Um dicionário da turma.
learning tools|ferramentas de aprendizado|Learning tools.|Ferramentas de aprendizado.
student habits|hábitos dos alunos|Student habits.|Hábitos dos alunos.
confidence boost|reforço de confiança|A confidence boost.|Um reforço de confiança.""")
W('A1-L113',"""weather report|previsão do tempo|A weather report.|Uma previsão do tempo.
indoor plan|plano interno|An indoor plan.|Um plano interno.
reason why|razão pela qual|The reason why.|A razão pela qual.
final choice|escolha final|The final choice.|A escolha final.
cold rain|chuva fria|Cold rain.|Chuva fria.
movie at home|filme em casa|A movie at home.|Um filme em casa.""")
W('A2-L010',"""trip story|história de viagem|A trip story.|Uma história de viagem.
funny moment|momento engraçado|A funny moment.|Um momento engraçado.""")
W('A2-L012',"""rain poem|poema da chuva|A rain poem.|Um poema da chuva.
wet street|rua molhada|A wet street.|Uma rua molhada.""")
W('A2-L013',"""missing slice|fatia sumida|A missing slice.|Uma fatia sumida.
sweet tooth|gosto por doces|A sweet tooth.|Gosto por doces.""")
W('A2-L019',"""lemon cake|bolo de limão|A lemon cake.|Um bolo de limão.
cake batter|massa de bolo|Cake batter.|Massa de bolo.
oven mitts|luvas de forno|Oven mitts.|Luvas de forno.
measuring cup|copo medidor|A measuring cup.|Um copo medidor.
kitchen timer|timer de cozinha|A kitchen timer.|Um timer de cozinha.
baking disaster|desastre na cozinha|A baking disaster.|Um desastre na cozinha.""")
W('A2-L031',"""sale rush|correria da promoção|A sale rush.|Uma correria da promoção.""")
W('A2-L037',"""bad day|dia ruim|A bad day.|Um dia ruim.
bike ride|passeio de bicicleta|A bike ride.|Um passeio de bicicleta.
party invitation|convite de festa|A party invitation.|Um convite de festa.
sore knee|joelho dolorido|A sore knee.|Um joelho dolorido.
lost phone|celular perdido|A lost phone.|Um celular perdido.
bad luck|azar|Bad luck.|Azar.""")
W('A2-L044',"""health fair|feira de saúde|A health fair.|Uma feira de saúde.
blood pressure check|aferição de pressão|A blood pressure check.|Uma aferição de pressão.
healthy menu|cardápio saudável|A healthy menu.|Um cardápio saudável.
free screening|triagem grátis|A free screening.|Uma triagem grátis.
fair booth|estande da feira|A fair booth.|Um estande da feira.
flu season|temporada de gripe|Flu season.|Temporada de gripe.
health tip|dica de saúde|A health tip.|Uma dica de saúde.
medical team|equipe médica|A medical team.|Uma equipe médica.
waiting line|fila de espera|A waiting line.|Uma fila de espera.""")
W('A2-L045',"""medical conference|congresso médico|A medical conference.|Um congresso médico.
flight to Lima|voo para Lima|A flight to Lima.|Um voo para Lima.
conference talk|palestra do congresso|A conference talk.|Uma palestra do congresso.
nurse team|equipe de enfermeiros|A nurse team.|Uma equipe de enfermeiros.
vaccine shortage|falta de vacinas|A vaccine shortage.|Falta de vacinas.
clinic stock|estoque da clínica|Clinic stock.|Estoque da clínica.
short stay|estadia curta|A short stay.|Uma estadia curta.
travel bag|mala de viagem|A travel bag.|Uma mala de viagem.
hotel in Lima|hotel em Lima|A hotel in Lima.|Um hotel em Lima.
business trip|viagem de trabalho|A business trip.|Uma viagem de trabalho.
return flight|voo de volta|A return flight.|Um voo de volta.
medical supplies|material médico|Medical supplies.|Material médico.""")
W('A2-L046',"""weak vowel|vogal fraca|A weak vowel.|Uma vogal fraca.
soft sound|som suave|A soft sound.|Um som suave.
stress pattern|padrão de acento|A stress pattern.|Um padrão de acento.
spoken English|inglês falado|Spoken English.|Inglês falado.
syllable|sílaba|An unstressed syllable.|Uma sílaba átona.
mouth position|posição da boca|Mouth position.|Posição da boca.
sentence rhythm|ritmo da frase|Sentence rhythm.|Ritmo da frase.
pronunciation class|aula de pronúncia|A pronunciation class.|Uma aula de pronúncia.
dinner invitation|convite para jantar|A dinner invitation.|Um convite para jantar.
relaxed voice|voz relaxada|A relaxed voice.|Uma voz relaxada.""")
W('A2-L047',"""dental checkup|consulta no dentista|A dental checkup.|Uma consulta no dentista.
tooth filling|obturação|A tooth filling.|Uma obturação.
dentist chair|cadeira do dentista|The dentist chair.|A cadeira do dentista.
cinema ticket|ingresso de cinema|A cinema ticket.|Um ingresso de cinema.
film time|horário do filme|The film time.|O horário do filme.
evening plan|plano da noite|An evening plan.|Um plano da noite.
nervous patient|paciente nervoso|A nervous patient.|Um paciente nervoso.
friend’s birthday|aniversário do amigo|A friend’s birthday.|O aniversário do amigo.
popcorn bucket|balde de pipoca|A popcorn bucket.|Um balde de pipoca.
after work|depois do trabalho|After work.|Depois do trabalho.
Friday night plans|planos de sexta à noite|Friday night plans.|Planos de sexta à noite.
weekend film|filme de fim de semana|A weekend film.|Um filme de fim de semana.""")
W('A2-L050',"""patient list|lista de pacientes|The patient list.|A lista de pacientes.
clinic schedule|agenda da clínica|The clinic schedule.|A agenda da clínica.
first visit|primeira consulta|A first visit.|Uma primeira consulta.
nurse office|sala da enfermeira|The nurse office.|A sala da enfermeira.
short checkup|consulta rápida|A short checkup.|Uma consulta rápida.
morning slot|horário da manhã|A morning slot.|Um horário da manhã.
medical advice|conselho médico|Medical advice.|Conselho médico.
calm patient|paciente calmo|A calm patient.|Um paciente calmo.
early arrival|chegada antecipada|An early arrival.|Uma chegada antecipada.
appointment card|cartão de consulta|An appointment card.|Um cartão de consulta.
reception|recepção|The reception.|A recepção.
clinic door|porta da clínica|The clinic door.|A porta da clínica.""")
W('A2-L051',"""backpacking trip|viagem de mochila|A backpacking trip.|Uma viagem de mochila.
first journey|primeira viagem|A first journey.|Uma primeira viagem.
host family|família anfitriã|A host family.|Uma família anfitriã.
village life|vida na vila|Village life.|Vida na vila.
mountain village|vila de montanha|A mountain village.|Uma vila de montanha.
travel story|história de viagem|A travel story.|Uma história de viagem.
lost camera|câmera perdida|A lost camera.|Uma câmera perdida.
storm warning|alerta de tempestade|A storm warning.|Um alerta de tempestade.
early start|saída cedo|An early start.|Uma saída cedo.
travel memory|lembrança de viagem|A travel memory.|Uma lembrança de viagem.
small backpack|mochila pequena|A small backpack.|Uma mochila pequena.
local guide|guia local|A local guide.|Um guia local.""")
W('A2-L052',"""park party|festa no parque|A park party.|Uma festa no parque.
picnic blanket|manta de piquenique|A picnic blanket.|Uma manta de piquenique.
live music|música ao vivo|Live music.|Música ao vivo.
snack table|mesa de petiscos|A snack table.|Uma mesa de petiscos.
cold drinks|bebidas geladas|Cold drinks.|Bebidas geladas.
start time|horário de início|The start time.|O horário de início.
bring a friend|traga um amigo|Bring a friend.|Traga um amigo.
free seat|lugar livre|A free seat.|Um lugar livre.
sunny afternoon|tarde ensolarada|A sunny afternoon.|Uma tarde ensolarada.
weekend meetup|encontro de fim de semana|A weekend meetup.|Um encontro de fim de semana.
open air|ar livre|An open-air party.|Uma festa ao ar livre.
guitar music|música de violão|Guitar music.|Música de violão.""")
W('A2-L053',"""onion soup|sopa de cebola|Onion soup.|Sopa de cebola.
chicken soup|sopa de galinha|Chicken soup.|Sopa de galinha.
soup spoon|colher de sopa|A soup spoon.|Uma colher de sopa.
big pot|panela grande|A big pot.|Uma panela grande.
sliced onion|cebola fatiada|Sliced onion.|Cebola fatiada.
boiling water|água fervente|Boiling water.|Água fervente.
family recipe|receita de família|A family recipe.|Uma receita de família.
cold day|dia frio|A cold day.|Um dia frio.
cooking steps|passos da receita|Cooking steps.|Passos da receita.
taste test|prova de sabor|A taste test.|Uma prova de sabor.
hot bowl|tigela quente|A hot bowl.|Uma tigela quente.
kitchen helper|ajudante de cozinha|A kitchen helper.|Um ajudante de cozinha.""")
W('A2-L054',"""city comparison|comparação de cidades|A city comparison.|Uma comparação de cidades.
old town|cidade antiga|The old town.|A cidade antiga.
high altitude|altitude elevada|High altitude.|Altitude elevada.
local food|comida local|Local food.|Comida local.
warm coat|casaco quente|A warm coat.|Um casaco quente.
hotel price|preço de hotel|The hotel price.|O preço do hotel.
travel blog|blog de viagem|A travel blog.|Um blog de viagem.
friendly people|pessoas simpáticas|Friendly people.|Pessoas simpáticas.
city size|tamanho da cidade|City size.|Tamanho da cidade.
street food|comida de rua|Street food.|Comida de rua.
cold nights|noites frias|Cold nights.|Noites frias.
big market|mercado grande|A big market.|Um mercado grande.""")
W('A2-L055',"""trek backpack|mochila de trilha|A trek backpack.|Uma mochila de trilha.
city bag|bolsa urbana|A city bag.|Uma bolsa urbana.
padded strap|alça acolchoada|A padded strap.|Uma alça acolchoada.
waterproof cover|capa impermeável|A waterproof cover.|Uma capa impermeável.
long trip|viagem longa|A long trip.|Uma viagem longa.
light weight|peso leve|Light weight.|Peso leve.
zipper pocket|bolso com zíper|A zipper pocket.|Um bolso com zíper.
product review|resenha de produto|A product review.|Uma resenha de produto.
old bag|bolsa velha|An old bag.|Uma bolsa velha.
store price|preço da loja|The store price.|O preço da loja.
mountain trip|viagem à montanha|A mountain trip.|Uma viagem à montanha.
carry weight|peso carregado|Carry weight.|Peso carregado.""")
W('A2-L056',"""short road|estrada curta|A short road.|Uma estrada curta.
long road|estrada longa|A long road.|Uma estrada longa.
green hills|colinas verdes|Green hills.|Colinas verdes.
fast walker|caminhante rápido|A fast walker.|Um caminhante rápido.
happy ending|final feliz|A happy ending.|Um final feliz.
road trip|viagem de carro|A road trip.|Uma viagem de carro.
brother’s road|caminho do irmão|His brother’s road.|O caminho do irmão dele.
side path|caminho lateral|A side path.|Um caminho lateral.
wild flowers|flores silvestres|Wild flowers.|Flores silvestres.
river bank|margem do rio|The river bank.|A margem do rio.
tree shade|sombra de árvore|Tree shade.|Sombra de árvore.
kind words|palavras gentis|Kind words.|Palavras gentis.
sunset road|estrada ao pôr do sol|A sunset road.|Uma estrada ao pôr do sol.
life lesson|lição de vida|A life lesson.|Uma lição de vida.""")
W('A2-L057',"""old street|rua antiga|An old street.|Uma rua antiga.
thank-you card|cartão de agradecimento|A thank-you card.|Um cartão de agradecimento.
young years|anos de juventude|Young years.|Anos de juventude.
place to sleep|lugar para dormir|A place to sleep.|Um lugar para dormir.
helping hand|mão amiga|A helping hand.|Uma mão amiga.
good deed|boa ação|A good deed.|Uma boa ação.
community help|ajuda comunitária|Community help.|Ajuda comunitária.
old friend|velho amigo|An old friend.|Um velho amigo.
small gift|presente pequeno|A small gift.|Um presente pequeno.
free time|tempo livre|Free time.|Tempo livre.
kindness|bondade|Simple kindness.|Bondade simples.
sharing|compartilhar|Sharing is good.|Compartilhar é bom.""")
W('A2-L058',"""world record|recorde mundial|A world record.|Um recorde mundial.
tall building|prédio alto|A tall building.|Um prédio alto.
long river|rio longo|A long river.|Um rio longo.
big desert|deserto grande|A big desert.|Um deserto grande.
popular sport|esporte popular|A popular sport.|Um esporte popular.
safe city|cidade segura|A safe city.|Uma cidade segura.
best food|melhor comida|The best food.|A melhor comida.
survey results|resultados da pesquisa|Survey results.|Resultados da pesquisa.
city ranking|ranking de cidades|A city ranking.|Um ranking de cidades.
fact sheet|ficha de dados|A fact sheet.|Uma ficha de dados.
beautiful park|parque bonito|A beautiful park.|Um parque bonito.
deep ocean|oceano profundo|A deep ocean.|Um oceano profundo.
high mountain|montanha alta|A high mountain.|Uma montanha alta.""")
W('A2-L059',"""trip award|prêmio da viagem|A trip award.|Um prêmio da viagem.
best view|melhor vista|The best view.|A melhor vista.
worst weather|pior clima|The worst weather.|O pior clima.
tasty meal|refeição saborosa|A tasty meal.|Uma refeição saborosa.
free upgrade|melhoria grátis|A free upgrade.|Uma melhoria grátis.
mountain top|topo da montanha|The mountain top.|O topo da montanha.
cold day|dia frio|A cold day.|Um dia frio.
grandma’s soup|sopa da vovó|Grandma’s soup.|A sopa da vovó.
big surprise|grande surpresa|A big surprise.|Uma grande surpresa.
trip highlight|destaque da viagem|A trip highlight.|Um destaque da viagem.
favorite day|dia favorito|My favorite day.|Meu dia favorito.
hotel room|quarto de hotel|A hotel room.|Um quarto de hotel.
travel photos|fotos de viagem|Travel photos.|Fotos de viagem.
group trip|viagem em grupo|A group trip.|Uma viagem em grupo.""")
W('A2-L060',"""storm of the decade|tempestade da década|The storm of the decade.|A tempestade da década.
patient teacher|professor paciente|A patient teacher.|Um professor paciente.
cheap option|opção barata|A cheap option.|Uma opção barata.
trip of a lifetime|viagem de uma vida|A trip of a lifetime.|Uma viagem de uma vida.
best result|melhor resultado|The best result.|O melhor resultado.
worst case|pior caso|The worst case.|O pior caso.
high point|ponto alto|The high point.|O ponto alto.
by far|de longe|By far the best.|De longe o melhor.
speaking class|aula de conversação|A speaking class.|Uma aula de conversação.
extreme weather|clima extremo|Extreme weather.|Clima extremo.
life choice|escolha de vida|A life choice.|Uma escolha de vida.
lecture hall|auditório|A lecture hall.|Um auditório.
note-taking|anotações|Note-taking skills.|Habilidades de anotação.""")
W('A2-L061',"""parents’ meeting|reunião de pais|A parents’ meeting.|Uma reunião de pais.
school visit|visita à escola|A school visit.|Uma visita à escola.
family night|noite em família|A family night.|Uma noite em família.
monthly class|aula mensal|A monthly class.|Uma aula mensal.
school hall|salão da escola|The school hall.|O salão da escola.
map reading|leitura de mapa|Map reading.|Leitura de mapa.
English class|aula de inglês|An English class.|Uma aula de inglês.
local school|escola local|A local school.|Uma escola local.
volunteer parent|pai voluntário|A volunteer parent.|Um pai voluntário.
school plan|plano da escola|A school plan.|Um plano da escola.
classroom door|porta da sala|The classroom door.|A porta da sala.
mayor’s help|ajuda do prefeito|The mayor’s help.|A ajuda do prefeito.
term report|boletim do período|A term report.|Um boletim do período.
open class|aula aberta|An open class.|Uma aula aberta.""")
W('A2-L062',"""pack list|lista de bagagem|A pack list.|Uma lista de bagagem.
travel rule|regra de viagem|A travel rule.|Uma regra de viagem.
daily medicine|remédio diário|Daily medicine.|Remédio diário.
sea trip|viagem ao mar|A sea trip.|Uma viagem ao mar.
summer trip|viagem de verão|A summer trip.|Uma viagem de verão.
light suitcase|mala leve|A light suitcase.|Uma mala leve.
old traveler|viajante experiente|An old traveler.|Um viajante experiente.
travel advice|conselho de viagem|Travel advice.|Conselho de viagem.
passport check|conferência de passaporte|A passport check.|Uma conferência de passaporte.
carry-on bag|bagagem de mão|A carry-on bag.|Uma bagagem de mão.
retired teacher|professor aposentado|A retired teacher.|Um professor aposentado.
sea breeze|brisa do mar|A sea breeze.|Uma brisa do mar.
age 70|aos 70 anos|At age 70.|Aos 70 anos.""")
W('A2-L063',"""morning train|trem da manhã|A morning train.|Um trem da manhã.
plan for today|plano para hoje|A plan for today.|Um plano para hoje.
friend’s hello|olá do amigo|A friend’s hello.|O olá do amigo.
bill payment|pagamento de conta|Bill payment.|Pagamento de conta.
final page|última página|The final page.|A última página.
goodbye wave|aceno de adeus|A goodbye wave.|Um aceno de adeus.
daily poem|poema do dia|A daily poem.|Um poema do dia.
platform clock|relógio da plataforma|A platform clock.|Um relógio da plataforma.
quick run|corrida rápida|A quick run.|Uma corrida rápida.
bright smile|sorriso brilhante|A bright smile.|Um sorriso brilhante.
short rhyme|rima curta|A short rhyme.|Uma rima curta.
meeting a friend|encontrar um amigo|Meeting a friend.|Encontrar um amigo.
ticket line|fila de bilhetes|A ticket line.|Uma fila de bilhetes.
busy morning|manhã agitada|A busy morning.|Uma manhã agitada.""")
W('A2-L064',"""coat return|devolução do casaco|A coat return.|Uma devolução de casaco.
lost receipt|recibo perdido|A lost receipt.|Um recibo perdido.
store policy|política da loja|A store policy.|Uma política da loja.
old boxes|caixas velhas|Old boxes.|Caixas velhas.
exchange desk|balcão de trocas|An exchange desk.|Um balcão de trocas.
return window|prazo de devolução|The return window.|O prazo de devolução.
warm coat|casaco quente|A warm coat.|Um casaco quente.
shop clerk|atendente da loja|A shop clerk.|Um atendente da loja.
winter clothes|roupas de inverno|Winter clothes.|Roupas de inverno.
funny strip|tirinha engraçada|A funny strip.|Uma tirinha engraçada.
unused item|item não usado|An unused item.|Um item não usado.
store credit|crédito da loja|Store credit.|Crédito da loja.
clothes closet|armário de roupas|A clothes closet.|Um armário de roupas.""")
