"""Bloco de verbos e expressões da aula 039: gorjeta e agradecimento."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('tip', '💵', 'dar gorjeta', ('tip', 'I tip twenty percent.', 'Eu dou vinte por cento de gorjeta.'), ('tips', 'She tips the waiter.', 'Ela dá gorjeta ao garçom.'), ('tipped', 'We tipped eighteen percent.', 'Nós demos dezoito por cento de gorjeta.'), ('tipping', 'I am tipping fifteen percent.', 'Estou dando quinze por cento de gorjeta.'), 'Tip é verbo e substantivo. Passado: tipped (p dobra).'),
  vb('leave', '👋', 'deixar', ('leave', 'I leave a tip.', 'Eu deixo uma gorjeta.'), ('leaves', 'He leaves ten dollars.', 'Ele deixa dez dólares.'), ('left', 'She left a big tip.', 'Ela deixou uma gorjeta grande.'), ('leaving', 'We are leaving now.', 'Estamos saindo agora.'), 'Irregular: leave vira left. Também significa “sair”.'),
  vb('thank', '🙏', 'agradecer', ('thank', 'I thank the waiter.', 'Eu agradeço ao garçom.'), ('thanks', 'She thanks the cook.', 'Ela agradece ao cozinheiro.'), ('thanked', 'He thanked Maya.', 'Ele agradeceu à Maya.'), ('thanking', 'I am thanking the waiter.', 'Estou agradecendo ao garçom.'), 'Thank you é o mais comum; thank + pessoa é o verbo.'),
  vb('enjoy', '😊', 'curtir / gostar', ('enjoy', 'We enjoy the food.', 'Nós gostamos da comida.'), ('enjoys', 'He enjoys the dinner.', 'Ele curte o jantar.'), ('enjoyed', 'I enjoyed the meal.', 'Eu gostei da refeição.'), ('enjoying', 'We are enjoying dinner.', 'Estamos curtindo o jantar.'), 'Enjoy your meal! = bom apetite.'),
  vb('give', '🤲', 'dar', ('give', 'I give a tip.', 'Eu dou uma gorjeta.'), ('gives', 'She gives change.', 'Ela dá o troco.'), ('gave', 'He gave ten dollars.', 'Ele deu dez dólares.'), ('giving', 'I am giving twenty dollars.', 'Estou dando vinte dólares.'), 'Irregular: give vira gave.')],
 verb_game=[
  dict(scene='Ontem ela deixou uma gorjeta grande.', en='Yesterday she ___ a big tip.', opts=['leave', 'left', 'leaves'], ans=1, pt='Ontem ela deixou uma gorjeta grande.', why='Passado irregular de leave: left.'),
  dict(scene='Ele sempre agradece ao garçom.', en='He always ___ the waiter.', opts=['thank', 'thanks', 'thanked'], ans=1, pt='Ele sempre agradece ao garçom.', why='Com “he” o presente leva -s: thanks.'),
  dict(scene='Vocês estão curtindo o jantar.', en='We are ___ dinner.', opts=['enjoy', 'enjoys', 'enjoying'], ans=2, pt='Estamos curtindo o jantar.', why='“are” + -ing: enjoying.'),
  dict(scene='Eu normalmente dou vinte por cento de gorjeta.', en='I usually ___ twenty percent.', opts=['tip', 'tips', 'tipped'], ans=0, pt='Eu normalmente dou vinte por cento de gorjeta.', why='Com “I” o presente fica na forma base: tip.')],
 expressions=[
  dict(en='How much is the tip?', pt='Quanto é a gorjeta?', ex='How much is the tip here?', exp='Para perguntar o valor usual da gorjeta.', c='a'),
  dict(en='twenty percent', pt='vinte por cento', ex='Twenty percent is common.', exp='A gorjeta nos EUA costuma ser 15 a 20 por cento.', c='b'),
  dict(en='Keep the change.', pt='Pode ficar com o troco.', ex='Here’s twenty. Keep the change.', exp='Para dar o troco como gorjeta.', c='c'),
  dict(en='Everything was great.', pt='Estava tudo ótimo.', ex='Everything was great, thank you!', exp='Resposta quando perguntam como foi.', c='d'),
  dict(en='You’re so kind.', pt='Você é muito gentil.', ex='Thank you! You’re so kind.', exp='Para agradecer uma gentileza.', c='a'),
  dict(en='Have a great night!', pt='Tenha uma ótima noite!', ex='Thanks! Have a great night!', exp='Despedida à noite.', c='b')],
 expr_game=[
  dict(cue='Você quer saber quanto deixar de gorjeta.', opts=['How much is the tip?', 'Keep the change.', 'Have a great night!'], ans=0, why='How much is…? pergunta o valor.'),
  dict(cue='O garçom pergunta como estava a comida.', opts=['Everything was great.', 'Twenty percent.', 'Keep the change.'], ans=0, why='Responda sobre a comida: Everything was great.'),
  dict(cue='Você quer deixar o troco para o garçom.', opts=['Keep the change.', 'How was everything?', 'You’re so kind.'], ans=0, why='Keep the change = fique com o troco.')])
