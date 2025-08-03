def p(g):
    a=g[0][0];h=sum(a not in r for r in g)+1;w=sum(a not in c for c in zip(*g))+1;return [[a]*w for _ in range(h)]
