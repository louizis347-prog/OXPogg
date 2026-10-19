# -*- coding: utf-8 -*-
# Leitura lúdica (rdgplay): conversa em balões; o aluno completa a lacuna tocando (1ª opção = correta).
M=('Mia','👩🏽','#E0499D');S=('Sam','🧑🏻‍🦱','#0C7A78')
def T(w,txt,pt,opts=None,hint=''):return {'w':w,'t':txt,'pt':pt,'o':opts,'h':hint}
P={
9801:("Missão: apresentar-se",[
 T(0,"Hi! [[I'm]] Mia.","Oi! Eu sou a Mia.",["I'm","Me","Im"],"I'm é a forma curta de I am, com apóstrofo."),
 T(1,"Welcome to New York! [[I'm]] Sam.","Bem-vinda a Nova York! Eu sou o Sam.",["I'm","I be","Am I"],"Para dizer quem você é: I'm + nome."),
 T(1,"Are you from Brazil?","Você é do Brasil?"),
 T(0,"Yes, [[I am]]! And you?","Sim, sou! E você?",["I am","I'm","I be"],"Na resposta curta de sim, volta para I am inteiro."),
 T(1,"No, [[I'm not]]. I'm from New York.","Não. Sou de Nova York.",["I'm not","I not","I don't"],"Para negar com be: I'm not.")],
 "**I'm** = I am. Mas na resposta curta de sim, diga **Yes, I am** (e não “Yes, I'm”)."),
70001:("Missão: no metrô",[
 T(0,"Look! [[I'm]] at the subway station.","Olhe! Estou na estação de metrô.",["I'm","I","Me am"],"Onde você está: I'm at…"),
 T(1,"Great! [[Are you]] with your friend?","Ótimo! Você está com sua amiga?",["Are you","You are","Do you"],"Na pergunta com be, o verbo vem primeiro: Are you…?"),
 T(0,"Yes, [[I am]]. She's buying a ticket.","Sim. Ela está comprando um bilhete.",["I am","I'm","I do"],"Resposta curta de sim: I am."),
 T(0,"[[I'm]] hungry. A bagel, please!","Estou com fome. Um bagel, por favor!",["I'm","I have","I be"],"Sentir fome usa be: I'm hungry.")],
 "**I'm** = I am. Perguntas começam com o verbo: **Are you…?**"),
30001:("Missão: apresentar a família",[
 T(0,"This is my sister. [[She's]] a teacher.","Esta é minha irmã. Ela é professora.",["She's","He's","It's"],"Mulher: she's (she is)."),
 T(0,"And that's my brother. [[He's]] in the garden.","E aquele é meu irmão. Ele está no jardim.",["He's","She's","It's"],"Homem: he's (he is)."),
 T(1,"Is that your dog?","Aquele é seu cachorro?"),
 T(0,"Yes, [[it's]] Max!","Sim, é o Max!",["it's","he's","they're"],"Animal ou coisa: it's (it is)."),
 T(1,"Your family is great! [[They're]] so nice.","Sua família é ótima! Eles são tão simpáticos.",["They're","There","Their"],"Várias pessoas: they're (they are).")],
 "**He's** (ele), **she's** (ela), **it's** (coisa/animal), **they're** (eles)."),
70002:("Missão: dizer oi aos pais",[
 T(0,"This is my mom. [[She's]] a nurse.","Esta é minha mãe. Ela é enfermeira.",["She's","He's","It's"],"Mulher: she's."),
 T(0,"And [[he's]] my dad. He's a driver.","E ele é meu pai. Ele é motorista.",["he's","she's","it's"],"Homem: he's."),
 T(1,"Is the cat yours?","O gato é seu?"),
 T(0,"Yes, [[it's]] Luna.","Sim, é a Luna.",["it's","she's","they're"],"Animal: it's."),
 T(1,"[[They're]] a great family!","Eles são uma ótima família!",["They're","Their","There"],"They're = they are.")],
 "Pessoas: **he's / she's**. Animais e coisas: **it's**. Vários: **they're**."),
9802:("Missão: de onde você é?",[
 T(1,"[[Are you]] from Brazil?","Você é do Brasil?",["Are you","You are","Do you"],"Na pergunta, o verbo vem antes: Are you…?"),
 T(0,"Yes, [[I am]]. And you?","Sim. E você?",["I am","I'm","I do"],"Resposta curta de sim: I am."),
 T(1,"No, [[I'm not]]. I'm from Mexico.","Não. Sou do México.",["I'm not","I not am","I don't"],"Para negar: I'm not."),
 T(0,"Cool! [[Are you]] from the city?","Legal! Você é da cidade?",["Are you","Is you","Do you"],"Are you…? com você.")],
 "Pergunta com be: **Are you…?** Resposta: **Yes, I am. / No, I'm not.**"),
70003:("Missão: no hotel",[
 T(1,"Welcome! [[Are you]] a guest?","Bem-vinda! Você é hóspede?",["Are you","You are","Do you"],"Are you…? é a pergunta com be."),
 T(0,"Yes, [[I am]]. I'm from Japan.","Sim. Sou do Japão.",["I am","I'm","I do"],"Resposta curta de sim: I am."),
 T(1,"Is your luggage in the car?","Sua bagagem está no carro?"),
 T(0,"No, it [[isn't]]. It's at the hotel.","Não, não está. Está no hotel.",["isn't","don't","not"],"Negativa com be: isn't (is not)."),
 T(1,"Great. Enjoy your stay!","Ótimo. Aproveite a estadia!")],
 "**Are you…?** → **Yes, I am.** Negativa: **isn't / aren't / I'm not**."),
30002:("Missão: perguntar sobre alguém",[
 T(1,"[[Is he]] from Japan?","Ele é do Japão?",["Is he","He is","Does he"],"Pergunta com he: Is he…?"),
 T(0,"Yes, [[he is]].","Sim, é.",["he is","he's","he does"],"Resposta curta de sim: he is."),
 T(1,"[[Is she]] from India?","Ela é da Índia?",["Is she","She is","Does she"],"Pergunta com she: Is she…?"),
 T(0,"No, [[she isn't]]. She's from Canada.","Não. Ela é do Canadá.",["she isn't","she not","she don't"],"Negativa: she isn't.")],
 "**Is he…? / Is she…?** — o verbo vem na frente. Resposta: **Yes, he is. / No, she isn't.**"),
70004:("Missão: colegas do mundo",[
 T(0,"[[Is she]] from Spain?","Ela é da Espanha?",["Is she","She is","Does she"],"Is she…?"),
 T(1,"Yes, [[she is]]. She loves soccer.","Sim. Ela adora futebol.",["she is","she's","she does"],"Resposta curta de sim: she is."),
 T(0,"[[Is it]] popular in Argentina too?","É popular na Argentina também?",["Is it","It is","Does it"],"Coisa: Is it…?"),
 T(1,"Yes, [[it is]]!","Sim, é!",["it is","it's","it does"],"Resposta curta de sim: it is.")],
 "Perguntas com be: **Is he / Is she / Is it…?** Respostas curtas: **he is / she is / it is**."),
9803:("Missão: dar seus dados",[
 T(1,"[[What's]] your name?","Qual é o seu nome?",["What's","Whats","What do"],"What's = what is."),
 T(0,"[[It's]] Ana Silva.","É Ana Silva.",["It's","Its","It are"],"It's = it is."),
 T(1,"Spell it, please.","Soletre, por favor."),
 T(0,"S-I-L-V-A. And [[your]] email is ana@mail.com.","S-I-L-V-A. E seu e-mail é ana@mail.com.",["your","you","you're"],"your = seu/sua.")],
 "**What's** = what is. Resposta: **It's…** Posse: **my / your**."),
70005:("Missão: e-mail e telefone",[
 T(1,"[[What's]] your email, please?","Qual é o seu e-mail, por favor?",["What's","What","Who's"],"What's + dado."),
 T(0,"[[It's]] ana at mail dot com.","É ana arroba mail ponto com.",["It's","Its","He's"],"It's = it is."),
 T(1,"Can you spell it?","Pode soletrar?"),
 T(0,"A-N-A. [[My]] phone is five-five-five.","A-N-A. Meu telefone é cinco-cinco-cinco.",["My","Me","I"],"my = meu/minha.")],
 "**What's your…?** → **It's…** E **my / your** antes do nome."),
}
