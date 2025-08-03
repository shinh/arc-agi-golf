def p(g):
    L=[r[:3] for r in g]
    for i,r in enumerate(g):
        for j in range(3):
            r[4+j]=L[2-j][i]
            r[8+j]=L[2-i][2-j]
    return g
