"""Bloco de verbos e expressões da aula 182: falta de energia."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('light', '🕯️', 'acender', ('light', 'We light a candle.', 'Nós acendemos uma vela.'), ('lights', 'Rosa lights three candles.', 'A Rosa acende três velas.'), ('lit', 'Leo lit a match.', 'O Leo acendeu um fósforo.'), ('lighting', 'I am lighting a candle.', 'Estou acendendo uma vela.'), 'Passado irregular: light vira lit.'),
  vb('check', '🔍', 'conferir, ver', ('check', 'I check the window.', 'Eu confiro a janela.'), ('checks', 'She checks outside.', 'Ela confere lá fora.'), ('checked', 'We checked the street.', 'Conferimos a rua.'), ('checking', 'I am checking the fridge.', 'Estou conferindo a geladeira.'), 'Check = ver se está tudo certo.'),
  vb('hold', '🤲', 'segurar', ('hold', 'I hold the flashlight.', 'Eu seguro a lanterna.'), ('holds', 'Leo holds the light.', 'O Leo segura a luz.'), ('held', 'She held my hand.', 'Ela segurou minha mão.'), ('holding', 'He is holding a candle.', 'Ele está segurando uma vela.'), 'Passado irregular: hold vira held.'),
  vb('stay', '🏠', 'ficar', ('stay', 'We stay at home.', 'Nós ficamos em casa.'), ('stays', 'The food stays cold.', 'A comida continua fria.'), ('stayed', 'They stayed calm.', 'Eles ficaram calmos.'), ('staying', 'I am staying inside.', 'Estou ficando dentro de casa.'), 'Stay = ficar em um lugar ou estado: stay calm.'),
  vb('feel', '💭', 'sentir', ('feel', 'I feel safe.', 'Eu me sinto seguro.'), ('feels', 'It feels cold.', 'Parece frio.'), ('felt', 'We felt the wind.', 'Sentimos o vento.'), ('feeling', 'I am feeling nervous.', 'Estou me sentindo nervoso.'), 'Passado irregular: feel vira felt.')],
 verb_game=[
  dict(scene='A Rosa acende uma vela agora.', en='Rosa ___ a candle.', opts=['light', 'lights', 'lit'], ans=1, pt='A Rosa acende uma vela.', why='Com Rosa (ela), o presente leva -s: lights.'),
  dict(scene='Ontem o Leo acendeu um fósforo.', en='Yesterday Leo ___ a match.', opts=['light', 'lit', 'lighting'], ans=1, pt='Ontem o Leo acendeu um fósforo.', why='Yesterday pede passado: lit.'),
  dict(scene='Agora você segura a lanterna.', en='I am ___ the flashlight.', opts=['hold', 'held', 'holding'], ans=2, pt='Estou segurando a lanterna.', why='Am + verbo termina em -ing: holding.'),
  dict(scene='Vocês ficam calmos na tempestade.', en='We ___ calm.', opts=['stay', 'stays', 'staying'], ans=0, pt='Nós ficamos calmos.', why='Com we, use a forma base: stay.')],
 expressions=[
  dict(en='The power is out.', pt='Acabou a luz.', ex='Oh no! The power is out.', exp='Para dizer que não há eletricidade.', c='a'),
  dict(en='the whole street', pt='a rua toda', ex='No, the whole street.', exp='Quando o problema afeta todo o lugar.', c='b'),
  dict(en='in the drawer', pt='na gaveta', ex='It is in the kitchen drawer.', exp='Para dizer onde está um objeto.', c='c'),
  dict(en='It works!', pt='Funciona!', ex='I found it. It works!', exp='Quando algo funciona bem.', c='d'),
  dict(en='Back to normal', pt='De volta ao normal', ex='Now everything is back to normal.', exp='Quando o problema acaba.', c='a'),
  dict(en='Make do', pt='Se virar com o que tem', ex='We make do with a candle.', exp='Resolver com poucos recursos.', c='b')],
 expr_game=[
  dict(cue='Você quer dizer que a energia acabou.', opts=['The power is out.', 'It works!', 'Back to normal.'], ans=0, why='The power is out = sem eletricidade.'),
  dict(cue='A lanterna acende e você comemora.', opts=['In the drawer.', 'It works!', 'The whole street.'], ans=1, why='It works! = funciona.'),
  dict(cue='A luz voltou e tudo está bem de novo.', opts=['Back to normal.', 'The power is out.', 'Make do.'], ans=0, why='Back to normal = de volta ao normal.')])
