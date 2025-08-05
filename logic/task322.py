def p(g):
    for x in range(3):
        v=0
        for y in range(3):
            c=g[y][x]
            if c:v=c
            else:g[y][x]=v
    return g
