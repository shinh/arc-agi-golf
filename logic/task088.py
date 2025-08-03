def p(g):
    d={}
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v:d.setdefault(v,[]).append((y,x))
    k=[c for c,s in d.items() if len(s)==4][0]
    s=d[k];ys,xs=zip(*s)
    a,b=min(ys)+1,max(ys)
    c,d=min(xs)+1,max(xs)
    return [[k*(g[y][x]>0)for x in range(c,d)]for y in range(a,b)]
