#!/usr/bin/env python3
"""Porta de VOCABULÁRIO do Pocket (offline). Lê os episódios em ordem de curso (a1 -> a2 -> b1...) e mede:
 - novas: palavras (radicais) nunca vistas antes -> limite por nível (carga de vocabulário)
 - nao_ensinadas: palavra nova que NÃO está no V: nem nas opções do B: do próprio episódio
 - cobertura: % das palavras do episódio já conhecidas (ou ensinadas nele)
 - avancadas: palavras de lista de teto (B1+/raras) proibidas em A1/A2
 - reuso: % do V: de cada episódio que reaparece em >=2 episódios posteriores (reciclagem)
Uso: python3 audit_vocab.py [-v] [--relatorio]   (exit 1 se achados bloqueantes)"""
import re,sys,glob,os,json
R=os.path.dirname(os.path.abspath(__file__))
WARM=25  # os primeiros episódios do A1 não têm base anterior: só aprendem, não são cobrados
LIM={'a1':dict(novas=14,cob=0.80),'a2':dict(novas=14,cob=0.82),'b1':dict(novas=18,cob=0.85),'b2':dict(novas=22,cob=0.88),'c1':dict(novas=26,cob=0.90),'c2':dict(novas=30,cob=0.92)}
# teto: palavras que não pertencem a A1/A2 (B1+ / raras). Estender conforme novos achados.
ADV=set('''although whereas nevertheless furthermore moreover consequently whilst notwithstanding albeit hence thus
ubiquitous ambiguous meticulous reluctant substantial inevitable sophisticated elaborate comprehensive profound
prestigious eloquent resilient scrutinize implement leverage facilitate mitigate endeavor undermine
negotiate negotiation accomplish accomplishment ambitious arbitrary autonomy bureaucracy compromise
controversy controversial delegate hypothesis implication legislation phenomenon prejudice
sustainability sustainable infrastructure inflation recession liability mortgage dividend
unemployment immigration diplomatic ideology'''.split())
def stem(w):
    w=w.lower().strip("'")
    for suf in ('ing','ed','es','s','ly'):
        if len(w)>len(suf)+2 and w.endswith(suf):
            b=w[:-len(suf)]
            if suf in('ing','ed') and len(b)>2 and b[-1]==b[-2] and b[-1] not in 'ls':b=b[:-1]
            return b
    return w
def words(t):return re.findall(r"[A-Za-z]+(?:'[a-z]+)?",re.sub(r'\{\d\}',' ',t))
def order():
    fs=[]
    for lv in ('a1','a2','b1','b2','c1','c2'):
        fs+=sorted(glob.glob(os.path.join(R,lv+'_arco*.txt')),key=lambda p:int(re.findall(r'arco(\d+)',p)[0]))
    return fs
def episodes():
    out=[]
    for f in order():
        lv=os.path.basename(f)[:2];cur=None
        for ln in open(f,encoding='utf-8'):
            ln=ln.rstrip('\n')
            if ln.startswith('T:'):
                cur=dict(f=os.path.basename(f),lv=lv,t=ln[2:].split('|')[0].strip(),txt=[],teach=set(),opts=[]);out.append(cur)
            elif cur is not None and ln[:2] in('D:','K:','S:','R:','X:','B:'):
                p=ln[2:].split('|')
                if ln[0]=='D':cur['txt'].append(p[1] if len(p)>1 else '')
                elif ln[0]=='S':cur['txt']+= [p[1],p[3]] if len(p)>3 else []
                elif ln[0]=='B':
                    cur['txt'].append(p[0]);cur['opts']+=[o.split('=')[0] for o in (p[2].split(';') if len(p)>2 else [])]
                else:cur['txt'].append(p[0])
            elif cur is not None and ln.startswith('V:'):
                for it in ln[2:].split(';'):
                    cur['teach'].add(it.split('|')[0].strip().lower())
    return out
def main(verbose=False,rel=False):
    eps=episodes();seen=set();bad=[];tot={}
    teachpos={}
    for i,e in enumerate(eps):
        ws=[stem(w) for t in e['txt'] for w in words(t)]
        tw=set(stem(w) for x in e['teach']|set(o.lower() for o in e['opts']) for w in words(x))
        types=set(ws);new=types-seen;unt=new-tw
        known=sum(1 for w in ws if w in seen or w in tw)/max(1,len(ws))
        adv=[w for t in e['txt'] for w in words(t) if w.lower() in ADV and e['lv'] in('a1','a2')]
        L=LIM[e['lv']];warm=i<WARM;tag=f"{e['f']} #{i+1} {e['t']}"
        if not warm and len(new)>L['novas']:bad.append((tag,'carga',f'{len(new)} palavras novas (>{L["novas"]}): '+', '.join(sorted(new)[:8])))
        if not warm and known<L['cob']:bad.append((tag,'cobertura',f'{known:.0%} conhecidas (<{L["cob"]:.0%})'))
        if adv:bad.append((tag,'avancada','palavra de teto B1+: '+', '.join(adv)))
        if not warm and len(unt)>6:bad.append((tag,'nao_ensinadas',f'{len(unt)} novas fora do V:/B: — '+', '.join(sorted(unt)[:8])))
        d=tot.setdefault(e['lv'],dict(eps=0,novas=0,cob=0.0,unt=0));d['eps']+=1;d['novas']+=len(new);d['cob']+=known;d['unt']+=len(unt)
        for x in e['teach']:teachpos.setdefault(stem(x.split()[0]) if x else x,[]).append(i)
        seen|=types
    # reuso: palavra ensinada reaparece em >=2 episódios posteriores
    later=[set(stem(w) for t in e['txt'] for w in words(t)) for e in eps]
    reuse=ok=0
    for i,e in enumerate(eps):
        for x in e['teach']:
            s=stem(x.split()[0]) if x else x;reuse+=1
            if sum(1 for j in range(i+1,min(len(eps),i+400)) if s in later[j])>=2:ok+=1
    pr=ok/max(1,reuse)
    if rel or verbose:
        print(f"Episódios lidos: {len(eps)} (meta do curso: 4800 → {len(eps)/4800:.0%})  | vocabulário único: {len(seen)} radicais")
        for lv,d in tot.items():print(f"  {lv.upper()}: {d['eps']} eps | média novas/ep {d['novas']/d['eps']:.1f} | cobertura média {d['cob']/d['eps']:.0%} | não-ensinadas/ep {d['unt']/d['eps']:.1f}")
        print(f"  reuso (palavra ensinada volta ≥2x nos próximos 400 eps): {pr:.0%}")
    if verbose:
        for b in bad:print('  ',*b)
    if pr<0.45:bad.append(('curso','reuso',f'só {pr:.0%} do vocabulário ensinado reaparece (mín 45%)'))
    c={}
    for b in bad:c[b[1]]=c.get(b[1],0)+1
    print(len(bad),'achados');print(c)
    return len(bad)
if __name__=='__main__':
    sys.exit(1 if main('-v' in sys.argv,'--relatorio' in sys.argv) else 0)
