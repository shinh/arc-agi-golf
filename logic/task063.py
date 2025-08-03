def p(g):
    h=len(g);w=len(g[0]);a=[r[:] for r in g]
    for r,s in zip(g,a):
        if s[0] and s[-1] and sum(s[1:-1])==0:r[1:-1]=[3]*(w-2)
    for x in range(w):
        if a[0][x] and a[-1][x] and sum(a[y][x] for y in range(1,h-1))==0:
            for y in range(1,h-1):g[y][x]=3
    return g
