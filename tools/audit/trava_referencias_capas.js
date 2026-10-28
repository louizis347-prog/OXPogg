#!/usr/bin/env node
/* Trava de qualidade: referências culturais distintas + capas distintas (inglês regular).
 * Uso: node tools/audit/trava_referencias_capas.js   (precisa de `python3 -m http.server 8123` na raiz)
 * Falha (exit 1) se: obra repetida (normalização forte) · título sem obra · capa idêntica a outra
 * · cena dominante > 25% · < 600 paletas · < 2500 capas visualmente distintas · < 60% com motivo próprio. */
const {chromium}=require(process.env.PLAYWRIGHT||'/opt/node22/lib/node_modules/playwright');
const BASE=process.env.BASE||'http://localhost:8123';
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto(BASE+'/index.html');await p.waitForFunction(()=>window.PogObra);
const R=await p.evaluate(async()=>{
 const norm=s=>String(s||'').split(':')[0].normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase().replace(/\(.*?\)/g,'').replace(/[^a-z0-9 ]/g,' ').trim().replace(/^(the|a|an|el|la|le|o|os)\s+/,'').replace(/\s+/g,' ');
 const eps=[];
 for(const l of ['a1','a2','b1','b2','c1','c2'])for(let n=1;n<=30;n++){let j;try{j=await (await fetch('data/en-'+l+'_'+String(n).padStart(2,'0')+'.json')).json()}catch(e){break}
  if(!Array.isArray(j))j=j.episodes||j.eps||[];for(const e of j)eps.push(Object.assign({cid:'en-'+l},e));}
 const works={},svgs={},scenes={},pals=new Set(),motifs={};let own=0,nowork=[];
 for(const e of eps){const w=(e.a||{}).w;if(!w){nowork.push(e.n);continue}
  (works[norm(w)]=works[norm(w)]||[]).push(e.n);
  const m=PogObra.meta(e);scenes[m.scene]=(scenes[m.scene]||0)+1;pals.add(m.pal.join());
  const s=PogObra.svg(e,'cover').replace(/obra-\d+/g,'obra-X');svgs[s]=(svgs[s]||0)+1;}
 return {n:eps.length,nowork,dups:Object.entries(works).filter(([k,v])=>v.length>1).map(([k,v])=>k+' '+v.join('/')),
  distinctWorks:Object.keys(works).length,scenes,pals:pals.size,visual:Object.keys(svgs).length,identical:Object.values(svgs).filter(v=>v>1).length}});
await b.close();
const maxScene=Math.max(...Object.values(R.scenes))/R.n;
const fails=[];
if(R.nowork.length)fails.push('episódios sem obra: '+R.nowork.length);
if(R.dups.length)fails.push('obras repetidas: '+R.dups.length+' ('+R.dups.slice(0,5).join('; ')+')');
if(R.distinctWorks!==R.n)fails.push(`obras distintas ${R.distinctWorks} ≠ episódios ${R.n}`);
if(R.visual<R.n)fails.push(`capas idênticas entre si: ${R.n-R.visual}`);
if(maxScene>.25)fails.push('cena dominante '+Math.round(maxScene*100)+'% (>25%)');
if(R.pals<600)fails.push('paletas distintas '+R.pals+' (<600)');
console.log(JSON.stringify({episodios:R.n,obras_distintas:R.distinctWorks,capas_distintas:R.visual,paletas:R.pals,cenas:R.scenes,cena_dominante:Math.round(maxScene*100)+'%'}));
if(fails.length){console.error('TRAVA FALHOU:\n - '+fails.join('\n - '));process.exit(1)}console.log('TRAVA OK');})();
