def p(g):
    h=len(g);w=len(g[0]);I=[r[:] for r in g]
    for y,r in enumerate(I):
        xs=[x for x,v in enumerate(r) if v]
        if len(xs)>1:
            a=xs[0];R=r[a:xs[-1]+1];Y=y;break
    n=len(R)
    for x in range(w):g[Y][x]=R[(x-a)%n]
    for x in range(w):
        ys=[y for y in range(h) if I[y][x]]
        if len(ys)>1:
            c=ys[0];C=[I[y][x] for y in range(c,ys[-1]+1)];X=x;break
    m=len(C)
    for y in range(h):g[y][X]=C[(y-c)%m]
    return g
