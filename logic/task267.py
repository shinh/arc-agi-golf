def p(g):
    b=g[-1][0];g[-1][0]=0
    a={c for r in g for c in r if c and c!=b}.pop()
    for r in g:
        for i,c in enumerate(r):
            if c==a:r[i]=b
    return g
