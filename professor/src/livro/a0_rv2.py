#!/usr/bin/env python3
"""A0 · Unidade 2: revisão (L026) e avaliação (L027)."""
from review import *
RV('A0-L026','Unit 2 review',
 goal='eu consigo usar a/an/the, plural, possessivos, this/that e adjetivos em frases novas.',
 read=('Reading · My room',text('My Room',['This is my room. It is small, but it is nice. My bed is blue. The desk is brown. That is my chair.','I have a red bag and two books. This book is my English book. These are my pens.','My sister’s room is big. Her door is white. I love my room!'],kicker='DIARY · Unit 2',by='Ana',gloss=[('room','quarto'),('bed','cama'),('desk','mesa de estudo'),('door','porta')])),
 tf=[('Ana’s bed is blue.','T','“My bed is blue.”'),('Ana’s room is big.','F','“It is small.”'),('Ana has a red bag.','T','“I have a red bag.”'),('Ana’s sister has a cat.','NG','O texto não fala de gato.')],
 mc=[('“desk” means…',['mesa de estudo','porta','cama'],0,'desk = mesa de estudo.'),('Which is correct?',['an apple','a apple','an book'],0,'Antes de som de vogal usamos **an**.')],
 recap=[table(['Tema','Lembrete'],[['Artigos','**a** + consoante · **an** + vogal · **the** = específico'],['Plural','book → books · box → boxes · child → children'],['Possessivos','**my, your, his, her**'],['Demonstrativos','**this / that** (singular) · **these / those** (plural)'],['be + adjetivo','**The room is small.** · **They are happy.**']],'Resumo da Unidade 2'),box('warn','Erros que ainda aparecem','**a apple**, **two book**, **she book** (use **her book**).')],
 dlg=('My things',[('Leo','Is this your bag?','Esta é a sua bolsa?'),('Ana','No, it isn’t. That bag is Maya’s.','Não. Aquela bolsa é da Maya.'),('Leo','Are those your books?','Aqueles são os seus livros?'),('Ana','Yes, they are. They are my English books.','Sim. São meus livros de inglês.'),('Leo','Your pens are nice.','Suas canetas são legais.'),('Ana','Thanks! I love them.','Obrigada! Eu adoro elas.')]),
 speak_=[('Point and say: This is my… / That is her…','Aponte e diga.','This is my book. That is her bag.'),('Describe your room with two adjectives.','Descreva seu quarto.','My room is small and nice.'),('Ask: Is this your pen?','Pergunte.','Is this your pen?')],
 wr=('Write 5 sentences about your room.','This is my room. It is small. My bed is blue. I have two books. I love my room!',['Usei **a/an**','Usei **my** ou **her/his**','Usei um **plural**'],'5 frases'),
 teach=['Leve **objetos reais** para a sala e use this/that apontando perto e longe.','Corrija **a/an** pelo som, não pela letra.','Peça que os alunos expliquem a regra uns aos outros.'])
RV('A0-L027','Unit 2 assessment',
 goal='eu consigo mostrar, em leitura, escuta, fala e escrita, que domino a Unidade 2.',
 read=('Reading · A notice',ad('Lost Bag!',['I have a lost bag. It is **black** and **small**.','It has two books and a blue pen.','My name is on the bag: **Leo**.','Is this your bag? Please call me. Thank you!'],gloss=[('lost','perdido'),('call','ligar'),('please','por favor')])),
 tf=[('The bag is big.','F','“It is black and small.”'),('The bag has two books.','T','“It has two books.”'),('The name on the bag is Leo.','T','“Leo.”'),('The pen is red.','F','“a blue pen.”')],
 mc=[('“lost” means…',['perdido','novo','grande'],0,'lost = perdido.'),('The bag is…',['black and small','red and big','white and new'],0,'“black and small.”')],
 recap=[table(['Verifique'],[['Eu uso **a / an / the** corretamente?'],['Eu faço o **plural** de palavras comuns?'],['Eu uso **my, your, his, her**?'],['Eu distingo **this / that**?'],['Eu descrevo coisas com **be + adjetivo**?']],'Lista de verificação da avaliação')],
 dlg=('Lost and found',[('Clerk','Hello. Can I help you?','Olá. Posso ajudar?'),('Leo','Yes. My bag is lost.','Sim. Minha bolsa está perdida.'),('Clerk','What is it like?','Como ela é?'),('Leo','It is black and small.','Ela é preta e pequena.'),('Clerk','Is this your bag?','Esta é a sua bolsa?'),('Leo','Yes, it is! Thank you.','Sim, é! Obrigado.')]),
 speak_=[('Describe a bag or a pen.','Descreva um objeto.','My bag is black and small.'),('Ask: Is that your book?','Pergunte.','Is that your book?'),('Say what you have (two things).','Diga o que você tem.','I have two books and a pen.')],
 wr=('Write a short notice for a lost object (5 sentences).','I have a lost pen. It is blue. It is small. My name is Ana. Please call me!',['Usei **a/an**','Usei **adjetivos**','Usei **my**'],'5 frases'),
 teach=['Aplique **sem consulta** e com tempo.','Grave a parte oral para comparar com a próxima avaliação.','Use a lista para **autoavaliação**.'],
 exam_extra=['Em testes de múltipla escolha, **elimine** primeiro as opções claramente erradas.'])
build_index();print('revisão e avaliação 2 ok')
