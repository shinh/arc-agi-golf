def p(g):
    return [[3*((g[i][j]==1)|(g[i+5][j]==2)) for j in range(4)]for i in range(4)]
