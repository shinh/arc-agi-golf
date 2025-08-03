def p(g):
    h=len(g)
    for x in range(len(g[0])):
        c=[g[y][x]for y in range(h)if g[y][x]]
        c=[0]*(h-len(c))+c
        for y,v in enumerate(c):g[y][x]=v
    return g
