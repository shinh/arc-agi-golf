def p(g):
    # find the anchor pattern then extend its columns downward
    s={0,6,8,9,11,12,16,17,18,24}
    for pc in range(10):
        P={(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==pc}
        if P:
            my,mx=max(P)
            if {(my-y)*7+mx-x for y,x in P}==s:break
    for dx in range(7):
        x=mx-dx
        sy=my+[-1,0,0,1][abs(3-dx)]
        for y in range(sy,20):
            c=g[y][x]
            if c:
                for y in range(sy,20):g[y][x]=c
    return g
