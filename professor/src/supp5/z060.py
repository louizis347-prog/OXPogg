"""Bloco de verbos e expressões da aula 060: atravessar a rua."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('cross', '🚸', 'atravessar', ('cross', 'We cross the street.', 'Nós atravessamos a rua.'), ('crosses', 'Uma crosses at the corner.', 'A Uma atravessa na esquina.'), ('crossed', 'They crossed on green.', 'Eles atravessaram no verde.'), ('crossing', 'I am crossing the street.', 'Estou atravessando a rua.'), 'Cross termina em ss: crosses (ele/ela), crossed.'),
  vb('look', '👀', 'olhar', ('look', 'I look both ways.', 'Eu olho para os dois lados.'), ('looks', 'Carlos looks left.', 'O Carlos olha para a esquerda.'), ('looked', 'She looked at the light.', 'Ela olhou para o sinal.'), ('looking', 'I am looking at the bike.', 'Estou olhando para a bicicleta.'), 'Look at = olhar para. Look both ways = olhar para os dois lados.'),
  vb('watch', '⚠️', 'prestar atenção / vigiar', ('watch', 'We watch the cars.', 'Nós ficamos de olho nos carros.'), ('watches', 'He watches the bikes.', 'Ele fica de olho nas bicicletas.'), ('watched', 'I watched the traffic.', 'Eu observei o trânsito.'), ('watching', 'I am watching for cars.', 'Estou atenta aos carros.'), 'Watch out! = Cuidado! Watch termina em ch: watches.'),
  vb('stop', '🛑', 'parar', ('stop', 'Cars stop at red.', 'Os carros param no vermelho.'), ('stops', 'The bus stops here.', 'O ônibus para aqui.'), ('stopped', 'The car stopped.', 'O carro parou.'), ('stopping', 'The car is stopping.', 'O carro está parando.'), 'No -ing e no passado dobra o p: stopping, stopped.'),
  vb('listen', '👂', 'escutar', ('listen', 'I listen for cars.', 'Eu escuto se vêm carros.'), ('listens', 'Uma listens to the signal.', 'A Uma escuta o sinal.'), ('listened', 'We listened carefully.', 'Nós escutamos com atenção.'), ('listening', 'I am listening for bikes.', 'Estou escutando se vêm bicicletas.'), 'Listen to = escutar. Regular: listened.')],
 verb_game=[
  dict(scene='O ônibus para aqui todo dia.', en='The bus ___ here.', opts=['stop', 'stops', 'stopping'], ans=1, pt='O ônibus para aqui.', why='Com “the bus” (ele) o presente leva -s: stops.'),
  dict(scene='Agora você atravessa a rua.', en='I am ___ the street.', opts=['cross', 'crossed', 'crossing'], ans=2, pt='Estou atravessando a rua.', why='“am” + -ing: crossing.'),
  dict(scene='Ontem o carro parou.', en='The car ___ at the red light.', opts=['stopped', 'stop', 'stops'], ans=0, pt='O carro parou no sinal vermelho.', why='Passado: dobra o p e põe -ed: stopped.'),
  dict(scene='O Carlos olha para a esquerda.', en='Carlos ___ left.', opts=['look', 'looks', 'looked'], ans=1, pt='O Carlos olha para a esquerda.', why='Com “Carlos” (ele) o presente leva -s: looks.')],
 expressions=[
  dict(en='Wait!', pt='Espere!', ex='Wait! The light is red.', exp='Para avisar alguém para parar.', c='a'),
  dict(en='When the light is green.', pt='Quando o sinal estiver verde.', ex='You can cross when the light is green.', exp='Para dizer a hora certa de atravessar.', c='b'),
  dict(en='Look both ways!', pt='Olhe para os dois lados!', ex='Look both ways before you cross.', exp='Aviso antes de atravessar a rua.', c='c'),
  dict(en='Be careful with bikes.', pt='Cuidado com as bicicletas.', ex='Be careful with bikes and cars.', exp='Para chamar atenção a um perigo.', c='d'),
  dict(en='Have a safe walk!', pt='Boa caminhada!', ex='Thanks! Have a safe walk!', exp='Para se despedir de quem vai andar.', c='a'),
  dict(en='Safety first.', pt='Segurança em primeiro lugar.', ex='Wait for green. Safety first.', exp='Frase comum sobre segurança.', c='b')],
 expr_game=[
  dict(cue='O sinal está vermelho e um amigo vai atravessar.', opts=['Wait! The light is red.', 'Have a safe walk!', 'Safety first.'], ans=0, why='Wait! pede para parar.'),
  dict(cue='Você quer dizer ao amigo para olhar para os dois lados.', opts=['Look both ways!', 'Wait!', 'Have a safe walk!'], ans=0, why='Both ways = os dois lados.'),
  dict(cue='Você quer se despedir de alguém que vai andar.', opts=['Have a safe walk!', 'When the light is green.', 'Wait!'], ans=0, why='Have a safe walk! = Boa caminhada!')])
