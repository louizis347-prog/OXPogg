#!/usr/bin/env python3
"""Porta de nível B1 (CEFR/PET): barra estruturas B2+ nas falas (D), frase-chave (K), exemplos (S,R), peças (B) e expressão (X).
Permitido no B1: tudo do A2 + condicional 2, used to, discurso indireto simples, present perfect contínuo, past perfect,
passiva (inclusive com agente), might/may, orações relativas (who/which/that/where), although/unless/whenever/however, wish + passado, so...that.
Proibido (B2+): 3º condicional / would have, should/could/must have + particípio, inversão negativa, subjuntivo,
future perfect, gerúndio perfeito, whereas/nevertheless/furthermore/moreover/consequently/notwithstanding/albeit/hence/thus,
cleft sentences (It was ... that / What I ... is), I wish + had, mixed conditionals, passive continuous complexa, 'were to', 'had better' etc."""
import re,glob,sys,collections
RULES=[
 ('3º condicional / would have',r"\bwould (?:not |never )?have \w+|\bif (?:i|you|he|she|we|they|it) had (?:\w+ed|been|gone|seen|done|known|taken|told|said|found|made)\b.*\bwould\b"),
 ('perfeito modal (B2)',r"\b(?:should|could|must|may|might|can't|cannot|couldn't) have (?:been|\w+ed|gone|seen|done|known|said|eaten|taken|told|made|found|heard)\b"),
 ('wish + past perfect',r"\bi wish (?:i|you|he|she|we|they|it) had\b|\bif only (?:i|you|he|she|we|they|it) had\b"),
 ('inversão negativa',r"\b(?:never|seldom|rarely|hardly|barely|scarcely|nowhere|little) (?:have|has|had|did|do|does|will|would|can|could) (?:i|you|he|she|we|they|it)\b|\bnot only [^.?!]*\b(?:but also)\b|\bno sooner\b|\bnot until\b"),
 ('conectivos B2',r"\b(?:whereas|nevertheless|nonetheless|furthermore|moreover|consequently|notwithstanding|albeit|hence|thus|henceforth|thereby|therefore|whilst|supposing|provided that|on condition that)\b"),
 ('future perfect',r"\bwill have (?:\w+ed|been|gone|seen|done|finished|taken|made|left|got|had)\b|\bwill have been \w+ing\b"),
 ('gerúndio perfeito',r"\bhaving (?:\w+ed|been|done|seen|made|taken|gone|left|had|got|written|known)\b"),
 ('cleft',r"\bit (?:was|is) [^.?!,]{1,30} that\b|\bwhat i (?:need|want|like|love|hate|mean|think) is\b|\bthe (?:thing|reason|place|person) (?:that|who|where) [^.?!]* is\b"),
 ('were to / had better / supposed to',r"\bwere to\b|\bhad better\b|\bwould rather\b|\bwould sooner\b|\bbe supposed to\b"),
 ('subjuntivo',r"\bit is (?:essential|important|vital|necessary) that (?:he|she|they|you|we|i) (?:be|go|come|take|do)\b|\binsist(?:ed)? that\b|\bsuggest(?:ed)? that\b|\bdemand(?:ed)? that\b"),
 ('passiva complexa',r"\b(?:is|are|was|were) being \w+ed\b|\bhas been \w+ed by\b.*\bwhich\b|\bis said to\b|\bis believed to\b|\bis thought to\b"),
 ('particípio absoluto',r"^[^.?!]*\b(?:being|having) \w+, (?:i|we|he|she|they|it|the)\b"),
 ('mixed conditionals',r"\bif (?:i|you|he|she|we|they|it) had (?:\w+ed|been|gone|seen|done|known|taken|told|said|found|made|come|left|met|gotten|got)\b[^.?!]*, (?:i|you|he|she|we|they|it) would (?!have)\b"),
 ('expressões B2+',r"\b(?:in spite of|on account of|with regard to|regarding the fact|due to the fact|in view of|by virtue of|as regards|insofar|inasmuch|hitherto|heretofore)\b"),
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
def main(pattern='b1_arco*.txt'):
    bad=[];cnt=collections.Counter()
    for f,i,l,t in lines(pattern):
        for name,rx in RULES:
            if re.search(rx,t):bad.append((f,i,name,l));cnt[name]+=1
    return bad,cnt
if __name__=='__main__':
    bad,cnt=main(sys.argv[1] if len(sys.argv)>1 and not sys.argv[1].startswith('-') else 'b1_arco*.txt')
    print(len(bad),'achados');print(dict(cnt))
    if '-v' in sys.argv:
        for f,i,n,l in bad:print(f,i,n,'|',l[:150])
    sys.exit(1 if bad else 0)
