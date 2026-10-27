# Camada de reescrita dos episódios B1 173–250 (ver ovrb1.py): auxiliar C() compacta os dados de cada continuação.
from v3.ovrb1 import OVR, L


def C(n, nm, ids, rs, cv, obra, hot4, vocab, verbs, lab, lines, quiz, fill):
    """nm: nomes; lines: (0|1, en, pt); quiz: (pergunta, pt, [3 opções (emoji, texto)], índice da fala); lab: (pt, dica, 3 palavras)."""
    ls = [[nm[s], en, pt] for s, en, pt in lines]
    q = [(a, b, c, 0, i, '%s diz: “%s”' % (ls[i][0], ls[i][1])) for a, b, c, i in quiz]
    voc = [(e, w, pt, 'Soa como “%s”.' % p) for e, w, pt, p in vocab]
    ws = lab[2]
    OVR[n] = dict(names=nm, ids=ids, rs=rs, cv=cv, obra=(ls[obra][1], ls[obra][2]), hot4=hot4, vocab=voc, verbs=verbs,
                  lab=L('l%d' % n, 'Laboratório de sons: %s, %s e %s' % (ws[0][0], ws[1][0], ws[2][0]), lab[0], lab[1], ws),
                  lines=ls, quiz=q, fill=fill)
