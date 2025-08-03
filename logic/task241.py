def p(g):
    n=len(g)
    for y in range(n):
        for x in range(y):
            g[x][y]=g[y][x];g[y][x]=0
    return g
