"""Remove opções de molde com 1 elemento (sem tradução) em arquivos ep_*.py."""
import re, sys
for f in sys.argv[1:]:
    s = open(f).read()
    def fix(m):
        t = m.group(0)
        t = re.sub(r",\s*\['[^'\]]*'\](?=\s*[\],])", '', t)
        t = re.sub(r"\[\['[^'\]]*'\],\s*", '[', t)
        return t
    s2 = re.sub(r"mold=\[.*?\n    speak=", fix, s, flags=re.S)
    open(f, 'w').write(s2)
