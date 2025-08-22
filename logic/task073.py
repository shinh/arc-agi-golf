def p(g):
    # drop third-row 1s to bottom
    for i in 0,1,2,3,4:
        if g[2][i]:g[-1][i],g[2][i]=1,0
    return g
