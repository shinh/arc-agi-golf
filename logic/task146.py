def p(g):
    for i in range(3):
        pce=g[i*3:i*3+3]
        if pce!=[list(r)for r in zip(*pce)]:return pce
