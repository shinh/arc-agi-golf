def p(g):
    # count 2x2 blocks of color 1
    c=sum(a[x]*a[x+1]*b[x]*b[x+1]==1 for a,b in zip(g,g[1:]) for x in range(8))
    return [[1]*c+[0]*(5-c)]
