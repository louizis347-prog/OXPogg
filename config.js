/* Configuração do Pogglot.
 * Tudo aqui é opcional. Deixe vazio para usar o modo DEMO (dados só neste navegador).
 *
 * supabaseUrl / supabaseAnonKey: login e comunidade reais (Supabase > Project Settings > API).
 *   Nunca coloque a chave service_role aqui.
 *
 * tts: voz neural em nuvem (ElevenLabs, Azure, Google, OpenAI ou um proxy seu). Sem isso o app usa a
 *   melhor voz instalada no aparelho. O áudio fica guardado no aparelho para uso offline.
 *   Exemplo:
 *   tts:{url:'https://seu-servidor/tts',method:'POST',headers:{},
 *        voices:{'en-US':{default:'alloy',f:['nova','shimmer'],m:['onyx','echo']}},
 *        // opcional: monta a requisição do jeito do seu provedor
 *        // request({text,lang,voice,rate}){return{url:'...',init:{method:'POST',body:JSON.stringify({...})}}}
 *       }
 *   O servidor deve responder com áudio (audio/mpeg ou audio/wav). Nunca coloque a chave do provedor aqui: guarde-a no seu servidor.
 *
 * checkoutUrl / checkoutUrlYear: links de pagamento mensal e anual. Preenchidos, ativam o paywall e os botões de assinar da landing.
 * priceMonth / priceYear: (opcional) textos de preço exibidos na landing, ex.: 'R$ 29,90'. Vazios, a landing não mostra preço.
 *
 * supportUrl: (opcional) link de apoio/doação (Pix, Apoia.se, Mercado Pago…); aparece no perfil do aluno.
 *
 * ai: correção do "Sua vez".
 *   endpoint: seu servidor recebe {lang,uiLang,prompt,chips,model,level,text} e devolve
 *             {corrected,score,issues:[{wrong,fix,why}],praise:[]}.
 *   teacher:  (opcional) endereço que recebe o mesmo JSON para correção humana; mostra o botão "Enviar ao professor".
 *   Sem endpoint, o app tenta o Claude da própria página (quando publicada como artefato) e, por último, uma conferência básica no aparelho.
 */
window.POGGLOT_CONFIG={supabaseUrl:'https://mgvjxrmtatwachhtjfmm.supabase.co',supabaseAnonKey:'sb_publishable_VIRbeM3pO0f_71uY8HUCCA_rSToliuU',tts:null,ai:{endpoint:'',teacher:''},analyticsEndpoint:'',supportUrl:'',checkoutUrl:'',checkoutUrlYear:'',priceMonth:'',priceYear:'',freeEpisodes:5};
