def p(g):
    # mirror X
    # reflect across 3x3 bounds
    for v in sum(g,[]):
        if v:
            s={(y,x)for y,r in enumerate(g)for x,c in enumerate(r)if c==v}
            y,x=min(s)
            if{(y+2,x),(y,x+2),(y+2,x+2),(y+1,x+1)}<=s:
                S=y*2+2;T=x*2+2
                for Y,r in enumerate(g):
                    for X,c in enumerate(r):
                        if c:g[Y][X]=g[S-Y][X]=g[Y][T-X]=g[S-Y][T-X]=c
                return g

