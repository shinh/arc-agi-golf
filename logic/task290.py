def p(g):
    X=[i for i in range(len(g[0])) if any(r[i] for r in g)]
    Y=[i for i,r in enumerate(g) if any(r)]
    a,b=[*{g[y][x] for y in range(Y[0],Y[-1]+1) for x in range(X[0],X[-1]+1) if g[y][x]}]
    return [[b if c==a else a for c in r[X[0]:X[-1]+1]] for r in g[Y[0]:Y[-1]+1]]
