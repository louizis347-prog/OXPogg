#!/usr/bin/env python3
"""Porta de nível A2 (CEFR/KET): barra estruturas B1+ nas falas (D), frase-chave (K), exemplos (S,R) e peças (B).
Permitido no A2: presente, passado simples, was/were + -ing, going to/will, comparativos/superlativos, can/could/may(pedido)/must/should/have to,
present perfect simples (ever/never/just/already/yet/for/since), if + presente + will, used to NÃO (B1)."""
import re,glob,sys,collections
RULES=[
 ('pres.perf.contínuo',r"\b(?:have|has|'ve) been \w+ing\b"),
 ('condicional 2 (if+passado)',r"\bif (?:i|you|he|she|we|they|it) (?:were|had|could|knew|won|found|lived|woke|got|made|took|came|went|saw|did|was)\b"),
 ('would hipotético',r"\bwhere would you\b|\bwhat would you (?!like)|\bi would (?:visit|wait|go|do|have|say|help|call|take|stay|buy|open|read|travel|start|sleep|run|eat|try)\b|\bif [^.?!]* would (?!like|love)"),
 ('past perfect',r"\bhad (?:\w+ed|been|gone|seen|done|eaten|left|taken|given|found|met|made|told|written|lost|known|become|begun|come|heard|read|said|thought|spoken|sold|paid|run|sat|stood)\b"),
 ('discurso indireto',r"\b(?:said|told me|asked me|told us) (?:that\b|i\b|he\b|she\b|we\b|they\b)|\btold (?:me|us|him|her|them) to\b|\basked (?:me|us|him|her|them) to\b"),
 ('passiva com agente',r"\b(?:was|were|is|are|been) \w+ed by\b|\bwas (?:built|made|written|given|sold) by\b"),
 ('might / may (possibilidade)',r"\bmight\b|\bmay (?:be|need|snow|rain|spend|sleep|have|help|get|come|go|feel|take|see|want|happen|not)\b"),
 ('conectivos B1',r"\b(?:unless|although|though|whenever|whereas|nevertheless|despite|however|therefore|otherwise|whether|as long as|in case)\b"),
 ('used to',r"\bused to \w+|\bget(?:ting)? used to\b|\bam used to\b|\bwhat did you use to\b"),
 ('so...that',r"\bso \w+ that\b|\bsuch (?:a|an) \w+ that\b"),
 ('wish / if only',r"\bi wish\b|\bif only\b"),
 ('perfeito modal',r"\b(?:should|could|must|would) have (?:been|\w+ed|gone|seen|done|known|said|eaten|taken)\b"),
 ('gerúndio perfeito',r"\bhaving \w+ed\b|\bhaving (?:been|done|seen)\b"),
 ('the more... the more',r"\\bthe (?:more|less|\\w+er) [^.?!,]*, the (?:more|less|\\w+er)\\b"),
 ('whom/whose',r"\bwhom\b|\bwhose\b"),
 ('what/where to + verbo',r"\b(?:what|where|who) to \w+\b"),
]
def lines(pattern):
    for f in sorted(glob.glob(pattern)):
        for i,l in enumerate(open(f,encoding='utf-8'),1):
            l=l.rstrip('\n')
            k=l[:2]
            if k in('D:','K:','S:','R:','B:','X:'):
                parts=l[2:].split('|')
                if k=='D:' and len(parts)>=2:txt=parts[1]
                elif k=='K:':txt=parts[0]
                elif k=='S:' and len(parts)>=5:txt=parts[1]+' | '+parts[3]
                elif k=='R:':txt=parts[0]
                elif k=='B:':txt=parts[0]+' | '+' | '.join(o.split('=')[0] for o in (parts[2].split(';') if len(parts)>2 else []))
                elif k=='X:':txt=parts[0]
                else:continue
                yield f,i,l,txt.lower().replace('’',"'")
def main(pattern='a2_arco*.txt'):
    bad=[];cnt=collections.Counter()
    for f,i,l,t in lines(pattern):
        for name,rx in RULES:
            if re.search(rx,t):bad.append((f,i,name,l));cnt[name]+=1
    return bad,cnt
if __name__=='__main__':
    bad,cnt=main(sys.argv[1] if len(sys.argv)>1 else 'a2_arco*.txt')
    print(len(bad),'achados');print(dict(cnt))
    if '-v' in sys.argv:
        for f,i,n,l in bad:print(f,i,n,'|',l[:150])
    sys.exit(1 if bad else 0)
