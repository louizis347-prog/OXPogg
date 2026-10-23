/* Pogglot: assinatura. Só ativa quando config.js tem checkoutUrl. */
(function(){
'use strict';
const cfg=()=>window.POGGLOT_CONFIG||{};
const esc=s=>String(s==null?'':s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const on=()=>!!(cfg().checkoutUrl||cfg().checkoutUrlYear);
const free=()=>Number.isFinite(+cfg().freeEpisodes)&&cfg().freeEpisodes!==''&&cfg().freeEpisodes!=null?+cfg().freeEpisodes:5;
let plan={premium:false},uid=null;
function cl(){return window.PogCloud}
async function refresh(){
  const C=window.PogComm,u=C&&C.user&&C.user();
  if(!u||!cl()||cl().mode!=='supabase'){plan={premium:false};uid=null;return plan}
  if(uid===u.id&&plan.at&&Date.now()-plan.at<300000)return plan;
  try{const r=await cl().rest('POST','/rest/v1/rpc/my_plan',{body:{}});plan={...r,at:Date.now()};uid=u.id;try{localStorage.setItem('pogglot:plan',JSON.stringify({uid:u.id,p:r.premium,until:r.until}))}catch(_){}}catch(e){}
  return plan;
}
function cached(){ // resposta imediata; a verificação real roda em segundo plano
  if(plan.premium)return true;
  try{const c=JSON.parse(localStorage.getItem('pogglot:plan')||'null');const u=window.PogComm&&PogComm.user&&PogComm.user();
    if(c&&u&&c.uid===u.id&&c.p&&(!c.until||new Date(c.until)>new Date()))return true}catch(_){}
  return false;
}
/* Liberação temporária para testes: todos os episódios abertos. Volte para false para reativar o limite gratuito. */
const OPEN_ALL=true;
function allow(cid,idx){
  if(OPEN_ALL||!on()||idx<free()||cached())return true;
  refresh().then(p=>{if(p.premium&&document.getElementById('pg-pay'))document.getElementById('pg-pay').remove()});
  paywall();return false;
}
function paywall(){
  if(document.getElementById('pg-pay'))return;
  const c=cfg(),u=window.PogComm&&PogComm.user&&PogComm.user();
  const m=c.checkoutUrl,y=c.checkoutUrlYear;
  const d=document.createElement('div');d.id='pg-pay';d.className='pg-pay';
  d.innerHTML=`<div class="pg-pay-b" role="dialog" aria-modal="true"><h3>⭐ Pogglot Premium</h3>
   <p>Os primeiros ${free()} episódios de cada curso são grátis. Assine para liberar todos os cursos, revisões e a comunidade completa.</p>
   <div class="pg-pay-pl">${m?`<a class="pg-btn" href="${esc(m)}" target="_blank" rel="noopener">Mensal</a>`:''}${y?`<a class="pg-btn" href="${esc(y)}" target="_blank" rel="noopener">Anual · economize</a>`:''}</div>
   <p class="pg-pay-s">${u?`Use o mesmo e-mail da sua conta (<b>${esc(u.email||'')}</b>) na compra. O acesso é liberado automaticamente.`:'Crie sua conta na aba Comunidade e use o <b>mesmo e-mail</b> na compra, é assim que o acesso é liberado.'}</p>
   <div class="pg-pay-pl"><button class="pg-btn ghost" id="pg-pay-re">Já assinei, verificar</button><button class="pg-btn ghost" id="pg-pay-x">Fechar</button></div><p class="pg-pay-s" id="pg-pay-m"></p></div>`;
  document.body.appendChild(d);
  d.querySelector('#pg-pay-x').onclick=()=>d.remove();
  d.querySelector('#pg-pay-re').onclick=async()=>{plan.at=0;const p=await refresh();if(p.premium){d.remove();alert('Premium ativo! 🎉')}else d.querySelector('#pg-pay-m').textContent=u?'Ainda não encontramos o pagamento. Pode levar alguns minutos.':'Entre na sua conta primeiro (aba Comunidade).'};
}
/* painel do admin: liberar/retirar acesso */
async function adminPanel(box){
  const R=(f,b)=>cl().rest('POST','/rest/v1/rpc/'+f,{body:b||{}});
  async function draw(){
    let rows=[];try{rows=await R('admin_entitlements')}catch(e){box.innerHTML=`<p class="pg-empty">${esc(e.message)}</p>`;return}
    box.innerHTML=`<section class="pg-card"><h4>Liberar acesso</h4><div class="pg-bill"><input class="pg-in" id="bl-e" type="email" placeholder="email@aluno.com"><select class="pg-in" id="bl-d"><option value="34">Mensal (34 dias)</option><option value="369">Anual (369 dias)</option><option value="7">Teste (7 dias)</option></select><button class="pg-btn" id="bl-g">Liberar</button></div></section>
     <section class="pg-card pg-lst"><h4>Assinantes (${rows.filter(r=>r.active).length} ativos)</h4><ul>${rows.length?rows.map(r=>`<li><span>${esc(r.email)} · ${esc(r.plan)} · ${esc(r.source)}<br><small>${r.expires_at?'até '+new Date(r.expires_at).toLocaleDateString():'sem fim'} ${r.active?'✅':'⛔'}</small></span>${r.active?`<button class="pg-btn ghost sm" data-rv="${esc(r.email)}">Retirar</button>`:''}</li>`).join(''):'<li>Nenhum ainda</li>'}</ul></section>`;
    box.querySelector('#bl-g').onclick=async()=>{const e=box.querySelector('#bl-e').value.trim().toLowerCase();if(!e)return;try{await R('admin_grant',{p_email:e,p_days:+box.querySelector('#bl-d').value});draw()}catch(x){alert(x.message)}};
    box.onclick=async ev=>{const b=ev.target.closest('[data-rv]');if(!b||!confirm('Retirar acesso?'))return;try{await R('admin_revoke',{p_email:b.dataset.rv});draw()}catch(x){alert(x.message)}};
  }
  draw();
}
function badge(){ // linha de status para o perfil
  if(!on())return '';
  return cached()?'<p class="pg-pay-s">⭐ Premium ativo</p>':'<p class="pg-pay-s">Plano grátis · <a href="#" id="pg-up">assinar Premium</a></p>';
}
document.addEventListener('click',e=>{if(e.target&&e.target.id==='pg-up'){e.preventDefault();paywall()}});
window.PogBilling={allow,refresh,paywall,adminPanel,badge,on};
setTimeout(()=>{if(on())refresh()},1500);
})();
