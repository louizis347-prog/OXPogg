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
 for(let k=0;k<12;k++){
   const info=await p.evaluate(()=>{const s=document.querySelector('#pstage');return s?s.innerText.slice(0,140).replace(/\n/g,' | '):'NOPLAYER'});
   console.log(k,info, '| CTA:',await p.evaluate(()=>{const c=document.querySelector('#pcta');return c?c.innerText+(c.disabled?' (disabled)':''):''}));
   await p.screenshot({path:`s${k}.png`});
   if(info==='NOPLAYER')break;
   await p.evaluate(()=>{const c=document.querySelector('#pcta');if(c&&!c.disabled)c.click();});await p.waitForTimeout(900);
 }
 console.log([...new Set(errs)].join('\n'));
 await b.close();
})();
