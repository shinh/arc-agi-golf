def p(g):
    # positions of the red
    s={(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==2};o={*s}
    # fill bounding boxes of clusters
    while s:
        q=[s.pop()]
        for y,x in q:
            for Y in range(y-2,y+3):
                for X in range(x-2,x+3):
                    p=(Y,X)
                    if p in s:s-={p};q+=p,
        A,B=zip(*q);a=min(A);b=max(A)+1;d=min(B);e=max(B)+1
        for Y in range(a,b):g[Y][d:e]=[4]*(e-d)
    for y,x in o:g[y][x]=2
    return g

