def p(g):
    return [[max(r[i],r[8-i])for i in range(4)]for r in g]
