// Confere que cada ficha de js/fichas-<curso>.js renderiza SVG saudável (sem DOM): tamanho, elementos, rostos, sem NaN/undefined.
// Uso: node tools/ficha/check_render.js [curso=en-a1]   (sai com código 1 se algum falhar)
const fs=require('fs'),path=require('path'),vm=require('vm');
const curso=process.argv[2]||'en-a1',root=path.join(__dirname,'..','..','js');
const ctx={window:{}};ctx.window=ctx;vm.createContext(ctx);
for(const f of['obra-ficha-lib.js','obra-ficha.js','fichas-'+curso+'.js'])vm.runInContext(fs.readFileSync(path.join(root,f),'utf8'),ctx,{filename:f});
const F=ctx.PogFichas||{},bad=[];let n=0;
for(const k of Object.keys(F)){n++;
  for(const mode of['cover','sticker','strip','face']){
    let s='';try{s=ctx.PogFicha.svg({n:+k},mode)}catch(e){bad.push(k+' '+mode+': '+e.message);continue}
    if(!s)bad.push(k+' '+mode+': vazio');
    else if(/NaN|undefined|\[object/.test(s))bad.push(k+' '+mode+': NaN/undefined no SVG');
    else if(mode==='cover'){const els=(s.match(/<(path|ellipse|circle|rect|line|polygon|g)\b/g)||[]).length,eyes=(s.match(/fill="#2b1d3a"\/><circle/g)||[]).length;
      if(els<110)bad.push(k+' cover: poucos elementos ('+els+' < 110)');
      if(eyes<1&&!/<ellipse[^>]*fill="#2b1d3a"/.test(s))bad.push(k+' cover: sem rosto visível');}
    else if(mode==='face'&&!/<ellipse[^>]*fill="#2b1d3a"/.test(s))bad.push(k+' face: sem olhos');
  }}
console.log('capas por ficha:',n,'| problemas:',bad.length);bad.slice(0,40).forEach(b=>console.log(' -',b));process.exit(bad.length?1:0);
