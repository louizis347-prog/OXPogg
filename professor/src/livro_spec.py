#!/usr/bin/env python3
"""Inventário do currículo (A0 → C2), transcrito da especificação do curso. Cada lista é uma string separada por ';'.
Nada aqui é inventado: são os itens da matriz curricular fornecida. Usado por livro_map.py para calcular as aulas e a rastreabilidade."""
S=lambda s:[x.strip() for x in s.split(';') if x.strip()]

# metas cumulativas: (mínimo, máximo) e meta de planejamento (ponto médio)
TARGETS={ # nível: (léxico, verbos-base, phrasal verbs, expressões+collocations, horas guiadas acumuladas)
 'A0':dict(lex=(150,250),verbs=(20,20),pv=(0,5),expr=(15,25),glh=(30,30)),
 'A1':dict(lex=(600,900),verbs=(60,60),pv=(10,15),expr=(50,80),glh=(90,100)),
 'A2':dict(lex=(1200,1800),verbs=(120,120),pv=(30,40),expr=(120,180),glh=(180,200)),
 'B1':dict(lex=(2500,3500),verbs=(200,200),pv=(70,90),expr=(250,350),glh=(350,400)),
 'B2':dict(lex=(4000,6000),verbs=(300,300),pv=(120,160),expr=(450,650),glh=(500,600)),
 'C1':dict(lex=(6500,9000),verbs=(400,400),pv=(200,250),expr=(700,1000),glh=(700,800)),
 'C2':dict(lex=(9000,12000),verbs=(500,500),pv=(280,350),expr=(1000,1400),glh=(1000,1200)),
}
NAMES={'A0':('Pré-A1','Zero absoluto'),'A1':('A1','Beginner'),'A2':('A2','Elementary / Pre-Intermediate'),'B1':('B1','Intermediate'),'B2':('B2','Upper-Intermediate'),'C1':('C1','Advanced'),'C2':('C2','Proficiency')}
GOAL={'A0':'Reconhecer e formar frases muito simples, com auxílio.','A1':'Apresentar-se, perguntar, responder e falar de necessidades básicas.','A2':'Descrever rotinas, experiências, planos e situações previsíveis.','B1':'Narrar acontecimentos, explicar opiniões e participar de conversas cotidianas.','B2':'Argumentar, debater, compreender conteúdos complexos e conversar com fluência razoável.','C1':'Comunicar-se com precisão, flexibilidade e naturalidade em ambientes sociais, profissionais e acadêmicos.','C2':'Compreender linguagem altamente complexa e expressar nuances com precisão, adequação e espontaneidade.'}
CRITERIA={'A0':'Compreender e produzir uma apresentação básica em interações guiadas, sem depender só da leitura de um roteiro.',
 'A1':'Conversa guiada sobre vida pessoal e rotina, situação simulada de compra e descrição escrita simples.',
 'A2':'Simular uma viagem (reserva, check-in, informações, problema) e produzir um relato escrito da experiência.',
 'B1':'Manter conversas sobre temas familiares sem roteiro, explicar experiências em sequência lógica e compreender os pontos principais de materiais claros.',
 'B2':'Apresentar uma proposta, responder a objeções e escrever um texto argumentativo estruturado com dados e exemplos.',
 'C1':'Participar de discussões exigentes com espontaneidade, compreender textos extensos e argumentos complexos, escrever de forma estruturada e adequar a linguagem ao público.',
 'C2':'Compreender grande diversidade de discursos complexos, integrar fontes, perceber ironia e nuances, adaptar o registro e produzir textos sofisticados e coesos.'}

# ---------------- vocabulário por campos (prioridade de cada nível) ----------------
VOCAB_FIELDS={
 'A0':S('Identidade (name, first name, last name, age, country, city, nationality);Pessoas (man, woman, boy, girl, friend, teacher, student);Cumprimentos (hello, hi, goodbye, good morning, good night);Família (mother, father, brother, sister, son, daughter);Objetos (book, pen, pencil, phone, computer, table, chair);Números 0–100 (idade, telefone, preços simples);Tempo (today, tomorrow, yesterday, morning, afternoon, evening, night);Cores (red, blue, green, black, white, yellow, brown);Lugares (home, school, work, store, restaurant, bathroom);Necessidades (water, food, help, money, time);Dias da semana e meses;Palavras interrogativas'),
 'A1':S('Vida pessoal;Rotina;Alimentação;Moradia;Trabalho;Lazer;Lugares'),
 'A2':S('Viagens;Compras;Saúde cotidiana;Experiências;Serviços;Planos;Problemas simples'),
 'B1':S('Educação;Relacionamentos;Carreira;Tecnologia;Cultura;Notícias;Sentimentos e decisões'),
 'B2':S('Sociedade;Economia básica;Meio ambiente;Política como tema de discussão;Ciência;Desenvolvimento profissional'),
 'C1':S('Negócios;Pesquisa;Comunicação intercultural;Problemas sociais;Análises;Negociações;Pensamento crítico'),
 'C2':S('Linguagem especializada;Discurso público;Filosofia;Literatura;Argumentação complexa;Retórica;Nuances culturais')}

# ---------------- verbos-base ----------------
VERBS={
 'A0':S('be;have;do;go;come;want;need;like;love;know;eat;drink;live;work;study;speak;read;write;see;help'),
 'A1':S('say;tell;ask;answer;talk;call;listen;walk;run;drive;ride;travel;arrive;leave;wake;sleep;wash;clean;cook;buy;pay;meet;visit;wait;give;show;thank;learn;teach;understand;practice;remember;make;take;get;put;use;find;look;watch;feel;think;prefer;hate;enjoy'),
 'A2':S('choose;decide;plan;hope;expect;enjoy;prefer;dislike;miss;forget;remember;try;stop;continue;spend;save;borrow;lend;cost;explain;describe;invite;suggest;offer;bring;send;receive;change;return;book;cancel;stay;arrive;depart;lose;break;fix;hurt;worry;agree;disagree;trust;support;improve;grow;become;keep;achieve'),
 'B1':S('believe;suppose;doubt;consider;realize;mention;discuss;argue;complain;apologize;avoid;refuse;accept;promise;intend;solve;repair;prevent;protect;handle;manage;organize;develop;provide;require;experience;discover;explore;notice;recognize;encourage;forgive;blame;disappoint;respect;increase;decrease;reduce;replace;improve;succeed;fail;achieve;depend;affect'),
 'B2':S('assess;evaluate;examine;compare;interpret;claim;deny;imply;emphasize;justify;investigate;identify;determine;detect;implement;establish;maintain;expand;influence;contribute;result;lead;trigger;negotiate;persuade;convince;compromise;enhance;strengthen;adapt;overcome;reveal;indicate;suggest;demonstrate;prioritize;allocate;invest;reconsider'),
 'C1':S('assert;maintain;contend;advocate;challenge;infer;deduce;perceive;distinguish;scrutinize;examine;assess;verify;clarify;elaborate;illustrate;specify;associate;correlate;attribute;link;evaluate;interpret;synthesize;transform;reshape;restructure;facilitate;undermine;reinforce;influence;constrain;prioritize;determine;acknowledge;endorse;convey;articulate;disclose;address'),
 'C2':S('substantiate;corroborate;refute;undermine;mitigate;exacerbate;reconcile;preclude;elucidate;discern;delineate;contextualize;scrutinize;pinpoint;underpin;entail;concede;challenge;synthesize')}
IRREGULAR=S('be/was-were/been;become/became/become;begin/began/begun;break/broke/broken;bring/brought/brought;buy/bought/bought;choose/chose/chosen;come/came/come;do/did/done;drink/drank/drunk;drive/drove/driven;eat/ate/eaten;fall/fell/fallen;feel/felt/felt;find/found/found;forget/forgot/forgotten;get/got/gotten;give/gave/given;go/went/gone;have/had/had;hear/heard/heard;know/knew/known;leave/left/left;lose/lost/lost;make/made/made;meet/met/met;pay/paid/paid;read/read/read;run/ran/run;say/said/said;see/saw/seen;send/sent/sent;sit/sat/sat;sleep/slept/slept;speak/spoke/spoken;spend/spent/spent;take/took/taken;teach/taught/taught;tell/told/told;think/thought/thought;understand/understood/understood;wear/wore/worn;write/wrote/written')
THIRD_PERSON=S('work→works;watch→watches;study→studies;have→has;do→does;go→goes')
KEY_VERBS={ # os 15 verbos mais produtivos: revisados em todos os níveis
 'get':'get home, get better, get ready, get a job, get someone to do something','take':'take a break, take time, take responsibility, take over','make':'make money, make progress, make sense, make someone laugh',
 'do':'do homework, do business, do well, do someone a favor','have':'have lunch, have to, have something done, have trouble doing','go':'go home, go out, go through, go wrong, go on',
 'come':'come back, come across, come up with, come to a conclusion','give':'give advice, give up, give in, give someone a hand','keep':'keep going, keep in touch, keep someone waiting',
 'put':'put on, put off, put up with, put something into practice','set':'set a goal, set up, set aside, set out','run':'run a business, run out of, run into, run smoothly',
 'hold':'hold a meeting, hold on, hold back, hold a position','turn':'turn on, turn down, turn into, turn out','bring':'bring something, bring up, bring about, bring someone along'}

# ---------------- phrasal verbs ----------------
PV={
 'A1':S('wake up;get up;sit down;stand up;turn on;turn off;put on;take off;come in;go out;look for;pick up'),
 'A2':S('check in;check out;fill out;drop off;find out;try on;put away;look after;run out of;hang out;come back;go back;look up;give back;call back;turn down;get along with;get on;get off;set up'),
 'B1':S('give up;put off;look forward to;deal with;get over;turn out;work out;bring up;carry on;come across;get rid of;keep up with;look into;point out;put up with;run into;take care of;take over;figure out;break down;show up;turn down'),
 'B2':S('bring about;come up with;cut back on;get away with;get by;get around to;go through;hold back;keep on;live up to;make up for;miss out on;put forward;rule out;set out;sort out;stand for;take into account;turn into;weigh up'),
 'C1':S('bring up to speed;brush up on;come down to;do away with;fall through;follow through on;get across;iron out;narrow down;phase out;rule something out;scale back;single out;step down;step up;take on;weigh in on;zero in on'),
 'C2':S('boil down to;crack down on;weed out;play down;walk back;put down to;set aside;spell out;back down;pull off;fall short of;brush aside;root out;bear out;hinge on;hold up;map out;iron out')}

# ---------------- expressões, idioms e collocations ----------------
EXPR={
 'A0':S('Nice to meet you;How are you?;I’m fine;Thank you;You’re welcome;Excuse me;I’m sorry;I don’t understand;Please repeat;What does it mean?;How do you say…?;See you later'),
 'A1':S('How’s it going?;Good to see you!;Where are you from?;What do you do?;Where is the restroom?;How much is it?;Can I have…?;I’d like…;I really like…;I’m not a fan of…;Sure!;Sounds good!;Not right now.;Really?;That’s nice!;That’s great!;Have a nice day!;See you around!'),
 'A2':S('Could you help me?;I’d like to book a room;Can I try this on?;Is there anything cheaper?;What happened?;That’s too bad;No worries;I can’t make it;Let me check;I’m not sure;I think…;I believe…;In my opinion…;I prefer… because…;I’m planning to…;I’m thinking about…;Maybe next time;I’m looking forward to…;What’s wrong?;It doesn’t work;I lost my…;Let me help you.'),
 'B1':S('It depends.;As far as I know…;To be honest…;The thing is…;As a matter of fact…;That makes sense.;I see your point.;It’s not a big deal.;It’s up to you.;I have no idea.;I couldn’t agree more.;I’m not used to it.;I changed my mind.;That reminds me…;Long story short…'),
 'B2':S('Get the hang of it;On the same page;A blessing in disguise;The bottom line is…;Easier said than done;Go the extra mile;At the end of the day…;It’s a matter of time.;Take something for granted;Out of the blue;Make ends meet;Be worth a shot;For the time being;That being said…'),
 'C1':S('To a certain extent…;Broadly speaking…;For the most part…;On the grounds that…;By and large…;In light of…;That is not to say that…;It is worth noting that…;There is little doubt that…;Be that as it may…;To put it into perspective…;The extent to which…'),
 'C2':S('Move the goalposts;Read between the lines;A double-edged sword;The tip of the iceberg;Draw the line;Split hairs;Go without saying;A slippery slope;A gray area;A point of contention;For all intents and purposes;Beside the point;In no uncertain terms')}
COLLOC={
 'A1':S('have breakfast/lunch/dinner;take a shower;take a break;go to work;go home;make breakfast;make coffee;do homework;do the dishes;listen to music;watch TV;spend time;spend money'),
 'B1':S('make progress;make an effort;make a mistake;take responsibility;take advantage of;take a risk;pay attention;pay a fine;pay the bills;keep a promise;keep in touch;keep a secret;reach an agreement;reach a conclusion;have an impact on;have access to;strong argument;serious problem;major difference'),
 'B2':S('pose a threat;pose a challenge;raise awareness;raise concerns;draw a conclusion;draw attention to;meet a deadline;meet expectations;address an issue;address a concern;play a crucial role;play a significant part;provide evidence;provide insight;make an informed decision;take appropriate measures'),
 'C1':S('compelling evidence;underlying assumptions;far-reaching consequences;widespread concern;a substantial increase;a fundamental shift;a plausible explanation;to reach a consensus;to challenge an assumption;to draw a distinction;to exercise discretion;to address shortcomings')}

# ---------------- gramática (itens obrigatórios de cada nível) ----------------
GRAM={
 'A0':S('Pronomes pessoais;am/is/are afirmativa;am/is/are negativa;am/is/are interrogativa e respostas curtas;Contrações (I’m, you’re, isn’t);Artigos básicos a/an/the;Singular e plural;Possessivos my/your/his/her;Demonstrativos this/that;Subject + be + adjective;Subject + be + noun;Subject + be + place;Subject + have + noun;Subject + like/need + noun;Wh-word + be (Where are you from?)'),
 'A1':S('Verb to be — revisão e ampliação;Present Simple;Present Simple — perguntas;Terceira pessoa -s/-es;Present Continuous;Present Simple × Continuous;Have / have got;There is / There are;Can / can’t;Imperatives;Wh- questions;Articles (a, an, the e ausência);Countable / uncountable;Some / any;Adverbs of frequency;Prepositions of place;Prepositions of time;Possessive adjectives/pronouns;Object pronouns;Adjective position;Like + -ing;Want / need + to;Basic conjunctions (and, but, because, or, so)'),
 'A2':S('Past Simple — regular;Past Simple — irregular;Past Simple — negative;Past Simple — questions;Past Continuous;Contraste Past Continuous + Past Simple;Future — going to;Future — will;Present Continuous para futuro;Comparatives;Superlatives;Modals (should, must, have to, could);don’t have to / mustn’t;Quantifiers (much, many, a lot of, a few, a little);Too / enough;Infinitive of purpose;Zero Conditional;First Conditional;Basic relative clauses (who, that, which);Present Perfect — introdução'),
 'B1':S('Present Perfect — experiências;Present Perfect — duração;Present Perfect × Past Simple;Present Perfect Continuous;Past Perfect;Used to;Would — hábitos passados;Second Conditional;Modal deduction (must, might);Modal impossibility (can’t);Basic Passive Voice;Present Passive;Reported Speech;Indirect questions;Defining relative clauses;Question tags;Verb + infinitive;Verb + gerund;Despite / although;So / such'),
 'B2':S('Present Perfect Continuous — consolidação;Past Perfect Continuous;Future Continuous;Future Perfect;Third Conditional;Mixed Conditionals — introdução;Wish — situações presentes;Wish — arrependimento;If only;Modal Perfect — crítica;Modal Perfect — dedução;Modal Perfect — possibilidade;Advanced Passive Voice;Have/get something done;Reported questions and commands;Reporting verbs;Non-defining relative clauses;Participle clauses — introdução;Contrast and concession (even though, despite, whereas);Discourse connectors (nevertheless, furthermore, consequently)'),
 'C1':S('Inversion after negative adverbials;Not only… but also — inversion;Hardly / scarcely;Conditional inversion (Had I known…);Inverted hypothetical (Were I…);Cleft sentences;Pseudo-cleft sentences;Emphatic structures;Advanced participle clauses;Perfect participle passive;Nominalization;Reporting passive;Subjunctive constructions;Mixed Conditionals;Advanced relative clauses;Concessive structures (Much as I admire…);Future Perfect Continuous;Ellipsis;Hedging;Advanced passive modality'),
 'C2':S('Controle de estruturas hipotéticas;Contrastes sutis (not so much… as…);Concessões sofisticadas;Inversão estilística;Reformulação de ênfase;Qualificação de afirmações;Argumentação contrafactual;Expressões de avaliação;Redução e condensação;Ambiguidade intencional')}
MODALS_B2=S('Possibilidade (may, might, could);Dedução forte (must, can’t);Conselho (should, ought to, had better);Obrigação (must, have to, be required to);Ausência de obrigação (don’t have to, needn’t);Possibilidade no passado (might have, could have);Dedução sobre o passado (must have, can’t have);Crítica ou arrependimento (should have, shouldn’t have);Expectativa (be supposed to);Probabilidade (be likely to, be unlikely to)')
PATTERNS_VERB={ # padrões verbais por nível
 'B1':S('want someone to do;ask someone to do;tell someone to do;let someone do;make someone do;enjoy doing;decide to do;be interested in doing;be good at doing;have trouble doing;spend time doing;It’s worth doing'),
 'B2':S('prevent someone from doing;accuse someone of doing;insist on doing;object to doing;suggest doing;recommend that + clause;be likely to do;be expected to do;would rather do;prefer doing A to doing B;stop doing / stop to do;remember doing / remember to do'),
 'C1':S('attribute something to something;distinguish something from something;refrain from doing;be inclined to do;take something into consideration;account for something;give rise to something;be subject to something')}
CONTRASTS_C2=S('claim × assert × allege × contend;suggest × imply × infer;convince × persuade;presume × assume;mitigate × alleviate;accurate × precise;plausible × possible × probable')
REGISTER_C2=S('Informal;Profissional;Diplomático;Analítico/acadêmico')
GENRES_C1=S('Academic essay;Report;Proposal;Formal email;Critical review;Presentation;Debate')

# ---------------- transversais ----------------
SENTENCE_PATTERNS=S('Subject + verb;Subject + verb + object;Subject + verb + complement;Subject + verb + indirect/direct object;Subject + verb + object + complement;Verb + to-infinitive;Verb + -ing;Verb + object + to-infinitive;Verb + object + bare infinitive;Preposition + -ing;Modal + base verb;Modal + have + participle;Have + past participle;Be + past participle;Have/get + object + participle;Adjective + to-infinitive;It + be + adjective + that-clause;Noun + that-clause;Reporting verb + clause;Relative clause;Conditional clause;Comparative clause;Participle clause;Cleft sentence;Inversion')
WORD_FAMILIES=S('act (action, active, actively, activity);decide (decision, decisive, decisively);create (creation, creative, creativity);succeed (success, successful, successfully);analyze (analysis, analytical, analytically);rely (reliable, reliability, unreliable);signify (significant, significance, significantly);conclude (conclusion, conclusive, conclusively)')
PREFIXES=S('un-;in-;im-;ir-;re-;mis-;dis-;over-;under-;pre-;post-;anti-')
SUFFIXES=S('-tion;-ment;-ness;-ity;-able;-ible;-ful;-less;-ly;-ize;-en')
PRON={
 'A0':S('Alfabeto e nomes das letras;Nome das letras × sons;Pronúncia de palavras de alta frequência;Entonação de perguntas;Contrações I’m, you’re, he’s, she’s, we’re, they’re'),
 'A1':S('ship/sheep;bed/bad;think/this;/h/ de house;r americano;I am × I’m;do you (fala rápida);sílaba tônica em palavras comuns'),
 'A2':S('Terminações do passado /t/ /d/ /ɪd/;Plural e 3ª pessoa /s/ /z/ /ɪz/;Schwa /ə/;Entonação de perguntas e pedidos educados;gonna e wanna (reconhecimento);Ligação entre palavras'),
 'B1':S('Word stress;Sentence stress;Entonação;Contrações e fala conectada (compreensão)'),
 'B2':S('Redução de palavras funcionais (to, of, for, and, can);Flap T americano;Ligações e assimilação;Entonação de contraste, surpresa, dúvida;Acento para enfatizar informação;Fala monitorada × informal'),
 'C1':S('Ênfase intencional;Pausas e ritmo;Expressividade;Organização da informação pela entonação'),
 'C2':S('Ajuste refinado de entonação;Ritmo e ênfase para nuances')}
COMPET={ # competências de conclusão (critérios práticos)
 'A1':S('Apresentar-se e conhecer outra pessoa;Falar de rotina, trabalho, escola e família;Perguntar preços, horários e direções;Descrever casa, pessoas e objetos;Fazer pedidos em lojas e restaurantes;Compreender mensagens lentas e claras;Escrever apresentação, mensagem ou descrição'),
 'A2':S('Contar o fim de semana;Explicar planos futuros;Relatar uma experiência simples;Resolver problemas previsíveis em viagem;Comparar alternativas;Sustentar conversa cotidiana'),
 'B1':S('Narrativa conectada;Explicar problemas;Dar motivos para opiniões;Falar de objetivos pessoais;Conversar sem roteiro;Compreender pontos principais de materiais claros'),
 'B2':S('Defender posições com argumentos;Discutir trabalho, educação, sociedade e cultura;Comparar vantagens e desvantagens;Explicar problemas abstratos;Compreender aulas, entrevistas, reportagens e debates;Produzir apresentações e textos argumentativos;Reformular quando falta uma palavra'),
 'C1':S('Discussões exigentes com espontaneidade;Compreender textos extensos e argumentos complexos;Escrever de forma estruturada;Adequar linguagem a diferentes públicos;Argumentar com precisão e flexibilidade'),
 'C2':S('Compreender grande diversidade de textos e discursos;Integrar fontes e sintetizar argumentos;Perceber ironia e sutilezas;Comunicar ideias complexas com precisão e espontaneidade;Adaptar o registro ao interlocutor;Argumentar, negociar e mediar;Usar vocabulário idiomático e figurado;Produzir textos sofisticados e coesos;Corrigir e reformular a própria produção')}
CICLO=S('Contextualização;Compreensão;Reconhecimento oral;Produção controlada;Produção espontânea;Revisão espaçada;Transferência')
BLOCOS_60MIN=[('Revisão ativa',5),('Contexto comunicativo',10),('Descoberta linguística',10),('Prática guiada',10),('Produção comunicativa',20),('Feedback e revisão',5)]
WORK_PROGRESSION={'A1':'I work at a hotel.','A2':'I worked at a hotel last year.','B1':'I’ve been working in customer service for three years.','B2':'I’m responsible for managing customer complaints and resolving unexpected issues.','C1':'My role involves overseeing operational procedures and implementing strategies to improve customer satisfaction.','C2':'My responsibilities encompass the strategic coordination of operational processes, with particular emphasis on service optimization and long-term organizational effectiveness.'}
