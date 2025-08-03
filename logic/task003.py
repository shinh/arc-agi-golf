def p(g):
    for r in g:
        for i,v in enumerate(r):
            if v==1:r[i]=2
    h=len(g)
    for k in range(1,h+1):
        if all(g[i]==g[i%k] for i in range(h)):break
    return [g[i%k][:] for i in range(9)]
