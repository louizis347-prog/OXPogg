# Elenco da série "Maple Street": 100 moradores. nome:país:profissão
RAW = """Mia:Brazil:teacher|Ken:Japan:chef|Pog:Pogland:guide|Sara:Egypt:nurse|Leo:Italy:waiter|Ana:Mexico:student|Tom:England:driver|Yuki:Japan:designer|Omar:Morocco:baker|Lily:China:student|
Jack:USA:mechanic|Nina:Russia:doctor|Raj:India:engineer|Emma:Canada:librarian|Carlos:Spain:musician|Zoe:Australia:vet|Ali:Turkey:shopkeeper|Eva:Germany:pilot|Sam:Ireland:postman|Dani:Argentina:dancer|
Hana:Korea:singer|Paul:France:painter|Maya:India:student|Ben:Scotland:farmer|Lucia:Peru:cook|Tariq:Pakistan:taxi driver|Ida:Sweden:architect|Joe:Jamaica:coach|Mei:China:dentist|Luis:Colombia:barista|
Amy:Wales:reporter|Kofi:Ghana:electrician|Rosa:Portugal:florist|Ivan:Poland:builder|Nora:Norway:skier|Diego:Chile:photographer|Lena:Austria:baker|Sami:Lebanon:tailor|Kate:New Zealand:ranger|Hugo:Belgium:clerk|
Aya:Japan:nurse|Finn:Denmark:sailor|Mina:Iran:professor|Beto:Brazil:footballer|Tessa:South Africa:lawyer|Noah:USA:pilot|Isla:Scotland:artist|Pablo:Mexico:gardener|Fatima:Nigeria:banker|Theo:Greece:fisher|
Cleo:Egypt:guide|Ryo:Japan:student|Alma:Spain:teacher|Dev:India:chef|Greta:Germany:cyclist|Remy:France:chef|Lola:Cuba:singer|Sven:Sweden:carpenter|Nadia:Algeria:doctor|Marco:Italy:driver|
Ruth:Kenya:runner|Andre:Portugal:waiter|Pia:Finland:designer|Cody:Canada:cowboy|Elif:Turkey:student|Jin:Korea:gamer|Olga:Ukraine:nurse|Max:Germany:engineer|Tina:Philippines:nurse|Gus:England:baker|
Zara:Pakistan:student|Hiro:Japan:fisher|Bella:Italy:waitress|Abel:Ethiopia:runner|Vera:Czechia:violinist|Colin:Ireland:fiddler|Sofia:Greece:waitress|Tao:China:cook|Mara:Romania:seamstress|Jonas:Lithuania:basketball player|
Dina:Jordan:pharmacist|Nico:Argentina:barista|Kira:Russia:skater|Pete:USA:fireman|Suri:Thailand:cook|Will:England:actor|Lara:Brazil:vet|Ian:Scotland:piper|Naomi:Kenya:teacher|Oscar:Peru:guide|
Rita:India:pilot|Felix:Austria:pianist|Una:Iceland:fisher|Kai:Hawaii:surfer|Mona:Saudi Arabia:doctor|Bruno:Brazil:cook|Jade:Jamaica:dancer|Otto:Netherlands:cyclist|Pru:England:gardener|Gigi:Italy:waitress"""
PEOPLE = []
for chunk in RAW.replace("\n", "").split("|"):
    nm, ct, jb = chunk.strip().split(":")
    PEOPLE.append(dict(name=nm, country=ct, job=jb))
assert len(PEOPLE) == 100, len(PEOPLE)

REG = {  # país -> (peles, cabelos)
 'light': (['pale', 'light'], ['blond', 'brown', 'auburn', 'red', 'black']),
 'med': (['tan', 'light', 'tan'], ['black', 'brown', 'black']),
 'brown': (['brown', 'tan'], ['black', 'brown']),
 'dark': (['dark', 'deep', 'brown'], ['black', 'black', 'brown']),
 'east': (['light', 'tan'], ['black', 'black', 'brown']),
}
LIGHT = 'England Scotland Ireland Wales Germany Sweden Norway Denmark Finland Iceland Poland Austria Belgium France Netherlands Czechia Lithuania Ukraine Russia Canada USA Australia New Zealand New Zealand Pogland'.split()
EAST = 'Japan China Korea Thailand Philippines'.split()
DARK = 'Nigeria Ghana Kenya Ethiopia South Africa Jamaica Algeria'.split()
BROWN = 'India Pakistan Brazil Peru Colombia Mexico Chile Cuba Argentina Hawaii'.split()
TOPS = ['#e8473b', '#4a90d9', '#f2b84b', '#5cb85c', '#9b6bd1', '#ee7fa8', '#3fb5a8', '#f08a4b', '#6d7fcc', '#c9ce5a']
HS_F = ['long', 'bob', 'braids', 'pigtails', 'ponytail', 'bun', 'curly', 'side', 'afro']
HS_M = ['short', 'spiky', 'curly', 'side', 'afro', 'bald', 'short']
FEM = set('Mia Sara Ana Yuki Lily Nina Emma Zoe Eva Dani Hana Maya Lucia Ida Mei Amy Rosa Nora Lena Kate Aya Mina Tessa Isla Fatima Cleo Alma Greta Lola Nadia Ruth Pia Elif Olga Tina Zara Bella Vera Sofia Mara Dina Kira Suri Lara Naomi Rita Una Mona Jade Pru Gigi'.split())

def look(i):
    p = PEOPLE[i]; c = p['country']
    reg = 'east' if c in EAST else 'dark' if c in DARK else 'brown' if c in BROWN else 'med' if c in ('Egypt', 'Morocco', 'Turkey', 'Iran', 'Lebanon', 'Jordan', 'Saudi Arabia', 'Italy', 'Spain', 'Portugal', 'Greece', 'Romania') else 'light'
    sk, hr = REG[reg]
    fem = p['name'] in FEM
    hs = (HS_F if fem else HS_M)[(i * 7 + 3) % len(HS_F if fem else HS_M)]
    o = dict(hs=hs, outfit='dress' if fem and i % 3 == 0 else 'shirt', top=TOPS[(i * 3 + 1) % len(TOPS)], hair=hr[(i * 5) % len(hr)], skin=sk[i % len(sk)])
    if p['name'] == 'Pog': return dict(hs='spiky', outfit='shirt', top='#7b5cf0', hair='blue', skin='light')
    if hs == 'bald': o.pop('hair')
    return o
LOOK = {p['name']: look(i) for i, p in enumerate(PEOPLE)}
