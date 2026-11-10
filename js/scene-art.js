/* Miniaturas de curso/idioma com a arte pintada da landing (img/landing/art). Substitui as cenas simples de SC.get para os cursos. */
(function(){
'use strict';
if(typeof SC==='undefined'||!SC.get)return;
var MAP={cv_usa:'en',cv_es:'es',cv_fr:'fr',cv_de:'de',cv_it:'it',cv_jp:'ja',cv_ko:'ko',cv_br:'pt',harbor:'en',railway:'en',park:'en',library:'en',fifth:'en'};
var POS=['50% 60%','18% 62%','82% 60%','50% 28%','30% 80%','70% 40%'],n=0,og=SC.get;
SC.get=function(k){
  var a=MAP[k];if(!a)return og(k);
  var p=POS[(n++)%POS.length];
  return '<img class="sc-art" src="img/landing/art/lang-'+a+'.svg" width="480" height="360" alt="" decoding="async" loading="lazy" style="object-position:'+p+'">';
};
window.PogLangArt=function(id){
  var m={en:'en',enes:'en',es:'es',fr:'fr',frbr:'fr',de:'de',debr:'de',it:'it',itbr:'it',ja:'ja',jabr:'ja',ko:'ko',kobr:'ko',pt:'pt',nb:'en',nbes:'es',nbfr:'fr',nbde:'de',nbja:'ja',nbeng:'en',nbit:'it',nbpt:'pt',pk:'en'};
  var a=m[id]||'en';return id==='pk'?'img/landing/art/course-pocket.svg':'img/landing/art/lang-'+a+'.svg';
};
})();
