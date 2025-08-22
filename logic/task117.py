def p(g):
    # mirror X
    # reflect across 3x3 bounds
    for v in sum(g,[]):
        if v:
            s={(y,x)for y,r in enumerate(g)for x,c in enumerate(r)if c==v}
            y,x=min(s)
            if{(y+2,x),(y,x+2),(y+2,x+2),(y+1,x+1)}<=s:
                s=y+y+2;t=x+x+2
                for y,r in enumerate(g):
                    for x,c in enumerate(r):
                        if c:g[y][x]=g[s-y][x]=g[y][t-x]=g[s-y][t-x]=c
                return g

