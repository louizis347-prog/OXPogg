const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage({viewport:{width:420,height:900}});
 const errs=[];p.on('pageerror',e=>errs.push('PAGEERR '+e.message+' '+(e.stack||'').split('\n').slice(0,3).join('|')));
 p.on('console',m=>{if(m.type()==='error')errs.push('CONSOLE '+m.text())});
 await p.goto('http://localhost:8765/index.html');await p.waitForTimeout(2000);
 for(const cid of ['nb-a1','nb-c1','en-a1','en-c2']){
  await p.evaluate(c=>{const d=document.createElement('button');d.dataset.course=c;document.body.appendChild(d);d.click();},cid);
  await p.waitForTimeout(3000);
  const n=await p.evaluate(()=>document.querySelectorAll('.test-node').length);
  console.log(cid,'test nodes',n,'nodes',await p.evaluate(()=>document.querySelectorAll('.node').length));
  if(n){const t=await p.evaluate(()=>document.querySelector('.test-node').dataset.test);console.log('testid',t);
   await p.evaluate(()=>document.querySelector('.test-node').click());await p.waitForTimeout(3000);
   console.log('after click:',(await p.evaluate(()=>document.body.innerText.slice(0,160))).replace(/\n/g,' | '));
   await p.evaluate(()=>{try{closePlayer()}catch(e){}});await p.waitForTimeout(500);}
 }
 console.log([...new Set(errs)].slice(0,10).join('\n'));
 await b.close();
})();
