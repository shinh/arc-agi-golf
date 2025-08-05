def p(g):
    parts=[g[i*3:(i+1)*3] for i in range(3)]
    for pce in parts:
        if pce!=[list(r) for r in zip(*pce)]:return pce
