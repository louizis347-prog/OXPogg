"""Remove four cultural-reference collisions in Spanish A2 139–198."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
changes={
  169:('Coco','Los tres huastecos','1948','filme de Ismael Rodríguez','O filme mexicano acompanha três irmãos e a cultura musical popular; esta aula usa a serenata como situação autoral.'),
  193:('Cien años de soledad','La historia oficial','1985','filme de Luis Puenzo','O filme argentino acompanha uma professora que revisita memórias e silêncios; esta aula usa a passagem do tempo numa situação autoral.'),
  194:('La lengua de las mariposas','Conducta','2014','filme de Ernesto Daranas','O filme cubano acompanha um estudante e seu professor; esta aula usa estudo, esforço e apoio numa situação autoral.'),
  197:('La casa de Bernarda Alba','Arrugas','2011','filme de Ignacio Ferreras','A animação espanhola acompanha amizades e memória na velhice; esta aula usa a letra eñe em uma situação autoral.'),
}

def replace(value,old,new):
    if isinstance(value,dict):
        for k,v in list(value.items()): value[k]=replace(v,old,new)
    elif isinstance(value,list): value[:]=[replace(v,old,new) for v in value]
    elif isinstance(value,str) and value==old: return new
    return value

def main():
    manifest=json.loads((ROOT/'data/manifest.json').read_text(encoding='utf-8'))
    for rel in manifest['es-a2']:
        p=ROOT/'data'/rel; data=json.loads(p.read_text(encoding='utf-8')); dirty=False
        for e in data:
            if e.get('n') not in changes: continue
            old,new,year,kind,desc=changes[e['n']]
            replace(e,old,new)
            e['a'].update({'k':kind,'w':new,'y':year,'d':desc})
            dirty=True
        if dirty: p.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
    print('referências corrigidas')

if __name__=='__main__': main()
