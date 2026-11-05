def _l(s):return [x.strip() for x in s.strip().splitlines() if x.strip()]
F2={}
F2['Moradia']=_l("""
condo;condomínio;A new condo.;Um condomínio novo.
duplex;duplex;A bright duplex.;Um duplex claro.
penthouse;cobertura;A luxury penthouse.;Uma cobertura de luxo.
studio;quitinete;A tiny studio.;Uma quitinete minúscula.
loft;loft;A modern loft.;Um loft moderno.
farmhouse;casa de fazenda;An old farmhouse.;Uma casa de fazenda antiga.
cabin;cabana;A wooden cabin.;Uma cabana de madeira.
mansion;mansão;A huge mansion.;Uma mansão enorme.
doorknob;maçaneta;A brass doorknob.;Uma maçaneta de latão.
doormat;capacho;A new doormat.;Um capacho novo.
mailbox;caixa de correio;An empty mailbox.;Uma caixa de correio vazia.
peephole;olho mágico;Look through the peephole.;Olhe pelo olho mágico.
intercom;interfone;Use the intercom.;Use o interfone.
lobby;saguão;The building lobby.;O saguão do prédio.
elevator;elevador;A slow elevator.;Um elevador lento.
basement;porão;A damp basement.;Um porão úmido.
attic;sótão;A dusty attic.;Um sótão empoeirado.
chimney;chaminé;A tall chimney.;Uma chaminé alta.
fireplace;lareira;A warm fireplace.;Uma lareira quente.
shutters;venezianas;Green shutters.;Venezianas verdes.
skylight;claraboia;A bright skylight.;Uma claraboia clara.
patio;pátio;A stone patio.;Um pátio de pedra.
porch;varanda de entrada;A wooden porch.;Uma varanda de madeira.
driveway;entrada de carros;A long driveway.;Uma entrada longa.
lawn;gramado;A neat lawn.;Um gramado aparado.
hedge;cerca viva;A green hedge.;Uma cerca viva verde.
mailslot;fenda de correio;A brass mailslot.;Uma fenda de correio de latão.
bookshelf;prateleira de livros;A crowded bookshelf.;Uma prateleira cheia de livros.
cushion;almofada;A soft cushion.;Uma almofada macia.
rug;tapete;A woolen rug.;Um tapete de lã.
wallpaper;papel de parede;Flowery wallpaper.;Papel de parede florido.
chandelier;lustre;A crystal chandelier.;Um lustre de cristal.
bulb;lâmpada;A bright bulb.;Uma lâmpada forte.
extension cord;extensão;Use an extension cord.;Use uma extensão.
smoke alarm;detector de fumaça;Test the smoke alarm.;Teste o detector de fumaça.
fire extinguisher;extintor;Keep a fire extinguisher.;Mantenha um extintor.
thermostat;termostato;Set the thermostat.;Regule o termostato.
pipe;cano;A leaking pipe.;Um cano vazando.
leak;vazamento;Fix the leak.;Conserte o vazamento.
plumber;encanador;Call the plumber.;Chame o encanador.
electrician;eletricista;Call the electrician.;Chame o eletricista.
repair;conserto;A quick repair.;Um conserto rápido.
renovation;reforma;A big renovation.;Uma grande reforma.
furniture;mobília;Second-hand furniture.;Mobília de segunda mão.
delivery;entrega;Furniture delivery.;Entrega de móveis.
assembly;montagem;Easy assembly.;Montagem fácil.
instructions;instruções;Read the instructions.;Leia as instruções.
cardboard;papelão;A cardboard box.;Uma caixa de papelão.
storage room;depósito;A small storage room.;Um depósito pequeno.
garage door;portão de garagem;Open the garage door.;Abra o portão da garagem.
bike rack;bicicletário;A bike rack.;Um bicicletário.
security;segurança;Good security.;Boa segurança.
doorman;porteiro;The doorman greets us.;O porteiro nos cumprimenta.
superintendent;zelador;Call the superintendent.;Chame o zelador.
tenant;inquilino;A quiet tenant.;Um inquilino calmo.
deposit;depósito (garantia);Pay a deposit.;Pague uma garantia.
utilities;contas de casa;Utilities are extra.;As contas são à parte.
electricity;eletricidade;Save electricity.;Economize eletricidade.
gas bill;conta de gás;Pay the gas bill.;Pague a conta de gás.
internet;internet;Fast internet.;Internet rápida.
heating;aquecimento;Central heating.;Aquecimento central.
cooling;refrigeração;Home cooling.;Refrigeração residencial.
insulation;isolamento;Good insulation.;Bom isolamento.
noise;barulho;Too much noise.;Barulho demais.
neighbor;vizinho;A noisy neighbor.;Um vizinho barulhento.
""")
F2['Trabalho']=_l("""
workplace;local de trabalho;A friendly workplace.;Um local de trabalho simpático.
career;carreira;A long career.;Uma carreira longa.
position;cargo;An open position.;Um cargo em aberto.
vacancy;vaga;A new vacancy.;Uma vaga nova.
candidate;candidato;A strong candidate.;Um candidato forte.
reference;referência;A good reference.;Uma boa referência.
skill;habilidade;A useful skill.;Uma habilidade útil.
experience;experiência;Two years of experience.;Dois anos de experiência.
training;treinamento;Staff training.;Treinamento da equipe.
internship;estágio;A summer internship.;Um estágio de verão.
apprentice;aprendiz;A young apprentice.;Um jovem aprendiz.
manager;gerente;A fair manager.;Um gerente justo.
team leader;líder de equipe;A calm team leader.;Um líder de equipe calmo.
colleague;colega;A kind colleague.;Uma colega gentil.
assistant;assistente;A helpful assistant.;Uma assistente prestativa.
client;cliente;A new client.;Um novo cliente.
contract;contrato;A signed contract.;Um contrato assinado.
payslip;holerite;Check your payslip.;Confira seu holerite.
tax;imposto;Pay your tax.;Pague seu imposto.
benefits;benefícios;Good benefits.;Bons benefícios.
vacation days;dias de férias;Ten vacation days.;Dez dias de férias.
sick leave;licença médica;Take sick leave.;Tire licença médica.
maternity leave;licença-maternidade;She is on maternity leave.;Ela está de licença-maternidade.
retirement;aposentadoria;An early retirement.;Uma aposentadoria antecipada.
commute;trajeto até o trabalho;A long commute.;Um trajeto longo.
office hours;horário de expediente;Office hours are nine to five.;O expediente é das nove às cinco.
lunch hour;hora do almoço;A short lunch hour.;Uma hora de almoço curta.
break room;sala de descanso;The break room is small.;A sala de descanso é pequena.
cubicle;baia;A quiet cubicle.;Uma baia silenciosa.
laptop;notebook;A light laptop.;Um notebook leve.
spreadsheet;planilha;Open the spreadsheet.;Abra a planilha.
database;banco de dados;A large database.;Um grande banco de dados.
password;senha;Change your password.;Mude sua senha.
network;rede;The network is down.;A rede caiu.
software;software;New software.;Software novo.
update;atualização;A system update.;Uma atualização do sistema.
backup;cópia de segurança;Make a backup.;Faça uma cópia de segurança.
email;e-mail;Send an email.;Envie um e-mail.
attachment;anexo;Open the attachment.;Abra o anexo.
subject line;assunto;Write a subject line.;Escreva um assunto.
agenda;pauta;Check the agenda.;Confira a pauta.
minutes;ata;Take the minutes.;Faça a ata.
goal;meta;A sales goal.;Uma meta de vendas.
target;objetivo;Hit the target.;Atinja o objetivo.
performance;desempenho;Good performance.;Bom desempenho.
feedback;retorno;Useful feedback.;Retorno útil.
review;avaliação;A yearly review.;Uma avaliação anual.
teamwork;trabalho em equipe;Good teamwork.;Bom trabalho em equipe.
leadership;liderança;Strong leadership.;Liderança forte.
negotiation;negociação;A tough negotiation.;Uma negociação difícil.
customer complaint;reclamação de cliente;Handle a customer complaint.;Resolva uma reclamação.
warehouse;armazém;A big warehouse.;Um armazém grande.
delivery truck;caminhão de entrega;A delivery truck.;Um caminhão de entrega.
assembly line;linha de montagem;An assembly line.;Uma linha de montagem.
safety helmet;capacete de segurança;Wear a safety helmet.;Use capacete de segurança.
uniform;uniforme;A clean uniform.;Um uniforme limpo.
name tag;crachá;Wear a name tag.;Use um crachá.
union;sindicato;Join the union.;Filie-se ao sindicato.
strike;greve;A long strike.;Uma greve longa.
unemployed;desempregado;An unemployed worker.;Um trabalhador desempregado.
freelance;autônomo;A freelance designer.;Uma designer autônoma.
remote;remoto;Remote work.;Trabalho remoto.
startup;startup;A small startup.;Uma startup pequena.
company;empresa;A big company.;Uma grande empresa.
branch;filial;A new branch.;Uma nova filial.
headquarters;sede;The headquarters.;A sede.
""")
F2['Lazer']=_l("""
leisure;lazer;Leisure time.;Tempo de lazer.
pastime;passatempo;A quiet pastime.;Um passatempo calmo.
craft;artesanato;A craft class.;Uma aula de artesanato.
pottery;cerâmica;Pottery lessons.;Aulas de cerâmica.
sculpture;escultura;A stone sculpture.;Uma escultura de pedra.
photography;fotografia;Black-and-white photography.;Fotografia em preto e branco.
baking;confeitaria;Home baking.;Confeitaria caseira.
sewing;costura;Sewing lessons.;Aulas de costura.
bird-watching;observação de aves;A bird-watching trip.;Uma viagem para observar aves.
stargazing;observar estrelas;A night of stargazing.;Uma noite de observação de estrelas.
kayaking;caiaque;Go kayaking.;Faça caiaque.
surfing;surfe;Learn surfing.;Aprenda surfe.
skiing;esqui;A skiing trip.;Uma viagem de esqui.
skating;patinação;Ice skating.;Patinação no gelo.
rock climbing;escalada;Rock climbing.;Escalada.
jogging;corrida leve;Morning jogging.;Corrida leve matinal.
volleyball;vôlei;Play volleyball.;Jogue vôlei.
basketball;basquete;A basketball court.;Uma quadra de basquete.
baseball;beisebol;A baseball game.;Um jogo de beisebol.
tennis;tênis;A tennis match.;Uma partida de tênis.
golf;golfe;A golf course.;Um campo de golfe.
bowling;boliche;Go bowling.;Jogue boliche.
darts;dardos;Play darts.;Jogue dardos.
karaoke;karaokê;A karaoke night.;Uma noite de karaokê.
magic trick;truque de mágica;A magic trick.;Um truque de mágica.
joke;piada;Tell a joke.;Conte uma piada.
riddle;charada;Solve a riddle.;Resolva uma charada.
crossword;palavras cruzadas;A crossword puzzle.;Palavras cruzadas.
trivia;perguntas e respostas;A trivia night.;Uma noite de perguntas e respostas.
quiz show;programa de perguntas;A TV quiz show.;Um programa de perguntas.
talk show;programa de entrevistas;A talk show.;Um programa de entrevistas.
reality show;reality show;A reality show.;Um reality show.
cartoon;desenho animado;A funny cartoon.;Um desenho animado engraçado.
trailer;trailer;A movie trailer.;Um trailer de filme.
sequel;continuação;A good sequel.;Uma boa continuação.
director;diretor;A famous director.;Um diretor famoso.
plot;enredo;A simple plot.;Um enredo simples.
review;crítica;A film review.;Uma crítica de filme.
bookstore;livraria;A cozy bookstore.;Uma livraria aconchegante.
bestseller;best-seller;A new bestseller.;Um novo best-seller.
audiobook;audiolivro;Listen to an audiobook.;Ouça um audiolivro.
blog;blog;A travel blog.;Um blog de viagem.
vlog;vlog;A daily vlog.;Um vlog diário.
subscriber;inscrito;A new subscriber.;Um novo inscrito.
livestream;transmissão ao vivo;Watch the livestream.;Assista à transmissão ao vivo.
app;aplicativo;A free app.;Um aplicativo grátis.
game console;console;A game console.;Um console.
joystick;controle;A wireless joystick.;Um controle sem fio.
level;fase;The last level.;A última fase.
weekend trip;viagem de fim de semana;A weekend trip.;Uma viagem de fim de semana.
barbecue;churrasco;A Sunday barbecue.;Um churrasco de domingo.
picnic;piquenique;A family picnic.;Um piquenique em família.
bonfire;fogueira;A night bonfire.;Uma fogueira noturna.
fireworks;fogos de artifício;Bright fireworks.;Fogos brilhantes.
parade;desfile;A colorful parade.;Um desfile colorido.
carnival;carnaval;A street carnival.;Um carnaval de rua.
fair;feira;A country fair.;Uma feira rural.
flea market;feira de pulgas;A flea market.;Uma feira de pulgas.
raffle;rifa;A charity raffle.;Uma rifa beneficente.
club;clube;A chess club.;Um clube de xadrez.
member;membro;A club member.;Um membro do clube.
""")
F2['Lugares']=_l("""
cathedral;catedral;A tall cathedral.;Uma catedral alta.
ruins;ruínas;Ancient ruins.;Ruínas antigas.
tower;torre;A clock tower.;Uma torre de relógio.
skyscraper;arranha-céu;A glass skyscraper.;Um arranha-céu de vidro.
bridge;ponte;A suspension bridge.;Uma ponte suspensa.
alley;beco;A narrow alley.;Um beco estreito.
roundabout;rotatória;Take the roundabout.;Pegue a rotatória.
overpass;viaduto;Under the overpass.;Debaixo do viaduto.
highway;rodovia;A busy highway.;Uma rodovia movimentada.
toll;pedágio;Pay the toll.;Pague o pedágio.
bus terminal;terminal de ônibus;A crowded bus terminal.;Um terminal de ônibus lotado.
ferry terminal;terminal de balsa;The ferry terminal.;O terminal de balsa.
marina;marina;A quiet marina.;Uma marina tranquila.
lighthouse;farol;A white lighthouse.;Um farol branco.
cliff;penhasco;A high cliff.;Um penhasco alto.
cave;caverna;A dark cave.;Uma caverna escura.
waterfall;cachoeira;A tall waterfall.;Uma cachoeira alta.
canyon;cânion;A deep canyon.;Um cânion fundo.
volcano;vulcão;An active volcano.;Um vulcão ativo.
glacier;geleira;A blue glacier.;Uma geleira azul.
meadow;campo;A green meadow.;Um campo verde.
orchard;pomar;An apple orchard.;Um pomar de maçãs.
vineyard;vinhedo;A quiet vineyard.;Um vinhedo calmo.
ranch;rancho;A horse ranch.;Um rancho de cavalos.
barn;celeiro;A red barn.;Um celeiro vermelho.
windmill;moinho de vento;An old windmill.;Um moinho de vento antigo.
dam;represa;A huge dam.;Uma represa enorme.
reservoir;reservatório;A full reservoir.;Um reservatório cheio.
swamp;pântano;A wet swamp.;Um pântano úmido.
jungle;selva;A thick jungle.;Uma selva densa.
savanna;savana;A dry savanna.;Uma savana seca.
tundra;tundra;A cold tundra.;Uma tundra fria.
coral reef;recife de coral;A coral reef.;Um recife de coral.
bay;baía;A calm bay.;Uma baía calma.
cape;cabo;A rocky cape.;Um cabo rochoso.
peninsula;península;A long peninsula.;Uma península longa.
continent;continente;A large continent.;Um continente grande.
province;província;A small province.;Uma província pequena.
county;condado;A rural county.;Um condado rural.
district;distrito;A historic district.;Um distrito histórico.
campus;campus;A green campus.;Um campus verde.
courthouse;fórum;The old courthouse.;O fórum antigo.
city hall;prefeitura;Visit city hall.;Visite a prefeitura.
embassy;embaixada;The embassy is closed.;A embaixada está fechada.
prison;prisão;An old prison.;Uma prisão antiga.
theme park;parque temático;A big theme park.;Um grande parque temático.
skating rink;pista de patinação;A skating rink.;Uma pista de patinação.
swimming pool;piscina;A public swimming pool.;Uma piscina pública.
sports center;centro esportivo;A sports center.;Um centro esportivo.
bookstore;livraria;A tiny bookstore.;Uma livraria minúscula.
bakery;padaria;A French bakery.;Uma padaria francesa.
butcher shop;açougue;A local butcher shop.;Um açougue local.
laundromat;lavanderia self-service;A laundromat.;Uma lavanderia self-service.
barber shop;barbearia;A barber shop.;Uma barbearia.
beauty salon;salão de beleza;A beauty salon.;Um salão de beleza.
florist;floricultura;A small florist.;Uma floricultura pequena.
toy store;loja de brinquedos;A toy store.;Uma loja de brinquedos.
hardware store;loja de ferragens;A hardware store.;Uma loja de ferragens.
pet shop;pet shop;A pet shop.;Um pet shop.
travel agency;agência de viagens;A travel agency.;Uma agência de viagens.
gas station;posto;An old gas station.;Um posto antigo.
car wash;lava-jato;A car wash.;Um lava-jato.
parking garage;garagem;A parking garage.;Uma garagem.
rest area;área de descanso;A rest area.;Uma área de descanso.
""")
F2['Viagens']=_l("""
travel agent;agente de viagens;Ask the travel agent.;Pergunte ao agente de viagens.
package tour;pacote turístico;A package tour.;Um pacote turístico.
all-inclusive;tudo incluído;An all-inclusive resort.;Um resort tudo incluído.
off-season;baixa temporada;Travel off-season.;Viaje na baixa temporada.
high season;alta temporada;High season prices.;Preços de alta temporada.
bargain flight;voo barato;Find a bargain flight.;Ache um voo barato.
direct flight;voo direto;A direct flight.;Um voo direto.
connecting flight;voo de conexão;Miss a connecting flight.;Perca um voo de conexão.
window seat;assento na janela;A window seat.;Um assento na janela.
aisle seat;assento no corredor;An aisle seat.;Um assento no corredor.
overhead bin;bagageiro;The overhead bin.;O bagageiro.
seat belt;cinto;Fasten your seat belt.;Aperte o cinto.
turbulence;turbulência;Some turbulence.;Alguma turbulência.
landing;pouso;A smooth landing.;Um pouso suave.
take-off;decolagem;An early take-off.;Uma decolagem cedo.
baggage claim;esteira de bagagem;Wait at baggage claim.;Espere na esteira.
arrivals;chegadas;The arrivals hall.;O saguão de chegadas.
departures;partidas;The departures board.;O painel de partidas.
information desk;balcão de informações;Ask at the information desk.;Pergunte no balcão de informações.
ticket office;bilheteria;The ticket office.;A bilheteria.
vending machine;máquina de venda;A vending machine.;Uma máquina de venda.
platform;plataforma;Platform five.;Plataforma cinco.
carriage;vagão;The first carriage.;O primeiro vagão.
conductor;condutor;The conductor checks tickets.;O condutor confere as passagens.
bus fare;tarifa de ônibus;A cheap bus fare.;Uma tarifa de ônibus barata.
metro map;mapa do metrô;Check the metro map.;Confira o mapa do metrô.
rental agency;locadora;A car rental agency.;Uma locadora de carros.
driver’s license;carteira de motorista;Show your driver’s license.;Mostre a carteira de motorista.
road trip;viagem de carro;A summer road trip.;Uma viagem de carro de verão.
detour;desvio;Take a detour.;Faça um desvio.
roadside;beira da estrada;A roadside café.;Um café de beira de estrada.
motel;motel;A cheap motel.;Um motel barato.
bed and breakfast;pousada;A cozy bed and breakfast.;Uma pousada aconchegante.
youth hostel;albergue da juventude;A youth hostel.;Um albergue da juventude.
dorm bed;cama em dormitório;A dorm bed.;Uma cama em dormitório.
check-out time;horário de saída;Check-out time is noon.;O horário de saída é meio-dia.
late check-out;saída tardia;Ask for a late check-out.;Peça saída tardia.
wake-up call;serviço de despertar;Book a wake-up call.;Peça um serviço de despertar.
minibar;frigobar;The minibar is full.;O frigobar está cheio.
safe;cofre;Use the room safe.;Use o cofre do quarto.
towel;toalha;Extra towels.;Toalhas extras.
view;vista;A sea view.;Uma vista para o mar.
balcony;sacada;A private balcony.;Uma sacada privativa.
pool;piscina;The hotel pool.;A piscina do hotel.
spa;spa;A hotel spa.;Um spa de hotel.
concierge;concierge;Ask the concierge.;Pergunte ao concierge.
bellhop;carregador;The bellhop helps.;O carregador ajuda.
tour guide;guia turístico;A funny tour guide.;Um guia turístico engraçado.
audio guide;audioguia;Rent an audio guide.;Alugue um audioguia.
entrance fee;taxa de entrada;The entrance fee.;A taxa de entrada.
opening hours;horário de funcionamento;Check the opening hours.;Confira o horário de funcionamento.
queue;fila;A long queue.;Uma fila longa.
crowded;lotado;A crowded square.;Uma praça lotada.
tourist trap;armadilha para turistas;Avoid tourist traps.;Evite armadilhas para turistas.
local food;comida local;Try local food.;Experimente comida local.
street food;comida de rua;Cheap street food.;Comida de rua barata.
specialty;especialidade;A local specialty.;Uma especialidade local.
bargaining;pechincha;Practice bargaining.;Pratique a pechincha.
sunscreen;protetor solar;Bring sunscreen.;Leve protetor solar.
mosquito repellent;repelente;Use mosquito repellent.;Use repelente.
first-aid kit;kit de primeiros socorros;Pack a first-aid kit.;Leve um kit de primeiros socorros.
power adapter;adaptador de tomada;Bring a power adapter.;Leve um adaptador de tomada.
travel pillow;travesseiro de viagem;A travel pillow.;Um travesseiro de viagem.
""")
F2['Compras']=_l("""
shopper;comprador;A smart shopper.;Um comprador esperto.
window shopping;olhar vitrines;Go window shopping.;Olhe vitrines.
shopping spree;farra de compras;A shopping spree.;Uma farra de compras.
sale season;época de promoções;The sale season.;A época de promoções.
black friday;black friday;Black Friday deals.;Ofertas de Black Friday.
price drop;queda de preço;A big price drop.;Uma grande queda de preço.
buy one get one;leve dois pague um;Buy one get one free.;Leve dois pague um.
loyalty card;cartão fidelidade;Use a loyalty card.;Use um cartão fidelidade.
membership;associação;A store membership.;Uma associação da loja.
cashback;dinheiro de volta;Get cashback.;Receba dinheiro de volta.
installment;parcela;Pay in installments.;Pague em parcelas.
down payment;entrada;A small down payment.;Uma entrada pequena.
interest;juros;High interest.;Juros altos.
debit card;cartão de débito;Pay by debit card.;Pague com cartão de débito.
contactless;por aproximação;Pay contactless.;Pague por aproximação.
PIN;senha do cartão;Enter your PIN.;Digite sua senha.
cash register;caixa registradora;The cash register.;A caixa registradora.
barcode;código de barras;Scan the barcode.;Leia o código de barras.
self-checkout;caixa automático;Use self-checkout.;Use o caixa automático.
bag fee;taxa de sacola;A bag fee.;Uma taxa de sacola.
reusable bag;sacola reutilizável;Bring a reusable bag.;Leve uma sacola reutilizável.
expiry date;validade;Check the expiry date.;Confira a validade.
ingredients list;lista de ingredientes;Read the ingredients list.;Leia a lista de ingredientes.
organic;orgânico;Organic vegetables.;Legumes orgânicos.
frozen;congelado;Frozen peas.;Ervilhas congeladas.
canned;enlatado;Canned beans.;Feijão enlatado.
fresh produce;hortifrúti;Fresh produce.;Hortifrúti fresco.
dairy;laticínios;The dairy aisle.;O corredor de laticínios.
bakery section;seção de padaria;The bakery section.;A seção de padaria.
deli counter;balcão de frios;The deli counter.;O balcão de frios.
sample;amostra;A free sample.;Uma amostra grátis.
cosmetics;cosméticos;A cosmetics store.;Uma loja de cosméticos.
perfume;perfume;A strong perfume.;Um perfume forte.
sunglasses;óculos de sol;New sunglasses.;Óculos de sol novos.
scarf;cachecol;A wool scarf.;Um cachecol de lã.
gloves;luvas;Warm gloves.;Luvas quentes.
sneakers;tênis;White sneakers.;Tênis brancos.
sandals;sandálias;Summer sandals.;Sandálias de verão.
boots;botas;Leather boots.;Botas de couro.
handbag;bolsa;A black handbag.;Uma bolsa preta.
belt;cinto;A leather belt.;Um cinto de couro.
tie;gravata;A silk tie.;Uma gravata de seda.
suit;terno;A grey suit.;Um terno cinza.
dress;vestido;A summer dress.;Um vestido de verão.
skirt;saia;A short skirt.;Uma saia curta.
jacket;jaqueta;A warm jacket.;Uma jaqueta quente.
raincoat;capa de chuva;A yellow raincoat.;Uma capa de chuva amarela.
swimsuit;roupa de banho;A new swimsuit.;Uma roupa de banho nova.
underwear;roupa íntima;Cotton underwear.;Roupa íntima de algodão.
pajamas;pijama;Soft pajamas.;Pijama macio.
toy;brinquedo;A wooden toy.;Um brinquedo de madeira.
electronics;eletrônicos;An electronics store.;Uma loja de eletrônicos.
headphones;fones de ouvido;Wireless headphones.;Fones sem fio.
charger;carregador;A phone charger.;Um carregador de celular.
tablet;tablet;A new tablet.;Um tablet novo.
camera;câmera;A digital camera.;Uma câmera digital.
printer ink;tinta de impressora;Buy printer ink.;Compre tinta de impressora.
stationery;papelaria;A stationery shop.;Uma papelaria.
furniture store;loja de móveis;A furniture store.;Uma loja de móveis.
flea market;feira de usados;A Sunday flea market.;Uma feira de usados de domingo.
auction;leilão;An online auction.;Um leilão online.
""")
F2['Saúde cotidiana']=_l("""
wellness;bem-estar;A wellness routine.;Uma rotina de bem-estar.
fitness;condicionamento;Good fitness.;Bom condicionamento.
workout;treino;A short workout.;Um treino curto.
warm-up;aquecimento;A quick warm-up.;Um aquecimento rápido.
cool-down;desaquecimento;A slow cool-down.;Um desaquecimento lento.
stretching;alongamento;Daily stretching.;Alongamento diário.
push-up;flexão;Do ten push-ups.;Faça dez flexões.
sit-up;abdominal;Do twenty sit-ups.;Faça vinte abdominais.
treadmill;esteira;Run on the treadmill.;Corra na esteira.
dumbbell;halter;A heavy dumbbell.;Um halter pesado.
gym membership;mensalidade da academia;Cancel the gym membership.;Cancele a mensalidade da academia.
personal trainer;personal trainer;Hire a personal trainer.;Contrate um personal trainer.
protein;proteína;Rich in protein.;Rico em proteína.
carbohydrate;carboidrato;Slow carbohydrates.;Carboidratos lentos.
fat;gordura;Low in fat.;Pouca gordura.
calorie;caloria;Count calories.;Conte calorias.
fiber;fibra;High in fiber.;Rico em fibra.
mineral;mineral;A daily mineral.;Um mineral diário.
supplement;suplemento;Take a supplement.;Tome um suplemento.
hydration;hidratação;Good hydration.;Boa hidratação.
balanced diet;dieta equilibrada;Eat a balanced diet.;Coma uma dieta equilibrada.
junk food;comida lixo;Avoid junk food.;Evite comida lixo.
sugar;açúcar;Cut down on sugar.;Reduza o açúcar.
salt;sal;Too much salt.;Sal demais.
snack;lanche;A healthy snack.;Um lanche saudável.
portion size;tamanho da porção;Watch the portion size.;Cuide do tamanho da porção.
overweight;acima do peso;Feel overweight.;Sentir-se acima do peso.
underweight;abaixo do peso;Be underweight.;Estar abaixo do peso.
scale;balança;Step on the scale.;Suba na balança.
height;altura;Measure your height.;Meça sua altura.
weight;peso;Check your weight.;Confira seu peso.
posture;postura;Good posture.;Boa postura.
muscle;músculo;A strong muscle.;Um músculo forte.
joint;articulação;A sore joint.;Uma articulação dolorida.
bone;osso;A broken bone.;Um osso quebrado.
skin;pele;Dry skin.;Pele seca.
hair;cabelo;Healthy hair.;Cabelo saudável.
nail;unha;A short nail.;Uma unha curta.
eyesight;visão;Good eyesight.;Boa visão.
hearing;audição;Poor hearing.;Audição ruim.
breathing;respiração;Slow breathing.;Respiração lenta.
heartbeat;batimento cardíaco;A fast heartbeat.;Um batimento cardíaco rápido.
blood;sangue;A blood sample.;Uma amostra de sangue.
lung;pulmão;A healthy lung.;Um pulmão saudável.
mental health;saúde mental;Care for mental health.;Cuide da saúde mental.
anxiety;ansiedade;Reduce anxiety.;Reduza a ansiedade.
meditation;meditação;Daily meditation.;Meditação diária.
therapy;terapia;Go to therapy.;Faça terapia.
relaxation;relaxamento;A moment of relaxation.;Um momento de relaxamento.
insomnia;insônia;Suffer from insomnia.;Sofrer de insônia.
nap;cochilo;A short nap.;Um cochilo curto.
sunburn;queimadura de sol;A bad sunburn.;Uma queimadura de sol forte.
mosquito bite;picada de mosquito;An itchy mosquito bite.;Uma picada de mosquito que coça.
first aid;primeiros socorros;Learn first aid.;Aprenda primeiros socorros.
hand sanitizer;álcool em gel;Use hand sanitizer.;Use álcool em gel.
face mask;máscara;Wear a face mask.;Use máscara.
health insurance;plano de saúde;Check health insurance.;Confira o plano de saúde.
medical record;prontuário;Ask for your medical record.;Peça seu prontuário.
referral;encaminhamento;Get a referral.;Receba um encaminhamento.
""")
for _k,_v in F2.items():
    pass
