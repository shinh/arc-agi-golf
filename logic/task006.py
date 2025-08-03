def p(g):
    o=create(3,3)
    for y in range(3):
        for x in range(3):
            if g[y][x]==g[y][x+4]==1:
                o[y][x]=2
    return o
