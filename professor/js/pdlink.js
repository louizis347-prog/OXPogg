/* Liga a aula ao vivo às mini lições do PoggloDict: acrescenta quadros "antes", aquecimento e "depois" a partir de data/pd_links.json.
   A aula original não é alterada: os quadros entram só quando a aula tem entrada no arquivo. */
(function(){
'use strict';
window.PDLINK={inject:function(L,all){
 var e=all&&all[String(L.n)];if(!e||!L.pages||L.pages.some(function(p){return p.kind==='pdlink'}))return;
 var pages=L.pages,at=pages.findIndex(function(p){return p.kind==='cover'});at=at<0?0:at+1;
 var add=[{t:'q1',stage:'mission',kind:'pdlink',mode:'antes',title:'PoggloDict · antes da aula',pd:e}];
 if((e.quiz||[]).length)add.push({t:'q1',stage:'mission',kind:'quiz',title:'Aquecimento · PoggloDict',instruction:'Revise em poucos minutos o que você viu nas mini lições do PoggloDict.',items:e.quiz});
 pages.splice.apply(pages,[at,0].concat(add));
 var end=pages.findIndex(function(p){return p.kind==='exit'});end=end<0?pages.length:end;
 pages.splice(end,0,{t:'q1',stage:'wrap',kind:'pdlink',mode:'depois',title:'PoggloDict · depois da aula',pd:e});
}};
})();
