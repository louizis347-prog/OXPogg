#!/usr/bin/env node
/* Trava de qualidade: referências culturais distintas + capas distintas (inglês regular).
 * Uso: node tools/audit/trava_referencias_capas.js   (precisa de `python3 -m http.server 8123` na raiz)
 * Falha (exit 1) se: obra repetida (normalização forte) · título sem obra · capa idêntica a outra
 * · cena dominante > 25% · < 600 paletas.
 * DETALHE (mínimos = menor valor medido nas 10 capas desenhadas à mão, arredondado para baixo):
 *   ≥110 elementos · ≥18 cores de preenchimento · ≥30 paths · ≥2 gradientes · ≥3 figuras com rosto
 *   (2 personagens + bichinho) · ≥6 itens de cenário. Cada recorte usado nos episódios precisa mostrar os rostos:
 *   O SVG precisa ser XML válido (sem atributos repetidos).
 *   cover/sticker/strip ≥2 rostos dentro do viewBox, face ≥1. */
const {chromium}=require(process.env.PLAYWRIGHT||'/opt/node22/lib/node_modules/playwright');
const BASE=process.env.BASE||'http://localhost:8123';
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto(BASE+'/index.html');await p.waitForFunction(()=>window.PogObra);
const R=await p.evaluate(async()=>{
 const norm=s=>String(s||'').split(':')[0].normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase().replace(/\(.*?\)/g,'').replace(/[^a-z0-9 ]/g,' ').trim().replace(/^(the|a|an|el|la|le|o|os)\s+/,'').replace(/\s+/g,' ');
 const eps=[];
 for(const l of ['a1','a2','b1','b2','c1','c2'])for(let n=1;n<=30;n++){let j;try{j=await (await fetch('data/en-'+l+'_'+String(n).padStart(2,'0')+'.json')).json()}catch(e){break}
  if(!Array.isArray(j))j=j.episodes||j.eps||[];for(const e of j)eps.push(Object.assign({cid:'en-'+l},e));}
 const MIN={el:110,fills:18,paths:30,grads:2,figs:3,decor:6},detail={};const bad={el:0,fills:0,paths:0,grads:0,figs:0,faces:0,decor:0};
 let hand=0;const works={},svgs={},scenes={},pals=new Set(),motifs={};let own=0,nowork=[];
 for(const e of eps){const w=(e.a||{}).w;if(!w){nowork.push(e.n);continue}
  (works[norm(w)]=works[norm(w)]||[]).push(e.n);
  const m=PogObra.meta(e);scenes[m.scene]=(scenes[m.scene]||0)+1;pals.add(m.pal.join());
  const s=PogObra.svg(e,'cover').replace(/obra-\d+/g,'obra-X');svgs[s]=(svgs[s]||0)+1;
  if(window.PogObraHand&&PogObraHand.has(e)){hand++;continue}
  for(const mode of ['cover','sticker','strip','face']){
   const box=document.createElement('div');box.innerHTML=PogObra.svg(e,mode);const sv=box.firstElementChild,all=[...sv.querySelectorAll('*')];
   if(mode==='cover'&&new DOMParser().parseFromString(PogObra.svg(e,mode),'image/svg+xml').querySelector('parsererror')){bad.xml=(bad.xml||0)+1;detail.xml=detail.xml||e.n}
   const fills=new Set(all.map(x=>x.getAttribute('fill')).filter(f=>f&&f!=='none'&&!/^url/.test(f)));
   const figs=[...sv.querySelectorAll('[data-fig]')],vb=sv.getAttribute('viewBox').split(' ').map(Number);
   const inView=figs.filter(g=>{const [x,y]=g.getAttribute('data-fig').split(',').map(Number);return x>=vb[0]&&x<=vb[0]+vb[2]&&y>=vb[1]&&y<=vb[1]+vb[3]}).length;
   const t=(c,k)=>{if(c){bad[k]++;if(!detail[k])detail[k]=e.n+'/'+mode}};
   if(mode==='cover'){t(all.length<MIN.el,'el');t(fills.size<MIN.fills,'fills');t(sv.querySelectorAll('path').length<MIN.paths,'paths');t(sv.querySelectorAll('linearGradient,radialGradient').length<MIN.grads,'grads');t(figs.length<MIN.figs,'figs');t(sv.querySelectorAll('[data-decor]').length<MIN.decor,'decor')}
   t(inView<(mode==='face'?1:2),'faces');}}
 return {hand,bad,detail,n:eps.length,nowork,dups:Object.entries(works).filter(([k,v])=>v.length>1).map(([k,v])=>k+' '+v.join('/')),
  distinctWorks:Object.keys(works).length,scenes,pals:pals.size,visual:Object.keys(svgs).length,identical:Object.values(svgs).filter(v=>v>1).length}});
await b.close();
const maxScene=Math.max(...Object.values(R.scenes))/R.n;
const fails=[];
if(R.nowork.length)fails.push('episódios sem obra: '+R.nowork.length);
if(R.dups.length)fails.push('obras repetidas: '+R.dups.length+' ('+R.dups.slice(0,5).join('; ')+')');
if(R.distinctWorks!==R.n)fails.push(`obras distintas ${R.distinctWorks} ≠ episódios ${R.n}`);
if(R.visual<R.n)fails.push(`capas idênticas entre si: ${R.n-R.visual}`);
for(const [k,v] of Object.entries(R.bad))if(v)fails.push(`detalhe insuficiente (${k}): ${v} capas/recortes, ex.: ${R.detail[k]}`);
if(maxScene>.25)fails.push('cena dominante '+Math.round(maxScene*100)+'% (>25%)');
if(R.pals<600)fails.push('paletas distintas '+R.pals+' (<600)');
console.log(JSON.stringify({episodios:R.n,obras_distintas:R.distinctWorks,capas_distintas:R.visual,desenhadas_a_mao:R.hand,paletas:R.pals,cenas:R.scenes,cena_dominante:Math.round(maxScene*100)+'%'}));
if(fails.length){console.error('TRAVA FALHOU:\n - '+fails.join('\n - '));process.exit(1)}console.log('TRAVA OK');})();
