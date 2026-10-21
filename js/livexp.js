/* Feedback de jogo ao vivo: XP da sessao, combo e precisao. Observa fxGrade/beep/sfx sem alterar a logica. */
(function(){
  var S={p:null,xp:0,combo:0,ok:0,n:0,last:0,seen:0},H=null,shown=0;
  var RM=function(){try{return matchMedia('(prefers-reduced-motion:reduce)').matches}catch(e){return false}};
  function head(){return document.querySelector('#player .p-head')}
  function mount(){
    var h=head();if(!h)return null;
    if(H&&H.parentNode===h)return H;
    H=document.createElement('div');H.className='lx-hud';H.setAttribute('aria-hidden','true');
    H.innerHTML='<span class="lx-xp">&#9889; <b>0</b> XP</span><span class="lx-combo"><i>&#128293;</i><b>x2</b></span><span class="lx-acc">&#127919; <b>100%</b></span>';
    h.appendChild(H);shown=0;return H;
  }
  function sync(){if(typeof P==='undefined'||!P)return false;if(S.p!==P){S={p:P,xp:0,combo:0,ok:0,n:0,last:0,seen:P.score||0};if(H){H.remove();H=null}}return !P.isTest}
  function roll(el,from,to){
    if(RM()||from===to){el.textContent=to;return}
    var t0=performance.now();(function f(t){var k=Math.min(1,(t-t0)/450);el.textContent=Math.round(from+(to-from)*k);if(k<1)requestAnimationFrame(f)})(t0);
  }
  function anim(el,c){if(RM())return;el.classList.remove(c);void el.offsetWidth;el.classList.add(c)}
  function paint(gain){
    var h=mount();if(!h)return;h.classList.add('on');
    var xe=h.querySelector('.lx-xp'),xb=xe.querySelector('b'),from=+xb.textContent||0;
    roll(xb,from,S.xp);
    var ce=h.querySelector('.lx-combo');
    if(S.combo>=2){ce.classList.add('on');ce.classList.toggle('hot',S.combo>=3);ce.querySelector('b').textContent='x'+S.combo;anim(ce,'pop')}else ce.classList.remove('on','hot');
    h.querySelector('.lx-acc b').textContent=Math.round(S.ok/Math.max(1,S.n)*100)+'%';
    if(gain){anim(xe,'pop');anim(xe,'glow');
      if(!RM()){var f=document.createElement('div');f.className='lx-float'+(S.combo>=2?' c':'');f.textContent='+'+gain+' XP'+(S.combo>=2?' 🔥x'+S.combo:'');h.appendChild(f);setTimeout(function(){f.remove()},1200)}
    }else anim(h,'shake');
  }
  function hit(ok){
    try{
      if(!sync())return;
      var now=Date.now();if(now-S.last<400)return;S.last=now;
      S.n++;if(ok){S.ok++;S.combo++;S.xp+=10;}else S.combo=0;
      S.seen=P.score||0;paint(ok?10:0);
    }catch(e){}
  }
  function wrap(name,fn){
    try{var o=window[name];if(typeof o!=='function'||o.__lx)return;
      var w=function(){var r=o.apply(this,arguments);try{fn.apply(null,arguments)}catch(e){}return r};w.__lx=1;window[name]=w}catch(e){}
  }
  function install(){
    wrap('fxGrade',function(ok){hit(!!ok)});
    wrap('beep',function(ok){hit(!!ok)});
    wrap('sfx',function(n){if(n==='tada'&&sync()&&(P.score||0)>S.seen)hit(true)});
  }
  install();
  window.addEventListener('load',install);
  window.__livexp=S;
})();
