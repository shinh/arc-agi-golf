def p(g):
    s={0,6,8,9,11,12,16,17,18,24}
    for pc in range(10):
        P={(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==pc}
        if P:
            my,mx=map(max,zip(*P))
            if {(my-y)*7+mx-x for y,x in P}==s:break
    for dx in range(7):
        x=mx-dx
        z=abs(3-dx)
        sy=my+[-1,0,0,1][z]
        for y in range(sy,20):
            c=g[y][x]
            if c:
                for y in range(sy,20):
                    g[y][x]=c
    return g
