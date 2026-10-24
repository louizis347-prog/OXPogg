# Elenco, obra e cenas dos episódios antigos, reaproveitados nos episódios refeitos.
import importlib

OLD = {}
for _b in ('ep_086_090', 'ep_091_093', 'ep_094_096', 'ep_097_100', 'ep_101_104', 'ep_105_107', 'ep_108_110', 'ep_116_118', 'ep_119_120'):
    for _e in importlib.import_module('v3.' + _b).EPS:
        OLD[_e['n']] = _e


def N(n):
    o = OLD[n]['v2']
    return dict(names=o['names'], ids=list(o['speakers'].values()), rs=o['stage']['rs'], obra=o['obra'])
