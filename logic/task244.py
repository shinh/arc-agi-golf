def p(g):
    n=len(g)
    k=sum(all(c==r[0] for c in r) for r in g)+1
    s=(n+1)//k
    o=[[g[i*s][j*s] for j in range(k)] for i in range(k)]
    return [r[::-1] for r in o]
