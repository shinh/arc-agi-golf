def p(g):
    return[[2*(g[y][x]==g[y+4][x]==0)for x in range(4)]for y in range(4)]
