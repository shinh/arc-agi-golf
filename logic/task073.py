def p(g):
    # drop third-row 1s to bottom
    g[-1],g[2]=[b>0 or a for a,b in zip(g[-1],g[2])],[0]*5
    return g
