// Exporta dos arquivos do PoggloDict (A1) título, gramática, palavras, gramática-exercício e mini-quiz de cada lição. Uso: node tools/pd_sel_export.js > saida.json
const fs=require('fs'),vm=require('vm'),path=require('path');const P=path.join(__dirname,'..','poglodict');const ctx={};vm.createContext(ctx);
for(const f of ['english-a1-plan.js','english-a1-content.js','english-a1-extra.js']){vm.runInContext(fs.readFileSync(path.join(P,f),'utf8').replace(/^const /gm,'var ').replace(/^function (\w+)/gm,'var $1=function $1'),ctx)}
const out={};ctx.englishA1Plans.forEach((p,i)=>{if(!p)return;const c=ctx.englishA1Content[i];out[i+1]={t:p.title,g:p.grammar,w:p.words.map(x=>x[0].toLowerCase()),gr:c&&c[3]?c[3]:null,quiz:c&&c[5]?c[5]:null}});
process.stdout.write(JSON.stringify(out));
