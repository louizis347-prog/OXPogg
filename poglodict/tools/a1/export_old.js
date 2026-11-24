// lê os arquivos ORIGINAIS (tools/a1/orig) e grava old.json: plan, content, pron, themes, blockphotos, extras
const fs=require('fs'),path=require('path');const D=path.join(__dirname,'orig');
const src=n=>fs.readFileSync(path.join(D,n),'utf8');
let plan=src('english-a1-plan.js');
const m=plan.match(/englishA1Plans=`([\s\S]*?)`\.split/)[1].split('\n').map(l=>{const [title,file,grammar,goal,terms]=l.split('|');return {title,file,grammar,goal,words:terms.split(';').map(t=>t.split('='))}});
const bp=plan.match(/englishA1BlockPhotoFiles=`([\s\S]*?)`\.split/)[1].split('\n').map(r=>r.split(' '));
const c=src('english-a1-content.js');
const content=eval(c.match(/const englishA1Content=(\[[\s\S]*?\n\]);/)[1]);
const themes=eval(c.match(/englishA1PhotoThemes=(\[[\s\S]*?\]);/)[1]);
const extras=eval('('+c.match(/englishA1ExtraWordExamples=(\{[\s\S]*?\n\});/)[1]+')');
const pron=eval(src('a1-pronunciation-data.js').replace(/^const a1PronunciationLab=/,'(').replace(/;\s*$/,'')+')');
fs.writeFileSync(path.join(__dirname,'old.json'),JSON.stringify({plan:m,blockPhotos:bp,content,themes,extras,pron},null,0));
console.log(m.length,bp.length,content.length,themes.length,Object.keys(extras).length,pron.length);
