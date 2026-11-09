from ext import A
def W(id,s):
    A(id,"\n".join("%s;%s;%s;%s"%tuple(x.split('|')) for x in s.strip().splitlines()))
W('A1-L073',"""turkey sandwich|sanduíche de peru|A turkey sandwich.|Um sanduíche de peru.
sandwich bread|pão de forma|Sandwich bread is soft.|O pão de forma é macio.
cheese slice|fatia de queijo|A cheese slice.|Uma fatia de queijo.
lunch bag|lancheira|A paper lunch bag.|Uma lancheira de papel.
bread knife|faca de pão|Use a bread knife.|Use uma faca de pão.
sliced tomato|tomate fatiado|Sliced tomato.|Tomate fatiado.
pickle|picles|A pickle slice.|Uma fatia de picles.
olive oil|azeite|A drop of olive oil.|Uma gota de azeite.
toasted|tostado|Toasted bread.|Pão tostado.
filling|recheio|A tasty filling.|Um recheio saboroso.
crust|casca do pão|Cut off the crust.|Corte a casca.
lunch break|pausa para o almoço|A lunch break.|Uma pausa para o almoço.""")
W('A1-L074',"""arrival time|hora de chegada|My arrival time.|Minha hora de chegada.
start time|hora de início|The start time.|A hora de início.
office hours|horário de expediente|Office hours are nine to five.|O expediente é das nove às cinco.
team meeting|reunião de equipe|A team meeting.|Uma reunião de equipe.
work email|e-mail de trabalho|A work email.|Um e-mail de trabalho.
boss’s office|sala do chefe|The boss’s office.|A sala do chefe.
coffee break|pausa para o café|A coffee break.|Uma pausa para o café.
work phone|telefone do trabalho|A work phone.|Um telefone do trabalho.
clear instructions|instruções claras|Give clear instructions.|Dê instruções claras.
new colleague|novo colega|A new colleague.|Um novo colega.
speak up|falar mais alto|Speak up in meetings.|Fale mais alto nas reuniões.""")
W('A1-L075',"""card message|mensagem do cartão|Write a card message.|Escreva a mensagem do cartão.
group gift|presente coletivo|A group gift.|Um presente coletivo.
price list|lista de preços|The price list.|A lista de preços.
birthday cake|bolo de aniversário|A birthday cake.|Um bolo de aniversário.
candles|velas|Blow out the candles.|Sopre as velas.
team spirit|espírito de equipe|Good team spirit.|Bom espírito de equipe.
fun fact|curiosidade|A fun fact.|Uma curiosidade.
gift wrap|embrulho|Colorful gift wrap.|Embrulho colorido.
secret friend|amigo secreto|A secret friend game.|Um amigo secreto.
shopping list|lista de compras|A shopping list.|Uma lista de compras.
delivery|entrega|A fast delivery.|Uma entrega rápida.""")
W('A1-L076',"""top drawer|gaveta de cima|The top drawer.|A gaveta de cima.
desk drawer|gaveta da mesa|A desk drawer.|Uma gaveta da mesa.
under the desk|embaixo da mesa|Look under the desk.|Olhe embaixo da mesa.
behind the lamp|atrás do abajur|Behind the lamp.|Atrás do abajur.
between the books|entre os livros|Between the books.|Entre os livros.
next to the printer|ao lado da impressora|Next to the printer.|Ao lado da impressora.
on top of|em cima de|On top of the cabinet.|Em cima do armário.
in front of|na frente de|In front of the door.|Na frente da porta.
opposite|em frente a|Opposite the window.|Em frente à janela.
lost and found|achados e perdidos|The lost and found.|Os achados e perdidos.
paperwork|papelada|Lost paperwork.|Papelada perdida.
big folder|pasta grande|A big folder.|Uma pasta grande.""")
W('A1-L077',"""study spot|lugar de estudo|A quiet study spot.|Um lugar de estudo silencioso.
library table|mesa de biblioteca|A library table.|Uma mesa de biblioteca.
quiet room|sala silenciosa|A quiet room.|Uma sala silenciosa.
study desk|escrivaninha|A study desk.|Uma escrivaninha.
noise-free|sem barulho|A noise-free place.|Um lugar sem barulho.
good light|boa iluminação|Good light helps.|Boa iluminação ajuda.
bus ride|viagem de ônibus|A short bus ride.|Uma viagem curta de ônibus.
study habits|hábitos de estudo|Good study habits.|Bons hábitos de estudo.
bookshelf|estante|A tall bookshelf.|Uma estante alta.
reading corner|cantinho de leitura|A reading corner.|Um cantinho de leitura.
outdoors|ao ar livre|Study outdoors.|Estude ao ar livre.
campus café|cafeteria do campus|The campus café.|A cafeteria do campus.
group table|mesa de grupo|A group table.|Uma mesa de grupo.
Wi-Fi password|senha do Wi-Fi|The Wi-Fi password.|A senha do Wi-Fi.""")
W('A1-L078',"""bus pass|passe de ônibus|A bus pass.|Um passe de ônibus.
bike lane|ciclovia|Use the bike lane.|Use a ciclovia.
subway ride|viagem de metrô|A subway ride.|Uma viagem de metrô.
commute time|tempo de trajeto|A short commute time.|Um tempo de trajeto curto.
cheap fare|tarifa barata|A cheap fare.|Uma tarifa barata.
on foot|a pé|Go on foot.|Vá a pé.
survey result|resultado da pesquisa|The survey result.|O resultado da pesquisa.
most workers|a maioria dos trabalhadores|Most workers take the bus.|A maioria dos trabalhadores pega ônibus.
in rush hour|na hora do rush|Travel in rush hour.|Viaje na hora do rush.
researcher|pesquisador|A survey researcher.|Um pesquisador.""")
W('A1-L079',"""front door|porta da frente|The front door.|A porta da frente.
back door|porta dos fundos|The back door.|A porta dos fundos.
stairwell|escada interna|The stairwell.|A escada interna.
first floor|primeiro andar|On the first floor.|No primeiro andar.
second floor|segundo andar|On the second floor.|No segundo andar.
ground floor|térreo|The ground floor.|O térreo.
meeting room|sala de reunião|A meeting room.|Uma sala de reunião.
restroom sign|placa do banheiro|The restroom sign.|A placa do banheiro.
fire alarm|alarme de incêndio|A fire alarm.|Um alarme de incêndio.
visitor badge|crachá de visitante|A visitor badge.|Um crachá de visitante.
office map|mapa do escritório|The office map.|O mapa do escritório.""")
W('A1-L080',"""weekly goal|meta semanal|A weekly goal.|Uma meta semanal.
alarm clock|despertador|Set the alarm clock.|Regule o despertador.
daily plan|plano diário|A daily plan.|Um plano diário.
to-do list|lista de tarefas|A to-do list.|Uma lista de tarefas.
sleep schedule|rotina de sono|A sleep schedule.|Uma rotina de sono.
study time|hora de estudo|Set study time.|Defina a hora de estudo.
rest day|dia de descanso|A rest day.|Um dia de descanso.
workout plan|plano de treino|A workout plan.|Um plano de treino.
time block|bloco de tempo|A time block.|Um bloco de tempo.
phone alarm|alarme do celular|A phone alarm.|Um alarme do celular.
phone timer|temporizador do celular|A phone timer.|Um temporizador do celular.""")
W('A1-L081',"""weekend hours|horário de fim de semana|Weekend hours are short.|O horário de fim de semana é curto.
holiday hours|horário de feriado|Holiday hours.|Horário de feriado.
service desk|balcão de atendimento|The service desk.|O balcão de atendimento.
new schedule|novo horário|A new schedule.|Um novo horário.
public office|repartição pública|A public office.|Uma repartição pública.
mayor’s office|gabinete do prefeito|The mayor’s office.|O gabinete do prefeito.
open to the public|aberto ao público|Open to the public.|Aberto ao público.
closed on Sundays|fechado aos domingos|Closed on Sundays.|Fechado aos domingos.
from nine to four|das nove às quatro|From nine to four.|Das nove às quatro.
starting in May|a partir de maio|Starting in May.|A partir de maio.
effective date|data de início|The effective date.|A data de início.""")
W('A1-L084',"""soccer coach|treinador de futebol|A soccer coach.|Um treinador de futebol.
tennis court|quadra de tênis|A tennis court.|Uma quadra de tênis.
training session|sessão de treino|A training session.|Uma sessão de treino.
season opener|abertura da temporada|The season opener.|A abertura da temporada.
home game|jogo em casa|A home game.|Um jogo em casa.
away game|jogo fora|An away game.|Um jogo fora.
final match|final|The final match.|A final.
team captain|capitão do time|The team captain.|O capitão do time.
sports bag|bolsa de esportes|A sports bag.|Uma bolsa de esportes.
fitness level|nível de condicionamento|A high fitness level.|Um nível alto de condicionamento.
injury|lesão|A knee injury.|Uma lesão no joelho.
cup final|final de copa|The cup final.|A final de copa.""")
W('A1-L085',"""spring flowers|flores de primavera|Spring flowers.|Flores de primavera.
morning dew|orvalho da manhã|Morning dew.|Orvalho da manhã.
cherry blossom|flor de cerejeira|A cherry blossom.|Uma flor de cerejeira.
gentle breeze|brisa suave|A gentle breeze.|Uma brisa suave.
quiet pond|lagoa calma|A quiet pond.|Uma lagoa calma.
falling leaves|folhas caindo|Falling leaves.|Folhas caindo.
first frost|primeira geada|The first frost.|A primeira geada.
winter moon|lua de inverno|The winter moon.|A lua de inverno.
summer rain|chuva de verão|A summer rain.|Uma chuva de verão.
autumn wind|vento de outono|The autumn wind.|O vento de outono.
sunset glow|brilho do pôr do sol|A sunset glow.|Um brilho do pôr do sol.
haiku|haiku|Write a haiku.|Escreva um haiku.
seasonal|sazonal|Seasonal change.|Mudança sazonal.""")
W('A1-L086',"""breakfast plate|prato de café da manhã|A breakfast plate.|Um prato de café da manhã.
breakfast table|mesa do café|The breakfast table.|A mesa do café.
fried egg|ovo frito|A fried egg.|Um ovo frito.
orange juice|suco de laranja|Orange juice.|Suco de laranja.
butter knife|faca de manteiga|A butter knife.|Uma faca de manteiga.
maple syrup|calda de bordo|Maple syrup.|Calda de bordo.
missing bacon|bacon sumido|The missing bacon.|O bacon sumido.
dog’s plate|prato do cachorro|The dog’s plate.|O prato do cachorro.
my own|meu próprio|My own plate.|Meu próprio prato.""")
W('A1-L087',"""party invitation|convite de festa|A party invitation.|Um convite de festa.
party snacks|petiscos de festa|Party snacks.|Petiscos de festa.
dance music|música de dança|Dance music.|Música de dança.
house party|festa em casa|A house party.|Uma festa em casa.
board games|jogos de tabuleiro|Play board games.|Jogue jogos de tabuleiro.
new game|jogo novo|A new game.|Um jogo novo.
Friday night|sexta à noite|On Friday night.|Na sexta à noite.
text message|mensagem de texto|A text message.|Uma mensagem de texto.
meeting point|ponto de encontro|The meeting point.|O ponto de encontro.
bring a friend|traga um amigo|Bring a friend.|Traga um amigo.
RSVP|confirmar presença|Please RSVP.|Confirme presença.
guest list|lista de convidados|The guest list.|A lista de convidados.""")
W('A1-L088',"""school bag|mochila escolar|A school bag.|Uma mochila escolar.
class books|livros da turma|The class books.|Os livros da turma.
homework folder|pasta de lição|A homework folder.|Uma pasta de lição.
whiteboard|quadro branco|Write on the whiteboard.|Escreva no quadro branco.
test paper|prova|A test paper.|Uma prova.
student desk|carteira|A student desk.|Uma carteira escolar.
teacher’s desk|mesa do professor|The teacher’s desk.|A mesa do professor.
free period|aula vaga|A free period.|Uma aula vaga.
class trip|passeio escolar|A class trip.|Um passeio escolar.
school day|dia de aula|A long school day.|Um dia de aula longo.
lesson plan|plano de aula|A lesson plan.|Um plano de aula.
students’ work|trabalho dos alunos|The students’ work.|O trabalho dos alunos.
our class|nossa turma|Our class is happy.|Nossa turma é feliz.""")
W('A1-L089',"""running shoes|tênis de corrida|New running shoes.|Tênis de corrida novos.
race day|dia da corrida|Race day is Saturday.|O dia da corrida é sábado.
finish line|linha de chegada|The finish line.|A linha de chegada.
water bottle|garrafa de água|A water bottle.|Uma garrafa de água.
running club|clube de corrida|A running club.|Um clube de corrida.
first month|primeiro mês|The first month.|O primeiro mês.
club member|sócio do clube|A club member.|Um sócio do clube.
sign up|inscrever-se|Sign up today.|Inscreva-se hoje.
coffee after|café depois|Coffee after the run.|Café depois da corrida.
group run|corrida em grupo|A group run.|Uma corrida em grupo.
five kilometers|cinco quilômetros|Five kilometers.|Cinco quilômetros.""")
W('A1-L090',"""pancake mix|mistura para panqueca|Pancake mix.|Mistura para panqueca.
family recipe|receita de família|A family recipe.|Uma receita de família.
mixing bowl|tigela de mistura|A big mixing bowl.|Uma tigela de mistura grande.
wooden spoon|colher de pau|A wooden spoon.|Uma colher de pau.
frying pan|frigideira|A hot frying pan.|Uma frigideira quente.
fresh fruit|fruta fresca|Fresh fruit.|Fruta fresca.
whipped cream|chantilly|Whipped cream.|Chantilly.
sunday breakfast|café de domingo|A Sunday breakfast.|Um café da manhã de domingo.
our table|nossa mesa|Our table.|Nossa mesa.
my share|minha parte|My share.|Minha parte.
happy morning|manhã feliz|A happy morning.|Uma manhã feliz.
cooking together|cozinhar juntos|Cooking together.|Cozinhar juntos.""")
W('A1-L091',"""weekend plans|planos de fim de semana|Weekend plans.|Planos de fim de semana.
football game|jogo de futebol|A football game.|Um jogo de futebol.
phone call|ligação|A phone call.|Uma ligação.
guitar lesson|aula de violão|A guitar lesson.|Uma aula de violão.
best friend|melhor amigo|My best friend.|Meu melhor amigo.
park bench|banco do parque|A park bench.|Um banco do parque.
picnic basket|cesta de piquenique|A picnic basket.|Uma cesta de piquenique.
see you soon|até breve|See you soon!|Até breve!
call me|ligue para mim|Call me later.|Ligue para mim depois.
with them|com eles|Come with them.|Venha com eles.
tell her|conte a ela|Tell her the news.|Conte a ela a novidade.
love him|amá-lo|We love him.|Nós o amamos.""")
W('A1-L092',"""study app|aplicativo de estudo|A study app.|Um aplicativo de estudo.
free trial|teste grátis|A free trial.|Um teste grátis.
daily lesson|lição diária|A daily lesson.|Uma lição diária.
word game|jogo de palavras|A word game.|Um jogo de palavras.
progress bar|barra de progresso|The progress bar.|A barra de progresso.
download|baixar|Download the app.|Baixe o aplicativo.
subscription|assinatura|A monthly subscription.|Uma assinatura mensal.
star rating|nota em estrelas|A five-star rating.|Uma nota de cinco estrelas.
user|usuário|A new user.|Um novo usuário.
screen time|tempo de tela|Less screen time.|Menos tempo de tela.
push notification|notificação|A push notification.|Uma notificação.
review|avaliação|Write a review.|Escreva uma avaliação.""")
W('A1-L093',"""after school|depois da aula|After school.|Depois da aula.
before dinner|antes do jantar|Before dinner.|Antes do jantar.
snack time|hora do lanche|It is snack time.|É hora do lanche.
dinner table|mesa de jantar|At the dinner table.|À mesa de jantar.
kitchen sink|pia da cozinha|The kitchen sink.|A pia da cozinha.
dish soap|detergente|Dish soap.|Detergente.
clean plate|prato limpo|A clean plate.|Um prato limpo.
mother’s voice|voz da mãe|Mother’s voice.|A voz da mãe.
fast speech|fala rápida|Fast speech.|Fala rápida.
sounds like|soa como|It sounds like “juh”.|Soa como “juh”.
homework time|hora da lição|Homework time.|Hora da lição de casa.""")
W('A1-L094',"""older people|pessoas idosas|Help older people.|Ajude pessoas idosas.
bus stop|ponto de ônibus|At the bus stop.|No ponto de ônibus.
a warm hello|um olá caloroso|A warm hello.|Um olá caloroso.
small act|pequeno gesto|A small act of kindness.|Um pequeno gesto de bondade.
lost senior|idoso perdido|A lost senior.|Um idoso perdido.
walk with|caminhar com|Walk with them.|Caminhe com eles.
help line|linha de ajuda|A help line.|Uma linha de ajuda.
neighbor’s door|porta do vizinho|A neighbor’s door.|A porta do vizinho.
town square|praça da cidade|The town square.|A praça da cidade.
offer help|oferecer ajuda|Offer help.|Ofereça ajuda.
community|comunidade|A caring community.|Uma comunidade atenciosa.""")
W('A1-L095',"""red car|carro vermelho|A red car.|Um carro vermelho.
big house|casa grande|A big house.|Uma casa grande.
nice new phone|celular novo e legal|A nice new phone.|Um celular novo e legal.
small round table|mesa redonda pequena|A small round table.|Uma mesa redonda pequena.
old wooden chair|cadeira velha de madeira|An old wooden chair.|Uma cadeira velha de madeira.
long black coat|casaco preto longo|A long black coat.|Um casaco preto longo.
beautiful old house|bela casa antiga|A beautiful old house.|Uma bela casa antiga.
opinion adjective|adjetivo de opinião|An opinion adjective.|Um adjetivo de opinião.
size adjective|adjetivo de tamanho|A size adjective.|Um adjetivo de tamanho.
color adjective|adjetivo de cor|A color adjective.|Um adjetivo de cor.
word order|ordem das palavras|English word order.|Ordem das palavras em inglês.
description|descrição|A clear description.|Uma descrição clara.""")
W('A1-L096',"""hot pan|panela quente|A hot pan.|Uma panela quente.
oven cloth|pano de forno|An oven cloth.|Um pano de forno.
hold tight|segurar firme|Hold tight.|Segure firme.
with both hands|com as duas mãos|With both hands.|Com as duas mãos.
phone button|botão do celular|A phone button.|Um botão do celular.
power button|botão de ligar|The power button.|O botão de ligar.
three seconds|três segundos|Three seconds.|Três segundos.
baby’s head|cabeça do bebê|Support the baby’s head.|Apoie a cabeça do bebê.
hold a meeting|realizar uma reunião|Hold a meeting.|Realize uma reunião.
look for keys|procurar chaves|Look for my keys.|Procurar minhas chaves.
dirty dishes|louça suja|Dirty dishes.|Louça suja.""")
W('A1-L097',"""round table|mesa redonda|A round table.|Uma mesa redonda.
soft blue shirt|camisa azul macia|A soft blue shirt.|Uma camisa azul macia.
big old book|livro grande e velho|A big old book.|Um livro grande e velho.
nice new lamp|abajur novo e bonito|A nice new lamp.|Um abajur novo e bonito.
thin wooden stick|vareta fina de madeira|A thin wooden stick.|Uma vareta fina de madeira.
shape|forma|A round shape.|Uma forma redonda.
material|material|A soft material.|Um material macio.
age|idade|Old age.|Idade avançada.
look at|olhar|Look at this lamp.|Olhe este abajur.
notice the order|repare na ordem|Notice the order.|Repare na ordem.
object|objeto|A small object.|Um objeto pequeno.
describe|descrever|Describe it.|Descreva.""")
W('A1-L100',"""wall paint|tinta de parede|Wall paint.|Tinta de parede.
paint roller|rolo de pintura|A paint roller.|Um rolo de pintura.
safe bridge|ponte segura|A safe bridge.|Uma ponte segura.
blue bridge|ponte azul|A blue bridge.|Uma ponte azul.
volunteer day|dia de voluntariado|A volunteer day.|Um dia de voluntariado.
local news|notícia local|Local news.|Notícia local.
happy place|lugar feliz|A happy place.|Um lugar feliz.
town project|projeto da cidade|A town project.|Um projeto da cidade.
painted red|pintado de vermelho|Painted red.|Pintado de vermelho.
keep it clean|mantenha limpo|Keep it clean.|Mantenha limpo.""")
W('A1-L101',"""stage light|luz de palco|A stage light.|Uma luz de palco.
pop star|astro do pop|A pop star.|Um astro do pop.
music video|clipe|A music video.|Um clipe.
new album|álbum novo|A new album.|Um álbum novo.
long dress|vestido longo|A long dress.|Um vestido longo.
silver necklace|colar de prata|A silver necklace.|Um colar de prata.
slow song|música lenta|A slow song.|Uma música lenta.
young singer|jovem cantora|A young singer.|Uma jovem cantora.
sold-out show|show lotado|A sold-out show.|Um show lotado.
fan letter|carta de fã|A fan letter.|Uma carta de fã.""")
W('A1-L102',"""weekend walk|caminhada de fim de semana|A weekend walk.|Uma caminhada de fim de semana.
lake view|vista do lago|A lake view.|Uma vista do lago.
slow day|dia tranquilo|A slow day.|Um dia tranquilo.
walking shoes|sapatos de caminhada|Walking shoes.|Sapatos de caminhada.
reading chair|poltrona de leitura|A reading chair.|Uma poltrona de leitura.
swimming pool|piscina|A swimming pool.|Uma piscina.
doing nothing|não fazer nada|Doing nothing.|Não fazer nada.
quiet time|tempo de silêncio|Quiet time.|Tempo de silêncio.
fresh air|ar fresco|Fresh air.|Ar fresco.
free day|dia livre|A free day.|Um dia livre.
nature|natureza|Enjoy nature.|Curta a natureza.""")
W('A1-L103',"""cooking class|aula de culinária|A cooking class.|Uma aula de culinária.
film night|noite de filme|A film night.|Uma noite de filme.
running shoes|tênis de corrida|Running shoes.|Tênis de corrida.
hobby|passatempo|A relaxing hobby.|Um passatempo relaxante.
favorite film|filme favorito|My favorite film.|Meu filme favorito.
sleepy|com sono|I feel sleepy.|Estou com sono.
tired legs|pernas cansadas|Tired legs.|Pernas cansadas.
dinner plan|plano de jantar|A dinner plan.|Um plano de jantar.
soup pot|panela de sopa|A soup pot.|Uma panela de sopa.
couch|sofá|On the couch.|No sofá.""")
W('A1-L104',"""turn left|vire à esquerda|Turn left here.|Vire à esquerda aqui.
turn right|vire à direita|Turn right there.|Vire à direita ali.
next to the bank|ao lado do banco|Next to the bank.|Ao lado do banco.
yellow house|casa amarela|The yellow house.|A casa amarela.
street corner|esquina|On the street corner.|Na esquina.
traffic light|semáforo|Turn at the traffic light.|Vire no semáforo.
go straight|siga em frente|Go straight.|Siga em frente.
phone number|número de telefone|My phone number.|Meu número de telefone.
birthday party|festa de aniversário|My birthday party.|Minha festa de aniversário.
get lost|se perder|Don’t get lost.|Não se perca.
landmark|ponto de referência|A landmark.|Um ponto de referência.
turn off|desligar|Turn off the TV.|Desligue a TV.""")
W('A1-L105',"""football match|partida de futebol|A football match.|Uma partida de futebol.
TV show|programa de TV|A TV show.|Um programa de TV.
weekend hobby|hobby de fim de semana|A weekend hobby.|Um hobby de fim de semana.
reading time|hora de leitura|Reading time.|Hora de leitura.
cooking show|programa de culinária|A cooking show.|Um programa de culinária.
playing games|jogar jogos|Playing games.|Jogar jogos.
all day|o dia todo|All day long.|O dia todo.
screen|tela|A big screen.|Uma tela grande.
couch potato|sedentário|A couch potato.|Um sedentário.
remote control|controle remoto|A remote control.|Um controle remoto.""")
W('A1-L106',"""airport pickup|transfer do aeroporto|An airport pickup.|Um transfer do aeroporto.
ride app|aplicativo de transporte|A ride app.|Um aplicativo de transporte.
taxi fare|tarifa de táxi|A taxi fare.|Uma tarifa de táxi.
front door|porta de casa|Pick you up at the front door.|Buscamos na porta de casa.
luggage|bagagem|Heavy luggage.|Bagagem pesada.
driver|motorista|A friendly driver.|Um motorista simpático.
early flight|voo cedo|An early flight.|Um voo cedo.
book a ride|reservar uma corrida|Book a ride.|Reserve uma corrida.
save money|economizar|Save money.|Economize.
wait outside|espere do lado de fora|Wait outside.|Espere do lado de fora.
pickup time|hora da busca|The pickup time.|A hora da busca.
website|site|Visit our website.|Visite nosso site.
trip|viagem|A short trip.|Uma viagem curta.
price|preço|A low price.|Um preço baixo.""")
W('A1-L107',"""birthday candles|velas de aniversário|Birthday candles.|Velas de aniversário.
cake pan|forma de bolo|A cake pan.|Uma forma de bolo.
electric mixer|batedeira elétrica|An electric mixer.|Uma batedeira elétrica.
vanilla extract|essência de baunilha|Vanilla extract.|Essência de baunilha.
baking powder|fermento em pó|Baking powder.|Fermento em pó.
cake mix|mistura para bolo|A cake mix.|Uma mistura para bolo.
oven timer|timer do forno|An oven timer.|Um timer do forno.
beginner baker|padeiro iniciante|A beginner baker.|Um confeiteiro iniciante.
follow the recipe|siga a receita|Follow the recipe.|Siga a receita.
frosting|cobertura|Sweet frosting.|Cobertura doce.""")
W('A1-L108',"""word stress|acento tônico|Word stress.|Acento tônico.
first syllable|primeira sílaba|The first syllable.|A primeira sílaba.
second syllable|segunda sílaba|The second syllable.|A segunda sílaba.
quiet weekend|fim de semana tranquilo|A quiet weekend.|Um fim de semana tranquilo.
free time|tempo livre|Free time.|Tempo livre.
family time|tempo em família|Family time.|Tempo em família.
practice with a friend|praticar com um amigo|Practice with a friend.|Pratique com um amigo.
dictionary mark|marca do dicionário|A dictionary mark.|Uma marca do dicionário.
louder voice|voz mais alta|A louder voice.|Uma voz mais alta.""")
W('A1-L109',"""mountain hostel|albergue de montanha|A mountain hostel.|Um albergue de montanha.
bunk bed|beliche|A bunk bed.|Um beliche.
shared kitchen|cozinha compartilhada|A shared kitchen.|Uma cozinha compartilhada.
hiking boots|botas de caminhada|Hiking boots.|Botas de caminhada.
warm blanket|cobertor quente|A warm blanket.|Um cobertor quente.
night sky|céu noturno|The night sky.|O céu noturno.
winter trip|viagem de inverno|A winter trip.|Uma viagem de inverno.
friendly staff|equipe simpática|Friendly staff.|Equipe simpática.
trail map|mapa da trilha|A trail map.|Um mapa da trilha.
sleeping place|lugar para dormir|A sleeping place.|Um lugar para dormir.""")
W('A1-L110',"""red door|porta vermelha|A red door.|Uma porta vermelha.
front garden|jardim da frente|A front garden.|Um jardim da frente.
warm street|rua aconchegante|A warm street.|Uma rua aconchegante.
street light|poste de luz|A street light.|Um poste de luz.
paint bucket|balde de tinta|A paint bucket.|Um balde de tinta.
cup of tea|xícara de chá|A cup of tea.|Uma xícara de chá.
nice neighbor|vizinho legal|A nice neighbor.|Um vizinho legal.
smile|sorriso|A big smile.|Um grande sorriso.
argument|discussão|A small argument.|Uma pequena discussão.
beautiful color|cor bonita|A beautiful color.|Uma cor bonita.""")
W('A1-L111',"""shopping spree|farra de compras|A shopping spree.|Uma farra de compras.
price tag|etiqueta de preço|Check the price tag.|Veja a etiqueta de preço.
warm jacket|jaqueta quente|A warm jacket.|Uma jaqueta quente.
good deal|bom negócio|A good deal.|Um bom negócio.
save money|economizar dinheiro|Save money.|Economize dinheiro.
spend wisely|gastar com sabedoria|Spend wisely.|Gaste com sabedoria.
need or want|necessidade ou desejo|Need or want?|Necessidade ou desejo?
shopping habit|hábito de compra|A shopping habit.|Um hábito de compra.
sale season|época de promoções|The sale season.|A época de promoções.
nervous shopper|comprador nervoso|A nervous shopper.|Um comprador nervoso.""")
W('A1-L112',"""class notes|anotações de aula|Class notes.|Anotações de aula.
pencil case|estojo|A pencil case.|Um estojo.
study materials|material de estudo|Study materials.|Material de estudo.
water bottle|garrafa de água|A water bottle.|Uma garrafa de água.
class preparation|preparação para a aula|Class preparation.|Preparação para a aula.
good habits|bons hábitos|Good habits.|Bons hábitos.
research study|estudo de pesquisa|A research study.|Um estudo de pesquisa.
bring along|levar junto|Bring along a pen.|Leve uma caneta junto.
learn more|aprender mais|Learn more.|Aprenda mais.
dictionary app|aplicativo de dicionário|A dictionary app.|Um aplicativo de dicionário.
enjoy learning|curtir aprender|Enjoy learning.|Curta aprender.""")
W('A1-L113',"""reason|razão|A good reason.|Uma boa razão.
rainy day|dia chuvoso|A rainy day.|Um dia chuvoso.
stay home|ficar em casa|Stay home.|Fique em casa.
go out|sair|Go out tonight.|Saia hoje à noite.
cold weather|tempo frio|Cold weather.|Tempo frio.
bored|entediado|I am bored.|Estou entediado.
choose one|escolha um|Choose one.|Escolha um.
cause and result|causa e resultado|Cause and result.|Causa e resultado.
sentence connector|conectivo de frase|A sentence connector.|Um conectivo de frase.
because of rain|por causa da chuva|Because of rain.|Por causa da chuva.""")
