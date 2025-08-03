def p(g):
    return [[3*(r[x+4]!=5 and r[x]!=7) for x in range(3)] for r in g]
