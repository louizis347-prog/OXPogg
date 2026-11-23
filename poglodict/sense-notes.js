const contrastNotes={
eng:{
  "'ve":{note:'Contração normalmente átona, comum na fala e na escrita informal. Use a forma completa quando quiser dar ênfase.', expansions:[
    ['I’ve finished my homework.','I have finished my homework.'],
    ['They’ve already left the station.','They have already left the station.']
  ]},
  can:{note:'No primeiro exemplo, can indica capacidade. No segundo, indica permissão.'},
  will:{note:'A frase da ligação pode ser uma promessa. A frase sobre a loja informa um horário futuro.'}
},
spa:{se:{note:'No primeiro exemplo, Ana lava as próprias mãos. No segundo, os dois amigos se abraçam mutuamente.'}},
ita:{lei:{note:'Com verbo na terceira pessoa, lei pode significar ela ou funcionar como tratamento formal. O vocativo signora torna o segundo uso explícito.'}},
deu:{haten:{note:'Empréstimo informal usado sobretudo na internet. Para descrever uma crítica de modo neutro, use kritisieren.'}},
ara:{سامي:{note:'Aqui é o nome próprio Sami. Quando usado como adjetivo em outros contextos, سامٍ pode significar elevado.'}},
jpn:{僕:{note:'Pronome de primeira pessoa. O tom costuma ser menos formal do que 私 em ambientes profissionais.'}},
por:{
  foi:{note:bilingual('The first example uses ir to describe movement. The second uses ser to describe the trip.', 'El primer ejemplo usa ir para expresar movimiento. El segundo usa ser para describir el viaje.')},
  achar:{note:bilingual('With a direct object, achar can mean “find.” With que, it often introduces an opinion.', 'Con un objeto directo, achar puede significar «encontrar». Con que, suele introducir una opinión.')},
  você:{note:bilingual('Você takes a third-person verb: você fala. In Brazil, tu is also common in some regions, with regional agreement patterns.', 'Você lleva el verbo en tercera persona: você fala. En Brasil también se usa tu en algunas regiones, con patrones de concordancia regionales.')},
  tom:{note:bilingual('The first example is about someone’s voice. The second describes a color.', 'El primer ejemplo se refiere a la voz. El segundo describe un color.')}
}
};
function entryNote(item){
  const usage=contrastNotes[lang]?.[item.row[0]];
  if(!usage)return '';
  return '<div class="entry-usage"><p>'+clean(companionText(usage.note))+'</p>'+
    (usage.expansions?'<dl>'+usage.expansions.map(([short,full])=>'<dt>'+nativeText(short)+'</dt><dd>'+nativeText(full)+'</dd>').join('')+'</dl>':'')+'</div>';
}
