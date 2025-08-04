def p(g):
    h=len(g);w=len(g[0]);z=sum(c==0 for r in g for c in r)
    c=[c for r in g for c in r if c][0];k=sum(c==x for r in g for x in r)
    o=[[0]*w*z for _ in range(h*z)]
    for t in range(k):
        by, bx=divmod(t,z)
        for y in range(h):
            for x in range(w):
                o[by*h+y][bx*w+x]=g[y][x]
    return o
