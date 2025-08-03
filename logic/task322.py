def p(g):
    for x in range(len(g[0])):
        v=0
        for y in range(len(g)):
            c=g[y][x]
            if c:v=c
            else:g[y][x]=v
    return g
