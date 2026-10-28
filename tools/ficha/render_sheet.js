// Renderiza as fichas de um JSON numa folha de capas (PNG) para conferir a arte SEM servidor. Uso: node tools/ficha/render_sheet.js fichas.json saida.png [colunas=4]
const { chromium } = require('playwright'); const fs=require('fs'),path=require('path');
(async()=>{
  const [,, src, out, colsArg]=process.argv; const cols=+colsArg||4;
  const F=JSON.parse(fs.readFileSync(src,'utf8')); const root=path.join(__dirname,'..','..','js');
  const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1500,height:900}});
  p.on('pageerror',e=>console.log('ERRO',e.message));
  await p.setContent(`<style>body{margin:0;background:#fff;font:12px system-ui}.g{display:grid;grid-template-columns:repeat(${cols},1fr);gap:8px;padding:8px}.c svg{width:100%;height:auto;display:block;border-radius:10px}b{display:block;padding:2px 4px}</style><div class="g" id="g"></div>`);
  await p.addScriptTag({path:path.join(root,'obra-ficha-lib.js')}); await p.addScriptTag({path:path.join(root,'obra-ficha.js')});
  const res=await p.evaluate(F=>{window.PogFichas=F;const g=document.getElementById('g');const bad=[];for(const n of Object.keys(F)){const f=F[n];let s='';try{s=PogFicha.svg({n:+n},'cover')}catch(x){s='';bad.push(n+': '+x.message)}
    if(!s)bad.push(n+': sem SVG');const d=document.createElement('div');d.className='c';d.innerHTML=s+'<b>'+n+' · '+(f.t||f.title||'')+'</b>';g.appendChild(d)}return bad},F);
  await p.waitForTimeout(300); await p.screenshot({path:out,fullPage:true}); await b.close();
  console.log(res.length?('PROBLEMAS:\n'+res.join('\n')):'ok: '+Object.keys(F).length+' capas -> '+out);
})();
