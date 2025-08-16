def p(g):
    # mirror pattern and overlay symmetrically
    a={(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==1}
    r={(9-x,y)for y,x in a}
    n=lambda s:(Y:=min(y for y,_ in s),X:=min(x for _,x in s))and{(y-Y,x-X)for y,x in s}
    R=lambda s:(X:=max(x for _,x in s))and{(X-x,y)for y,x in s}
    m=0;sh=a
    for dy in range(-10,10):
        for dx in range(-10,10):
            b={(y+dy,x+dx)for y,x in r}
            if all(-1<y<10 and-1<x<10 for y,x in b)and(t:=n(a|b))==R(t)and(k:=len(a&b))>m:m=k;sh=b
    for y,x in sh-a:g[y][x]=2
    return g

