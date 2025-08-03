def p(g):
    w=1-len(g[0])%2
    for r in g:
        for x in range(len(r)):
            if r[x]==5 and x%2==w:r[x]=3
    return g
