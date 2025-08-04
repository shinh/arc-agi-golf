def p(g):
    c=min({v for r in g for v in r},key=lambda v:sum(r.count(v)for r in g))
    s={(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==c}
    o=s.copy();u=set()
    while s:
        q=[s.pop()];t=set(q)
        while q:
            y,x=q.pop()
            for Y in range(y-2,y+3):
                for X in range(x-2,x+3):
                    p=(Y,X)
                    if p in s:s.remove(p);q.append(p);t.add(p)
        ys,xs=zip(*t)
        u|={(y,x)for y in range(min(ys),max(ys)+1)for x in range(min(xs),max(xs)+1)}
    for y,x in u:g[y][x]=4
    for y,x in o:g[y][x]=c
    return g
