def p(g):
    y=min(i for i,r in enumerate(g)if any(r))
    x=min(i for i in range(10)if any(r[i]for r in g))
    return [r[x:x+3]for r in g[y:y+3]]
