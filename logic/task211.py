def p(g):
    b=[r[::-1]+r for r in g]
    r=[v[::-1] for v in b[::-1]]
    return r+b+r
