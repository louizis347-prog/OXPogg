"""Porta de nível A1: o diálogo não pode usar futuro, passado nem estruturas A2+.
Permitidos como blocos prontos: would like, can/could you, may I, let us."""
import re,glob,collections
STRICT=r"\b(will|won't|going to|gonna|did|didn't|was|wasn't|were|weren't|went|saw|ate|took|made|came|left|met|forgot|lost|woke|flew|bought|told|found|gave|got|had|watched|stayed|visited|moved|called|played|lived|loved|tried|walked|happened|started|finished|learned|asked|helped|should|might|must|have to|has to|used to|been)\b"
def eps(pattern='a1_arco*.txt'):
    for f in sorted(glob.glob(pattern)):
        cur=None
        for l in open(f):
            l=l.rstrip('\n')
            if l.startswith('T:'):
                if cur: yield cur
                cur={'f':f,'t':l[2:].split('|')[0].strip(),'en':[]}
            elif cur and l.startswith('D:'): cur['en'].append(l.split('|')[1])
            elif cur and l.startswith('K:'): cur['en'].append(l[2:].split('|')[0])
        if cur: yield cur
if __name__=='__main__':
    n=bad=0;por=collections.Counter()
    for e in eps():
        n+=1
        h=set(re.findall(STRICT,' '.join(e['en']).lower()))
        if h:
            bad+=1;por[e['f'][7:9]]+=1
    print('episódios',n,'acima do A1',bad);print(sorted(por.items()))
