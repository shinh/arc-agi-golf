def p(g):
    for r in g:
        for i,v in enumerate(r):
            if v==1:r[i]=2
    for k in range(1,7):
        if all(g[i]==g[i%k] for i in range(6)):break
    return [g[i%k][:] for i in range(9)]
