def p(g):
    h=len(g);w=len(g[0])
    o=[r[:] for r in g]
    R={};C={}
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v==8:(R.setdefault(y,[]).append(x),C.setdefault(x,[]).append(y))
    for y,xs in R.items():
        a=min(xs);b=max(xs)
        for x in range(a,b+1):o[y][x]=8
    for x,ys in C.items():
        a=min(ys);b=max(ys)
        for y in range(a,b+1):o[y][x]=8
    return o
