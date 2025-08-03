def p(g):
    c=sum(g[y][x]==g[y][x+1]==g[y+1][x]==g[y+1][x+1]==1 for y in range(8) for x in range(8))
    return [[1]*c+[0]*(5-c)]
