const placementCompetencies=[
  ['grammar','Gramática','notebook'],['vocabulary','Vocabulário','map'],
  ['reading','Leitura','book'],['listening','Compreensão oral','chat']
];
const placementLevels=6;
const placementItemsPerLevel=10;
const placementStorage='english-placement-v2';
let placementState;
function freshPlacement(){
  return {started:false,finished:false,stage:0,answers:{},skipped:[],writing:''};
}
function readPlacement(){
  const saved=read(placementStorage,{});
  if(!saved||typeof saved!=='object')return freshPlacement();
  const result=freshPlacement();
  result.started=saved.started===true;
  result.finished=saved.finished===true;
  result.stage=Number.isInteger(saved.stage)&&saved.stage>=0&&saved.stage<placementLevels?saved.stage:0;
  result.writing=typeof saved.writing==='string'?saved.writing.slice(0,6000):'';
  result.skipped=Array.isArray(saved.skipped)?[...new Set(saved.skipped.filter(level=>Number.isInteger(level)&&level>=0&&level<placementLevels))]:[];
  for(const [key,answer] of Object.entries(saved.answers||{})){
    if(/^[0-5]-[0-9]$/.test(key)&&Number.isInteger(answer)&&answer>=0&&answer<4)result.answers[key]=answer;
  }
  if(result.finished&&placementIncompleteLevel(result)!==null)result.finished=false;
  return result;
}
function savePlacement(){write(placementStorage,placementState);}
function placementItems(stage){
  return [...placementUse[stage],...placementReading[stage][2],...placementListening[stage][1]];
}
function placementSkill(index){
  return index<4?'grammar':index<6?'vocabulary':index<8?'reading':'listening';
}
function placementIncompleteLevel(state,limit=placementLevels){
  for(let stage=0;stage<limit;stage++){
    const length=state.skipped.includes(stage)?8:placementItemsPerLevel;
    for(let i=0;i<length;i++)if(!Object.hasOwn(state.answers,stage+'-'+i))return stage;
  }
  return null;
}
function placementResults(state){
  const scores=Array.from({length:placementLevels},(_,stage)=>{
    const result=Object.fromEntries(placementCompetencies.map(([key])=>[key,{correct:0,total:0}]));
    const skipped=state.skipped.includes(stage);
    placementItems(stage).forEach((_,i)=>{
      const skill=placementSkill(i);
      if(skill==='listening'&&skipped)return;
      result[skill].total++;
      if(state.answers[stage+'-'+i]===0)result[skill].correct++;
    });
    const correct=Object.values(result).reduce((n,m)=>n+m.correct,0);
    const total=Object.values(result).reduce((n,m)=>n+m.total,0);
    const passed=correct>=(skipped?6:8)&&result.grammar.correct+result.vocabulary.correct>=4&&
      (skipped?result.reading.correct===2:result.reading.correct>=1&&result.listening.correct>=1);
    return {stage,correct,total,result,passed};
  });
  const gap=scores.find(({passed})=>!passed);
  const firstUnassessed=scores.find(row=>row.result.listening.total===0)?.stage;
  const candidate=gap?.stage??placementLevels-1;
  const recommended=firstUnassessed===undefined?candidate:Math.min(candidate,firstUnassessed);
  const totals=Object.fromEntries(placementCompetencies.map(([skill])=>[skill,scores.reduce((sum,row)=>({
    correct:sum.correct+row.result[skill].correct,total:sum.total+row.result[skill].total
  }),{correct:0,total:0})]));
  return {scores,totals,recommended,audioCoverage:firstUnassessed===undefined};
}
function placementOrdering(stage,index){
  const orders=[[2,0,3,1],[1,3,0,2],[0,2,1,3],[3,1,2,0]];
  return orders[(index+stage*3)%orders.length];
}
function placementQuestion(stage,index){
  const [question,...rest]=placementItems(stage)[index];
  const key=stage+'-'+index;
  return '<fieldset class="placement-question"><legend lang="en-US"><span>'+(index+1)+'.</span> '+clean(question)+'</legend>'+
    placementOrdering(stage,index).map(option=>'<label lang="en-US" class="placement-option"><input type="radio" name="p-'+key+'" data-placement-answer="'+key+'" value="'+option+'"'+
      (placementState.answers[key]===option?' checked':'')+'><span>'+clean(rest[option])+'</span></label>').join('')+'</fieldset>';
}
function placementBlock(title,glyph,content){
  return '<section class="placement-block"><h3>'+routeIcon(glyph)+clean(title)+'</h3>'+content+'</section>';
}
function placementStage(){
  const stage=placementState.stage;
  const audioSkipped=placementState.skipped.includes(stage),model=placementReading[stage];
  const questions=indices=>indices.map(i=>placementQuestion(stage,i)).join('');
  const stepTabs=levels.map((label,i)=>{
    const available=i<=stage||placementIncompleteLevel(placementState,i)===null;
    return '<button type="button" data-placement-stage="'+i+'"'+(i===stage?' aria-current="step"':'')+(available?'':' disabled')+'>'+label+'</button>';
  }).join('');
  const answered=Array.from({length:placementItemsPerLevel},(_,i)=>i).filter(i=>
    (i<8||!audioSkipped)&&Object.hasOwn(placementState.answers,stage+'-'+i)).length;
  return '<div class="placement-stages" aria-label="Etapas do teste">'+stepTabs+'</div><form id="placementForm">'+
    '<div class="placement-stage-head"><div><h2 id="placementFocus" tabindex="-1">Etapa '+levels[stage]+'</h2><p id="placementAnswered" aria-live="polite">'+answered+' de '+(audioSkipped?8:10)+' respondidas</p></div>'+
      '<progress id="placementProgress" value="'+answered+'" max="'+(audioSkipped?8:10)+'" aria-label="Questões respondidas na etapa"></progress></div>'+
    placementBlock('Gramática','notebook',questions([0,1,2,3]))+
    placementBlock('Vocabulário','map',questions([4,5]))+
    placementBlock('Leitura','book','<div class="placement-passage" lang="en-US"><strong>'+clean(model[0])+'</strong><p>'+clean(model[1])+'</p></div>'+questions([6,7]))+
    placementBlock('Compreensão oral','chat',audioSkipped?
      '<p>Etapa de áudio pulada. O relatório mostrará a cobertura de escuta.</p><button type="button" data-placement-toggle-audio>Ativar questões de áudio</button>':
      '<p>Ouça a mensagem em inglês e responda às duas perguntas. Use a voz do navegador.</p><div class="controls"><button type="button" data-placement-audio>Ouvir a mensagem</button><button type="button" data-placement-toggle-audio>Estou sem áudio</button></div>'+
      '<p id="placementAudioStatus" class="meta" role="status"></p>'+questions([8,9]))+
    '<p id="placementError" class="placement-error" role="alert"></p><div class="controls placement-actions">'+
      (stage>0?'<button type="button" data-placement-stage="'+(stage-1)+'">Etapa anterior</button>':'')+
      '<button class="primary">'+(stage===placementLevels-1?'Ver resultado':'Próxima etapa')+'</button></div></form>';
}
function placementCorrections(){
  return levels.map((level,stage)=>{
    const skip=placementState.skipped.includes(stage);
    const questions=placementItems(stage).map(([question,correct,w1,w2,w3,reason],i)=>{
      const options=[correct,w1,w2,w3],raw=placementState.answers[stage+'-'+i];
      const missed=skip&&i>=8;
      const status=missed?'Não avaliada':raw===0?'Correta':'Incorreta';
      return '<li><p><strong lang="en-US">'+clean(question)+'</strong></p><p>'+status+
        (missed?'':' · Sua resposta: <span lang="en-US">'+clean(options[raw])+'</span>')+'</p>'+
        '<p>Resposta: <span lang="en-US">'+clean(correct)+'</span> · '+clean(reason)+'</p></li>';
    }).join('');
    return '<details><summary>Gabarito '+level+'</summary><h4>Transcrição do áudio</h4><p lang="en-US">'+
      clean(placementListening[stage][0])+'</p><ol class="placement-corrections">'+questions+'</ol></details>';
  }).join('');
}
function placementReport(){
  const {scores,totals,recommended,audioCoverage}=placementResults(placementState);
  const [writing,speaking]=placementProduction[recommended];
  const metrics=placementCompetencies.map(([key,label,glyph])=>{
    const {correct,total}=totals[key];
    return '<article class="placement-metric">'+routeIcon(glyph)+'<h3>'+label+'</h3><strong>'+
      (total?correct+'/'+total:'Sem respostas')+'</strong>'+(total?'<progress aria-label="'+label+'" value="'+correct+'" max="'+total+'"></progress>':'')+'</article>';
  }).join('');
  const summary=scores.map(row=>'<tr><th scope="row">'+levels[row.stage]+'</th>'+
    placementCompetencies.map(([skill])=>{const {correct,total}=row.result[skill];return '<td>'+(total?correct+'/'+total:'Pulada')+'</td>';}).join('')+
    '<td>'+row.correct+'/'+row.total+'</td><td>'+(row.passed?'Base para avançar':'Vale revisar')+'</td></tr>').join('');
  return '<div class="placement-results"><div class="placement-outcome"><div><p class="lesson-context">Ponto de partida sugerido</p>'+
    '<h2 id="placementFocus" tabindex="-1">Inglês '+levels[recommended]+'</h2><p>O resultado indica onde começar a estudar pela amostra de habilidades do teste.</p>'+
    (audioCoverage?'':'<p>A escuta teve etapas puladas. A sugestão fica limitada à primeira etapa em que faltou avaliação de áudio.</p>')+
    '<button class="primary" type="button" data-placement-use="'+recommended+'">Abrir trilha '+levels[recommended]+'</button></div>'+
    routeIllustration('flag')+'</div><section><h3>Resultado por competência</h3><div class="placement-metrics">'+metrics+
    '</div></section><section class="placement-block"><h3>'+routeIcon('map')+'Resultados por etapa</h3>'+
    '<div class="placement-table"><table><thead><tr><th>Nível</th><th>Gramática</th><th>Vocabulário</th><th>Leitura</th><th>Escuta</th><th>Total</th><th>Indicação</th></tr></thead><tbody>'+
    summary+'</tbody></table></div><details><summary>Como a sugestão é calculada</summary>'+
    '<p>O teste procura a primeira etapa com lacunas no percurso. Com áudio, exige 8 de 10 acertos, ao menos 4 de 6 em gramática e vocabulário e pelo menos um acerto em cada parte de compreensão. Sem áudio, exige 6 de 8, ambas as respostas de leitura corretas e mantém a recomendação limitada à primeira etapa com escuta pulada.</p></details></section>'+
    '<section class="placement-block"><h3>'+routeIcon('puzzle')+'Produção escrita e oral</h3><p>Atividades de autoavaliação. Elas ficam fora da nota automática.</p>'+
    '<h4>Escrita</h4><p>'+clean(writing)+'</p><label for="placementWriting">Seu texto em inglês</label>'+
    '<textarea id="placementWriting" rows="5" maxlength="6000" lang="en-US" placeholder="Type your response here.">'+clean(placementState.writing)+'</textarea>'+
    '<h4>Fala</h4><p>'+clean(speaking)+'</p><details class="voice-panel"><summary>Gravar uma resposta</summary><p>O áudio fica nesta página.</p><button type="button" data-record>Gravar minha voz</button><audio controls hidden></audio><p class="voice-status" role="status"></p></details>'+
    '<h4>Critérios para conferir sua resposta</h4><ul><li>Cumpri o que foi pedido e organizei as ideias?</li><li>Usei palavras e estruturas adequadas à situação?</li><li>Meu texto ou minha fala ficaria claro para outra pessoa?</li></ul></section>'+
    '<section class="placement-block"><h3>'+routeIcon('check')+'Gabarito comentado</h3>'+placementCorrections()+
    '</section><button type="button" data-placement-reset>Refazer o teste</button></div>';
}
function renderPlacement(){
  if(!placementState)placementState=readPlacement();
  const container=$('placementTest');
  container.innerHTML=placementState.finished?placementReport():placementState.started?placementStage():
    '<div class="placement-intro"><div><h2 id="placementFocus" tabindex="-1">Descubra seu ponto de partida</h2>'+
    '<p>São <strong>60 questões</strong> em seis etapas, do A1 ao C2. Separe cerca de 25 a 40 minutos. Você pode parar e continuar neste navegador.</p>'+
    '<p>O relatório separa gramática, vocabulário, leitura e escuta. A escrita e a fala têm atividades de autoavaliação ao final.</p>'+
    '<button type="button" class="primary" data-placement-start>Começar teste</button></div>'+routeIllustration('map')+'</div>';
  if(container.dataset.events)return;
  container.dataset.events='true';
  container.addEventListener('change',event=>{
    const key=event.target.dataset.placementAnswer;
    if(!key)return;
    placementState.answers[key]=Number(event.target.value);savePlacement();
    const stage=placementState.stage,length=placementState.skipped.includes(stage)?8:10;
    const count=Array.from({length},(_,i)=>i).filter(i=>Object.hasOwn(placementState.answers,stage+'-'+i)).length;
    $('placementAnswered').textContent=count+' de '+length+' respondidas';
    $('placementProgress').value=count;
  });
  container.addEventListener('input',event=>{
    if(event.target.id==='placementWriting'){placementState.writing=event.target.value;savePlacement();}
  });
  container.addEventListener('submit',event=>{
    if(event.target.id!=='placementForm')return;
    event.preventDefault();
    const incomplete=placementIncompleteLevel(placementState,placementState.stage+1);
    if(incomplete!==null){
      if(incomplete!==placementState.stage){placementState.stage=incomplete;savePlacement();movePlacement();}
      $('placementError').textContent='Responda às questões desta etapa antes de avançar.';
      $('placementError').scrollIntoView?.({block:'nearest'});
      return;
    }
    if(placementState.stage<placementLevels-1)placementState.stage++;
    else placementState.finished=true;
    savePlacement();movePlacement();
  });
  container.addEventListener('click',event=>{
    const button=event.target.closest('button');
    if(!button||button.disabled)return;
    if(button.dataset.placementStart!==undefined){placementState.started=true;savePlacement();movePlacement();return;}
    if(button.dataset.placementReset!==undefined){
      placementState=freshPlacement();savePlacement();movePlacement();return;
    }
    if(button.dataset.placementStage!==undefined){
      placementState.stage=Number(button.dataset.placementStage);savePlacement();movePlacement();return;
    }
    if(button.dataset.placementToggleAudio!==undefined){
      const stage=placementState.stage, index=placementState.skipped.indexOf(stage);
      if(index>=0)placementState.skipped.splice(index,1);else placementState.skipped.push(stage);
      savePlacement();movePlacement();return;
    }
    if(button.dataset.placementAudio!==undefined){
      const played=speech(placementListening[placementState.stage][0],.88,'en-US');
      $('placementAudioStatus').textContent=played?'Áudio iniciado. Você pode ouvir novamente.':'A voz do navegador está indisponível. Use a opção Estou sem áudio.';
      return;
    }
    if(button.dataset.placementUse!==undefined){location.hash=catalogHash('eng',Number(button.dataset.placementUse));return;}
    if(button.dataset.record!==undefined)handleLessonTools(event);
  });
}
function movePlacement(){
  stopVoiceTools();
  if(window.speechSynthesis)window.speechSynthesis.cancel();
  renderPlacement();
  $('placementFocus')?.focus({preventScroll:true});
  $('placementFocus')?.scrollIntoView?.({block:'start'});
}
