# Troca de verbos e palavras que ainda repetiam com o episódio vizinho (ver ova2b.RP).
from v3.ova2b import RP, VL, L


def V(v, ic, pt, ok, bad, ex, ex_pt, note):
    return (v, ic, pt, ok, bad, ex, ex_pt, note)


RP(7081187, vocab={'snow': ('☀️', 'sunshine', 'sol', 'Soa como “SÂN-xain”.')})
RP(7920027, verbs={'travel': V('schedule', '🗓️', 'agendar', 'I schedule a trip.', 'I schedules a trip.', 'She scheduled it.', 'Ela agendou.', 'she **schedules**.')},
   vocab={'planner': ('📅', 'calendar', 'calendário', 'Soa como “KÉ-len-der”.')})
RP(920029, verbs={'like': V('adore', '😍', 'adorar', 'I adore pasta.', 'I adores pasta.', 'She adores cake.', 'Ela adora bolo.', 'she **adores**.')})
RP(7920030, verbs={'cost': V('bargain', '🤝', 'pechinchar', 'He bargains for a price.', 'He bargain for a price.', 'We bargained.', 'Pechinchamos.', 'he **bargains**.')})
RP(7081211, verbs={'like': V('dislike', '👎', 'não gostar', 'I dislike waiting.', 'I dislikes waiting.', 'He dislikes noise.', 'Ele não gosta de barulho.', 'he **dislikes**.')})
RP(81212, vocab={'homework': ('📓', 'notebook', 'caderno', 'Soa como “NÔUT-buk”.')})
RP(7920031, verbs={'rest': V('relax', '🛋️', 'relaxar', 'You should relax.', 'You should relaxes.', 'She relaxes at home.', 'Ela relaxa em casa.', 'she **relaxes**.')})
RP(7081218, verbs={'go': V('attend', '🎟️', 'frequentar', 'I attend every concert.', 'I attends every concert.', 'She attends shows.', 'Ela vai a shows.', 'she **attends**.')})
RP(7081223, verbs={'win': V('beat', '🥇', 'vencer', 'We beat the team.', 'We beats the team.', 'They beat us.', 'Eles nos venceram.', 'she **beats**.')})
RP(7081228, verbs={'worry': V('rush', '💨', 'apressar-se', 'I rush to the meeting.', 'I rushes to the meeting.', 'He rushes home.', 'Ele corre para casa.', 'he **rushes**.')})
RP(81229, verbs={'have': V('own', '🏠', 'possuir', 'She owns a shop.', 'She own a shop.', 'They own a car.', 'Eles têm um carro.', 'she **owns**.')})
RP(7081229, verbs={'win': V('conquer', '🏆', 'conquistar', 'The army conquers the hill.', 'The army conquer the hill.', 'They conquered fear.', 'Eles venceram o medo.', 'it **conquers**.')})
RP(7081230, verbs={'hug': V('embrace', '🤗', 'abraçar', 'They embrace at the gate.', 'They embraces at the gate.', 'She embraced me.', 'Ela me abraçou.', 'she **embraces**.')})
RP(7081235, verbs={'move': V('relocate', '📦', 'mudar-se', 'We relocate to the coast.', 'We relocates to the coast.', 'They relocated.', 'Eles se mudaram.', 'he **relocates**.')},
   vocab={'party': ('🔥', 'campfire', 'fogueira', 'Soa como “KÉMP-fáier”.')})
RP(7081240, verbs={'save': V('invest', '📈', 'investir', 'She invests in gold.', 'She invest in gold.', 'We invested a lot.', 'Investimos muito.', 'she **invests**.')})
RP(7081241, vocab={'escalator': ('🛗', 'elevator', 'elevador', 'Soa como “É-le-vêi-ter”.')})
VL(81242, lab=L('ea', 'Laboratório de sons: breakfast, brush e sleep', 'ea soa é; u soa â; ee soa í.', 'Em breakfast, ea soa é: BRÉK-fast.',
                [('breakfast', 'BRÉK-fast', 'café da manhã', 'ea = é', 'breaker', 'BRÊI-ker'), ('brush', 'BRÂX', 'escova', 'u = â', 'bush', 'BÚX'), ('sleep', 'SLÍP', 'dormir', 'ee = í', 'slap', 'SLÉP')],
                ['He has breakfast.', 'Ele toma café da manhã.']))
RP(7081244, vocab={'hotel': ('🚉', 'station', 'estação', 'Soa como “STÊI-xon”.')})
RP(7081251, verbs={'watch': V('stream', '📡', 'transmitir', 'She streams the show.', 'She stream the show.', 'We streamed it.', 'Nós assistimos online.', 'she **streams**.')},
   vocab={'series': ('🎬', 'show', 'programa', 'Soa como “XÔU”.')})
RP(81252, verbs={'hear': V('tune', '📻', 'sintonizar', 'He tunes the radio.', 'He tune the radio.', 'I tuned in.', 'Sintonizei.', 'he **tunes**.')})
RP(7920036, vocab={'manners': ('🎶', 'lullaby', 'canção de ninar', 'Soa como “LÂ-la-bái”.')})
RP(7081254, vocab={'thread': ('🔘', 'button', 'botão', 'Soa como “BÂ-ton”.')})
RP(7081257, verbs={'work': V('earn', '💵', 'ganhar', 'She earns a good salary.', 'She earn a good salary.', 'I earned it.', 'Eu ganhei.', 'she **earns**.')})
RP(7081261, vocab={'manager': ('🧑‍💼', 'director', 'diretor', 'Soa como “di-RÉK-ter”.')})
RP(7081263, vocab={'practice': ('⭐', 'rating', 'classificação', 'Soa como “RÊI-ting”.')})
RP(81265, verbs={'study': V('enroll', '📝', 'matricular-se', 'She enrolls in a course.', 'She enroll in a course.', 'He enrolled today.', 'Ele se matriculou hoje.', 'she **enrolls**.')})
RP(920038, verbs={'be': V('become', '🦋', 'tornar-se', 'It becomes cool.', 'It become cool.', 'She became a fan.', 'Ela virou fã.', 'it **becomes**.')})
RP(7081269, verbs={'sound': V('rival', '🥊', 'rivalizar', 'He rivals the master.', 'He rival the master.', 'They rivaled him.', 'Eles rivalizaram com ele.', 'he **rivals**.')})
RP(81272, verbs={'be': V('wait', '⏳', 'esperar', 'We wait at home.', 'We waits at home.', 'He waited inside.', 'Ele esperou lá dentro.', 'we **wait**.')})
RP(7081272, verbs={'rain': V('drizzle', '🌦️', 'chuviscar', 'It drizzles in the evening.', 'It drizzle in the evening.', 'It drizzled all day.', 'Chuviscou o dia todo.', 'it **drizzles**.')},
   vocab={'storm': ('⚡', 'lightning', 'relâmpago', 'Soa como “LÁIT-ning”.')})
RP(81273, verbs={'rain': V('pour', '🌧️', 'chover forte', 'It pours in July.', 'It pour in July.', 'It poured at night.', 'Choveu forte à noite.', 'it **pours**.')})
RP(7081273, verbs={'be': V('reach', '🌡️', 'atingir', 'It reaches fifty degrees.', 'It reach fifty degrees.', 'It reached a record.', 'Atingiu um recorde.', 'it **reaches**.')})
RP(920039, verbs={'be': V('remain', '📍', 'permanecer', 'It remains the same.', 'It remain the same.', 'They remained here.', 'Eles ficaram aqui.', 'it **remains**.')})
RP(7081284, vocab={'number': ('🎓', 'diploma', 'diploma', 'Soa como “di-PLÔU-ma”.')})
RP(7920041, verbs={'write': V('draft', '📝', 'rascunhar', 'He drafts an email.', 'He draft an email.', 'I drafted a reply.', 'Rascunhei uma resposta.', 'he **drafts**.')})
RP(7081290, verbs={'avoid': V('skip', '⏭️', 'pular', 'Popeye skips dessert.', 'Popeye skip dessert.', 'She skipped lunch.', 'Ela pulou o almoço.', 'he **skips**.')},
   vocab={'fat': ('🍭', 'candy', 'bala', 'Soa como “KÉN-di”.')})
RP(81291, verbs={'taste': V('smell', '👃', 'cheirar', 'I smell fresh bread.', 'I smells fresh bread.', 'She smells the soup.', 'Ela cheira a sopa.', 'she **smells**.')})
RP(81296, verbs={'be': V('seem', '👀', 'parecer', 'It seems the same.', 'It seem the same.', 'They seem alike.', 'Eles parecem iguais.', 'it **seems**.')})
RP(7081296, verbs={'be': V('differ', '↔️', 'diferir', 'Life differs here.', 'Life differ here.', 'Cities differ a lot.', 'As cidades diferem muito.', 'it **differs**.')})
RP(81299, verbs={'be': V('obey', '✅', 'obedecer', 'Students obey the rules.', 'Students obeys the rules.', 'He obeys the teacher.', 'Ele obedece ao professor.', 'he **obeys**.')})
RP(7920043, vocab={'badge': ('🏨', 'lobby', 'saguão', 'Soa como “LÓ-bi”.')})
RP(7081302, verbs={'mean': V('clarify', '💡', 'esclarecer', 'She clarifies the rule.', 'She clarify the rule.', 'He clarified it.', 'Ele esclareceu.', 'she **clarifies**.')},
   vocab={'mean': ('🧩', 'clue', 'pista', 'Soa como “KLÚ”.')})
RP(7081305, vocab={'meeting': ('🚀', 'mission', 'missão', 'Soa como “MÍ-xon”.')})
RP(7920044, verbs={'check': V('weigh', '⚖️', 'pesar', 'The agent weighs the bag.', 'The agent weigh the bag.', 'It weighed ten kilos.', 'Pesou dez quilos.', 'it **weighs**.')})
RP(81311, verbs={'pay': V('split', '✂️', 'dividir', 'We split the bill.', 'We splits the bill.', 'She split the cake.', 'Ela dividiu o bolo.', 'we **split**.')})
RP(7081315, vocab={'afraid': ('😞', 'upset', 'chateado', 'Soa como “ap-SÉT”.')})
RP(7081318, verbs={'drive': V('accelerate', '🚀', 'acelerar', 'He accelerates too fast.', 'He accelerate too fast.', 'I accelerated.', 'Eu acelerei.', 'he **accelerates**.')})
RP(7081325, verbs={'rest': V('stretch', '🤸', 'alongar', 'I stretch every day.', 'I stretches every day.', 'She stretches daily.', 'Ela se alonga todo dia.', 'she **stretches**.')})
RP(7920047, verbs={'add': V('blend', '🥣', 'misturar', 'She blends the flour.', 'She blend the flour.', 'He blended the batter.', 'Ele misturou a massa.', 'she **blends**.')})
RP(7081334, verbs={'eat': V('nibble', '🍪', 'beliscar', 'I nibble cookies.', 'I nibbles cookies.', 'He nibbled a biscuit.', 'Ele beliscou um biscoito.', 'he **nibbles**.')})
RP(7081339, verbs={'rest': V('recuperate', '🩹', 'recuperar-se', 'She recuperates fast.', 'She recuperate fast.', 'I recuperated well.', 'Eu me recuperei bem.', 'she **recuperates**.')})
RP(81345, verbs={'like': V('prefer', '⭐', 'preferir', 'I prefer tea.', 'I prefers tea.', 'He prefers coffee.', 'Ele prefere café.', 'he **prefers**.')})
