def p(g):
    for v in range(10):
        t=[(y,x)for y,r in enumerate(g)for x,u in enumerate(r)if u==v]
        if len(t)==2:
            (y,x),(Y,X)=t
            dy=(Y>y)-(Y<y);dx=(X>x)-(X<x)
            for i in range(abs(Y-y)+1):g[y+i*dy][x+i*dx]=v
    return g
