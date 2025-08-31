def p(g):
    # mirror central pattern horizontally
    c=next(i for r in g for i in r if i)
    for _ in'01':
        for r in g:
            if{*r}=={0,c}:m=r.index(c)+15-r[::-1].index(c);csx=m>>1;cex=-~m>>1
        for r in g:
            if{*r[cex:]}-{0,c}:r[cex:]=(r[csx::-1]+[0]*16)[:16-cex]
            r.reverse()
    return g
