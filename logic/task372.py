def p(g):
    return [[max(a,b) for a,b in zip(g[i],g[i+6])] for i in range(5)]
