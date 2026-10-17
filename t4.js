const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage({viewport:{width:420,height:900}});
 p.on('pageerror',e=>console.log('PAGEERR',e.message));
 await p.goto('http://localhost:8765/index.html');await p.waitForTimeout(2000);
 for(const [cid,tid] of [['nb-a1','mt90003'],['nb-a1','mt90001'],['nb-c1','mt90801'],['nb-c1','mt90811'],['nb-b2','']]){
  await p.evaluate(c=>{const d=document.createElement('button');d.dataset.course=c;document.body.appendChild(d);d.click();},cid);
  await p.waitForTimeout(2500);
  const r=await p.evaluate(({cid,tid})=>{try{
    const tests=arcTests(cid).map(x=>x.id);
    const out=[];for(const t of tests.slice(0,30)){let q=null,err=null;try{q=buildArcTest(cid,t)}catch(e){err=e.message}
      out.push(t+':'+(err?'ERR '+err:(q?q.qs.length:'null')));}
    return out.join(' ');}catch(e){return 'EXC '+e.message}},{cid,tid});
  console.log(cid,r);
 }
 await b.close();
})();
