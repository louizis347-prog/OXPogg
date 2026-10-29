// Auditoria de layout do player, quadro a quadro: (1) palavra partida em duas linhas, (2) elemento estourando a largura da tela,
// (3) texto cortado por overflow:hidden. Uso: node tools/audit/layout_player.js WxH idx curso [maxFrames]
const {chromium}=require(process.env.PLAYWRIGHT||'/opt/node22/lib/node_modules/playwright');
const [,,vp,idx,cid,mx]=process.argv;const [W,H]=vp.split('x').map(Number);
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:W,height:H}});
await p.goto('http://localhost:8123/app.html');await p.evaluate(()=>{try{sessionStorage.setItem('pogglot:intro','1')}catch(e){}});await p.reload();await p.waitForTimeout(2000);
try{await p.click('text=Agora não',{timeout:1500})}catch(e){}
await p.evaluate(async([c,ix])=>{await ensureLangLoaded(c);if(window.PogBilling)PogBilling.allow=()=>true;play(c,ix)},[cid,+idx]);
await p.addStyleTag({content:'*,*::before,*::after{animation:none!important;transition:none!important}'});await p.waitForTimeout(1600);
const probs=[];
for(let i=0;i<(+mx||30);i++){
  const r=await p.evaluate(()=>{
    const out=[],pl=document.getElementById('player'),k=P.steps[P.i];
    const w=document.createTreeWalker(pl,NodeFilter.SHOW_TEXT);
    while(w.nextNode()){const n=w.currentNode,t=n.nodeValue;if(!t.trim())continue;const el=n.parentElement;if(!el||el.closest('svg,script,style,#pbub'))continue;
      const cs=getComputedStyle(el);if(cs.visibility==='hidden'||cs.display==='none')continue;
      const rr=el.getBoundingClientRect();if(rr.bottom<0||rr.top>innerHeight)continue;
      const re=/\S+/g;let m;while((m=re.exec(t))){if(m[0].length<4)continue;
        const r=document.createRange();r.setStart(n,m.index);r.setEnd(n,m.index+m[0].length);const rects=[...r.getClientRects()].filter(x=>x.width>1);
        if(rects.length>1&&Math.abs(rects[0].top-rects[rects.length-1].top)>6)out.push({tipo:'palavra-partida',w:m[0].slice(0,24),cls:String(el.className&&el.className.baseVal===undefined?el.className:'').slice(0,40)});}}
    document.querySelectorAll('#pstage *').forEach(el=>{const r=el.getBoundingClientRect();if(r.width<2)return;const cs=getComputedStyle(el);if(cs.position==='fixed')return;
      if(r.right>innerWidth+2||r.left<-2){if(!el.closest('.ps-stage,.ps-hot,svg,.cb-tabs,[class*=scroll],.ps-qs'))out.push({tipo:'estoura-largura',w:Math.round(r.right-innerWidth)+'px',cls:String(el.className&&el.className.baseVal===undefined?el.className:el.tagName).slice(0,40)})}});
    return {k,out}});
  for(const o of r.out)probs.push({frame:i,k:r.k,...o});
  if(r.k==='done')break;
  await p.evaluate(()=>{document.querySelectorAll('.ps-q').forEach(q=>{const o=q.querySelectorAll('.ps-o:not([disabled])');if(o.length)o[0].click()})});await p.waitForTimeout(150);
  await p.evaluate(()=>{const b=document.getElementById('pcta');if(b&&!b.disabled)b.click();else document.getElementById('pskip')&&document.getElementById('pskip').click()});await p.waitForTimeout(600);
}
const g={};for(const o of probs){const key=o.tipo+'|'+o.cls;(g[key]=g[key]||[]).push(o)}
console.log(`${cid} #${idx} ${vp}: ${probs.length} problemas em ${Object.keys(g).length} grupos`);
for(const [k,v] of Object.entries(g).sort((a,b)=>b[1].length-a[1].length).slice(0,10))console.log(' ',String(v.length).padStart(3),k,'| ex:',v[0].w,'| frame',v[0].k);
await b.close()})();
