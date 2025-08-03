def p(g):
    w=len(g[0]);o=[r[:] for r in g]
    for y in range(1,len(g)-1):
        r=g[y]
        if any(c not in (0,5) for c in r):
            a=r[1]+5;b=r[5]+5;c=r[9]+5
            row=[a]*3+[5]+[b]*3+[5]+[c]*3
            o[y-1]=o[y]=o[y+1]=row
    return o
