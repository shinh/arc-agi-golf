def p(g):
    t=next(i for i,r in enumerate(g) if any(r))
    a=g[t:len(g)-next(i for i,r in enumerate(g[::-1]) if any(r))]
    return [a[(i-t)%len(a)] for i in range(len(g))]
