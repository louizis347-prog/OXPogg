const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage({viewport:{width:420,height:900}});
 const errs=[];p.on('pageerror',e=>errs.push('PAGEERR '+e.message+' '+(e.stack||'').split('\n').slice(0,2).join('|')));
 await p.goto('http://localhost:8765/index.html');await p.waitForTimeout(2000);
 await p.evaluate(c=>{const d=document.createElement('button');d.dataset.course=c;document.body.appendChild(d);d.click();},'nb-c1');
 await p.waitForTimeout(2500);
 await p.evaluate(()=>document.querySelector('.test-node').click());await p.waitForTimeout(1500);
 for(let k=0;k<14;k++){
   const info=await p.evaluate(()=>{const s=document.querySelector('#pstage');return s?s.innerText.slice(0,110).replace(/\n/g,' | '):'NOPLAYER'});
   console.log(k,info);
   if(info==='NOPLAYER')break;
   // answer: click first opt or fill input
   await p.evaluate(()=>{const o=document.querySelector('#pstage .opt');if(o)o.click();const i=document.querySelector('#pstage input[type=text],#pstage textarea');if(i){i.value='x';i.dispatchEvent(new Event('input',{bubbles:true}));}});
   await p.waitForTimeout(400);
   await p.evaluate(()=>{const c=document.querySelector('#pcta');if(c&&!c.disabled)c.click();});await p.waitForTimeout(400);
   await p.evaluate(()=>{const c=document.querySelector('#pcta');if(c&&!c.disabled)c.click();});await p.waitForTimeout(500);
 }
 await p.screenshot({path:'t8.png'});
 console.log([...new Set(errs)].join('\n'));
 await b.close();
})();
