const bundledData=new Map();
const dataLoads=new Map();
window.poggloRegisterData=(name,data)=>bundledData.set(name,data);
function loadJson(name){
  if(!/^[a-z-]+\.json$/.test(name))return Promise.reject(new Error('Invalid data file'));
  if(!window.POGGLO_OFFLINE)return fetch(name).then(response=>{
    if(!response.ok)throw Error(response.status);
    return response.json();
  });
  if(bundledData.has(name))return Promise.resolve(bundledData.get(name));
  if(dataLoads.has(name))return dataLoads.get(name);
  const request=new Promise((resolve,reject)=>{
    const script=document.createElement('script');
    script.src='dados/'+name+'.js';
    script.onload=()=>{
      script.remove();
      if(!bundledData.has(name))reject(new Error('Missing offline data'));
      else resolve(bundledData.get(name));
    };
    script.onerror=()=>{script.remove();reject(new Error('Missing offline file'));};
    document.head.appendChild(script);
  }).catch(error=>{dataLoads.delete(name);throw error;});
  dataLoads.set(name,request);
  return request;
}
if(window.POGGLO_OFFLINE)document.documentElement.dataset.offline='true';
