def p(g):
    a=[(y,x) for y,r in enumerate(g) for x,v in enumerate(r) if v==2]
    y0=min(y for y,_ in a);y1=max(y for y,_ in a)
    x0=min(x for _,x in a);x1=max(x for _,x in a)
    o=[[0]*len(g[0])for _ in g]
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v==2:o[y][x]=2
            if v==5:o[max(y0-1,min(y1+1,y))][max(x0-1,min(x1+1,x))]=5
    return o
