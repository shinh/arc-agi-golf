def p(g):
    h=w=23
    flat=[v for r in g for v in r]
    c=min(set(flat),key=flat.count)
    ys=[y for y,r in enumerate(g) for x,v in enumerate(r) if v==c]
    xs=[x for y,r in enumerate(g) for x,v in enumerate(r) if v==c]
    t,b=min(ys),max(ys);l,r=min(xs),max(xs)
    dy=(b-t+1)//2;dx=(r-l+1)//2
    for k in range(30):
        T=t-k*dy;L=l-k*dx;B=b+k*dy;R=r+k*dx
        for x in range(max(L,0),min(R,w-1)+1):
            if 0<=T<h:g[T][x]=c
            if 0<=B<h:g[B][x]=c
        for y in range(max(T,0),min(B,h-1)+1):
            if 0<=L<w:g[y][L]=c
            if 0<=R<w:g[y][R]=c
    return g
