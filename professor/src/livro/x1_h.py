"""Auxiliares do lote X1 (B2-L103 a B2-L202): V compacto e Q com pronúncia padrão para os rótulos do plano."""
from q import *
import q as _q
def V(s):
    o=[]
    for p in s.split('|'):
        e,t=p.split('=');o.append(f'{e};{t};{e[0].upper()+e[1:]}.;{t[0].upper()+t[1:]}.')
    return o
PR={'Ligações e assimilação':('Sons se ligam e se transformam: did you → didja; want you → wanchu; pick it up → pi-ki-dup.',['did you','want you','pick it up','last night','what you']),
'Entonação de contraste, surpresa, dúvida':('Tom desce-sobe para contraste e surpresa; sobe para dúvida: Really? ↗ I said BLUE, not green.',['Really?','You did?','I said blue.','Not that one.','Is that so?']),
'Acento para enfatizar informação':('A palavra nova ou importante recebe o acento mais forte: I want the RED one, not the blue one.',['I want the RED one.','She said TUESDAY.','Not TWO, THREE.','He BOUGHT it.']),
'Fala monitorada × informal':('Fala monitorada usa a forma completa; a informal reduz: going to → gonna, want to → wanna, kind of → kinda.',['going to / gonna','want to / wanna','kind of / kinda','got to / gotta','give me / gimme']),
'Flap T americano':('Entre vogais o /t/ americano vira um toque rápido /ɾ/: water, better, city, got it.',['water','better','city','got it','a lot of']),
'Redução de palavras funcionais (to, of, for, and, can)':('Palavras funcionais ficam fracas: to /tə/, of /əv/, for /fər/, and /ən/, can /kən/.',['a cup of tea','fish and chips','I can go','time to go','for me'])}
def Q(id,*a,**k):
    k.setdefault('pron',PR.get(_q.PLAN[id]['pron']))
    return _q.Q(id,*a,**k)
