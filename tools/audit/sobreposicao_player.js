// Acha ícones/emojis/SVG que ficam em cima de texto no player (quadro a quadro). Uso: node tools/audit/sobreposicao_player.js WxH idx curso [maxFrames]
const {chromium}=require(process.env.PLAYWRIGHT||'/opt/node22/lib/node_modules/playwright');
const [,,vp,idx,cid,mx]=process.argv;const [W,H]=vp.split('x').map(Number);
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:W,height:H}});
await p.goto('http://localhost:8123/app.html');await p.evaluate(()=>{try{sessionStorage.setItem('pogglot:intro','1')}catch(e){}});await p.reload();await p.waitForTimeout(2000);
try{await p.click('text=Agora não',{timeout:1500})}catch(e){}
await p.evaluate(async([c,ix])=>{await ensureLangLoaded(c);if(window.PogBilling)PogBilling.allow=()=>true;play(c,ix)},[cid,+idx]);
await p.addStyleTag({content:'*,*::before,*::after{animation:none!important;transition:none!important}'});await p.waitForTimeout(1600);
const all=[];
for(let i=0;i<(+mx||30);i++){
  const r=await p.evaluate(()=>{
    const out=[],k=P.steps[P.i],st=document.getElementById('pstage');if(!st)return {k,out};
    const EM=/[\u{1F300}-\u{1FAFF}☀-➿⭐✅❌]/u;
    const vis=el=>{const c=getComputedStyle(el);return c.visibility!=='hidden'&&c.display!=='none'&&+c.opacity>0};
    const rect=el=>el.getBoundingClientRect();
    const inView=r=>r.width>2&&r.height>2&&r.bottom>0&&r.top<innerHeight;
    const icons=[];
    st.querySelectorAll('svg').forEach(s=>{if(s.closest('.ps-stage,.ps-hot,.ps-hb,.az-scene,.ps-sticker,.fg-reveal,.fg,.obra-art,.ps-c,.ps-chars,.ps-face,[class*=scene],[class*=cover]'))return;if(vis(s))icons.push({el:s,r:rect(s),t:'svg'})});
    const w=document.createTreeWalker(st,NodeFilter.SHOW_TEXT);const texts=[];
    while(w.nextNode()){const n=w.currentNode,s=n.nodeValue;if(!s.trim())continue;const el=n.parentElement;if(!el||el.closest('svg,script,style,.ps-stage'))continue;if(!vis(el))continue;
      const rg=document.createRange();rg.selectNodeContents(n);
      if(EM.test(s)&&!/[A-Za-zÀ-ÿ0-9]/.test(s)){if(!el.closest('.ps-hot,.ps-hb,.ps-hot-bank,.pr-star,.ps-ico.big,.ps-fig'))icons.push({el,r:rect(el),t:'emoji'});continue}
      for(const rc of rg.getClientRects())texts.push({el,r:rc,s:s.trim().slice(0,30)})}
    for(const ic of icons){if(!inView(ic.r))continue;
      for(const tx of texts){if(ic.el===tx.el||ic.el.contains(tx.el)||tx.el.contains(ic.el))continue;
        const a=ic.r,b=tx.r;const ix=Math.max(0,Math.min(a.right,b.right)-Math.max(a.left,b.left)),iy=Math.max(0,Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top));
        const area=ix*iy;if(area>0.25*Math.min(a.width*a.height,b.width*b.height)&&area>30)
          out.push({ic:ic.t+':'+String(ic.el.className&&ic.el.className.baseVal===undefined?ic.el.className:ic.el.tagName).slice(0,30),tx:tx.s,txc:String(tx.el.className&&tx.el.className.baseVal===undefined?tx.el.className:'').slice(0,30),w:Math.round(ix)+'x'+Math.round(iy)})}}
    return {k,out}});
  for(const o of r.out)all.push({frame:i,k:r.k,...o});
  if(r.k==='done')break;
  await p.evaluate(()=>{document.querySelectorAll('.ps-q').forEach(q=>{const o=q.querySelectorAll('.ps-o:not([disabled])');if(o.length)o[0].click()})});await p.waitForTimeout(150);
  await p.evaluate(()=>{const b=document.getElementById('pcta');if(b&&!b.disabled)b.click();else document.getElementById('pskip')&&document.getElementById('pskip').click()});await p.waitForTimeout(600);
}
const g={};for(const o of all){const key=o.ic+' x '+o.txc;(g[key]=g[key]||[]).push(o)}
console.log(`${cid} #${idx} ${vp}: ${all.length} sobreposições em ${Object.keys(g).length} grupos`);
for(const [k,v] of Object.entries(g).sort((a,b)=>b[1].length-a[1].length).slice(0,10))console.log(' ',String(v.length).padStart(3),k,'| texto:',JSON.stringify(v[0].tx),'| área',v[0].w,'| frame',v[0].k);
await b.close()})();
