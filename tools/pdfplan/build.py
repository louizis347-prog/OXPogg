#!/usr/bin/env python3
"""Gera um PDF de planejamento por curso regular (capa, alinhamento CEFR/exame, tabela dos episódios por nível).
Fonte: data/<curso>-<nivel>_NN.json (+ data/skel/en-*.json para o roteiro do inglês). Saída: docs/planos/<curso>.pdf"""
import json,re,html,subprocess,sys,os
R=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(R)
LV=['a1','a2','b1','b2','c1','c2']
M=json.load(open('data/manifest.json'))
CEFR={'a1':'Iniciante','a2':'Básico','b1':'Intermediário','b2':'Intermediário avançado','c1':'Avançado','c2':'Maestria'}
EX={ # nível -> exame de proficiência (correspondência aproximada)
'en':('Inglês americano para brasileiros','Cambridge English · IELTS · TOEFL',{'a1':'Cambridge Pre-A1 / A1 (Starters, Movers)','a2':'Cambridge A2 Key · IELTS ~3.0–4.0','b1':'Cambridge B1 Preliminary · IELTS 4.0–5.0','b2':'Cambridge B2 First · IELTS 5.5–6.5','c1':'Cambridge C1 Advanced · IELTS 7.0–8.0','c2':'Cambridge C2 Proficiency · IELTS 8.5–9.0'},'#2E6F95','🇺🇸','Português'),
'es':('Espanhol para brasileiros','DELE (Instituto Cervantes) · SIELE',{k:'DELE '+k.upper() for k in LV},'#D2404F','🇪🇸','Português'),
'fr':('Francês para hispanofalantes','DELF / DALF (França Educação Internacional)',{'a1':'DELF A1','a2':'DELF A2','b1':'DELF B1','b2':'DELF B2','c1':'DALF C1','c2':'DALF C2'},'#3E5FA0','🇫🇷','Español'),
'frbr':('Francês para brasileiros','DELF / DALF (França Educação Internacional)',{'a1':'DELF A1','a2':'DELF A2','b1':'DELF B1','b2':'DELF B2','c1':'DALF C1','c2':'DALF C2'},'#3E5FA0','🇫🇷','Português'),
'it':('Italiano para brasileiros','CILS (Siena) · CELI (Perugia)',{'a1':'CILS A1 · CELI impatto','a2':'CILS A2 · CELI 1','b1':'CILS B1 · CELI 2','b2':'CILS B2 · CELI 3','c1':'CILS C1 · CELI 4','c2':'CILS C2 · CELI 5'},'#2E7D32','🇮🇹','Português'),
'de':('Alemão para brasileiros','Goethe-Zertifikat · telc · TestDaF',{k:'Goethe-Zertifikat '+k.upper() for k in LV},'#C9A227','🇩🇪','Português'),
'ja':('Japonês para brasileiros','JLPT (Japanese-Language Proficiency Test)',{'a1':'JLPT N5','a2':'JLPT N4','b1':'JLPT N3','b2':'JLPT N2','c1':'JLPT N1','c2':'Além do N1 (sem exame equivalente)'},'#D6336C','🇯🇵','Português'),
'ko':('Coreano para brasileiros','TOPIK (Test of Proficiency in Korean)',{'a1':'TOPIK I · nível 1','a2':'TOPIK I · nível 2','b1':'TOPIK II · nível 3','b2':'TOPIK II · nível 4','c1':'TOPIK II · nível 5','c2':'TOPIK II · nível 6'},'#D6336C','🇰🇷','Português'),
'zhbr':('Mandarim para brasileiros','HSK (Hànyǔ Shuǐpíng Kǎoshì)',{'a1':'HSK 1','a2':'HSK 2','b1':'HSK 3','b2':'HSK 4','c1':'HSK 5','c2':'HSK 6 (e níveis 7–9 do HSK 3.0)'},'#C62828','🇨🇳','Português'),
'pt':('Português do Brasil para hispanofalantes','Celpe-Bras (só certifica nível intermediário ou acima)',{'a1':'Sem exame oficial (preparatório)','a2':'Sem exame oficial (preparatório)','b1':'Sem exame oficial (preparatório)','b2':'Celpe-Bras Intermediário','c1':'Celpe-Bras Avançado','c2':'Celpe-Bras Avançado Superior'},'#2E9E6A','🇧🇷','Español'),
'enesh':('Inglés americano para hispanohablantes','Cambridge English · IELTS · TOEFL',{'a1':'Cambridge Pre-A1 / A1','a2':'Cambridge A2 Key · IELTS ~3.0–4.0','b1':'Cambridge B1 Preliminary · IELTS 4.0–5.0','b2':'Cambridge B2 First · IELTS 5.5–6.5','c1':'Cambridge C1 Advanced · IELTS 7.0–8.0','c2':'Cambridge C2 Proficiency · IELTS 8.5–9.0'},'#2E6F95','🇺🇸','Español'),
}
esc=lambda s:html.escape(str(s if s is not None else ''))
def strip(s):return re.sub(r'\*\*','',str(s or ''))
def vocab(x):
    out=[]
    for w in (x.get('v') or [])[:8]:
        if isinstance(w,(list,tuple)) and w:
            a=str(w[0]); b=''
            if len(w)>1 and isinstance(w[1],str) and not re.match(r'^[\U0001F000-\U0001FFFF☀-➿]',w[1]) : b=w[1]
            elif len(w)>2 and isinstance(w[2],str): b=w[2]
            out.append(a+(' ('+b+')' if b else ''))
        else: out.append(str(w))
    return ', '.join(out)
def gram(x):
    g=x.get('g')
    if isinstance(g,dict) and isinstance(g.get('t'),str): return strip(g['t'])
    return ''
def title(x):
    return re.sub(r'^[ABC][12]\s*·\s*(Épisode|Episodio|Episódio|Episode|エピソード)\s*\d+\s*[:：]\s*','',str(x.get('t') or ''))
def frames_roteiro(x):
    v=[];e=[]
    for f in x.get('fr') or []:
        if f.get('k')=='verbs':
            v=[(i.get('v'),i.get('pt')) for i in f.get('items',[]) if isinstance(i,dict)]
        if f.get('k')=='pgexp':
            e=[(i.get('en') or i.get('es') or i.get('fr') or i.get('t'),i.get('pt'),i.get('tag')) for i in f.get('items',[]) if isinstance(i,dict)]
    return v,e
def load(cid):
    items=[]
    for lv in LV:
        for f in M[f'{cid}-{lv}']:
            for x in json.load(open('data/'+f)): x['_lv']=lv; items.append(x)
    return items
def build(cid):
    name,exam,exmap,color,flag,lang=EX[cid]
    items=load(cid)
    skel={}
    if cid=='en':
        for lv in LV:
            for s in json.load(open(f'data/skel/en-{lv}.json')): skel[s['n']]=s
    has_pairs=any('xn' in x for x in items) and cid=='en'
    rows_by={lv:[] for lv in LV}
    ep=0
    for x in items:
        ep+=1
        rows_by[x['_lv']].append((ep,x))
    # en: ep range (pares)
    def eprange(ep,x):
        return str(ep)
    # numeração em pares para en
    if cid=='en':
        rows_by={lv:[] for lv in LV}; k=0
        for x in items:
            k+=1; rows_by[x['_lv']].append((k,x))
    show_rt=(cid=='en')
    css=f'''<style>
@page{{size:A4 landscape;margin:9mm 8mm}}@page cover{{size:A4 portrait;margin:0}}
*{{box-sizing:border-box}}body{{font:8.6px/1.28 system-ui,"Noto Sans",sans-serif;color:#1d1a2e;margin:0}}
.cover{{page:cover;height:297mm;width:210mm;padding:26mm 20mm;color:#fff;background:linear-gradient(155deg,{color} 0%,#1d1a2e 78%);position:relative;overflow:hidden;break-after:page}}
.cover:before{{content:"";position:absolute;right:-60mm;top:-40mm;width:150mm;height:150mm;border-radius:50%;background:rgba(255,255,255,.08)}}
.cover:after{{content:"";position:absolute;left:-40mm;bottom:-50mm;width:130mm;height:130mm;border-radius:50%;background:rgba(255,255,255,.06)}}
.brand{{font-size:15px;letter-spacing:.35em;text-transform:uppercase;opacity:.85;font-weight:700}}
.flag{{font-size:70px;margin:34mm 0 6mm}}
.cover h1{{font-size:44px;line-height:1.05;margin:0 0 8mm;max-width:150mm;font-weight:800}}
.cover .sub{{font-size:17px;opacity:.9;max-width:140mm;line-height:1.35}}
.stats{{display:flex;gap:6mm;margin-top:18mm;position:relative;z-index:1}}
.stat{{background:rgba(255,255,255,.14);border-radius:14px;padding:6mm 7mm;min-width:38mm}}
.stat b{{display:block;font-size:30px}}.stat span{{font-size:11px;opacity:.85}}
.foot{{position:absolute;left:20mm;bottom:16mm;font-size:11px;opacity:.8;z-index:1}}
h2{{font-size:16px;margin:0 0 3mm;color:{color}}}h3{{font-size:13px;margin:0 0 2mm}}
.pg{{break-after:page}}.note{{background:#f6f4fb;border-left:4px solid {color};padding:3mm 4mm;margin:3mm 0;font-size:10px;line-height:1.45;border-radius:6px}}
table{{border-collapse:collapse;width:100%}}th,td{{border:1px solid #c9c4d8;padding:2px 4px;vertical-align:top;text-align:left}}
th{{background:{color};color:#fff;font-size:8.4px}}tr{{break-inside:avoid}}tr:nth-child(even) td{{background:#faf9fd}}
small{{color:#6a6580}}.lvhead{{display:flex;justify-content:space-between;align-items:baseline;border-bottom:3px solid {color};margin:0 0 2mm;padding-bottom:1mm}}
.bt td{{font-size:10.5px;padding:4px 6px}}</style>'''
    h=[f'<!doctype html><meta charset=utf-8><title>{esc(name)}</title>',css]
    n=len(items)
    h.append(f'<section class="cover"><div class="brand">Pogglot</div><div class="flag">{flag}</div><h1>{esc(name)}</h1><div class="sub">Planejamento dos episódios, do A1 ao C2, alinhado ao CEFR e ao exame {esc(exam)}.</div>'
             f'<div class="stats"><div class="stat"><b>{n:,}</b><span>episódios</span></div><div class="stat"><b>6</b><span>níveis CEFR</span></div><div class="stat"><b>{len(rows_by["a1"])+sum(len(rows_by[l]) for l in LV[1:]):,}</b><span>{"pares de episódios" if cid=="en" else "linhas de planejamento"}</span></div></div>'
             f'<div class="foot">Material de planejamento interno · idioma da interface: {lang}</div></section>'.replace(',','.'))
    # alinhamento
    h.append('<section class="pg"><h2>Alinhamento: CEFR e exame de proficiência</h2><table class="bt"><tr><th>Nível<th>CEFR<th>Exame de referência<th>Episódios<th>Faixa de episódios</tr>')
    ep0=1
    for lv in LV:
        cnt=sum(1 for x in items if x['_lv']==lv)
        h.append(f'<tr><td><b>{lv.upper()}</b><td>{CEFR[lv]}<td>{esc(exmap[lv])}<td>{cnt}<td>{ep0}–{ep0+cnt-1}</tr>'.replace(',',',')); ep0+=cnt
    h.append('</table>')
    h.append(f'<div class="note"><b>Exame de referência:</b> {esc(exam)}. A correspondência entre nível CEFR e exame é aproximada (cada banca publica a sua própria equivalência).</div>')
    notes=[]
    if cid=='en': notes.append('Cada linha é um episódio, com conteúdo próprio. As colunas de verbos, expressões e gírias são o roteiro do episódio; onde aparece <i>(em elaboração)</i>, o roteiro próprio ainda será escrito.')
    else: notes.append('Cada linha é um episódio, na ordem em que aparece no curso.')
    notes.append('O vocabulário mostrado é o das primeiras palavras do episódio; a coluna de gramática fica em branco (—) quando o episódio ainda não tem uma estrutura gramatical definida nos dados.')
    h.append('<div class="note">'+' '.join(notes)+'</div></section>')
    cols='<tr><th style="width:5%">Ep<th style="width:15%">Título<th style="width:16%">Tema / objetivo<th style="width:14%">Estrutura gramatical<th style="width:'+str(18 if show_rt else 48)+'%">Vocabulário'
    if show_rt: cols+='<th style="width:9%">Verbos<th style="width:14%">Expressões comuns<th style="width:9%">Gírias'
    cols+='</tr>'
    for lv in LV:
        rows=rows_by[lv]
        h.append(f'<section class="pg"><div class="lvhead"><h2>{lv.upper()} · {CEFR[lv]}</h2><small>{esc(exmap[lv])} · {sum(1 for x in items if x["_lv"]==lv)} episódios</small></div><table>{cols}')
        for ep,x in rows:
            sk=skel.get(x['n']) if cid=='en' else None
            if sk and sk.get('status')=='roteiro':
                r=f'<tr><td>{eprange(ep,x)}<td><b>{esc(sk["titulo"])}</b><td>{esc(sk["tema"])}<td>{esc(sk["gramatica"].get("estrutura") or "—")}<td>{esc(", ".join(a+" ("+b+")" if b else a for a,b in sk["vocabulario_pt"]))}'
            else:
                r=f'<tr><td>{eprange(ep,x)}<td><b>{esc(title(x))}</b><td>{esc(strip(x.get("s")))}<td>{esc(gram(x)) or "—"}<td>{esc(vocab(x))}'
            if show_rt:
                s=skel.get(x['n'])
                if s and s.get('status')=='pendente':
                    r=r.replace('<td>'+esc(vocab(x))+'</tr>','') if False else r
                    r+='<td colspan=3><i>(em elaboração)</i>'
                elif s and s.get('status')=='roteiro':
                    vb=', '.join(a for a,b in s['verbos']); ex='<br>'.join(f'{esc(a)} <small>{esc(b)}</small>' for a,b in s['expressoes']); gi='<br>'.join(f'{esc(a)} <small>{esc(b)}</small>' for a,b in (s.get('girias') or []))
                    g2=s['gramatica'].get('estrutura') or ''
                    r=r.replace('<td>—<td>','<td>'+esc(g2 or '—')+'<td>',1) if not gram(x) else r
                else:
                    v,e=frames_roteiro(x)
                    vb=', '.join(f'{a}' for a,b in v)
                    ex='<br>'.join(f'{esc(a)} <small>{esc(b)}</small>' for a,b,t in e if t!='Gíria'); gi='<br>'.join(f'{esc(a)} <small>{esc(b)}</small>' for a,b,t in e if t=='Gíria')
                r+=f'<td>{esc(vb) or "—"}<td>{ex or "—"}<td>{gi or "—"}'
            h.append(r+'</tr>')
        h.append('</table></section>')
    out=f'/tmp/plan_{cid}.html'
    open(out,'w').write(''.join(h))
    return out
if __name__=='__main__':
    cids=sys.argv[1:] or list(EX)
    os.makedirs('docs/planos',exist_ok=True)
    js="const {chromium}=require('/opt/node-tools/node_modules/playwright');(async()=>{const b=await chromium.launch();for(const [i,o] of JSON.parse(process.argv[2])){const p=await b.newPage();await p.goto('file://'+i);await p.pdf({path:o,format:'A4',landscape:true,printBackground:true,preferCSSPageSize:true});await p.close()}await b.close()})()"
    open('/tmp/pdfplan.js','w').write(js)
    jobs=[(build(c),f'{R}/docs/planos/{c}.pdf') for c in cids]
    subprocess.run(['node','/tmp/pdfplan.js',json.dumps(jobs)],check=True)
    for c in cids: print(c,os.path.getsize(f'docs/planos/{c}.pdf')//1024,'KB')
