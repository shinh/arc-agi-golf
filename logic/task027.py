def p(g):
    h=len(g);w=len(g[0])
    a={(y,x)for y in range(h)for x in range(w)if g[y][x]==1}
    r={(w-1-x,y)for y,x in a}
    n=lambda s:{(y-min(y for y,_ in s),x-min(x for _,x in s))for y,x in s}
    R=lambda s:{(max(x for _,x in s)-x,y)for y,x in s}
    m=0;sh=a
    for dy in range(-h,h):
        for dx in range(-w,w):
            b={(y+dy,x+dx)for y,x in r}
            if any(y<0 or y>=h or x<0 or x>=w for y,x in b):
                continue
            t=n(a|b)
            if t==R(t):
                k=len(a&b)
                if k>m:m=k;sh=b
    o=[r[:]for r in g]
    for y,x in sh-a:o[y][x]=2
    return o

