def p(g):# extend colors right/down
    c=0
    for r in g:
        d=0
        for x,v in enumerate(r):
            d=d or v
            r[x]=d or r[x]
        r[-1]=c=d or c
    return g

