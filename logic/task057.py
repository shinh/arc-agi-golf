def p(g):
    a=c=8;b=d=-1
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v:a=min(a,y);b=max(b,y);c=min(c,x);d=max(d,x)
    return [r[c:d+1]*2 for r in g[a:b+1]]
