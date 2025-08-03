def p(g):
    for i,v in enumerate(g[2]):
        if v:
            g[2][i]=0
            g[-1][i]=1
    return g
