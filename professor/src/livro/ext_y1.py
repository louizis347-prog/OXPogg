"""Palavras extras do agente Y1 (C2-L051 a C2-L100); sem pendências: fills = 0."""
from ext import A
def W(id,s):
    A(id,"\n".join("%s;%s;%s;%s"%tuple(x.split("|")) for x in s.strip().splitlines()))
