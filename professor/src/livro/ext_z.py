from ext import A
def W(id,s):
    A(id,"\n".join('%s;%s;%s;%s'%tuple(x.split('|')) for x in s.strip().splitlines()))
W('C2-L106','oratorical cadence|cadência oratória|Oratorical cadence.|Cadência oratória.\nkeynote rhythm|ritmo de discurso principal|Keynote rhythm.|Ritmo de discurso principal.\nrhetorical pause|pausa retórica|Rhetorical pause.|Pausa retórica.\ncrowd response|reação da plateia|Crowd response.|Reação da plateia.')
W('C2-L152','ethical doctrine|doutrina ética|Ethical doctrine.|Doutrina ética.\nmoral axiom|axioma moral|Moral axiom.|Axioma moral.')
W('C2-L153','rhetorical nuance|nuance retórica|Rhetorical nuance.|Nuance retórica.\nverb connotation|conotação do verbo|Verb connotation.|Conotação do verbo.')
W('C2-L159','metaphysical claim|afirmação metafísica|Metaphysical claim.|Afirmação metafísica.\ndialectical method|método dialético|Dialectical method.|Método dialético.\nontological question|questão ontológica|Ontological question.|Questão ontológica.\nepistemic doubt|dúvida epistêmica|Epistemic doubt.|Dúvida epistêmica.')
W('C2-L168','moral duty clause|cláusula de dever moral|Moral duty clause.|Cláusula de dever moral.')
