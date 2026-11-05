"""Reservas temáticas por campo vocabular (palavras), expressões gerais e verbos, para completar as cotas sem repetir."""
def _l(s):return [x.strip() for x in s.strip().splitlines() if x.strip()]
FIELD={}
FIELD['Vida pessoal']=_l("""
hobby;passatempo;My hobby is music.;Meu passatempo é música.
friendship;amizade;A true friendship.;Uma amizade verdadeira.
personality;personalidade;A warm personality.;Uma personalidade calorosa.
birthday party;festa de aniversário;A big birthday party.;Uma grande festa de aniversário.
nickname;apelido;His nickname is Leo.;O apelido dele é Leo.
gender;gênero;Write your gender.;Escreva seu gênero.
nationality;nacionalidade;What is your nationality?;Qual é sua nacionalidade?
language;idioma;I speak two languages.;Falo dois idiomas.
twin;gêmeo;My twin is tall.;Meu gêmeo é alto.
teenager;adolescente;A shy teenager.;Um adolescente tímido.
adult;adulto;An adult class.;Uma turma de adultos.
elderly;idoso;An elderly man.;Um senhor idoso.
generation;geração;A new generation.;Uma nova geração.
habit;hábito;A good habit.;Um bom hábito.
dream;sonho;A big dream.;Um grande sonho.
goal;objetivo;A clear goal.;Um objetivo claro.
fear;medo;A strong fear.;Um medo forte.
joy;alegria;Pure joy.;Pura alegria.
mood;humor;A good mood.;Um bom humor.
opinion;opinião;My opinion is simple.;Minha opinião é simples.
advice;conselho;Good advice.;Bom conselho.
secret;segredo;A small secret.;Um pequeno segredo.
birthday;aniversário;My birthday is soon.;Meu aniversário é em breve.
wedding;casamento;A nice wedding.;Um casamento bonito.
couple;casal;A happy couple.;Um casal feliz.
relative;parente;A distant relative.;Um parente distante.
stepmother;madrasta;My stepmother is kind.;Minha madrasta é gentil.
nephew;sobrinho;My nephew is five.;Meu sobrinho tem cinco anos.
niece;sobrinha;My niece sings.;Minha sobrinha canta.
godmother;madrinha;My godmother calls.;Minha madrinha liga.
roommate;colega de quarto;My roommate cooks.;Meu colega de quarto cozinha.
partner;parceiro;My partner works.;Meu parceiro trabalha.
stranger;estranho;A kind stranger.;Um estranho gentil.
guest;convidado;A polite guest.;Um convidado educado.
host;anfitrião;A warm host.;Um anfitrião caloroso.
volunteer;voluntário;A young volunteer.;Um jovem voluntário.
citizen;cidadão;A proud citizen.;Um cidadão orgulhoso.
resident;morador;A new resident.;Um novo morador.
pet;animal de estimação;My pet is a cat.;Meu bicho é um gato.
puppy;filhote;A tiny puppy.;Um filhote minúsculo.
kitten;gatinho;A soft kitten.;Um gatinho macio.
shy;tímido;A shy girl.;Uma menina tímida.
polite;educado;A polite boy.;Um menino educado.
rude;mal-educado;A rude answer.;Uma resposta mal-educada.
lazy;preguiçoso;A lazy day.;Um dia preguiçoso.
brave;corajoso;A brave woman.;Uma mulher corajosa.
clever;esperto;A clever child.;Uma criança esperta.
funny;engraçado;A funny uncle.;Um tio engraçado.
serious;sério;A serious face.;Um rosto sério.
generous;generoso;A generous aunt.;Uma tia generosa.
patient;paciente;A patient teacher.;Uma professora paciente.
curious;curioso;A curious kid.;Uma criança curiosa.
lonely;solitário;A lonely night.;Uma noite solitária.
excited;animado;We are excited.;Estamos animados.
nervous;nervoso;I feel nervous.;Sinto-me nervoso.
confused;confuso;He looks confused.;Ele parece confuso.
embarrassed;envergonhado;I am embarrassed.;Estou envergonhado.
grateful;grato;I am grateful.;Sou grato.
jealous;com ciúmes;Don’t be jealous.;Não tenha ciúmes.
selfie;selfie;Take a selfie.;Tire uma selfie.
profile;perfil;Update your profile.;Atualize seu perfil.
username;nome de usuário;Choose a username.;Escolha um nome de usuário.
password;senha;A strong password.;Uma senha forte.
signature;assinatura;Write your signature.;Escreva sua assinatura.
form;formulário;Fill out the form.;Preencha o formulário.
""")
FIELD['Rotina']=_l("""
alarm;despertador;The alarm rings.;O despertador toca.
snooze;soneca;Hit the snooze.;Aperte a soneca.
mirror;espelho;Look in the mirror.;Olhe no espelho.
comb;pente;A plastic comb.;Um pente de plástico.
razor;barbeador;A new razor.;Um barbeador novo.
shampoo;xampu;A bottle of shampoo.;Um frasco de xampu.
toothpaste;pasta de dente;Mint toothpaste.;Pasta de dente de menta.
lunchbox;marmita;Pack a lunchbox.;Prepare uma marmita.
bus pass;passe de ônibus;Show your bus pass.;Mostre o passe de ônibus.
rush;pressa;Morning rush.;Correria da manhã.
nap;cochilo;Take a nap.;Tire um cochilo.
errand;tarefa externa;Run an errand.;Faça uma tarefa externa.
grocery store;mercado;Go to the grocery store.;Vá ao mercado.
pharmacy;farmácia;Stop by the pharmacy.;Passe na farmácia.
post office;correio;Mail it at the post office.;Envie pelo correio.
dry cleaner;lavanderia;Pick up from the dry cleaner.;Busque na lavanderia.
gas;gasolina;Fill up with gas.;Abasteça.
laundry;roupa suja;Do the laundry.;Lave a roupa.
dishwasher;lava-louças;Load the dishwasher.;Carregue a lava-louças.
trash;lixo;Take out the trash.;Leve o lixo para fora.
bedtime;hora de dormir;It is bedtime.;É hora de dormir.
pillow;travesseiro;A soft pillow.;Um travesseiro macio.
blanket;cobertor;A warm blanket.;Um cobertor quente.
news;notícias;Watch the news.;Assista ao noticiário.
podcast;podcast;Listen to a podcast.;Ouça um podcast.
playlist;lista de músicas;A morning playlist.;Uma lista de músicas matinal.
snack;lanche;An afternoon snack.;Um lanche da tarde.
dinner;jantar;A late dinner.;Um jantar tarde.
dessert;sobremesa;A sweet dessert.;Uma sobremesa doce.
dawn;amanhecer;At dawn.;Ao amanhecer.
dusk;entardecer;At dusk.;Ao entardecer.
midnight;meia-noite;At midnight.;À meia-noite.
afternoon;tarde;Every afternoon.;Toda tarde.
schedule;horário;A busy schedule.;Um horário cheio.
appointment;compromisso;An appointment at ten.;Um compromisso às dez.
chore;tarefa doméstica;An easy chore.;Uma tarefa doméstica fácil.
shopping list;lista de compras;Write a shopping list.;Escreva uma lista de compras.
ironing;passar roupa;Do the ironing.;Passe a roupa.
vacuum cleaner;aspirador;Use the vacuum cleaner.;Use o aspirador.
alarm clock;relógio despertador;A loud alarm clock.;Um despertador alto.
leave;partir;I leave at eight.;Saio às oito.
usually;geralmente;I usually walk.;Geralmente ando.
sometimes;às vezes;Sometimes I run.;Às vezes corro.
never;nunca;I never skip.;Nunca falto.
weekday;dia útil;A busy weekday.;Um dia útil movimentado.
weekend;fim de semana;A lazy weekend.;Um fim de semana preguiçoso.
yawn;bocejo;A big yawn.;Um grande bocejo.
stretch;espreguiçar;Stretch in bed.;Espreguice na cama.
bathrobe;roupão;A white bathrobe.;Um roupão branco.
slippers;chinelos;Soft slippers.;Chinelos macios.
doorstep;soleira;On the doorstep.;Na soleira.
keys;chaves;Find my keys.;Ache minhas chaves.
umbrella;guarda-chuva;Take an umbrella.;Leve um guarda-chuva.
wallet;carteira;Check your wallet.;Confira sua carteira.
commute;trajeto;A short commute.;Um trajeto curto.
timetable;horário de transporte;Check the timetable.;Confira o horário.
""")
FIELD['Alimentação']=_l("""
flour;farinha;A bag of flour.;Um saco de farinha.
sugar;açúcar;A spoon of sugar.;Uma colher de açúcar.
salt;sal;A pinch of salt.;Uma pitada de sal.
oil;óleo;Olive oil.;Azeite.
vinegar;vinagre;A little vinegar.;Um pouco de vinagre.
mustard;mostarda;Hot mustard.;Mostarda forte.
ketchup;ketchup;Tomato ketchup.;Ketchup de tomate.
mayonnaise;maionese;A spoon of mayonnaise.;Uma colher de maionese.
honey;mel;Sweet honey.;Mel doce.
jam;geleia;Berry jam.;Geleia de frutas.
bread;pão;Fresh bread.;Pão fresco.
rice;arroz;White rice.;Arroz branco.
beans;feijão;Black beans.;Feijão preto.
lentils;lentilhas;Cooked lentils.;Lentilhas cozidas.
noodles;macarrão;Hot noodles.;Macarrão quente.
potato;batata;A baked potato.;Uma batata assada.
onion;cebola;A red onion.;Uma cebola roxa.
carrot;cenoura;A raw carrot.;Uma cenoura crua.
lettuce;alface;Crisp lettuce.;Alface crocante.
cucumber;pepino;A cool cucumber.;Um pepino fresco.
pepper;pimentão;A green pepper.;Um pimentão verde.
broccoli;brócolis;Steamed broccoli.;Brócolis no vapor.
corn;milho;Sweet corn.;Milho doce.
peas;ervilhas;Green peas.;Ervilhas verdes.
apple;maçã;A red apple.;Uma maçã vermelha.
banana;banana;A ripe banana.;Uma banana madura.
orange;laranja;A juicy orange.;Uma laranja suculenta.
grape;uva;Sweet grapes.;Uvas doces.
peach;pêssego;A soft peach.;Um pêssego macio.
pear;pera;A green pear.;Uma pera verde.
strawberry;morango;A fresh strawberry.;Um morango fresco.
watermelon;melancia;Cold watermelon.;Melancia gelada.
pineapple;abacaxi;Sweet pineapple.;Abacaxi doce.
beef;carne bovina;Grilled beef.;Carne bovina grelhada.
pork;carne de porco;Roast pork.;Porco assado.
lamb;cordeiro;Roast lamb.;Cordeiro assado.
shrimp;camarão;Fried shrimp.;Camarão frito.
tuna;atum;Canned tuna.;Atum em lata.
salmon;salmão;Baked salmon.;Salmão assado.
sausage;linguiça;Grilled sausage.;Linguiça grelhada.
butter;manteiga;Melted butter.;Manteiga derretida.
yogurt;iogurte;Plain yogurt.;Iogurte natural.
cream;creme;Fresh cream.;Creme fresco.
juice;suco;Orange juice.;Suco de laranja.
lemonade;limonada;Cold lemonade.;Limonada gelada.
soda;refrigerante;A can of soda.;Uma lata de refrigerante.
sparkling water;água com gás;Sparkling water.;Água com gás.
smoothie;vitamina;A fruit smoothie.;Uma vitamina de frutas.
chocolate;chocolate;Dark chocolate.;Chocolate amargo.
candy;doce;Hard candy.;Bala dura.
cake;bolo;Chocolate cake.;Bolo de chocolate.
pie;torta;Apple pie.;Torta de maçã.
ice cream;sorvete;Vanilla ice cream.;Sorvete de baunilha.
pizza;pizza;Cheese pizza.;Pizza de queijo.
hamburger;hambúrguer;A big hamburger.;Um hambúrguer grande.
fries;batata frita;Hot fries.;Batatas fritas quentes.
salad;salada;Mixed salad.;Salada mista.
soup;sopa;Chicken soup.;Sopa de galinha.
stew;ensopado;Beef stew.;Ensopado de carne.
sandwich;sanduíche;A ham sandwich.;Um sanduíche de presunto.
appetizer;entrada;A small appetizer.;Uma entrada pequena.
main course;prato principal;The main course.;O prato principal.
bill;conta;Ask for the bill.;Peça a conta.
tip;gorjeta;Leave a tip.;Deixe uma gorjeta.
reservation;reserva;A table reservation.;Uma reserva de mesa.
vegetarian;vegetariano;A vegetarian menu.;Um cardápio vegetariano.
spoon;colher;A clean spoon.;Uma colher limpa.
chopsticks;hashis;Use chopsticks.;Use hashis.
frying pan;frigideira;A hot frying pan.;Uma frigideira quente.
cutting board;tábua de corte;A wooden cutting board.;Uma tábua de corte de madeira.
bake;assar;Bake for an hour.;Asse por uma hora.
boil;ferver;Boil the water.;Ferva a água.
fry;fritar;Fry the eggs.;Frite os ovos.
grill;grelhar;Grill the fish.;Grelhe o peixe.
roast;assar (carne);Roast the chicken.;Asse o frango.
""")
FIELD['Moradia']=_l("""
apartment;apartamento;A bright apartment.;Um apartamento claro.
house;casa;A big house.;Uma casa grande.
cottage;chalé;A small cottage.;Um chalé pequeno.
dormitory;alojamento;A student dormitory.;Um alojamento estudantil.
bedroom;quarto;A tidy bedroom.;Um quarto arrumado.
living room;sala de estar;A cozy living room.;Uma sala aconchegante.
dining room;sala de jantar;A formal dining room.;Uma sala de jantar formal.
bathroom;banheiro;A clean bathroom.;Um banheiro limpo.
hall;corredor;A narrow hall.;Um corredor estreito.
staircase;escadaria;A wooden staircase.;Uma escadaria de madeira.
ceiling;teto;A high ceiling.;Um teto alto.
floor;piso;A tile floor.;Um piso de azulejo.
wall;parede;A white wall.;Uma parede branca.
window;janela;A wide window.;Uma janela larga.
door;porta;A heavy door.;Uma porta pesada.
gate;portão;A metal gate.;Um portão de metal.
fence;cerca;A low fence.;Uma cerca baixa.
yard;quintal;A green yard.;Um quintal verde.
terrace;terraço;A sunny terrace.;Um terraço ensolarado.
carpet;carpete;A thick carpet.;Um carpete grosso.
curtain;cortina;A long curtain.;Uma cortina longa.
blinds;persiana;Close the blinds.;Feche as persianas.
mirror;espelho;A round mirror.;Um espelho redondo.
picture frame;porta-retrato;A wooden picture frame.;Um porta-retrato de madeira.
couch;sofá;A leather couch.;Um sofá de couro.
armchair;poltrona;A soft armchair.;Uma poltrona macia.
coffee table;mesa de centro;A glass coffee table.;Uma mesa de centro de vidro.
bookcase;estante;A tall bookcase.;Uma estante alta.
wardrobe;guarda-roupa;A big wardrobe.;Um guarda-roupa grande.
dresser;cômoda;An old dresser.;Uma cômoda antiga.
nightstand;criado-mudo;A small nightstand.;Um criado-mudo pequeno.
bunk bed;beliche;A wooden bunk bed.;Um beliche de madeira.
mattress;colchão;A firm mattress.;Um colchão firme.
sheet;lençol;A clean sheet.;Um lençol limpo.
pillowcase;fronha;A soft pillowcase.;Uma fronha macia.
fridge;geladeira;A full fridge.;Uma geladeira cheia.
freezer;congelador;A cold freezer.;Um congelador gelado.
stove;fogão;A gas stove.;Um fogão a gás.
oven;forno;A hot oven.;Um forno quente.
microwave;micro-ondas;A small microwave.;Um micro-ondas pequeno.
dishwasher;lava-louças;A quiet dishwasher.;Uma lava-louças silenciosa.
washing machine;máquina de lavar;A new washing machine.;Uma máquina de lavar nova.
dryer;secadora;An electric dryer.;Uma secadora elétrica.
water heater;aquecedor de água;A broken water heater.;Um aquecedor de água quebrado.
air conditioner;ar-condicionado;Turn on the air conditioner.;Ligue o ar-condicionado.
fan;ventilador;A ceiling fan.;Um ventilador de teto.
radiator;radiador;A warm radiator.;Um radiador quente.
light bulb;lâmpada;Change the light bulb.;Troque a lâmpada.
switch;interruptor;Press the switch.;Aperte o interruptor.
socket;tomada;An empty socket.;Uma tomada livre.
shower;chuveiro;A hot shower.;Um chuveiro quente.
bathtub;banheira;A deep bathtub.;Uma banheira funda.
sink;pia;A small sink.;Uma pia pequena.
toilet;vaso sanitário;A clean toilet.;Um vaso limpo.
bin;lixeira;A kitchen bin.;Uma lixeira de cozinha.
broom;vassoura;A new broom.;Uma vassoura nova.
bucket;balde;A full bucket.;Um balde cheio.
ladder;escada de mão;A tall ladder.;Uma escada alta.
toolbox;caixa de ferramentas;A heavy toolbox.;Uma caixa de ferramentas pesada.
screwdriver;chave de fenda;A small screwdriver.;Uma chave de fenda pequena.
hammer;martelo;A strong hammer.;Um martelo forte.
nail;prego;A long nail.;Um prego longo.
paint;tinta;White paint.;Tinta branca.
brush;pincel;A wide brush.;Um pincel largo.
rent;aluguel;Monthly rent.;Aluguel mensal.
landlord;proprietário;A fair landlord.;Um proprietário justo.
mortgage;financiamento;A long mortgage.;Um financiamento longo.
neighbourhood;vizinhança;A safe neighbourhood.;Uma vizinhança segura.
lease;contrato;A one-year lease.;Um contrato de um ano.
""")
FIELD['Trabalho']=_l("""
employee;funcionário;A new employee.;Um novo funcionário.
employer;empregador;A fair employer.;Um empregador justo.
coworker;colega;A helpful coworker.;Um colega prestativo.
supervisor;supervisor;The supervisor smiles.;O supervisor sorri.
director;diretor;The director speaks.;O diretor fala.
receptionist;recepcionista;A polite receptionist.;Uma recepcionista educada.
secretary;secretária;The secretary calls.;A secretária liga.
accountant;contador;The accountant counts.;O contador conta.
salesperson;vendedor;A good salesperson.;Um bom vendedor.
cashier;caixa;The cashier waits.;O caixa espera.
mechanic;mecânico;The mechanic works.;O mecânico trabalha.
electrician;eletricista;An honest electrician.;Um eletricista honesto.
carpenter;carpinteiro;A skilled carpenter.;Um carpinteiro habilidoso.
architect;arquiteto;A young architect.;Uma jovem arquiteta.
designer;designer;A creative designer.;Uma designer criativa.
programmer;programador;A fast programmer.;Um programador rápido.
translator;tradutor;A careful translator.;Uma tradutora cuidadosa.
journalist;jornalista;A busy journalist.;Um jornalista ocupado.
photographer;fotógrafo;A famous photographer.;Um fotógrafo famoso.
pilot;piloto;An experienced pilot.;Um piloto experiente.
flight attendant;comissário;A friendly flight attendant.;Uma comissária simpática.
firefighter;bombeiro;A brave firefighter.;Um bombeiro corajoso.
police officer;policial;A fair police officer.;Um policial justo.
judge;juiz;The judge listens.;O juiz escuta.
lawyer;advogado;A smart lawyer.;Um advogado esperto.
surgeon;cirurgião;A calm surgeon.;Um cirurgião calmo.
dentist;dentista;A gentle dentist.;Um dentista gentil.
pharmacist;farmacêutico;The pharmacist helps.;O farmacêutico ajuda.
farmer;agricultor;A hard-working farmer.;Um agricultor trabalhador.
fisherman;pescador;An old fisherman.;Um pescador idoso.
baker;padeiro;The baker wakes early.;O padeiro acorda cedo.
butcher;açougueiro;The butcher cuts meat.;O açougueiro corta carne.
tailor;alfaiate;A skilled tailor.;Um alfaiate habilidoso.
hairdresser;cabeleireiro;A trendy hairdresser.;Um cabeleireiro moderno.
cleaner;faxineiro;A careful cleaner.;Uma faxineira cuidadosa.
guard;segurança;A night guard.;Um segurança noturno.
driver;motorista;A bus driver.;Um motorista de ônibus.
resume;currículo;Send your resume.;Envie seu currículo.
cover letter;carta de apresentação;Write a cover letter.;Escreva uma carta de apresentação.
interview;entrevista;A job interview.;Uma entrevista de emprego.
application;candidatura;Send an application.;Envie uma candidatura.
hire;contratar;They hire students.;Eles contratam estudantes.
fire;demitir;He was fired.;Ele foi demitido.
promotion;promoção;Get a promotion.;Receba uma promoção.
raise;aumento;Ask for a raise.;Peça um aumento.
salary;salário;A fair salary.;Um salário justo.
overtime;hora extra;Work overtime.;Faça hora extra.
full-time;período integral;A full-time job.;Um emprego de período integral.
part-time;meio período;A part-time job.;Um emprego de meio período.
shift;turno;The morning shift.;O turno da manhã.
deadline;prazo;A tight deadline.;Um prazo apertado.
meeting;reunião;A long meeting.;Uma reunião longa.
conference;conferência;A big conference.;Uma grande conferência.
presentation;apresentação;A short presentation.;Uma apresentação curta.
report;relatório;A weekly report.;Um relatório semanal.
invoice;fatura;Send the invoice.;Envie a fatura.
budget;orçamento;A small budget.;Um orçamento pequeno.
profit;lucro;A big profit.;Um grande lucro.
customer;cliente;A loyal customer.;Um cliente fiel.
supplier;fornecedor;A local supplier.;Um fornecedor local.
stapler;grampeador;A red stapler.;Um grampeador vermelho.
scissors;tesoura;Sharp scissors.;Tesoura afiada.
envelope;envelope;A white envelope.;Um envelope branco.
stamp;selo;A postage stamp.;Um selo postal.
printer;impressora;A noisy printer.;Uma impressora barulhenta.
whiteboard;quadro branco;Write on the whiteboard.;Escreva no quadro branco.
""")
FIELD['Lazer']=_l("""
hobby;passatempo;A relaxing hobby.;Um passatempo relaxante.
painting;pintura;A small painting.;Uma pintura pequena.
drawing;desenho;A quick drawing.;Um desenho rápido.
knitting;tricô;Learn knitting.;Aprenda tricô.
gardening;jardinagem;Enjoy gardening.;Curta jardinagem.
fishing;pesca;A day of fishing.;Um dia de pesca.
hiking;trilha;Go hiking.;Faça uma trilha.
camping;acampamento;A camping trip.;Uma viagem de acampamento.
cycling;ciclismo;Weekend cycling.;Ciclismo de fim de semana.
swimming;natação;Swimming lessons.;Aulas de natação.
yoga;ioga;Morning yoga.;Ioga matinal.
dancing;dança;Salsa dancing.;Dança de salsa.
chess;xadrez;Play chess.;Jogue xadrez.
cards;cartas;Play cards.;Jogue cartas.
board game;jogo de tabuleiro;A board game night.;Uma noite de jogo de tabuleiro.
puzzle;quebra-cabeça;A hard puzzle.;Um quebra-cabeça difícil.
video game;videogame;A new video game.;Um videogame novo.
comic;história em quadrinhos;A funny comic.;Uma história em quadrinhos engraçada.
novel;romance;A long novel.;Um romance longo.
poem;poema;A short poem.;Um poema curto.
magazine;revista;A fashion magazine.;Uma revista de moda.
documentary;documentário;A nature documentary.;Um documentário de natureza.
series;série;A popular series.;Uma série popular.
episode;episódio;The last episode.;O último episódio.
cinema;cinema;An old cinema.;Um cinema antigo.
theater;teatro;A big theater.;Um teatro grande.
concert;show;A live concert.;Um show ao vivo.
festival;festival;A summer festival.;Um festival de verão.
museum;museu;A science museum.;Um museu de ciências.
gallery;galeria;An art gallery.;Uma galeria de arte.
exhibition;exposição;A photo exhibition.;Uma exposição de fotos.
zoo;zoológico;A small zoo.;Um zoológico pequeno.
aquarium;aquário;A big aquarium.;Um aquário grande.
amusement park;parque de diversões;An amusement park.;Um parque de diversões.
roller coaster;montanha-russa;A fast roller coaster.;Uma montanha-russa rápida.
beach;praia;A sandy beach.;Uma praia de areia.
pool;piscina;A cool pool.;Uma piscina fresca.
playground;parquinho;A busy playground.;Um parquinho movimentado.
stadium;estádio;A huge stadium.;Um estádio enorme.
match;partida;A football match.;Uma partida de futebol.
team;time;A strong team.;Um time forte.
coach;treinador;A tough coach.;Um treinador rígido.
fan;torcedor;A loud fan.;Um torcedor barulhento.
score;placar;The final score.;O placar final.
goal;gol;A great goal.;Um golaço.
tournament;torneio;A local tournament.;Um torneio local.
champion;campeão;A young champion.;Um jovem campeão.
trophy;troféu;A silver trophy.;Um troféu de prata.
ticket;ingresso;A cheap ticket.;Um ingresso barato.
guitar;violão;An old guitar.;Um violão antigo.
piano;piano;A grand piano.;Um piano de cauda.
drums;bateria;Loud drums.;Bateria alta.
violin;violino;A soft violin.;Um violino suave.
band;banda;A rock band.;Uma banda de rock.
song;canção;A new song.;Uma nova canção.
lyrics;letra;Learn the lyrics.;Aprenda a letra.
microphone;microfone;A wireless microphone.;Um microfone sem fio.
playlist;lista de músicas;A party playlist.;Uma lista para a festa.
party;festa;A surprise party.;Uma festa surpresa.
costume;fantasia;A funny costume.;Uma fantasia engraçada.
gift;presente;A small gift.;Um presente pequeno.
photo;foto;A family photo.;Uma foto de família.
album;álbum;A photo album.;Um álbum de fotos.
""")
FIELD['Lugares']=_l("""
city;cidade;A big city.;Uma cidade grande.
town;cidade pequena;A quiet town.;Uma cidade pequena e calma.
village;vila;A tiny village.;Uma vila minúscula.
suburb;subúrbio;A green suburb.;Um subúrbio verde.
downtown;centro;Downtown is busy.;O centro está movimentado.
neighborhood;bairro;A friendly neighborhood.;Um bairro simpático.
street;rua;A narrow street.;Uma rua estreita.
avenue;avenida;A wide avenue.;Uma avenida larga.
bridge;ponte;An old bridge.;Uma ponte antiga.
tunnel;túnel;A long tunnel.;Um túnel longo.
crossroad;cruzamento;A busy crossroad.;Um cruzamento movimentado.
traffic light;semáforo;A red traffic light.;Um semáforo vermelho.
sidewalk;calçada;A wide sidewalk.;Uma calçada larga.
bus stop;ponto de ônibus;A crowded bus stop.;Um ponto de ônibus lotado.
subway station;estação de metrô;A deep subway station.;Uma estação de metrô funda.
train station;estação de trem;A big train station.;Uma grande estação de trem.
airport;aeroporto;A busy airport.;Um aeroporto movimentado.
harbor;porto;A small harbor.;Um porto pequeno.
parking lot;estacionamento;A free parking lot.;Um estacionamento grátis.
gas station;posto de gasolina;A night gas station.;Um posto de gasolina noturno.
supermarket;supermercado;A big supermarket.;Um supermercado grande.
bakery;padaria;A warm bakery.;Uma padaria aconchegante.
pharmacy;farmácia;A late pharmacy.;Uma farmácia que fecha tarde.
bank;banco;A local bank.;Um banco local.
post office;correio;A small post office.;Um correio pequeno.
police station;delegacia;The police station.;A delegacia.
fire station;corpo de bombeiros;A fire station.;Um posto de bombeiros.
hospital;hospital;A children’s hospital.;Um hospital infantil.
clinic;clínica;A health clinic.;Uma clínica de saúde.
school;escola;A public school.;Uma escola pública.
university;universidade;A big university.;Uma universidade grande.
library;biblioteca;A quiet library.;Uma biblioteca silenciosa.
museum;museu;An art museum.;Um museu de arte.
church;igreja;An old church.;Uma igreja antiga.
temple;templo;A peaceful temple.;Um templo tranquilo.
mosque;mesquita;A blue mosque.;Uma mesquita azul.
castle;castelo;A medieval castle.;Um castelo medieval.
palace;palácio;A royal palace.;Um palácio real.
monument;monumento;A famous monument.;Um monumento famoso.
statue;estátua;A bronze statue.;Uma estátua de bronze.
square;praça;A crowded square.;Uma praça lotada.
fountain;fonte;A tall fountain.;Uma fonte alta.
park;parque;A city park.;Um parque da cidade.
garden;jardim;A botanic garden.;Um jardim botânico.
lake;lago;A calm lake.;Um lago calmo.
river;rio;A long river.;Um rio longo.
beach;praia;A quiet beach.;Uma praia tranquila.
island;ilha;A small island.;Uma ilha pequena.
mountain;montanha;A snowy mountain.;Uma montanha nevada.
forest;floresta;A dark forest.;Uma floresta escura.
desert;deserto;A hot desert.;Um deserto quente.
valley;vale;A green valley.;Um vale verde.
hill;colina;A grassy hill.;Uma colina gramada.
farm;fazenda;A dairy farm.;Uma fazenda leiteira.
factory;fábrica;A toy factory.;Uma fábrica de brinquedos.
market;mercado;A weekend market.;Uma feira de fim de semana.
shopping center;shopping;A huge shopping center.;Um shopping enorme.
cinema;cinema;A small cinema.;Um cinema pequeno.
stadium;estádio;A football stadium.;Um estádio de futebol.
hotel;hotel;A beach hotel.;Um hotel de praia.
hostel;albergue;A cheap hostel.;Um albergue barato.
restaurant;restaurante;A family restaurant.;Um restaurante familiar.
café;café;A corner café.;Um café de esquina.
pub;bar;A cozy pub.;Um bar aconchegante.
nightclub;boate;A loud nightclub.;Uma boate barulhenta.
border;fronteira;A closed border.;Uma fronteira fechada.
capital;capital;The capital city.;A capital.
coast;litoral;A rocky coast.;Um litoral rochoso.
""")
FIELD['Viagens']=_l("""
trip;viagem;A short trip.;Uma viagem curta.
journey;jornada;A long journey.;Uma jornada longa.
flight;voo;A night flight.;Um voo noturno.
layover;escala;A long layover.;Uma escala longa.
boarding pass;cartão de embarque;Show your boarding pass.;Mostre o cartão de embarque.
gate;portão de embarque;Gate twelve.;Portão doze.
runway;pista;A long runway.;Uma pista longa.
customs;alfândega;Pass customs.;Passe pela alfândega.
passport control;controle de passaporte;Wait at passport control.;Espere no controle de passaporte.
visa;visto;A tourist visa.;Um visto de turista.
luggage;bagagem;Light luggage.;Bagagem leve.
carry-on;bagagem de mão;A small carry-on.;Uma bagagem de mão pequena.
suitcase;mala;A red suitcase.;Uma mala vermelha.
backpack;mochila;A light backpack.;Uma mochila leve.
tag;etiqueta;A luggage tag.;Uma etiqueta de bagagem.
lost luggage;bagagem extraviada;Report lost luggage.;Informe bagagem extraviada.
check-in desk;balcão de check-in;Go to the check-in desk.;Vá ao balcão de check-in.
security check;revista de segurança;A quick security check.;Uma revista rápida.
departure lounge;sala de embarque;The departure lounge.;A sala de embarque.
duty-free;duty free;A duty-free shop.;Uma loja duty free.
taxi;táxi;Take a taxi.;Pegue um táxi.
shuttle;transfer;A hotel shuttle.;Um transfer do hotel.
rental car;carro alugado;A cheap rental car.;Um carro alugado barato.
ferry;balsa;Take the ferry.;Pegue a balsa.
cruise;cruzeiro;A week-long cruise.;Um cruzeiro de uma semana.
coach;ônibus de viagem;A comfortable coach.;Um ônibus de viagem confortável.
sleeper train;trem-leito;Book a sleeper train.;Reserve um trem-leito.
one-way;só ida;A one-way ticket.;Uma passagem só de ida.
return ticket;passagem de volta;Buy a return ticket.;Compre uma passagem de volta.
timetable;horário;Check the timetable.;Confira o horário.
delay;atraso;A long delay.;Um longo atraso.
cancellation;cancelamento;A flight cancellation.;Um cancelamento de voo.
reservation;reserva;A hotel reservation.;Uma reserva de hotel.
single room;quarto de solteiro;A single room.;Um quarto de solteiro.
double room;quarto de casal;A double room.;Um quarto de casal.
reception;recepção;Ask at reception.;Pergunte na recepção.
key card;cartão-chave;Use your key card.;Use seu cartão-chave.
room service;serviço de quarto;Order room service.;Peça serviço de quarto.
breakfast buffet;buffet de café;A big breakfast buffet.;Um grande buffet de café.
sightseeing;turismo;Go sightseeing.;Faça turismo.
guided tour;visita guiada;Join a guided tour.;Faça uma visita guiada.
guidebook;guia de viagem;Buy a guidebook.;Compre um guia de viagem.
map;mapa;A city map.;Um mapa da cidade.
souvenir;lembrança;A small souvenir.;Uma lembrança pequena.
postcard;cartão-postal;Send a postcard.;Envie um cartão-postal.
landmark;ponto turístico;A famous landmark.;Um ponto turístico famoso.
viewpoint;mirante;A high viewpoint.;Um mirante alto.
beach resort;resort de praia;A beach resort.;Um resort de praia.
campsite;camping;A quiet campsite.;Um camping tranquilo.
tent;barraca;A small tent.;Uma barraca pequena.
sleeping bag;saco de dormir;A warm sleeping bag.;Um saco de dormir quente.
trail;trilha;A mountain trail.;Uma trilha de montanha.
exchange rate;taxa de câmbio;A good exchange rate.;Uma boa taxa de câmbio.
currency;moeda;Local currency.;Moeda local.
traveler’s check;cheque de viagem;An old traveler’s check.;Um cheque de viagem antigo.
insurance;seguro;Travel insurance.;Seguro de viagem.
jet lag;jet lag;Bad jet lag.;Jet lag forte.
homesick;com saudade de casa;I feel homesick.;Sinto saudade de casa.
adventure;aventura;A big adventure.;Uma grande aventura.
itinerary;roteiro;A busy itinerary.;Um roteiro cheio.
destination;destino;A popular destination.;Um destino popular.
local;local;A local guide.;Um guia local.
foreigner;estrangeiro;A friendly foreigner.;Um estrangeiro simpático.
translation;tradução;A quick translation.;Uma tradução rápida.
phrasebook;guia de conversação;Buy a phrasebook.;Compre um guia de conversação.
""")
FIELD['Compras']=_l("""
mall;shopping;A busy mall.;Um shopping movimentado.
department store;loja de departamentos;A big department store.;Uma grande loja de departamentos.
boutique;butique;A small boutique.;Uma butique pequena.
market stall;barraca de feira;A fruit market stall.;Uma barraca de frutas.
grocery;mercado;Buy groceries.;Compre mantimentos.
aisle;corredor;Aisle three.;Corredor três.
shopping cart;carrinho de compras;A full shopping cart.;Um carrinho cheio.
basket;cesta;A small basket.;Uma cesta pequena.
checkout;caixa;Go to the checkout.;Vá ao caixa.
cashier;caixa (pessoa);A friendly cashier.;Um caixa simpático.
receipt;recibo;Keep the receipt.;Guarde o recibo.
price tag;etiqueta de preço;Read the price tag.;Leia a etiqueta de preço.
discount;desconto;A big discount.;Um grande desconto.
coupon;cupom;Use this coupon.;Use este cupom.
bargain;pechincha;A real bargain.;Uma pechincha real.
clearance;liquidação;A clearance sale.;Uma liquidação.
special offer;oferta especial;A special offer.;Uma oferta especial.
refund;reembolso;Ask for a refund.;Peça reembolso.
exchange;troca;An easy exchange.;Uma troca fácil.
warranty;garantia;A long warranty.;Uma garantia longa.
fitting room;provador;The fitting room is free.;O provador está livre.
size;tamanho;What size?;Qual tamanho?
medium;médio;A medium shirt.;Uma camisa média.
large;grande;A large coat.;Um casaco grande.
tight;apertado;These jeans are tight.;Esta calça está apertada.
loose;folgado;A loose shirt.;Uma camisa folgada.
fit;servir;It fits well.;Serve bem.
sleeve;manga;A long sleeve.;Uma manga longa.
collar;gola;A white collar.;Uma gola branca.
pocket;bolso;A deep pocket.;Um bolso fundo.
zipper;zíper;A broken zipper.;Um zíper quebrado.
button;botão;A missing button.;Um botão faltando.
leather;couro;A leather bag.;Uma bolsa de couro.
cotton;algodão;A cotton shirt.;Uma camisa de algodão.
wool;lã;A wool sweater.;Um suéter de lã.
silk;seda;A silk scarf.;Um lenço de seda.
denim;jeans (tecido);Denim jacket.;Jaqueta jeans.
stripes;listras;Blue stripes.;Listras azuis.
pattern;estampa;A flower pattern.;Uma estampa de flores.
plain;liso;A plain shirt.;Uma camisa lisa.
trendy;da moda;A trendy jacket.;Uma jaqueta da moda.
second-hand;de segunda mão;A second-hand bike.;Uma bicicleta de segunda mão.
brand;marca;A famous brand.;Uma marca famosa.
label;etiqueta;Check the label.;Confira a etiqueta.
shopping bag;sacola;A paper shopping bag.;Uma sacola de papel.
gift card;vale-presente;A gift card.;Um vale-presente.
wrapping paper;papel de embrulho;Colorful wrapping paper.;Papel de embrulho colorido.
online order;pedido online;An online order.;Um pedido online.
delivery;entrega;Fast delivery.;Entrega rápida.
tracking number;código de rastreio;Enter the tracking number.;Digite o código de rastreio.
package;pacote;A small package.;Um pacote pequeno.
shipping;frete;Free shipping.;Frete grátis.
credit card;cartão de crédito;Pay by credit card.;Pague com cartão de crédito.
cash;dinheiro vivo;Pay in cash.;Pague em dinheiro.
change;troco;Count the change.;Conte o troco.
pay;pagar;Pay at the counter.;Pague no balcão.
afford;ter condições de pagar;I can’t afford it.;Não posso pagar isso.
cheap;barato;A cheap shirt.;Uma camisa barata.
expensive;caro;An expensive watch.;Um relógio caro.
reasonable;razoável;A reasonable price.;Um preço razoável.
sold out;esgotado;It is sold out.;Está esgotado.
in stock;em estoque;Is it in stock?;Está em estoque?
customer service;atendimento ao cliente;Call customer service.;Ligue para o atendimento.
""")
FIELD['Saúde cotidiana']=_l("""
health;saúde;Good health.;Boa saúde.
illness;doença;A mild illness.;Uma doença leve.
symptom;sintoma;A common symptom.;Um sintoma comum.
fever;febre;A high fever.;Uma febre alta.
cough;tosse;A dry cough.;Uma tosse seca.
sore throat;dor de garganta;I have a sore throat.;Estou com dor de garganta.
runny nose;nariz escorrendo;A runny nose.;Um nariz escorrendo.
headache;dor de cabeça;A bad headache.;Uma dor de cabeça forte.
stomachache;dor de barriga;I have a stomachache.;Estou com dor de barriga.
toothache;dor de dente;A terrible toothache.;Uma dor de dente terrível.
backache;dor nas costas;A constant backache.;Uma dor nas costas constante.
dizzy;tonto;I feel dizzy.;Sinto-me tonto.
nausea;náusea;A wave of nausea.;Uma onda de náusea.
rash;erupção;A red rash.;Uma erupção vermelha.
allergy;alergia;A pollen allergy.;Uma alergia a pólen.
infection;infecção;A throat infection.;Uma infecção de garganta.
flu;gripe;The flu is back.;A gripe voltou.
cold;resfriado;A bad cold.;Um resfriado forte.
sprain;torção;An ankle sprain.;Uma torção no tornozelo.
bruise;hematoma;A purple bruise.;Um hematoma roxo.
cut;corte;A small cut.;Um corte pequeno.
burn;queimadura;A minor burn.;Uma queimadura leve.
bandage;curativo;Change the bandage.;Troque o curativo.
cast;gesso;A cast on his arm.;Um gesso no braço dele.
crutches;muletas;He uses crutches.;Ele usa muletas.
wheelchair;cadeira de rodas;A folding wheelchair.;Uma cadeira de rodas dobrável.
ambulance;ambulância;Call an ambulance.;Chame uma ambulância.
emergency;emergência;An emergency room.;Um pronto-socorro.
waiting room;sala de espera;The waiting room is full.;A sala de espera está cheia.
appointment;consulta;Book an appointment.;Marque uma consulta.
check-up;exame de rotina;A yearly check-up.;Um exame anual.
prescription;receita;A new prescription.;Uma nova receita.
pharmacy;farmácia;Visit the pharmacy.;Visite a farmácia.
pill;comprimido;Take one pill.;Tome um comprimido.
tablet;pastilha;A white tablet.;Uma pastilha branca.
syrup;xarope;Cough syrup.;Xarope para tosse.
ointment;pomada;Apply the ointment.;Aplique a pomada.
drops;gotas;Eye drops.;Colírio.
vitamin;vitamina;Take a vitamin.;Tome uma vitamina.
dose;dose;The right dose.;A dose certa.
side effect;efeito colateral;A mild side effect.;Um efeito colateral leve.
thermometer;termômetro;Use a thermometer.;Use um termômetro.
blood pressure;pressão arterial;Check blood pressure.;Meça a pressão.
pulse;pulso;A slow pulse.;Um pulso lento.
x-ray;raio-X;Take an x-ray.;Faça um raio-X.
test;exame;A blood test.;Um exame de sangue.
vaccine;vacina;Get a vaccine.;Tome uma vacina.
injection;injeção;A small injection.;Uma injeção pequena.
surgery;cirurgia;A short surgery.;Uma cirurgia curta.
recovery;recuperação;A fast recovery.;Uma recuperação rápida.
rest;repouso;Get plenty of rest.;Descanse bastante.
diet;dieta;A balanced diet.;Uma dieta equilibrada.
exercise;exercício;Daily exercise.;Exercício diário.
sleep;sono;Eight hours of sleep.;Oito horas de sono.
stress;estresse;Reduce stress.;Reduza o estresse.
dentist;dentista;Visit the dentist.;Visite o dentista.
filling;obturação;A new filling.;Uma obturação nova.
glasses;óculos;New glasses.;Óculos novos.
contact lenses;lentes de contato;Wear contact lenses.;Use lentes de contato.
hearing aid;aparelho auditivo;A small hearing aid.;Um aparelho auditivo pequeno.
patient;paciente;A new patient.;Um novo paciente.
nurse;enfermeiro;A kind nurse.;Um enfermeiro gentil.
specialist;especialista;See a specialist.;Consulte um especialista.
""")
try:
    from pools2 import F2
    from pools3 import F3
    from pools4 import F4
    from pools5 import F5
    from pools6 import G6
    for _d in(F2,F3,F4,F5):
        for _k,_v in _d.items():FIELD[_k]=FIELD.get(_k,[])+_v
    for _k in list(FIELD):FIELD[_k]=FIELD[_k]+G6
except ImportError:pass
EXPRS=_l("""
Could I ask something?=Posso perguntar uma coisa?
I’m just looking.=Só estou olhando.
It’s up to you.=Você decide.
Take your time.=Sem pressa.
Just a moment, please.=Só um momento, por favor.
That sounds fun!=Parece divertido!
Let me think.=Deixe-me pensar.
I’ll be right back.=Já volto.
What’s up?=E aí?
Good luck!=Boa sorte!
Be careful!=Tenha cuidado!
Here you go.=Aqui está.
How about you?=E você?
I don’t mind.=Não me importo.
Help yourself.=Sirva-se.
Keep in touch.=Mantenha contato.
Could you repeat that?=Pode repetir?
I’m looking forward to it.=Estou ansioso por isso.
What do you recommend?=O que você recomenda?
It depends.=Depende.
Never mind.=Deixa pra lá.
That’s a good idea.=Boa ideia.
I’m on my way.=Estou a caminho.
Hang on a second.=Espere um segundo.
What a surprise!=Que surpresa!
I’d love to.=Eu adoraria.
Sorry I’m late.=Desculpe o atraso.
It’s a deal.=Combinado.
Say hello for me.=Dê um oi por mim.
Get well soon.=Melhoras.
Congratulations!=Parabéns!
Thanks for your help.=Obrigado pela ajuda.
I’m afraid not.=Receio que não.
Cheers!=Saúde!
Right on time.=Bem na hora.
Out of order.=Fora de serviço.
On sale.=Em promoção.
Do me a favor.=Faça-me um favor.
Not bad.=Nada mal.
Make up your mind.=Decida-se.
Let’s get started.=Vamos começar.
Let’s call it a day.=Vamos encerrar por hoje.
Don’t worry about it.=Não se preocupe.
It’s not a big deal.=Não é nada demais.
I’ve got a question.=Tenho uma pergunta.
Could you do me a favor?=Pode me fazer um favor?
I’ll take care of it.=Eu cuido disso.
It’s on the house.=É por conta da casa.
That’s very kind of you.=É muito gentil da sua parte.
Take it easy.=Vá com calma.
Have a seat.=Sente-se.
Make yourself comfortable.=Fique à vontade.
I couldn’t agree more.=Concordo plenamente.
You’re welcome.=De nada.
Excuse me for a moment.=Com licença um momento.
I beg your pardon?=Como disse?
What do you mean?=O que você quer dizer?
Is that all?=É só isso?
How come?=Como assim?
No way!=De jeito nenhum!
Me too.=Eu também.
So do I.=Eu também (afirmativo).
Neither do I.=Eu também não.
I see what you mean.=Entendo o que você quer dizer.
That makes sense.=Isso faz sentido.
It’s worth a try.=Vale a tentativa.
Better late than never.=Antes tarde do que nunca.
Practice makes perfect.=A prática leva à perfeição.
Easy come, easy go.=O que vem fácil, vai fácil.
First things first.=Primeiro o mais importante.
Time flies.=O tempo voa.
Better safe than sorry.=Melhor prevenir que remediar.
Let’s keep in contact.=Vamos manter contato.
See you next time.=Até a próxima.
Give me a call.=Me ligue.
Drop me a line.=Mande-me um recado.
Pick up the pace.=Acelere.
Lend me a hand.=Me dê uma mão.
Watch your step.=Cuidado onde pisa.
Mind the gap.=Cuidado com o vão.
Fasten your seat belt.=Aperte o cinto.
Wait your turn.=Espere sua vez.
Ladies first.=As damas primeiro.
Break the ice.=Quebrar o gelo.
Piece of cake.=Moleza.
Under the weather.=Meio doente.
Once in a while.=De vez em quando.
As soon as possible.=O mais rápido possível.
By the way.=A propósito.
On the other hand.=Por outro lado.
In the meantime.=Enquanto isso.
All of a sudden.=De repente.
At the moment.=No momento.
In a hurry.=Com pressa.
For a change.=Para variar.
Just in case.=Por precaução.
""")
VERBS=_l("""
open;abrir;I open the window.;She opens the door.
close;fechar;I close the door.;He closes the window.
begin;começar;We begin at nine.;She begins early.
finish;terminar;I finish at five.;He finishes soon.
carry;carregar;I carry a bag.;She carries a box.
push;empurrar;I push the door.;He pushes the cart.
pull;puxar;I pull the rope.;She pulls the door.
throw;jogar;I throw the ball.;He throws a stone.
catch;pegar;I catch the bus.;She catches the ball.
send;enviar;I send a letter.;She sends a text.
receive;receber;I receive a gift.;He receives mail.
borrow;pegar emprestado;I borrow a pen.;She borrows a book.
lend;emprestar;I lend a pen.;He lends money.
sell;vender;I sell fruit.;She sells cars.
choose;escolher;I choose a seat.;She chooses red.
win;ganhar;I win a prize.;He wins often.
lose;perder;I lose my keys.;She loses time.
forget;esquecer;I forget names.;He forgets keys.
remember;lembrar;I remember you.;She remembers it.
smell;cheirar;I smell flowers.;It smells good.
taste;provar;I taste soup.;It tastes sweet.
sound;soar;It sounds fun.;That sounds good.
laugh;rir;We laugh a lot.;She laughs loudly.
cry;chorar;I cry at movies.;The baby cries.
shout;gritar;Don’t shout.;He shouts loudly.
whisper;sussurrar;I whisper to her.;He whispers softly.
stand;ficar de pé;I stand in line.;She stands up.
hurry;apressar-se;I hurry home.;She hurries to work.
invite;convidar;I invite friends.;She invites us.
agree;concordar;I agree with you.;He agrees with me.
believe;acreditar;I believe you.;She believes him.
guess;adivinhar;I guess the answer.;He guesses well.
count;contar;I count to ten.;She counts coins.
spell;soletrar;I spell my name.;She spells it.
translate;traduzir;I translate texts.;She translates it.
move;mover, mudar-se;I move the chair.;She moves house.
change;mudar;I change my plan.;She changes jobs.
turn;virar;I turn left.;She turns right.
follow;seguir;I follow the map.;He follows me.
lead;liderar;I lead the team.;She leads well.
join;juntar-se;I join the club.;She joins us.
share;dividir;I share a room.;She shares food.
trust;confiar;I trust you.;He trusts her.
fix;consertar;I fix bikes.;He fixes the door.
build;construir;I build models.;She builds houses.
break;quebrar;I break a plate.;He breaks a rule.
cut;cortar;I cut bread.;She cuts the paper.
draw;desenhar;I draw flowers.;She draws well.
paint;pintar;I paint walls.;He paints boats.
sing;cantar;I sing songs.;She sings well.
dance;dançar;I dance salsa.;She dances well.
jump;pular;I jump high.;He jumps rope.
climb;escalar;I climb hills.;She climbs trees.
swim;nadar;I swim daily.;He swims fast.
fly;voar;I fly to Rome.;Birds fly south.
ride;andar de;I ride a bike.;She rides a horse.
park;estacionar;I park here.;He parks outside.
pay;pagar;I pay cash.;She pays the bill.
cost;custar;It costs ten.;That costs a lot.
spend;gastar;I spend little.;He spends time.
save;economizar;I save money.;She saves time.
earn;ganhar (salário);I earn little.;She earns well.
wear;usar (roupa);I wear a coat.;She wears blue.
fit;servir;It fits me.;This fits well.
hurt;machucar;My leg hurts.;His back hurts.
heal;cicatrizar;It heals fast.;The cut heals.
feel;sentir;I feel tired.;She feels fine.
need;precisar;I need help.;She needs time.
prefer;preferir;I prefer tea.;He prefers coffee.
mean;significar;What does it mean?;It means “yes”.
happen;acontecer;What happened?;It happens often.
seem;parecer;It seems fine.;She seems happy.
become;tornar-se;I become tired.;She becomes calm.
grow;crescer;I grow tomatoes.;Kids grow fast.
die;morrer;Plants die in winter.;The fire dies.
live;morar;I live here.;She lives alone.
""")
EXPRS+=_l("""
I was wondering if…=Eu queria saber se…
Would you mind…?=Você se importaria de…?
I’d appreciate it.=Eu agradeceria.
Do you mind if I…?=Você se importa se eu…?
Would it be possible to…?=Seria possível…?
I’m afraid I can’t.=Receio que não possa.
That’s exactly what I need.=É exatamente o que preciso.
It’s not what I expected.=Não é o que eu esperava.
How much is it altogether?=Quanto custa tudo junto?
Do you accept cards?=Vocês aceitam cartão?
Can I pay by card?=Posso pagar com cartão?
Could I get a receipt?=Posso ter um recibo?
Is this on sale?=Isto está em promoção?
Do you have a smaller size?=Tem um tamanho menor?
It doesn’t fit.=Não serve.
I’ll think about it.=Vou pensar.
I’ll take it.=Vou levar.
Keep the change.=Fique com o troco.
Is there a discount?=Tem desconto?
What time do you close?=A que horas fecham?
Where can I find…?=Onde posso achar…?
Could you point me to…?=Pode me indicar…?
It’s on the second floor.=Fica no segundo andar.
It’s right behind you.=Está logo atrás de você.
Go straight ahead.=Siga em frente.
Turn left at the corner.=Vire à esquerda na esquina.
It’s a five-minute walk.=São cinco minutos a pé.
You can’t miss it.=Não tem como errar.
Which platform?=Qual plataforma?
Is this seat taken?=Este lugar está ocupado?
How long is the flight?=Quanto dura o voo?
What time does it leave?=A que horas sai?
Is breakfast included?=O café da manhã está incluído?
Could I have the key, please?=Pode me dar a chave, por favor?
I’d like to check out.=Gostaria de fazer check-out.
Is there a bus to…?=Tem ônibus para…?
How much is the fare?=Quanto é a tarifa?
Can I get a refund?=Posso ter reembolso?
My flight was canceled.=Meu voo foi cancelado.
I’ve lost my passport.=Perdi meu passaporte.
I have a reservation.=Tenho uma reserva.
I’m here on vacation.=Estou aqui de férias.
It’s my first time here.=É minha primeira vez aqui.
What’s worth seeing?=O que vale a pena ver?
Could you take a photo?=Pode tirar uma foto?
Is it far from here?=Fica longe daqui?
I don’t feel well.=Não estou me sentindo bem.
I have a headache.=Estou com dor de cabeça.
I need to see a doctor.=Preciso ver um médico.
It hurts here.=Dói aqui.
How long have you had it?=Há quanto tempo você sente isso?
Take this twice a day.=Tome isto duas vezes ao dia.
Get plenty of rest.=Descanse bastante.
Drink lots of water.=Beba muita água.
You should see a specialist.=Você deveria ver um especialista.
It’s nothing serious.=Não é nada grave.
I’m allergic to…=Sou alérgico a…
I feel much better.=Sinto-me muito melhor.
What seems to be the problem?=Qual parece ser o problema?
Do you have any allergies?=Tem alguma alergia?
Open wide, please.=Abra bem a boca, por favor.
Breathe in, breathe out.=Inspire, expire.
Roll up your sleeve.=Arregace a manga.
It won’t hurt.=Não vai doer.
Make an appointment.=Marque uma consulta.
Can I reschedule?=Posso remarcar?
Something came up.=Surgiu um imprevisto.
I’m running late.=Estou atrasado.
I’ll be there in ten minutes.=Chego em dez minutos.
Sorry to keep you waiting.=Desculpe a espera.
Thanks for waiting.=Obrigado por esperar.
I’m afraid it’s sold out.=Receio que esteja esgotado.
Is that everything?=É tudo?
Anything else?=Algo mais?
Will that be all?=Será só isso?
For here or to go?=Para comer aqui ou levar?
Here’s your change.=Aqui está seu troco.
Have a good one!=Tenha um ótimo dia!
Same to you!=Igualmente!
Don’t mention it.=Não há de quê.
My pleasure.=O prazer é meu.
I’m glad to hear that.=Fico feliz em saber.
I’m sorry to hear that.=Sinto muito saber disso.
What a pity!=Que pena!
That’s a shame.=É uma pena.
Lucky you!=Que sorte a sua!
Poor thing!=Coitadinho!
Good for you!=Que bom para você!
You’re kidding!=Você está brincando!
I can’t believe it!=Não acredito!
Hold on a minute.=Espere um minuto.
Could you speak more slowly?=Pode falar mais devagar?
How do you pronounce this?=Como se pronuncia isto?
What’s the word for…?=Qual é a palavra para…?
I’m not sure I understand.=Não tenho certeza se entendo.
Could you spell that?=Pode soletrar?
Is this right?=Isto está certo?
I got it.=Entendi.
Let me see.=Deixe-me ver.
Let me get this straight.=Deixe-me entender direito.
Sounds like a plan.=Parece um bom plano.
Count me in.=Pode contar comigo.
Count me out.=Pode me tirar dessa.
I’m up for it.=Topo.
I’m not in the mood.=Não estou a fim.
It’s my turn.=É minha vez.
After you.=Depois de você.
Go ahead.=Vá em frente.
Be my guest.=Fique à vontade.
Mind your head.=Cuidado com a cabeça.
Watch out!=Cuidado!
Look out!=Atenção!
Hands up!=Mãos ao alto!
Stay tuned.=Fique ligado.
Keep it up!=Continue assim!
Way to go!=Muito bem!
Nice job!=Bom trabalho!
Well done!=Muito bem!
Good point.=Bom argumento.
Fair enough.=Justo.
Exactly!=Exatamente!
Absolutely!=Com certeza!
Not really.=Na verdade, não.
Not at all.=De jeito nenhum.
Sort of.=Mais ou menos.
Kind of.=Meio que.
More or less.=Mais ou menos.
As usual.=Como sempre.
As I said…=Como eu disse…
To be honest…=Para ser honesto…
Frankly speaking…=Falando francamente…
In my opinion…=Na minha opinião…
As far as I know…=Até onde sei…
If you ask me…=Se você quer saber…
By the way…=A propósito…
Anyway…=De qualquer modo…
So far so good.=Até agora tudo bem.
Better than nothing.=Melhor que nada.
Better luck next time.=Mais sorte da próxima vez.
Out of sight, out of mind.=Longe dos olhos, longe do coração.
Actions speak louder than words.=Ações valem mais que palavras.
Where there’s a will, there’s a way.=Querer é poder.
Rome wasn’t built in a day.=Roma não foi construída em um dia.
""")
EXPRS+=_l("""
I’m on it.=Estou cuidando disso.
That’s news to me.=Isso é novidade para mim.
It’s a long story.=É uma longa história.
Long story short…=Resumindo…
What’s the catch?=Qual é a pegadinha?
It’s a piece of cake.=É moleza.
It slipped my mind.=Esqueci completamente.
It’s on the tip of my tongue.=Está na ponta da língua.
I’m all ears.=Sou todo ouvidos.
Speak of the devil.=Falando no diabo.
You never know.=Nunca se sabe.
It’s not my cup of tea.=Não é a minha praia.
Let’s split the bill.=Vamos dividir a conta.
This one’s on me.=Esta é por minha conta.
I’m stuffed.=Estou cheio.
I’m starving.=Estou morrendo de fome.
I’m exhausted.=Estou exausto.
I’m so tired.=Estou muito cansado.
I’m thrilled.=Estou empolgado.
I’m fed up.=Estou farto.
I’m in a hurry.=Estou com pressa.
I’m in a bad mood.=Estou de mau humor.
I’m off today.=Estou de folga hoje.
I’m out of cash.=Estou sem dinheiro.
I’m broke.=Estou sem grana.
I’m between jobs.=Estou entre empregos.
I’m on vacation.=Estou de férias.
I’m on a diet.=Estou de dieta.
I’m lost.=Estou perdido.
I’m all set.=Estou pronto.
I’m done.=Terminei.
I’m with you.=Estou com você.
I’m not into it.=Não curto isso.
I’m into music.=Curto música.
I’m new here.=Sou novo aqui.
I’m just passing through.=Só estou de passagem.
I’m getting off here.=Vou descer aqui.
I’m getting there.=Estou chegando lá.
I’m working on it.=Estou trabalhando nisso.
I’m looking for…=Estou procurando…
I’m used to it.=Estou acostumado.
I’m about to leave.=Estou prestes a sair.
I’m supposed to…=Eu deveria…
I’d rather stay home.=Prefiro ficar em casa.
I’d better go.=É melhor eu ir.
I’d like a refund.=Gostaria de um reembolso.
I’d like to make a reservation.=Gostaria de fazer uma reserva.
We’re out of milk.=Acabou o leite.
We’re running out of time.=Estamos ficando sem tempo.
We’re in luck.=Estamos com sorte.
We’re almost there.=Estamos quase lá.
We’ll see.=Vamos ver.
We’d better hurry.=É melhor nos apressarmos.
You’ve got a point.=Você tem razão.
You’re right.=Você tem razão.
You’re not alone.=Você não está sozinho.
You’re in my way.=Você está no meu caminho.
You look great!=Você está ótimo!
You must be joking.=Você deve estar brincando.
You should try it.=Você deveria experimentar.
You’d better not.=É melhor não.
You can say that again.=Pode apostar.
You bet.=Pode apostar.
You name it.=O que você quiser.
It’s my fault.=É minha culpa.
It’s about time.=Já era hora.
It’s no use.=Não adianta.
It’s no wonder.=Não é de admirar.
It’s a pleasure.=É um prazer.
It’s a small world.=O mundo é pequeno.
It’s getting late.=Está ficando tarde.
It’s getting dark.=Está escurecendo.
It’s raining cats and dogs.=Está chovendo canivete.
It’s freezing.=Está congelando.
It’s boiling hot.=Está um forno.
It’s a lovely day.=É um dia lindo.
It’s a long way.=É um longo caminho.
It’s worth it.=Vale a pena.
It’s time to go.=É hora de ir.
It’s okay.=Tudo bem.
It happens.=Acontece.
It doesn’t matter.=Não importa.
It makes no difference.=Não faz diferença.
It means a lot.=Significa muito.
It looks great.=Parece ótimo.
It tastes awful.=Está com gosto horrível.
It smells good.=Cheira bem.
It feels soft.=É macio ao toque.
It sounds familiar.=Parece familiar.
""")
EXPRS+=_l("""
I’d say…=Eu diria que…
As far as I’m concerned…=No que me diz respeito…
I’m under the impression that…=Tenho a impressão de que…
It seems to me that…=Parece-me que…
I tend to think…=Costumo achar…
I’m inclined to agree.=Tendo a concordar.
That’s not how I see it.=Não vejo assim.
I take your point.=Entendo seu argumento.
Let me put it this way.=Deixe-me dizer assim.
What I mean is…=O que quero dizer é…
Let me rephrase that.=Deixe-me reformular.
To sum up…=Resumindo…
All in all…=No geral…
On the whole…=Em geral…
Generally speaking…=De modo geral…
In a nutshell…=Em poucas palavras…
First of all…=Antes de mais nada…
Last but not least…=Por último, mas não menos importante…
In addition…=Além disso…
Moreover…=Além do mais…
However…=No entanto…
Nevertheless…=Mesmo assim…
As a result…=Como resultado…
For this reason…=Por essa razão…
That’s why…=É por isso que…
Because of this…=Por causa disso…
In order to…=A fim de…
So as to…=Para…
Instead of…=Em vez de…
Apart from that…=Fora isso…
Except for…=Exceto…
According to…=De acordo com…
In terms of…=Em termos de…
With regard to…=Com relação a…
As for me…=Quanto a mim…
It goes without saying…=Nem é preciso dizer…
Needless to say…=Nem é preciso dizer…
Believe it or not…=Acredite ou não…
Strange but true.=Estranho, mas verdade.
To tell the truth…=Para dizer a verdade…
Come to think of it…=Pensando bem…
Now that you mention it…=Agora que você falou…
That reminds me…=Isso me lembra…
Speaking of which…=Por falar nisso…
Before I forget…=Antes que eu esqueça…
By the way, did you hear…?=A propósito, você soube…?
Guess what!=Adivinhe só!
You won’t believe this.=Você não vai acreditar.
It turns out that…=Acontece que…
It happened to me once.=Aconteceu comigo uma vez.
I’ll never forget the day…=Nunca vou esquecer o dia…
It was a close call.=Foi por pouco.
It made my day.=Alegrou meu dia.
It was a blast.=Foi demais.
It was a nightmare.=Foi um pesadelo.
It was nothing special.=Não foi nada de especial.
It was out of this world.=Foi sensacional.
It cost me a fortune.=Me custou uma fortuna.
It was a rip-off.=Foi um roubo.
It was a steal.=Foi uma pechincha.
It’s worth every penny.=Vale cada centavo.
It’s a bit pricey.=É um pouco caro.
It’s within my budget.=Cabe no meu orçamento.
I’ll split it with you.=Divido com você.
I’ll pay my share.=Pago minha parte.
Could we split the bill?=Podemos dividir a conta?
Do you take reservations?=Vocês aceitam reservas?
We’d like a table for four.=Gostaríamos de uma mesa para quatro.
Could we sit outside?=Podemos sentar do lado de fora?
What’s today’s special?=Qual é o prato do dia?
I’ll have the same.=Quero o mesmo.
Could I get a refill?=Pode encher de novo?
Could we have the check?=Pode trazer a conta?
Keep the change, please.=Fique com o troco, por favor.
I’d like to book a table.=Gostaria de reservar uma mesa.
I’d like to cancel my booking.=Gostaria de cancelar minha reserva.
Could I change my reservation?=Posso alterar minha reserva?
I’m afraid we’re fully booked.=Receio que estejamos lotados.
There’s a waiting list.=Há lista de espera.
Please hold the line.=Aguarde na linha.
I’ll put you through.=Vou transferir sua ligação.
Could you call me back?=Pode me ligar de volta?
I’ll get back to you.=Retorno para você.
Could I leave a message?=Posso deixar um recado?
Speak up, please.=Fale mais alto, por favor.
You’re breaking up.=Está cortando.
The line is bad.=A linha está ruim.
I’ll text you.=Mando uma mensagem.
Send me the details.=Me mande os detalhes.
Let’s stay in touch.=Vamos manter contato.
Thanks anyway.=Obrigado de qualquer forma.
Sorry for the trouble.=Desculpe o incômodo.
No harm done.=Sem problema.
It’s my bad.=Foi mal.
I owe you one.=Te devo uma.
You saved my life.=Você salvou minha vida.
I can’t thank you enough.=Não tenho como agradecer.
Don’t mention it.=Imagina.
It’s the least I could do.=É o mínimo que eu podia fazer.
""")
VERBS+=_l("""
accept;aceitar;I accept the offer.;She accepts gifts.
achieve;alcançar;I achieve my goals.;He achieves a lot.
add;adicionar;I add salt.;She adds sugar.
admire;admirar;I admire her.;He admires art.
admit;admitir;I admit my mistake.;He admits it.
adopt;adotar;I adopt a dog.;She adopts a cat.
advise;aconselhar;I advise you.;She advises him.
afford;ter condições de pagar;I can’t afford it.;He can afford it.
allow;permitir;I allow it.;She allows it.
announce;anunciar;I announce a plan.;He announces news.
appear;aparecer;Stars appear.;She appears at nine.
apply;candidatar-se;I apply for a job.;She applies today.
arrange;organizar;I arrange a trip.;He arranges a party.
attend;frequentar;I attend class.;She attends church.
avoid;evitar;I avoid noise.;He avoids sugar.
bake;assar;I bake bread.;She bakes cakes.
behave;comportar-se;I behave well.;He behaves badly.
belong;pertencer;It belongs to me.;She belongs here.
blame;culpar;I blame myself.;He blames us.
blow;soprar;I blow out candles.;The wind blows.
bother;incomodar;Don’t bother me.;It bothers him.
breathe;respirar;I breathe slowly.;She breathes deeply.
burn;queimar;I burn toast.;It burns fast.
calm;acalmar;I calm the baby.;She calms him.
care;importar-se;I care about you.;He cares a lot.
celebrate;comemorar;We celebrate today.;She celebrates her birthday.
chat;conversar;We chat online.;She chats with friends.
cheer;torcer;We cheer loudly.;He cheers for his team.
collect;colecionar;I collect stamps.;She collects coins.
compare;comparar;I compare prices.;She compares two phones.
complain;reclamar;I complain rarely.;He complains often.
connect;conectar;I connect the cable.;She connects the TV.
copy;copiar;I copy the text.;He copies files.
cover;cobrir;I cover the pot.;She covers her head.
create;criar;I create art.;He creates games.
damage;danificar;Rain damages roofs.;It damages the car.
deliver;entregar;I deliver mail.;She delivers pizza.
depend;depender;It depends.;She depends on him.
disappear;desaparecer;Clouds disappear.;It disappears fast.
discover;descobrir;I discover new places.;He discovers a path.
discuss;discutir (um tema);We discuss plans.;She discusses it.
divide;dividir;I divide the cake.;He divides the work.
dream;sonhar;I dream of travel.;She dreams a lot.
dress;vestir;I dress quickly.;She dresses well.
drop;deixar cair;I drop my keys.;He drops a glass.
earn;ganhar (salário);I earn little.;She earns more.
educate;educar;We educate children.;She educates adults.
enter;entrar;I enter the room.;He enters quietly.
escape;escapar;I escape the heat.;The cat escapes.
exist;existir;Dragons don’t exist.;It exists.
expect;esperar;I expect rain.;She expects a call.
explore;explorar;I explore the city.;He explores caves.
fail;falhar;I fail sometimes.;It fails twice.
fall;cair;Leaves fall.;She falls asleep.
fill;encher;I fill the glass.;She fills the tank.
fold;dobrar;I fold the shirt.;He folds the map.
gain;ganhar (obter);I gain weight.;She gains confidence.
gather;reunir;We gather here.;She gathers wood.
greet;cumprimentar;I greet my neighbor.;She greets guests.
guide;guiar;I guide tourists.;He guides us.
handle;lidar com;I handle problems.;She handles stress.
hide;esconder;I hide the gift.;He hides the key.
hire;contratar;We hire students.;She hires a chef.
hug;abraçar;I hug my mother.;He hugs his son.
imagine;imaginar;I imagine a beach.;She imagines it.
improve;melhorar;I improve daily.;It improves fast.
include;incluir;It includes breakfast.;The price includes tax.
increase;aumentar;Prices increase.;It increases daily.
introduce;apresentar;I introduce my friend.;She introduces him.
join;juntar-se;I join the club.;He joins us.
judge;julgar;I judge fairly.;He judges the contest.
kick;chutar;I kick the ball.;He kicks hard.
knock;bater (na porta);I knock twice.;She knocks softly.
lift;levantar;I lift a box.;He lifts weights.
manage;conseguir, gerenciar;I manage a shop.;She manages well.
mark;marcar;I mark the date.;She marks the page.
mention;mencionar;I mention it.;He mentions your name.
miss;perder;I miss the bus.;She misses home.
mix;misturar;I mix colors.;She mixes the batter.
notice;notar;I notice details.;He notices a change.
obey;obedecer;I obey rules.;The dog obeys.
operate;operar;I operate machines.;She operates daily.
pack;arrumar mala;I pack a bag.;She packs light.
pass;passar;I pass the salt.;She passes the exam.
perform;apresentar-se;I perform on stage.;He performs well.
plan;planejar;I plan a trip.;She plans carefully.
prepare;preparar;I prepare dinner.;He prepares a talk.
protect;proteger;I protect my phone.;She protects kids.
prove;provar;I prove my point.;It proves nothing.
punish;punir;We don’t punish kids.;He punishes crime.
recommend;recomendar;I recommend this book.;She recommends tea.
reduce;reduzir;I reduce waste.;He reduces costs.
refuse;recusar;I refuse the offer.;She refuses to go.
remove;remover;I remove the lid.;He removes the stain.
repeat;repetir;I repeat the word.;She repeats it.
rescue;resgatar;I rescue animals.;He rescues a cat.
rest;descansar;I rest at noon.;She rests a lot.
reserve;reservar;I reserve a table.;She reserves a seat.
""")
EXPRS+=_l("""
Don’t get me wrong.=Não me leve a mal.
Let’s get down to business.=Vamos ao que interessa.
It’s a long shot.=É uma aposta arriscada.
It’s a close call.=Foi por pouco.
It’s a win-win.=É bom para os dois lados.
It’s all good.=Está tudo bem.
It’s all Greek to me.=Não entendo nada.
It’s anyone’s guess.=Ninguém sabe.
It’s up in the air.=Está indefinido.
It’s on the way.=Está a caminho.
It’s out of the question.=Está fora de cogitação.
It’s not rocket science.=Não é nenhuma ciência.
It’s about time.=Já era hora.
It’s better than nothing.=É melhor que nada.
It could be worse.=Poderia ser pior.
It couldn’t be better.=Não poderia ser melhor.
It takes two to tango.=É preciso dois para dançar.
It runs in the family.=É de família.
It rings a bell.=Isso me lembra algo.
It slipped through the cracks.=Passou despercebido.
It was touch and go.=Foi por um fio.
It’s no big deal.=Não é nada demais.
Let it go.=Deixe pra lá.
Let me know.=Me avise.
Let me handle it.=Deixe comigo.
Let’s not jump to conclusions.=Não vamos tirar conclusões precipitadas.
Let’s play it by ear.=Vamos improvisar.
Let’s sleep on it.=Vamos dormir sobre isso.
Let’s touch base.=Vamos nos falar.
Let’s wrap this up.=Vamos finalizar.
Hold your horses.=Calma aí.
Hang in there.=Aguente firme.
Hang on.=Aguarde.
Keep an eye on it.=Fique de olho.
Keep me posted.=Me mantenha informado.
Keep your chin up.=Cabeça erguida.
Make a long story short.=Resumindo.
Make yourself heard.=Faça-se ouvir.
Mind your own business.=Cuide da sua vida.
Pull yourself together.=Recomponha-se.
Put yourself in my shoes.=Ponha-se no meu lugar.
Read between the lines.=Leia nas entrelinhas.
See eye to eye.=Concordar plenamente.
Speak your mind.=Diga o que pensa.
Take it or leave it.=É pegar ou largar.
Take my word for it.=Acredite em mim.
Take a rain check.=Deixar para outra vez.
Take it with a grain of salt.=Não leve tão a sério.
Think outside the box.=Pense fora da caixa.
Turn over a new leaf.=Começar de novo.
Walk on eggshells.=Pisar em ovos.
Work out the details.=Acertar os detalhes.
Cut to the chase.=Ir direto ao ponto.
Beat around the bush.=Enrolar.
Bite the bullet.=Encarar o problema.
Call it a day.=Encerrar por hoje.
Face the music.=Encarar as consequências.
Get cold feet.=Ficar com medo.
Go the extra mile.=Dar um passo além.
Jump on the bandwagon.=Aderir à moda.
Miss the boat.=Perder a oportunidade.
Hit the road.=Pegar a estrada.
Hit the books.=Estudar com afinco.
Hit the sack.=Ir dormir.
Under the weather.=Meio doente.
Over the moon.=Nas nuvens.
Out of the blue.=Do nada.
On the same page.=Na mesma sintonia.
On cloud nine.=Nas nuvens.
In the same boat.=No mesmo barco.
In hot water.=Em apuros.
In a nutshell.=Resumindo.
In the long run.=A longo prazo.
In the nick of time.=Em cima da hora.
At the end of the day.=No fim das contas.
At first sight.=À primeira vista.
At your service.=Às suas ordens.
By all means.=Com certeza.
By heart.=De cor.
For good.=Para sempre.
For sure.=Com certeza.
From scratch.=Do zero.
Once and for all.=De uma vez por todas.
Sooner or later.=Cedo ou tarde.
Step by step.=Passo a passo.
Word for word.=Palavra por palavra.
Back to square one.=De volta à estaca zero.
Back on track.=De volta aos trilhos.
Ahead of schedule.=Adiantado.
Behind schedule.=Atrasado.
On a tight budget.=Com orçamento apertado.
On the other side.=Do outro lado.
Right away.=Imediatamente.
Right now.=Agora mesmo.
Any time.=A qualquer hora.
Any day now.=A qualquer dia.
Every now and then.=De vez em quando.
Now and again.=Vez ou outra.
No matter what.=Não importa o quê.
No wonder.=Não é de admirar.
No offense.=Sem ofensa.
No hard feelings.=Sem ressentimentos.
No strings attached.=Sem compromisso.
No pain, no gain.=Sem esforço, sem resultado.
Not at all.=De jeito nenhum.
Not to mention…=Sem falar de…
Not that I know of.=Não que eu saiba.
""")
