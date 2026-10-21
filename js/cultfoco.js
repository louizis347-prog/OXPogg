/* Pogglot · quadro "Cultura em foco" (cultfoco).
   Inserido em tempo de execução nos ~20% finais dos cursos regulares (en-a1..c2, es-a1..c2, it, fr, de, pt),
   sem editar os JSON. Kill-switch: window.POG_CULTFOCO=false. Dados: js/cultfoco-data.js. */
(function(){
'use strict';
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined'||typeof EP==='undefined')return;
FX_KIND.cultfoco='story';FX_LABEL.cultfoco='Cultura em foco';

var TAIL=0.2;                     /* fração final do curso que recebe o quadro */
var NGAP=3;                       /* rodadas de "palavra certa" */
var CC=function(cid){
  if(/^en-[abc][12]$/.test(cid))return 'us';
  if(/^es-[abc][12]$/.test(cid))return 'es';
  return {it:'it',fr:'fr',de:'de',pt:'br'}[cid]||null;
};
var COUNTS=null;
try{fetch('data/counts.json').then(function(r){return r.json()}).then(function(j){COUNTS=j}).catch(function(){})}catch(e){}

var H=function(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})};
var plain=function(s){return String(s).replace(/\[\[|\]\]/g,'')};
var hash=function(s){var h=7;for(var i=0;i<s.length;i++)h=(h*31+s.charCodeAt(i))>>>0;return h};
var say2=function(t,slow){try{fxSay(String(t),null,slow)}catch(e){}};
var sfx2=function(n){try{sfx(n)}catch(e){}};

/* ---------------- UI (PT / ES) ---------------- */
var UI={
 pt:{kicker:'Cultura em foco',tap:'Toque nas palavras marcadas para ver o significado.',listen:'Ouvir o texto',gist:'Em uma frase',
     opinion:'Sua opinião',noWrong:'Aqui não há resposta certa: sua opinião conta!',thanks:'Obrigado por compartilhar!',
     fill:'Escolha a palavra certa',gapOf:'Palavra',pickOpinion:'Escolha uma opção',read:'Ler o texto',toOp:'Dar minha opinião',toGap:'Completar o texto',
     next:'Próxima',result:'Ver resultado',done:'Você completou o texto!',cont:'Continuar',doneT:'Cultura em foco concluída',
     fromEp:'Do episódio',hint:'Ouça a frase e pense no sentido do texto.',quote:'Frase conhecida',review:'Texto completo'},
 es:{kicker:'Cultura en foco',tap:'Toca las palabras marcadas para ver su significado.',listen:'Escuchar el texto',gist:'En una frase',
     opinion:'Tu opinión',noWrong:'Aquí no hay respuesta correcta: ¡tu opinión cuenta!',thanks:'¡Gracias por compartir!',
     fill:'Elige la palabra correcta',gapOf:'Palabra',pickOpinion:'Elige una opción',read:'Leer el texto',toOp:'Dar mi opinión',toGap:'Completar el texto',
     next:'Siguiente',result:'Ver resultado',done:'¡Completaste el texto!',cont:'Continuar',doneT:'Cultura en foco completada',
     fromEp:'Del episodio',hint:'Escucha la frase y piensa en el sentido del texto.',quote:'Frase conocida',review:'Texto completo'}};
var lang=function(){
  try{if(P&&P.c&&P.c.ui==='es')return 'es';if(typeof ST!=='undefined'&&ST.homeLang==='es')return 'es'}catch(e){}
  return 'pt';
};

/* ---------------- ilustração ---------------- */
function artFallback(tp){
  var c=tp.c||['#6fa8dc','#274a8c'],em=Array.from(tp.em||'🌍');
  var uid='cfg'+hash(tp.id)%9999;
  return '<svg class="cf-svg" viewBox="0 0 200 100" preserveAspectRatio="xMidYMid slice" role="img" aria-hidden="true"><defs><linearGradient id="'+uid+'" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="'+c[0]+'"/><stop offset="1" stop-color="'+c[1]+'"/></linearGradient></defs>'
   +'<rect width="200" height="100" fill="url(#'+uid+')"/><circle cx="160" cy="26" r="13" fill="#fff" opacity=".35"/>'
   +'<path d="M0 78 Q40 52 80 70 T160 66 T200 74 V100 H0Z" fill="#000" opacity=".18"/><path d="M0 88 Q50 68 100 84 T200 82 V100 H0Z" fill="#000" opacity=".22"/>'
   +'<text x="'+(em.length>1?64:100)+'" y="64" font-size="46" text-anchor="middle">'+H(em[0])+'</text>'
   +(em.length>1?'<text x="136" y="70" font-size="36" text-anchor="middle">'+H(em[1])+'</text>':'')+'</svg>';
}
function art(tp){
  try{
    var I=window.PogIllus;
    if(I){
      var r=null;
      if(typeof I.auto==='function')r=I.auto([tp.id,tp.t,tp.em].filter(Boolean),{mood:'day'});
      if(typeof r==='string'&&r.indexOf('<')>=0)return r;
    }
  }catch(e){}
  return artFallback(tp);
}

/* ---------------- escolha do tópico ---------------- */
function epBlob(e){
  var s='';
  try{s+=' '+(e.t||'')+' '+JSON.stringify(e.a||'')+' '+JSON.stringify(e.h||'');
    (e.fr||[]).forEach(function(f){if(/^cult/.test(f.k)||f.k==='cover')s+=' '+JSON.stringify(f).replace(/"pa":\{[^}]*\}/g,'')});}catch(x){}
  return s.toLowerCase();
}
function buildFrame(cid,idx,e){
  var C=window.POG_CULTFOCO_DATA&&window.POG_CULTFOCO_DATA.countries[CC(cid)];
  if(!C)return null;
  var blob=epBlob(e),n=C.topics.length,pool=[];
  C.topics.forEach(function(tp,i){
    var dup=(tp.k||[]).some(function(k){return blob.indexOf(k)>=0});
    if(!dup)pool.push(i);
  });
  if(!pool.length)pool=C.topics.map(function(_,i){return i});
  var h=hash(cid);
  var ti=pool[(idx*5+h)%pool.length];
  var tp=C.topics[ti];
  /* palavras do exercício: terms entre [[ ]] com distratores, em frases diferentes */
  var sents=tp.t.split(/(?<=[.!?»”])\s+/),cand=[];
  var terms=[];(tp.t.match(/\[\[(.+?)\]\]/g)||[]).forEach(function(m){terms.push(m.slice(2,-2))});
  terms.forEach(function(w){if(tp.w[w]&&tp.w[w].length>=4){
    var si=-1;sents.forEach(function(s,k){if(s.indexOf('[['+w+']]')>=0)si=k});
    cand.push({w:w,s:si});}});
  var start=(Math.floor(idx/Math.max(1,pool.length))+h)%Math.max(1,cand.length),pick=[],used={};
  for(var k=0;k<cand.length&&pick.length<NGAP;k++){
    var c=cand[(start+k)%cand.length];
    if(used[c.s])continue;used[c.s]=1;pick.push(c.w);
  }
  for(var k2=0;k2<cand.length&&pick.length<NGAP;k2++){var c2=cand[(start+k2)%cand.length];if(pick.indexOf(c2.w)<0)pick.push(c2.w)}
  if(!pick.length)return null;
  return {k:'cultfoco',cc:CC(cid),ti:ti,qi:(idx+h)%C.quotes.length,ask:(idx+h)%3,gap:pick,rounds:pick.slice(),
          work:e.a&&e.a.w?String(e.a.w):''};
}

/* ---------------- renderização ---------------- */
function termHtml(tp,L){
  /* separa em segmentos: [[termo]] vira botão; chaves extras de tp.w (fora de colchetes) também */
  var raw=tp.t,out='',rx=/\[\[(.+?)\]\]/g,last=0,m,plainParts=[];
  var extras=Object.keys(tp.w).filter(function(k){return raw.indexOf('[['+k+']]')<0&&raw.split(k).length===2});
  var link=function(txt){
    var s=H(txt);
    extras.forEach(function(k){var hk=H(k);s=s.replace(hk,'<button type="button" class="cf-t" data-k="'+hk+'">'+hk+'</button>')});
    return s;
  };
  while((m=rx.exec(raw))){
    out+=link(raw.slice(last,m.index))+'<button type="button" class="cf-t" data-k="'+H(m[1])+'">'+H(m[1])+'</button>';
    last=m.index+m[0].length;
  }
  return out+link(raw.slice(last));
}
function hl(parts){return H(parts[0])+'<span class="cf-mark">'+H(parts[1])+'</span>'+H(parts[2])}

FXR.cultfoco=function(f,st,n){
  var data=window.POG_CULTFOCO_DATA,C=data&&data.countries[f.cc],tp=C&&C.topics[f.ti];
  if(!tp){st.innerHTML='<div class="step"><p>Quadro indisponível.</p></div>';cta(P.t.cont,true);return}
  var L=lang(),T=UI[L],plainText=plain(tp.t);
  var phase=0,hits=0,ri=0;
  P.fx.done=false;P.fx.cta=null;
  var quote=C.quotes[f.qi%C.quotes.length];
  var ask=(function(){
    if(f.ask===0)return tp.a[L];
    var g=data.generic[L][f.ask-1],name=tp.h[L][1];
    return [g[0].replace('{t}',name)].concat(g.slice(1));
  })();
  var kbar=function(){return (P.e&&Array.isArray(P.e.fr))?fxKindBar(f,n):''};
  var chips=function(){
    return '<div class="cf-chips"><span>'+H(C.flag)+' '+H(C.name[L])+'</span>'+(f.work?'<span>🎬 '+H(T.fromEp)+': '+H(f.work)+'</span>':'')+'</div>';
  };
  var frame=function(inner,cls){
    st.innerHTML='<div class="step fx cf cf-p'+phase+(cls?' '+cls:'')+((P.e&&Array.isArray(P.e.fr))?'':' cf-lg')+'">'+kbar()+inner+'</div>';
  };
  /* ---------- fase 0: ler ---------- */
  var drawRead=function(){
    phase=0;
    frame('<div class="cf-grid"><div class="cf-side"><div class="cf-art">'+art(tp)+'</div><h2 class="cf-h"><small>'+H(T.kicker)+'</small>'+hl(tp.h[L])+'</h2>'+chips()+'</div>'
      +'<div class="cf-main"><div class="cf-text" id="cft"><p>'+termHtml(tp,L)+'</p><div class="cf-pop" id="cfp" hidden></div></div>'
      +'<div class="cf-bar"><button type="button" class="cf-listen" id="cfl">🔊 '+H(T.listen)+'</button><span class="cf-tap">'+H(T.tap)+'</span></div>'
      +'<div class="cf-gist"><b>'+H(T.gist)+'</b> '+H(tp.g[L])+'</div></div></div>');
    wirePop();
    var lb=st.querySelector('#cfl');if(lb)lb.onclick=function(){sfx2('pop');say2(plainText,false)};
    P.fx.cta=function(){drawAsk();return true};
    cta(T.toOp+' ▶',true,true);
    say(L==='es'?'Lee el texto y toca las palabras marcadas.':'Leia o texto e toque nas palavras marcadas.');
  };
  var wirePop=function(){
    var box=st.querySelector('#cft'),pop=st.querySelector('#cfp');if(!box||!pop)return;
    var close=function(){pop.hidden=true;box.querySelectorAll('.cf-t.on').forEach(function(x){x.classList.remove('on')})};
    box.querySelectorAll('.cf-t').forEach(function(b){b.onclick=function(ev){
      ev.stopPropagation();var k=b.getAttribute('data-k'),
        key=Object.keys(tp.w).filter(function(x){return H(x)===k})[0],w=key&&tp.w[key];if(!w)return;
      var same=b.classList.contains('on');close();if(same)return;
      b.classList.add('on');sfx2('pop');say2(key,false);
      pop.innerHTML='<b>'+H(key)+'</b><span>'+H(w[L==='es'?1:0])+'</span>';pop.hidden=false;
      var br=b.getBoundingClientRect(),cr=box.getBoundingClientRect(),pw=pop.offsetWidth,ph=pop.offsetHeight;
      var left=Math.max(4,Math.min(cr.width-pw-4,br.left-cr.left+br.width/2-pw/2));
      var top=br.top-cr.top-ph-6;if(top<2)top=br.bottom-cr.top+6;
      pop.style.left=left+'px';pop.style.top=top+'px';}});
    box.onclick=close;
  };
  /* ---------- fase 1: citação + opinião ---------- */
  var drawAsk=function(){
    phase=1;var qs=ask.slice(1);
    frame('<div class="cf-grid cf-grid2"><div class="cf-side"><div class="cf-quote"><small>'+H(T.quote)+'</small><q lang="'+H(C.lang)+'">'+H(quote[0])+'</q><cite>'+H(quote[1])+'</cite>'
      +(quote[L==='es'?3:2]?'<span class="cf-qtr">'+H(quote[L==='es'?3:2])+'</span>':'')+'<button type="button" class="cf-qs" id="cfq" aria-label="'+H(T.listen)+'">🔊</button></div></div>'
      +'<div class="cf-main"><div class="cf-ask"><small>'+H(T.opinion)+'</small><h3>'+H(ask[0])+'</h3><div class="cf-opts">'+qs.map(function(o,i){return '<button type="button" class="cf-o" data-i="'+i+'">'+H(o)+'</button>'}).join('')+'</div>'
      +'<div class="cf-note" id="cfn">'+H(T.noWrong)+'</div></div></div></div>');
    var q=st.querySelector('#cfq');if(q)q.onclick=function(){sfx2('pop');say2(quote[0],false)};
    var picked=false;
    st.querySelectorAll('.cf-o').forEach(function(b){b.onclick=function(){
      st.querySelectorAll('.cf-o').forEach(function(x){x.classList.remove('sel')});b.classList.add('sel');sfx2('pop');
      if(!picked){picked=true;st.querySelector('#cfn').textContent=T.thanks+' '+T.noWrong;
        P.fx.cta=function(){drawGap();return true};cta(T.toGap+' ▶',true,true);say(T.thanks)}}});
    P.fx.cta=null;cta(T.pickOpinion,false);
    /* quem não quer opinar pode seguir pelo botão de pular do player */
    P.fx.cta=function(){if(!picked)return true;drawGap();return true};
    say(L==='es'?'¿Y tú, qué piensas?':'E você, o que acha?');
  };
  /* ---------- fase 2: palavra certa ---------- */
  var sents=tp.t.split(/(?<=[.!?»”])\s+/);
  var drawGap=function(){
    phase=2;
    if(ri>=f.gap.length)return finish();
    var w=f.gap[ri],ent=tp.w[w],tries=0,done=false;
    var sent=sents.filter(function(s){return s.indexOf('[['+w+']]')>=0})[0]||'';
    var shown=H(plain(sent.replace('[['+w+']]','@@')).trim()).replace('@@','<span class="cf-g" id="cfg">＿＿＿</span>');
    var opts=fxShuffle([w,ent[2],ent[3]]);
    frame('<div class="cf-grid cf-grid2"><div class="cf-side"><h2 class="cf-h cf-h2"><small>'+H(T.kicker)+'</small>'+H(T.fill)+' <em>'+(ri+1)+'/'+f.gap.length+'</em></h2><div class="vw-bar"><i style="width:'+(ri/f.gap.length*100)+'%"></i></div><div class="cf-art cf-art2">'+art(tp)+'</div></div>'
      +'<div class="cf-main"><div class="cf-sent" lang="'+H(C.lang)+'">“'+shown+'”</div>'
      +'<div class="cf-wopts">'+opts.map(function(o){return '<button type="button" class="cf-w">'+H(o)+'</button>'}).join('')+'</div><div class="cf-hint" id="cfh"></div><div id="fb"></div></div></div>');
    cta(T.fill,false);
    var nxt=function(ok){if(ok)hits++;var last=ri>=f.gap.length-1;P.fx.cta=function(){ri++;drawGap();return true};cta((last?T.result:T.next)+' ▶',true,true)};
    st.querySelectorAll('.cf-w').forEach(function(b){b.onclick=function(){
      if(done)return;
      if(b.textContent===w){
        done=true;var g=st.querySelector('#cfg');g.textContent=w;g.classList.add('ok');
        st.querySelectorAll('.cf-w').forEach(function(x){x.disabled=true});b.classList.add('ok');
        P.streak=tries?0:(P.streak||0)+1;fxGrade(true,'',w);say2(plain(sent),false);nxt(!tries);
      }else{
        tries++;b.classList.add('no');b.disabled=true;P.streak=0;sfx2('oops');
        st.querySelector('#cfh').textContent='💡 '+T.hint;
        if(tries>=2){ /* revela a resposta após duas tentativas erradas */
          done=true;var g2=st.querySelector('#cfg');g2.textContent=w;g2.classList.add('ok');
          st.querySelectorAll('.cf-w').forEach(function(x){x.disabled=true;if(x.textContent===w)x.classList.add('ok')});
          fxGrade(false,'',w);nxt(false);
        }
      }}});
    say(L==='es'?'Elige la palabra que completa la frase.':'Escolha a palavra que completa a frase.');
  };
  var finish=function(){
    P.score+=hits;P.fx.done=true;
    var sc=f.gap.length?hits/f.gap.length:1,stars=sc>=.8?3:sc>=.5?2:1;
    frame('<div class="cf-grid cf-grid2"><div class="cf-side"><div class="cf-art">'+art(tp)+'</div><div class="rp-res">'+'★'.repeat(stars)+'☆'.repeat(3-stars)+'</div></div>'
      +'<div class="cf-main"><div class="cf-done"><b>'+H(T.done)+'</b><span>'+H(tp.g[L])+'</span><small>'+H(C.flag)+' '+H(C.name[L])+' · '+H(plain(tp.h[L].join('')))+'</small></div></div></div>');
    sfx2('tada');try{confetti(40)}catch(e){}
    P.fx.cta=null;cta(T.cont,true,true);say(T.doneT+'!');
  };
  drawRead();
};

/* ---------------- montagem segura no play() ---------------- */
function enabled(){return window.POG_CULTFOCO!==false}
function inTail(cid,idx){
  var arr=EP[cid];if(!arr||!arr.length)return false;
  var len=arr.length;
  if(COUNTS&&COUNTS[cid]&&COUNTS[cid]>len)len=COUNTS[cid];   /* contagem do manifesto, se o array ainda estiver parcial */
  return idx>=Math.floor(len*(1-TAIL));
}
function inject(cid,idx){
  try{
    if(!enabled()||!CC(cid))return false;
    var e=EP[cid]&&EP[cid][idx];
    if(!e||e.__cfDone)return !!(e&&e.__cfDone===2);
    if(!inTail(cid,idx)){return false}
    /* episódios sem e.fr (formato antigo, ex.: es-b2..c2): o quadro entra como passo extra em P.steps */
    if(!Array.isArray(e.fr)||!e.fr.length){
      e.__cfDone=2;var fr0=buildFrame(cid,idx,e);if(!fr0){e.__cfDone=true;return false}
      e.__cfFrame=fr0;return true;
    }
    e.__cfDone=true;
    if(e.fr.some(function(f){return f&&f.k==='cultfoco'}))return false;
    /* o padrão regular do repositório (obra principal + cena da obra) já cobre a cultura: não repete */
    if(e.fr.some(function(f){return f&&f.k==='cultob'})&&e.fr.some(function(f){return f&&f.k==='cultcena'}))return false;
    var fr=buildFrame(cid,idx,e);if(!fr)return false;
    /* posição: logo depois do bloco cultural inicial (cover + cult*), senão após a capa */
    var pos=1,lead=0;
    for(var i=0;i<Math.min(e.fr.length,4);i++){var k=e.fr[i]&&e.fr[i].k;if(k==='cover'||/^cult/.test(k||'')||k==='bridge'||k==='cwords'||k==='hook')lead=i+1;else break}
    pos=Math.max(1,lead);
    /* em episódios curtos de cult1/cwords/cquiz, vai depois do quiz */
    if(e.fr[0]&&e.fr[0].k==='cult1'){pos=e.fr.length>=3&&e.fr[2].k==='cquiz'?3:Math.min(e.fr.length,lead||1)}
    e.fr.splice(Math.min(pos,e.fr.length),0,fr);
    return true;
  }catch(x){try{console.warn('cultfoco',x)}catch(_){}return false}
}
/* passo extra para episódios sem e.fr */
function legacyStep(cid,idx){
  try{
    var e=EP[cid]&&EP[cid][idx];
    if(!e||!e.__cfFrame||typeof P==='undefined'||!P||P.e!==e||!Array.isArray(P.steps)||P.steps.indexOf('cultfoco')>=0)return;
    var at=P.steps.indexOf('scene');at=at>=0?at+1:Math.min(1,P.steps.length-1);
    P.steps.splice(at,0,'cultfoco');P.cfFrame=e.__cfFrame;P.total=(P.total||0)+e.__cfFrame.rounds.length;
  }catch(x){try{console.warn('cultfoco legacy',x)}catch(_){}}
}
function renderLegacy(){
  var st=document.getElementById('pstage');if(!st||!P||!P.cfFrame)return false;
  P.answered=false;P.sel=null;
  try{setProg()}catch(e){}
  try{var pb=document.getElementById('pback');if(pb)pb.disabled=P.i<=0;var sk=document.getElementById('pskip');if(sk)sk.disabled=false;
    var bd=document.getElementById('pbody');if(bd)bd.scrollTop=0;st.dataset.kind='story';
    st.style.setProperty('--kind-c','var(--river)');st.style.setProperty('--kind-l','var(--river-l)')}catch(e){}
  P.fx={n:0,cta:null};try{clearTimeout(fxSeq.t)}catch(e){}
  FXR.cultfoco(P.cfFrame,st,0);
  return true;
}
var _tot=window.fxTotal;
if(typeof _tot==='function'&&!_tot.__cf){
  window.fxTotal=function(e){
    var n=_tot.apply(this,arguments);
    try{(e&&e.fr||[]).forEach(function(f){if(f&&f.k==='cultfoco')n+=(f.rounds||[]).length})}catch(x){}
    return n;
  };
  window.fxTotal.__cf=1;
}
var _play=window.play;
if(typeof _play==='function'&&!_play.__cf){
  window.play=function(cid,idx){
    var ok=inject(cid,idx);
    var r=_play.apply(this,arguments);
    if(ok)legacyStep(cid,idx);
    return r;
  };
  window.play.__cf=1;
}
var _render=window.render;
if(typeof _render==='function'&&!_render.__cf){
  window.render=function(){
    try{if(typeof P!=='undefined'&&P&&!P.isTest&&P.steps&&P.steps[P.i]==='cultfoco'&&P.cfFrame){if(renderLegacy())return}}catch(x){try{console.warn('cultfoco render',x)}catch(_){}}
    return _render.apply(this,arguments);
  };
  window.render.__cf=1;
}
var _cc=window.ctaClick;
if(typeof _cc==='function'&&!_cc.__cf){
  window.ctaClick=function(){
    try{if(typeof P!=='undefined'&&P&&!P.isTest&&P.steps&&P.steps[P.i]==='cultfoco'&&P.cfFrame){
      var fx=P.fx;if(fx&&fx.cta){var r=fx.cta();if(r)return}
      var cur=document.querySelector('#pstage .step'),adv=function(){try{chime('step')}catch(e){}P.i++;render()};
      if(cur){cur.classList.add('out');setTimeout(adv,260)}else adv();return}}catch(x){try{console.warn('cultfoco cta',x)}catch(_){}}
    return _cc.apply(this,arguments);
  };
  window.ctaClick.__cf=1;
}
window.POG_CULTFOCO_API={inject:inject,inTail:inTail,build:buildFrame,country:CC};
})();
