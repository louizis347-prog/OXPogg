// Exporta o vocabulário aceito pelas fichas (peças da biblioteca) para tools/ficha/vocab.json. Uso: node tools/ficha/export_vocab.js
const fs=require('fs'),path=require('path');
global.window={};
require('../../js/obra-ficha-lib.js');require('../../js/obra-ficha.js');
const L=window.PogFichaLib,F=window.PogFicha;
const v=Object.assign({},L.VOCAB,{scene:F.VOCAB.scene,tod:F.VOCAB.tod,decor:F.VOCAB.decor,propAt:F.VOCAB.propAt});
fs.writeFileSync(path.join(__dirname,'vocab.json'),JSON.stringify(v,null,1));
console.log(Object.entries(v).map(([k,a])=>k+':'+a.length).join(' '));
