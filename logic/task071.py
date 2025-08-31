def p(g):
    c=[c for c in sum(g,[])if c][0]
    for o in range(2):
        for r in g:
            if{*r}=={0,c}:
                sx=r.index(c)
                ex=15-r[::-1].index(c)
                csx=sx+ex>>1
                cex=sx+ex+1>>1
        for r in g:
            if{*r[cex:]}-{0,c}:
                r[cex:]=(r[csx::-1]+[0]*99)[:16-cex]
        g=[r[::-1]for r in g]
    return g
