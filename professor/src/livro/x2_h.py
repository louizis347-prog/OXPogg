"""Auxiliar do lote X2: notas de pronúncia para rótulos que o q.py não conhece (B2 e C1)."""
from q import *
import q as _q
PNX={
'Redução de palavras funcionais (to, of, for, and, can)':('Palavras funcionais ficam fracas: to /tə/, of /əv/, for /fər/, and /ən/, can /kən/. Só ganham força no fim da frase ou em contraste (Yes, I CAN).',['a cup of tea','going to go','for a minute','you and me','I can swim']),
'Flap T americano':('No inglês americano, o /t/ entre vogais soa como um /d/ rápido (flap): water, better, city, a lot of.',['water','better','city','a lot of','meeting']),
'Ligações e assimilação':('Sons se ligam e se transformam: did you → didja, want you → wanchu, pick it up → pi-ki-dup.',['did you','want you','pick it up','last night']),
'Entonação de contraste, surpresa, dúvida':('A voz sobe na dúvida e na surpresa (Really? ↗) e desce na certeza; no contraste, a palavra-chave sobe e a outra fica baixa.',['Really? ↗','I said BLUE, not green.','It’s ready. ↘','Maybe? ↗']),
'Acento para enfatizar informação':('O acento muda de lugar para destacar a informação nova: I want the RED one / I WANT the red one.',['I want the RED one.','She SAID she’d come.','It’s not MY idea.']),
'Fala monitorada × informal':('Na fala monitorada (reunião, prova) pronunciamos as formas completas; na informal reduzimos: going to → gonna, because → ’cause.',['going to / gonna','because / ’cause','want to / wanna','give me / gimme']),
'Ênfase intencional':('A ênfase intencional destaca a palavra que carrega o sentido: sílaba forte, mais longa e mais alta. Mudar a palavra enfatizada muda a mensagem.',['I didn’t say HE stole it.','I didn’t SAY he stole it.','Not only did she COME, she LED.']),
'Pausas e ritmo':('Faça pausas curtas entre grupos de sentido (thought groups) e mantenha o ritmo: sílabas fortes em intervalos regulares, fracas comprimidas.',['In my view, | the plan | is sound.','Having reviewed the data, | we agreed.']),
'Expressividade':('A expressividade vem de variar altura, volume e velocidade: sobe para entusiasmo, desce para firmeza, pausa antes da ideia importante.',['That is absolutely remarkable!','I was, frankly, astonished.','Well… it depends.']),
'Organização da informação pela entonação':('A entonação organiza o discurso: queda = informação completa; subida = há mais por vir; a informação nova recebe o foco (nuclear stress).',['First, ↗ we cut costs. ↘','If it fails, ↗ we adapt. ↘','The key point ↗ is timing. ↘']),
}
_Q=_q.Q
def Q(id,*a,**k):
    if 'pron' not in k and PLAN[id]['pron'] in PNX:k['pron']=PNX[PLAN[id]['pron']]
    return _Q(id,*a,**k)
