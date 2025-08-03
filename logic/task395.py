def p(g):
    return [[2*(g[y][x]==g[y+3][x]==0) for x in range(3)] for y in range(3)]
