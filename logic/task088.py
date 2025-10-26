def p(g):
    a=sum(g,[])
    i=a.index(next(filter(abs,a)))
    m=len(g[0])
    e=len(a)+~a[::-1].index(a[i])
    return [[r and a[i] for r in r[i%m+1:e%m]] for r in g[i//m+1:e//m]]