"""IPA americano via CMUdict (sem inventar: devolve '' se alguma palavra faltar)."""
import re
import cmudict
_D = cmudict.dict()
M = {'AA':'ɑ','AE':'æ','AH':'ʌ','AO':'ɔ','AW':'aʊ','AY':'aɪ','EH':'ɛ','ER':'ɚ','EY':'eɪ','IH':'ɪ','IY':'i','OW':'oʊ','OY':'ɔɪ','UH':'ʊ','UW':'u',
     'B':'b','CH':'tʃ','D':'d','DH':'ð','F':'f','G':'ɡ','HH':'h','JH':'dʒ','K':'k','L':'l','M':'m','N':'n','NG':'ŋ','P':'p','R':'ɹ','S':'s','SH':'ʃ','T':'t','TH':'θ','V':'v','W':'w','Y':'j','Z':'z','ZH':'ʒ'}
def word(w):
    p = _D.get(w.lower())
    if not p: return ''
    syms = []  # (symbol, stress, is_vowel)
    for ph in p[0]:
        m = re.match(r'([A-Z]+)(\d?)$', ph)
        b, s = m.group(1), m.group(2)
        v = bool(s)
        sym = 'ə' if (b == 'AH' and s == '0') else M[b]
        syms.append([sym, s, v])
    marks = {}
    for i, (sym, s, v) in enumerate(syms):
        if s in ('1', '2'):
            j = i
            while j > 0 and not syms[j-1][2]: j -= 1
            n = i - j
            if j > 0 and n > 1:
                j = i - (3 if (n >= 3 and syms[i-n][0] == 's') else 2)
            elif j > 0:
                j = i - n
            marks[j] = 'ˈ' if s == '1' else 'ˌ'
    return ''.join(marks.get(i, '') + sy[0] for i, sy in enumerate(syms))
def ipa(phrase):
    ws = re.findall(r"[A-Za-z']+", phrase)
    if not ws or len(ws) > 4: return ''
    r = [word(w) for w in ws]
    return '' if not all(r) else '/' + ' '.join(r) + '/'
if __name__ == '__main__':
    for t in ['name', 'first name', 'teacher', 'pen pal', 'xyzzy']: print(t, ipa(t))
