// Verbetes extras do dicionário inglês (gerado por tools/poglodict_build_dict.py; fonte: fontes/dicionario/en_extra.json)
const englishExtraWords=[];

(function(){
const ART={cup:'Comida e bebida',ticket:'Viagem e transporte',city:'Casa e cidade',park:'Casa e cidade',chat:'Pessoas e relações',notebook:'Trabalho e estudo',health:'Vocabulário geral',map:'Vocabulário geral',flag:'Vocabulário geral'};
const stores=()=>[
  typeof englishA1Plans!=='undefined'&&{plans:englishA1Plans,content:englishA1Content,themes:englishA1PhotoThemes},
  typeof englishA2Plans!=='undefined'&&{plans:englishA2Plans,content:englishA2Content,themes:englishA2PhotoThemes},
  typeof englishB1Plans!=='undefined'&&{plans:englishB1Plans,content:englishB1Content,themes:englishB1PhotoThemes}
].filter(Boolean);
const lemmas=w=>[w.replace(/ies$/,'y'),w.replace(/es$/,''),w.replace(/s$/,''),w.replace(/ing$/,''),w.replace(/ing$/,'e'),w.replace(/ed$/,''),w.replace(/ed$/,'e')];
const original=addSceneWords;
addSceneWords=function(language,base){
  const words=original(language,base);
  if(language!=='eng')return words;
  const entry=(word,part,pt,en,enPt,theme)=>({theme:theme||'Vocabulário geral',
    row:[word,pt,part,part==='phrase'?1:0,en||'','','',enPt||'','','',pt,0,'','','','lesson'],second:null});
  for(const [word,part,pt,en,enPt] of englishExtraWords)if(!words.has(word))words.set(word,entry(word,part,pt,en,enPt));
  for(const store of stores()){
    store.plans.forEach((plan,i)=>{
      if(!plan)return;
      const rows=store.content[i]?[...store.content[i][0],...store.content[i][1]]:[];
      const theme=ART[store.themes[i]]||'Vocabulário geral';
      for(const [raw,pt] of plan.words){
        const word=raw.toLowerCase().replace(/[.!?]+$/,'').trim();
        if(!word||/…/.test(word)||words.has(word))continue;
        const phrase=/\s/.test(word);
        let part=phrase?'phrase':'noun';
        if(!phrase)for(const l of lemmas(word)){const e=words.get(l);if(e&&e.row[2]&&e.row[2]!=='phrase'){part=e.row[2];break;}}
        const line=rows.find(r=>r[0].toLowerCase().includes(word));
        words.set(word,entry(word,part,pt,line?line[0]:'',line?line[1]:'',theme));
      }
    });
  }
  return words;
};
})();
