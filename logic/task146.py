def p(g,i=0):
    pce=g[i:i+3]
    return pce==[[*r]for r in zip(*pce)]and p(g,i+3)or pce
