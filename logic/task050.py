def p(g):
    for r in g:
        a=[i for i,v in enumerate(r)if v==8]
        if a[1:]:
            for i in range(a[0]+1,a[-1]):
                if r[i]<1:r[i]=3
    h=len(g)
    for x in range(len(g[0])):
        a=[y for y in range(h)if g[y][x]==8]
        if a[1:]:
            for y in range(a[0]+1,a[-1]):
                if g[y][x]<1:g[y][x]=3
    return g
