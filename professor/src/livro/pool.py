"""Reserva de vocabulário A0–A1 (palavra;tradução;exemplo;tradução do exemplo) para trocar repetições e abastecer as revisões."""
RAW="""
mother;mãe;My mother cooks well.;Minha mãe cozinha bem.
father;pai;My father drives a bus.;Meu pai dirige um ônibus.
sister;irmã;My sister is ten.;Minha irmã tem dez anos.
daughter;filha;Her daughter is shy.;A filha dela é tímida.
son;filho;His son plays football.;O filho dele joga futebol.
uncle;tio;My uncle lives in Rio.;Meu tio mora no Rio.
aunt;tia;My aunt visits on Sunday.;Minha tia visita no domingo.
cousin;primo;My cousin is a nurse.;Meu primo é enfermeiro.
grandmother;avó;My grandmother makes cake.;Minha avó faz bolo.
grandfather;avô;My grandfather tells stories.;Meu avô conta histórias.
husband;marido;Her husband is a pilot.;O marido dela é piloto.
wife;esposa;His wife is a teacher.;A esposa dele é professora.
baby;bebê;The baby sleeps.;O bebê dorme.
boy;menino;The boy runs fast.;O menino corre rápido.
girl;menina;The girl reads a book.;A menina lê um livro.
man;homem;The man is tall.;O homem é alto.
woman;mulher;The woman is kind.;A mulher é gentil.
child;criança;The child is happy.;A criança está feliz.
people;pessoas;Many people like music.;Muitas pessoas gostam de música.
neighbour;vizinho;My neighbour is friendly.;Meu vizinho é simpático.
pilot;piloto;The pilot is calm.;O piloto está calmo.
nurse;enfermeiro;The nurse helps people.;O enfermeiro ajuda pessoas.
farmer;agricultor;The farmer has cows.;O agricultor tem vacas.
driver;motorista;The driver is polite.;O motorista é educado.
singer;cantor;The singer is famous.;O cantor é famoso.
artist;artista;The artist paints flowers.;O artista pinta flores.
dentist;dentista;The dentist is kind.;O dentista é gentil.
cook;cozinheiro;The cook makes soup.;O cozinheiro faz sopa.
lawyer;advogado;The lawyer works downtown.;O advogado trabalha no centro.
police;polícia;The police help us.;A polícia nos ajuda.
head;cabeça;My head hurts.;Minha cabeça dói.
face;rosto;Wash your face.;Lave o rosto.
eye;olho;I have brown eyes.;Tenho olhos castanhos.
ear;orelha;My ear is cold.;Minha orelha está fria.
nose;nariz;Her nose is small.;O nariz dela é pequeno.
mouth;boca;Open your mouth.;Abra a boca.
tooth;dente;I brush my teeth.;Escovo os dentes.
arm;braço;My arm is strong.;Meu braço é forte.
leg;perna;My leg hurts.;Minha perna dói.
foot;pé;My foot is big.;Meu pé é grande.
finger;dedo;Ten fingers.;Dez dedos.
back;costas;My back hurts.;Minhas costas doem.
stomach;barriga;My stomach hurts.;Minha barriga dói.
heart;coração;A kind heart.;Um coração bondoso.
shirt;camisa;A white shirt.;Uma camisa branca.
shoe;sapato;I need new shoes.;Preciso de sapatos novos.
sock;meia;A pair of socks.;Um par de meias.
hat;chapéu;She wears a hat.;Ela usa um chapéu.
jeans;calça jeans;My jeans are blue.;Minha calça jeans é azul.
skirt;saia;A long skirt.;Uma saia longa.
sweater;suéter;A warm sweater.;Um suéter quente.
pocket;bolso;Keys in my pocket.;Chaves no meu bolso.
belt;cinto;A black belt.;Um cinto preto.
glasses;óculos;I wear glasses.;Uso óculos.
bag;bolsa;A heavy bag.;Uma bolsa pesada.
wallet;carteira;My wallet is empty.;Minha carteira está vazia.
umbrella;guarda-chuva;Take an umbrella.;Leve um guarda-chuva.
watch;relógio;A new watch.;Um relógio novo.
ring;anel;A gold ring.;Um anel de ouro.
mirror;espelho;Look in the mirror.;Olhe no espelho.
sofa;sofá;A soft sofa.;Um sofá macio.
bed;cama;A big bed.;Uma cama grande.
shelf;prateleira;Books on the shelf.;Livros na prateleira.
carpet;tapete;A red carpet.;Um tapete vermelho.
curtain;cortina;Close the curtain.;Feche a cortina.
wall;parede;A white wall.;Uma parede branca.
floor;chão;The floor is clean.;O chão está limpo.
roof;telhado;A red roof.;Um telhado vermelho.
garden;jardim;A green garden.;Um jardim verde.
garage;garagem;The car is in the garage.;O carro está na garagem.
bathroom;banheiro;The bathroom is clean.;O banheiro está limpo.
bedroom;quarto;My bedroom is small.;Meu quarto é pequeno.
living room;sala de estar;The living room is big.;A sala de estar é grande.
stairs;escada;Go up the stairs.;Suba a escada.
bell;campainha;Ring the bell.;Toque a campainha.
towel;toalha;A clean towel.;Uma toalha limpa.
soap;sabonete;A bar of soap.;Uma barra de sabonete.
toothbrush;escova de dentes;A new toothbrush.;Uma escova de dentes nova.
blanket;cobertor;A warm blanket.;Um cobertor quente.
pillow;travesseiro;A soft pillow.;Um travesseiro macio.
clock;relógio de parede;The clock is slow.;O relógio está atrasado.
television;televisão;Turn off the television.;Desligue a televisão.
radio;rádio;Turn on the radio.;Ligue o rádio.
computer;computador;My computer is new.;Meu computador é novo.
screen;tela;A big screen.;Uma tela grande.
keyboard;teclado;A quiet keyboard.;Um teclado silencioso.
battery;bateria;The battery is low.;A bateria está fraca.
charger;carregador;Where is my charger?;Onde está meu carregador?
email;e-mail;I send an email.;Envio um e-mail.
password;senha;My password is secret.;Minha senha é secreta.
website;site;Visit our website.;Visite nosso site.
photo;foto;A nice photo.;Uma foto bonita.
video;vídeo;A short video.;Um vídeo curto.
message;mensagem;A long message.;Uma mensagem longa.
bread;pão;Fresh bread.;Pão fresco.
butter;manteiga;Butter on toast.;Manteiga na torrada.
jam;geleia;Strawberry jam.;Geleia de morango.
sugar;açúcar;Two spoons of sugar.;Duas colheres de açúcar.
salt;sal;A little salt.;Um pouco de sal.
oil;óleo;Olive oil.;Azeite.
beef;carne bovina;I like beef.;Gosto de carne bovina.
pork;carne de porco;Pork and rice.;Carne de porco e arroz.
chicken;frango;Grilled chicken.;Frango grelhado.
fish;peixe;Fresh fish.;Peixe fresco.
shrimp;camarão;Fried shrimp.;Camarão frito.
potato;batata;Boiled potatoes.;Batatas cozidas.
carrot;cenoura;A raw carrot.;Uma cenoura crua.
lettuce;alface;Green lettuce.;Alface verde.
cucumber;pepino;A cold cucumber.;Um pepino gelado.
garlic;alho;A clove of garlic.;Um dente de alho.
mushroom;cogumelo;Fried mushrooms.;Cogumelos fritos.
corn;milho;Sweet corn.;Milho doce.
peas;ervilhas;Green peas.;Ervilhas verdes.
lemon;limão;Lemon juice.;Suco de limão.
grape;uva;Sweet grapes.;Uvas doces.
pear;pera;A ripe pear.;Uma pera madura.
peach;pêssego;A juicy peach.;Um pêssego suculento.
strawberry;morango;Strawberry cake.;Bolo de morango.
watermelon;melancia;Cold watermelon.;Melancia gelada.
pineapple;abacaxi;Sweet pineapple.;Abacaxi doce.
juice;suco;Orange juice.;Suco de laranja.
tea;chá;Hot tea.;Chá quente.
beer;cerveja;A cold beer.;Uma cerveja gelada.
wine;vinho;Red wine.;Vinho tinto.
cookie;biscoito;A chocolate cookie.;Um biscoito de chocolate.
candy;doce;Sweet candy.;Doce de açúcar.
chocolate;chocolate;Dark chocolate.;Chocolate amargo.
ice cream;sorvete;Vanilla ice cream.;Sorvete de baunilha.
pizza;pizza;A hot pizza.;Uma pizza quente.
hamburger;hambúrguer;A big hamburger.;Um hambúrguer grande.
noodles;macarrão asiático;Hot noodles.;Macarrão quente.
menu;cardápio;Look at the menu.;Olhe o cardápio.
bill;conta;The bill, please.;A conta, por favor.
tip;gorjeta;Leave a tip.;Deixe uma gorjeta.
fork;garfo;A clean fork.;Um garfo limpo.
knife;faca;A sharp knife.;Uma faca afiada.
glass;copo;A glass of water.;Um copo de água.
bottle;garrafa;A bottle of milk.;Uma garrafa de leite.
can;lata;A can of soda.;Uma lata de refrigerante.
bowl;tigela;A bowl of soup.;Uma tigela de sopa.
napkin;guardanapo;A paper napkin.;Um guardanapo de papel.
breakfast;café da manhã;Breakfast is at seven.;O café da manhã é às sete.
snack;lanche;A small snack.;Um lanche pequeno.
dessert;sobremesa;Cake for dessert.;Bolo de sobremesa.
hungry;com fome;I am hungry.;Estou com fome.
thirsty;com sede;She is thirsty.;Ela está com sede.
hot;quente;Hot soup.;Sopa quente.
cold;frio;Cold water.;Água fria.
sweet;doce;A sweet cake.;Um bolo doce.
sour;azedo;A sour lemon.;Um limão azedo.
salty;salgado;Salty fries.;Batatas fritas salgadas.
delicious;delicioso;A delicious soup.;Uma sopa deliciosa.
fresh;fresco;Fresh fruit.;Fruta fresca.
cheap;barato;A cheap ticket.;Uma passagem barata.
expensive;caro;An expensive watch.;Um relógio caro.
heavy;pesado;A heavy box.;Uma caixa pesada.
light;leve;A light bag.;Uma bolsa leve.
tall;alto;A tall tree.;Uma árvore alta.
short;baixo, curto;A short skirt.;Uma saia curta.
fat;gordo;A fat cat.;Um gato gordo.
thin;magro;A thin man.;Um homem magro.
strong;forte;A strong arm.;Um braço forte.
weak;fraco;A weak tea.;Um chá fraco.
young;jovem;A young teacher.;Uma jovem professora.
old;velho;An old house.;Uma casa velha.
new;novo;A new phone.;Um celular novo.
clean;limpo;A clean room.;Um quarto limpo.
dirty;sujo;Dirty shoes.;Sapatos sujos.
empty;vazio;An empty glass.;Um copo vazio.
full;cheio;A full bag.;Uma bolsa cheia.
open;aberto;The shop is open.;A loja está aberta.
closed;fechado;The bank is closed.;O banco está fechado.
easy;fácil;An easy test.;Uma prova fácil.
difficult;difícil;A difficult word.;Uma palavra difícil.
quick;rápido;A quick lunch.;Um almoço rápido.
slow;lento;A slow train.;Um trem lento.
loud;alto (som);Loud music.;Música alta.
quiet;silencioso;A quiet street.;Uma rua silenciosa.
dark;escuro;A dark room.;Um quarto escuro.
bright;claro;A bright day.;Um dia claro.
soft;macio;A soft towel.;Uma toalha macia.
hard;duro, difícil;A hard bed.;Uma cama dura.
rich;rico;A rich man.;Um homem rico.
poor;pobre;A poor village.;Uma vila pobre.
safe;seguro;A safe place.;Um lugar seguro.
dangerous;perigoso;A dangerous road.;Uma estrada perigosa.
busy;ocupado;A busy day.;Um dia ocupado.
free;livre, grátis;A free ticket.;Uma entrada grátis.
ready;pronto;Dinner is ready.;O jantar está pronto.
sick;doente;I feel sick.;Sinto-me doente.
healthy;saudável;Healthy food.;Comida saudável.
angry;com raiva;He is angry.;Ele está com raiva.
sad;triste;She is sad today.;Ela está triste hoje.
happy;feliz;A happy child.;Uma criança feliz.
afraid;com medo;I am afraid of dogs.;Tenho medo de cães.
nervous;nervoso;I feel nervous.;Sinto-me nervoso.
bored;entediado;I am bored.;Estou entediado.
excited;animado;We are excited.;Estamos animados.
surprised;surpreso;She looks surprised.;Ela parece surpresa.
proud;orgulhoso;I am proud of you.;Tenho orgulho de você.
lonely;solitário;He feels lonely.;Ele se sente solitário.
lucky;sortudo;You are lucky.;Você tem sorte.
sleepy;com sono;I am sleepy.;Estou com sono.
dog;cachorro;A friendly dog.;Um cachorro amigável.
cat;gato;A black cat.;Um gato preto.
bird;pássaro;A small bird.;Um pássaro pequeno.
horse;cavalo;A brown horse.;Um cavalo marrom.
cow;vaca;A white cow.;Uma vaca branca.
pig;porco;A pink pig.;Um porco rosa.
chicken coop;galinheiro;The chicken coop is small.;O galinheiro é pequeno.
rabbit;coelho;A white rabbit.;Um coelho branco.
mouse;rato;A small mouse.;Um rato pequeno.
monkey;macaco;A funny monkey.;Um macaco engraçado.
lion;leão;A strong lion.;Um leão forte.
elephant;elefante;A big elephant.;Um elefante grande.
snake;cobra;A long snake.;Uma cobra longa.
duck;pato;A yellow duck.;Um pato amarelo.
insect;inseto;A small insect.;Um inseto pequeno.
butterfly;borboleta;A colorful butterfly.;Uma borboleta colorida.
tree;árvore;A tall tree.;Uma árvore alta.
flower;flor;A red flower.;Uma flor vermelha.
grass;grama;Green grass.;Grama verde.
forest;floresta;A dark forest.;Uma floresta escura.
mountain;montanha;A high mountain.;Uma montanha alta.
beach;praia;A sunny beach.;Uma praia ensolarada.
sea;mar;A blue sea.;Um mar azul.
island;ilha;A small island.;Uma ilha pequena.
sky;céu;A clear sky.;Um céu limpo.
cloud;nuvem;A white cloud.;Uma nuvem branca.
star;estrela;A bright star.;Uma estrela brilhante.
moon;lua;A full moon.;Uma lua cheia.
wind;vento;A strong wind.;Um vento forte.
snow;neve;White snow.;Neve branca.
storm;tempestade;A big storm.;Uma grande tempestade.
fog;neblina;Thick fog.;Neblina espessa.
weather;tempo (clima);Nice weather.;Tempo bom.
season;estação;My favorite season.;Minha estação favorita.
spring;primavera;Spring is warm.;A primavera é quente.
autumn;outono;Autumn is cool.;O outono é fresco.
winter;inverno;Winter is cold.;O inverno é frio.
desert;deserto;A dry desert.;Um deserto seco.
village;vila;A small village.;Uma vila pequena.
farm;fazenda;A big farm.;Uma fazenda grande.
bridge;ponte;A long bridge.;Uma ponte longa.
church;igreja;An old church.;Uma igreja antiga.
hospital;hospital;A large hospital.;Um hospital grande.
pharmacy;farmácia;The pharmacy is open.;A farmácia está aberta.
post office;correio;The post office is near.;O correio é perto.
police station;delegacia;Where is the police station?;Onde fica a delegacia?
supermarket;supermercado;I go to the supermarket.;Vou ao supermercado.
bakery;padaria;The bakery smells good.;A padaria cheira bem.
museum;museu;An old museum.;Um museu antigo.
cinema;cinema;We go to the cinema.;Vamos ao cinema.
theater;teatro;A big theater.;Um teatro grande.
stadium;estádio;A full stadium.;Um estádio lotado.
airport;aeroporto;The airport is far.;O aeroporto é longe.
station;estação;The station is busy.;A estação está movimentada.
hotel;hotel;A cheap hotel.;Um hotel barato.
market;mercado;A busy market.;Um mercado movimentado.
square;praça;A quiet square.;Uma praça silenciosa.
corner;esquina;On the corner.;Na esquina.
traffic;trânsito;Heavy traffic.;Trânsito pesado.
road;estrada;A long road.;Uma estrada longa.
train;trem;A fast train.;Um trem rápido.
plane;avião;The plane is late.;O avião está atrasado.
boat;barco;A small boat.;Um barco pequeno.
bicycle;bicicleta;A new bicycle.;Uma bicicleta nova.
motorcycle;moto;A loud motorcycle.;Uma moto barulhenta.
truck;caminhão;A big truck.;Um caminhão grande.
ticket;passagem;A train ticket.;Uma passagem de trem.
passport;passaporte;Show your passport.;Mostre seu passaporte.
suitcase;mala;A heavy suitcase.;Uma mala pesada.
map;mapa;A city map.;Um mapa da cidade.
trip;viagem;A short trip.;Uma viagem curta.
tourist;turista;A tourist asks.;Um turista pergunta.
guide;guia;The guide is friendly.;O guia é simpático.
postcard;cartão-postal;Send a postcard.;Envie um cartão-postal.
camera;câmera;A small camera.;Uma câmera pequena.
tent;barraca;A green tent.;Uma barraca verde.
engine;motor;A noisy engine.;Um motor barulhento.
fuel;combustível;Low on fuel.;Pouco combustível.
pencil;lápis;A sharp pencil.;Um lápis apontado.
eraser;borracha;I need an eraser.;Preciso de uma borracha.
ruler;régua;A long ruler.;Uma régua longa.
notebook;caderno;A blue notebook.;Um caderno azul.
backpack;mochila;A heavy backpack.;Uma mochila pesada.
blackboard;lousa;Write on the blackboard.;Escreva na lousa.
lesson;lição;An easy lesson.;Uma lição fácil.
exam;prova;A hard exam.;Uma prova difícil.
question;pergunta;A good question.;Uma boa pergunta.
answer;resposta;The right answer.;A resposta certa.
word;palavra;A new word.;Uma palavra nova.
sentence;frase;A short sentence.;Uma frase curta.
page;página;Open page ten.;Abra a página dez.
story;história;A funny story.;Uma história engraçada.
poem;poema;A short poem.;Um poema curto.
newspaper;jornal;Read the newspaper.;Leia o jornal.
magazine;revista;A fashion magazine.;Uma revista de moda.
letter;carta;I write a letter.;Escrevo uma carta.
university;universidade;A big university.;Uma universidade grande.
subject;matéria;My favorite subject.;Minha matéria favorita.
history;história (matéria);History is fun.;História é divertida.
science;ciência;Science class.;Aula de ciências.
math;matemática;Math is hard.;Matemática é difícil.
music;música;Loud music.;Música alta.
art;arte;An art class.;Uma aula de arte.
sport;esporte;My favorite sport.;Meu esporte favorito.
team;equipe;A strong team.;Uma equipe forte.
player;jogador;A good player.;Um bom jogador.
ball;bola;A red ball.;Uma bola vermelha.
goal;gol;A great goal.;Um golaço.
game;jogo;A fun game.;Um jogo divertido.
prize;prêmio;The first prize.;O primeiro prêmio.
swim;nadar;I swim in the sea.;Nado no mar.
jump;pular;Jump high.;Pule alto.
climb;escalar;Climb the tree.;Suba na árvore.
dance;dançar;We dance together.;Dançamos juntos.
sing;cantar;I sing in the shower.;Canto no chuveiro.
draw;desenhar;She draws well.;Ela desenha bem.
paint;pintar;Paint the wall.;Pinte a parede.
cook;cozinhar;I cook dinner.;Cozinho o jantar.
bake;assar;Bake a cake.;Asse um bolo.
clean;limpar;Clean the table.;Limpe a mesa.
wash;lavar;Wash your hands.;Lave as mãos.
sweep;varrer;Sweep the floor.;Varra o chão.
fix;consertar;Fix the door.;Conserte a porta.
open;abrir;Open the window.;Abra a janela.
close;fechar;Close the door.;Feche a porta.
push;empurrar;Push the door.;Empurre a porta.
pull;puxar;Pull the rope.;Puxe a corda.
carry;carregar;Carry this bag.;Carregue esta bolsa.
throw;jogar;Throw the ball.;Jogue a bola.
catch;pegar;Catch the ball.;Pegue a bola.
send;enviar;Send a letter.;Envie uma carta.
receive;receber;Receive a gift.;Receba um presente.
borrow;pegar emprestado;Borrow a pen.;Pegue uma caneta emprestada.
lend;emprestar;Lend me a book.;Empreste-me um livro.
sell;vender;Sell the car.;Venda o carro.
choose;escolher;Choose a color.;Escolha uma cor.
win;ganhar;Win a prize.;Ganhe um prêmio.
lose;perder;Lose a game.;Perca um jogo.
forget;esquecer;Don’t forget your keys.;Não esqueça as chaves.
smell;cheirar;Smell the flower.;Cheire a flor.
taste;provar;Taste the soup.;Prove a sopa.
sound;som;A loud sound.;Um som alto.
laugh;rir;We laugh a lot.;Rimos muito.
cry;chorar;The baby cries.;O bebê chora.
shout;gritar;Don’t shout.;Não grite.
whisper;sussurrar;Whisper, please.;Sussurre, por favor.
sit;sentar;Sit here.;Sente aqui.
stand;ficar de pé;Stand in line.;Fique na fila.
sleep;dormir;I sleep eight hours.;Durmo oito horas.
dream;sonho;A strange dream.;Um sonho estranho.
wake;acordar;I wake at six.;Acordo às seis.
stop;parar;Stop here.;Pare aqui.
start;começar;The class starts.;A aula começa.
finish;terminar;Finish your work.;Termine seu trabalho.
begin;começar;Let’s begin.;Vamos começar.
wait;esperar;Wait a minute.;Espere um minuto.
hurry;apressar-se;Hurry up!;Apresse-se!
visit;visitar;Visit your aunt.;Visite sua tia.
invite;convidar;Invite a friend.;Convide um amigo.
meet;encontrar;Meet me here.;Encontre-me aqui.
help;ajudar;Help me, please.;Ajude-me, por favor.
need;precisar;I need help.;Preciso de ajuda.
want;querer;I want water.;Quero água.
love;amar;I love music.;Amo música.
hate;odiar;I hate noise.;Odeio barulho.
enjoy;curtir;I enjoy swimming.;Curto nadar.
worry;preocupar-se;Don’t worry.;Não se preocupe.
hope;esperar (ter esperança);I hope so.;Espero que sim.
believe;acreditar;I believe you.;Acredito em você.
agree;concordar;I agree with you.;Concordo com você.
guess;adivinhar;Guess my age.;Adivinhe minha idade.
count;contar;Count to ten.;Conte até dez.
spell;soletrar;Spell your name.;Soletre seu nome.
translate;traduzir;Translate this word.;Traduza esta palavra.
today;hoje;Today is Monday.;Hoje é segunda.
tomorrow;amanhã;See you tomorrow.;Até amanhã.
yesterday;ontem;I was home yesterday.;Fiquei em casa ontem.
morning;manhã;Good morning.;Bom dia.
afternoon;tarde;Good afternoon.;Boa tarde.
evening;noite (início);Good evening.;Boa noite.
midnight;meia-noite;It is midnight.;É meia-noite.
noon;meio-dia;Lunch is at noon.;O almoço é ao meio-dia.
early;cedo;I get up early.;Levanto cedo.
late;tarde, atrasado;I am late.;Estou atrasado.
always;sempre;I always smile.;Sempre sorrio.
never;nunca;I never smoke.;Nunca fumo.
sometimes;às vezes;Sometimes I walk.;Às vezes ando.
often;frequentemente;I often read.;Costumo ler.
again;de novo;Say it again.;Diga de novo.
already;já;I already know.;Eu já sei.
still;ainda;I still work.;Ainda trabalho.
soon;em breve;See you soon.;Até breve.
later;mais tarde;See you later.;Até mais tarde.
now;agora;Come now.;Venha agora.
then;então;Then we eat.;Então comemos.
before;antes;Wash before eating.;Lave antes de comer.
after;depois;After lunch.;Depois do almoço.
year;ano;This year.;Este ano.
month;mês;Next month.;Mês que vem.
week;semana;Last week.;Semana passada.
hour;hora;One hour.;Uma hora.
minute;minuto;Wait a minute.;Espere um minuto.
second;segundo;One second.;Um segundo.
birthday;aniversário;Happy birthday!;Feliz aniversário!
holiday;feriado;A long holiday.;Um feriado longo.
party;festa;A big party.;Uma grande festa.
wedding;casamento;A beautiful wedding.;Um lindo casamento.
gift;presente;A nice gift.;Um presente bonito.
card;cartão;A birthday card.;Um cartão de aniversário.
money;dinheiro;I have no money.;Não tenho dinheiro.
coin;moeda;A silver coin.;Uma moeda de prata.
price;preço;A low price.;Um preço baixo.
cash;dinheiro vivo;I pay in cash.;Pago em dinheiro.
bank;banco;The bank is closed.;O banco está fechado.
change;troco;Keep the change.;Fique com o troco.
shop;loja;A small shop.;Uma loja pequena.
sale;liquidação;A big sale.;Uma grande liquidação.
size;tamanho;What size?;Qual tamanho?
color;cor;A bright color.;Uma cor viva.
number;número;A lucky number.;Um número da sorte.
phone;telefone;My phone rings.;Meu telefone toca.
picture;imagem;A pretty picture.;Uma imagem bonita.
paper;papel;A sheet of paper.;Uma folha de papel.
box;caixa;An empty box.;Uma caixa vazia.
rope;corda;A long rope.;Uma corda longa.
hammer;martelo;A heavy hammer.;Um martelo pesado.
key;chave;Lost keys.;Chaves perdidas.
lock;fechadura;The lock is broken.;A fechadura está quebrada.
fire;fogo;A small fire.;Um fogo pequeno.
smoke;fumaça;Black smoke.;Fumaça preta.
water;água;Cold water.;Água fria.
ice;gelo;Ice in my drink.;Gelo na minha bebida.
air;ar;Fresh air.;Ar fresco.
earth;terra;The Earth is round.;A Terra é redonda.
world;mundo;The whole world.;O mundo todo.
country;país;A big country.;Um país grande.
city;cidade;A busy city.;Uma cidade movimentada.
language;idioma;A new language.;Um idioma novo.
culture;cultura;A rich culture.;Uma cultura rica.
flag;bandeira;A red flag.;Uma bandeira vermelha.
doctor;médico;The doctor is kind.;O médico é gentil.
medicine;remédio;Take your medicine.;Tome seu remédio.
fever;febre;I have a fever.;Estou com febre.
cough;tosse;A bad cough.;Uma tosse forte.
headache;dor de cabeça;I have a headache.;Estou com dor de cabeça.
pain;dor;A sharp pain.;Uma dor aguda.
cold (illness);resfriado;I have a cold.;Estou resfriado.
bandage;curativo;A clean bandage.;Um curativo limpo.
exercise;exercício;Daily exercise.;Exercício diário.
health;saúde;Good health.;Boa saúde.
sleep (noun);sono;Eight hours of sleep.;Oito horas de sono.
job;emprego;A good job.;Um bom emprego.
boss;chefe;A kind boss.;Uma chefe gentil.
salary;salário;A good salary.;Um bom salário.
meeting;reunião;A short meeting.;Uma reunião curta.
office;escritório;A big office.;Um escritório grande.
factory;fábrica;A noisy factory.;Uma fábrica barulhenta.
customer;cliente;A happy customer.;Um cliente feliz.
manager;gerente;The manager is busy.;O gerente está ocupado.
holiday (vacation);férias;A long vacation.;Férias longas.
idea;ideia;A great idea.;Uma ótima ideia.
problem;problema;A big problem.;Um grande problema.
reason;razão;A good reason.;Uma boa razão.
secret;segredo;A big secret.;Um grande segredo.
rule;regra;The first rule.;A primeira regra.
plan;plano;A good plan.;Um bom plano.
dream (noun);sonho;A big dream.;Um grande sonho.
luck;sorte;Good luck!;Boa sorte!
trouble;problema;I am in trouble.;Estou em apuros.
danger;perigo;Danger ahead.;Perigo à frente.
noise;barulho;Too much noise.;Barulho demais.
silence;silêncio;Total silence.;Silêncio total.
beauty;beleza;Natural beauty.;Beleza natural.
truth;verdade;Tell the truth.;Diga a verdade.
friend;amigo;A good friend.;Um bom amigo.
enemy;inimigo;A big enemy.;Um grande inimigo.
guest;convidado;A welcome guest.;Um convidado bem-vindo.
stranger;estranho;A kind stranger.;Um estranho gentil.
club;clube;A book club.;Um clube do livro.
group;grupo;A small group.;Um grupo pequeno.
""".strip().splitlines()
POOL=[]
for _l in RAW:
    _p=_l.split(';')
    if len(_p)==4:POOL.append(tuple(_p))

# expressões e colocações novas para as revisões (2 por aula de revisão/avaliação)
EXPRPOOL=[("It’s up to you.","Você decide."),("No problem.","Sem problema."),("Take your time.","Sem pressa."),("Just a moment, please.","Só um momento, por favor."),("I’m not sure.","Não tenho certeza."),("That sounds fun!","Parece divertido!"),("Let me think.","Deixe-me pensar."),("I’ll be right back.","Já volto."),("What’s up?","E aí, tudo bem?"),("Good luck!","Boa sorte!"),("Be careful!","Tenha cuidado!"),("Here you go.","Aqui está."),("Nice to meet you.","Prazer em conhecer."),("How about you?","E você?"),("I don’t mind.","Não me importo."),("Make yourself at home.","Fique à vontade."),("Help yourself.","Sirva-se."),("It’s my treat.","É por minha conta."),("Keep in touch.","Mantenha contato."),("Long time no see!","Quanto tempo!"),("Excuse me, where is…?","Com licença, onde fica…?"),("Could you repeat that?","Pode repetir?"),("I’m looking forward to it.","Estou ansioso por isso."),("What do you recommend?","O que você recomenda?"),("It depends.","Depende."),("Go ahead.","Fique à vontade (pode ir)."),("Never mind.","Deixa pra lá."),("That’s a good idea.","Boa ideia."),("I’m on my way.","Estou a caminho."),("Hang on a second.","Espere um segundo."),("What a surprise!","Que surpresa!"),("I’d love to.","Eu adoraria."),("Sorry I’m late.","Desculpe o atraso."),("It’s a deal.","Combinado."),("Say hello for me.","Dê um oi por mim."),("Have a good trip.","Boa viagem."),("Get well soon.","Melhoras."),("Congratulations!","Parabéns!"),("Thanks for your help.","Obrigado pela ajuda."),("I’m afraid not.","Receio que não."),("Make a wish.","Faça um pedido."),("Cheers!","Saúde!"),("Right on time.","Bem na hora."),("Out of order.","Fora de serviço."),("On sale.","Em promoção."),("Just looking, thanks.","Só olhando, obrigado."),("Keep the change.","Fique com o troco."),("Do me a favor.","Faça-me um favor."),("Not bad.","Nada mal.")]
