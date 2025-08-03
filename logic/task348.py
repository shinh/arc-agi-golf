def p(g):
    h=len(g);w=len(g[0]);o=[r[:]for r in g];c=b=0
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v==7:c=x;b=y
    for y in range(b,-1,-1):
        d=b-y
        for e in range(d+1):
            v=7+e%2
            x=c+e
            if x<w:o[y][x]=v
            x=c-e
            if x>=0:o[y][x]=v
    return o
