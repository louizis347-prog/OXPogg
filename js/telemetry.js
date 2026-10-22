/* Telemetria mínima e opcional: mede o caminho do produto sem coletar texto, áudio ou PII. */
(function(w){'use strict';
  var cfg=w.POGGLOT_CONFIG||{},KEY='pogglot:telemetry',MAX=80;
  function queue(){try{return JSON.parse(localStorage.getItem(KEY)||'[]')}catch(e){return[]}}
  function save(a){try{localStorage.setItem(KEY,JSON.stringify(a.slice(-MAX)))}catch(e){}}
  function send(ev){var a=queue();a.push(ev);save(a);var url=cfg.analyticsEndpoint;if(!url||!/^https:\/\//i.test(url))return;try{var body=JSON.stringify(ev);if(navigator.sendBeacon){navigator.sendBeacon(url,new Blob([body],{type:'application/json'}));}else{fetch(url,{method:'POST',headers:{'content-type':'application/json'},body,keepalive:true}).catch(function(){})}}catch(e){}}
  function event(name,meta){send({name:name,meta:meta||{},at:new Date().toISOString(),path:location.pathname+location.hash})}
  w.PogTelemetry={event:event,local:function(){return queue()}};
  document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('[data-course],[data-ep],[data-go],[data-hl]');if(!b)return;var meta={};if(b.dataset.course)meta.course=b.dataset.course;if(b.dataset.ep)meta.episode=b.dataset.ep;if(b.dataset.go)meta.destination=b.dataset.go;if(b.dataset.hl)meta.interface=b.dataset.hl;event('interaction',meta)},true);
  event('page_view');
})(window);
