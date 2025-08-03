def p(g):
    h=len(g);w=len(g[0]);m=w-1
    o=[[8]*w for _ in g]
    for i in range(h):
        t=(h-1-i)%(m*2)
        o[i][t if t<w else 2*m-t]=1
    return o
