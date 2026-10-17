const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage({viewport:{width:420,height:900}});
 const errs=[];p.on('pageerror',e=>errs.push('PAGEERR '+e.message+' '+(e.stack||'').split('\n').slice(0,3).join('|')));
 p.on('console',m=>{if(m.type()==='error')errs.push('CONSOLE '+m.text())});
 await p.goto('http://localhost:8765/index.html');await p.waitForTimeout(2000);
 await p.evaluate(c=>{const d=document.createElement('button');d.dataset.course=c;document.body.appendChild(d);d.click();},'nb-c1');
 await p.waitForTimeout(2500);
 await p.evaluate(()=>document.querySelector('.node[data-ep]').click());await p.waitForTimeout(2000);
 console.log(await p.evaluate(()=>JSON.stringify({i:P.i,steps:P.steps,keys:Object.keys(P)})).then(s=>s.slice(0,300)));
 for(const i of [1,4,5]){
  await p.evaluate(i=>{P.i=i;render();},i);await p.waitForTimeout(800);
  for(let k=0;k<14;k++){await p.evaluate(()=>{const c=document.querySelector('#pcta');if(c&&!c.disabled)c.click();});await p.waitForTimeout(350);
    const sh=await p.evaluate(()=>[...document.querySelectorAll('#nbsp button, #nbshow')].map(x=>x.id).join(','));if(sh){await p.evaluate(()=>{const s=document.querySelector('#nbshow');if(s)s.click();});await p.waitForTimeout(300);}}
  console.log(i,await p.evaluate(()=>document.querySelector('#pstage').innerText.slice(0,80).replace(/\n/g,' | ')),await p.evaluate(()=>document.querySelectorAll('.nb-row').length),'rows');
  await p.screenshot({path:`c${i}.png`});
 }
 console.log([...new Set(errs)].join('\n'));
 await b.close();
})();
