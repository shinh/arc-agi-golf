def p(g):
    # mirror pattern and overlay symmetrically
    a={(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==1}
    r={(9-x,y)for y,x in a}
    m=-1
    for dy in range(-9,10):
        b={(y+dy,x)for y,x in r}
        if all(-1<y<10 for y,_ in b)and(k:=len(a&b))>m:m=k;sh=b
    for y,x in sh-a:g[y][x]=2
    return g

