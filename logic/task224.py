def p(g):
    o=[r[:] for r in g]
    P=[(y,x) for y,r in enumerate(g) for x,c in enumerate(r) if c==5]
    ys=[y for y,x in P];xs=[x for y,x in P]
    t=min(ys)+1;b=max(ys);l=min(xs)+1;r=max(xs)
    c=next(g[y][x] for y in range(t,b) for x in range(l,r) if g[y][x] not in(0,5))
    for x in range(l,r):o[t][x]=o[b-1][x]=c
    for y in range(t,b):o[y][l]=o[y][r-1]=c
    return o
