def p(g):
    # color of rarest pixel
    f=sum(g,[]);c=min(f,key=f.count)
    # positions of that color
    s={(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==c};o={*s}
    while s:
        y,x=s.pop();q=[(y,x)];a=b=y;d=e=x
        while q:
            y,x=q.pop()
            a=min(a,y);b=max(b,y);d=min(d,x);e=max(e,x)
            for Y in range(y-2,y+3):
                for X in range(x-2,x+3):
                    p=(Y,X)
                    if p in s:s.remove(p);q+=p,
        for Y in range(a,b+1):g[Y][d:e+1]=[4]*(e-d+1)
    for y,x in o:g[y][x]=c
    return g

