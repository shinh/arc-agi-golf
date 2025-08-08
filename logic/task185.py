def p(g):
    sx=sy=99
    ex=ey=-1
    for y in range(len(g)):
        for x in range(len(g[0])):
            if g[y][x]not in g[0]:
                sx=min(sx,x)
                sy=min(sy,y)
                ex=max(ex,x)
                ey=max(ey,y)
    l=(ey-sy)//3
    o=[]
    for y in(0,1,2):
        r=[]
        for x in(0,1,2):
            c=g[sy+l*y][sx+l*x]
            q=0
            if c not in g[0]:
                if c==g[sy+l*y+l][sx+l*x]==g[sy+l*y][sx+l*x+l]==g[sy+l*y+l][sx+l*x+l]:
                    q=c
            r.append(q)
        o.append(r)
    return o
